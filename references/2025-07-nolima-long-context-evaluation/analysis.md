---
title: "NoLiMa: Long-Context Evaluation Beyond Literal Matching"
authors: "Modarressi, Deilamsalehy, Dernoncourt, Bui, Rossi, Yoon, Schutze"
year: 2025
venue: "ICML 2025"
paper_type: conference-paper
categories: ["long-context-evaluation", "benchmarking"]
scope: ["literal matching confound in NIAH benchmarks", "latent associative reasoning evaluation"]
benchmarks_used: ["nolima", "niah", "ruler", "babilong", "infinitebench"]
models_introduced: []
models_evaluated: ["gpt-4", "llama-3-8b", "llama-3-70b", "gemini-1.5-pro"]
key_claims:
  - id: C1
    claim: "Existing NIAH-style benchmarks contain substantial literal overlap (ROUGE-1 up to 0.966) between questions and context, allowing models to exploit surface-level token matching"
    evidence: "Table 1, Section 2"
    status: supported
  - id: C2
    claim: "NoLiMa achieves ROUGE-1 precision of only 0.069, effectively eliminating literal matching confounds while remaining simple in short contexts (base scores 76.7-99.3%)"
    evidence: "Table 1, Table 3, Section 3"
    status: supported
  - id: C3
    claim: "At 32K tokens, 11 of 13 models drop below 50% of their base score on NoLiMa, despite near-perfect short-context performance"
    evidence: "Table 3, Section 4.4"
    status: supported
  - id: C4
    claim: "Two-hop latent reasoning is harder than one-hop at all context lengths, with the performance gap widening as context increases"
    evidence: "Figure 2a, Section 4.4.1"
    status: supported
  - id: C5
    claim: "In two-hop scenarios, performance depends more on total context length than needle position, indicating attention mechanism overload rather than positional encoding limitations"
    evidence: "Figure 3c-d, Section 4.4.2"
    status: supported
  - id: C6
    claim: "CoT prompting and reasoning models improve performance but fail to achieve full-length generalization -- all models drop below 50% at 32K on NoLiMa-Hard"
    evidence: "Tables 4-5, Section 4.4.3"
    status: supported
  - id: C7
    claim: "Literal matches dramatically simplify the task when present as cues (direct questions: 98.5% at 32K) and severely degrade performance when serving as distractors (GPT-4o effective length drops to 1K)"
    evidence: "Table 6, Figure 5, Section 4.4.4"
    status: supported
cross_references:
  - target: 2023-11-needle-in-a-haystack
    type: extends
    detail: "NoLiMa extends vanilla NIAH by removing literal overlap between questions and needles, requiring latent associative reasoning instead of surface matching"
  - target: 2024-10-ruler-context-size
    type: complementary
    detail: "RULER adds synthetic complexity to NIAH (multi-needle, variable tracking); NoLiMa instead removes literal cues. Llama 3.1 70B achieves 32K effective length on RULER but only 2K on NoLiMa"
  - target: 2024-12-babilong-long-context-reasoning
    type: complementary
    detail: "BABILong adds reasoning complexity via fact-chaining; NoLiMa notes BABILong counting achieves only 28% at 0K, confounding task difficulty with context-length difficulty"
  - target: 2024-08-infinitebench-long-context-evaluation
    type: complementary
    detail: "InfiniteBench QA has the highest literal overlap measured (ROUGE-1 = 0.966); NoLiMa achieves only 0.069, providing a complementary low-overlap evaluation"
  - target: 2024-02-lost-in-the-middle
    type: extends
    detail: "NoLiMa confirms lost-in-the-middle in one-hop tasks but shows that in two-hop scenarios context length dominates over position, challenging a purely positional explanation"
  - target: 2022-03-in-context-learning-induction-heads
    type: complementary
    detail: "Induction heads provide the mechanistic basis for why literal matches simplify NIAH: attention excels at recalling repetitive patterns"
  - target: 2024-01-roformer-rope
    type: complementary
    detail: "RoPE's relative-distance property is used in the aligned-depth analysis to disentangle position encoding from context-length effects"
  - target: 2022-12-chain-of-thought-prompting
    type: complementary
    detail: "CoT prompting is evaluated on NoLiMa; it helps more on two-hop tasks but fails to fully mitigate the challenge"
  - target: 2024-05-yarn-context-extension
    type: complementary
    detail: "YaRN cited as a key context-extension method that enabled the long-context models evaluated by NoLiMa"
  - target: 2023-06-pi-positional-interpolation
    type: complementary
    detail: "Positional interpolation cited as a key context-extension method that enabled the long-context models evaluated by NoLiMa"
  - target: 2024-03-gemini-1.5-long-context
    type: evaluates
    detail: "NOLIMA evaluates Gemini 1.5 Pro/Flash; effective length drops to 2K without literal matching cues, challenging the near-perfect NIAH recall claims"
  - target: 2024-11-genuinely-difficult-long-context
    type: extends
    detail: "NOLIMA directly addresses the under-explored high-dispersion quadrant identified by Goldman et al. by removing literal cues and requiring latent associative reasoning, targeting the genuinely difficult long-context tasks they call for"
