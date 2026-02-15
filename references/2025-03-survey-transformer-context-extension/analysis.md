---
title: "A Survey on Transformer Context Extension: Approaches and Evaluation"
authors: "Liu, Yu, Xu, Li, Zhu"
year: 2025
venue: "arXiv 2025"
paper_type: preprint
categories: ["context-extension", "position-encoding", "attention-efficiency", "benchmarking", "long-context-evaluation"]
scope: ["Transformer-based LLMs", "long context processing", "positional encoding for context extension", "context compression methods", "retrieval-augmented long context", "attention pattern modifications", "long context evaluation benchmarks and metrics"]
benchmarks_used: []
models_introduced: []
models_evaluated: []
key_claims:
  - id: C1
    claim: "Existing surveys on long context lack a comprehensive, non-overlapping taxonomy covering both approaches and evaluation"
    evidence: "Section 1, comparison with Zhao et al. (2023), Huang et al. (2023), Pawar et al. (2024), Dong et al. (2023b), Li et al. (2025), Shi et al. (2024)"
    status: supported
    scope: "Long context survey literature as of early 2025"
    magnitude: "qualitative"
  - id: C2
    claim: "Long context approaches can be cleanly divided into four non-overlapping categories: positional encoding, context compression, retrieval augmented, and attention pattern"
    evidence: "Section 3, Figure 1"
    status: unvalidated
    scope: "Transformer-based LLMs only; excludes efficient Transformers, SSMs, multimodal long context, and RAG with external knowledge"
    magnitude: "qualitative -- taxonomy claim, no quantitative measure"
  - id: C3
    claim: "Three inherent challenges drive long context degradation: OOD problems from unseen positions, Lost-in-the-Middle phenomenon, and quadratic attention complexity"
    evidence: "Section 2, citing Han et al. (2024) for OOD and Liu et al. (2024a) for Lost-in-the-Middle"
    status: supported
    scope: "Pre-trained Transformer LLMs processing sequences beyond pretrained context length"
    magnitude: "qualitative -- framework-level claim identifying root causes"
  - id: C4
    claim: "NoPE (no positional encoding) outperforms designed PE strategies on reasoning tasks when causal masks are used, because sequential processing naturally incorporates positional information"
    evidence: "Section 3.1, citing Kazemnejad et al. (2024)"
    status: supported
    scope: "Reasoning tasks with causal decoding only"
    magnitude: "qualitative -- directional comparison, no specific numbers reported in survey"
  - id: C5
    claim: "Evaluation metrics have progressed through three stages: algorithmic metrics (PPL, accuracy), model-based metrics (BERTScore, BARTScore), and LLM-based metrics, with increasing correlation to human judgments"
    evidence: "Section 4.3, Appendix B.3"
    status: supported
    scope: "Long context evaluation metrics specifically; general NLG evaluation trajectory"
    magnitude: "qualitative -- trend claim based on cited literature (Wang et al., 2023a; Li et al., 2023a)"
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: evaluates
    detail: "Surveys the Transformer architecture as the foundation for all long context methods"
  - target: 2024-01-roformer-rope
    type: evaluates
    detail: "Surveys RoPE as the core positional encoding modified by most context extension methods (Section 3.1.1)"
  - target: 2023-06-pi-positional-interpolation
    type: evaluates
    detail: "Reviews Position Interpolation as a position index scaling method under the RoPE variants taxonomy (Section 3.1.1)"
  - target: 2023-06-rope-ntk
    type: evaluates
    detail: "Reviews NTK-by-parts interpolation as a base frequency adjustment method (Section 3.1.1, Appendix A.1.1)"
  - target: 2024-05-yarn-context-extension
    type: evaluates
    detail: "Reviews YaRN as combining NTK-by-parts with temperature scaling for base frequency adjustment (Section 3.1.1, Appendix A.1.1)"
  - target: 2022-04-alibi-train-short-test-long
    type: evaluates
    detail: "Reviews ALiBi as the canonical predefined attention bias method (Section 3.1.2, Appendix A.1.2)"
  - target: 2019-07-transformer-xl
    type: evaluates
    detail: "Reviews Transformer-XL as the foundational sliding window attention pattern method (Section 3.4.1, Appendix A.4.1)"
  - target: 2024-05-attention-sinks-streaming
    type: evaluates
    detail: "Reviews StreamingLLM as a sliding window method that preserves attention to initial tokens (Section 3.4.1, Appendix A.4.1)"
  - target: 2023-12-landmark-attention-infinite-context
    type: evaluates
    detail: "Reviews Landmark Attention for block-level retrieval granularity and grouped softmax attention (Sections 3.3.1, 3.3.3, 3.3.4)"
  - target: 2024-02-lost-in-the-middle
    type: evaluates
    detail: "Identifies Lost-in-the-Middle as one of three inherent challenges for long context processing (Section 2)"
  - target: 2023-12-positional-encoding-length-generalization
    type: evaluates
    detail: "Cites finding that NoPE outperforms designed PE on reasoning tasks with causal masks (Section 3.1)"
  - target: 2020-04-longformer-long-document-transformer
    type: evaluates
    detail: "References Longformer for perplexity evaluation methodology in long context benchmarks (Section 4.3.1)"
  - target: 2022-12-scrolls-long-language-sequences
    type: evaluates
    detail: "Includes SCROLLS as a Phase I long context benchmark with 1k-4k token lengths (Table 1, Section 4.1)"
  - target: 2023-12-zeroscrolls-zero-shot-long-text
    type: evaluates
    detail: "Includes ZeroSCROLLS as a Phase I benchmark and credits it with pioneering diverse automatic evaluation metrics (Table 1, Appendix B.3.1)"
  - target: 2024-08-longbench-bilingual-benchmark
    type: evaluates
    detail: "Includes LongBench as a Phase I benchmark with tri-interval partitioning and data sampling strategies (Table 1, Appendix B.1)"
  - target: 2024-08-infinitebench-long-context-evaluation
    type: evaluates
    detail: "Includes InfiniteBench as a Phase II benchmark supporting 0k-200k tokens with code debugging and retrieval tasks (Table 1)"
  - target: 2024-08-l-eval-standardized-evaluation
    type: evaluates
    detail: "Includes L-Eval as a Phase II benchmark with 3k-200k token range and keyword substitution for knowledge leakage prevention (Table 1, Appendix B.1.2)"
  - target: 2024-06-ada-leval-length-adaptable-benchmark
    type: evaluates
    detail: "Includes Ada-LEval as a Phase II length-adaptable benchmark with 1k-128k token range (Table 1)"
  - target: 2024-07-longrope-context-extension
    type: complementary
    detail: "LongRoPE extends RoPE-based interpolation via evolutionary search for per-dimension rescale factors; falls within the base frequency adjustment subcategory of this survey's taxonomy"
  - target: 2024-06-effective-long-context-scaling
    type: complementary
    detail: "Llama 2 Long represents continual pretraining for context extension; addresses the same challenges surveyed here"
  - target: 2025-05-100-longbench-long-context-benchmarks
    type: complementary
    detail: "Comprehensive meta-analysis of 100+ long context benchmarks; provides deeper empirical analysis of the evaluation landscape this survey taxonomizes"
