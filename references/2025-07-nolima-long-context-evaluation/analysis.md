# NoLiMa: Long-Context Evaluation Beyond Literal Matching

**Authors:** Ali Modarressi, Hanieh Deilamsalehy, Franck Dernoncourt, Trung Bui, Ryan Rossi, Seunghyun Yoon, Hinrich Schutze (LMU Munich, MCML, Adobe Research)
**Date:** July 2025, ICML 2025 (PMLR 267); arXiv:2502.05167

---

## Core Research Problem

Needle-in-a-haystack (NIAH) tests are the dominant synthetic evaluation for long-context LLMs: a relevant "needle" is hidden in a long irrelevant "haystack," and the model must retrieve it. Extensions of NIAH add multiple needles, fact-chaining, distractors, or in-context reasoning (Hsieh et al., 2024; Levy et al., 2024; Kuratov et al., 2024). However, in all these variants the question and the needle share substantial **literal lexical overlap** -- tokens from the question appear verbatim in the needle or surrounding context.

The attention mechanism is inherently adept at identifying and recalling repetitive patterns (Olsson et al., 2022; Arora et al., 2024). When literal matches exist, models can exploit surface-level token matching to locate the needle, sidestepping genuine associative reasoning. This confound also extends to downstream QA benchmarks: long-document and multi-document QA datasets (Zhang et al., 2024; Bai et al., 2024; Yen et al., 2024) implicitly contain literal overlap between questions and relevant passages.

Quantitatively, popular benchmarks exhibit high ROUGE precision between question and context: Vanilla NIAH reaches R-1 = 0.905, RULER S-NIAH reaches 0.571, and InfBench QA reaches 0.966. Some benchmarks (e.g., BABILong counting at 28% accuracy at 0K, or Ancestral Tree Challenge) address this by making tasks inherently too complex even in short contexts, conflating task difficulty with context-length difficulty.

The core challenge is: **how to evaluate whether LLMs can retrieve information from long contexts when the question and the relevant fact share no literal overlap, requiring latent associative reasoning instead of surface matching.**

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

Here the model must chain: Saxony → Dresden → Semper Opera House → Yuki.

Each needle group also includes an **inverted** template, reversing the order of [CHAR] and W_n:
- **Default**: ". . . [CHAR] . . . W_n"
- **Inverted**: "W_n . . . [CHAR] . . ."

### Key Technical Components

**Needle Set Design.** 5 groups of needles with 2 word-order variations each. Each group contains 2--6 keyword pairs, yielding 28 keyword pairs and 58 question-needle pairs total. Design constraints:
- Keywords ensure **simplicity**: the associations are clear without irrelevant context.
- Character names are drawn from a diverse pool and randomized to mitigate tokenization and ethnic bias (Navigli et al., 2023; Jiang et al., 2024). Names already in haystacks are excluded.
- W_n is **uniquely** associated with W_q (e.g., "Cambridge" is avoided because it maps to multiple countries).
- Language-specific markers (orthographic, morphological) are minimized.
- Preface phrases (e.g., "Actually," "In 2013, after waiting in line...") isolate needles from preceding context.

**Haystack Filtering Pipeline.** Two-stage process:
1. **Distractor Filtering**: Uses Contriever (Izacard et al., 2022) embeddings to find haystack words with high semantic or substring similarity to question keywords W_q. Top-20 similar words per W_q are manually inspected; sentences containing flagged words are removed.
2. **Filtering Undesired Answer Candidates**: A semi-automatic redaction process scans haystack text in chunks (1000-character chunks with 800-character stride, ~250 tokens each). Each chunk is paired with each question and fed to Llama 3.3 70B (instruction-tuned) with a short instruction and 4 few-shot examples (2 positive, 2 N/A). Flagged non-N/A responses are manually reviewed. Process repeats until no further removals are needed. Llama 3.3 70B achieves 99.8% on a 100-chunk control test, confirming it understands the filtering task.

**Haystack Construction.** 10 open-license books, each covering at least 50K tokens. Haystacks are built by iteratively and randomly selecting a book, extracting a continuous snippet (under 250 tokens), and appending until the haystack exceeds 2K lines (>60K tokens). Random snippet concatenation mitigates potential memorization of publicly available books.

**Literal Overlap Quantification.** ROUGE precision (R-1, R-2, R-L) measures how many question tokens occur in the context:

| Benchmark | R-1 | R-2 | R-L |
|---|---|---|---|
| InfBench QA (Zhang et al., 2024) | 0.966 | 0.545 | 0.960 |
| InfBench MC (Zhang et al., 2024) | 0.946 | 0.506 | 0.932 |
| RULER QA (Hsieh et al., 2024) | 0.809 | 0.437 | 0.693 |
| HELMET RAG (Yen et al., 2024) | 0.689 | 0.304 | 0.555 |
| Vanilla NIAH (Kamradt, 2023) | 0.905 | 0.789 | 0.855 |
| RULER S-NIAH (Hsieh et al., 2024) | 0.571 | 0.461 | 0.500 |
| BABILong 0K (Kuratov et al., 2024) | 0.553 | 0.238 | 0.522 |
| **NoLiMa** | **0.069** | **0.002** | **0.067** |

### Experimental Setup

**Models.** 13 models claiming at least 128K context support:
- Closed-source: GPT-4o, GPT-4o Mini, Gemini 1.5 Pro, Gemini 1.5 Flash, Gemini 2.0 Flash, Claude 3.5 Sonnet
- Open-weight: Llama 3.1 8B / 70B / 405B, Llama 3.3 70B, Mistral Large 2, Command R+, Jamba 1.5 Mini
- Reasoning models (for analysis): GPT-o1, GPT-o3 Mini, DeepSeek-R1-Distill-Llama-70B
- Extended evaluations (Appendix E): GPT-4.1 series, Gemini 2.5 Flash, Llama 4 Maverick/Scout, Gemma 3 series

Open-weight models deployed via vLLM (Kwon et al., 2023) with HuggingFace weights. Greedy decoding for standard models; default sampling for GPT-o1/o3 Mini; top-P (p = 0.95, temperature 0.6) for R1-based models. Max generation tokens: 192 (standard), 1536 (reasoning models, including reasoning + output).

**Evaluation protocol.** Context lengths: 250, 500, 1K, 2K, 4K, 8K, 16K, 32K (and 64K, 128K for select models). Each needle placed 26 times at equal intervals across the context length. With 5 random haystacks, 58 question-needle pairs, and 26 placements, this yields **7,540 tests per context length**.

**Metrics.**
- **Accuracy**: proportion of tests where the model's output contains the correct character name.
- **Base score**: for each question-needle pair, average accuracy over 5 haystacks, then take the maximum across 250/500/1K contexts. Final base score is the mean of these maxima across all 58 pairs. This controls for inherent task difficulty independent of context length.
- **Effective length**: the maximum tested length at which the score remains above **85% of the base score** (adapted from Hsieh et al., 2024, who used a fixed 85.6% threshold).
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

- **At 32K, 11 out of 13 models drop below 50% of their base score.**
- GPT-4o is the strongest, with effective length 8K, but still declines from 99.3% base to 69.7% at 32K.
- For comparison, Llama 3.1 70B achieves effective lengths of 16K on BABILong (QA1) and 32K on RULER, but only **2K** on NoLiMa.
- Models with lower base scores (e.g., Claude 3.5 Sonnet, Gemini 2.0 Flash) sometimes show better **length generalization** than models with higher base scores (e.g., Llama 3.1 70B), achieving higher raw scores at 4K.
- Model scaling improves performance (8B → 70B, Flash → Pro, mini → full), but benefits diminish at larger scales (70B → 405B gap is smaller than 8B → 70B).
- "Lite" models (Gemini 1.5 Flash, GPT-4o mini, Llama 3.1 8B) perform well at <1K but fail to generalize.

**Extended evaluations (64K and 128K, Appendix E):** GPT-4o maintained over 50% of its base score at 128K (56.0%). Gemini 2.0 Flash dropped to 16.4%. GPT-4.1 improved to effective length 16K but still dropped below 65% at 128K.

### Latent Hops and Inversion Analysis

**One-hop vs. two-hop.** Two-hop tasks are harder at all context lengths, and the gap widens as context grows. GPT-4o handles both effectively up to 4K. At 32K, GPT-4o drops to 57.4% on two-hop (vs. 79.8% on one-hop); Llama 3.3 70B drops to 25.9% on two-hop (vs. 56.2% on one-hop).

**Default vs. inverted order.** Inverted templates ("[W_n] . . . [CHAR]") are harder than default ("[CHAR] . . . [W_n]"). In the default order, the question's W_q can attend to W_n which already contains information about the character (mentioned earlier in sequence), allowing effective backtracing. In the inverted order, when W_q attends to W_n, the character has not yet been mentioned, forcing reliance on weaker signals, which deteriorate in longer contexts.

### Needle Placement Depth Analysis