open_questions:
  - question: "Can architectural improvements beyond standard attention address the latent association retrieval challenge in long contexts without literal cues?"
    addressed_by: null
  - question: "What is the mechanistic explanation for why inverted needle templates (W_n before CHAR) cause greater difficulty than default order?"
    addressed_by: null
  - question: "How do NoLiMa findings translate to real-world downstream tasks such as RAG systems where queries and relevant documents have lexical gaps?"
    addressed_by: null
  - question: "Can training methods be developed to improve latent associative reasoning in long contexts without relying on literal overlap?"
    addressed_by: null
---
# NoLiMa: Long-Context Evaluation Beyond Literal Matching

**Authors:** Ali Modarressi, Hanieh Deilamsalehy, Franck Dernoncourt, Trung Bui, Ryan Rossi, Seunghyun Yoon, Hinrich Schutze (LMU Munich, MCML, Adobe Research)
**Date:** July 2025, ICML 2025 (PMLR 267); arXiv:2502.05167

---

## Core Research Problem

Needle-in-a-haystack (NIAH) tests are the dominant synthetic evaluation for long-context LLMs: a relevant "needle" is hidden in a long irrelevant "haystack," and the model must retrieve it. Extensions add multiple needles, fact-chaining, distractors, or in-context reasoning (Hsieh et al., 2024; Levy et al., 2024; Kuratov et al., 2024). However, in all these variants the question and the needle share substantial **literal lexical overlap** -- tokens from the question appear verbatim in the needle or surrounding context.

The attention mechanism is inherently adept at identifying and recalling repetitive patterns (Olsson et al., 2022; Arora et al., 2024). When literal matches exist, models can exploit surface-level token matching to locate the needle, sidestepping genuine associative reasoning. This confound extends to downstream QA benchmarks: long-document and multi-document QA datasets (Zhang et al., 2024; Bai et al., 2024; Yen et al., 2024) implicitly contain literal overlap between questions and relevant passages.

Quantitatively, popular benchmarks exhibit high ROUGE precision between question and context: Vanilla NIAH reaches R-1 = 0.905, RULER S-NIAH reaches 0.571, and InfiniteBench QA reaches 0.966 (Table 1). Some benchmarks (e.g., BABILong counting at 28% accuracy at 0K, or Ancestral Tree Challenge) address saturation by making tasks inherently too complex even in short contexts, confounding task difficulty with context-length difficulty.

**The core challenge is: how to evaluate whether LLMs can retrieve information from long contexts when the question and the relevant fact share no literal overlap, requiring latent associative reasoning instead of surface matching.**

---

## Problem Solutions

NoLiMa is a NIAH-style benchmark where questions and needles are designed to have **minimal lexical overlap** (ROUGE-1 precision of only 0.069 vs. 0.905 for vanilla NIAH). The key idea is:

1. Needles contain a keyword W_n (e.g., "Semper Opera House") that is related to the question keyword W_q (e.g., "Dresden") only through **latent associative links** -- world knowledge or commonsense -- with no shared tokens.
2. The task remains inherently simple in short contexts (base scores of 76.7%--99.3% across 13 models), isolating context-length generalization as the sole variable.
3. A two-stage haystack filtering pipeline removes both distractor words with high semantic similarity to question keywords and any text that could serve as a plausible false answer, ensuring clean experimental conditions.

---

## Approach Details

### Method

NoLiMa follows the vanilla NIAH structure: a single needle is placed in a haystack of irrelevant text (book snippets), and the model must answer a question by finding the needle. The critical difference is that the question keyword W_q and the needle keyword W_n share no lexical overlap and are connected only by latent knowledge.

