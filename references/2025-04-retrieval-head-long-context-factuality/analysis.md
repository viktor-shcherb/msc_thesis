---
title: "Retrieval Head Mechanistically Explains Long-Context Factuality"
authors: "Wu, Wang, Xiao, Peng, Fu"
year: 2025
venue: "ICLR 2025"
paper_type: conference-paper
categories: ["mechanistic-interpretability", "attention-analysis", "long-context-evaluation"]
scope: ["retrieval head identification", "long-context factuality", "attention head specialization"]
benchmarks_used: ["niah", "mmlu", "gsm8k", "musique"]
models_introduced: []
models_evaluated: ["llama-2-7b", "llama-2-13b", "mistral-7b", "mixtral-8x7b", "yi-6b", "yi-34b", "qwen1.5-14b"]
key_claims:
  - id: C1
    claim: "A sparse set of retrieval heads (less than 5% of all attention heads) exists universally across model families, scales, and finetuning types"
    evidence: "Figure 3, Section 3.1"
    status: supported
    scope: "4 model families (Llama-2, Yi, Qwen1.5, Mistral), 6B--34B and 8x7B MoE, base/chat/MoE variants"
    magnitude: "3--6% of attention heads have retrieval score > 0.1 across all 8 configurations"
  - id: C2
    claim: "Retrieval heads are intrinsic to base models and preserved through continued pretraining, chat finetuning, and sparse upcycling"
    evidence: "Figure 5, Figure 6, Section 3.3"
    status: supported
    scope: "3 within-family comparisons (Llama-2, Qwen1.5, Mistral), Pearson correlation on retrieval score distributions"
    magnitude: "within-family Pearson r > 0.8 (Llama: 0.84, Qwen: 0.87, Mistral: 0.91); cross-family r < 0.1"
  - id: C3
    claim: "Retrieval heads are dynamically activated: the strongest heads always activate regardless of context, while weaker heads activate on specific tokens and contexts"
    evidence: "Figure 4, Section 3.2"
    status: supported
    scope: "Llama-2-7B-80K and Yi-6B-200K, ~600 NIAH instances per model"
    magnitude: "12 always-active heads (Llama-2-7B-80K), 36 always-active heads (Yi-6B-200K) with activation frequency = 1.0"
  - id: C4
    claim: "Masking retrieval heads causally degrades Needle-in-a-Haystack performance and produces hallucination, while masking equal numbers of random non-retrieval heads has much weaker effect"
    evidence: "Figure 1, Figure 7, Section 4.1"
    status: supported
    scope: "Llama-2-7B-80K, Yi-6B-200K, Mixtral-8x7B-v0.1; progressive masking K = 2 to 100 heads"
    magnitude: "all models drop below 50 NIAH score at K=50 (~5% of heads); random masking stays at 80%+"
  - id: C5
    claim: "Retrieval heads significantly influence extractive QA, with masking 100 retrieval heads reducing F1 from 56.7 to 32.3 while masking 100 random heads only reduces F1 to 55.4"
    evidence: "Figure 8, Section 4.2"
    status: supported
    scope: "Mistral-7B-Instruct-v0.2 only, synthesized news-based extractive QA dataset"
    magnitude: "F1 drop of 24.4 points (retrieval heads) vs 1.3 points (random heads) at K=100"
  - id: C6
    claim: "Chain-of-thought reasoning heavily relies on retrieval heads because the model must refer back to input information, while answer-only prompting using intrinsic knowledge is minimally affected"
    evidence: "Figure 10, Figure 11, Section 4.3"
    status: supported
    scope: "Mistral-7B-Instruct-v0.2 only, GSM8K/MMLU/MuSiQue with and without CoT"
    magnitude: "GSM8K CoT: 45.1 -> 2.0 (mask 100 retrieval); MMLU CoT: 43.6 -> 24.8; without CoT: minimal change"
  - id: C7
    claim: "When retrieval fails, retrieval heads predominantly attend to attention sink tokens (initial tokens), linking retrieval failure to the attention sink phenomenon"
    evidence: "Figure 9, Section 4.1"
    status: supported
    scope: "Mistral-7B-Instruct-v0.2, observed during NIAH hallucination cases"
    magnitude: "qualitative observation linking two phenomena; no numerical measure of sink attention proportion"
