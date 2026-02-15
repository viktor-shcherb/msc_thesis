# Our Benchmark: HELMET [p. 3-6]

In this work, the authors seek to overcome the shortcomings of existing benchmarks by meeting the following desiderata: (1) diverse coverage across different tasks and capabilities of LCLMs, (2) controllable context lengths that support more than 128K input tokens, and (3) reliable evaluation for both base and instruction-tuned models [p. 3]. In this section, they describe the datasets used in HELMET and how they improve upon existing benchmarks in terms of settings and metrics [p. 3]. An overview of HELMET is shown in Table 3 [p. 3].

**Table 3** (p. 4): Overview of evaluation datasets. They select datasets that cover various important long-context capabilities. SubEM: substring exact match.

| Category | Dataset | Metrics | Description |
|----------|---------|---------|-------------|
| **Retrieval-augmented generation** | Natural Questions | SubEM | Factoid question answering |
| | TriviaQA | SubEM | Trivia question answering |
| | PopQA | SubEM | Long-tail entity question answering |
| | HotpotQA | SubEM | Multi-hop question answering |
| **Generation with citations** | ALCE ASQA | Recall, Cite | Answer ambiguous questions with citations |
| | ALCE Qampari | Recall, Cite | Answer factoid questions with citations |
| **Passage re-ranking** | MS MARCO | NDCG@10 | Rerank passage for a query |
| **Many-shot in-context learning** | TREC Coarse | Accuracy | Question type classification, 6 labels |
| | TREC Fine | Accuracy | Question type classification, 50 labels |
| | NLU | Accuracy | Task intent classification, 68 labels |
| | BANKING77 | Accuracy | Banking intent classification, 77 labels |
| | CLINC150 | Accuracy | Intent classification, 151 labels |
| **Long-document QA** | NarrativeQA | Model-based | Book and movie script QA |
| | x-BENCH QA | ROUGE F1 | Novel QA with entity replacement |
| | x-BENCH MC | Accuracy | Novel multiple-choice QA with entity replacement |
| **Summarization** | x-BENCH Sum | Model-based | Novel summarization with entity replacement |
| | Multi-LexSum | Model-based | Summarizing multiple legal documents |
| **Synthetic recall** | JSON KV | SubEM | Retrieve a key in JSON dictionary |
| | RULER MK Needle | SubEM | Retrieve the needle (a number) within noisy needles |
| | RULER MK UUID | SubEM | Retrieve the needle (a UUID) within noisy needles |
| | RULER MV | SubEM | Retrieve multiple values for one needle (key) |

**Table 2** (p. 3): Comparison of long-context benchmarks: ZeroSCROLLS (Shaham et al., 2023), Long-Bench (Bai et al., 2024), L-Eval (An et al., 2024), RULER (Hsieh et al., 2024), x-BENCH (Zhang et al., 2024b), and HELMET. L: input tokens. †: All datasets have L < 128K except one dataset. ‡: L-Eval uses LLMs to compute reference-free, pairwise win-rates; authors design reference-based model evaluation for specific tasks.

| Benchmark | Type of tasks | | | | | | Benchmark features | |
|-----------|---------------|---|---|---|---|---|-------------------|---|
| | Cite RAG | Re-rank | Long-QA | Summ ICL | Synthetic Recall | Robust Eval. | L ≥ 128k | Controllable L |
| ZeroSCROLLS | x | x | x | checkmark | checkmark | x | x | x | x† | x |
| LongBench | x | checkmark | x | checkmark | checkmark | checkmark | checkmark | x | x† | x |
| L-Eval | x | x | x | checkmark | x | x | x | x‡ | x† | x |
| RULER | x | x | x | x | x | x | checkmark | checkmark | checkmark | checkmark |
| x-BENCH | x | x | x | checkmark | x | x | checkmark | x | checkmark | checkmark |
| HELMET (Ours) | checkmark | checkmark | checkmark | checkmark | checkmark | checkmark | checkmark | checkmark | checkmark | checkmark |

## 2.1 Realistic and Diverse Long-Context Applications [p. 3-5]

### Retrieval-augmented generation (RAG)

