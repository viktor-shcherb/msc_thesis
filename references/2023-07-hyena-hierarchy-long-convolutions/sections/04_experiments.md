# Experiments [p. 9-12]

## Shrinking the gap on in-context learning

[p. 9-10]

The authors begin by empirically motivating the Hyena design, including the choice of long convolution parametrization. They consider the suite of tasks described in Table 4.1. The evaluation is grounded in recent work on mechanistic interpretability of Transformers (Elhage et al., 2021; Power et al., 2022; Olsson et al., 2022; Zhang et al., 2022). Associative recall, in particular, has been successfully used to guide the design of H3 (Dao et al., 2022c). The authors extend the suite of tasks from these works and include benchmarking more challenging versions of each task. For example, solving associative recall with a vocabulary size of only 10 reveals whether a model is structurally capable of performing recall. Testing on much longer sequences and larger vocabularies reveals additional gaps in performance that are otherwise hidden. [p. 9]

**Table 4.1:** A selection of our *mechanistic design* benchmarks. [p. 9]

| Task | Prompt | Target |
|---|---|---|
| Associative Recall | a, 1, b, e, 3, f, b | e |
| Majority | a, g, g, g, e, f, g | g |
| Counting | a, b, b, b, a, c, b | 4 |
| ICL of Functions | $x_0, f(x_0), \ldots x_n$ | $f(x_n)$ |
| Arithmetic | 1, 3, 5, +, 6, 8, 3 | 8, 1, 8 |

**How to parametrize long convolutions.** The authors compare the performance of the following long convolution parametrizations for $S^1$ and $S^2$ in an order 2 Hyena: [p. 9]

- **Conv1d:** Explicit convolutions (regular convolution layers with fixed filter size).
- **FNO:** Filters parametrized explicitly in the frequency-domain (Li et al., 2020).
- **H3:** Implicit parametrization using state-space models (SSMs), in particular the standard S4 (Gu et al., 2021).
- **TransferFunc:** Implicit parametrization via transfer functions, a classical system-theoretic generalization of SSMs (Footnote 8: Transfer functions roughly correspond to a frequency-domain representation of SSMs).
- **CKConv:** Implicit parametrization using FFNs (Romero et al., 2021b).
- **Hyena:** Combination of implicit parametrizations via FFNs (with exponential decay modulation as shown in Figure 3.1), and short explicit filters.

All models have the same width and 2 layers. Figure 4.1 shows implicit approaches based on FFNs outperform other long convolutions, with the gap widening on longer sequences and larger vocabulary sizes. A different model is trained on each setting of sequence length and vocabulary size. The ranking is correlated with the ability to decouple sequence length from parameter count (Hyena, CKConv, TransferFunc, H3) and expressivity (Hyena, CKConv). Similar trends are observed on the other tasks. [p. 10]

**Figure 4.1** (p. 9): "Benchmark of long convolution parametrizations in order 2 Hyena operators on associative recall (%). Our results show that implicit parametrizations scale more favorably in vocabulary size (number of possible values of tokens in the input) and length of the sequence."

The figure contains four panels showing Associative Recall accuracy (%) vs. Sequence Length ($2^7$ to $2^{15}$) for Vocabulary Sizes 10, 20, 30, and 40. Six methods are compared: Hyena (star marker), CKConv (diamond), Transfer Function (circle), H3 (cross), Conv1D (triangle), and FNO (star, different color). Key observations: At Vocabulary Size 10, most methods achieve near 100% for shorter sequences, but Conv1D and FNO drop sharply at longer lengths. Hyena maintains high accuracy across all vocabulary sizes and sequence lengths. As vocabulary size increases to 30 and 40, the gap widens: Hyena consistently outperforms, while H3, Conv1D, and FNO degrade substantially. CKConv and TransferFunc also maintain decent performance but trail Hyena at the largest settings.

**Pushing sequence length to the limit.** The authors evaluate associative recall performance on extremely long sequences of length 131k. To the best of their knowledge, these represent the first empirical display of attention-free in-context learning on sequences of this length. The gap between parametrization schemes widens as shown in Appendix A, with Hyena outperforming CKConv by 80 points. [p. 10]

**Comparing operators.** The authors repeat the associative recall experiment, this time benchmarking different 2 layer models rather than changing the convolution parametrization: an order 2 Hyena, GSS (Mehta et al., 2022), H3 (Dao et al., 2022c), AFT-conv (Zhai et al., 2021), RWKV (Peng, 2021), and a standard GPT (Brown et al., 2020) using FlashAttention (Dao et al., 2022b). As shown in Table 4.2, Hyena is the only operator able to solve the task. The results challenge the observation that only Transformers are capable of challenging in-context learning. Rankings of model performance at a fixed sequence length on The Pile are consistent with rankings on aggregate scores on the synthetics (Appendix C). [p. 10]

**Table 4.2:** Test accuracy (%) for associative recall on longer sequences, vocabulary size 30. The symbol **X** is used to mark settings where the model does not fit in memory. [p. 10]

