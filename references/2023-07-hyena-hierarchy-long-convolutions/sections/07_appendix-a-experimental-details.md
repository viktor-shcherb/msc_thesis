# A Experimental Details [p. 18-21]

[p. 18]

An implementation of Hyena is available online (link provided in paper).

## A.1 Mechanistic Design Synthetic Benchmarks

[p. 18]

The synthetic reasoning benchmarks are inspired by mechanistic interpretability (Elhage et al., 2021), in-context learning (ICL) (Garg et al., 2022), and language model benchmarking (Liang et al., 2022) research. The evaluation revolves around 4 main tasks:

- **Associative recall:** Each string is produced by concatenating key-value tuples from a different random dictionary. This test verifies whether a model is able to extract the right value given a key as prompt, effectively applying a data-controlled shift (delay).
- **Majority voting and counting:** Testing if a model can *densely* activate its data-controlled matrix, i.e., through many non-zero entries (consider the string 'a a a a a a a b $\to$ a').
- **ICL of linear functions:** Verifying whether a model can perform ICL on real-valued inputs. Prompts are generated as $x_1, w^k x_1, \ldots, x_n \to w^k x_n$, where both $x_k$ and $w^k \in R^{n_o}$ are sampled from a normal distribution.
- **Arithmetic:** Basic capability check.

For each task, models are trained using the hyperparameters shown in Table A.1. The authors consider increasing settings of difficulty controlled by sequence length, spanning values 1024, 2048, 4098, 8196, 16392, 32784, 65568, 131136 and vocabulary sizes 10, 20, 30, 40. For ICL of functions, they vary instead the dimension $n_o$. [p. 18]

For associative recall on longer sequences, multiple copies of key-value tuples appear in the prompt. To see this, consider how likely it is to sample multiple copies of a particular key-value pair with a vocabulary size of 40, in order to form a sequence of 100k characters. Models capable of looking further back in the sequence effectively see more data, and can solve challenging versions of the in-context learning task. Increasing the vocabulary size has the effect of increasing the average distance between instances of the same key-value pair in each prompt, highlighting performance gaps between different approaches. [p. 18]

**Table A.1:** Hyperparameter settings for reasoning and in-context learning tasks. [p. 18]

| Parameter | Value |
|---|---|
| Optimizer | AdamW |
| Optimizer momentum | $\beta_1, \beta_2 = 0.9, 0.98$ |
| Base learning rate | 0.0005 |
| Weight decay | 0.1 |
| Dropout | None |
| Batch size | 32 |
| Training epochs | 200 |
| Num samples | 2000 |
| Learning rate schedule | cosine decay |
| Warmup epochs | 10 |
| Warmup schedule | linear |
| Number of layers | 2 |
| Width | 64 |

### Long convolution comparisons

[p. 18-19]

The authors compare different convolution parametrizations, embedding them in an order 2 Hyena operator. All convolutions are applied separately to input channels (referred to as single-input single-output (SISO) in signal processing, or *depthwise* in other machine learning contexts).

- **Conv1d:** Explicit convolutions (regular convolution layers with fixed filter size). A fixed filter size of 64 is used, to match parameters of the other approaches.
- **FNO:** Filters parametrized explicitly in the frequency-domain (Li et al., 2020). Number of modes set to 64.
- **H3:** Implicit parametrization using state-space models (SSMs), in particular the standard S4 (Gu et al., 2021). State dimension set to 64.
- **TransferFunc:** Implicit parametrization via transfer functions, a classical system-theoretic generalization of SSMs. Transfer functions are defined by a ratio of polynomials (the authors parametrize the coefficients, and evaluate the polynomials efficiently via FFTs). Order set to 64.
- **CKConv:** Implicit parametrization using FFNs (Romero et al., 2021b).
- **Hyena:** Combination of implicit parametrizations via FFNs (with exponential decay modulation as shown in Figure 3.1), and short explicit filters.

CKConv and Hyena use the same size of FFNs (width 32 to match in parameters). [p. 19]

In Table A.1, the authors report additional results on the challenging setting of sequence length 131072 and vocabulary size 30. Implicit parametrizations of convolutions outperform explicit parametrizations on associative recall, with CKConv and Hyena greatly improving on the ability to extract the right key, value relations from different inputs. In Appendix C, they discuss how results on their synthetic tasks can be indicative of performance at a larger scale. [p. 19]

**Table A.2:** Test accuracy (%) in associative recall on sequences of length 131072, vocabulary size 30. [p. 19]

| Hyena | CKConv | TransferFunc | H3 | FNO | Conv1d |
|---|---|---|---|---|---|
| 97.2 | 14.3 | 0.5 | 0.6 | 0.3 | 0.5 |

### Operator comparisons

[p. 19]