Each needle follows a template with three placeholders:
- **[CHAR]**: a randomly assigned character name (the correct answer)
- **W_n**: the needle keyword (e.g., a building, landmark, dietary restriction)
- **W_q**: the query keyword used in the question (e.g., a city, food, beverage)

Example (one-hop):
> Needle: "Actually, Yuki lives next to the **Semper Opera House**."
> Question: "Which character has been to **Dresden**?"

The model must infer that the Semper Opera House is in Dresden -- a latent association with zero token overlap.

Two-hop examples add a further reasoning step:
> Question: "Which character has been to **the state of Saxony**?"

Here the model must chain: Saxony --> Dresden --> Semper Opera House --> Yuki.

Each needle group also includes an **inverted** template, reversing the order of [CHAR] and W_n:
- **Default**: ". . . [CHAR] . . . W_n"
- **Inverted**: "W_n . . . [CHAR] . . ."

### Key Technical Components

**Needle Set Design.** 5 groups of needles with 2 word-order variations each (Table 7, Appendix A). Each group contains 2--6 keyword pairs, yielding 28 keyword pairs and 58 question-needle pairs total. Design constraints:
- Keywords ensure **simplicity**: the associations are clear without irrelevant context.
- Character names are drawn from a diverse pool and randomized to mitigate tokenization and ethnic bias (Navigli et al., 2023; Jiang et al., 2024). Names already in haystacks are excluded.
- W_n is **uniquely** associated with W_q (e.g., "Cambridge" is avoided because it maps to multiple countries).
- Language-specific markers (orthographic, morphological) are minimized.
- Preface phrases (e.g., "Actually," "In 2013, after waiting in line...") isolate needles from preceding context.

**Haystack Filtering Pipeline.** Two-stage process (Figure 1):
1. **Distractor Filtering**: Uses Contriever (Izacard et al., 2022) embeddings to find haystack words with high semantic or substring similarity to question keywords W_q. Top-20 similar words per W_q are manually inspected; sentences containing flagged words are removed.
2. **Filtering Undesired Answer Candidates**: A semi-automatic redaction process scans haystack text in chunks (1000-character chunks with 800-character stride, ~250 tokens each). Each chunk is paired with each question and fed to Llama 3.3 70B (instruction-tuned) with a short instruction and 4 few-shot examples (2 positive, 2 N/A). Flagged non-N/A responses are manually reviewed. Process repeats until no further removals are needed. Llama 3.3 70B achieves 99.8% on a 100-chunk control test, confirming it understands the filtering task (Section 4.2).

**Haystack Construction.** 10 open-license books, each covering at least 50K tokens. Haystacks are built by iteratively and randomly selecting a book, extracting a continuous snippet (under 250 tokens), and appending until the haystack exceeds 2K lines (>60K tokens). Random snippet concatenation mitigates potential memorization of publicly available books (Section 4.1).

**Literal Overlap Quantification.** ROUGE precision (R-1, R-2, R-L) measures how many question tokens occur in the context (Table 1):

| Benchmark | R-1 | R-2 | R-L |
|---|---|---|---|
| InfiniteBench QA (Zhang et al., 2024) | 0.966 | 0.545 | 0.960 |
| InfiniteBench MC (Zhang et al., 2024) | 0.946 | 0.506 | 0.932 |
| RULER QA (Hsieh et al., 2024) | 0.809 | 0.437 | 0.693 |
| HELMET RAG (Yen et al., 2024) | 0.689 | 0.304 | 0.555 |
| Vanilla NIAH (Kamradt, 2023) | 0.905 | 0.789 | 0.855 |
| RULER S-NIAH (Hsieh et al., 2024) | 0.571 | 0.461 | 0.500 |
| BABILong 0K (Kuratov et al., 2024) | 0.553 | 0.238 | 0.522 |
| **NoLiMa** | **0.069** | **0.002** | **0.067** |

### Experimental Setup

**Models.** 13 models claiming at least 128K context support (Table 8):
- Closed-source: GPT-4o, GPT-4o Mini, Gemini 1.5 Pro, Gemini 1.5 Flash, Gemini 2.0 Flash, Claude 3.5 Sonnet
- Open-weight: Llama 3.1 8B / 70B / 405B, Llama 3.3 70B, Mistral Large 2, Command R+, Jamba 1.5 Mini
- Reasoning models (for analysis): GPT-o1, GPT-o3 Mini, DeepSeek-R1-Distill-Llama-70B
- Extended evaluations (Appendix E): GPT-4.1 series, Gemini 2.5 Flash, Llama 4 Maverick/Scout, Gemma 3 series

