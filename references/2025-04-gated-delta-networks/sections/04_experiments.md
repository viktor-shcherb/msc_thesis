# Experiments [p. 6-9]

## Setup [p. 6]

Our experiments encompass a comprehensive comparison of recent state-of-the-art architectures, including pure Transformer-based approaches, and hybrid architectures [p. 6]. We evaluate against the following baselines: RetNet (Sun et al., 2023a), HGRN2 (Qin et al., 2024b), Mamba (Gu & Dao, 2023), Mamba2 (Dao & Gu, 2024b), Samba (Ren et al., 2024), and DeltaNet (Yang et al., 2024b) [p. 6]. For fair comparison, all models are trained under identical conditions with 1.3B parameters on 100B tokens sampled from the FineWeb-Edu dataset (Penedo et al., 2024) [p. 6]. We use the AdamW optimizer with a peak learning rate of 4e-4, weight decay of 0.1, and gradient clipping of 1.0 [p. 6]. The learning rate follows a cosine annealing schedule with a 1B token warm-up period [p. 6]. We use Mamba2's parameterization for α but omit it for brevity⁷ [p. 6, footnote].

and batch size of 0.5M tokens [p. 7]. All models employ the Llama2 tokenizer with a vocabulary size of 32,000 [p. 7]. For sequence modeling, we set the training length to 4K tokens, with Samba and our hybrid models using a sliding window size of 2K [p. 7]. See § B.1 for evaluation settings and § B.2 for ablation studies [p. 7].

**Figure 1** (p. 7): "Visualization of the (hybrid) and block design of Gated DeltaNet models. Gated DeltaNet-H1 and H2 use Gated DeltaNet + SWA and Mamba2 + Gated DeltaNet + SWA patterns, respectively. In the block design, query/key/value paths consist of linear proj., shortconv., SiLU and L2 norm; value path includes linear proj., shortconv. and SiLU; alpha/beta use linear proj.; and output gate applies linear proj. with SiLU."

Description: Architecture diagram showing three model variants (GatedDeltaNet-H1, GatedDeltaNet-H2, and Block Design)
- Key elements: Left shows GatedDeltaNet-H1 stacking MLP, SWA, MLP, and Gated DeltaNet blocks; Middle shows GatedDeltaNet-H2 with SWA, MLP, Gated DeltaNet, MLP, and Mamba2 blocks; Right shows detailed block design with Linear, Norm, Gated Delta Rule components, and paths for q/k/v processing including Conv, Norm, Linear operations
- Notable patterns: The block design shows parallel processing paths with gating mechanisms and normalization layers
- Supports claim: Illustrates the hybrid architecture design combining different attention mechanisms

## Common-sense reasoning [p. 7]

In Table 3, we present the language modeling perplexity and zero-shot accuracy on common-sense reasoning benchmarks for models with 400M and 1.3B parameters [p. 7]. Gated DeltaNet consistently outperforms linear models, including RetNet, HGRN2, Mamba, Mamba2, and DeltaNet, at both scales [p. 7]. As expected, the hybrid variant further enhances performance [p. 7].

**Table 3** (p. 7): Performance comparison on language modeling and zero-shot common-sense reasoning.

| Model | Wiki.<br>ppl ↓ | LMB.<br>ppl ↓ | LMB.<br>acc. ↑ | PIQA<br>↑ | Hella.<br>swag ↑ | Wino.<br>grande ↑ | ARC-e<br>acc. ↑ | ARC-c<br>acc. ↑ | SIQA<br>↑ | BoolQ<br>acc. ↑ | Avg.<br>↑ |
|--------|------------|-----------|------------|-------|----------|-----------|------------|------------|-------|------------|-------|
| *Recurrent models* | | | | | | | | | | | |
| RetNet | 19.08 | 17.27 | 40.52 | 70.07 | 49.16 | 54.14 | 67.34 | 33.78 | 40.78 | 60.39 | 52.02 |
| HGRN2 | 19.10 | 17.69 | 39.54 | 70.45 | 49.53 | 52.80 | 69.40 | 35.32 | 40.83 | 56.66 | 51.79 |
| Mamba | 17.92 | 15.96 | 43.98 | 71.32 | 52.91 | 52.95 | 69.57 | 35.40 | 39.89 | 61.13 | 53.12 |
| Mamba2 | 18.25 | 16.52 | 42.65 | 70.62 | 50.64 | 52.25 | 67.42 | 33.79 | 40.72 | 60.43 | 52.69 |
| DeltaNet | 17.71 | 16.38 | 42.46 | 70.72 | 50.94 | 53.43 | 68.47 | 35.66 | 40.22 | 55.29 | 52.14 |
| Gated DeltaNet | **16.42** | **12.17** | **46.65** | **72.25** | **55.76** | **52.45** | **71.21** | **38.39** | **40.25** | **60.24** | **55.32** |
| *Attention or hybrid models* | | | | | | | | | | | |
| Transformer++ | 18.53 | 18.32 | 42.60 | 70.02 | 50.23 | 53.51 | 68.83 | 35.10 | 40.66 | 57.09 | 52.25 |
| Samba | 16.13 | 13.29 | 44.94 | 70.94 | 53.42 | 55.56 | 68.81 | 36.17 | 39.96 | 62.17 | 54.00 |
| Gated DeltaNet-H1 | 16.07 | 12.13 | 47.73 | 72.57 | 56.53 | 58.40 | 71.25 | 40.10 | 41.40 | 63.33 | 56.40 |
| Gated DeltaNet-H2 | **15.71** | **12.25** | **46.96** | **72.36** | **56.33** | **57.77** | **71.59** | **39.69** | **42.25** | **60.21** | **56.48** |