The authors compare different models on the same associative recall task, using hyperparameters in Table A.1. Hyena uses their filter parametrization with decay windowing for long convolutions, and short explicit convolutions of size 3 after the dense input projections. All other models use defaults from their largest scale experiment, while keeping the size to 2 layers and width 64. [p. 19]

### A note on Transformer performance

[p. 19]

Transformers can solve associative recall tasks with longer sequences, provided the length does not prevent them from fitting in memory, and enough examples are present in the training data. In all experiments, the authors keep the number of samples fixed (2000), a regime where Transformers struggle to find the generalizing solution (see Table A.1). [p. 19]

For shorter sequences (see Appendix C), Transformers solve the task easily even with limited data, comparably to Hyena. [p. 19]

More broadly, these different properties of attention and attention-free token-mixing layers may explain improved performance when they are combined in hybrid architectures (Dao et al., 2022c). The focus on this work has been identifying an architecture capable of performing without attention, which is necessary to tackle domains where long sequences are common. However, when training with shorter sequences (up to 8k), if final downstream performance is the only metric of interest, improved results can be obtained by hybridizing models similarly to H3 (Dao et al., 2022c). [p. 19]

## A.2 Language Modeling

[p. 19-20]

**WikiText103:** The authors train 125M parameter models on WikiText103 and compare perplexity to Transformers, hybrid models such as H3 (Dao et al., 2022c), and other variants of subquadratic attention. All models use the same GPT2 tokenizer with vocabulary size 50257. They test order 3 Hyena with their proposed filter parametrization for two long convolutions, and a shorter explicit convolution on the third. They also consider Hyena (slim) that are 1.5x deeper than Transformers (12 versus 18 layers), with width multiplier of the FFNs set to 2. They find trading-off width for depth to be generally favourable. These modifications are made possible by the reduction in overall FLOPs of Hyena operators compared to self-attention, in particular non-parametric FLOPs which include materialization of the attention matrix, application of softmax, and matrix-value reduction. [p. 19]

**Table A.3:** Hyperparameter settings for The Pile, 125M. [p. 20]

| Parameter | Value |
|---|---|
| Optimizer | AdamW |
| Optimizer momentum | $\beta_1, \beta_2 = 0.9, 0.98$ |
| Peak learning rate | 0.0006 |
| Warmup learning rate init | 0.000001 |
| Learning rate min | 0.00006 |
| Weight decay | 0.1 |
| Dropout | None |
| Batch size | 256 |
| Learning rate schedule | cosine decay |
| Warmup schedule | linear |

**The Pile:** The authors follow the same procedure and train 125M and 355M-sized models on The Pile (Gao et al., 2020). Hyperparameters are reported in Table A.3. Hyperparameters for 355M are the same beyond a reduction in peak learning rate to $4 \cdot 10^{-4}$. For larger models (1.3B), they set a learning rate of $2.2 \cdot 10^{-4}$. [p. 20]

They perform three experiments for each model type and size, and train for 5, 10, 15 billion tokens at a sequence length 2024 and global batch size 256. All models are trained on a single node of 8 A100 80GB GPUs. They use order 2 Hyenas, with the same architectural considerations described above for WikiText103. [p. 20]

In addition to data scaling experiments at 5, 10 and 15 billion tokens, they provide preliminary results for models at the 1.3B parameter scale (10.8 perplexity after 5 billion tokens), and train a 153M model (130 billion tokens), reaching a perplexity of 9.8. The 153M is the same used in their downstream evaluation on SuperGLUE. [p. 20]

Training hyperparameters match those of standard GPT training pipelines, and are thus likely suboptimal for new attention-free architectures such as Hyena. The authors run some preliminary experiments and find that e.g., some modifications to the learning rate schedule, currently involving linear warmup and cosine decay, to improve perplexity at convergence of Hyena models (they recommend slightly lower learning rates for Hyena models compared to GPT of a similar size). Despite these findings, they use standard GPT hyperparameters for both GPT and Hyena. [p. 20]

**PG-19:** The authors also report results of additional training runs on other datasets. They train a Hyena 153M model on the standard PG-19 long-range corpus (Rae et al., 2019), with a context length of 16k tokens, reaching a test perplexity of 14.6 (using the standard GPT2 tokenizer) in 8 epochs. [p. 20]

**Architectures:** Architectural hyperparameters for Hyena are shown in Table A.4. They use sine as an activation function for the FFN of Hyena filters. [p. 20]

**Table A.4:** Hyena architecture hyperparameters. [p. 20]

| Size | depth | width | FFN width | filter FFN width | filter FFN depth | sine freq. |
|---|---|---|---|---|---|---|
| 125M | 12 | 768 | 3072 | 64 | 4 | 14 |
| 125M-slim | 18 | 768 | 1536 | 64 | 4 | 14 |
| 153M | 18 | 864 | 1728 | 64 | 4 | 14 |
| 355M | 36 | 1024 | 2048 | 64 | 4 | 14 |
| 1.3B | 36 | 2048 | 4096 | 64 | 4 | 14 |