| Sequence length | Hyena | FlashTransformer | Transformer | GSS | H3 | AFT | RWKV |
|---|---|---|---|---|---|---|---|
| 30k | 100.0 | 32.4 | **X** | 5.3 | 8.4 | 2.3 | 12.4 |
| 64k | 100.0 | 26.7 | **X** | 2.1 | 4.3 | 1.2 | 6.5 |
| 131k | 97.2 | **X** | **X** | 0.1 | 0.6 | 0.8 | 2.3 |

**Generality of Hyena operators and filters.** Hyena operators and filters can also be applied successfully beyond language tasks. The authors experiment on sequential CIFAR, where pixels are flattened as a sequence, and use the same operator defined for language. They reach the accuracy of standard S4 (Gu et al., 2021) with same model size (91%). In Section 4.5 and Appendix A, they discuss larger-scale image classification experiments with Hyena. [p. 10]

## Language Modeling

[p. 10-11]

The authors verify the scaling of Hyena on autoregressive language modeling. They evaluate perplexity on WikiText103 (Table 4.3) and The Pile (Table 4.4). On The Pile, they train different models for 5, 10, 15 billion tokens (different runs), adjusting the learning rate scheduler. Hyena is the first attention-free, convolution architecture to match GPT quality with a 20% (Footnote 9: The FLOP reduction consists in the *non-parametric* FLOPs of SelfAttention devoted to attention matrix computation. The ratio of parametric to non-parametric FLOPs (and hence the gains) depend on the ratio of model width $D$ and sequence length $L$ used in training.) reduction in total FLOPs. Preliminary scaling laws are shown in Figure 4.2, collecting the training runs at 5, 10, 15 billion tokens. Each curve represents a different training run. In Appendix A, results on the PG-19 long-range benchmark are provided (Rae et al., 2019). [p. 10]

**Figure 4.2** (p. 11): "Preliminary 'scaling law' of language models on The Pile. Comparison of our approach (red) based on long convolutions and gating (Hyena) and a standard GPT (blue) (Brown et al., 2020). We reach perplexity of GPT with a smaller training FLOP budget."

The figure plots Loss (y-axis, ranging from approximately 2.21 to 2.44) vs. FLOPs (x-axis, ranging from approximately $1.3 \times 10^{19}$ to $4.9 \times 10^{19}$). Two curves are shown: Hyena (red, star markers) and GPT (blue/teal, diamond markers). Both curves decrease as FLOPs increase. Key observation: Hyena achieves roughly the same loss as GPT at each FLOP level, with the Hyena curve slightly below or overlapping GPT at intermediate FLOP values. At the highest FLOP point (~$4.9 \times 10^{19}$), both converge to approximately 2.21-2.22 loss, but Hyena reaches comparable loss levels earlier (at lower FLOPs). Data points correspond to 355M parameter models.

**Table 4.3:** Perplexity on WikiText103 (same tokenizer). * are results from (Dao et al., 2022c). Deeper and thinner models (Hyena-slim) achieve lower perplexity. [p. 11]

| Model | Perplexity |
|---|---|
| Transformer (125M) | 18.6 |
| Hybrid H3 (125M) | 18.5* |
| Performer (125M) | 26.8* |
| Reformer (125M) | 25.6* |
| AFT-conv (125M) | 28.2 |
| Linear Attention (125M) | 25.6* |
| Hyena-3 (125M) | 18.6 |
| Hyena-3-slim (125M) | 18.5 |

**Table 4.4:** Perplexity on The Pile for models trained until a total number of tokens e.g., 5 billion (different runs for each token total). All models use the same tokenizer (GPT2). FLOP count is for the 15 billion token run. [p. 11]

| Model | 5B | 10B | 15B | FLOPs ($10^{19}$) |
|---|---|---|---|---|
| GPT (125M) | 13.3 | 11.9 | 11.2 | 1.88 |
| Hyena-2 (153M) | 13.3 | 11.8 | 11.1 | 1.87 |
| GPT (355M) | 11.4 | 9.8 | 9.1 | 4.77 |
| Hyena-2 (355M) | 11.3 | 9.8 | 9.2 | 3.93 |

## Downstream Evaluation

[p. 10-11]

The authors perform a downstream evaluation on SuperGLUE (Wang et al., 2019) tasks. They compare Hyena (trained for 137 billion tokens) with the best available pre-trained attention-free model, RWKV (Peng, 2021) (trained for 332 billion tokens), and a reference GPTNeo (Black et al., 2021) (trained for 300 billion tokens) of the same size. Tables 4.5 and 4.6 summarize the results. Hyena performs similarly to other models despite having been trained on less than half the number of total tokens. The authors observe Hyena to display characteristic few-shot capabilities of standard Transformers, with some tasks e.g., MultiRC seeing a lift of more than 20% accuracy over zero-shot when the model is provided additional prompts as context. The improvements are more noticeable in generation tasks, where the additional prompts can instruct the model on how it should be responding to the questions. An additional downstream evaluation on the LAMBADA task (Paperno et al., 2016) is reported in Appendix A. [p. 11]

