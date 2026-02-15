# Effects of optimization on attention sink [p. 5-6]

[p. 5-6]

The authors pre-train a series of LLaMA models to conduct experiments, based on the repos (Zhang et al., 2024a; Liu et al., 2024a). Due to the intractability of replicating LLaMA pre-training, we design small-sized models. Following Liu et al. (2024a), we set hidden dimension $d = 768$, block number $L = 10$, head number $H = 8$, intermediate size of FFN as 1536, resulting in approximately 60M parameters except for word embeddings and unembeddings. We keep the other design the same as LLaMA2 models, including Rotary (Su et al., 2024), pre-norm structure, RMSNorm (Zhang & Sennrich, 2019) as LN, SwiGLU activation (Shazeer, 2020) in FFN, etc [p. 5].

For data distribution, we sample 5B tokens from the Pile dataset (Gao et al., 2020; Liu et al., 2024a). We set the context length to 2048 tokens, the batch size to 1M tokens, and the training step to 20k (including 100 steps for warm-up). We adopt a cosine scheduling. The optimizer uses AdamW (Loshchilov & Hutter, 2017) with a weight decay ratio of 0.1. We use the Pile-CC validation loss (Gao et al., 2020; Liu et al., 2024a) to measure the model performance and sample 100 sequences with $T = 64$ (no BOS token) out of training to compute the metric $\text{Sink}_1^\epsilon$ with $\epsilon = 0.3$ [p. 6].

## Optimization steps [p. 6]

As visualized in Figure 4(*Middle*), under our default setup, attention sink emerges after certain optimization steps, e.g., between 1k and 2k steps. With the progression of pre-training, attention sink becomes more obvious [p. 6].

## Learning rate [p. 6]

With a smaller learning rate, it takes longer training steps to lower training loss, as present in Figure 4(*Right*). Meanwhile, attention sink is also delayed. Besides, as shown in Table 9, we also find that a smaller learning rate results in LMs with less obvious attention sink, even if we compensate for more training steps. But further decreasing learning rate significantly affects the optimization and model performance, e.g., affecting the emergence of attention sink [p. 6].

## Batch size [p. 6]

In Table 10(*Left*), we find that only modifying batch size has no effects on attention sink [p. 6].

**Takeaways:** 1. Attention sink emerges after LMs are trained effectively. 2. Attention sink appears less obvious in LMs trained with small learning rates [p. 6].

**Table 2** (p. 6): "Larger weight decay ratios tend to induce more attention sink heads in LMs. But much larger values hurt the model performance and attention sink disappears."

| $\gamma$ | 0.0 | 0.001 | 0.01 | 0.1 | 0.5 | 1.0 | 2.0 | 5.0 |
|----------|-----|-------|------|-----|-----|-----|-----|-----|
| $\text{Sink}_1^\epsilon$ (%) | 15.20 | 15.39 | 15.23 | 18.18 | 41.08 | 37.71 | 6.13 | 0.01 |
| valid loss | 3.72 | 3.72 | 3.72 | 3.73 | 3.80 | 3.90 | 4.23 | 5.24 |

**Figure 5** (p. 6): "(*Left*) Attention pattern for prefix language modeling. (*Middle*) Attention sink does not only appear on the first token but among the first $p$ tokens for LMs with $p = 5$. (*Right*) With less training data, attention sink disappears. Meanwhile, trained LMs demonstrate overfitting behaviors."

Description: Three panels showing attention patterns and training data effects
- Key elements: Left - triangular heatmap showing attention pattern with prefix region of length $p$; Middle - bar chart showing attention scores at different token positions (sample1-5) with prefix LM and training data labels; Right - line plot showing training loss, valid loss, and sink metrics vs training data amount in billions (0 to 2.5-5.0B)
- Notable patterns: Left - attention distributed within prefix region; Middle - sink appears at positions 1-5 within prefix; Right - sink metric increases with more training data (crosses valid loss around 1-1.5B tokens), insufficient data leads to overfitting
- Supports claim: Demonstrates that sink position is task-dependent and emergence requires sufficient training data
