# 1. Introduction [p. 4-5]

[p. 4] In the past few years, Large Language Models (LLMs) (Anthropic, 2023; Google, 2023; OpenAI, 2022, 2023) have undergone rapid development. The intelligence of an LLM tends to improve as the number of parameters increases, exhibiting emergent capabilities across various tasks (Wei et al., 2022). However, the improvement comes at the cost of larger computing resources for training and a potential decrease in inference throughput.

DeepSeek-V2 is introduced as a strong open-source Mixture-of-Experts (MoE) language model, characterized by economical training and efficient inference through an innovative Transformer architecture. It has a total of 236B parameters, of which 21B are activated for each token, and supports a context length of 128K tokens. [p. 4]

## Key Architectural Innovations

Two main optimizations are applied to the attention modules and Feed-Forward Networks (FFNs) within the Transformer framework (Vaswani et al., 2017):

**(1) Multi-head Latent Attention (MLA):** The KV cache of Multi-Head Attention (MHA) (Vaswani et al., 2017) poses a significant obstacle to inference efficiency of LLMs. Existing approaches such as Grouped-Query Attention (GQA) (Ainslie et al., 2023) and Multi-Query Attention (MQA) (Shazeer, 2019) often compromise performance in their attempt to reduce the KV cache. MLA is an attention mechanism equipped with low-rank key-value joint compression. Empirically, MLA achieves superior performance compared with MHA, and meanwhile significantly reduces the KV cache during inference. [p. 4]

**(2) DeepSeekMoE:** The DeepSeekMoE architecture (Dai et al., 2024) is adopted for FFNs. It uses fine-grained expert segmentation and shared expert isolation for higher potential in expert specialization. It demonstrates great advantages compared with conventional MoE architectures like GShard (Lepikhin et al., 2021), enabling training strong models at an economical cost. Expert parallelism is employed during training with supplementary mechanisms to control communication overheads and ensure load balance. [p. 4]

## Pre-training and Alignment

[p. 4] A high-quality and multi-source pre-training corpus consisting of 8.1T tokens is constructed. Compared with the corpus used in DeepSeek 67B (DeepSeek-AI, 2024), this corpus features an extended amount of data, especially Chinese data, and higher data quality.

After pre-training, 1.5M conversational sessions are collected encompassing various domains such as math, code, writing, reasoning, safety, and more, to perform Supervised Fine-Tuning (SFT) for DeepSeek-V2 Chat (SFT). Then, following DeepSeekMath (Shao et al., 2024), Group Relative Policy Optimization (GRPO) is employed to further align the model with human preference and produce DeepSeek-V2 Chat (RL). [p. 4]

## Evaluation Highlights

[p. 4-5] Even with only 21B activated parameters, DeepSeek-V2 still achieves top-tier performance among open-source models and becomes the strongest open-source MoE language model. Compared with DeepSeek 67B, DeepSeek-V2 saves 42.5% of training costs, reduces the KV cache by 93.3%, and boosts the maximum generation throughput to 5.76 times.

[p. 5] DeepSeek-V2 Chat (RL) achieves 38.9 length-controlled win rate on AlpacaEval 2.0 (Dubois et al., 2024), 8.97 overall score on MT-Bench (Zheng et al., 2023), and 7.91 overall score on AlignBench (Liu et al., 2023). English open-ended conversation evaluations demonstrate top-tier performance among open-source chat models. The evaluation on AlignBench indicates that in Chinese, DeepSeek-V2 Chat (RL) outperforms all open-source models, and even beats most closed-source models.

## DeepSeek-V2-Lite

[p. 5] DeepSeek-V2-Lite is also released: a smaller model equipped with MLA and DeepSeekMoE for the open-source community. It has a total of 15.7B parameters, where 2.4B are activated for each token. Detailed descriptions can be found in Appendix B.

## Paper Outline