**Table 4.5:** Zero-shot accuracy (%) on SuperGLUE tasks for small models. [p. 11]

| Model | WSC | WIC | RTE | CB | MultiRC | ReCoRD | BoolQ | COPA | Average |
|---|---|---|---|---|---|---|---|---|---|
| GPTNeo (Black et al., 2021) | **27.9** | 50.0 | 45.1 | **41.1** | 0.0 | **61.7** | **62.2** | 62.0 | **43.8** |
| RWKV (Peng, 2021) | 13.4 | **52.3** | **46.9** | 25.0 | 0.0 | 58.5 | 59.2 | **66.0** | 40.2 |
| Hyena | 21.2 | 50.5 | 46.6 | 39.3 | **1.1** | 59.4 | 51.8 | **70.0** | 41.5 |

---
[p. 12 continued]

**Table 4.6:** Few-shot (3) accuracy (%) on SuperGLUE tasks for small models. [p. 12]

| Model | WSC | WIC | RTE | CB | MultiRC | ReCoRD | BoolQ | COPA | Average |
|---|---|---|---|---|---|---|---|---|---|
| GPTNeo (Black et al., 2021) | 38.5 | **50.0** | **53.8** | **42.9** | **22.4** | **61.4** | **61.0** | 63.0 | **49.1** |
| RWKV (Peng, 2021) | 32.7 | 49.4 | 47.2 | 37.5 | 0.0 | 58.3 | 55.0 | **64.0** | 43.0 |
| Hyena | **39.4** | **50.1** | 47.6 | **46.4** | **26.7** | 58.1 | **56.0** | **70.0** | **49.3** |

## Benchmarking

[p. 12]

The authors benchmark runtime of an order 2 Hyena operator compared to attention and FlashAttention layers (Dao et al., 2022b). Hyena uses a fused CUDA kernel to perform FFTConv (Dao et al., 2022c). They set batch size to 64 and measure runtime (in milliseconds). Results are provided in Figure 4.3. Hyena speedups reach 100x at sequence length 64K. Crossover points for Hyena and attention is at length 2048, and for Hyena and FlashAttention is between 4096 and 8196. Despite the absolute reduction in FLOPs, speedups are achieved only on longer sequences when the gap grows sufficiently large. This occurs because hardware utilization of Hyena is lower than FlashAttention. The authors expect the gap between theoretical maximum speedup to shrink with improved implementations of FFTConv and specialized hardware. [p. 12]

**Figure 4.3** (p. 12): "Benchmarking runtime of Hyena, Attention and FlashAttention with varying sequence lengths. Batch size is set to 64. The figure on the right is an inset showing a zoomed-in portion of the figure on the left."

The figure has two panels. The left panel plots Runtime (ms) (y-axis, 0 to over 100) vs. Sequence Length (x-axis, log scale from $10^3$ to $10^5$). Three lines are shown: Hyena (solid green), Attention (solid blue), and FlashAttention (dashed red). Attention runtime grows steeply (quadratically), exceeding 100 ms before $10^5$. FlashAttention grows more slowly but still super-linearly. Hyena remains nearly flat and far below both attention variants across the full range. The right panel is a zoomed inset (Sequence Length from $10^3$ to roughly $10^{3.8}$, Runtime 0 to 6 ms) showing the crossover region. At short sequence lengths (~$10^3$), Hyena, Attention, and FlashAttention have comparable runtimes (all under 2 ms). Hyena crosses below Attention at approximately length 2048 and below FlashAttention between lengths 4096 and 8196.

## Large-Scale Image Classification

[p. 12]

The authors demonstrate the potential of Hyena as a general deep learning operator by applying it to image classification. On ImageNet, they drop-in replace attention layers in the *Vision Transformer* (ViT) (Dosovitskiy et al., 2020) with the Hyena operator (without changes from its language counterpart) and match performance with ViT. They also show that using smaller image patches boosts performance in both attention and Hyena. Since this results in longer sequence lengths, they expect Hyena to outperform in speed as patches get more fine-grained approaching pixel-level. On CIFAR-2D, they test a 2D version of Hyena long convolution filters in a standard convolutional architecture, which improves on the 2D long convolutional model S4ND (Nguyen et al., 2022) in accuracy with a 8% speedup and 25% fewer parameters. See Appendix A.4 for additional vision architectures and training procedure details. [p. 12]

**Table 4.7:** Image classification top-1 accuracy. [p. 12]

| Model | Patch Size | Seq Len | Dataset | Acc (%) |
|---|---|---|---|---|
| ViT (87M) | 16x16 | 196 | ImageNet-1k | 78.5 |
| Hyena-ViT (88M) | 16x16 | 196 | ImageNet-1k | 78.5 |
| ViT (87M) | 8x8 | 1024 | ImageNet-1k | 80.0 |
| Hyena-ViT (88M) | 8x8 | 1024 | ImageNet-1k | 79.8 |
| S4ND-ISO (268k) | - | - | CIFAR-10 | 89.9 |
| Hyena-ISO (202k) | - | - | CIFAR-10 | 91.2 |