open_questions:
  - question: "How can methods from different taxonomy categories (positional encoding, compression, retrieval, attention pattern) be effectively integrated?"
    addressed_by: null
  - question: "How can models be trained on short sequences but perform well on long contexts (train-short-test-long) without positional encoding modifications?"
    addressed_by: null
  - question: "How can the Lost-in-the-Middle phenomenon be fully resolved with targeted solutions and appropriate verification methods?"
    addressed_by: null
  - question: "How can existing long context methods scale to models of different sizes and architectural frameworks?"
    addressed_by: null
  - question: "How can long context benchmarks be designed with coherent content and genuine long-distance dependencies rather than synthetic tasks?"
    addressed_by: null
  - question: "How can knowledge leakage in long context evaluation be addressed as LLM training data scope expands?"
    addressed_by: null
---
# A Survey on Transformer Context Extension: Approaches and Evaluation

**Authors:** Yijun Liu, Jinzheng Yu, Yang Xu, Zhongyang Li, Qingfu Zhu (Harbin Institute of Technology, Communication University of China, Huawei Technologies)
**Date:** March 2025, arXiv:2503.13299v2

---

## Core Research Problem

Transformer-based LLMs trained on fixed context windows degrade when processing sequences beyond their pretrained length. Three inherent challenges drive this degradation (Section 2): (1) **out-of-distribution (OOD) problems** from unseen inter-token distances, increased attended token counts, and implicitly encoded starting-token positions (Han et al., 2024); (2) the **"Lost in the Middle" phenomenon**, where models attend to information at the beginning and end of input while neglecting middle content (Liu et al., 2024a); and (3) **quadratic attention complexity**, making direct training or inference on long context prohibitively expensive (Zhou et al., 2024).

Existing surveys on this topic have significant gaps. Zhao et al. (2023) cover only positional encoding approaches. Li et al. (2025) and Shi et al. (2024) focus exclusively on KV cache optimization. Huang et al. (2023) and Pawar et al. (2024) propose taxonomies with overlapping categories (e.g., methods belonging to multiple categories simultaneously). Dong et al. (2023b) cover general text-processing methods not specific to long context. Furthermore, most existing surveys pay little or no attention to evaluation methodology (Section 1). **The core gap is the absence of a systematic, comprehensive, and non-overlapping taxonomy covering both long context approaches and evaluation.**

---

## Problem Solutions

This survey proposes a four-category taxonomy for long context approaches, paired with a three-perspective framework for evaluation (Section 1, Figure 1):

1. **Positional encoding** (Section 3.1): Variants of RoPE (position index adjustment, base frequency adjustment, structural modification) and attention bias methods (learnable, predefined).
2. **Context compression** (Section 3.2): Soft compression (summary tokens at hidden-state level) and hard compression (direct text shortening via selection or summarization).
3. **Retrieval augmented** (Section 3.3): Selectively incorporating history tokens from KV cache via a four-step pipeline: retrieval granularity, similarity computation, positional encoding, and attention calculation.
4. **Attention pattern** (Section 3.4): Sliding window, parallel context, and sparse attention mechanisms that modify the range of tokens attended to.

For evaluation, the survey organizes existing benchmarks across three dimensions: data characteristics (length level, number of examples, domain), tasks (seven categories), and metrics (algorithmic, model-based, LLM-based) (Section 4).

---

## Approach Details

