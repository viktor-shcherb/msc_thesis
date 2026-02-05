---
title: "Yi: Open Foundation Models by 01.AI"
authors: "Young, Chen, Li, Huang, Zhang, Zhang, Wang, Li, Zhu, Chen, et al."
year: 2024
venue: "arXiv preprint 2403.04652"
paper_type: preprint
categories: ["model-release", "architecture", "long-context-evaluation"]
scope: ["open foundation models", "bilingual English-Chinese LLMs", "data quality over quantity", "depth upscaling", "200K context extension"]
benchmarks_used: ["mmlu", "bbh", "c-eval", "cmmlu", "gaokao-bench", "piqa", "hellaswag", "winogrande", "arc", "boolq", "squad", "csqa", "gsm8k", "math-hendrycks", "humaneval", "mbpp", "truthfulqa", "niah", "alpaca-eval", "mmmu"]
models_introduced: ["yi-6b", "yi-34b", "yi-9b"]
models_evaluated: ["gpt-4", "gpt-3.5-turbo", "llama-2-70b", "falcon-7b", "mistral-7b"]
key_claims:
  - id: C1
    claim: "Yi-34B achieves 76.3 on MMLU (5-shot), outperforming LLaMA 2 70B (69.7) and approaching GPT-3.5 (69.1), despite being half the parameter count"
    evidence: "Table 2, Section 6.1.1"
    status: supported
  - id: C2
    claim: "Yi-34B achieves 81.4 on C-Eval and 83.7 on CMMLU, substantially outperforming all other open models on Chinese benchmarks including Qwen 14B (72.1/71.0)"
    evidence: "Table 2, Section 6.1.1"
    status: supported
  - id: C3
    claim: "Context extension to 200K tokens via RoPE ABF and continual pretraining on only 5B tokens causes minimal degradation: Yi-34B MMLU drops from 76.32 to 75.56 (0.76 points)"
    evidence: "Table 6, Section 7.1"
    status: supported
  - id: C4
    claim: "Fewer than 10K carefully curated SFT examples suffice for competitive chat performance, significantly outperforming scaling-based approaches like UltraChat on Alpaca Eval 2.0"
    evidence: "Figure 5, Section 3.2"
    status: supported
  - id: C5
    claim: "4-bit quantization (AWQ) of Yi-34B-Chat reduces memory requirements with less than 1% accuracy drop on MMLU/CMMLU"
    evidence: "Table 4, Section 4.3"
    status: supported
  - id: C6
    claim: "Depth upscaling from Yi-6B (32 layers) to Yi-9B (48 layers) followed by 800B tokens of continual pretraining yields massive gains: GSM8K 32.5->52.3, HumanEval 15.9->39.0"
    evidence: "Table 8, Section 7.3"
    status: supported
  - id: C7
    claim: "Yi-34B-Chat achieves 94.08 on AlpacaEval, surpassing LLaMA 2-Chat 70B (92.66) and approaching GPT-3.5-Turbo (89.37)"
    evidence: "Table 5, Section 6.2.2"
    status: supported
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Uses decoder-only Transformer architecture with modifications (RMSNorm, SwiGLU, RoPE, GQA)"
  - target: 2024-01-roformer-rope
    type: extends
    detail: "Uses RoPE positional encoding with adjusted base frequency (RoPE ABF) for extension to 200K context"
  - target: 2023-02-llama-open-efficient-foundation
    type: extends
    detail: "Architecture directly based on LLaMA with identical components (RMSNorm, SwiGLU, RoPE); code implementation built on LLaMA"
  - target: 2023-07-llama-2-open-foundation-chat
    type: concurrent
    detail: "Both are open-weight bilingual model families; Yi extends GQA to smaller 6B model (LLaMA 2 only uses GQA at 70B) and trains on 3.1T tokens vs 2T"
  - target: 2024-10-ruler-context-size
    type: extended-by
    detail: "RULER evaluates Yi-34B on synthetic long-context tasks including multi-needle retrieval"
  - target: 2025-04-retrieval-head-long-context-factuality
    type: extended-by
    detail: "Wu et al. evaluate Yi-6B and Yi-34B to discover and analyze retrieval heads for long-context factuality"
  - target: 2025-03-longiclbench-long-in-context-learning
    type: extended-by
    detail: "LongICLBench evaluates Yi-6B-200K on extreme-label in-context learning tasks"