cross_references:
  - target: 2022-03-in-context-learning-induction-heads
    type: extends
    detail: "Extends the concept of specialized attention heads from induction heads (pattern matching for in-context learning) to retrieval heads (conditional copy-paste from arbitrary context positions)"
  - target: 2024-05-attention-sinks-streaming
    type: complementary
    detail: "When retrieval heads fail to find relevant information, they attend to attention sink tokens; connects the attention sink phenomenon to retrieval failure and hallucination (Section 4.1, Figure 9)"
  - target: 2023-11-needle-in-a-haystack
    type: uses-benchmark
    detail: "Needle-in-a-Haystack is the core evaluation methodology for detecting and validating retrieval heads across ~600 test instances per model"
  - target: 2023-07-llama-2-open-foundation-chat
    type: evaluates
    detail: "Llama-2-7B and Llama-2-13B (including 80K and 64K extended variants) are primary models for retrieval head detection and property analysis"
  - target: 2021-11-ff-layers-key-value-memories
    type: complementary
    detail: "Builds on the distinction that FFN layers store knowledge while attention layers implement algorithms; retrieval heads specifically implement conditional copy-paste"
  - target: 2022-12-chain-of-thought-prompting
    type: complementary
    detail: "CoT reasoning is shown to heavily depend on retrieval heads because the model needs to refer back to input information during multi-step reasoning (Section 4.3)"
  - target: 2021-12-transformer-circuits-framework
    type: complementary
    detail: "Extends the mechanistic interpretability program by identifying a specific subnet (retrieval heads) implementing the conditional retrieval algorithm"
  - target: 2023-10-mistral-7b
    type: evaluates
    detail: "Mistral 7B is used alongside Llama 2 and Yi models for cross-family retrieval head analysis"
  - target: 2024-03-yi-open-foundation-models
    type: evaluates
    detail: "Yi-6B and Yi-34B used for retrieval head discovery and cross-family analysis of retrieval head properties"
open_questions:
  - question: "What other algorithms and functionalities are implemented by the remaining ~95% of non-retrieval attention heads?"
    addressed_by: null
  - question: "Can KV cache be radically pruned to retain only retrieval heads' KV states while maintaining factuality for long-context tasks?"
    addressed_by: null
  - question: "Why do no linear attention or SSM architectures pass the Needle-in-a-Haystack test, and is full attention necessary for retrieval heads to function?"
    addressed_by: null
  - question: "What is the detailed mechanism by which retrieval heads support chain-of-thought reasoning beyond simple input-to-output copy-paste?"
    addressed_by: null
---

# Retrieval Head Mechanistically Explains Long-Context Factuality

**Authors:** Wenhao Wu (Peking University), Yizhong Wang (University of Washington), Guangxuan Xiao (MIT), Hao Peng (UIUC), Yao Fu (University of Edinburgh)
**Date:** April 2025, ICLR 2025 Oral (arXiv:2404.15574)

---

## Core Research Problem

Despite progress in long-context language models, it remains unclear how transformer-based LLMs internally retrieve relevant information from arbitrary positions within long input. The Needle-in-a-Haystack test (Kamradt, 2023) demonstrates that models can locate and reproduce a short sentence embedded at any depth in a long context, but the internal mechanism enabling this behavior has not been identified. Prior work on specialized attention heads -- CopyNet (Gu et al., 2016), which implements single-head copy-paste in RNNs, and Induction Heads (Olsson et al., 2022), which implement implicit program induction for in-context learning -- suggests that retrieval may also be localized to specific heads, but this has not been verified empirically for long-context information retrieval.

The gap is practically consequential because understanding the retrieval mechanism has direct implications for **KV cache compression** (which could inadvertently destroy retrieval capability), **hallucination diagnosis** (understanding when and why models fabricate instead of faithfully reporting), and the design of **efficient attention mechanisms**. The core challenge: **what internal mechanism enables long-context language models to retrieve information from arbitrary positions, and what happens mechanistically when this capability fails?**

---

## Problem Solutions

The paper discovers **retrieval heads** -- a sparse set of attention heads that implement a conditional copy-paste algorithm, redirecting information from the input to the output. The solution rests on three components:

1. **A retrieval score metric** that quantifies each attention head's copy-paste frequency during Needle-in-a-Haystack decoding, enabling systematic identification of retrieval heads across models (Section 2, Equation 1).

2. **Large-scale empirical characterization** across 4 model families (Llama-2, Yi, Qwen1.5, Mistral), 6 scales (6B to 34B and 8x7B MoE), and 3 finetuning types (continued pretraining, SFT+RLHF, sparse upcycling), establishing that retrieval heads are universal, sparse (<5% of heads), intrinsic to base models, and causally necessary for factual retrieval (Sections 3--4).

