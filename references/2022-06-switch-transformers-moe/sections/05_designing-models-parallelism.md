# 5. Designing Models with Data, Model, and Expert-Parallelism [p. 18-21]

[p. 18-19]

Arbitrarily increasing the number of experts is subject to diminishing returns (Figure 4). Here the authors describe *complementary* scaling strategies. The common way to scale a Transformer is to increase dimensions in tandem, like d_model or d_ff. This increases both the parameters and computation performed and is ultimately limited by the memory per accelerator. Once it exceeds the size of the accelerator's memory, single program multiple data (SPMD) model-parallelism can be employed. This section studies the trade-offs of combining data, model, and expert-parallelism.

## Reviewing the Feed-Forward Network (FFN) Layer [p. 19-20]

[p. 19-20]

The FFN layer is used as an example of how data, model and expert-parallelism works in Mesh TensorFlow (Shazeer et al., 2018). Assume B tokens in the batch, each of dimension d_model. Both the input (x) and output (y) of the FFN are of size [B, d_model] and the intermediate (h) is of size [B, d_ff] where d_ff is typically several times larger than d_model. In the FFN, the intermediate is h = xW_in and then the output of the layer is y = ReLU(h)W_out. Thus W_in and W_out are applied independently to each token and have sizes [d_model, d_ff] and [d_ff, d_model].

Two aspects of partitioning are described: how the *weights* and *batches of data* divide over cores, depicted in Figure 9. All cores available are denoted as N which Mesh Tensorflow may then remap into a logical multidimensional mesh of processors. A two-dimensional logical mesh is created, with one dimension representing the number of ways for data-parallel sharding (n) and the other, the model-parallel sharding (m). The total cores must equal the ways to shard across both data and model-parallelism, e.g. N = n x m. To shard the layer across cores, the tensors containing that batch of B tokens are sharded across n data-parallel cores, so each core contains B/n tokens. Tensors and variables with d_ff are then sharded across m model-parallel cores. For the variants with experts-layers, E experts are considered, each of which can process up to C tokens.

**Notation table** (p. 20):

| Term | Description |
|---|---|
| B | Number of tokens in the batch. |
| N | Number of total cores. |
| n | Number of ways for data-parallelism sharding. |
| m | Number of ways for model-parallelism sharding. |
| E | Number of experts in Switch layers. |
| C | Expert capacity, the batch size of each expert. |

## 5.1 Data Parallelism [p. 20]

[p. 20]

When training data parallel models, which is the standard for distributed training, then all cores are allocated to the data-parallel dimension or n = N, m = 1. This has the advantage that no communication is needed until the entire forward and backward pass is finished and the gradients need to be then aggregated across all cores. This corresponds to the left-most column of Figure 9.

## 5.2 Model Parallelism [p. 20]

[p. 20]

A scenario is considered where all cores are allocated exclusively to the model-parallel dimension and so n = 1, m = N. Now all cores must keep the full B tokens and each core will contain a unique slice of the weights. For each forward and backward pass, a communication cost is now incurred. Each core sends a tensor of [B, d_model] to compute the second matrix multiplication ReLU(h)W_out because the d_ff dimension is partitioned and must be summed over. As a general rule, whenever a dimension that is partitioned across cores must be summed, then an all-reduce operation is added for both the forward and backward pass. This contrasts with pure data parallelism where an all-reduce only occurs at the end of the entire forward and backward pass.

## 5.3 Model and Data Parallelism [p. 21]

[p. 21]

It is common to mix both model and data parallelism for large scale models, which was done in the largest T5 models (Raffel et al., 2019; Xue et al., 2020) and in GPT-3 (Brown et al., 2020). With a total of N = n x m cores, now each core will be responsible for B/n tokens and d_ff/m of both the weights and intermediate activation. In the forward and backward pass each core communicates a tensor of size [B/n, d_model] in an all-reduce operation.

**Figure 9** (p. 21): "Data and weight partitioning strategies. Each 4x4 dotted-line grid represents 16 cores and the shaded squares are the data contained on that core (either model weights or batch of tokens). We illustrate both how the model weights and the data tensors are split for each strategy. **First Row:** illustration of how *model weights* are split across the cores. Shapes of different sizes in this row represent larger weight matrices in the Feed Forward Network (FFN) layers (e.g larger d_ff sizes). Each color of the shaded squares identifies a unique weight matrix. The number of parameters *per core* is fixed, but larger weight matrices will apply more computation to each token. **Second Row:** illustration of how the *data batch* is split across cores. Each core holds the same number of tokens which maintains a fixed memory usage across all strategies. The partitioning strategies have different properties of allowing each core to either have the same tokens or different tokens across cores, which is what the different colors symbolize."