open_questions:
  - question: "Would scaling Yi beyond 34B parameters with the same data quality pipeline yield proportional reasoning improvements, given the paper's claim that reasoning correlates strongly with model scale?"
    addressed_by: null
  - question: "Can the data-quality-over-quantity approach to SFT (<10K examples) generalize to domains requiring specialized knowledge (e.g., medicine, law) where curated examples are expensive?"
    addressed_by: null
  - question: "What is the optimal deduplication strength for pretraining data, given that Yi's aggressive filtering removes substantially more data than CCNet or RefinedWeb?"
    addressed_by: null
  - question: "Does the long-context capability truly exist intrinsically in the 4K base model, or does continual pretraining inject new capabilities rather than merely unlocking existing ones?"
    addressed_by: null
---

# Yi: Open Foundation Models by 01.AI

**Authors:** Alex Young, Bei Chen, Chao Li, Chengen Huang, Ge Zhang, Guanwei Zhang, ..., Zonghong Dai (01.AI)
**Date:** March 2024, arXiv:2403.04652

---

## Core Research Problem

Despite the proliferation of open-weight large language models (LLaMA, Falcon, Qwen, Baichuan), most technical reports emphasize architectural innovations or scaling laws while underreporting data engineering decisions. Existing open-weight models at the 34B parameter scale either lack strong bilingual (English-Chinese) performance (LLaMA 2), lag on reasoning benchmarks (Falcon), or do not document their data pipelines in detail (Qwen). Furthermore, the conventional Chinchilla-optimal training regime (Hoffmann et al., 2022) targets compute-optimal token counts (~1T for 34B parameters) that may underperform at inference time compared to overtrained models. The core challenge was: **how to build a bilingual open-weight model family that maximizes downstream performance through data quality engineering rather than architectural novelty, while remaining deployable on consumer hardware (RTX 4090, 24GB).**

---

## Problem Solutions

Yi addresses the problem through three principles:

1. **Data quality over quantity.** A cascaded data cleaning pipeline with aggressive deduplication produces 3.1T tokens of high-quality bilingual data. The authors explicitly prefer "3T tokens over sophisticated engineering over 10T tokens without extensive filtering."

2. **Deliberate over-training.** The 34B model is trained on 3.1T tokens -- roughly 3x the Chinchilla-optimal budget -- to compensate for being smaller than 70B-class models. After int4 quantization, the 34B chat model fits in 24GB GPU memory.

3. **Quality-first alignment.** Fewer than 10K hand-curated, multi-round-iterated SFT examples replace the million-scale instruction datasets used by FLAN and UltraChat.

---

## Approach Details

### Architecture

Yi uses a **decoder-only Transformer** with code based on LLaMA. The stated assumption is: "when trained on extensive data of high-enough quality, a standard architecture can exhibit advanced capability."

### Model Configurations

| Parameter | Yi-6B | Yi-34B |
|---|---|---|
| Hidden Size | 4096 | 7168 |
| Query Heads | 32 | 56 |
| KV Heads | 4 | 8 |
| Layers | 32 | 60 |
| Pretrain Seq. Length | 4096 | 4096 |
| Max Learning Rate | 3e-4 | 1.5e-4 |

### Key Technical Components

#### Grouped-Query Attention (GQA)

Unlike LLaMA 2 (which uses GQA only at 70B), Yi applies GQA to **both** the 6B and 34B models. GQA splits query heads into G groups, sharing a single KV head within each group. The authors report "no performance degradation after applying GQA to our 6B smaller model."

#### SwiGLU Activation

SwiGLU is used as the post-attention activation. The activation size is reduced from `4h` to `8h/3` (where `h` is hidden size) to maintain comparable parameter counts after the KV-head reduction from GQA.

#### RoPE with Adjusted Base Frequency (RoPE ABF)

Standard RoPE is used for positional encoding, with base frequency adjustment (Xiong et al., 2023) enabling extension to 200K context without architectural changes. The authors view long-context capability as **intrinsic**: "the base model already has the capability to model longer than 4K dependency even the model is trained shorter, and the post-train / finetuning procedure simply release this capability."