### Taxonomy of Approaches

#### 3.1 Positional Encoding

**Variants of RoPE.** The survey organizes RoPE-based methods into three subcategories based on which component of the rotation matrix R^d_{Theta,m} they modify (Section 3.1.1, Appendix A.1.1):

RoPE encodes relative position in self-attention via the rotation matrix:

> sim(q_m, k_n) = q_m^T R^d_{Theta,n-m} k_n = (R^d_{Theta,m} q_m)^T (R^d_{Theta,n} k_n)

where R^d_{Theta,m} is parameterized by position index m and the function family Theta = {theta_i = 10000^{-2(i-1)/d}, i in [1, 2, ..., d/2]} (Equation 3, Appendix A.1.1).

1. **Position index adjustment** -- modifying the allocation or scaling of position index m:
   - *Index reallocation:* Dual Chunk Attention (DCA, An et al., 2024) distributes pretrained position indexes based on query-key relative position relationships without training.
   - *Index scaling:* Position Interpolation (PI, Chen et al., 2023b) scales m to m' = m * L/L', inserting additional positional encoding between adjacent integer positions.
   - *Combined:* ReRoPE (Su, 2023) keeps within-window relative positions unchanged while scaling positions outside the window.

2. **Base frequency adjustment** -- modifying theta_i in the trigonometric function terms of the rotation matrix, following the NTK-theory principle of "extrapolation on high-frequency and interpolation on low-frequency" (Tancik et al., 2020):
   - *Base change:* NTK-aware scaling (Peng and Quesnelle, 2023; Roziere et al., 2023) changes the base b from the default 10000 to a higher value.
   - *Direct theta_i scaling:* NTK-by-parts (bloc97, 2023) scales theta_i per dimension as a function of dimension i and input length L'. YaRN (Peng et al., 2023) incorporates temperature t related to L' on top of NTK-by-parts to further improve extrapolation.

3. **Structural modification** -- adjusting the RoPE formula itself:
   - XPOS (Sun et al., 2022) introduces a position-dependent exponential bias to enhance decay on distant tokens.

Liu et al. (2024b) provide scaling laws for RoPE-based extrapolation (Appendix A.1.1).

**Attention bias.** Methods that add a bias f_bias(m, n) to the query-key similarity (Section 3.1.2, Appendix A.1.2):

> sim(q_m, k_n) = q_m^T k_n + f_bias(m, n)

- *Learnable:* T5 relative bias (Raffel et al., 2020) uses a learnable function of m - n varying per head. KERPLE (Chi et al., 2022a) uses parameterized kernel functions.
- *Predefined:* ALiBi (Press et al., 2021) uses f_bias(m, n) = 2^{-8/H} * (n - m), depending on the number of attention heads H. Sandwich (Chi et al., 2022b) defines f_bias as the product of sinusoidal positional encodings.

**Key observation:** Kazemnejad et al. (2024) find that NoPE (no positional encoding) outperforms designed PE strategies on reasoning tasks when causal masks are used, because sequential left-to-right decoding naturally incorporates positional information (Section 3.1). This finding suggests PE design should account for the natural sequential information present in causal decoding (single paper cited, limited evidence).

#### 3.2 Context Compression

**Soft compression** (hidden-state level, Section 3.2.1, Appendix A.2.1):
- *Recurrent Memory Transformer* (RMT, Bulatov et al., 2022): Segments input, appends memory tokens at start/end of each segment, propagates last hidden states to next segment. Through iterative propagation, the model utilizes inter-segment contextual information.
- *Recurrent Attention Network* (RAN, Li et al., 2023b): Appends a Global Perception Cell (GPC) vector at the start of each segment's hidden representation. Introduces a Memory Review scheme using cross-attention between GPC hidden states from all segments and the original input.
- *AutoCompressors* (Chevalier et al., 2023): Built on RMT, compresses segments into summary vectors that form soft prompts for subsequent segments.
- *In-context Autoencoder* (ICAE, Ge et al., 2023): Appends memory tokens at end of input, trains model to compress context into short memory slots and reconstruct original context via autoencoding pretraining.
- *Gisting* (Mu et al., 2024b): Compresses prompts into shorter gist tokens for inference speed.

**Hard compression** (text level, Section 3.2.2, Appendix A.2.2):
- *LLMLingua* (Jiang et al., 2023): Trains small model aligned with LLM output, uses PPL as token importance metric, prunes unimportant tokens.
- *LongLLMLingua* (Jiang et al., 2024b): Extends LLMLingua with question-aware compression to preserve key information related to the query.
- *MEMWALKER* (Chen et al., 2023a): Hierarchical summarization building a tree structure for efficient query-based search during inference.

#### 3.3 Retrieval Augmented

The survey identifies a four-step processing paradigm (Section 3.3, Appendix A.3):

1. **Retrieval granularity** (Section 3.3.1): Token-level (MemTRM, FoT, Unlimiformer -- simple but computationally intensive, risk of semantic discontinuities) vs. block-level (LongMEM and RPT use mean pooling of token representations; InfLLM uses representative scoring of tokens within blocks; Landmark introduces a new vocabulary token at block boundaries to summarize block information).

2. **Similarity computation** (Section 3.3.2): All methods use dot-product of query and key vectors, following standard attention.