Open-weight models deployed via vLLM (Kwon et al., 2023) with HuggingFace weights. Greedy decoding for standard models; default sampling for GPT-o1/o3 Mini; top-P (p = 0.95, temperature 0.6) for R1-based models. Max generation tokens: 192 (standard), 1536 (reasoning models, including reasoning + output) (Appendix C).

**Evaluation protocol.** Context lengths: 250, 500, 1K, 2K, 4K, 8K, 16K, 32K (and 64K, 128K for select models). Each needle placed 26 times at equal intervals across the context length. With 5 random haystacks, 58 question-needle pairs, and 26 placements, this yields **7,540 tests per context length** (Section 4.1).

**Metrics (Section 4.3):**
- **Accuracy**: proportion of tests where the model's output contains the correct character name.
- **Base score**: for each question-needle pair, average accuracy over 5 haystacks, then take the maximum across 250/500/1K contexts. Final base score is the mean of these maxima across all 58 pairs. This controls for inherent task difficulty independent of context length.
- **Effective length**: the maximum tested length at which the score remains above **85% of the base score** (adapted from Hsieh et al., 2024, who used a fixed 85.6% threshold based on Llama 2 at 4K).
- **Normalized score**: accuracy / base score.

### Key Results

**Main benchmark (Table 3):**

| Model | Claimed Length | Effective Length | Base Score (x0.85: Thr.) | 1K | 2K | 4K | 8K | 16K | 32K |
|---|---|---|---|---|---|---|---|---|---|
| GPT-4o | 128K | 8K | 99.3 (84.4) | 98.1 | 98.0 | 95.7 | 89.2 | 81.6 | 69.7 |
| Llama 3.3 70B | 128K | 2K | 97.3 (82.7) | 94.2 | 87.4 | 81.5 | 72.1 | 59.5 | 42.7 |
| Llama 3.1 405B | 128K | 2K | 94.7 (80.5) | 89.0 | 85.0 | 74.5 | 60.1 | 48.4 | 38.0 |
| Llama 3.1 70B | 128K | 2K | 94.5 (80.3) | 91.0 | 81.8 | 71.2 | 62.7 | 51.8 | 43.2 |
| Gemini 1.5 Pro | 2M | 2K | 92.6 (78.7) | 86.4 | 82.7 | 75.4 | 63.9 | 55.5 | 48.2 |
| Jamba 1.5 Mini | 256K | <1K | 92.4 (78.6) | 76.3 | 74.1 | 70.8 | 62.2 | 52.7 | 43.6 |
| Command R+ | 128K | <1K | 90.9 (77.3) | 77.0 | 73.5 | 66.2 | 39.5 | 21.3 | 7.4 |
| Gemini 2.0 Flash | 1M | 4K | 89.4 (76.0) | 87.7 | 87.5 | 77.9 | 64.7 | 48.2 | 41.0 |
| Mistral Large 2 | 128K | 2K | 87.9 (74.7) | 86.1 | 85.5 | 73.3 | 51.4 | 32.6 | 18.8 |
| Claude 3.5 Sonnet | 200K | 4K | 87.5 (74.4) | 85.4 | 84.0 | 77.6 | 61.7 | 45.7 | 29.8 |
| Gemini 1.5 Flash | 1M | <1K | 84.7 (72.0) | 68.6 | 61.6 | 51.0 | 44.4 | 35.5 | 28.6 |
| GPT-4o mini | 128K | <1K | 84.8 (72.1) | 67.7 | 58.2 | 44.2 | 32.6 | 20.6 | 13.7 |
| Llama 3.1 8B | 128K | 1K | 76.7 (65.2) | 65.7 | 54.4 | 44.1 | 31.9 | 22.6 | 14.2 |

- **At 32K, 11 out of 13 models drop below 50% of their base score** (Section 4.4).
- GPT-4o is the strongest, with effective length 8K, but still declines from 99.3% base to 69.7% at 32K.
- For comparison, Llama 3.1 70B achieves effective lengths of 16K on BABILong (QA1) and 32K on RULER, but only **2K** on NoLiMa (Section 4.4).
- Models with lower base scores (e.g., Claude 3.5 Sonnet, Gemini 2.0 Flash) sometimes show better **length generalization** than models with higher base scores (e.g., Llama 3.1 70B), achieving higher raw scores at 4K (Section 4.4).
- Model scaling improves performance (8B to 70B, Flash to Pro, mini to full), but benefits diminish at larger scales (70B to 405B gap is smaller than 8B to 70B) (Section 4.4).
- "Lite" models (Gemini 1.5 Flash, GPT-4o mini, Llama 3.1 8B) perform well at <1K but fail to generalize (Section 4.4).