#### Tokenization

- **Algorithm:** BPE via SentencePiece.
- **Vocabulary size:** 64,000 tokens.
- Numbers split into individual digits. Rare characters fall back to unicode-byte encoding.
- **No dummy prefix** (leading whitespace): "the assumption does not always hold even in the English context, especially for sentences that begin with quotation marks, also it does not show positive effect in Chinese context."

### Data Pipeline

The pretraining corpus consists of **3.1 trillion tokens** of English and Chinese data with the following composition (Figure 2):

| Source | Tokens | Percentage |
|---|---|---|
| Webpage | 2522B | 80.06% |
| Code | 266B | 8.53% |
| Paper | 152B | 4.87% |
| Book | 84B | 3.09% |
| Other | 61B | 1.05% |
| Encyclopedia | 34B | 1.09% |

The data cleaning pipeline (Figure 1) is cascaded:

1. **Language filtering:** CCNet pipeline (Wenzek et al., 2020) for language identification and perplexity scoring.
2. **Heuristic rule filters:** URL/domain/word blocklists, document length, special symbol ratios, repeated n-grams. PII anonymization.
3. **Learned filters:** Four scorers -- perplexity scorer (KenLM), quality scorer (Wikipedia-like classifier), document coherence scorer, and safety scorer.
4. **Cluster-based filters:** Unsupervised semantic clustering with quality annotation. Low-quality clusters excluded.
5. **Cascaded deduplication:** Document-level MinHash, sub-document exact match, paragraph-level deduplication, topic-model categorization with down-sampling of advertisements.

The pipeline produces a "much higher removal ratio than existing pipelines like CCNet, RefinedWeb, and RedPajama."

### Pretraining

- **Data:** 3.1T tokens, bilingual English and Chinese.
- **Sequence length:** 4096.
- **Regime:** Post-Chinchilla optimal -- overtrained on ~3x the compute-optimal token count.

### Supervised Fine-Tuning (SFT)

**Core philosophy:** "Quality is All You Need" -- fewer than 10K multi-turn instruction-response dialog pairs, each handcrafted and polished over multiple iterations from user feedback. This aligns with LIMA (Zhou et al., 2023) and explicitly deviates from FLAN and UltraChat.

**Hyperparameters:**
- **Loss:** Next-word prediction, computed only on responses (not system/user tokens).
- **Optimizer:** AdamW (beta_1=0.9, beta_2=0.999, eps=1e-8).
- **Sequence length:** 4096. **Batch size:** 64. **Training steps:** 300.
- **Learning rate:** Constant 1e-5. **Weight decay:** 0.1. **Gradient clipping:** 1.0.
- **NEFTune noise scale:** 45 for Yi-34B-Chat, 5 for Yi-6B-Chat.
- **Format:** ChatML-style (OpenAI, 2023).

**Data construction techniques:**
1. Compound instructions progressively evolved for complexity (inspired by WizardLM).
2. Introduction-body-conclusion response format with bullet-point bodies (extended from LIMA).
3. CoT formatting uses "Step-Back" pattern (Zheng et al., 2023).
4. Hallucination reduction: ensure responses do not exceed model's knowledge.
5. Repetition reduction: rewrite repetitive turns.
6. Data mixture grid search over {1, 1/2, 1/4, 1/8, 1/16, 1/32, 1/64} proportions per ability.

### Long-Context Extension (200K)

**Method -- two lightweight phases:**

**Phase 1: Continual pretraining.** Full-attention model (no sparse or sliding window attention) trained on 5B tokens with 4M batch size (~100 optimization steps). Data mixture: original pretraining data + length-upsampled long sequences (mostly books) + multi-document QA with recitation. Key finding: "Only 1-2B tokens is enough for the model to converge to low loss on 4K-200K length."

**Phase 2: Supervised fine-tuning.** Short-context SFT data mixed with synthetic long-context document QA. Before answering, the model recites or paraphrases the original paragraph to encourage retrieval behavior and discourage hallucination.

**Engineering:** Computation-communication overlapping, sequence parallelism, communication compression. Full attention is maintained even at 200K input -- no architectural modifications.

### Depth Upscaling (Yi-9B)