## In-context retrieval on real-world data [p. 7]

Table 4 presents results on real-world recall-intensive tasks used by Arora et al. (2024b) [p. 7]. As expected, linear recurrent models show a significant performance gap compared to Transformers, while hybrid models combining linear recurrence and attention outperform pure attention models in retrieval tasks [p. 7-8].

For pure recurrent models, despite DeltaNet's superior performance on synthetic in-context retrieval tasks (Yang et al., 2024b), its real-world retrieval performance lags behind Mamba2, consistent with our observations in S-NIAH-2 and S-NIAH-3 from Table 2 [p. 8]. Gated DeltaNet outperforms both DeltaNet and Mamba2 thanks to its gated delta rule, though the improvement margin is smaller than in Table 2 [p. 8]. We attribute this reduced performance gap to instruction-unaligned small language models being prone to repetition errors, which are the primary source of errors in these tasks (cf. Arora et al. (2024b, Appendix E)) [p. 8]. Since this issue is largely independent of the update rule choice, the performance differences between models are less pronounced compared to Table 2 [p. 8].

**Table 4** (p. 7): Accuracy on recall-world retrieval tasks with input truncated to 2K tokens. SQD: SQUADE. TQA: Trivial QA.

| Models | SWDE | SQD | FDA | TQA | NQ | Drop | Avg |
|--------|------|-----|-----|-----|-----|------|-----|
| *Recurrent models* | | | | | | | |
| RetNet | 14.0 | 28.5 | 7.0 | 54.4 | 16.2 | 17.3 | 22.9 |
| HGRN2 | 8.3 | 25.3 | 4.8 | 51.2 | 14.2 | 16.9 | 20.1 |
| Mamba | 9.8 | 25.8 | 3.7 | 54.3 | 14.9 | 17.4 | 21.0 |
| Mamba2 | 19.1 | 33.6 | **25.3** | **61.0** | **20.8** | 19.2 | 29.8 |
| DeltaNet | 17.9 | **30.9** | 18.4 | 53.9 | 17.3 | 18.6 | 26.2 |
| Gated DeltaNet | **25.4** | **34.8** | **23.7** | **60.0** | **20.0** | **19.8** | **30.6** |
| *Attention or hybrid models* | | | | | | | |
| Transformer++ | 29.5 | 38.0 | **52.2** | 58.3 | 22.5 | 21.6 | 37.0 |
| Samba | 33.0 | 39.2 | 50.5 | 57.7 | 23.5 | 20.2 | 37.4 |
| Gated DeltaNet-H1 | 35.6 | **39.7** | 52.0 | **60.1** | **24.6** | **22.5** | 39.0 |
| Gated DeltaNet-H2 | **38.2** | **40.4** | 50.7 | **63.3** | **24.8** | **23.3** | **40.1** |

## Length extrapolation on long sequences [p. 8]

As shown in Fig. 2, we evaluate the models' capacity to extrapolate to sequences of up to 20K tokens across six long-context benchmarks [p. 8]. Gated DeltaNet achieves the lowest overall perplexity across RNN models [p. 8]. While we observe mixed results in length extrapolation, Gated DeltaNet exhibits relatively more robust performance, suggesting better memory management [p. 8]. The hybrid models further improve upon this by leveraging attention for long context, alleviating the memory management burden on their recurrent components [p. 8]. Future work will explore these models' capabilities on even longer sequences [p. 8].

**Figure 2** (p. 8): Length extrapolation on six long benchmarks.

Description: Six line plots showing perplexity vs. sequence length (4k, 8k, 14k, 20k) for different models
- Key elements: Six subplots for GovReport, QMSum, NarrativeQA, Qasper, CodeParrot, and PG19; each showing multiple colored lines representing Mamba1, DeltaNet, Mamba2, Samba, GatedDeltaNet, GatedDeltaNet-H1, and GatedDeltaNet-H2
- Notable patterns: GatedDeltaNet generally shows lower and more stable perplexity across increasing sequence lengths compared to other recurrent models; hybrid models (H1 and H2) show competitive performance with attention-based models
- Supports claim: Demonstrates Gated DeltaNet's robust memory management and length extrapolation capabilities

## Long context understanding [p. 8]