A "lost-in-the-middle" effect (Liu et al., 2024) appears in one-hop tasks at 32K, with performance dipping when the needle is in the middle. In two-hop tasks, however, **longer contexts dampen the entire performance distribution** -- performance declines even at the edges of the context window, unlike vanilla NIAH where edge placement reliably yields high accuracy.

An **aligned-depth** analysis of the last 2K tokens (where needle placements are aligned across context lengths) reveals that:
- In one-hop tasks, plot lines drop toward the center (position-dependent, consistent with lost-in-the-middle).
- In two-hop tasks, plot lines remain **relatively stable** over the last 2K positions, but **context length significantly reduces the overall performance level**. Since Llama 3.x uses RoPE (a relative PE), and the relative distance between question and needle is constant, position encoding cannot explain the performance drop. The limiting factor is the **increased number of tokens** the attention mechanism must process.

### Chain-of-Thought and Reasoning Models

**CoT prompting on Llama 3.3 70B:**

| Setting | 4K | 8K | 16K | 32K |
|---|---|---|---|---|
| One-hop w/o CoT | 90.3 | 84.1 | 73.2 | 56.2 |
| One-hop w/ CoT | 95.6 | 91.1 | 82.6 | 60.6 |
| Increase rate | 5.9% | 8.3% | 12.8% | 7.8% |
| Two-hop w/o CoT | 70.7 | 57.4 | 42.7 | 25.9 |
| Two-hop w/ CoT | 82.4 | 70.1 | 56.7 | 34.3 |
| Increase rate | 16.5% | 22.1% | 32.7% | 32.4% |

CoT helps more on two-hop tasks and at longer contexts, but two-hop with CoT barely matches one-hop without CoT. The questions cannot be further decomposed into simpler steps -- the difficulty lies in reasoning through the latent association, not in multi-step decomposition.

**Reasoning models on NoLiMa-Hard** (10 hardest needle-question pairs):

| Model | Base Score | 4K | 8K | 16K | 32K |
|---|---|---|---|---|---|
| Llama 3.3 70B w/o CoT | 98.3 | 55.5 | 37.2 | 16.7 | 8.9 |
| Llama 3.3 70B w/ CoT | 97.1 | 73.0 | 51.2 | 31.8 | 10.1 |
| GPT-o1 | 99.9 | 92.0 | 78.0 | 60.1 | 31.1 |
| GPT-o3 Mini | 98.8 | 52.8 | 36.9 | 25.5 | 18.9 |
| DeepSeek R1-DL-70b | 99.9 | 91.4 | 75.5 | 49.4 | 20.7 |

Near-perfect base scores confirm the task is simple. All models drop below 50% at 32K. Reasoning models outperform CoT prompting but still fail to achieve full-length generalization.

### Ablation Study: Literal Match Effect

**Direct questions** (asking about W_n directly, resembling vanilla NIAH):

| Setting | 8K | 16K | 32K |
|---|---|---|---|
| Direct | 98.3 | 98.5 | 98.5 |
| One-hop | 84.1 | 73.2 | 56.2 |
| One-hop w/ Literal Match (MC) | 98.7 | 97.4 | 93.1 |
| Two-hop | 57.4 | 42.7 | 25.9 |
| Two-hop w/ Literal Match (MC) | 96.3 | 94.6 | 87.2 |

Adding literal matches (via multiple-choice options containing the correct character name) dramatically simplifies the task, even when the underlying latent reasoning requirement is unchanged. The character names as answer options allow the model to focus its search within a smaller scope.

**Distracting literal matches.** Inserting a distractor sentence containing W_q (e.g., "There was an article about Dresden in the daily newspaper") but irrelevant to the question severely degrades performance. With distractors, GPT-4o's effective length drops to just 1K; Llama 3.3 70B performs even worse. Distractors are placed between the 20%--80% marks of context length, at least 20% of context length away from the needle.

---

## Conclusions

1. **Literal matches are a pervasive confound in long-context benchmarks.** Existing NIAH variants and downstream QA benchmarks contain substantial lexical overlap between questions and relevant context (ROUGE-1 up to 0.966), which allows models to exploit surface-level token matching rather than genuine reasoning.

2. **NoLiMa isolates latent associative reasoning from surface matching.** With ROUGE-1 of only 0.069, the benchmark provides a clean measure of whether models can retrieve information through world knowledge and commonsense associations rather than literal cues.