Yi-6B (32 layers) is upscaled to Yi-9B (48 layers) by duplicating middle layers 12-28 (16 layers), following Kim et al. (2023) -- SOLAR. The duplicated layers have cosine similarity between inputs and outputs approaching 1.0, causing minimal performance degradation at initialization (Table 8: MMLU drops only from 63.2 to 63.0 without any further training).

After continual pretraining on ~800B tokens (70% recently collected, enhanced code coverage in final stage) with constant learning rate 3e-5 and gradually increasing batch size from 4M tokens, Yi-9B achieves large gains over Yi-6B.

### Vision-Language Model (Yi-VL)

Yi-VL follows the LLaVA architecture: a vision encoder (CLIP ViT-H/14, initialized from OpenCLIP, image resolution 448x448) projects image features into the LLM's embedding space via a projector. Three-stage training: (1) 100M image-text pairs for vision-language alignment (LAION-400M subset), (2) 25M image-text pairs for visual knowledge acquisition, (3) 1M multi-modal instruction data for SFT.

### Experimental Setup

**Base model evaluation:** Greedy decoding, no post-processing.
- Commonsense Reasoning: PIQA, SIQA, HellaSwag, WinoGrande, ARC, OpenBookQA (0-shot); CommonsenseQA (7-shot).
- Reading Comprehension: SQuAD, QuAC, BoolQ (0-shot average).
- Math: GSM8K (8-shot), MATH (4-shot), pass@1, no CoT or majority voting.
- Code: HumanEval, MBPP (average pass@1).
- Aggregated: MMLU (5-shot), CMMLU (5-shot), Gaokao-Bench (5-shot), BBH (3-shot).

**Chat model evaluation:** Both 0-shot (with CoT for GSM8K and BBH) and few-shot settings. Human evaluation via AlpacaEval, LMSys Chatbot Arena, and SuperClue (Chinese).

### Key Results

**Base models (Table 2):**

| Model | Size | MMLU | BBH | C-Eval | CMMLU | Gaokao | CR | RC | Code | Math |
|---|---|---|---|---|---|---|---|---|---|---|
| GPT-4 | -- | 83.0 | 86.7 | 69.9 | 71.0 | 72.3 | 89.3 | -- | 65.3 | 66.1 |
| GPT-3.5 | -- | 69.1 | 70.1 | 52.5 | 55.5 | 51.1 | 83.1 | -- | 54.8 | 35.6 |
| LLaMA 2 | 70B | 69.7 | 64.9 | 50.1 | 53.3 | 23.3 | 72.7 | 72.3 | 38.4 | 35.2 |
| Qwen | 14B | 66.7 | 53.4 | 72.1 | 71.0 | 62.5 | 74.2 | 72.5 | 40.6 | 43.1 |
| Falcon | 180B | 70.4 | 54.0 | 57.8 | 58.0 | 59.0 | 74.4 | -- | -- | -- |
| **Yi** | **6B** | **63.2** | **42.8** | **72.0** | **75.5** | **72.2** | **72.2** | **68.7** | **21.1** | **18.6** |
| **Yi** | **34B** | **76.3** | **54.3** | **81.4** | **83.7** | **82.8** | **80.7** | **76.5** | **32.1** | **40.8** |

- Yi-34B outperforms LLaMA 2 70B on MMLU by +6.6 points (76.3 vs 69.7) despite being half the size.
- Yi-34B substantially outperforms all open models on Chinese benchmarks (C-Eval 81.4, CMMLU 83.7).
- Yi-6B outperforms LLaMA 2 70B on Chinese benchmarks (CMMLU 75.5 vs 53.3).

**Math and code (Table 3):**

| Model | Size | GSM8K | MATH | HumanEval | MBPP |
|---|---|---|---|---|---|
| LLaMA 2 | 70B | 56.8 | 13.5 | 31.7 | 45.0 |
| **Yi** | **34B** | **67.2** | **14.4** | **23.2** | **41.0** |
| **Yi** | **6B** | **32.5** | **4.6** | **15.9** | **26.3** |

- Yi-34B exceeds LLaMA 2 70B on GSM8K (67.2 vs 56.8) but lags on HumanEval (23.2 vs 31.7).

**Chat models (Table 4, selected):**