**Extended evaluations (64K and 128K, Table 10, Appendix E):** GPT-4o maintained over 50% of its base score at 128K (56.0%). Gemini 2.0 Flash dropped to 16.4%. GPT-4.1 improved to effective length 16K but still dropped below 65% at 128K (64.7%).

### Latent Hops and Inversion Analysis

**One-hop vs. two-hop (Figure 2a, Section 4.4.1).** Two-hop tasks are harder at all context lengths, and the gap widens as context grows. GPT-4o handles both effectively up to 4K. At 32K, GPT-4o drops to 57.4% on two-hop (vs. 79.8% on one-hop); Llama 3.3 70B drops to 25.9% on two-hop (vs. 56.2% on one-hop) (Tables 11-12, Appendix F).

**Default vs. inverted order (Figure 2b, Section 4.4.1).** Inverted templates ("W_n . . . [CHAR]") are harder than default ("[CHAR] . . . W_n"). In the default order, the question's W_q can attend to W_n which already contains information about the character (mentioned earlier in sequence), allowing effective backtracing. In the inverted order, when W_q attends to W_n, the character has not yet been mentioned, forcing reliance on weaker signals, which deteriorate in longer contexts.

### Needle Placement Depth Analysis

A "lost-in-the-middle" effect (Liu et al., 2024) appears in one-hop tasks at 32K, with performance dipping when the needle is in the middle (Figure 3a). In two-hop tasks, however, **longer contexts dampen the entire performance distribution** -- performance declines even at the edges of the context window, unlike vanilla NIAH where edge placement reliably yields high accuracy (Figure 3b).

An **aligned-depth** analysis of the last 2K tokens (Figure 3c-d, Figure 4) -- where needle placements are aligned across context lengths -- reveals that:
- In one-hop tasks, plot lines drop toward the center (position-dependent, consistent with lost-in-the-middle) (Figure 3c).
- In two-hop tasks, plot lines remain **relatively stable** over the last 2K positions, but **context length significantly reduces the overall performance level** (Figure 3d). Since Llama 3.x uses RoPE (a relative PE), and the relative distance between question and needle is constant, position encoding cannot explain the performance drop. The limiting factor is the **increased number of tokens** the attention mechanism must process (Section 4.4.2).

### Chain-of-Thought and Reasoning Models

**CoT prompting on Llama 3.3 70B (Table 4, Section 4.4.3):**

| Setting | 4K | 8K | 16K | 32K |
|---|---|---|---|---|
| One-hop w/o CoT | 90.3 | 84.1 | 73.2 | 56.2 |
| One-hop w/ CoT | 95.6 | 91.1 | 82.6 | 60.6 |
| Increase rate | 5.9% | 8.3% | 12.8% | 7.8% |
| Two-hop w/o CoT | 70.7 | 57.4 | 42.7 | 25.9 |
| Two-hop w/ CoT | 82.4 | 70.1 | 56.7 | 34.3 |
| Increase rate | 16.5% | 22.1% | 32.7% | 32.4% |

CoT helps more on two-hop tasks and at longer contexts, but two-hop with CoT barely matches one-hop without CoT. The questions cannot be further decomposed into simpler steps -- the difficulty lies in reasoning through the latent association, not in multi-step decomposition (Section 4.4.3).

**Reasoning models on NoLiMa-Hard (Table 5, Section 4.4.3)** -- 10 hardest needle-question pairs from the 58 available:

| Model | Base Score | 4K | 8K | 16K | 32K |
|---|---|---|---|---|---|
| Llama 3.3 70B w/o CoT | 98.3 | 55.5 | 37.2 | 16.7 | 8.9 |
| Llama 3.3 70B w/ CoT | 97.1 | 73.0 | 51.2 | 31.8 | 10.1 |
| GPT-o1 | 99.9 | 92.0 | 78.0 | 60.1 | 31.1 |
| GPT-o3 Mini | 98.8 | 52.8 | 36.9 | 25.5 | 18.9 |
| DeepSeek R1-DL-70b | 99.9 | 91.4 | 75.5 | 49.4 | 20.7 |