3. **Causal masking experiments** demonstrating that removing retrieval heads causes hallucination while removing equal numbers of non-retrieval heads has minimal effect, and that chain-of-thought reasoning -- but not intrinsic-knowledge tasks -- depends on retrieval heads (Sections 4.1--4.3).

---

## Approach Details

### Method

The **retrieval score** measures the frequency of a head's copy-paste operations during autoregressive decoding. Given a question **q** with answer **k** (the needle) inserted in context **x** (the haystack), during greedy decoding the current generated token is *w* and the attention scores of head *h* are **a** in R^|**x**|. Head *h* is said to copy-paste a token if: (1) *w* is a token within the needle **k**, and (2) x_j = *w* where j = arg max(**a**) and j is within the needle's index range i_x (the most-attended input token is the same token as the one being generated, located within the needle). Let **g_h** be the set of all tokens copy-pasted by head *h*:

> Retrieval score for head *h* = |**g_h** intersection **k**| / |**k**|

This is a token-level recall rate: a score of 0.9 on a 10-token needle means the head copy-pasted 9 of the 10 tokens (Equation 1, Section 2).

### Key Technical Components

**Detection algorithm.** For each model, three unique (q, k, x) tuples are compiled, each with a semantically irrelevant needle that cannot be answered from the model's internal knowledge (verified by manual inspection). For each tuple, the NIAH test is run on 20 lengths uniformly sampled from 1K--50K tokens, with the needle inserted at 10 uniformly spaced depths. This yields ~600 test instances per model. The retrieval score is averaged across all instances. The authors note this scale gives stable outputs as scores converge after just a few samples. The threshold for classifying a head as a retrieval head is set at **0.1** -- the head must copy-paste at least 10% of needle tokens on average (Section 2, Figure 3).

**Activation frequency** complements the retrieval score. While the retrieval score measures the average fraction of tokens retrieved, activation frequency measures the fraction of test instances where a head is activated on at least one token. A head with high activation frequency but low retrieval score is **context-sensitive** (activated often but on few tokens per instance). A head with both metrics high is a **strong, context-insensitive retrieval head** (Section 3.2, Figure 4).

**Models examined.** The study covers 4 base models and their variants (Table 1, Section 2):

| Base Model | Variant | Variation Type |
|---|---|---|
| Llama-2-7B | Llama-2-7B-80K | Length extension via continued pretraining |
| | Llama-2-13B-64K | Model scaling and length extension |
| Mistral-7B-v0.2 | Mistral-7B-Instruct-v0.2 | SFT and RLHF |
| | Mixtral-8x7B-v0.1 | Sparse upcycling to Mixture of Experts |
| Yi-6B | Yi-6B-200K | Length extension via continued pretraining |
| | Yi-34B-200K | Model scaling and length extension |
| Qwen1.5-14B | Qwen1.5-14B-Chat | SFT and RLHF |

### Experimental Setup

**Property analysis (Sections 3.1--3.3):** All models in Table 1 are used to demonstrate universality, sparsity, dynamic activation, and intrinsic nature of retrieval heads. The retrieval score distribution is computed for each model across ~600 NIAH instances (20 lengths x 10 depths x 3 samples).

**Downstream task evaluation (Sections 4.1--4.3):** Mistral-7B-Instruct-v0.2 is the primary model (32K context). Head masking experiments progressively mask K = {2, 5, 10, 15, 20, 30, 50, 100} heads, comparing retrieval heads (sorted by retrieval score) versus random non-retrieval heads.

- **Needle-in-a-Haystack:** An additional set of needle tests distinct from the detection set (Section 4.1). Multiple models tested for masking: Llama-2-7B-80K, Yi-6B-200K, Mixtral-8x7B-v0.1 (Figure 7).
- **Extractive QA:** Synthesized from up-to-date news articles with GPT-4-generated QA pairs, designed so the knowledge does not exist in the model's internal knowledge. Evaluated on Mistral-7B-Instruct-v0.2 only (Section 4.2).
- **Chain-of-thought reasoning:** MMLU, MuSiQue, and GSM8K, tested with and without CoT prompting on Mistral-7B-Instruct-v0.2 only (Section 4.3).

**Reproducibility:** Code available at https://github.com/nightdessert/Retrieval_Head. No variance estimates or multiple-seed results are reported. Downstream evaluations use a single model (Mistral-7B-Instruct-v0.2) (limited evidence for downstream claims). The extractive QA dataset construction details are provided (news articles + GPT-4 QA generation) but the dataset itself is not publicly released in the paper.

