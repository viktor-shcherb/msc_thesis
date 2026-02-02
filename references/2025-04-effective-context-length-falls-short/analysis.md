# Why Does the Effective Context Length of LLMs Fall Short?

**Authors:** Chenxin An, Jun Zhang, Ming Zhong, Lei Li, Shansan Gong, Yao Luo, Jingjing Xu, Lingpeng Kong (The University of Hong Kong, ByteDance Inc., University of Illinois Urbana-Champaign)
**Date:** April 2025, ICLR 2025, arXiv:2410.18745

---

## Core Research Problem

Despite advances in distributed training and efficient attention (FlashAttention, Ring Attention), the **effective context lengths** of open-source LLMs fall far short of their claimed training context lengths. On the RULER benchmark (Hsieh et al., 2024), Llama 3.1 70B has an effective context length of only 64K despite being trained with a 128K context window using scaled RoPE base frequency. More broadly, most open-source models demonstrate an effective context length less than 50% of their training length. Prior work has focused on extending context windows through data engineering (Fu et al., 2024b; Hu et al., 2024), synthetic data generation (An et al., 2024b; Zhao et al., 2024), and architectural modifications to RoPE base frequency (Peng et al., 2023; Chen et al., 2023). However, these approaches treat the symptom (short effective context) without identifying the root cause. The core challenge is: **why does the effective context length of LLMs fall short of their training context lengths, and can this gap be closed without additional training?**

---

## Problem Solutions

The paper identifies the root cause as the **left-skewed position frequency distribution** -- a pattern of severe undertraining of long-distance relative position indices during pretraining and post-training stages -- and proposes STRING (ShifTed Rotary position embeddING), a training-free inference-time fix. The solution is built on:

1. **Diagnosis -- left-skewed position frequency distribution:** In pretraining corpora such as SlimPajama-627B, the frequency of relative position indices decreases dramatically with distance. For a 2048-token context window, positions i <= 1024 account for more than 80% of all position index occurrences, while positions i >= 1536 constitute less than 5%. This undertraining of distant positions directly limits the model's ability to gather information from far-away tokens.

2. **Probing evidence -- position frequency determines effective length:** Controlled pretraining experiments show that models achieve similar effective context lengths when they have been exposed to similar frequencies of position indices, regardless of their maximum training lengths. The growth trend of effective length aligns with the position frequency distribution.

3. **STRING -- shifting well-trained positions to replace undertrained ones:** During inference, STRING drops infrequent position indices at the tail of the distribution and shifts well-trained (frequent) position indices from the main diagonal of the position matrix to the bottom-left corner, enabling the model to represent long-range dependencies using frequently encountered positions. A small local window preserves neighboring-token relationships.

---

## Approach Details

### Method

#### Left-Skewed Position Frequency Distribution

For relative positional encodings such as RoPE (Su et al., 2022), the relative position matrix P after computing Q^T K for a training length L is a Toeplitz matrix:

> P[m][n] = m - n

The frequency of relative position i within a single sequence is f(i) = L - i. Across a pretraining corpus C, the total frequency is:

> f(i) = sum over s in C of max(|s| - i, 0), for 0 <= i < L

This distribution is inherently left-skewed: position 0 occurs in every token pair, while position L-1 occurs only once per maximum-length sequence. The skew is compounded by the real-world data length distribution, which is also biased toward shorter sequences. In SlimPajama-627B with a 2048-token training length, even with a uniform data length distribution, position frequency declines quadratically; when all data are concatenated to fill the context window, it still declines linearly.

#### Probing Experiments on Position Frequency and Effective Length

Two 1.3B-parameter TinyLlama models were pretrained from scratch on SlimPajama with context lengths of 2K and 4K tokens (1T tokens total). Effective context length was measured every 10B tokens using a 4-needle Needle-in-a-Haystack task (500 tests per length, 128-token steps). Three findings emerged:

**(1) Larger training context window consumes fewer tokens to achieve the same effective context length:** The 4K model achieved an effective length of 1.4K after 400B tokens; the 2K model required ~1T tokens for the same.

**(2) Models achieve similar effective context lengths at similar position frequencies, regardless of training length:** When plotting effective length against position frequency f(i) at that length (Figure 2b), the growth curves of both models align. For example, both reach 1,280-token effective length when f(1280) = 100B.