The authors use open-domain question answering (ODQA)—which requires retrieving from a knowledge corpus and then generating correct answers (Chen et al., 2017)—as a representation of retrieval-augmented generation (RAG) applications [p. 3]. They utilize Natural Questions (NQ; Kwiatkowski et al., 2019), TriviaQA (Joshi et al., 2017), HotpotQA (Yang et al., 2018), and PopQA (Mallen et al., 2023) [p. 3]. They use the gold passage (the passage with the answer) from Petroni et al. (2021), or otherwise use Wikipedia passages [p. 3].

Given an input length L, they first determine the number of passages k that can fit within L tokens, then retrieve k passages³ from the corpus⁴ that do not contain the answer as distractors [p. 3]. This differs from previous works that randomly sample passages from the corpus (Lee et al., 2024) and is more realistic and challenging [p. 3-4].

For NQ, TQA, and PopQA, they take the top k − 1 distractors and insert the gold passage at six evenly distributed positions following Liu et al. (2023) [p. 4]. For HotpotQA, which requires two gold passages, they combine them and the top k − 2 distractors and randomly shuffle them into three permutations [p. 4]. They use SubEM (whether the answer is included in the output), following previous work (Asai et al., 2024a) [p. 4]. See §B.1 for more details [p. 4].

### Generation with citations (Cite)

The authors leverage ALCE (Gao et al., 2023) to evaluate LCLMs on a realistic application of answering questions while providing correct attributions (Bohnet et al., 2022) [p. 4]. Given multi-faceted questions and relevant passages, models are required to generate a long-text answer and cite supporting passage IDs at the end of each sentence [p. 4]. This tests models' ability to utilize the passages in the context and generates answers with correct instructions about citation formats [p. 4].

They use the ASQA (Stelmakh et al., 2022) and QAMPARI (Rubin et al., 2022) subsets from ALCE [p. 4]. For an input length L, they first determine the number of passages k, and use the top k retrieved passages from Wikipedia as contexts [p. 4]. The model's outputs are evaluated on correctness and citation quality, and they report the average across all metrics, see §B.2 for more details [p. 4].

### Passage re-ranking (Re-rank)

Re-ranking retrieved passages based on their relevance to the query is an important application of LCLMs (Sun et al., 2023) [p. 4]. The task requires the model to retrieve relevant information, compare, and reason over different parts of the contexts [p. 4]. They use the MS MARCO dataset (Bajaj et al., 2018), where each instance contains a query and passages retrieved by BM25 (Robertson & Zaragoza, 2009) from the Internet [p. 4]. Each passage has annotations of a relevance label—perfect, highly relevant, relevant, or not relevant [p. 4].

They determine the number of passages k from the input length L, and randomly sample k passages with balanced labels for each test query [p. 4]. The model is prompted with the query and passages, and is instructed to output the top-10 document IDs ranked by relevance [p. 4]. They report NDCG@10 [p. 4]. Details are in §B.3 [p. 4].

### Many-shot in-context learning (ICL)

In-context learning (ICL) is a key ability that enables LLMs to adapt to new tasks on the fly (Brown et al., 2020) [p. 4]. Recent studies (Ratner et al., 2023; Xu et al., 2024; Li et al., 2024c; Bertsch et al., 2024) explore performing many-shot ICL (with thousands of examples) with LCLMs [p. 4]. Following Bertsch et al. (2024), the authors focus on datasets with large label spaces: TREC-coarse, TREC-fine (Li & Roth, 2002), BANKING77 (Casanueva et al., 2020), CLINC150 (Larson et al., 2019), and NLU (Liu et al., 2019) [p. 4].

They adjust the number of shots to control the input length L, and the number of examples in each class is balanced [p. 4]. They report accuracy on the test set [p. 4].

One difference from previous works is that they map original natural language labels (e.g., location) into numbered labels (i.e., 0, 1) to test how well a model can learn new tasks instead of relying on its pre-trained priors (Wei et al., 2023; Pan et al., 2024; Min et al., 2022) [p. 5]. More details are in §B.4 [p. 5].

### Long-document question answering (LongQA)

