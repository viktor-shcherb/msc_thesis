# Ada-LEval: Evaluating Long-Context LLMs with Length-Adaptable Benchmarks

**Authors:** Chonghua Wang, Haodong Duan, Songyang Zhang, Dahua Lin, Kai Chen (Shanghai AI Laboratory, Shanghai Jiao Tong University)
**Date:** June 2024, NAACL 2024 (arXiv:2404.06480)

---

## Core Research Problem

Existing long-context benchmarks such as L-Eval (An et al., 2023) and LongBench (Bai et al., 2023) suffer from three limitations. First, they integrate test samples of varying lengths (from 2k to ~32k tokens) into a single evaluation, making it difficult to assess model capabilities at specific length ranges. Second, they do not cover the ultra-long setting (32k+ tokens) that the latest LLMs claim to support -- GPT-4-Turbo (128k tokens), Claude-2.1 (200k tokens), and Kimi Chat (200k Chinese characters). Third, their reliance on traditional QA and summarization tasks does not require comprehensive content understanding; many questions can be answered from a small portion of the input.

Prior benchmarks like SCROLLS (Shaham et al., 2022) established multi-task long-text evaluation but are limited to moderate lengths and do not provide mechanisms for controlling test case length. L-Eval and LongBench offer broader task coverage but use fixed-length documents and open-ended metrics (F1, ROUGE) that may not align with human judgments.

**The core challenge is how to build a length-adaptable benchmark that requires full-text comprehension, scales to ultra-long contexts (128k tokens), and provides precise accuracy-based evaluation.**

---

## Problem Solutions

Ada-LEval introduces two tasks -- TSort (text segment ordering) and BestAnswer (best answer selection) -- that are length-adaptable, require full-text comprehension, and use exact accuracy metrics.

1. **Controllable length.** Test case length is tuned by adjusting the number and length of text segments (TSort) or the number of distractor answers (BestAnswer), producing samples from 1k to 128k tokens.
2. **Full-text comprehension required.** Both tasks mandate reading the entire input: TSort requires understanding all segments to determine their order; BestAnswer requires comparing all candidate answers to identify the best one.
3. **Precise accuracy measurement.** TSort has a single correct ordering; BestAnswer uses the answer explicitly accepted by the original questioner as ground truth. No subjective metrics like ROUGE or F1 are needed.

---

## Approach Details

### Method

Ada-LEval provides two complementary tasks designed for length-adaptable evaluation of long-context LLMs.

**TSort.** The model receives N shuffled text segments extracted from contiguous chapters of a book, along with adjacent paragraphs before and after the chapters as contextual hints. The task is to sort the segments into their original order. A response is correct only if it exactly matches the original sequence. For long-context settings (2k--16k), N is fixed at 4, giving a random guess accuracy of 1/4! = 1/24 ≈ 4.2%.

**BestAnswer.** The model receives a programming question from Stack Overflow and a set of candidate answers. The ground truth is the answer explicitly accepted by the original asker. Distractor answers include both intra-question answers (other answers to the same question, posted before the accepted answer) and inter-question answers (answers from questions with similar tags). Random guess accuracy is 1/N, where N varies per question based on the number of candidates at each length setting.

### Key Technical Components

**Source data.** TSort uses BookSum (Kryściński et al., 2021), derived from Project Gutenberg. Genres with non-sequential structure (epistolary literature, poetry) are excluded. Chapter numbers and annotations are removed to prevent superficial cue exploitation. BestAnswer uses threads from 23 Stack Overflow tags (JavaScript, Python, C++, etc.), with the top 2,500 questions per tag selected by popularity.

**Length control.** For TSort, the segment count (N=4) and per-segment length upper limit are fixed at each target length; a stride parameter between beginning paragraphs generates diverse test cases. For BestAnswer, the same questions are reused across all long-context length settings, with the number of inter-question distractor answers adjusted to reach the target length. Under ultra-long settings, tag similarity constraints are relaxed to provide enough distractors.

**Data statistics (GPT-4 CL100K tokenizer):**