3. **Performance degrades sharply with context length when literal matches are absent.** At 32K tokens, 11 of 13 models fall below 50% of their base score. Even GPT-4o, the strongest performer, drops from 99.3% to 69.7%. This contrasts dramatically with RULER and BABILong, where the same models achieve effective lengths of 16K--32K.

4. **The attention mechanism is the bottleneck.** The aligned-depth analysis demonstrates that performance depends more on total context length than on needle position, especially in two-hop scenarios. With relative position encodings (RoPE), position alone cannot explain the degradation -- the sheer volume of tokens overwhelms attention when surface cues are absent.

5. **Two-hop reasoning amplifies the challenge.** Adding a second associative hop widens the performance gap at every context length. Models that handle one-hop well at 4K often fail on two-hop at the same length, and the gap widens further at 8K+.

6. **CoT and reasoning models improve but do not solve the problem.** CoT prompting yields 5.9%--32.7% improvement depending on setting, and GPT-o1 outperforms CoT at shorter lengths, but all models still drop below 50% at 32K on the hard subset. The fundamental difficulty -- attending to the right tokens in a long context without literal cues -- remains unresolved.

7. **Literal matches as distractors are actively harmful.** When irrelevant sentences share tokens with the question, models are drawn to those surface matches and away from the latent-association needle, reducing effective length to as low as 1K even for GPT-4o.

8. **Implications for downstream applications.** In RAG systems or search engines, a relevant document with the correct answer may have a lexical gap with the query. If retrieved alongside documents with higher lexical similarity, models may struggle to extract the correct answer due to distraction by surface overlap.

---

## Core References and Why They Are Referenced

### Needle-in-a-Haystack Foundations

- **Kamradt (2023)** -- *Needle in a Haystack -- Pressure Testing LLMs.* Introduced the original NIAH benchmark that NoLiMa extends. NoLiMa's "Direct" ablation condition replicates vanilla NIAH to demonstrate how literal matches simplify the task.
- **Mohtashami & Jaggi (2023)** -- *Random-Access Infinite Context Length for Transformers.* Co-originator of the NIAH evaluation paradigm.

### Long-Context Benchmarks

- **Hsieh et al. (2024)** -- *RULER: What's the Real Context Size of Your Long-Context Language Models?* Provides the S-NIAH and multi-needle NIAH extensions that NoLiMa contrasts against. NoLiMa adopts the concept of **effective length** from RULER (adapting the 85% threshold to be relative to each model's base score rather than a fixed value).
- **Kuratov et al. (2024)** -- *BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack.* Provides fact-chaining NIAH extensions. NoLiMa notes that BABILong's counting task achieves only 28% at 0K, confounding task difficulty with context-length difficulty.
- **Zhang et al. (2024)** -- *InfBench: Extending Long Context Evaluation Beyond 100K Tokens.* Used in Table 1 as a high-literal-overlap benchmark (R-1 = 0.966 for QA).
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

#### Cross-References in Available Papers

- **Lost in the Middle (Liu et al., 2024)** (`2024-02-lost-in-the-middle`): NoLiMa directly references the "lost-in-the-middle" effect in its needle placement depth analysis (Section 4.4.2, Figure 3a). The NoLiMa findings refine this observation: the lost-in-the-middle pattern holds for one-hop tasks but is overshadowed by context-length effects in two-hop scenarios.
- **RULER (Hsieh et al., 2024)** (`2024-10-ruler-context-size`): NoLiMa adopts RULER's concept of effective length (Section 4.3) and contrasts against RULER's S-NIAH variant in Table 1 (R-1 = 0.571). Llama 3.1 70B achieves an effective length of 32K on RULER but only 2K on NoLiMa, directly demonstrating that literal matches inflate effective-length estimates. The "Direct" ablation (Table 6) at 98.3%--98.5% accuracy at 8K--32K mirrors RULER-style performance.
- **Positional Interpolation (Chen et al., 2023)** (`2023-06-pi-positional-interpolation`): Cited in NoLiMa's introduction as one of the methods that enabled the long-context capabilities being evaluated.
- **YaRN (Peng et al., 2024)** (`2024-05-yarn-context-extension`): Cited alongside PI as a context-extension method.
- **DroPE** (`2025-12-drope-dropping-positional-embeddings`): Both papers evaluate long-context performance using NIAH-based tests and both discuss attention mechanisms as limiting factors. DroPE focuses on extending context via positional embedding modification, while NoLiMa evaluates existing models' inherent limitations. NoLiMa's finding that RoPE's relative distance property cannot explain degradation at fixed depth but varying context length is directly relevant to DroPE's motivation for modifying positional embeddings.