[p. 5-6] The rest of the paper covers: model architecture of DeepSeek-V2 (Section 2), pre-training endeavors including data construction, hyper-parameter settings, infrastructures, long context extension, and model performance and efficiency evaluation (Section 3), alignment including SFT, RL, evaluation results, and discussion (Section 4), and conclusion with limitations and future work (Section 5).

## Figures

**Figure 1** (p. 1): "Figure 1 | (a) MMLU accuracy vs. activated parameters, among different open-source models. (b) Training costs and inference efficiency of DeepSeek 67B (Dense) and DeepSeek-V2."

Panel (a) is a scatter plot with x-axis "Activated Parameters (Billions)" (0-100) and y-axis "Performance (MMLU)" (55-80). DeepSeek-V2 appears at approximately (21B, ~79) at the top of the chart, outperforming models with far more activated parameters. Other models shown include: LLaMA 2 13B (~55), LLaMA 1 33B (~57), LLaMA 2 34B (~63), LLaMA 3 8B (~65), Mistral 7B (~61), Command R (~68), Mixtral 8x7B (~70), Qwen1.5 32B (~73), DBRX (~74), Mixtral 8x22B (~77), Qwen1.5 72B (~77), LLaMA 3 70B (~79), Command R+ (~76), DeepSeek 67B (~73), Grok-1 (~73), LLaMA 2 70B (~69), LLaMA 1 65B (~64). Model families shown: LLaMA 1, LLaMA 2, LLaMA 3, Mixtral, Command R, Qwen1.5.

Panel (b) consists of three horizontal bar charts comparing DeepSeek 67B and DeepSeek-V2:
- Training Costs (K GPU Hours/T Tokens): DeepSeek 67B uses ~300K, DeepSeek-V2 uses ~175K, annotated "saving 42.5% of training costs"
- KV Cache for Generation (KB/Token): DeepSeek 67B uses ~400 KB/Token, DeepSeek-V2 uses ~27 KB/Token, annotated "reducing KV cache by 93.3%"
- Maximum Generation Throughput (Tokens/Sec): DeepSeek 67B ~9,000, DeepSeek-V2 ~50,000+, annotated "576% of maximum throughput"

**Figure 2** (p. 5): "Figure 2 | Illustration of the architecture of DeepSeek-V2. MLA ensures efficient inference by significantly reducing the KV cache for generation, and DeepSeekMoE enables training strong models at an economical cost through the sparse architecture."

The figure shows a Transformer Block (repeated L times) with two main components:
- Left side: standard Transformer block diagram showing Attention -> RMS Norm -> Feed-Forward Network -> RMS Norm with residual connections.
- Right side expanded view: The MLA (Multi-head Latent Attention) mechanism at bottom showing input hidden $\mathbf{h}_t$ being compressed into latent vectors $\mathbf{c}_t^Q$ (for queries) and $\mathbf{c}_t^{KV}$ (for keys/values). From $\mathbf{c}_t^Q$, compressed query components $\{\mathbf{q}_{t,i}^C\}$ and RoPE query components $\{\mathbf{q}_{t,i}^R\}$ are produced and concatenated into $\{[\mathbf{q}_{t,i}^C; \mathbf{q}_{t,i}^R]\}$. From $\mathbf{c}_t^{KV}$, compressed key components $\{\mathbf{k}_{t,i}^C\}$ and value components $\{\mathbf{v}_{t,i}^C\}$ are produced; a separate $\mathbf{k}_t^R$ (with RoPE applied) is concatenated with compressed keys to form $\{[\mathbf{k}_{t,i}^C; \mathbf{k}_t^R]\}$. The hatched circles on $\mathbf{c}_t^{KV}$ and $\mathbf{k}_t^R$ indicate "Cached During Inference." The DeepSeekMoE component at top shows input hidden $\mathbf{u}_t$ going through a Router that selects Top-$K_r$ from $N_r$ routed experts (numbered 1, 2, 3, 4, ..., $N_r-1$, $N_r$), plus $N_s$ shared experts (numbered 1 to $N_s$), producing output hidden $\mathbf{h}_t'$.