- The figure shows five parallelism strategies side by side: Data Parallelism, Model Parallelism, Model and Data Parallelism, Expert and Data Parallelism, and Expert, Model and Data Parallelism. Each strategy is illustrated with two 4x4 grids (16 cores): the top row shows how model weights are distributed (same-colored small squares = same weights, different colors = different weight slices, larger squares = larger d_ff), and the bottom row shows how the data batch is distributed (same-colored squares = same tokens, different colors = different tokens). In Data Parallelism, all cores hold the same (small) weights but different data. In Model Parallelism, cores hold different weight slices but the same data. Model and Data Parallelism combines both. Expert and Data Parallelism assigns unique expert weights per core with different data. Expert, Model and Data Parallelism combines all three dimensions.

---
[p. 22 continued]

## 5.4 Expert and Data Parallelism [p. 22]

[p. 22]

Next the partitioning strategy for expert and data parallelism is described. Switch Transformers will allocate all of their cores to the data partitioning dimension n, which will also correspond to the number of experts in the model. For each token per core a router locally computes assignments to the experts. The output is a binary matrix of size [n, B/n, E, C] which is partitioned across the first dimension and determines expert assignment. This binary matrix is then used to do a gather via matrix multiplication with the input tensor of [n, B/n, d_model].

$$\text{einsum}([n, B/n, d_{model}], [n, B/n, E, C], \text{dimension} = [B/n]) \quad (7)$$

Equation 7 computes the einsum that produces the final tensor of shape [n, E, C, d_model], which is sharded across the first dimension.

Because each core has its own expert, an all-to-all communication of size [E, C, d_model] is performed to now shard the E dimension instead of the n-dimension. There are additional communication costs of bfloat16 tensors of size E x C x d_model in the forward pass to analogously receive the tokens from each expert located on different cores. See Appendix F for a detailed analysis of the expert partitioning code.

## 5.5 Expert, Model and Data Parallelism [p. 22]

[p. 22]

In the design of the best model, the authors seek to balance the FLOPS per token and the parameter count. When scaling the number of experts, the number of parameters increases, but the FLOPs per token do not change. In order to increase FLOPs, the d_ff dimension must also be increased (which also increases parameters, but at a slower rate). This presents a trade-off: as d_ff increases, memory per core will be exhausted, which then necessitates increasing m. But since there is a fixed number of cores N, and N = n x m, increasing m requires decreasing n, which forces use of a smaller batch-size (in order to hold tokens per core constant).

When combining both model and expert-parallelism, there will be all-to-all communication costs from routing the tokens to the correct experts along with the internal all-reduce communications from the model parallelism. Balancing the FLOPS, communication costs and memory per core becomes quite complex when combining all three methods where the best mapping is empirically determined. See further analysis in section 5.6 for how the number of experts affects the downstream performance as well.

## 5.6 Towards Trillion Parameter Models [p. 22-24]

[p. 22-23]

Combining expert, model and data parallelism, two large Switch Transformer models are designed, one with 395 billion and 1.6 trillion parameters, respectively. The authors study how these models perform on both upstream pre-training as language models and their downstream fine-tuning performance. The parameters, FLOPs per sequence and hyper-parameters of the two different models are listed in Table 9. Standard hyper-parameters of the Transformer, including d_model, d_ff, d_kv, number of heads and number of layers are described, as well as a less common feature, FFN_GEGLU, which refers to a variation of the FFN layer where the expansion matrix is substituted with two sets of weights which are non-linearly combined (Shazeer, 2020).

The Switch-C model is designed using only expert-parallelism, and no model-parallelism, as described earlier in Section 5.4. As a result, the hyper-parameters controlling the width, depth, number of heads, and so on, are all much smaller than the T5-XXL model. In contrast, the Switch-XXL is FLOP-matched to the T5-XXL model, which allows for larger dimensions of the hyper-parameters, but at the expense of additional communication costs induced by model-parallelism (see Section 5.5 for more details).

**Table 9** (p. 23): "Switch model design and pre-training performance. We compare the hyper-parameters and pre-training performance of the T5 models to our Switch Transformer variants. The last two columns record the pre-training model quality on the C4 data set after 250k and 500k steps, respectively. We observe that the Switch-C Transformer variant is 4x faster to a fixed perplexity (with the same compute budget) than the T5-XXL model, with the gap increasing as training progresses."

*Part 1: Architecture hyper-parameters*