| Model | Size | MMLU 5-shot | CMMLU 5-shot | GSM8K 4-shot | TruthfulQA |
|---|---|---|---|---|---|
| Qwen-Chat | 14B | 65.0 | 70.6 | 61.2 | 52.5 |
| LLaMA2-Chat | 70B | 59.9 | 41.0 | 58.7 | 54.0 |
| **Yi-Chat** | **6B** | **61.0** | **74.7** | **44.9** | **50.6** |
| **Yi-Chat** | **34B** | **73.5** | **81.3** | **76.0** | **62.4** |

**Quantization impact:** Yi-34B-Chat MMLU 5-shot: 73.5 (bf16) vs 73.7 (8-bit GPTQ) vs 72.4 (4-bit AWQ). Less than 1% accuracy drop.

**Human evaluation (Table 5):**

| Model | Size | AlpacaEval | Chatbot Arena Elo | SuperClue |
|---|---|---|---|---|
| GPT-4-Turbo | -- | 97.7 | 1243 | 89.79 |
| GPT-3.5-Turbo | -- | 89.37 | 1117 | 59.39 |
| LLaMA2-Chat | 70B | 92.66 | 1077 | -- |
| **Yi-Chat** | **34B** | **94.08** | **1110** | **71.87** |

- Yi-34B-Chat surpasses LLaMA 2-Chat 70B on AlpacaEval (94.08 vs 92.66) and on SuperClue exceeds GPT-3.5-Turbo (71.87 vs 59.39).

**200K context -- MMLU degradation (Table 6):**

| Model | MMLU 4K | MMLU 200K | Delta |
|---|---|---|---|
| Yi-6B | 63.24 | 61.73 | -1.51 |
| Yi-34B | 76.32 | 75.56 | -0.76 |

**Depth upscaling -- Yi-9B (Table 8):**

| Model | MMLU | GSM8K | MATH | HumanEval | MBPP |
|---|---|---|---|---|---|
| Yi-6B | 63.2 | 32.5 | 4.6 | 15.9 | 26.3 |
| Yi-9B Init (no training) | 63.0 | 31.3 | 4.1 | 12.8 | 25.8 |
| Yi-9B (800B tokens) | **68.4** | **52.3** | **15.9** | **39.0** | **54.4** |

**SFT data scaling (Figure 5):** Yi data shows a clear scaling advantage over UltraChat on Alpaca Eval 2.0. At ~10^4 data points, Yi data already approaches GPT-3.5 performance, while UltraChat requires ~10^6.

---

## Limitations and Failure Modes

The paper does not include a dedicated limitations section but acknowledges the following throughout:

1. **Math and coding gaps.** "There are still discernible disparities between our model and existing open-source and close-source models, particularly in tasks related to mathematics and coding" (Section 6.1.1). Yi-34B HumanEval (23.2) lags behind LLaMA 2 70B (31.7) and GPT-3.5 (48.1). The authors attribute this to deliberately not incorporating extensive math/code content in pretraining.

2. **Gap with GPT-4.** "Open-source LLMs still lag behind the performance of GPT-4 and GPT-3.5 on various benchmarks" (Section 6.1.2). The gap is especially large on BBH (54.3 vs 86.7), code (32.1 vs 65.3), and math (40.8 vs 66.1).

3. **Smaller models require more SFT data.** "Yi-6B-Chat does not exhibit strong mathematical capabilities (on both GSM8K and the Hungarian mathematics exam). We speculate that smaller models may require more data to activate their corresponding abilities during the SFT stage" (Section 6.2.1).

4. **Data cleaning pipeline is imperfect.** "Since data cleaning is a very complicated pipeline and it is extremely difficult to conduct extensive grid-search styled optimizations, our current solution may still have room for improvements" (Section 8).

5. **Benchmark evaluation limitations.** The authors invoke Goodhart's principle and note that differences in prompts, post-processing, and sampling "may potentially induce significant variations in the outcomes" (Section 6.2.1).

6. **Internal evaluation bias.** "Our internal evaluation results may be unfair to other models, making it difficult to accurately represent the true capability level of our model" (Section 6.2.2). The paper therefore reports only external evaluation results.

7. **No explicit safety evaluation.** Beyond a brief description of the RAISE safety engine and TruthfulQA scores, the paper provides no systematic safety evaluation (no ToxiGen, no red-teaming, no adversarial testing results).