**(3) The growth trend of effective length aligns with the position frequency distribution:** Both models consume ~300B tokens to reach 1,024-token effective length (where their position frequencies are close), but diverge thereafter as the frequency gap widens.

Furthermore, evaluating 13 open-source models on NIAH, most failure cases occur within the first L/3 of the document (Table 4), indicating that the last L/3 positions fall into the undertrained tail of the position frequency distribution.

#### STRING: Manipulating the Position Matrix

STRING operates in three steps on the relative position matrix P, illustrated for L = 9, N = 6 (threshold for frequent positions), S = L - N = 3 (shift offset):

**(1) Dropping Infrequent Positions:** Remove all position indices i >= N from the matrix.

**(2) Shifting Frequent Positions:** Shift remaining position indices from the main diagonal to fill the empty bottom-left triangle. The shift offset is S = L - N:

> P[m][n] = P[m][n] - S if m >= n - S; P[m][n] otherwise (Eq. 3)

**(3) Restoring Locality with a Small Window:** Shifting disrupts local relationships by setting relative positions on the S-th diagonal to zero. A small local window W << S restores emphasis on the W closest neighboring tokens:

> P[m][n] = P[m][n] - S + W if m >= n - S; P[m][n] otherwise (Eq. 4)

### Key Technical Components

- **Hyperparameters:** The authors recommend W >= 32 and L/3 <= S <= L/2. For all experiments across downstream tasks: **S = L/3** and **W = 128**.
- **Ablation on W:** Performance is significantly better than RoPE when W >= 32. As long as W << S, further increasing W does not cause a performance drop.
- **Ablation on S:** Within the range L/5 to L/2, performance increases with S. The trend slows when S exceeds L/3, indicating that at least the last 33-50% of positions can be overwritten.

### FlashAttention Implementation

STRING is implemented via FlashAttention (Dao et al., 2022) by splitting attention into two components:

1. **Sliding window attention** around the main diagonal for positions where m < n - S. Uses standard (unmodified) position indices for both queries and keys.

2. **Shifted self-attention** in the bottom-left triangle for positions where m >= n - S. Query position indices are shifted: `pids_q_shifted = pids_query - S + W`. Keys retain original position indices. Only the last N rows of Q attend to the first N columns of K,V.

The two attention outputs are merged using a weighted combination based on their respective softmax normalizers (Algorithm 2). STRING incurs no additional computational cost beyond the standard FlashAttention implementation -- inference time overhead is within 0.3 seconds per token, and GPU memory increase is less than 5GB on Llama3.1 8B at 128K context.

### Experimental Setup

**Models:** Seven open-source base models with training lengths 2K-128K: TinyLlama-1.3B (pretrained by authors, 2K), TinyLlama-1.1B-3T (2K), Llama-2-7B (4K), Llama-3-8B (8K), LWM-7B-base (32K), Mistral-7B-base (32K), Llama-3.1-8B (128K). For RULER and InfiniteBench: additionally Llama3.1 70B and Qwen2 72B.

**Baselines:** Original RoPE, and five training-free extrapolation methods: NTK-Aware RoPE (LocalLLaMA, 2023), YaRN (Peng et al., 2023), ReRoPE (Su, 2023), Self-Extend (Jin et al., 2024), and DCA (An et al., 2024a). For extrapolation baselines, the training length is set to 2/3 of the original and the extrapolation scaling factor is 3/2.

**Evaluation benchmarks:**
- Needle-in-a-Haystack (4-needle, gkamradt 2023): 500 test cases per model, tested at training length
- RULER (Hsieh et al., 2024): 13 tasks (NIAH variants, variable tracing, aggregation, QA), 500 test cases per task, tested at 128K
- InfiniteBench (Zhang et al., 2024d): long-context QA, summarization, retrieval, math, code, tested at 128K

### Key Results

**Needle-in-a-Haystack (4-needle) at training length:**