| Model | Parameters | FLOPs/seq | d_model | FFN_GEGLU | d_ff | d_kv | Num. Heads |
|---|---|---|---|---|---|---|---|
| T5-Base | 0.2B | 124B | 768 | checkmark | 2048 | 64 | 12 |
| T5-Large | 0.7B | 425B | 1024 | checkmark | 2816 | 64 | 16 |
| T5-XXL | 11B | 6.3T | 4096 | checkmark | 10240 | 64 | 64 |
| Switch-Base | 7B | 124B | 768 | checkmark | 2048 | 64 | 12 |
| Switch-Large | 26B | 425B | 1024 | checkmark | 2816 | 64 | 16 |
| Switch-XXL | 395B | 6.3T | 4096 | checkmark | 10240 | 64 | 64 |
| Switch-C | 1571B | 890B | 2080 | | 6144 | 64 | 32 |

*Part 2: Expert configuration and pre-training quality*

| Model | Expert Freq. | Num. Layers | Num Experts | Neg. Log Perp. @250k | Neg. Log Perp. @ 500k |
|---|---|---|---|---|---|
| T5-Base | -- | 12 | -- | -1.599 | -1.556 |
| T5-Large | -- | 24 | -- | -1.402 | -1.350 |
| T5-XXL | -- | 24 | -- | -1.147 | -1.095 |
| Switch-Base | 1/2 | 12 | 128 | -1.370 | -1.306 |
| Switch-Large | 1/2 | 24 | 128 | -1.248 | -1.177 |
| Switch-XXL | 1/2 | 24 | 64 | **-1.086** | **-1.008** |
| Switch-C | 1 | 15 | 2048 | -1.096 | -1.043 |

[p. 23]

**Sample efficiency versus T5-XXL.** In the final two columns of Table 9, the negative log perplexity on the C4 corpus after 250k and 500k steps is recorded. After 250k steps, both Switch Transformer variants improve over the T5-XXL version's negative log perplexity by over 0.061.^{10} To contextualize the significance of a gap of 0.061, the T5-XXL model had to train for an *additional* 250k steps to increase 0.052. The gap continues to increase with additional training, with the Switch-XXL model out-performing the T5-XXL by 0.087 by 500k steps.

10. This reported quality difference is a lower bound, and may actually be larger. The T5-XXL was pre-trained on an easier C4 data set which included duplicated, and thus easily copied, snippets within examples. [p. 23, footnote 10]

**Training instability.** However, as described in the introduction, large sparse models can be unstable, and as the scale increases, some sporadic issues are encountered. The larger Switch-C model, with 1.6T parameters and 2048 experts, exhibits no training instability at all. Instead, the Switch XXL version, with nearly 10x larger FLOPs per sequence, is sometimes unstable. As a result, though this is the better model on a step-basis, the authors do not pre-train for a full 1M steps, in-line with the final reported results of T5 (Raffel et al., 2019).

[p. 24]

**Reasoning fine-tuning performance.** As a preliminary assessment of model quality, a Switch-XXL model partially pre-trained on 503B tokens, or approximately half the text used by the T5-XXL model, is used. Using this checkpoint, multi-task training for efficiency is conducted, where all tasks are learned jointly, rather than individually fine-tuned. SQuAD accuracy on the validation set increases to 89.7 versus state-of-the-art of 91.3. Next, the average SuperGLUE test score is recorded at 87.5 versus the T5 version obtaining a score of 89.3 compared to the state-of-the-art of 90.0 (Wang et al., 2019). On ANLI (Nie et al., 2019), Switch XXL improves over the prior state-of-the-art to get a 65.7 accuracy versus the prior best of 49.4 (Yang et al., 2020). The authors note that while the Switch-XXL has state-of-the-art Neg. Log Perp. on the upstream pre-training task, its gains have not yet fully translated to SOTA downstream performance. This issue is studied more in Appendix E.

**Knowledge-based fine-tuning performance.** An early examination of the model's knowledge is also conducted with three closed-book knowledge-based tasks: Natural Questions, WebQuestions and TriviaQA, without additional pre-training using Salient Span Masking (Guu et al., 2020). In all three cases, improvements are observed over the prior state-of-the-art T5-XXL model (without SSM). Natural Questions exact match increases to 34.4 versus the prior best of 32.8, Web Questions increases to 41.0 over 37.2, and TriviaQA increases to 47.5 versus 42.9.

Summing up, despite training on less than half the data of other models, comparable and sometimes state-of-the-art model quality is already found. Currently, the Switch Transformer translates substantial upstream gains better to knowledge-based tasks than reasoning-tasks (see Appendix E). Extracting stronger fine-tuning performance from large expert models is an active research question, and the pre-training perplexity indicates future improvements should be possible.