3. **Positional encoding** (Section 3.3.3): Most methods (MemTRM, FoT, InfLLM) assign the same position vector to all retrieved tokens, based on the finding by Dai et al. (2019) that relative position of distant tokens is not important. Landmark re-encodes relative positions of retrieved and local context together.

4. **Attention calculation** (Section 3.3.4): Standard attention (FoT, InfLLM), cross attention (Unlimiformer), Joint Attention with learnable weighting V_a = g * V_l + (1 - g) * V_r where g is a learnable parameter (MemTRM, LongMEM), or Grouped Softmax with per-block attention weighted by retrieval scores (Landmark).

#### 3.4 Attention Pattern

**Sliding window** (Section 3.4.1, Appendix A.4.1): Segment-by-segment attention with inter-segment information transfer.
- Transformer-XL (Dai et al., 2019): Concatenates previous segment hidden states to current segment, hierarchically expanding receptive field by reusing key and value information from the previous segment.
- LM-Infinite (Han et al., 2024): Lambda-shaped attention mask attending to initial tokens and nearby tokens. Identifies that starting tokens occupy a distinct feature space causing generalization failures.
- StreamingLLM (Xiao et al., 2023): Similar approach preserving attention to "attention sink" starting tokens.

**Parallel context** (Section 3.4.2, Appendix A.4.2): Folds context into independent segments sharing position indexes.
- PCW (Ratner et al., 2022): Splits input into context and task tokens; context segments compute attention independently, then all context is concatenated for task token decoding.
- Structured Prompting (Hao et al., 2022): Similar folding with Rescaled Attention to prevent test tokens from over-attending to demonstrations.

These methods require no training and can be plug-and-played into existing models (Section 3.4.2).

**Sparse attention** (Section 3.4.3, Appendix A.4.3): Reduces number of tokens in attention computation.
- LongNet (Ding et al., 2023): Dilated attention with exponentially increasing field, reducing quadratic to linear complexity. Performs multiple sets of sparse attention calculations, each attending to a different range (denser at small range, sparser at large range).
- MEGABYTE (Yu et al., 2023): Hierarchical byte-level then global-level attention -- a small local model encodes at byte level, then a larger global model processes at larger granularity.
- LongLoRA (Chen et al., 2023c): S^2-Attention groups attention heads to attend to different overlapping local windows, leveraging multi-head attention to integrate local information.

### Evaluation Framework

#### Data Characteristics (Section 4.1, Table 1, Appendix B.1)

The survey organizes 11 benchmarks by three data characteristics. Given that current models mainly support context windows exceeding 100K tokens, benchmarks are categorized into two phases:

| Benchmark | Length Level | #Examples | Domain |
|---|---|---|---|
| **Phase I (< 100K)** | | | |
| SCROLLS | 1k-4k | 119,495 | Literature, Dialog |
| ZeroSCROLLS | 0k-16k | 4,378 | Wiki, Literature, Dialog |
| LongBench | 0k-4k, 4k-8k, >8k | 4,750 | Wiki, Literature, Dialog, Report, Code, News |
| LooGLE | 0k-24k | 776 | Wiki, Paper |
| BAMBOO | 0k-4k, 4k-16k | 1,502 | Wiki, Dialog, Report, Code, Paper |
| LongICLBench | 2k-50k | 3,000 | Dialog, News, Common Sense |
| **Phase II (>= 100K)** | | | |
| L-Eval | 3k-200k | 411 | Literature, Dialog, News, Paper, Common Sense |
| Ada-LEval | 1k-128k | 117,500 | Literature, Code |
| InfiniteBench | 0k-200k | 3,946 | Literature, Dialog, Code |
| NeedleBench | 1k-4k/8k/12k/128k/200k/1M+ | - | Wiki, Literature, Dialog, Report, Code, News |
| LV-Eval | 0k-16k/32k/64k/128k/256k | 1,729 | Wiki, Literature, Dialog, Report, Code, News, Paper |

Phase I benchmarks use bi- or tri-interval length partitioning (BAMBOO bi-interval, LongBench tri-interval). Phase II benchmarks refine to five- and six-interval schemas (LV-Eval five-interval, NeedleBench six-interval), enabling finer-grained analysis of how length affects performance (Appendix B.1.1).

