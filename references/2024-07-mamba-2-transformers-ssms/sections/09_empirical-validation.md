# 9 Empirical Validation [p. 28–31]

[p. 28] The authors empirically evaluate Mamba-2 on synthetic recall tasks that have been challenging for recurrent models (Section 9.1), and standard language modeling pre-training and downstream evaluations (Section 9.2). They validate that the SSD algorithm is much more efficient than Mamba-1 (Section 9.3) and comparable to optimized attention for moderate sequence lengths. Finally, various design choices in the Mamba-2 architecture are ablated (Section 9.4).

## 9.1 Synthetics: Associative Recall

[p. 28] Synthetic associative recall tasks have been popular for testing the ability of language models to look up information in their context. Broadly, they involve feeding autoregressive models pairs of key-value associations, and then prompting the model to produce the correct completion upon being shown a previously-seen key. The **multi-query associative recall (MQAR)** task is a particular formulation of this task that requires the model to memorize multiple associations (Arora, Eyuboglu, Timalsina, et al. 2024). The original Mamba paper reported results on related synthetic tasks, in particular Selective Copying (Gu and Dao 2023) and Induction Heads (Olsson et al. 2022), which can be seen as easier associative recall tasks. The MQAR task is also closely related to "phonebook look-up" tasks which have been shown to be challenging for recurrent models such as SSMs, due to their finite state capacity (De et al. 2024; Jelassi et al. 2024).

[p. 30] The authors compare on a challenging version of the MQAR setup from (Arora, Eyuboglu, Zhang, et al. 2024), using a harder task, longer sequences, and smaller models. Baselines include standard multi-head softmax attention as well as the Based architecture which combines convolutions, local attention, and a linear attention variant.

Results are shown in Figure 8. While Mamba-1 struggles on this task, Mamba-2 performs well across all settings. Surprisingly, it is significantly better than Mamba-1 even when the state sizes are controlled (N = 16). (The authors are not sure which aspect of the architecture is the predominant factor, which remains a question to explore in future work.) Additionally, this task validates the importance of state size: increasing from N = 16 to N = 64 and N = 256 consistently improves performance on MQAR, as the larger state allows more information (key-value pairs) to be memorized.

**Figure 8** (p. 28): "(**Multi-Query Associative Recall (MQAR)**). Associative recall tasks are challenging for SSMs, which must memorize all relevant information into their recurrent state. The SSD layer combined with improved architecture allows for much larger state sizes in Mamba-2, which performs significantly better than Mamba-1 and even vanilla attention."

The figure shows three panels for Sequence Length: 256, 512, and 1024. Each panel plots Accuracy (y-axis, 0.00 to 1.00) vs. Model dimension (x-axis: 32, 64, 128, 256). Six models are compared:
- **Attention** (blue): Generally achieves high accuracy (~1.0) at larger model dimensions, but drops at smaller dimensions for longer sequences.
- **Based** (orange): Achieves moderate to high accuracy; performance degrades with longer sequences.
- **Mamba (N=16)** (green): Generally struggles, with accuracy often below 0.50 across settings.
- **Mamba-2 (N=16)** (red): Substantially better than Mamba-1 at the same state size; reaches ~0.75-1.0 at larger model dimensions.
- **Mamba-2 (N=64)** (purple): Further improvement, approaching or matching attention performance.
- **Mamba-2 (N=256)** (brown): Best SSM performance, matching or exceeding attention in most settings.

Key trend: increasing state size N from 16 to 64 to 256 consistently improves Mamba-2 performance. Mamba-2 with N=256 matches or exceeds attention in all three sequence length settings.

## 9.2 Language Modeling

[p. 30] Following standard protocols in LLMs, the authors train and evaluate the Mamba-2 architecture on standard autoregressive language modeling against other architectures. They compare both pretraining metrics (perplexity) and zero-shot evaluations. The model sizes (depth and width) follow GPT3 specifications, from 125m to 2.7B. They use the Pile dataset (L. Gao, Biderman, et al. 2020), and follow the training recipe described in Brown et al. (2020). This follows the same setup as reported in Mamba (Gu and Dao 2023); training details are in Appendix D.

### 9.2.1 Scaling Laws

[p. 30] For baselines, the authors compare against both Mamba and its Transformer++ recipe (Gu and Dao 2023), which is based on the PaLM and LLaMA architectures (e.g. rotary embedding, SwiGLU MLP, RMSNorm instead of LayerNorm, no linear bias, and higher learning rates). As Mamba has already demonstrated that it outperforms the standard Transformer architecture (GPT3 architecture) as well as recent subquadratic architectures (H3 (Dao, D. Y. Fu, et al. 2023), Hyena (Poli et al. 2023), RWKV-4 (B. Peng, Alcaide, et al. 2023), RetNet (Y. Sun et al. 2023)), they omit those in the plot for clarity (see Gu and Dao (2023) for comparisons).