| Task | Setting | Total Cases Built | Max Tokens | Avg Tokens |
|---|---|---|---|---|
| TSort | 2k | 5,123 | 2,000 | 1,816 |
| TSort | 4k | 5,451 | 4,000 | 3,724 |
| TSort | 8k | 5,324 | 8,000 | 7,663 |
| TSort | 16k | 4,957 | 16,000 | 15,662 |
| TSort | 32k | 2,206 | 32,000 | 31,226 |
| TSort | 64k | 1,658 | 64,000 | 62,407 |
| TSort | 128k | 782 | 127,800 | 121,488 |
| BestAnswer | 1k | 7,526 | 1,128 | 955 |
| BestAnswer | 16k | 7,526 | 15,964 | 15,646 |
| BestAnswer | 32k | 200 | 32,974 | 32,329 |
| BestAnswer | 64k | 200 | 64,216 | 63,274 |
| BestAnswer | 128k | 200 | 127,059 | 126,098 |

**Evaluation protocol.** Zero-shot evaluation for all models. Open-source models use 1,000-testcase subsets; proprietary models use 200-testcase subsets (long-context) and 50-testcase subsets (ultra-long). Instruction following rate and copy instruction rate are measured alongside accuracy. Evaluation conducted via OpenCompass (Contributors, 2023).

### Experimental Setup

**Models evaluated:**

| Model | Type | Context Window |
|---|---|---|
| GPT-4-Turbo-0125 | Proprietary | 128k |
| GPT-4-Turbo-1106 | Proprietary | 128k |
| GPT-3.5-Turbo-1106 | Proprietary | 16k |
| Claude-2 | Proprietary | 100k |
| LongChat-7b-v1.5-32k | Open-source | 32k |
| ChatGLM2-6B-32k | Open-source | 32k |
| ChatGLM3-6B-32k | Open-source | 32k |
| Vicuna-7b-v1.5-16k | Open-source | 16k |
| Vicuna-13b-v1.5-16k | Open-source | 16k |
| InternLM2-7b | Open-source | -- |

Ultra-long evaluation (32k--128k) is limited to GPT-4-Turbo, Claude-2, Claude-2.1, and InternLM2-7b (BestAnswer only).

### Key Results

**TSort (long-context, N=4, random guess ≈ 4.2%):**

| Model | 2k | 4k | 8k | 16k |
|---|---|---|---|---|
| GPT-4-Turbo-0125 | 15.5 | 16.5 | 8.5 | 5.5 |
| GPT-4-Turbo-1106 | 18.5 | 15.5 | 7.5 | 3.5 |
| GPT-3.5-Turbo-1106 | 4.0 | 4.5 | 4.5 | 5.5 |
| Claude-2 | 5.0 | 5.0 | 4.5 | 3.0 |
| Vicuna-13b-v1.5-16k | 5.4 | 5.0 | 2.4 | 3.1 |
| Random Guess | 4.2 | 4.2 | 4.2 | 4.2 |

- **Only GPT-4-Turbo significantly exceeds random at 2k--8k.** At 16k, GPT-4-Turbo deteriorates to random-guess level. All other models perform at or near random across all settings.

**BestAnswer (long-context):**

| Model | 1k | 2k | 4k | 8k | 16k |
|---|---|---|---|---|---|
| GPT-4-Turbo-0125 | 73.5 | 73.5 | 65.5 | 56.5 | 44.5 |
| GPT-4-Turbo-1106 | 74.0 | 73.5 | 67.5 | 53.5 | 44.0 |
| GPT-3.5-Turbo-1106 | 61.5 | 48.5 | 41.5 | 17.0 | 2.5 |
| Claude-2 | 65.0 | 43.5 | 23.5 | 17.0 | 11.0 |
| InternLM2-7b | 58.6 | 49.5 | 33.9 | 13.4 | 0.8 |
| Random Guess | 26.7 | 10.1 | 4.5 | 2.3 | 1.1 |

- **GPT-4-Turbo achieves state-of-the-art on BestAnswer**, maintaining 44.5% at 16k with ~100 distractors. Claude-2 is second at 11%. Open-source models decline to random by 8k--16k.

**Ultra-long-context results (32k--128k):**

| Task | Model | 32k | 64k | 128k |
|---|---|---|---|---|
| TSort | GPT-4-Turbo-0125 | 2.0 | 4.0 | 2.0 |
| TSort | GPT-4-Turbo-1106 | 6.0 | 6.0 | 6.0 |
| TSort | Claude-2 / Claude-2.1 | 0.0 | 0.0 | 0.0 |
| TSort | Random Guess | 4.2 | 4.2 | 4.2 |
| BestAnswer | GPT-4-Turbo-0125 | 30.0 | 0.0 | 0.0 |
| BestAnswer | GPT-4-Turbo-1106 | 16.0 | 0.0 | 0.0 |
| BestAnswer | Claude-2 / Claude-2.1 | 4.0 | 0.0 | 0.0 |
| BestAnswer | Random Guess | 0.6 | 0.3 | 0.1 |