The authors use NarrativeQA (Kočiský et al., 2018) and the English book QA and multiple choice (MC) subsets from x-BENCH (Zhang et al., 2024b) for evaluating long-document QA [p. 5]. They select those tasks for their abundant context lengths (Table 4) [p. 5]. They truncate the document from the end based on the evaluation length L [p. 5]. They use ROUGE F1 for x-BENCH QA (answers are mostly entity names) and accuracy for x-BENCH MC and NarrativeQA [p. 5]. For NarrativeQA, because the answers can be long text and open-ended, they design and use a model-based evaluation (§2.2) [p. 5].

**Table 4** (p. 5): Dataset lengths.

| Datasets | Medium | Max |
|----------|---------|-----|
| ZeroSCROLLS | | |
| QASPER | 6K | 12K |
| GovReport | 12K | 33K |
| QuALITY | 9K | 11K |
| SQuALITY | 8K | 10K |
| HELMET | | |
| NarrativeQA | 73K | 518K |
| x-BENCH QA | 191K | 835K |
| x-BENCH MC | 167K | 835K |
| x-BENCH Sum | 154K | 835K |
| Multi-LexSum | 90K | 5M |

### Summarization (Summ)

Summarization tests LCLMs' ability to synthesize information across long contexts [p. 5]. The authors select the legal document summarization (legal document summarization) and the English summarization task from x-BENCH (novel summarization) (Zhang et al., 2024b) as representative for this category (see Table 4) [p. 5]. They truncate the document from the end based on the evaluation length L [p. 5]. They use their model-based evaluation (§2.2) for both datasets instead of the commonly used ROUGE, as it better reflects human judgment [p. 5].

### Synthetic recall

Synthetic recall tasks, such as needle-in-a-haystack (NIAH), stress test models' ability to recall relevant information (the "needle") from long contexts [p. 5]. They have gained popularity for being easy to use (as they can test any arbitrary length) and easy to control (can placing the "needle" at any position) [p. 5]. For this category, the authors select four synthetic tasks from RULER (an extended version of NIAH; Hsieh et al., 2024) and also add a JSON KV retrieval task (Liu et al., 2023), which they find more challenging [p. 5]. They select those tasks that correlate well with application-driven tasks; in-depth discussions are in §3.1 [p. 5]. Following previous works, they report the percentage of the ground truth answers that are substrings in the generation (SubEM) [p. 5]. Refer to §B.5 for more details [p. 5].

## 2.2 Reliable Evaluation Metrics [p. 5-6]

Existing long-context benchmarks (Zhang et al., 2024b; Shaham et al., 2023) largely rely on n-gram overlap metrics like ROUGE (Lin, 2004), which has been shown to correlate poorly with human judgment for tasks with long outputs, such as summarization (Goyal et al., 2023; Deutsch et al., 2022; Krishna et al., 2023) [p. 5]. L-Eval (An et al., 2024) employs LLMs to compute reference-free "win rates," which neglect the available answer annotations and always require evaluating model pairs [p. 5]. Instead, the authors design a reference-based model evaluation method for long-document QA and summarization that is more reliable and easy to use [p. 5].

### Question answering

In NarrativeQA, they prompt GPT-4o⁵ with the question, the ground truth, and the model output to check for fluency and correctness [p. 5]. The fluency score is either 0 (incoherent or repetitive) or 1 (fluent), and the correctness score takes on the value of 0 (incorrect), 1 (partly correct), 2 (correct but not fully relevant), and 3 (correct and relevant) [p. 5]. They take the product of the two as the final score, normalizing it to a range of [0, 100] [p. 5].

### Summarization

Following previous works (Kamoi et al., 2023; Zhang & Bansal, 2021), they first decompose the gold summary into atomic claims and use GPT-4o to check if each claim is supported by the generation (recall) and if each sentence in the generation is supported by the reference summary (precision) [p. 5]. They then compute the F1 score from the recall and precision scores [p. 5-6]. Additionally, they ask GPT-4o to evaluate fluency (0 or 1) and take its product with the F1 score as the final score [p. 6]. In each step, they prompt GPT-4o with handwritten examples [p. 6].

**Figure 2** (p. 6): Comparison between ROUGE-L F1 and model-based evaluation metric on summarization tasks.