| Model | L_train | RoPE | DCA | STRING |
|---|---|---|---|---|
| TinyLlama-1.3B (ours) | 2K | 56.6 | 74.4 | **84.6** |
| TinyLlama-1.1B-3T | 2K | 69.8 | 80.2 | **97.2** |
| Llama-2-7B | 4K | 98.0 | 91.6 | **100.0** |
| Llama-3-8B | 8K | 99.8 | 99.9 | **99.6** |
| LWM-7B-base | 32K | 31.8 | 28.8 | **50.4** |
| Mistral-7B-base | 32K | 52.8 | 64.2 | **73.0** |
| Llama-3.1-8B | 128K | 66.0 | 72.8 | **95.2** |
| **Average** | -- | 67.8 | 73.1 | **85.7** |

- STRING outperforms all methods on every model except Llama-3-8B (where all methods saturate near 100%).
- The average improvement over the next best method (DCA) is 12.6 points.

**RULER at 128K sequence length:**

| Model | Effective/Claimed | NIAH | VT | Aggregation | QA | Avg. |
|---|---|---|---|---|---|---|
| GPT-4-1106-preview | 64K / 128K | 84.8 | 99.6 | 79.7 | 59.0 | 81.2 |
| GLM4 (open-source best) | 64K / 1M | 94.4 | 97.7 | 49.7 | 63.6 | 83.1 |
| Llama3.1 (8B) | 32K / 128K | 92.6 | 70.4 | 36.2 | 58.8 | 77.0 |
| Llama3.1 (8B) + STRING | 32K / 128K | 94.0 | 88.1 | 37.6 | 62.7 | 80.0 |
| Llama3.1 (70B) | 64K / 128K | 78.9 | 59.2 | 39.8 | 47.6 | 66.6 |
| Llama3.1 (70B) + STRING | 100K / 128K | 92.7 | 95.6 | 50.0 | 63.0 | **81.7** |
| Qwen2 (72B) | 64K / 128K | 48.0 | 79.0 | 70.3 | 47.2 | 53.7 |
| Qwen2 (72B) + STRING | 100K / 128K | 91.2 | 98.4 | 83.7 | 52.2 | **84.6** |

- STRING improves Llama3.1 70B by 15.1 points and Qwen2 72B by 30.9 points.
- Both models with STRING surpass GPT-4-128K (81.2) in average performance.
- Effective context length increases from 64K to 100K for both 70B-scale models.
- At 100K test length, Llama3.1-STRING (70B) scores 87.2 and Qwen2-STRING (72B) scores 87.8.
- Other extrapolation methods (YaRN, DCA, Self-Extend, ReRoPE) fail to improve Llama3.1-8B on RULER.

**InfiniteBench at 128K:**

| Tasks | GPT-4 | Claude2 | Llama3.1 70B RoPE | Llama3.1 70B STRING |
|---|---|---|---|---|
| En.Sum | 14.73 | 14.45 | 26.89 | 27.64 |
| En.QA | 22.22 | 11.97 | 13.68 | 16.73 |
| En.MC | 67.25 | 62.88 | 76.41 | 81.98 |
| En.Dia | 8.50 | 46.50 | 18.00 | 30.50 |
| Retr.KV | 89.00 | 65.40 | 2.22 | 76.07 |
| Code.debug | 39.59 | 2.28 | 29.20 | 32.80 |
| Math.find | 60.00 | 32.29 | 40.92 | 46.28 |
| **Avg.** | 55.69 | 47.96 | 45.25 | **56.88** |

- STRING improves Llama3.1 70B by 11.63 points average, surpassing GPT-4-128K (55.69 vs 56.88).
- The largest single-task gain is on Retr.KV: from 2.22 to 76.07 (+73.85 points).

### Pretraining Setup (for TinyLlama-1.3B probing experiments)

- Architecture: TinyLlama 1.1B (hidden size 2048, FFN size 5632, 32 attention heads, 22 layers) with Llama3 tokenizer (128,256 tokens)
- Dataset: SlimPajama-627B, 1T tokens total
- Optimizer: AdamW, cosine learning rate schedule, max LR 4e-4, min LR 4e-5, warmup 2000 steps
- Batch size: 4M tokens, gradient clipping 1.0
- Hardware: 16 NVIDIA 80G A100 GPUs (2 nodes); ~28 days for 2K, ~32 days for 4K

### Limitations