### Key Results

**Retrieval heads are universal and sparse (Figure 3, Section 3.1).** Across all 8 model configurations, 3--6% of attention heads have a retrieval score > 0.1:

| Model | Architecture | Score = 0 | Score 0--0.1 | Score 0.1--0.5 | Score 0.5--1 |
|---|---|---|---|---|---|
| Llama-2-7B-80K | 32 x 32 heads | 70.2% | 26.5% | 2.6% | 0.6% |
| Yi-6B-200K | 32 x 32 heads | 50.7% | 43.7% | 4.9% | 0.8% |
| Qwen1.5-14B | 40 x 40 heads | 53.5% | 42.8% | 3.2% | 0.6% |
| Mistral-7B-v0.2 | 32 x 32 heads | 65.2% | 30.8% | 3.7% | 0.5% |
| Llama-2-13B-64K | 40 x 40 heads | 73.2% | 24.8% | 1.7% | 0.4% |
| Yi-34B-200K | 60 x 56 heads | 44.8% | 51.8% | 3.1% | 0.4% |
| Qwen1.5-14B-Chat | 40 x 40 heads | 71.1% | 24.6% | 4.2% | 0.1% |
| Mixtral-8x7B-v0.1 | 32 x 32 heads | 57.6% | 36.2% | 5.5% | 0.7% |

- Despite large differences in total head counts and architecture, the fraction of retrieval heads (score > 0.1) stays within the same 3--6% interval across all models (tested across 4 families and 8 configurations -- strong evidence for universality).

**Retrieval heads are intrinsic and preserved across model derivations (Figures 5, 6, Section 3.3).** The Pearson correlation of retrieval score distributions between base models and their variants exceeds 0.8 within families (Llama-2-7B vs. Llama-2-7B-80K: 0.84; Qwen1.5-14B vs. Chat: 0.87; Mistral-7B-v0.2 vs. Mixtral-8x7B: 0.91). Cross-family correlations are near zero (values from Figure 6: 0.00087, -0.022, -0.021), reflecting distinct pretraining recipes. Continued pretraining for context extension, chat finetuning, and sparse upcycling all preserve the same set of retrieval heads (3 within-family pairs tested -- moderate evidence).

**Retrieval heads are dynamically activated (Figure 4, Section 3.2).** Llama-2-7B-80K has **12** strongest retrieval heads that are always activated (activation frequency = 1.0) under all tested contexts. Yi-6B-200K has **36** such heads. Weaker retrieval heads activate only on specific tokens and contexts, collectively covering different pieces of the target information. The gap between activation frequency and retrieval score reveals context-sensitivity: heads with high activation frequency but low retrieval score are activated in many contexts but only on certain tokens.

**Masking retrieval heads causally degrades NIAH (Figure 7, Section 4.1).** Masking the top K retrieval heads progressively degrades Needle-in-a-Haystack accuracy for all tested models (Llama-2-7B-80K, Yi-6B-200K, Mixtral-8x7B-v0.1). When K reaches 50 (~5% of all heads), all models' scores drop below 50. Masking equal numbers of random non-retrieval heads causes much weaker degradation (scores remain at 80%+). Three error types emerge with increasing masking (Section 4.1, Figure 9):

1. **Incomplete retrieval** -- retrieval heads capture only partial information (appears first, when heads of score > 0.4 are masked). Each retrieval head "holds a small piece of the needle."
2. **Hallucination** -- model generates fluent but unfactual content; retrieval heads attend to attention sink tokens (initial tokens) rather than the needle.
3. **Wrong extraction** -- model retrieves irrelevant content from the haystack.

**Extractive QA (Figure 8, Section 4.2, Mistral-7B-Instruct-v0.2):**

| Setting | F1 |
|---|---|
| No masking | 56.7 |
| Mask 50 retrieval heads | 47.5 |
| Mask 100 retrieval heads | 32.3 |
| Mask 50 random heads | 55.7 |
| Mask 100 random heads | 55.4 |

- Masking retrieval heads reduces ExtractQA F1 by 9.2 points (50 heads) and 24.4 points (100 heads), while masking random heads causes reductions of only 1.0 and 1.3 points (single model, single dataset -- limited evidence for generalization beyond this setting).

**Chain-of-thought reasoning depends on retrieval heads (Figure 10, Section 4.3, Mistral-7B-Instruct-v0.2).** With CoT prompting, masking retrieval heads severely degrades performance. Without CoT (answer-only), masking has minimal effect:

| Task | Metric | No Mask | Mask 100 Retrieval | Mask 100 Random |
|---|---|---|---|---|
| GSM8K (w/ CoT) | Acc | 45.1 | 2.0 | 21.3 |
| MMLU (w/ CoT) | Acc | 43.6 | 24.8 | 29.3 |
| MuSiQue (w/ CoT) | F1 | 14.2 | 9.9 | 11.3 |
| GSM8K (w/o CoT) | Acc | 1.8 | 2.5 | 2.3 |
| MMLU (w/o CoT) | Acc | 57.2 | 54.0 | 54.2 |
| MuSiQue (w/o CoT) | F1 | 16.0 | 14.9 | 12.5 |

- With CoT, masking retrieval heads causes the model to become "blind" to input information: it hallucinates or misreads problem descriptions during multi-step reasoning. For example, the model misreads "$22.50" as "$22" or loses track of numerical values in arithmetic chains (Figure 11). Without CoT, the model generates answers from intrinsic knowledge stored in FFN layers, making retrieval heads less relevant (Section 4.3). Tested on single model only (limited evidence for generalization).

### Connection to Attention Sinks

During hallucination (when the model fails to retrieve the needle), retrieval heads predominantly attend to the initial token of the input -- the attention sink (Xiao et al., 2023). This establishes a mechanistic link: **attention sinks serve as the default target when retrieval heads cannot locate the relevant information** (Section 4.1, Figure 9). The model produces fluent but unfactual output in this state, explaining why the attention sink phenomenon co-occurs with hallucination in long-context settings. This is a qualitative observation from case analysis, not a quantitative measurement of sink attention proportions.

### Implications for KV Cache Compression and Efficient Attention

Since only ~5% of attention heads are retrieval heads, the remaining ~95% of heads' KV cache could potentially be aggressively compressed or pruned without loss of retrieval capability. For Llama-2-7B at 100K context, the KV cache requires more than 50GB memory, while 2K context requires less than 1GB; selective pruning of non-retrieval heads' KV could significantly reduce deployment cost (Section 5). The paper also notes that no linear attention or SSM architecture passes the Needle-in-a-Haystack test, and that Mistral v0.1 (sliding window attention) failed NIAH while v0.2 (full attention) passed, providing evidence that **full attention over the complete KV cache is necessary for retrieval heads to function** (Section 5). Neither KV cache pruning nor the full-attention necessity claim is experimentally validated in this paper; both are discussed as implications for future work.

---

## Limitations and Failure Modes

- **Fixed threshold.** The retrieval head threshold of 0.1 is chosen empirically; sensitivity to this choice is not analyzed (Section 2).

- **Detection depends on NIAH.** The retrieval score is defined using the Needle-in-a-Haystack paradigm, which tests literal copy-paste. Whether retrieval heads also mediate more abstract retrieval (paraphrasing, inference from context) is not examined.

- **Downstream evaluation on one model only.** The causal masking experiments (Sections 4.1--4.3) use Mistral-7B-Instruct-v0.2 exclusively for extractive QA and CoT tasks. While property analysis covers multiple families, the downstream influence results are not verified across models.

- **Approximate numbers from figures.** The NIAH masking results (Figure 7) are presented as line charts without exact numerical values in the text, beyond the statement that all models drop below 50 at K=50.

- **No theoretical explanation.** The paper is purely empirical. No formal model is offered for why retrieval heads emerge, why their proportion is ~5%, or why they concentrate in specific layers.

- **KV cache compression not validated.** The suggestion that non-retrieval heads' KV cache can be pruned is discussed as future work but not experimentally verified (Section 5).

- **[Inferred] Short needles only.** The detection algorithm uses short needle sentences. Whether retrieval heads handle retrieval of longer, multi-paragraph information is not tested.

- **[Inferred] No variance estimates.** Single run per configuration is used throughout; no standard deviations or confidence intervals are reported, limiting assessment of result stability.

- **[Inferred] English-only evaluation.** All experiments use English text; generalizability to other languages is not examined.

#### Scope and Comparability

- **What was not tested:** Models above 34B dense (no 70B+ models); non-English contexts; abstractive or paraphrased retrieval tasks; models with linear attention, SSMs, or hybrid architectures (these are discussed qualitatively but not evaluated with the retrieval score framework). No evaluation of retrieval heads during fine-grained tasks like multi-hop reasoning where the "needle" spans multiple passages.