Description: Heatmap table comparing ROUGE-L F1 scores (left columns) and InfBench-Sum scores (right columns) for Multi-LexSum and InfBench-Sum tasks across different models and context lengths.

Key details shown:
- Models: GPT-4o-08, Gemini-1.5-Pro, Claude-3.5-Sonnet, Llama-3.2-3B-Inst, Llama-3.1-8B-Inst, Llama-3.1-70B-Inst, Mistral-7B-Inst-v0.1, Mistral-7B-Inst-v0.3
- Context lengths: 8K, 16K, 32K, 64K, 128K for both tasks
- ROUGE-L scores shown in left columns with color gradient
- "Ours" (model-based) scores shown in right columns with color gradient
- Notable pattern: Model-based evaluation shows more consistent trends with increased input length, while ROUGE remains almost the same
- Metric clearly differentiates models while ROUGE shows little distinction
- Supports claim: Their metric shows more consistent trends; reflects the performance gain on GPT-4o with increased input length, while ROUGE remains almost the same; their metric also clearly differentiates models while ROUGE shows little distinction.

Empirically, their reference-based model evaluation reflects more consistent trends, as shown in Figure 2 [p. 6]:

1. Llama-3.1-8B-Inst achieves similar ROUGE scores to GPT-4o, while their evaluation reveals a significant gap [p. 6]
2. Their metric accurately identifies incoherent generations and shows lower performance for models with smaller context windows, such as the Mistral models [p. 6]
3. Their metric exhibits a substantially more positive trend for GPT-4o as input length increases, whereas ROUGE-L remains within a 2-point absolute difference [p. 6]

They further validate the model-based evaluation through human studies, which suggest their new metrics highly correlate with human judgments [p. 6]: for example, on x-BENCH Sum, their metric reaches a human-model agreement of Cohen's κ = 0.91 for summary precision and κ = 0.76 for recall [p. 6]. More details on the human studies are in §B [p. 6].

## 2.3 Robust Prompting and Controlled Evaluation Settings [p. 6]

### Robust prompting reduces noise and enables evaluation on base models

Many long-context benchmarks require models to follow instructions and only support evaluating instruction-tuned models (Zhang et al., 2024b; Shaham et al., 2023) [p. 6]. However, many model developments do not incorporate instruction tuning (Chen et al., 2023; Fu et al., 2024), leaving these models reliant on perplexity-based evaluation or synthetic tasks [p. 6]. To support long-context research efforts, the authors design their benchmark so that at least a subset of the datasets accommodates evaluating base models [p. 6].

Existing benchmarks mostly use zero-shot prompting (Shaham et al., 2023; Zhang et al., 2024b), which leads to inconsistent output formats, especially for base models [p. 6]. For example, the model may output a long answer in RAG when a short answer is required [p. 6]. They add two-shot demonstrations in the prompt for all tasks to address this issue [p. 6]. As shown in Table 8⁶, both base and instruction-tuned models significantly benefit from the demonstrations [p. 6].

Furthermore, they employ the length-instruction-enhanced evaluation from L-Eval for long-generation tasks (i.e., summarization), which has been shown to have substantially more consistent and reliable evaluations (An et al., 2024) [p. 6]. As a result, they find that their reproduction of previous datasets, such as x-BENCH QA tasks, better reflects the capabilities of LCLMs, as shown in Table 7 [p. 6]. The use of demonstrations and improved instructions more accurately depicts how models perform in real applications [p. 6].

### Controlled input length and difficulty

An important dimension to consider when evaluating LCLMs is the input length L, as longer input can provide more information while challenging the model's ability to process distracting contexts [p. 6]. As discussed in §2.1, they can control the input length L for each task by either adjusting the number of retrieved passages, the number of demonstrations, or truncating the document text to fit within the specified lengths [p. 6]. This allows them to study model performance at or beyond the length of current frontier LCLMs (≥ 128K) [p. 6].

---

Footnotes from this section:
³They use Alibaba-NLP/gte-large-en-v1.5 for retrieval (Zhang et al., 2024a).
⁴They use Wikipedia 2019-8-01 dump, split into 100-word passages (Petroni et al., 2021).
⁵GPT-4o-2024-05-13
⁶Except for ICL (the number of shots varies) and RULER (they follow the original formatting).