Near-perfect base scores confirm the task is simple. All models drop below 50% at 32K. Reasoning models outperform CoT prompting but still fail to achieve full-length generalization (Section 4.4.3).

### Ablation Study: Literal Match Effect

**Direct questions (Table 6, Section 4.4.4)** -- asking about W_n directly, resembling vanilla NIAH:

| Setting | 8K | 16K | 32K |
|---|---|---|---|
| Direct | 98.3 | 98.5 | 98.5 |
| One-hop | 84.1 | 73.2 | 56.2 |
| One-hop w/ Literal Match (MC) | 98.7 | 97.4 | 93.1 |
| Two-hop | 57.4 | 42.7 | 25.9 |
| Two-hop w/ Literal Match (MC) | 96.3 | 94.6 | 87.2 |

Adding literal matches (via multiple-choice options containing the correct character name) dramatically simplifies the task, even when the underlying latent reasoning requirement is unchanged. The character names as answer options allow the model to focus its search within a smaller scope (Section 4.4.4).

**Distracting literal matches (Figure 5, Section 4.4.4).** Inserting a distractor sentence containing W_q (e.g., "There was an article about Dresden in the daily newspaper") but irrelevant to the question severely degrades performance. With distractors, GPT-4o's effective length drops to just 1K; Llama 3.3 70B performs even worse. Distractors are placed between the 20%--80% marks of context length, at least 20% of context length away from the needle (Appendix D). While adding distractors slightly lowers base scores (GPT-4o: 93.8, Llama 3.3 70B: 84.4), the normalized plots still clearly illustrate a performance drop at longer lengths (Section 4.4.4).

---

## Limitations and Failure Modes

1. **Small needle set.** The benchmark comprises only 58 question-needle pairs across 5 template groups. The limited variety means the benchmark tests a narrow range of associative link types (geographic landmarks, dietary restrictions). Generalizability to other kinds of latent associations is not validated. [Inference: not stated explicitly by authors.]

2. **English-only evaluation.** All needles, questions, and haystacks are in English. The paper does not address multilingual generalization of the literal-matching confound or NoLiMa performance.

3. **No fine-tuning or training interventions explored.** The paper evaluates only inference-time methods (standard prompting, CoT, reasoning models). Whether training-time interventions could improve latent associative retrieval is not investigated.

4. **Haystack filtering relies on a single model.** Llama 3.3 70B is used for the filtering pipeline; biases in this model could affect which content is flagged and removed. The 99.8% control test score is high but not perfect (Section 4.2).

5. **Manual review by a single author.** All manual reviews in both filtering steps were conducted by one author (footnote 4), introducing potential subjectivity.

6. **Limited context lengths for most models.** The main evaluation covers only up to 32K tokens; 64K and 128K are tested for only two models (GPT-4o and Gemini 2.0 Flash) with reduced placement count (11 instead of 26) (Appendix E).

7. **Base score variation across models.** Some models have substantially lower base scores (e.g., Llama 3.1 8B at 76.7%), making it harder to isolate context-length effects from general model capability differences. The normalized score partially addresses this.

---

## Conclusions

### Contributions

1. **Identification of literal matching as a pervasive confound.** Existing NIAH variants and downstream QA benchmarks contain substantial lexical overlap between questions and relevant context (ROUGE-1 up to 0.966), which allows models to exploit surface-level token matching rather than genuine reasoning (Table 1, Section 2).

2. **NoLiMa benchmark design.** A NIAH-style benchmark with ROUGE-1 of only 0.069 that isolates latent associative reasoning from surface matching, while remaining simple in short contexts (base scores 76.7%--99.3%) (Table 1, Table 3, Section 3).

3. **Sharp performance degradation without literal cues.** At 32K tokens, 11 of 13 models fall below 50% of their base score. Even GPT-4o drops from 99.3% to 69.7%. This contrasts with RULER and BABILong, where the same models achieve effective lengths of 16K--32K (Table 3, Section 4.4).

4. **Context length dominates over position in complex reasoning.** The aligned-depth analysis demonstrates that in two-hop scenarios, performance depends on total context length rather than needle position, implicating the attention mechanism's capacity to process many tokens without surface cues as the bottleneck (Figure 3c-d, Section 4.4.2).