- **Comparability notes:** The paper's "retrieval score" metric is specific to literal token-level copy-paste and may not capture semantic retrieval, making direct comparison with other interpretability studies that define retrieval more broadly (e.g., probing for factual recall) difficult. The NIAH test uses short, semantically irrelevant needles, which differs from realistic retrieval scenarios where the target information may be paraphrased or distributed across multiple locations. The 0.1 threshold for classification as a retrieval head is paper-specific; other works may use different thresholds or continuous measures, complicating cross-study comparison. The downstream evaluations use Mistral-7B-Instruct-v0.2 with 32K context, while property analyses use various models at various context lengths (1K--200K), so downstream conclusions may not transfer to other model-context combinations.

---

## Conclusions

### Contributions

1. **Discovered retrieval heads as the mechanism for long-context information retrieval.** A sparse set of attention heads (<5%) implements a conditional copy-paste algorithm that redirects information from input to output. These heads are universal across 4 model families, 6 scales, and 3 finetuning types (Figure 3, Section 3.1).

2. **Established five key properties of retrieval heads.** They are universal, sparse, intrinsic (present in base models with Pearson r > 0.8 across derivations), dynamically activated (strongest heads always active, weaker heads context-dependent), and causally necessary for factual retrieval (Figures 3--7, Sections 3--4).

3. **Linked retrieval head failure to the attention sink phenomenon and hallucination.** When retrieval heads fail, they attend to attention sink tokens (initial positions) rather than relevant content, producing fluent but unfactual output (Figure 9, Section 4.1).

4. **Demonstrated retrieval heads' influence on extractive QA.** Masking 100 retrieval heads reduces F1 by 24.4 points, while masking 100 random heads reduces F1 by 1.3 points on Mistral-7B-Instruct-v0.2 (Figure 8, Section 4.2).

5. **Showed chain-of-thought reasoning depends on retrieval heads.** CoT-prompted tasks (GSM8K, MMLU, MuSiQue) are severely degraded by masking retrieval heads, while answer-only tasks relying on intrinsic knowledge are minimally affected (Figure 10, Section 4.3).

### Implications

1. **KV cache compression should preserve retrieval heads.** Since only ~5% of heads are retrieval heads, aggressive compression of non-retrieval heads' KV could reduce deployment cost without sacrificing factuality. The paper notes Llama-2-7B 100K context requires >50GB KV cache; retaining only retrieval heads' KV could yield substantial memory savings (Section 5). [Inference: not experimentally validated.]

2. **Full attention may be necessary for long-context retrieval.** No linear attention or SSM architecture passes NIAH; Mistral v0.1 with sliding window failed while v0.2 with full attention succeeded, suggesting retrieval heads require full KV cache access (Section 5). [Inference: formal proof or controlled experiment not provided.]

3. **Hallucination diagnosis may be possible via retrieval head monitoring.** Since hallucination correlates with retrieval heads attending to attention sinks rather than relevant content, monitoring retrieval head attention patterns could enable real-time hallucination detection. [Inference: not experimentally validated.]

4. **The CoT--retrieval relationship warrants deeper investigation.** The finding that multi-step reasoning depends on retrieval heads suggests that reasoning quality is bottlenecked by the model's ability to refer back to previously generated and input information, not just by its capacity for logical inference (Section 4.3). [Inference: the mechanistic link beyond "the model needs to read back" is not characterized.]

---

## Key Claims

1. **C1: Retrieval heads are universal and sparse.** Across all 8 model configurations (4 families, 6B--34B and 8x7B MoE, base and finetuned), 3--6% of attention heads have a retrieval score above 0.1. The ratio is consistent despite large differences in total head counts and architecture (Figure 3, Section 3.1). **Scope:** 4 model families, 6B--34B dense and 8x7B MoE. **Magnitude:** 3--6% of heads classified as retrieval heads. Status: **supported** (tested across 8 model configurations -- strong evidence for universality within the tested scale range).

2. **C2: Retrieval heads are intrinsic to base models.** Base models already contain retrieval heads as a consequence of large-scale pretraining. Continued pretraining (Llama-2-7B to 80K), chat finetuning (Qwen1.5-14B to Chat), and sparse upcycling (Mistral-7B to Mixtral-8x7B) all preserve the same retrieval heads. Within-family Pearson correlation exceeds 0.8 (Llama: 0.84, Qwen: 0.87, Mistral: 0.91); cross-family correlation is near zero (0.00087, -0.022, -0.021 from Figure 6) (Figure 5, Figure 6, Section 3.3). **Scope:** 3 within-family comparisons. **Magnitude:** Pearson r = 0.84--0.91 within families; r < 0.1 cross-family. Status: **supported** (3 distinct adaptation types tested -- moderate evidence).