- **All models collapse at 64k+ tokens on BestAnswer.** No model produces any correct answers at 64k or 128k. On TSort, GPT-4-Turbo achieves only random-level accuracy across all ultra-long settings; Claude produces zero correct answers.

### Ablation Studies

**Perplexity evaluation on TSort.** When open-source models evaluate TSort via perplexity (selecting the lowest-perplexity permutation among all 24 orderings), accuracy jumps dramatically: Vicuna-13b-v1.5-16k achieves 79.3--89.2% (vs. 2.4--5.4% generative). This shows models can distinguish correct ordering internally but fail to follow instructions and produce the correct output in generative mode.

| Model (PPL Eval) | 2k | 4k | 8k |
|---|---|---|---|
| Vicuna-13b-v1.5-16k | 79.3 | 86.7 | 89.2 |
| Vicuna-7b-v1.5-16k | 70.1 | 78.3 | 77.7 |
| LongChat-7b-v1.5-32k | 60.9 | 68.3 | 77.4 |
| ChatGLM3-6B-32k | 50.1 | 57.0 | 59.3 |
| Random Guess | 4.2 | 4.2 | 4.2 |

**Position bias in BestAnswer.** All models show significant position bias. Most models achieve higher accuracy when the ground-truth answer is positioned at the beginning. GPT-4-Turbo-1106 at 8k: 90.0% (front) vs. 38.0% (middle) vs. 40.5% (rear). Claude-2 uniquely performs best when the ground truth is at the rear (59.0% vs. 34.0% front at 1k). Position bias intensifies as input length increases.

**Scalable position embeddings.** NTK-aware Scaled RoPE, ReRoPE, and Leaky ReRoPE are evaluated on Vicuna-v1.5 (4k base context). All methods improve accuracy beyond the original 4k window (e.g., at 8k, NTK achieves 3.9% vs. 0.0% for Original-4k on Vicuna-7b). Performance is comparable to models trained on 16k contexts with Flash Attention, suggesting scalable position embeddings are a viable alternative to expensive long-context training.

**Comparison with other benchmarks.** GPT-4-Turbo-1106 evaluated on BestAnswer (16k), NarrativeQA (LongBench subset), and GovReport (LongBench subset) with progressive text truncation. BestAnswer shows the steepest performance drop when truncated: from 44.0% (full) to 11.0% (2k), a 33-point drop. NarrativeQA drops only 8.4 points (33.1 to 24.7), and GovReport actually improves slightly when truncated. This confirms that Ada-LEval requires more comprehensive text understanding than traditional QA and summarization tasks.

### Error Analysis

Most errors fall into two categories: (1) failure to follow instructions (not outputting a valid answer format) and (2) copying the example answer provided in the prompt. GPT-4-Turbo maintains near-perfect instruction following and low copy rates. Claude-2, LongChat, and Vicuna models suffer primarily from elevated copy instruction rates (Claude-2: 95--99% on TSort). ChatGLM models suffer from low instruction following rates. All models except GPT-4-Turbo find it harder to follow instructions as text length increases.

### Limitations

1. **Cannot distinguish open-source models.** Due to poor instruction following and high copy instruction rates, Ada-LEval accuracy scores for open-source models cluster near random guess, limiting discriminative power among them.
2. **Difficulty ceiling at ultra-long settings.** Even state-of-the-art proprietary models achieve 0% on BestAnswer at 64k+, constraining the benchmark's applicability to current models.

---

## Conclusions

1. **First length-adaptable long-context benchmark.** Ada-LEval introduces two tasks (TSort and BestAnswer) that can generate test cases at any target length from 1k to 128k tokens, addressing the inflexibility of fixed-length benchmarks like LongBench and L-Eval.

2. **Full-text comprehension is required.** Truncation experiments demonstrate that BestAnswer performance degrades far more sharply than NarrativeQA or GovReport when input is truncated, confirming that Ada-LEval tasks require reading and understanding the entire input.

3. **All models fail at ultra-long contexts.** No model achieves meaningful accuracy on BestAnswer at 64k+ tokens. On TSort, even GPT-4-Turbo produces only random-level accuracy at 32k--128k. This directly contradicts the claimed context windows of 100k--200k tokens.

4. **Generative performance lags far behind perceptual understanding.** PPL-based evaluation on TSort shows open-source models can distinguish correct orderings (up to 89.2%) but fail to produce them generatively (maximum 5.4%), revealing a fundamental gap between comprehension and instruction-following capabilities.