5. **Quantification of literal match effect.** Direct ablations show that adding literal matches (via MC options) raises accuracy from 56.2% to 93.1% (one-hop) and 25.9% to 87.2% (two-hop) at 32K, while adding literal-match distractors reduces GPT-4o's effective length to 1K (Table 6, Figure 5, Section 4.4.4).

6. **Evaluation of CoT and reasoning models.** CoT prompting yields 5.9%--32.7% improvement depending on setting, and reasoning models (GPT-o1) outperform CoT at shorter lengths, but all models still drop below 50% at 32K on the hard subset (Tables 4-5, Section 4.4.3).

### Implications

1. **Benchmark scores may overestimate long-context capability.** High performance on literal-overlap benchmarks (RULER, vanilla NIAH) does not imply robust long-context utilization when surface cues are absent. Model developers and users should consider NoLiMa-style evaluations alongside traditional benchmarks.

2. **RAG systems are vulnerable to lexical gap failures.** In search engines or RAG systems, a relevant document with the correct answer may have a lexical gap with the query. If retrieved alongside documents with higher lexical similarity, models may struggle to extract the correct answer. [Speculative: stated by authors in Section 5 but not empirically validated.]

3. **Attention mechanism improvements needed.** The fundamental bottleneck appears to be the attention mechanism's difficulty in processing large numbers of tokens without repetitive patterns to anchor on. Architectural innovations beyond standard self-attention may be required. [Speculative: implication of findings.]

---

## Key Claims

1. **C1: Literal overlap is pervasive in existing benchmarks.** ROUGE-1 precision between questions and relevant context ranges from 0.553 (BABILong 0K) to 0.966 (InfiniteBench QA), providing surface cues that simplify retrieval (Table 1, Section 2). Status: **supported**.

2. **C2: NoLiMa eliminates literal matching confounds.** With ROUGE-1 of only 0.069 and base scores of 76.7%--99.3%, the benchmark provides a clean measure of latent associative reasoning independent of task complexity (Table 1, Table 3, Section 3). Status: **supported**.

3. **C3: Performance collapses at 32K without literal cues.** 11 of 13 models drop below 50% of their base score at 32K. GPT-4o, the strongest performer, drops from 99.3% to 69.7% (Table 3, Section 4.4). Status: **supported**.

4. **C4: Two-hop reasoning amplifies context-length degradation.** The gap between one-hop and two-hop performance widens with increasing context: at 32K, GPT-4o scores 79.8% (one-hop) vs. 57.4% (two-hop); Llama 3.3 70B scores 56.2% vs. 25.9% (Figure 2a, Tables 11-12, Section 4.4.1). Status: **supported**.

5. **C5: Context length, not position, is the bottleneck in complex reasoning.** In the aligned-depth analysis of two-hop tasks, performance remains stable across the last 2K positions but drops with total context length, even though RoPE maintains constant relative distances (Figure 3c-d, Section 4.4.2). Status: **supported**.

6. **C6: CoT and reasoning models cannot fully compensate.** On NoLiMa-Hard, GPT-o1 achieves 92.0% at 4K but drops to 31.1% at 32K. Two-hop with CoT barely matches one-hop without CoT (Tables 4-5, Section 4.4.3). Status: **supported**.

7. **C7: Literal matches both simplify and distract.** Adding MC answer options raises two-hop accuracy from 25.9% to 87.2% at 32K. Adding irrelevant literal-match distractors reduces GPT-4o's effective length from 8K to 1K (Table 6, Figure 5, Section 4.4.4). Status: **supported**.

---

## Open Questions

1. **Can architectural improvements beyond attention address latent association retrieval in long contexts?** The paper identifies attention mechanism overload as the bottleneck but does not propose solutions. Alternative architectures (state-space models, hybrid approaches) are not evaluated. Not yet addressed.

2. **What is the mechanistic explanation for inversion difficulty?** The paper hypothesizes that inverted templates force reliance on weaker signals because the character name follows W_n in sequence, but deeper mechanistic analysis is explicitly left for future work (Section 4.4.1). Not yet addressed.

3. **How do NoLiMa findings translate to real-world downstream tasks?** The paper speculates about RAG implications (Section 5) but does not empirically validate on multi-document QA or retrieval-augmented settings. Not yet addressed.

4. **Can training methods improve latent associative reasoning without literal cues?** Only inference-time interventions (CoT, reasoning models) are tested. Whether targeted fine-tuning, data augmentation, or curriculum learning could improve performance is unexplored. Not yet addressed.