### FLOP computation

[p. 20-21]

The number of *floating point operations* (FLOPs) reported in the main text are computed using the same strategy as in (Hoffmann et al., 2022). For GPT, the authors do not use the approximation, opting instead for the more accurate formula based on FLOP counts of individual layers. In the case of Hyena, FLOPs are computed using the same method, except attention layers are replaced by: [p. 20]

i. Projections: order $\times$ d_model $\times$ d_model $\times$ seq_len.

ii. Short conv on projections: order $\times$ d_model $\times$ seq_len $\times$ filter_len (usually 3).

iii. FFTConv: $5 \times (\text{order} - 1) \times \text{d\_model} \times \log(\text{seq\_len}) \times \text{seq\_len}$.

iv. Output: d_model $\times$ d_model $\times$ seq_len.

with a leading factor 2 to account for both additions and multiplications. [p. 21]

## A.3 Downstream Evaluation

[p. 21]

**SuperGLUE:** The authors evaluate models on the SuperGLUE (Wang et al., 2019) with the parsing pipeline of (Arora et al., 2022). For all tasks except WIC, CB and BoolQ, they generate a response using greedy decoding, then check for the gold label. WIC, CB and BoolQ use logit scoring instead of generation. [p. 21]

**Models:** The models considered are the open-source checkpoint of GPTNeo 125M trained for 300B tokens The Pile, and the RWKV-v4 169M checkpoint trained for 332B tokens on The Pile. Hyena is a 153M model trained for 137B tokens on The Pile. [p. 21]

**LAMBADA:** The authors evaluate Hyena on the LAMBADA (Paperno et al., 2016) task. They apply a stop word filter and check whether predictions for all tokens corresponding to the last word agree with the ground truth. The small Hyena model trained on 137B tokens reaches 44.64% accuracy. [p. 21]

## A.4 Image Classification

[p. 21]

**ImageNet:** The authors use ImageNet-1k which consists of 1000 classes and 1.3M images and train from scratch with no outside data on 8 Nvidia A100 GPUs. In their ViT benchmark, they swap the attention layers with the Hyena operator defined in their language experiments, and remove the class token and positional embeddings, similar to S4ND (Nguyen et al., 2022). The parameter count is kept similar at 87M ViT-B (base) vs 88M Hyena-ViT. The training procedure from T2T-ViT (Yuan et al., 2021) is used, including augmentations such as RandAugment (Cubuk et al., 2020), Mixup (Zhang et al., 2017), and AugMix (Hendrycks et al., 2019). See Table A.5 for hyperparameter settings used. [p. 21]

**CIFAR-10:** The authors use CIFAR-10 in sequential and 2D experiments. For sequential, they use the Hyena operator defined in their language tasks and compare with an S4 model (Gu et al., 2021) of the same size by swapping layers in the residual blocks. In 2D, they learn Hyena filters (in both $x$ and $y$ dimensions) that are equal to the size of the input shape, and forgo the gating mechanism from their language experiments. They window (i.e., apply a soft mask spatially to) the Hyena filters with a decay term. The rate of decay varies across channels, ensuring different sizes of the filters at initialization. They compare with another implicit 2D convolution, S4ND (Nguyen et al., 2022), by swapping the model layers with the 2D Hyena filters. The "isometric" model consists of 4 residual blocks of model dimension 128. They use basic image augmentations, 0.1 dropout, 0.03 weight decay and train for 100 epochs using a Nvidia T4 GPU. [p. 21]

**Table A.5:** ViT and ViT-Hyena settings for ImageNet-1k. [p. 22]

| Parameter | Value |
|---|---|
| Image size | $224^2$ |
| Optimizer | AdamW |
| Optimizer momentum | $\beta_1, \beta_2 = 0.9, 0.999$ |
| Weight init | trunc. normal (std=0.02) |
| ViT base learning rate | $1e^{-3}$ |
| Hyena-ViT base learning rate | $2e^{-4}$ |
| ViT weight decay | 0.05 |
| Hyena-ViT weight decay | 0.01 |
| Dropout | None |
| Batch size | 1024 |
| Training epochs | 300 |
| Learning rate schedule | cosine decay |
| Warmup epochs | 10 |
| Warmup schedule | linear |
| RandAugment (Cubuk et al., 2020) | (9, 0.5, layers=2) |
| Mixup (Zhang et al., 2017) | 0.8 |
| Cutmix (Yun et al., 2019) | 1.0 |
| Random erasing (Zhong et al., 2020) | 0.25 |
| Label smoothing (Szegedy et al., 2016) | 0.1 |
| Stochastic depth (Huang et al., 2016) | 0.1 |
| Exp.mov. avg (EMA) (Polyak and Juditsky, 1992) | None |