---

## Conclusions

### Contributions

1. **Data quality engineering as the primary performance driver.** Yi demonstrates that a standard LLaMA-style architecture trained on 3.1T carefully curated bilingual tokens can outperform larger models (Yi-34B at 76.3 MMLU surpasses LLaMA 2 70B at 69.7), attributing gains primarily to data pipeline design rather than architectural novelty (Table 2, Section 6.1.2).

2. **Efficient bilingual open-weight models.** Yi-34B achieves state-of-the-art Chinese benchmark scores (C-Eval 81.4, CMMLU 83.7) while maintaining competitive English performance, demonstrating that a bilingual data mixture need not compromise either language (Table 2).

3. **Quality-first SFT with fewer than 10K examples.** The paper validates the LIMA hypothesis at scale: fewer than 10K hand-curated instruction examples, iterated with user feedback, outperform million-scale instruction datasets on Alpaca Eval 2.0 (Figure 5, Section 3.2).

4. **Lightweight 200K context extension.** Full-attention 200K context achieved through RoPE ABF and only 5B tokens of continual pretraining, with less than 1 point MMLU degradation for Yi-34B (Table 6, Section 7.1). No architectural modifications (sparse attention, sliding windows) required.

5. **Depth upscaling as a cost-effective scaling strategy.** Layer duplication from Yi-6B to Yi-9B with 800B tokens of continual pretraining produces large gains on code and math (HumanEval 15.9->39.0, GSM8K 32.5->52.3) without training from scratch (Table 8, Section 7.3).

6. **Consumer-hardware deployability.** After int4 quantization, Yi-34B-Chat fits on a single RTX 4090 (24GB) with less than 1% accuracy drop on MMLU/CMMLU (Table 4, Section 4.3).

### Implications

1. **Over-training beyond Chinchilla-optimal pays off for deployment.** Training on 3.1T tokens for a 34B model (~3x compute-optimal) delivers consistently better downstream performance. The model "has not saturated at 3.1T" (Section 8). This supports the inference-aware scaling perspective of Sardana & Frankle (2023) over strict compute-optimal training.

2. **Data pipeline details matter more than architecture at current scales.** The paper positions data engineering as the bottleneck for open-model performance, suggesting that diminishing returns from architectural innovations may redirect the field toward data quality research. This is a strong claim that requires validation across different model families.

3. **Long-context capability may be intrinsic to pretrained models.** The authors argue that "the base model already has the capability to model longer than 4K dependency" and that continual pretraining merely "releases" this capability (Section 7.1). This is speculative and merits further investigation.

---

## Key Claims

1. **Yi-34B outperforms LLaMA 2 70B on MMLU by +6.6 points (76.3 vs 69.7) at half the parameter count.** Evidence: Table 2, Section 6.1.1. Status: **supported**.

2. **Yi-34B achieves 81.4 on C-Eval and 83.7 on CMMLU, substantially outperforming all open models on Chinese benchmarks.** Evidence: Table 2. Status: **supported**.

3. **Context extension to 200K via RoPE ABF causes less than 1 MMLU point degradation for Yi-34B (76.32 to 75.56).** Needle-in-a-Haystack shows near-perfect retrieval across all depths and lengths (Figure 6). Evidence: Table 6, Figure 6, Section 7.1. Status: **supported**.

4. **Fewer than 10K curated SFT examples outperform million-scale instruction datasets (UltraChat) on Alpaca Eval 2.0.** Evidence: Figure 5, Section 3.2. Status: **supported**.

5. **4-bit quantization reduces memory requirements with less than 1% accuracy drop on MMLU/CMMLU benchmarks.** Yi-34B-Chat MMLU 5-shot: 73.5 (bf16) vs 72.4 (4-bit AWQ). Evidence: Table 4. Status: **supported**.

6. **Depth upscaling from Yi-6B (32 layers) to Yi-9B (48 layers) with 800B tokens of continual pretraining yields GSM8K +19.8 (32.5 to 52.3) and HumanEval +23.1 (15.9 to 39.0).** Evidence: Table 8, Section 7.3. Status: **supported**.