As demonstrated in Table 5, we evaluated the models' performance on LongBench (Bai et al., 2023) [p. 8]. In recurrent models, Gated DeltaNet shows consistent advantages, especially in single-doc QA, few-shot in-context learning, and Code tasks, demonstrating its superior capabilities in retrieval, in-context learning, and state tracking, respectively [p. 8].

## Throughput Comparison [p. 8]

The training throughput comparison across different models is presented in Fig. 3 [p. 8]. As our analysis shows, the gated delta rule introduces only marginal overhead compared to the original delta rule, with Gated DeltaNet achieving essentially the same throughput as DeltaNet [p. 8]. Both are slightly slower than Mamba2 (2-3K tokens/sec) due to their more expressive transition matrices [p. 8].

The Transformer++ achieves the best performance in the 2K context window domain, thanks to the highly optimized Flash-Attention-2 kernel (Dao, 2023) [p. 8]. Consequently, hybrid approaches combining 2K window-size SWA attention with other token mixers demonstrate higher throughput than standalone mixers: Samba outperforms Mamba, while Gated DeltaNet-H1 and -H2 outperform Gated DeltaNet [p. 8-9]. Notably, Gated DeltaNet-H1 maintains compelling training throughput across all sequence lengths, even on short sequences [p. 9].

**Table 5** (p. 9): Accuracy on 14 tasks from LongBench (Bai et al., 2023): Narrative QA, QasperQA, MultiField QA, HotpotQA, 2WikiMulti QA, Musique, GovReport, QMSum, MultiNews, TRec, Trivia QA, SamSum, LCC, and RepoBench-P by order.

| Model | Single-Doc QA<br>NQA  QQA  MFQ | Multi-Doc QA<br>HQA  2WM  Mus | Summarization<br>GvR  QMS  MNs | Few-shot<br>TRC  TQA  SSM | Code<br>LCC  RBP | Avg |
|--------|-------------------------------|------------------------------|------------------------------|--------------------------|-----------------|-----|
| *Recurrent models* | | | | | | |
| RetNet | 12.1  10.7  19.1 | 10.7  **18.0**  5.8 | 4.8  15.8  7.9 | 19.0  18.0  **12.8** | 14.1  17.9 | 13.2 |
| HGRN2 | 10.7  **12.1**  19.1 | 11.3  15.7  **6.0** | 5.2  15.1  **9.2** | 16.0  15.8  10.3 | **18.6**  20.8 | 13.5 |
| Mamba | 12.0  10.7  20.4 | 10.1  16.2  6.0 | 2.7  15.9  8.4 | 21.5  21.9  11.2 | 17.9  19.6 | 14.6 |
| Mamba2 | 13.1  10.3  20.6 | 10.9  18.0  5.7 | 4.5  15.2  9.1 | 19.1  19.6  8.7 | 16.1  17.0 | 13.7 |
| DeltaNet | 11.3  11.3  18.8 | **11.8**  15.1  6.7 | 6.7  14.5  7.4 | 13.0  **23.6**  8.4 | 17.6  20.6 | 13.5 |
| Gated DeltaNet | **14.1**  **14.0**  **23.3** | 13.7  **14.4**  **5.8** | **7.5**  **16.4**  **7.9** | **30.0**  22.4  **23.0** | **18.7**  **22.1** | **16.6** |
| *Attention or hybrid models* | | | | | | |
| Transformer++ | 11.8  9.3  10.0 | 10.9  4.2  6.1 | 7.4  15.8  6.6 | 16.9  13.5  3.9 | 17.2  18.7 | 11.0 |
| Samba | 12.5  12.6  25.4 | 11.2  19.7  6.8 | **9.1**  15.7  11.0 | 20.0  **23.7**  22.8 | 18.3  24.1 | 15.9 |
| Gated DeltaNet-H1 | 14.5  12.3  **26.6** | 12.9  **23.6**  6.7 | **12.1**  **17.5**  **12.8** | **23.5**  23.9  **28.8** | **19.5**  19.2 | **17.8** |
| Gated DeltaNet-H2 | **22.2**  **15.0**  **27.1** | **12.7**  20.6  **7.5** | **10.4**  16.2  **12.0** | **30.5**  **22.2**  **27.9** | 19.9  **23.1** | **18.4** |

**Figure 3** (p. 9): Training throughput comparison of 1.3B models on a single H100 GPU.

Description: Line plot showing throughput (thousands tokens per second) vs. sequence length × batch size
- Key elements: X-axis shows 2K×16, 4K×8, 8K×4, 16K×2; Y-axis ranges from 25 to 60 thousand tokens/sec; Multiple colored lines for Transformer++, DeltaNet, Gated DeltaNet, Mamba1, Mamba2, Gated DeltaNet-H1, Samba, and Gated DeltaNet-H2
- Notable patterns: Transformer++ shows steep decline from ~55K to ~27K tokens/sec as sequence length increases; Gated DeltaNet and DeltaNet maintain nearly identical throughput around 48-50K tokens/sec; Hybrid models H1 and H2 show competitive throughput especially at longer sequences
- Supports claim: Demonstrates that gated delta rule introduces minimal overhead and that hybrid architectures maintain strong training efficiency