5. **Strong position bias in answer selection.** All models exhibit significant position bias on BestAnswer, with most preferring answers near the beginning of the input. This bias intensifies as context length grows, suggesting that models increasingly rely on position rather than content at longer lengths.

6. **Scalable position embeddings improve long-context capability.** NTK-aware Scaled RoPE, ReRoPE, and Leaky ReRoPE extend effective context beyond the training window and achieve performance comparable to models explicitly trained on longer contexts.

---

## Core References and Why They Are Referenced

### Prior Long-Context Benchmarks

- **Shaham et al. (2022)** -- *SCROLLS.* Referenced as an earlier multi-task long-context benchmark. Ada-LEval addresses SCROLLS's limitations of fixed-length evaluation and lack of ultra-long settings.
- **An et al. (2023)** -- *L-Eval.* A long-context evaluation benchmark with close-ended and open-ended tasks. Ada-LEval critiques L-Eval for inflexible text lengths (up to ~32k) and reliance on traditional QA/summarization.
- **Bai et al. (2023)** -- *LongBench.* A bilingual long-context benchmark covering six task categories. Ada-LEval critiques LongBench for fixed-length test cases, open-ended metrics, and lack of ultra-long settings.

### Task Source Data

- **Kryściński et al. (2021)** -- *BookSum.* Provides the Project Gutenberg book data used to construct TSort. Text segments are extracted from contiguous chapters with identifiers removed.
- **Kočiskỳ et al. (2018)** -- *NarrativeQA.* Used as a comparison benchmark (LongBench subset) in the truncation experiment to demonstrate that Ada-LEval requires more comprehensive text understanding.
- **Huang et al. (2021)** -- *GovReport.* Used as a comparison benchmark (LongBench subset) in the truncation experiment; performance on GovReport actually improves with truncation, unlike Ada-LEval.

### Long-Context Techniques

- **Su et al. (2021)** -- *RoPE (RoFormer).* The base positional encoding used by most evaluated models. Scalable RoPE variants (NTK-aware, ReRoPE) are evaluated in the ablation study.
- **Chen et al. (2023b)** -- *Position Interpolation.* Linearly scales down position indices to extend context windows. Referenced as a key scalable position embedding technique that ChatGLM2-32k employs.
- **Su (2023)** -- *ReRoPE / Leaky ReRoPE.* Rectified Rotary Position Embeddings that control scaling via a window size parameter. Evaluated on Vicuna-v1.5, achieving performance comparable to models trained on 16k contexts.
- **Press et al. (2021)** -- *ALiBi.* An alternative position encoding applying linearly decreasing attention penalties. Referenced as a contrasting approach to RoPE-based methods.

### Models and Evaluation Infrastructure

- **OpenAI (2023)** -- *GPT-4.* GPT-4-Turbo is the top-performing model across both tasks, but still collapses at ultra-long settings (0% on BestAnswer at 64k+).
- **Zheng et al. (2023)** -- *Vicuna / MT-Bench.* Vicuna models are used both as open-source baselines and as the testbed for scalable position embedding ablations.
- **Contributors (2023)** -- *OpenCompass.* The open-source evaluation platform used to conduct all experiments.

### Long-Context Modeling Approaches

- **Dao et al. (2022a)** -- *FlashAttention.* An efficient attention implementation referenced as enabling longer context windows without changing the model architecture.
- **Ding et al. (2023)** -- *LongNet / Dilated Attention.* Reduces attention complexity to near-linear and scales to 1 billion tokens, but Liu et al. (2023a) showed such mechanisms struggle with middle portions of long texts.
- **Liu et al. (2023a)** -- *Lost in the Middle.* Identified that LLMs struggle to use information in the middle of long contexts. Ada-LEval's position bias results (Section 4.5.2) are consistent with this finding.

#### Cross-References in Available Papers

- **SCROLLS (2022-12-scrolls-long-language-sequences):** Ada-LEval references SCROLLS as a prior multi-task long-context benchmark with fixed evaluation lengths. Both benchmarks use BookSum-derived data, though for different tasks (summarization in SCROLLS vs. segment ordering in Ada-LEval).
- **LongBench (2024-07-longbench-bilingual-multitask):** Ada-LEval directly compares against LongBench subsets (NarrativeQA, GovReport) in its truncation experiment (Table 10), showing that Ada-LEval requires more full-text comprehension.