Figure 9 shows scaling laws under the standard Chinchilla (Hoffmann et al. 2022) protocol, on models from $\approx 125M$ to $\approx 1.3B$ parameters.

**Figure 9** (p. 29): "(**Scaling Laws.**) Models of size $\approx 125M$ to $\approx 1.3B$ parameters, trained on the Pile. Mamba-2 matches or exceeds the performance of Mamba as well as a strong 'Transformer++' recipe. Compared to our Transformer baseline, Mamba-2 is Pareto dominant on performance (perplexity), theoretical FLOPs, and actual wall-clock time."

The figure plots Perplexity (y-axis, log scale, ranging from approximately $6 \times 10^0$ to $10^1$) vs. FLOPs (x-axis, log scale, ranging from approximately $10^{19}$ to $10^{20}$). Three models are shown:
- **Transformer++** (orange): Highest perplexity at each FLOP budget.
- **Mamba** (purple): Lower perplexity than Transformer++, with several data points from small to large.
- **Mamba-2** (blue): Matches or slightly beats Mamba at each FLOP budget, Pareto-dominating Transformer++.

All three lines show decreasing perplexity with increasing FLOPs, as expected. Mamba-2 is consistently at or below Mamba, which is consistently below Transformer++.

### 9.2.2 Downstream Evaluations

[p. 30] Table 1 shows the performance of Mamba-2 on a range of popular downstream zero-shot evaluation tasks, compared to the most well-known open source models at these sizes, most importantly Pythia (Biderman et al. 2023) which were trained with the same tokenizer, dataset, and training length (300B tokens) as the authors' models.

**Table 1** (p. 29): "(**Zero-shot Evaluations.**) Best results for each size in bold, second best underlined. We compare against open source LMs with various tokenizers, trained for up to 300B tokens. Pile refers to the validation split, comparing only against models trained on the same dataset and tokenizer (GPT-NeoX-20B). For each model size, Mamba outperforms Mamba, and generally matches Pythia at twice the model size. Full results in Table 10."

| Model | Token. | Pile ppl $\downarrow$ | LAMBADA ppl $\downarrow$ | LAMBADA acc $\uparrow$ | HellaSwag acc $\uparrow$ | PIQA acc $\uparrow$ | Arc-E acc $\uparrow$ | Arc-C acc $\uparrow$ | WinoGrande acc $\uparrow$ | OpenbookQA acc $\uparrow$ | Average acc $\uparrow$ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Pythia-1B | NeoX | 7.82 | 7.92 | 56.1 | 47.2 | 70.7 | 57.0 | 27.1 | 53.5 | 31.4 | 49.0 |
| Mamba-790M | NeoX | 7.33 | 6.02 | 62.7 | 55.1 | 72.1 | 61.2 | 29.5 | 56.1 | 34.2 | 53.0 |
| **Mamba-2-780M** | NeoX | 7.26 | **5.86** | 61.7 | 54.9 | **72.0** | **61.0** | **28.5** | **60.2** | **36.2** | **53.5** |
| Hybrid H3-1.3B | GPT2 | — | 11.25 | 49.6 | 52.6 | 71.3 | 59.2 | 28.1 | 56.9 | 34.4 | 50.3 |
| Pythia-1.4B | NeoX | 7.51 | 6.08 | 61.7 | 52.1 | 71.0 | 60.5 | 28.5 | 57.2 | 30.8 | 51.7 |
| RWKV4-1.5B | NeoX | 7.70 | 7.04 | 56.4 | 52.5 | 72.4 | 60.5 | 29.4 | 54.6 | 34.0 | 51.4 |
| Mamba-1.4B | NeoX | 6.80 | 5.04 | 65.0 | 59.1 | 74.2 | 65.5 | 32.8 | **61.5** | 36.4 | 56.4 |
| **Mamba-2-1.3B** | NeoX | **6.66** | **5.02** | **65.7** | **59.9** | **73.2** | **64.3** | **33.3** | 60.9 | **37.8** | **56.4** |
| Hybrid H3-2.7B | GPT2 | — | 7.92 | 55.7 | 59.7 | 73.3 | 65.6 | 32.3 | 61.4 | 33.6 | 54.5 |
| Pythia-2.8B | NeoX | 6.73 | 5.04 | 64.7 | 59.3 | 74.0 | 64.1 | 32.9 | 59.7 | 35.2 | 55.7 |
| RWKV4-3B | NeoX | 7.00 | 5.24 | 63.9 | 59.6 | 73.7 | 67.8 | 33.1 | 59.6 | 37.0 | 56.4 |
| Mamba-2.8B | NeoX | 6.22 | 4.23 | 69.2 | 66.1 | 75.2 | 69.7 | **36.3** | **63.5** | 39.6 | 59.9 |
| **Mamba-2-2.7B** | NeoX | **6.09** | **4.10** | **69.7** | **66.6** | **76.4** | **69.6** | 36.4 | 64.0 | **38.8** | **60.2** |