3. **C3: Retrieval heads are dynamically activated.** The strongest retrieval heads (12 for Llama-2-7B-80K, 36 for Yi-6B-200K) have activation frequency 1.0 and are always active regardless of context. Weaker heads activate on specific tokens and contexts, collectively covering different parts of the target information. This explains partial retrieval: removing a subset of heads yields incomplete output as each head "holds a small piece of the needle" (Figure 4, Section 3.2). **Scope:** Llama-2-7B-80K and Yi-6B-200K. **Magnitude:** 12 and 36 always-active heads, respectively. Status: **supported** (2 models examined in detail -- moderate evidence).

4. **C4: Masking retrieval heads causes hallucination in NIAH.** Progressive masking of the top K retrieval heads degrades NIAH accuracy for all models (Llama-2-7B-80K, Yi-6B-200K, Mixtral-8x7B-v0.1). At K=50 (~5% of heads), all models score below 50. Masking equal numbers of random non-retrieval heads causes much smaller degradation, with scores remaining at 80%+ (Figure 7, Section 4.1). **Scope:** 3 models tested with progressive masking. **Magnitude:** below 50 NIAH score at K=50 vs 80%+ for random masking. Status: **supported** (3 models across 2 families -- moderate evidence).

5. **C5: Retrieval heads significantly influence extractive QA.** On Mistral-7B-Instruct-v0.2, masking 50 retrieval heads reduces F1 from 56.7 to 47.5 (drop of 9.2 points); masking 100 reduces to 32.3 (drop of 24.4 points). Masking 50 and 100 random heads yields F1 of 55.7 and 55.4, respectively (Figure 8, Section 4.2). **Scope:** Mistral-7B-Instruct-v0.2 only, synthesized news QA. **Magnitude:** F1 drop of 24.4 points (retrieval) vs 1.3 points (random) at K=100. Status: **supported** (single model, single dataset -- limited evidence for generalization).

6. **C6: CoT reasoning depends on retrieval heads.** With CoT prompting on Mistral-7B-Instruct-v0.2, masking 100 retrieval heads drops GSM8K accuracy from 45.1 to 2.0 and MMLU accuracy from 43.6 to 24.8. Without CoT, the same masking causes minimal change (GSM8K: 1.8 to 2.5; MMLU: 57.2 to 54.0). The model becomes "blind" to input information during reasoning when retrieval heads are masked (Figure 10, Figure 11, Section 4.3). **Scope:** Mistral-7B-Instruct-v0.2 only, 3 benchmarks. **Magnitude:** GSM8K CoT accuracy 45.1 to 2.0; MMLU CoT 43.6 to 24.8. Status: **supported** (single model, 3 tasks -- moderate evidence for the phenomenon, limited evidence for generalization).

7. **C7: Failed retrieval defaults to attention sinks.** When retrieval heads fail to locate the needle (either naturally or through masking), they predominantly attend to the initial token of the input -- the attention sink. This produces fluent but hallucinated output (Figure 9, Section 4.1). **Scope:** Observed during NIAH failure cases on Mistral-7B-Instruct-v0.2. **Magnitude:** qualitative observation (no quantitative measure of sink attention proportion). Status: **supported** (qualitative case analysis, not quantified).

---

## Open Questions

1. **What functionalities do the ~95% of non-retrieval attention heads implement?** The paper identifies retrieval as a function of <5% of heads but does not characterize the remainder. The authors suggest "there exist more algorithms and functionalities implemented by other types of attention heads to be discovered by future research" (Section 5). Not addressed.

2. **Can KV cache be pruned to retain only retrieval heads' KV without loss of factuality?** The paper estimates this could yield significant memory savings (>50GB to a fraction for Llama-2-7B at 100K context) but leaves experimental validation to future work (Section 5). Not addressed.

3. **Is full attention necessary for retrieval heads?** No linear attention, SSM, or hybrid architecture passes the NIAH test. Mistral v0.1 (sliding window) fails while v0.2 (full attention) succeeds. But a formal analysis of why retrieval heads require full KV cache access is absent (Section 5). Not addressed.

4. **What is the detailed relationship between retrieval heads and CoT reasoning?** The paper shows a strong empirical dependence but does not provide a mechanistic account of how retrieval heads participate in multi-step reasoning beyond simple copy-paste from input to output (Section 4.3). Not addressed.

---