---

## Core References and Why They Are Referenced

### Needle-in-a-Haystack Foundations

- **Kamradt (2023)** -- *Needle in a Haystack -- Pressure Testing LLMs.* Introduced the original NIAH benchmark that NoLiMa extends. NoLiMa's "Direct" ablation condition replicates vanilla NIAH to demonstrate how literal matches simplify the task.
- **Mohtashami & Jaggi (2023)** -- *Random-Access Infinite Context Length for Transformers.* Co-originator of the NIAH evaluation paradigm.

### Long-Context Benchmarks

- **Hsieh et al. (2024)** -- *RULER: What's the Real Context Size of Your Long-Context Language Models?* Provides S-NIAH and multi-needle NIAH extensions that NoLiMa contrasts against. NoLiMa adopts the concept of **effective length** from RULER (adapting the 85% threshold to be relative to each model's base score rather than a fixed value).
- **Kuratov et al. (2024)** -- *BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack.* Provides fact-chaining NIAH extensions. NoLiMa notes that BABILong's counting task achieves only 28% at 0K, confounding task difficulty with context-length difficulty.
- **Zhang et al. (2024)** -- *InfiniteBench: Extending Long Context Evaluation Beyond 100K Tokens.* Used in Table 1 as a high-literal-overlap benchmark (R-1 = 0.966 for QA).
- **Yen et al. (2024)** -- *HELMET: How to Evaluate Long-Context Language Models Effectively and Thoroughly.* HELMET RAG used in Table 1 (R-1 = 0.689).
- **Goldman et al. (2024)** -- *Is It Really Long Context If All You Need Is Retrieval?* Supports NoLiMa's argument by categorizing long-context tasks as association recall.

### Attention Mechanism and Association Recall

- **Olsson et al. (2022)** -- *In-Context Learning and Induction Heads.* Provides the mechanistic basis for NoLiMa's argument: attention excels at recalling repetitive patterns (induction heads), which explains why literal matches simplify NIAH.
- **Arora et al. (2024)** -- *Zoology: Measuring and Improving Recall in Efficient Language Models.* Further supports that attention is inherently adept at identifying associations present in the input.

### Lost-in-the-Middle Effect

- **Liu et al. (2024)** -- *Lost in the Middle: How Language Models Use Long Contexts.* NoLiMa's needle placement analysis confirms the lost-in-the-middle effect in one-hop tasks, but shows that in two-hop scenarios, context length dominates over position.

### Positional Encodings

- **Su et al. (2024)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* RoPE is used in the Llama 3.x models evaluated; the aligned-depth analysis uses RoPE's relative-distance property to disentangle position from context-length effects.

### Context Extension Methods

- **Chen et al. (2023)** -- *Extending Context Window of Large Language Models via Positional Interpolation.* Cited as one of the long-context scaling methods that enabled the models evaluated by NoLiMa.
- **Peng et al. (2024)** -- *YaRN: Efficient Context Window Extension of Large Language Models.* Cited alongside PI as a key context-extension method.

### Reasoning and Prompting

- **Wei et al. (2022)** -- *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models.* Foundation for the CoT analysis in Section 4.4.3.
- **OpenAI et al. (2024)** -- *OpenAI o1 System Card.* GPT-o1 is the primary reasoning model evaluated on NoLiMa-Hard.
- **DeepSeek-AI et al. (2025)** -- *DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning.* DeepSeek-R1-Distill-Llama-70B evaluated on NoLiMa-Hard.

### Haystack Filtering

- **Izacard et al. (2022)** -- *Unsupervised Dense Information Retrieval with Contrastive Learning.* Contriever embeddings are used in the distractor filtering stage of the haystack construction pipeline.

### Models Evaluated

- **Hurst et al. (2024)** -- *GPT-4o System Card.* GPT-4o is the top performer on NoLiMa.
- **Gemini Team et al. (2023; 2024)** -- *Gemini family.* Gemini 1.5 Pro/Flash and 2.0 Flash evaluated.
- **Dubey et al. (2024)** -- *The Llama 3 Herd of Models.* Llama 3.1 8B/70B/405B evaluated.
- **Meta (2024)** -- *Llama 3.3 Model Card.* Llama 3.3 70B evaluated; also used for haystack filtering.
- **Anthropic (2024)** -- *Claude 3.5 Sonnet Model Card Addendum.* Claude 3.5 Sonnet evaluated.