The probing experiments only investigate pretraining lengths smaller than 4K tokens. The question of how to effectively implement long-context training at scale remains open. STRING addresses the left-skewed distribution at inference time only; addressing it during training (e.g., by adjusting the frequency distribution of training data) is left as future work but may require data with a distribution similar to the original pretraining corpus to preserve reasoning ability.

---

## Conclusions

1. **Left-skewed position frequency distribution is the root cause of the effective context length gap:** The frequency of relative position indices in pretraining corpora decreases dramatically with distance. Positions in the last L/3 of the context window are severely undertrained, directly limiting models' ability to gather distant information.

2. **Position frequency -- not training length -- determines effective context length:** Controlled pretraining experiments demonstrate that models achieve comparable effective context lengths when exposed to similar position frequencies, regardless of their maximum training lengths. This provides a causal explanation for the <50% effective-to-training length ratio observed across open-source LLMs.

3. **STRING achieves substantial gains without any training:** By shifting well-trained position indices to replace infrequent ones during inference, STRING improves NIAH (4-needle) performance by an average of 18 points across seven models, boosts Llama3.1 70B and Qwen2 72B by over 10 points on RULER and InfiniteBench, and establishes new state-of-the-art results for open-source LLMs.

4. **Larger models benefit more from STRING:** The performance gains on 70B-scale models are substantially larger than on 8B models, suggesting that frequent positions in larger models possess a stronger latent capacity for modeling long-range dependencies that is simply not being exploited under standard position encoding.

5. **Open-source models can rival commercial models on long-context tasks:** With STRING, Llama3.1 70B surpasses GPT-4-128K on both RULER (81.7 vs 81.2) and InfiniteBench (56.88 vs 55.69), demonstrating that the gap between open-source and commercial models on long-context tasks is largely attributable to ineffective position encoding rather than fundamental model limitations.

6. **Efficient FlashAttention implementation:** STRING can be implemented with negligible overhead (within 0.3s per token and <5GB additional memory compared to standard FlashAttention) by splitting attention into sliding window and shifted self-attention components.

---

## Core References and Why They Are Referenced

### Positional Encoding Foundations
- **Su et al. (2022)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* Introduces RoPE, the positional encoding used by all models in the paper. STRING operates by manipulating RoPE's relative position matrix.
- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Foundational transformer architecture; establishes the self-attention mechanism that inherently lacks positional information.

### Context Extension Methods (Baselines)
- **Chen et al. (2023)** -- *Extending Context Window of Large Language Models via Positional Interpolation (PI).* Position Interpolation is referenced as a foundational context extension method; STRING's approach is fundamentally different (manipulating the position matrix rather than rescaling position indices).
- **LocalLLaMA (2023)** -- *NTK-Aware Scaled RoPE (Reddit post).* Baseline method that increases the RoPE base frequency for extrapolation. STRING outperforms it on all NIAH experiments (Table 1).
- **Peng et al. (2023)** -- *YaRN: Efficient Context Window Extension.* The most established RoPE extension method; used as a primary baseline. STRING outperforms YaRN on all models in Table 1 and is the only method to improve Llama3.1-8B on RULER (Table 2).
- **Su (2023)** -- *ReRoPE (Rectified Rotary Position Embeddings).* Position matrix modification method used as a baseline. ReRoPE modifies attention mechanism computation and is less compatible with FlashAttention.
- **Jin et al. (2024)** -- *Self-Extend LLM Context Window Without Tuning.* Training-free method using repeated positions for extrapolation; baseline in Tables 1 and 2.
- **An et al. (2024a)** -- *Training-Free Long-Context Scaling of Large Language Models (DCA).* By the same first author; second-best method after STRING in the NIAH experiments (73.1% vs 85.7% average). DCA also manipulates the position matrix but uses a different strategy.

### Models Used in Evaluation
- **Llama Team (2024)** -- *The Llama 3 Herd of Models.* Provides Llama3.1 8B and 70B, the primary large-scale evaluation models. The paper demonstrates that STRING increases Llama3.1 70B's effective length from 64K to 100K on RULER.
- **Bai et al. (2023)** -- *Qwen Technical Report.* Provides Qwen2 72B. STRING improves Qwen2 72B by over 30 points on RULER, achieving 84.6 average -- the highest open-source score.
- **Touvron et al. (2023a)** -- *LLaMA: Open and Efficient Foundation Language Models.* Architecture basis for TinyLlama pretraining experiments.
- **Zhang et al. (2024b)** -- *TinyLlama: An Open-Source Small Language Model.* Architecture and training framework used for the probing experiments.
- **Mistral.AI (2024)** -- *Mistral 7B.* One of the seven evaluation models in the NIAH experiments.
- **Liu et al. (2024a)** -- *LargeWorldModel (LWM-7B-base).* Long-context model used in NIAH evaluation; trained with Ring Attention.