### 9.2.3 Hybrid Models: Combining SSD Layer with MLP and Attention

[p. 30] Recent and concurrent work (Dao, D. Y. Fu, et al. 2023; De et al. 2024; Glorioso et al. 2024; Lieber et al. 2024) suggests that a hybrid architecture with both SSM layers and attention layers could improve the model quality over that of a Transformer, or a pure SSM (e.g., Mamba) model, especially for in-context learning. The authors explore the different ways that SSD layers can be combined with attention and MLP to understand the benefits of each. Empirically they find that having around 10% of the total layers being attention performs best. Combining with attention and MLP also works better than either pure Transformer++ or Mamba-2.

**SSD and Attention.** The authors find that SSD and attention layers are complementary: by themselves (e.g. in the Mamba-2 architecture vs. Transformer++) their performance (measured by perplexity) is nearly the same, but a mixture of SSD and attention layers outperforms the pure Mamba-2 or Transformer++ architecture. They show some results (Table 2) for the 350M model (48 layers) trained to 7B tokens on the Pile with the GPT-2 tokenizer (same number of parameters, same hyperparameters, same training and validation set). Adding in just a few attention layers already yields notable improvement and strikes the best balance between quality and efficiency. They hypothesize that the SSM layers function well as a general sequence-to-sequence mapping, and attention layers act as a retrieval mechanism to quickly refer to previous tokens in the sequence instead of forcing the model to compress all the context to its memory (SSM states). [p. 30]

**Table 2** (p. 31): "(**Combining SSD and Attention Blocks.**) Perplexity of a 350M model with 48 layers, with different number of attention layers. Having around a 10% ratio of attention layers performs best."

| Num. Attn Blocks | 0 (Mamba-2) | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 9 | 11 | 15 | 24 | Transformer++ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Perplexity $\downarrow$ | 8.60 | 8.38 | 8.32 | 8.29 | 8.29 | 8.28 | **8.26** | 8.27 | 8.28 | 8.30 | 8.34 | 8.50 | 8.68 |

Best perplexity is 8.26 with 6 attention layers out of 48 total (12.5%), consistent with the authors' finding that around 10% attention layers performs best. Pure Mamba-2 (8.60) outperforms pure Transformer++ (8.68).

**Hybrid Models with SSD, MLP, and Attention.** [p. 31] The authors compare different ways that SSD can be combined with the (gated) MLP and attention layers, and evaluate at the 2.7B scale (64 layers), trained to 300B tokens on the Pile (same number of parameters, same hyperparameters, same training and validation set, same data order):

1. Transformer++: 32 attention layers and 32 gated MLP, interleaving.
2. Mamba-2: 64 SSD layers.
3. Mamba-2-MLP: 32 SSD and 32 gated MLP layers, interleaving.
4. Mamba-2-Attention: 58 SSD layers and 6 attention layers (at indices 9, 18, 27, 36, 45, 56)$^6$.
5. Mamba-2-MLP-Attention: 28 SSD layers and 4 attention layers, interleaving with 32 gated MLP layers.

$^6$ In small-scale experiments, the authors find that as long as the attention layers are spaced out, not at the very beginning or at the very end, the model quality does not depend very much on the exact location of the attention layers.

[p. 31] Validation perplexity on the Pile, as well as zero-shot evaluation, is reported in Table 3. In general, the quality of Transformer++ and Mamba-2 models are around the same. Adding just 6 attention layers noticeably improves over the pure Mamba-2 model (and over Transformer++). Adding MLP layers reduces model quality, but can (i) speed up training and inference due to the simplicity and hardware-efficiency of the MLP layer (ii) be easier to up-cycle to MoE models by replacing MLP layers with mixture-of-experts.

**Table 3** (p. 31): "(**Zero-shot Evaluations.**) Best results for each size in bold. We compare different ways SSD, MLP, and attention layers can be combined, evaluated at 2.7B scale trained to 300B tokens on the Pile."