**Knowledge leakage** is addressed through three strategies (Appendix B.1.2): (1) data sampling (LongBench's random and uniform sampling), (2) keyword substitution and sentence rewriting (L-Eval, BAMBOO, InfiniteBench, LV-Eval), and (3) non-overlapping data leveraging using datasets released after model deployment (LooGLE, BAMBOO). However, since specific training data for most LLMs remains undisclosed, none of these methods can completely guarantee absence of overlap.

#### Task Taxonomy (Section 4.2, Appendix B.2)

Seven task categories:

1. **Question Answering**: Single-hop (SQuAD, TriviaQA, NarrativeQA) and multi-hop (2WikiMQA, MuSiQue, HotpotQA). Metrics: F1, exact match, ROUGE, BLEU.
2. **Needle-in-a-Haystack**: Passkey retrieval (Mohtashami and Jaggi, 2023), extended to 10-digit numbers (InfiniteBench), key-value retrieval from JSON. NeedleBench proposes multi-needle retrieval (S-RT, M-RT) and multi-needle reasoning (M-RS). Metrics: Levenshtein distance similarity.
3. **Statistical Tasks**: Long arithmetic calculation (GSM8K and extensions like E-GSM), numerical information extraction (InfiniteBench, LooGLE), sentiment aggregation (ZeroSCROLLS/Space), paragraph counting (LongBench/PassageCount).
4. **Code**: Code completion (LCC, RepoBench-P, PrivateEval using pass@1 and edit similarity), code running (InfiniteBench, 2-10 cascading function calls with addition/subtraction), code debugging (InfiniteBench/PyPI with syntactic/semantic/logical errors).
5. **In-Context Learning**: Long example learning (TREC 50-class, LSHT 24-class) and many-shot learning (hundreds to thousands of examples, Agarwal et al., 2024).
6. **Text Generation**: Language modeling, single-document summarization (SQuALITY, GovReport, QMSum, SummScreenFD), multi-document summarization (MultiNews), open-ended text generation (ProxyQA, LongWriter with AgentWrite, LongLAMP/LongPersonalizer). Metrics: ROUGE, BLEU.
7. **Other Tasks**: Reordering (Booksum), context consistency / hallucination detection (BAMBOO SenHallu/AbsHallu), summary source paragraph identification (LongBench), character identification in dialogues.

#### Metrics Evolution (Section 4.3, Appendix B.3)

Three developmental stages:

1. **Algorithmic metrics** (Section 4.3.1): PPL, accuracy, F1, ROUGE, BLEU. Limitations: fail to measure content quality (Reiter and Belz, 2009), miss syntactic accuracy (Stent et al., 2005), low correlation with human judgments for open-ended generation (An et al., 2023), and require gold references (Tan et al., 2024). Improvements include LV-Eval's two-stage scoring (keyword recall then F1) and NeedleBench's Circular Evaluation for option reordering.

   Key formulas from Appendix B.3.1:

   > PPL = 2^{H(p)}, where H(p) = -(1/N) * sum_{i=1}^{N} log_2 P(w_i | w_1, ..., w_{i-1})

   > ROUGE-N = sum_{S in R} sum_{ngram in S} Count_match(ngram) / sum_{S in R} sum_{ngram in S} Count(ngram)

   > BLEU = BP * exp(sum_{n=1}^{N} w_n * log p_n), where BP = 1 if c > r, else exp(1 - r/c)

2. **Model-based metrics** (Section 4.3.2): BERTScore (cosine similarity of BERT token embeddings), BARTScore (log-likelihood from BART). Better human correlation but still relies on pretrained representations and requires reference texts.

   > BARTScore = (1/|C|) * sum_{c in C} (1/L_c) * sum_i log p_theta(c_i | c_{<i}, r)

3. **LLM-based metrics** (Section 4.3.3): Prompting LLMs for multi-dimensional assessment (GPTScore, G-EVAL) and interpretable reasoning. Higher agreement with human evaluation (Wang et al., 2023a; Li et al., 2023a), more flexible, but costly, stochastic, and lacking human emotion. Benchmarks incorporating LLM-based metrics include LooGLE (GPT-4 scoring), L-Eval (word count requirements), ProxyQA (proxy question accuracy).

---

## Limitations and Failure Modes

1. **Scope exclusions.** The survey explicitly excludes efficient Transformers in general settings, SSMs, multimodal long context, long chain-of-thought reasoning, and external-knowledge RAG (Section 1). This means important context extension approaches like Mamba, RWKV, and Ring Attention are not covered.

2. **No experiments.** The survey does not conduct any empirical comparison of the methods it reviews. All claims about method effectiveness are reported from original papers without independent verification or controlled comparison.

3. **Taxonomy boundary cases.** While the authors claim their four-category taxonomy avoids overlaps (unlike prior surveys), some methods arguably span categories. For example, retrieval-augmented methods involve attention pattern modification (KV cache retrieval changes which tokens are attended to), and sliding window methods like StreamingLLM could be viewed as a form of hard compression.

4. **Benchmark coverage limited to pre-2024.** The benchmarks surveyed (Table 1) go up to NeedleBench and LV-Eval. More recent benchmarks (RULER, BABILong, HELMET, LongBench v2, LongBench Pro, NOLIMA) are not included.

5. **Limited depth on individual methods.** As a breadth-focused survey, individual method descriptions are necessarily brief. Key technical details (e.g., YaRN's alpha/beta parameters, LongRoPE's evolutionary search) are condensed.

6. **[Inferred]** The survey does not discuss how the four-category taxonomy handles methods that combine approaches from multiple categories (e.g., a model using both RoPE modification and sparse attention). No formal criteria for resolving borderline classification cases are provided.

7. The authors acknowledge: "Due to the rapidly evolving nature of the field of Transformer context extension, our survey may not capture the latest developments, particularly those that emerged near or after the time of writing" (Limitations section, p. 9).

### Scope and Comparability

- **What was not tested:** The survey covers only Transformer-based approaches, excluding SSM-based alternatives (Mamba, S4), hybrid architectures, and linear attention variants. Focus is on long input context, not long generation or retrieval-augmented generation with external knowledge. No empirical evaluation of the surveyed methods is performed.
- **Comparability notes:** The taxonomy is presented as conceptual; no formal criteria are provided for resolving borderline cases. Cross-paper comparison of methods is limited to descriptions from original papers, which may use different experimental setups, model sizes, and evaluation protocols. The benchmark table (Table 1) aggregates statistics from original papers without normalization for tokenizer differences (e.g., token counts may vary across models for the same text).

---

## Conclusions

### Contributions

1. **Four-category approach taxonomy.** Proposes a taxonomy dividing long context methods into positional encoding (with RoPE variants and attention bias subcategories), context compression (soft and hard), retrieval augmented (with a four-step paradigm), and attention pattern (sliding window, parallel context, sparse attention) (Section 3, Figure 1).

2. **Three-perspective evaluation framework.** Organizes long context evaluation across data characteristics (length, examples, domain), tasks (seven categories), and metrics (three developmental stages) (Section 4).

3. **Identification of three core challenges.** Frames the long context problem around OOD issues, Lost-in-the-Middle phenomenon, and quadratic complexity as fundamental drivers (Section 2).

4. **Future research roadmap.** Identifies ten open problems across approaches (method integration, long text generation, sparse attention limitations, Lost-in-the-Middle resolution, train-short-test-long, scalability, information filtering trade-offs) and evaluation (knowledge leakage, novel benchmark design, updated LLM-based metrics) (Section 5).

### Implications

1. Method integration across taxonomy categories may be necessary to address all three challenges simultaneously -- no single category addresses OOD, Lost-in-the-Middle, and quadratic complexity together (speculative, Section 5.1).

2. The progression from algorithmic to LLM-based metrics suggests that long context evaluation is moving toward more human-aligned but also more expensive and stochastic assessment methods (Section 4.3).

3. The NoPE finding (Kazemnejad et al., 2024) suggests that positional encoding design should account for the natural sequential information present in causal decoding, potentially reducing the complexity of context extension methods (speculative, Section 3.1).

---

## Key Claims

**C1. Existing surveys lack a comprehensive, non-overlapping taxonomy covering both approaches and evaluation.** The authors compare with six prior surveys: Zhao et al. (2023) cover only positional encoding; Li et al. (2025) and Shi et al. (2024) cover only KV cache; Huang et al. (2023) have overlapping categories where methods belong to multiple categories; Pawar et al. (2024) also has overlap with interpolation/extrapolation classification; Dong et al. (2023b) include general methods not specific to long context. None systematically cover evaluation (Section 1). *Scope:* Long context survey literature as of early 2025. *Magnitude:* qualitative -- taxonomy gap identified across 6 prior surveys. Status: **supported** (the comparison with prior surveys is well-documented, survey-level evidence spanning 6 cited works).

**C2. Long context approaches divide into four non-overlapping categories.** The four categories -- positional encoding, context compression, retrieval augmented, and attention pattern -- are claimed to be distinct and non-overlapping (Section 3, Figure 1). *Scope:* Transformer-based LLMs only; excludes efficient Transformers, SSMs, multimodal long context, and RAG. *Magnitude:* qualitative -- taxonomy claim with no formal boundary criteria. Status: **unvalidated** -- no formal criterion for category boundaries is provided. Retrieval-augmented methods modify attention patterns (which tokens are attended to), and sliding window methods perform a form of context compression (discarding distant tokens). The taxonomy's cleanness is asserted rather than proven (author claim only, no external validation).

**C3. Three inherent challenges drive long context degradation.** OOD problems from three factors (unseen inter-token distances, increased attended tokens, implicitly encoded starting-token positions), Lost-in-the-Middle (models neglect middle content), and quadratic complexity (Section 2). *Scope:* Pre-trained Transformer LLMs processing beyond pretrained context length. *Magnitude:* qualitative -- framework identifies root causes, each supported by cited empirical work. Status: **supported**, citing Han et al. (2024) for OOD and Liu et al. (2024a) for Lost-in-the-Middle (each challenge supported by individual empirical studies, moderate evidence).

**C4. NoPE outperforms designed PE strategies on reasoning tasks with causal masks.** Citing Kazemnejad et al. (2024), the survey notes that sequential left-to-right processing with causal masks naturally incorporates positional information, making explicit PE unnecessary for some tasks (Section 3.1). *Scope:* reasoning tasks with causal decoding only. *Magnitude:* qualitative -- directional comparison without specific scores reported in the survey. Status: **supported** (single cited paper, limited evidence for the specific claim; broader implications speculative).

**C5. Evaluation metrics have progressed through three stages with increasing human correlation.** Algorithmic metrics (PPL, F1, ROUGE) -> model-based metrics (BERTScore, BARTScore) -> LLM-based metrics (GPTScore, G-EVAL). LLM-based metrics show enhanced agreement with human evaluation (Section 4.3, citing Wang et al., 2023a; Li et al., 2023a). *Scope:* Long context and general NLG evaluation metrics. *Magnitude:* qualitative -- trend claim based on multiple cited studies. Status: **supported** (multiple citations establishing the trend, moderate evidence).

---

## Open Questions

1. **How can methods from different categories be effectively integrated?** The survey identifies method integration as a key future direction but provides no concrete proposals or examples of successful integration (Section 5.1). Unresolved.

2. **Can "train short, test long" be achieved without positional encoding modifications?** The survey notes that no existing method successfully trains on short texts while excelling on long context (Section 5.1). Unresolved.

3. **How can the Lost-in-the-Middle phenomenon be fully resolved?** The survey notes this remains unsolved, with no targeted solutions or appropriate verification methods (Section 5.1). Partially addressed by: `2024-02-lost-in-the-middle`, `2024-12-lost-in-the-middle-in-between`.

4. **How can long context methods scale across model sizes and architectures?** The survey highlights scalability as an open problem (Section 5.1). Unresolved.

5. **How can benchmarks with genuine long-distance dependencies be designed?** The survey suggests constructing benchmarks with coherent content requiring multi-book processing (Section 5.2). Partially addressed by: `2025-05-100-longbench-long-context-benchmarks`.

6. **How can knowledge leakage in evaluation be addressed?** As LLM training data expands, current mitigation strategies (keyword substitution, non-overlapping data) become increasingly ineffective (Section 5.2). Unresolved.

---

## Core References and Why They Are Referenced

### Challenge Identification

- **Han et al. (2024)** -- *LM-Infinite: Zero-Shot Extreme Length Generalization.* Provides the theoretical and empirical analysis of three OOD factors driving context extension failure: unseen distances, increased attended tokens, and starting-token position information. Also proposes the lambda-shaped attention mask (Sections 2, 3.4.1).
- **Liu et al. (2024a)** -- *Lost in the Middle.* Discovers that LLMs focus on beginning and end of input while neglecting middle content, established as one of three inherent challenges (Section 2).

### Positional Encoding Methods

- **Su et al. (2024)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* Core PE method modified by most context extension approaches; provides the rotation matrix formulation R^d_{Theta,m} with Theta = {theta_i = 10000^{-2(i-1)/d}} (Section 3.1.1, Equation 3).
- **Chen et al. (2023b)** -- *Extending Context Window via Positional Interpolation.* Position Interpolation method (position index scaling m to m' = m * L/L') serving as the foundational position index adjustment approach (Section 3.1.1).
- **Peng and Quesnelle (2023)** -- *NTK-Aware Scaled RoPE.* Base frequency adjustment via changing b = 10000 to higher values (Section 3.1.1, Appendix A.1.1).
- **bloc97 (2023)** -- *NTK-by-parts Interpolation.* Dimension-dependent theta_i scaling as a function of dimension and input length (Section 3.1.1, Appendix A.1.1).
- **Peng et al. (2023)** -- *YaRN.* Combines NTK-by-parts with temperature t scaling for improved base frequency adjustment (Section 3.1.1, Appendix A.1.1).
- **Press et al. (2021)** -- *ALiBi: Train Short, Test Long.* Canonical predefined attention bias f_bias(m,n) = 2^{-8/H} * (n - m) (Section 3.1.2, Appendix A.1.2).
- **Kazemnejad et al. (2024)** -- *Impact of Positional Encoding on Length Generalization.* Finding that NoPE outperforms designed PE on reasoning tasks with causal masks (Section 3.1).
- **Sun et al. (2022)** -- *XPOS.* Structural modification of RoPE with position-dependent exponential bias (Section 3.1.1, Appendix A.1.1).
- **An et al. (2024)** -- *Dual Chunk Attention.* Training-free position index reallocation based on query-key relative positions (Section 3.1.1, Appendix A.1.1).
- **Su (2023)** -- *ReRoPE.* Combined approach using direct extrapolation within window and interpolation outside (Section 3.1.1, Appendix A.1.1).
- **Liu et al. (2024b)** -- *Scaling Laws of RoPE-based Extrapolation.* Provides scaling laws for RoPE-based extrapolation (Appendix A.1.1).
- **Raffel et al. (2020)** -- *T5.* Learnable relative attention bias with function of m - n varying per head (Section 3.1.2, Appendix A.1.2).
- **Chi et al. (2022a)** -- *KERPLE.* Parameterized kernel functions as learnable attention bias (Section 3.1.2, Appendix A.1.2).
- **Chi et al. (2022b)** -- *Sandwich.* Predefined attention bias using sinusoidal encoding products (Section 3.1.2, Appendix A.1.2).

### Context Compression Methods

- **Bulatov et al. (2022)** -- *Recurrent Memory Transformer.* Foundational soft compression method using segment-level memory tokens with iterative propagation (Section 3.2.1, Appendix A.2.1).
- **Li et al. (2023b)** -- *Recurrent Attention Network.* Extends RMT concept with Global Perception Cell and Memory Review cross-attention scheme (Appendix A.2.1).
- **Chevalier et al. (2023)** -- *AutoCompressors.* Extends RMT with summary vectors forming soft prompts for subsequent segments (Section 3.2.1, Appendix A.2.1).
- **Ge et al. (2023)** -- *In-context Autoencoder (ICAE).* Memory tokens for context compression with autoencoding pretraining (Section 3.2.1, Appendix A.2.1).
- **Mu et al. (2024b)** -- *Gisting.* Compresses prompts into gist tokens for inference speedup (Section 3.2.1, Appendix A.2.1).
- **Jiang et al. (2023)** -- *LLMLingua.* PPL-based token importance scoring and pruning for hard compression (Section 3.2.2, Appendix A.2.2).
- **Jiang et al. (2024b)** -- *LongLLMLingua.* Question-aware hard compression extending LLMLingua (Section 3.2.2, Appendix A.2.2).
- **Chen et al. (2023a)** -- *MEMWALKER.* Hierarchical summarization with tree structure for query-based search (Section 3.2.2, Appendix A.2.2).

### Retrieval-Augmented Methods

- **Wu et al. (2022)** -- *Memorizing Transformers (MemTRM).* Token-level retrieval with joint attention and uniform position encoding for retrieved tokens (Sections 3.3.1, 3.3.3, 3.3.4, Appendix A.3).
- **Tworkowski et al. (2024)** -- *Focused Transformer (FoT).* Token-level retrieval with standard attention and contrastive training for context scaling (Sections 3.3.1, 3.3.4).
- **Bertsch et al. (2024a)** -- *Unlimiformer.* Token-level retrieval with cross attention for unlimited length input (Sections 3.3.1, 3.3.4).
- **Wang et al. (2024b)** -- *LongMEM.* Block-level retrieval with mean pooling and joint attention (Sections 3.3.1, 3.3.4).
- **Rubin and Berant (2023)** -- *RPT (Retrieval-Pretrained Transformer).* Block-level retrieval with mean pooling (Section 3.3.1).
- **Xiao et al. (2024)** -- *InfLLM.* Block-level retrieval with representative scoring and standard attention (Sections 3.3.1, 3.3.4).
- **Mohtashami and Jaggi (2023, 2024)** -- *Landmark Attention.* Block-level retrieval using landmark tokens with grouped softmax attention and position re-encoding (Sections 3.3.1, 3.3.3, 3.3.4).

### Attention Pattern Methods

- **Dai et al. (2019)** -- *Transformer-XL.* Foundational sliding window method with segment-level hidden state reuse (Section 3.4.1, Appendix A.4.1).
- **Xiao et al. (2023)** -- *StreamingLLM.* Identifies attention sinks in initial tokens and preserves them during sliding window inference (Section 3.4.1, Appendix A.4.1).
- **Ratner et al. (2022)** -- *Parallel Context Windows (PCW).* Folds context into independent segments sharing position indexes (Section 3.4.2, Appendix A.4.2).
- **Hao et al. (2022)** -- *Structured Prompting.* Folds demonstrations with Rescaled Attention to prevent over-attending (Section 3.4.2, Appendix A.4.2).
- **Ding et al. (2023)** -- *LongNet.* Dilated attention with exponentially increasing field, reducing quadratic to linear complexity (Section 3.4.3, Appendix A.4.3).
- **Yu et al. (2023)** -- *MEGABYTE.* Hierarchical byte-level then global-level attention (Section 3.4.3, Appendix A.4.3).
- **Chen et al. (2023c)** -- *LongLoRA.* S^2-Attention grouping heads to attend to different overlapping local windows (Section 3.4.3, Appendix A.4.3).

### Evaluation Benchmarks

- **Shaham et al. (2022)** -- *SCROLLS.* Phase I benchmark (1k-4k tokens) for fine-tuning evaluation (Table 1).
- **Shaham et al. (2023)** -- *ZeroSCROLLS.* Phase I zero-shot benchmark pioneering diverse automatic evaluation metrics (Table 1, Appendix B.3.1).
- **Bai et al. (2023)** -- *LongBench.* Phase I bilingual benchmark with tri-interval partitioning and data sampling strategies (Table 1, Appendix B.1.1).
- **Li et al. (2023a)** -- *LooGLE.* Phase I benchmark using non-overlapping data and GPT-4 scoring (Table 1, Appendix B.1.2, B.3.3).
- **Dong et al. (2023a)** -- *BAMBOO.* Phase I benchmark with context consistency tasks and keyword substitution (Table 1, Appendix B.1.2).
- **Li et al. (2024c)** -- *LongICLBench.* Phase I benchmark for long in-context learning (Table 1).
- **An et al. (2023)** -- *L-Eval.* Phase II benchmark (3k-200k tokens) with keyword substitution and word count requirements for LLM evaluation (Table 1, Appendix B.1.2).
- **Wang et al. (2024a)** -- *Ada-LEval.* Phase II length-adaptable benchmark (1k-128k) (Table 1).
- **Zhang et al. (2024)** -- *InfiniteBench.* Phase II benchmark extending to 200k tokens with code debugging and 10-digit passkey retrieval (Table 1, Appendix B.2.2).
- **Li et al. (2024b)** -- *NeedleBench.* Phase II benchmark with six-interval schema and multi-needle reasoning tasks (S-RT, M-RT, M-RS) (Table 1, Appendix B.2.2).
- **Yuan et al. (2024)** -- *LV-Eval.* Phase II benchmark with five-interval schema up to 256k tokens and two-stage scoring (Table 1, Appendix B.3.1).

### Evaluation Metrics

- **Zhang et al. (2020)** -- *BERTScore.* Cosine similarity of BERT token embeddings for text similarity (Section 4.3.2, Appendix B.3.2).
- **Yuan et al. (2021)** -- *BARTScore.* Log-likelihood scoring from BART for text evaluation (Section 4.3.2, Appendix B.3.2).
- **Fu et al. (2023)** -- *GPTScore.* Using generative pre-trained models for text evaluation (Appendix B.3.3).
- **Liu et al. (2023c)** -- *G-EVAL.* Reference-free content scoring via chain-of-thought evaluation steps (Appendix B.3.3).

### Foundational Architecture

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Foundational Transformer architecture that all surveyed methods extend or modify.