### Evaluation Benchmarks
- **Hsieh et al. (2024)** -- *RULER: What's the Real Context Size of Your Long-Context Language Models?* Primary long-context benchmark with 13 synthetic tasks. STRING establishes new open-source SOTA on RULER at 128K.
- **Zhang et al. (2024d)** -- *InfiniteBench: Extending Long Context Evaluation Beyond 100K Tokens.* Real-world long-context tasks (QA, summarization, retrieval, code, math). STRING enables Llama3.1 70B to surpass GPT-4-128K.
- **gkamradt (2023)** -- *Needle-in-a-Haystack.* The foundational long-context retrieval test. The paper uses the 4-needle variant following the Llama 3.1 report.

### Pretraining Data and Infrastructure
- **Cerebras (2023)** -- *SlimPajama-627B.* Pretraining corpus for the TinyLlama probing experiments and for analyzing the left-skewed position frequency distribution.
- **Dao (2023)** -- *FlashAttention-2.* Essential for STRING's implementation on modern LLMs with long context windows; STRING is implemented by combining sliding window attention and shifted self-attention within FlashAttention.

### Long-Context Scaling and Related Work
- **Kaplan et al. (2020)** -- *Scaling Laws for Neural Language Models.* Referenced for the methodology of analyzing how effective length grows with consumed tokens.
- **Beltagy et al. (2020)** -- *Longformer.* Introduces sliding window attention, one of the two attention patterns STRING combines.

#### Cross-References in Available Papers

- **PI (2023-06-pi-positional-interpolation):** STRING references PI as a foundational context extension method. PI rescales position indices uniformly (m -> mL/L'), while STRING manipulates the position matrix to replace infrequent positions with frequent ones. PI is not a direct baseline in STRING's experiments but is part of the broader context of RoPE modification methods.
- **NTK-Aware Scaled RoPE (2023-06-rope-ntk):** Used as one of six baselines in STRING's NIAH experiments (Table 1). NTK-Aware achieves 67.6% average vs STRING's 85.7%. STRING differs fundamentally: NTK-Aware modifies the RoPE base frequency, while STRING directly manipulates the position matrix at inference time.
- **YaRN (2024-05-yarn-context-extension):** Used as a primary baseline throughout. On NIAH (Table 1), YaRN scores 70.5% vs STRING's 85.7%. On RULER for Llama3.1-8B (Table 2), YaRN fails to improve over base RoPE (76.3 vs 77.0), while STRING achieves 80.0. STRING's approach is orthogonal to YaRN: YaRN rescales frequencies with a learned temperature, while STRING shifts position indices in the attention matrix.
- **Lost in the Middle (2024-02-lost-in-the-middle):** Not directly cited by STRING, but thematically related. Lost in the Middle documents the U-shaped performance curve (models fail at retrieving mid-context information). STRING's probing experiments (Section 3, Figure 4) provide a causal explanation: mid-context corresponds to large relative positions in the undertrained tail of the position frequency distribution. STRING's position shifting directly addresses the mechanism underlying the "lost in the middle" phenomenon for information at large relative distances from the query.
- **RULER (2024-10-ruler-context-size):** Used as the primary evaluation benchmark for STRING's large-scale experiments (Table 2). STRING achieves new open-source SOTA on RULER at 128K: Qwen2 72B + STRING scores 84.6, surpassing GPT-4-128K (81.2) and the previous open-source best GLM4 (83.1).
- **DroPE (2025-12-drope-dropping-positional-embeddings):** DroPE takes a fundamentally different approach to the same problem space: rather than manipulating position indices at inference time, DroPE removes positional embeddings entirely and recalibrates. STRING and DroPE share the insight that standard RoPE is suboptimal for long-context use, but propose opposite remedies -- STRING works within the RoPE framework while DroPE abandons it.