| Model | Token. | Pile ppl $\downarrow$ | LAMBADA ppl $\downarrow$ | LAMBADA acc $\uparrow$ | HellaSwag acc $\uparrow$ | PIQA acc $\uparrow$ | Arc-E acc $\uparrow$ | Arc-C acc $\uparrow$ | WinoGrande acc $\uparrow$ | OpenbookQA acc $\uparrow$ | Average acc $\uparrow$ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Transformer++ | NeoX | 6.13 | 3.99 | 70.3 | 66.4 | 75.2 | 67.7 | 37.8 | 63.9 | 40.4 | 60.2 |
| Mamba-2 | NeoX | 6.09 | 4.10 | 69.7 | 66.6 | **76.4** | 69.6 | 36.4 | 64.0 | 38.8 | 60.2 |
| Mamba-2-MLP | NeoX | 6.13 | 4.18 | 69.3 | 65.0 | 76.4 | 68.1 | 37.0 | 63.1 | 38.2 | 59.6 |
| Mamba-2-Attention | NeoX | **5.95** | **3.85** | **71.1** | **67.8** | 75.8 | **69.9** | **37.8** | **65.3** | 39.0 | **61.0** |
| Mamba-2-MLP-Attention | NeoX | 6.00 | 3.95 | 70.0 | 66.6 | 75.4 | 70.6 | 38.6 | 64.6 | 39.2 | 60.7 |

Mamba-2-Attention (58 SSD + 6 attention layers) achieves the best average accuracy (61.0) and lowest Pile perplexity (5.95), outperforming both pure Transformer++ and pure Mamba-2.

## 9.3 Speed Benchmarks

[p. 31] The authors benchmark the speed of the SSD algorithm against Mamba's scan implementation and FlashAttention-2 (Figure 10). SSD, thanks to its reformulation to use matrix multiplication as a subroutine, can exploit specialized matrix multiplication (matmul) units on GPUs, also known as tensor cores. As a result, it is 2-8x faster than Mamba's fused associative scan, which does not leverage matmul units. Due to its linear scaling in sequence length, SSD is faster than FlashAttention-2 starting at sequence length 2K.

However, the Mamba-2 model as a whole might not be as efficient to train as Transformer at short sequence length (e.g. at 2K), since a Transformer with $L$ layers would have $\frac{L}{2}$ MLP layers and $\frac{L}{2}$ attention layers, while a Mamba-2 model would have $L$ SSD layers for the same number of parameters. Generally the MLP layers are very hardware efficient since they consist of simple matrix multiplication and pointwise linearity. As shown in Section 9.2.3, one can also combine $\frac{L}{2}$ SSD layers and $\frac{L}{2}$ MLP layers to speed up training at short sequence length.

**Figure 10** (p. 29): "(**Efficiency Benchmarks.**) (*Left*) Our SSD is 2 -- 8x faster than a Mamba fused scan for large state expansion ($N = 64$) and faster than FlashAttention-2 for sequence length 2k and above. (*Right*) Sequence length 4K: Increasing state expansion slows down the Mamba optimized scan implementation linearly. SSD can handle much larger state expansion factors without much slowdown."

The figure has two panels:
- **Left panel ("SSD, Scan, Convolution vs Attention time (A100 80GB PCIe)"):** Plots Time in ms (y-axis, log scale, from 0.1 to 1000) vs. Sequence length (x-axis, from 512 to 512K). Lines shown:
  - FlashAttention-2 (red dashed): Quadratic scaling, slowest for long sequences.
  - Convolution (green dashed): Linear scaling but with a high constant.
  - Scan (PyTorch), state dim 64 (orange dashed): Slow implementation.
  - Scan (Mamba), state dim 64 (purple): Faster than PyTorch scan, linear scaling.
  - SSD (ours), state dim 64 (blue): Fastest for most sequence lengths, crosses below FlashAttention-2 around 2K.
- **Right panel ("SSD vs Scan time (A100 80GB PCIe)"):** Plots Time in ms (y-axis, 0 to 7) vs. State dim (x-axis, from 4/16 to 256). Sequence length fixed at 4K. Lines shown:
  - FlashAttention-2 (red dashed): Constant time (independent of state dim), around 1ms.
  - Scan (Mamba) (purple): Time increases linearly with state dimension, from ~1ms at small N to ~6ms at N=256.
  - SSD (ours) (blue): Nearly flat, only slight increase with state dimension, staying around 1ms or below even at N=256.

Key result: SSD's time is nearly independent of state dimension, while Mamba's scan time scales linearly with N. This enables Mamba-2 to use much larger state dimensions without a significant speed penalty.