7. **Yi-34B-Chat achieves 94.08 on AlpacaEval, surpassing LLaMA 2-Chat 70B (92.66).** Chatbot Arena Elo of 1110, close to GPT-3.5-Turbo (1117). Evidence: Table 5, Section 6.2.2. Status: **supported**.

---

## Open Questions

1. **Scaling beyond 34B parameters.** The authors claim "reasoning capability is strongly correlated with model scale when the amount of pretraining data is fixed" (Section 8). Would a 70B+ Yi model with the same data quality pipeline achieve proportionally better reasoning? Not addressed.

2. **SFT data quantity for specialized domains.** The <10K SFT approach works for general chat, but can it generalize to domains requiring specialized knowledge where curated examples are expensive? The paper notes smaller models may "require more data to activate their corresponding abilities" (Section 6.2.1). Not addressed.

3. **Optimal deduplication strength.** Yi's aggressive pipeline has a "much higher removal ratio" than CCNet/RefinedWeb/RedPajama. What is the optimal deduplication strength, and does over-deduplication risk removing useful variation? Acknowledged as difficult to optimize (Section 8). Not addressed.

4. **Intrinsic long-context capability.** The claim that long-context capability is intrinsic to the 4K base model (Section 7.1) raises the question: does continual pretraining unlock existing capability or inject new capability? If intrinsic, why is 5B tokens of continual pretraining necessary at all? Not systematically validated.

5. **Safety evaluation.** The paper describes a RAISE safety engine but provides no systematic adversarial safety evaluation. How does Yi compare to models with documented safety pipelines (LLaMA 2-Chat, GPT-4) on red-teaming and toxicity benchmarks? Not addressed.

---

## Core References and Why They Are Referenced

### Architecture Foundations

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* The original Transformer architecture. Yi retains the decoder-only autoregressive structure.
- **Su et al. (2021)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* Provides RoPE, used with adjusted base frequency for 200K context extension.
- **Ainslie et al. (2023)** -- *GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints.* GQA applied to both Yi-6B and Yi-34B, unlike LLaMA 2 which restricts GQA to 70B only.
- **Shazeer (2020)** -- *GLU Variants Improve Transformer.* SwiGLU activation with reduced dimension (8h/3) to compensate for GQA parameter reduction.

### Direct Predecessors

- **Touvron et al. (2023a)** -- *LLaMA: Open and Efficient Foundation Language Models.* Architecture and code base that Yi builds upon.
- **Touvron et al. (2023b)** -- *Llama 2: Open Foundation and Fine-Tuned Chat Models.* Concurrent open-weight release; Yi extends GQA to smaller models and trains on more tokens (3.1T vs 2T).

### Scaling Laws and Training Methodology

- **Hoffmann et al. (2022)** -- *Training Compute-Optimal Large Language Models (Chinchilla).* Yi deliberately trains beyond Chinchilla-optimal, following the "post-Chinchilla" regime.
- **Sardana & Frankle (2023)** -- *Beyond Chinchilla-Optimal.* Inference-aware scaling laws that support Yi's over-training approach.

### Data Pipeline

- **Wenzek et al. (2020)** -- *CCNet.* Yi's language filtering and perplexity scoring built on the CCNet pipeline.
- **Penedo et al. (2023)** -- *The RefinedWeb Dataset for Falcon LLM.* Deduplication methodology that Yi extends with additional cascaded stages.

### Fine-Tuning Philosophy

- **Zhou et al. (2023)** -- *LIMA: Less Is More for Alignment.* The philosophical anchor for Yi's <10K SFT approach.
- **Xu et al. (2023)** -- *WizardLM.* Compound instruction evolution strategy adopted for SFT data construction.

### Long-Context Extension

- **Xiong et al. (2023)** -- *Effective Long-Context Scaling of Foundation Models.* RoPE ABF method used for extending context to 200K.

### Depth Upscaling

- **Kim et al. (2023)** -- *SOLAR 10.7B: Scaling Large Language Models with Simple yet Effective Depth Up-Scaling.* Direct methodological basis for Yi's 6B-to-9B depth upscaling via layer duplication.

### Vision-Language

- **Liu et al. (2023a, 2023b)** -- *LLaVA.* Primary methodological inspiration for Yi-VL's architecture and three-stage training pipeline.