## Core References and Why They Are Referenced

### Mechanistic Interpretability Foundations

- **Olsson et al. (2022)** -- *In-Context Learning and Induction Heads.* Induction heads implement implicit program induction for in-context learning by searching for repeated patterns. The retrieval head concept extends this to conditional information retrieval from arbitrary context positions -- a related but distinct algorithm. The paper draws a direct analogy: "just like induction heads are accountable for in-context learning, there might exist special heads that are accountable for information retrieval" (Section 1).

- **Gu et al. (2016)** -- *Incorporating Copying Mechanism in Sequence-to-Sequence Learning (CopyNet).* CopyNet is a single-layer, single-head attention mechanism from the RNN era that copy-pastes tokens from input to output. Retrieval heads are the multi-layer, multi-head analogue in modern transformers (Section 1).

- **Bricken et al. (2023)** -- *Towards Monosemanticity.* Referenced for the broader mechanistic interpretability program. The retrieval head discovery is positioned as pinpointing "a particular subnet implementing the conditional retrieval algorithm" (Section 1).

- **Geva et al. (2020)** -- *Transformer Feed-Forward Layers Are Key-Value Memories.* Establishes the FFN-as-knowledge-storage view. The paper builds on the complementary distinction: FFN layers store knowledge, attention layers implement algorithms, and retrieval heads specifically implement the copy-paste retrieval algorithm (Section 5).

### Attention Mechanism Analysis

- **Xiao et al. (2023)** -- *Efficient Streaming Language Models with Attention Sinks.* The attention sink phenomenon directly connects to retrieval head failure: when retrieval heads cannot find the needle, they attend to attention sink tokens (initial positions) instead. The paper notes that context compression methods that remove KV states of retrieval heads will fail to maintain factuality (Section 4.1, Section 1).

### Models Used in Evaluation

- **Touvron et al. (2023)** -- *Llama 2: Open Foundation and Fine-Tuned Chat Models.* Provides Llama-2-7B and Llama-2-13B as base models, with Fu et al. (2024) providing their 80K and 64K extended variants.

- **Jiang et al. (2023)** -- *Mistral 7B.* Provides Mistral-7B-v0.2 as the primary model for downstream evaluation. Also notable for the comparison between v0.1 (sliding window, fails NIAH) and v0.2 (full attention, passes NIAH).

- **Jiang et al. (2024)** -- *Mixtral of Experts.* Provides Mixtral-8x7B-v0.1 (derived from Mistral-7B via sparse upcycling) to study retrieval heads in MoE architectures.

- **Young et al. (2024)** -- *Yi: Open Foundation Models by 01.AI.* Provides Yi-6B and Yi-34B models and their 200K extended variants.

- **Bai et al. (2023)** -- *Qwen Technical Report.* Provides Qwen1.5-14B and its Chat variant.

### Evaluation Benchmarks

- **Kamradt (2023)** -- *Needle in a Haystack.* The NIAH test is the foundational evaluation for both detecting retrieval heads and validating their causal role. ~600 instances per model used for detection.

- **Wei et al. (2022)** -- *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models.* CoT prompting is used to demonstrate that multi-step reasoning depends on retrieval heads, unlike answer-only generation (Section 4.3).

- **Hendrycks et al. (2020)** -- *Measuring Massive Multitask Language Understanding (MMLU).* Used in Section 4.3 to test retrieval head influence on knowledge-based QA with and without CoT.

- **Cobbe et al. (2021)** -- *Training Verifiers to Solve Math Word Problems (GSM8K).* Used in Section 4.3 to test retrieval head influence on math reasoning with and without CoT.

### Efficient Attention and KV Cache

- **Ge et al. (2023)** -- *Model Tells You What to Discard: Adaptive KV Cache Compression for LLMs.* Referenced as KV cache compression work that should consider retrieval head preservation (Section 1).

- **Kang et al. (2024)** -- *GEAR: An Efficient KV Cache Compression Recipe for Near-Lossless Generative Inference of LLM.* Another KV compression method that the retrieval head framework could inform (Section 1).

### Alternative Architectures

- **Gu and Dao (2023)** -- *Mamba: Linear-Time Sequence Modeling with Selective State Spaces.* Referenced when discussing that no SSM architecture passes the NIAH test, providing indirect evidence for the necessity of full attention for retrieval heads (Section 5).

- **De et al. (2024)** -- *Griffin: Mixing Gated Linear Recurrences with Local Attention.* Referenced as a hybrid architecture that does not pass the NIAH test (Section 5).
