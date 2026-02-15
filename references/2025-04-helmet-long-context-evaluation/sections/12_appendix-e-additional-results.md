# Appendix E: Additional Results [p. 35]

## E.1 Correlation between Synthetic and Downstream Tasks [p. 35]

The authors show the correlation between all synthetic and RAG datasets with other downstream tasks in Figure 8 [p. 35]. They see that the synthetic tasks are generally less correlated with the downstream tasks, whereas the RAG datasets are more correlated with other downstream tasks [p. 35]. Furthermore, there appears to be a pattern between the complexity of the synthetic task and its correlation with other tasks—the more complex the task, the higher its correlation with other downstream tasks [p. 35]. Furthermore, noisier variants tend to be more reflective of real-world applications, as seen in the difference between RULER MK Essay and RULER MK Needle, where the context is other distracting needles [p. 35]. Upon closer inspection, they note that Needle MK Needle/UUID, JSON KV, and NIAH MV generally have relatively high correlation with other realistic datasets, and are able to test the recall abilities of the model [p. 35]. Thus, they select these four datasets as part of the HELMET synthetic recall subset [p. 35]. They validate this selection by checking the correlation between this set and other downstream tasks, and found that it generally has higher correlation than using synthetic datasets individually [p. 35]. There may be more optimal methods for selecting synthetic datasets, and they leave this as future work [p. 35].

## E.2 Correlation between Datasets [p. 36]

The authors plot the correlation between all HELMET datasets in Figure 9 [p. 36]. In general, the datasets in each category are strongly correlated with each other [p. 36]. One exception to this observation is the lack of correlation between the ALCE datasets [p. 36]. This suggests that writing the correct citations is a different skill from answering questions with facts [p. 36]. They also observe some low correlation between datasets for long-document QA and ICL, but this is likely due to the diversity within each categories [p. 36].

---
[p. 36-41 continued]

**Table 11** (p. 36): Model-based evaluation prompt for summarization fluency score.

The table presents the full prompt template used for model-based evaluation of summarization fluency. The prompt instructs a judge model to evaluate text coherence, fluency, and grammatical correctness using a scoring rubric:
- Score 0 (incoherent, repetitive, or incomplete): Incoherent sentences, repetitive sentences (even if not by exact words), incomplete answers, or gibberish. Note that even if the answer is coherent, if it is repetitive in form, it should be given a score of 0
- Score 1 (coherent, non-repetitive answer): Coherent, non-repetitive, fluent, grammatically correct answers. If the text is coherent, non-repetitive, and fluent, but the sentence is truncated, it should still be given a score of 1

The prompt includes two demonstration examples:
- Example 1: "Summary: The U.S. government brought a criminal case against four defendants." (repetitive but coherent) → Score 0
- Example 2: Full summary about a case challenging curfews in Los Angeles and San Bernardino → Score 1

The output format is JSON: `{{"fluency": 1}}` with the text to evaluate provided as `Text: ''{text}''`

**Figure 8** (p. 37): Spearman's correlation at 128K input length, calculated across 30 instruction-tuned models, between all synthetic and RAG tasks and other downstream tasks.

Description: Heatmap showing correlation coefficients between different tasks.
- Rows: Various task types including NIAH, RULER variants (S Repeat, S UUID, MK Essay, MK Needle, MK UUID, MQ, MV), CWE, FWE, VT, RULER SQUAD, RULER HotpotQA, RULER, JSON KV, Recall, NQ, HotpotQA, PopQA, TriviaQA, RAG
- Columns: ICL, Cite, Rerank, LongQA, Sum, Avg
- Notable patterns: Color-coded cells show correlation values ranging from approximately -0.61 (red/negative) to 0.93 (green/positive)
- Supports claim: Synthetic tasks like RULER MK Needle/UUID, JSON KV, and NIAH MV have relatively high correlation with realistic datasets; RAG tasks generally show higher correlation with downstream tasks than simple synthetic tasks

## E.3 Positional Embedding Extrapolation Remains a Challenge [p. 37]

A key component of LCLMs is its positional embeddings, as it's essential to how the model processes positional information and extrapolate to long sequences [p. 37]. Thus, they also consider models that leverage positional extrapolation during inference [p. 37]. Specifically, they show Llama-3-Inst with the original RoPE embedding and changing the Theta base to 16M during inference, and Qwen2-Inst with YaRN scaling [p. 37]. Formally, RoPE defines $θ_d = b^{-2d/|D|}$, where $θ_d$ is the angle at the d-th hidden state, b is a constant called the base, and |D| is the size of the hidden state (Su et al., 2021) [p. 37].

Llama-3 sets b = 500,000 during training, and they evaluate with both the original base and setting b = 16,000,000 [p. 37-38].

For the Qwen2 models, they use RoPE scaling during inference, since the original model was trained on sequence lengths up to 32K tokens [p. 38]. Specifically, they follow the recommended scaling factor specified in their HuggingFace model card⁸ [p. 38].

They find that existing positional embeddings still struggle at out-of-distribution length, with both families of models dropping sharply in performance past L = 32768, shown in Figure 7 [p. 38]. The same trend also applies to models across different model sizes from 8B to 70B [p. 38]. Finally, altering the positional embedding may lead to degradation at shorter lengths, which is evident for Llama-3-8B-Inst on ODQA and ICL [p. 38]. The problem of effectively extrapolating positional embeddings persists as an open challenge [p. 38].

⁸https://huggingface.co/Qwen/Qwen2-7B-Instruct#processing-long-texts

**Figure 9** (p. 38): Spearman's correlation at 128K input length, calculated across 35 instruction-tuned models, between all HELMET datasets and category averages.

Description: Large heatmap showing pairwise correlations between all HELMET datasets.
- Rows and columns: Comprehensive list of all datasets including JSON KV, ZAIV MK Needle, NIAH MK UUID, RULER MK Essay, NIAH, MQ, HotpotQA, PopQA, TriviaQA, RAG, ALCE ColIns, ALCE Cite Recall, ALCE Cite Precision, ALCE QA, QAMPARI CoIns, QAMPARI Cite Recall, QAMPARI Cite Precision, QAMPARI QA, QAMPARI Cora Recall, Cite, NarrativeQA, InfBench QA, InfBench MC, LSQT QA, LongQA, Multi-LexSum Fluency, Multi-LexSum Recall, Multi-LexSum Precision, Sum, TREC-Covid, TREC-Cohere, MIRACL, CQADupStack, NLU, ICL, Cite, Rerank, LongQA, Sum, Avg
- Notable patterns: Cells show correlation values with color coding (green for positive, red for negative correlations). Most categories show strong internal correlation, but ALCE datasets show low correlation with each other
- Supports claim: Datasets within each category are strongly correlated, except ALCE datasets which show low internal correlation, suggesting citation accuracy is a different skill from question answering

## E.4 Presence of Lost in the Middle [p. 38]

Previous works found that models often struggle with recalling facts in the middle of the input, a phenomenon named lost in the middle (Liu et al., 2023) [p. 38]. In this work, they extend the previous analysis to input length up to 128K tokens [p. 38-39]. They place the needle at six different evenly spaced depths in the context, and evaluate the models' ability to retrieve the needle [p. 39]. In our study, the needle may be either a key in the JSON dictionary or an answer to a question [p. 39]. They show the results in Figure 11 for JSON KV, Figure 12 for Natural Questions, Figure 13 for PopQA, and Figure 14 for TriviaQA [p. 39]. They find that the model in general prefers to retrieve the needle from contexts at the beginning of the input (e.g., Llama-3 and Llama-3.1, Llama-3.2), the model's performance when the needle is in the middle of the context is often better than when it is at the start of the context for long inputs [p. 39].

## E.5 Comparison between Base and Instruction-tuned Models [p. 39]

Previous benchmarks largely focus on evaluating instruction-tuned models (Shaham et al., 2023; Zhang et al., 2024b) [p. 39]. As a result, most existing benchmarks often turn to perplexity and synthetic tasks to evaluate their models (Fu et al., 2024; Yen et al., 2024; AI et al., 2024) [p. 39]. However, as they have seen in this work, it is important to evaluate LCLMs on diverse downstream tasks to get a full picture of the model's capabilities [p. 39]. Furthermore, comparing base and instruction-tuned models is essential in understanding the impact of instruction tuning and extrapolated performance at long contexts [p. 39]. Thus, they built HELMET to be compatible with both base and instruction-tuned models through in-context learning examples [p. 39]. Taking a closer look at the examples in Figure 10, they find that instruction-tuning generally improves the performance of the model across all tasks [p. 39]. Instruction-tuning at long contexts may yield more benefits than simply scaling up the model sizes; for example, Llama-3.1-8B-Inst outperforms Llama-3.1-70B on most tasks [p. 39].

## E.6 Performance of Claude [p. 39]

In this subsection, they investigate the relatively low performance of the Claude-3.5-Sonnet model in comparison to other proprietary models, such as GPT-4o and Gemini [p. 39]. They qualitatively analyze the model outputs and find that the main reason for Claude's low performance is its tendency to not follow instructions and just answer the questions directly [p. 39]. For example, it often does not output the citation markers for Cite (Table 17), does not follow the exact formatting rules for the passage rankings task (Table 18), and does not output the classification label for ICL (Table 18) [p. 39]. Sometimes it even refuses to answer the question due to copyright concerns (Table 17) [p. 39]. Thus, it has a lower score on these tasks [p. 39]. They argue that it is important for LCLMs to closely follow user instructions in real applications so they should penalize models that do not [p. 39]. Sometimes, the output may be truncated due to the restriction on the maximum number of generated tokens (Table 16), in contrast to other closed-source models do generate more concise outputs as specified in the instruction and demonstrated by the ICL examples [p. 39].

## E.7 Full Results [p. 39]

They provide all the detailed evaluation numbers on each dataset at each length here: https://shorturl.at/5wjVl [p. 39].

**Table 12** (p. 40): Model-based evaluation prompt for summarization recall score. Here they show the demonstrations for Multi-LexSum.

The table presents the full prompt template for evaluating summarization recall. The prompt instructs a judge model to evaluate whether key points from an expert-written summary are present in a provided summary. The summary is based on a set of legal documents about civil lawsuit cases.

The grading rubric evaluates each key point by deciding if it is present in the provided summary:
- A key point is considered present if its factual information is well-supported by the provided summary
- Score equals the number of key points present in the provided summary

The prompt includes two demonstration examples:
- Example 1: Case about curfew orders challenged in Los Angeles and San Bernardino. Shows 7 key points with reasoning for each. Final recall score is 4 (out of 7 key points present)
- Example 2: (omitted for brevity notation)

The output format is JSON: `{{"recall": 2}}` with key points as `{keypoints}` and summary as `''{summary}''`

**Table 13** (p. 41): Model-based evaluation prompt for summarization precision score. Here they show the demonstrations for Multi-LexSum.

The table presents the full prompt template for evaluating summarization precision. The prompt instructs a judge model to decide if each sentence in the provided summary is supported by the information provided in the expert summary.

The grading rubric evaluates precision:
- A sentence is considered supported if its main/major facts align with information in the expert summary
- A sentence is still considered supported even if some of its minor details, such as entity names, names of laws and previous court cases, are not explicitly mentioned in the expert summary
- A sentence is not supported if its major facts are not mentioned or contradicted in the expert summary
- Score equals the number of sentences in the provided summary that are supported by the expert summary

The prompt includes two demonstration examples:
- Example 1: Case about lawsuit in U.S. District Court for Central District of California regarding curfew orders. Shows sentence-by-sentence reasoning. Final precision score is 3 (out of 4 sentences supported), with sentence count of 4
- Example 2: (omitted for brevity notation)

The output format is JSON: `{{"precision": 2, "sentence_count": 6}}` with expert summary as `''{expert_summary}''` and provided summary as `''{summary}''`

---
[p. 42-46 continued]

**Table 14** (p. 42): Comparison between ROUGE-L F1 scores, which is commonly used in previous works but cannot identify errors in generations, and our GPT-4o-based evaluation metric, which better reflects user experience and achieves better separability. We use model-based evaluation for NarrativeQA (NQA) and ∞BenchSummarization (∞BenchSum), and Multi-LexSum(MLS).

| Model | NarrativeQA | | ∞Bench Sum | | Multi-LexSum | |
|-------|------------|-----|------------|-----|--------------|-----|
| | F1 | GPT | R-L | GPT | R-L | GPT |
| GPT-4o-05 | 46.5 | 55.4 | 17.3 | 44.8 | 25.8 | 55.4 |
| GPT-4o-08 | 43.1 | 51.3 | 16.8 | 31.1 | 24.9 | 56.1 |
| Claude-3.5-Sonnet | 16.2 | 43.5 | 14.2 | 30.5 | 22.0 | 50.9 |
| Gemini-1.5-Flash | 39.0 | 42.9 | 17.0 | 28.7 | 24.5 | 51.1 |
| Gemini-1.5-Pro | 42.8 | 50.9 | 16.1 | 32.0 | 25.8 | 58.1 |
| Llama-3-8B-Inst | 1.0 | 6.7 | 6.8 | 0.0 | 8.0 | 3.3 |
| Llama-3-8B-Inst-Theta | 3.3 | 4.1 | 7.6 | 0.0 | 12.4 | 22.3 |
| Llama-3-70B-Inst-Theta | 4.9 | 10.9 | 5.9 | 0.0 | 14.4 | 24.0 |
| Llama-3.1-8B-Inst | 45.1 | 47.7 | 17.4 | 16.2 | 25.2 | 46.9 |
| Llama-3.1-70B-Inst | 38.3 | 54.0 | 17.5 | 19.8 | 25.2 | 51.6 |
| Llama-3.2-1B-Inst | 14.5 | 18.2 | 16.6 | 2.9 | 23.1 | 20.3 |
| Llama-3.2-3B-Inst | 23.8 | 36.7 | 16.5 | 12.4 | 23.7 | 43.6 |
| Mistral-7B-Inst-v0.1 | 12.3 | 16.0 | 12.6 | 4.2 | 22.1 | 16.1 |
| Mistral-7B-Inst-v0.2 | 14.9 | 21.0 | 15.4 | 1.0 | 20.0 | 23.4 |
| Mistral-7B-Inst-v0.3 | 21.0 | 22.0 | 12.3 | 0.1 | 19.0 | 24.4 |

**Table 15** (p. 43): Length denotes the training length of the model or, if not known, the claimed context window. For MoE models, we denote the number of activated/total parameters. We change the RoPE (Su et al., 2021) θ during inference for some models and is denoted with -θ. Most models use RoPE (Su et al., 2021), PI (Chen et al., 2023), LongRoPE (Ding et al., 2024), or YaRN (Peng et al., 2024).

[THIS IS TABLE: A comprehensive table listing model details including Name, Length, Architecture, Positional Emb., # Params, and Inst.? columns. The table is divided into sections for Proprietary models, Llama-2-based models, Llama-3-based models, ProLong, Mistral-based models, Yi models, Phi-3 models, Qwen-2 models, Qwen2.5 models, Jamba models, and others. Each row contains specific technical details about different language models.]

Key entries include:
- Proprietary models: GPT-4 series (128000-1000000 length), Claude-3.5-Sonnet (200000), Gemini models (1048576-2097152)
- Llama-2-based: Various configurations from 8192-80000 length with Full-attention architecture
- Llama-3-based: Models with 8192 length, Full-attention, using RoPE with various parameter counts
- Mistral-based: 8192-524288 length models with Sliding-window or Full-attention
- Yi models: 200000 length with Full-attention and RoPE
- Phi-3 models: 131072 length with various attention mechanisms (Blocksparse, Full-attention, LongRoPE)
- Qwen-2: 32768 length with Full-attention and YaRN
- Qwen2.5: 131072 length with Dual-Chunk Attention and YaRN
- Jamba: 262144 length with Hybrid (Mamba + Full-attention) MoE
- ProLong and other specialized models with various configurations

**Figure 10** (p. 44): Results of instruction-tuned and base models on HELMET categories at various lengths. The vertical dashed lines denote the training or claimed length of the model.

Description: Large comprehensive heatmap showing model performance across different categories and lengths.
- Rows: Multiple models including GPT-4, GPT-4o variants, Claude-3.5-Sonnet, Gemini variants, Llama families (2, 3, 3.1, 3.2, 3.7), Yarn-Llama, Mistral variants, MegaBeam-Mistral, Ministral-8B, Phi-3 variants, Yi variants, Qwen0.5, Qwen2, Qwen2.5, Jamba, ProLong
- Columns: Four main category groups (Recall, RAG, Cite, Re-rank) and a summary (LongQA, Avg) evaluated at different input lengths: 8K, 16K, 32K, 64K, 128K
- Color coding: Green indicates better performance, red indicates worse performance, with numerical scores in each cell
- Notable patterns: Performance generally degrades at longer context lengths for many models; proprietary models (GPT-4o, Gemini) maintain better performance across lengths; vertical dashed lines mark each model's training/claimed length
- Supports claim: Shows comprehensive comparison across all HELMET categories, demonstrating that instruction-tuning and model architecture significantly impact long-context capabilities

**Figure 11** (p. 45): Performance of models on JSON KV (Liu et al., 2023) at different depths. Depth is the position of the gold KV pair, and its values are [0.0, 0.2, 0.4, 0.6, 0.8, 1.0], where 0.0 is the beginning of the context (the top of each heatmap) and 1.0 is the end (the bottom of each heatmap).

Description: Grid of heatmaps showing performance on JSON KV task at different depths and lengths.
- Layout: Multiple small heatmaps arranged in a grid, one for each model
- Models shown: GPT-4, GPT-4o-mini, GPT-4o-05, GPT-4o-08, Claude-3.5-Sonnet, Gemini-1.5-Flash, Gemini-1.5-Pro, Llama-2-7B-32K, Yarn-Llama-2-7B-64k, Yarn-Llama-2-7B-128k, Llama-3-8B, Llama-3-8B Inst, Llama-3-8B Inst-θ, Llama-3-70B Inst, Llama-3-70B Inst-θ, Llama-3.1-8B, Llama-3.1-8B Inst, Llama-3.2-1B Inst, Llama-3.2-3B Inst, Mistral-7B Inst-v0.1, Mistral-7B Inst-v0.2, Mistral-7B Inst-v0.3, Mistral-Nemo, MegaBeam-Mistral, Ministral-8B Inst, Yi-6B-200K, Yi-34B-200K, Phi-3-mini-Inst, Phi-3-mini-128k-Inst, Phi-3-med-128k-Inst, Qwen0.5-7B, Qwen2-7B Inst, Qwen2.5-7B Inst, Qwen2.5-14B Inst-1M, ProLong, Jamba-v0.1, Jamba-1.5-Mini
- X-axis: Input lengths (8K, 16K, 32K, 64K, 128K)
- Y-axis: Depth positions (0.0 to 1.0 from top to bottom)
- Color coding: Green indicates successful retrieval, red/pink indicates failure
- Notable patterns: Most models show strong performance at beginning positions (depth 0.0), variable performance in middle positions, and often degradation at longer lengths beyond training window
- Supports claim: Demonstrates "lost in the middle" phenomenon where models struggle more with information at certain depths, though patterns vary by model

**Figure 12** (p. 46): Performance of models on Natural Questions (Kwiatkowski et al., 2019) at different depths. Depth is the position of the gold passage, and its values are [0.0, 0.2, 0.4, 0.6, 0.8, 1.0], where 0.0 is the beginning of the context (the top of each heatmap) and 1.0 is the end (the bottom of each heatmap).

Description: Grid of heatmaps showing performance on Natural Questions task at different depths and lengths.
- Layout: 6×6 grid of small heatmaps, each representing a different model
- Models shown (in grid order, left to right, top to bottom): GPT-4, GPT-4o-mini, GPT-4o-05, GPT-4o-08, Claude-3.5-Sonnet, Gemini-1.5-Flash, Gemini-1.5-Pro, Llama-2-7B-32K, Llama-2-7B-32K Inst, Llama-2-7B Inst-θ, Llama-3-8B, Llama-3-8B Inst, Llama-3-8B Inst-θ, Llama-3-70B Inst, Llama-3-70B Inst-θ, Llama-3.1-8B, Llama-3.1-8B Inst, Llama-3.1-70B Inst, Llama-3.2-1B, Llama-3.2-1B Inst, Llama-3.2-3B, Llama-3.2-3B Inst, Llama-3-70B, Llama-3-70B Inst, Mistral-7B Inst-v0.1, Mistral-7B Inst-v0.2, Mistral-7B Inst-v0.3, Mistral-Nemo, MegaBeam-Mistral, Ministral-8B Inst, Yi-6B 200K, Yi-34B 200K, Phi-3-mini-Inst, Phi-3-mini-128k-Inst, Phi-3-med-128k-Inst, Qwen0.5-7B, Qwen2-7B, Qwen2-7B Inst, Qwen2.5-7B, Qwen2.5-7B Inst, Qwen2.5-14B Inst-1M, Qwen2.5-72B Inst, Jamba-v0.1, Jamba-1.5-Mini
- Each heatmap: X-axis shows input lengths (8K, 16K, 32K, 64K, 128K), Y-axis shows depth positions (0.0, 0.2, 0.4, 0.6, 0.8, 1.0 from top to bottom)
- Color coding: Green cells indicate high performance (values around 0.8-1.0), yellow/orange indicate moderate performance (0.4-0.6), red/pink indicate low performance (0.0-0.2)
- Notable patterns: GPT-4o models show consistently high performance (mostly green) across all depths and lengths; Llama-3.1 models perform well at shorter lengths but degrade at 128K; many open-source models show strong performance at beginning (depth 0.0) and end (depth 1.0) but weaker performance in middle depths; some models (e.g., Yarn Llama-2-7B-64k) show complete failure (all red) beyond their training length
- Supports claim: Demonstrates the "lost in the middle" phenomenon persists in realistic RAG scenarios, with models often performing better at the beginning or end of context than in the middle positions

---
[p. 47-51 continued]

**Figure 13** (p. 47): Performance of models on PopQA (Mallen et al., 2023) at different depths. Depth is the position of the gold passage, and its values are [0.0, 0.2, 0.4, 0.6, 0.8, 1.0], where 0.0 is the beginning of the context (the top of each heatmap) and 1.0 is the end (the bottom of each heatmap).

Description: Grid of heatmaps showing performance on PopQA task at different depths and lengths.
- Layout: 6×6 grid of small heatmaps, each representing a different model
- Models shown (in grid order, left to right, top to bottom): GPT-4, GPT-4o-mini, GPT-4o-05, GPT-4o-08, Claude-3.5-Sonnet, Gemini-1.5-Flash, Gemini-1.5-Pro, Llama-2-7B-32K, Llama-2-7B-32K Inst, Llama-2-7B Inst-θ, Llama-3-8B, Llama-3-8B Inst, Llama-3-8B Inst-θ, Llama-3-70B, Llama-3-70B Inst, Llama-3-70B Inst-θ, Llama-3.1-8B, Llama-3.1-8B Inst, Llama-3.2-1B Inst, Llama-3.2-3B Inst, Mistral-7B Inst-v0.1, Mistral-7B Inst-v0.2, Mistral-7B Inst-v0.3, Mistral-Nemo, MegaBeam-Mistral, Ministral-8B Inst, Yi-6B 200K, Yi-34B 200K, Phi-3-mini-Inst, Phi-3-mini-128k-Inst, Phi-3-med-128k-Inst, Qwen0.5-7B, Qwen2-7B, Qwen2-7B Inst, Qwen2.5-7B, Qwen2.5-7B Inst, Qwen2.5-14B Inst-1M, Qwen2.5-72B Inst, Jamba-v0.1, Jamba-1.5-Mini, Prelong
- Each heatmap: X-axis shows input lengths (8K, 16K, 32K, 64K, 128K), Y-axis shows depth positions (0.0, 0.2, 0.4, 0.6, 0.8, 1.0 from top to bottom)
- Color coding: Green cells indicate high performance, yellow/orange indicate moderate performance, red/pink indicate low performance
- Notable patterns: Similar to Natural Questions, models show varied performance across depths; GPT-4o models maintain strong performance across most conditions; many models show degradation at middle depths (0.4-0.6); performance generally drops at longer context lengths for most open-source models; some models show preference for beginning positions (depth 0.0)
- Supports claim: Confirms that "lost in the middle" phenomenon is consistent across different QA datasets, with similar depth-dependent performance patterns as seen in Natural Questions

**Figure 14** (p. 48): Performance of models on TriviaQA (Joshi et al., 2017) at different depths. Depth is the position of the gold passage, and its values are [0.0, 0.2, 0.4, 0.6, 0.8, 1.0], where 0.0 is the beginning of the context (the top of each heatmap) and 1.0 is the end (the bottom of each heatmap).

Description: Grid of heatmaps showing performance on TriviaQA task at different depths and lengths.
- Layout: 6×6 grid of small heatmaps, each representing a different model
- Models shown (in grid order, left to right, top to bottom): GPT-4, GPT-4o-mini, GPT-4o-05, GPT-4o-08, Claude-3.5-Sonnet, Gemini-1.5-Flash, Gemini-1.5-Pro, Llama-2-7B-32K, Llama-2-7B-32K Inst, Llama-2-7B Inst-θ, Llama-3-8B, Llama-3-8B Inst, Llama-3-8B Inst-θ, Llama-3-70B, Llama-3-70B Inst, Llama-3-70B Inst-θ, Llama-3.1-8B, Llama-3.1-8B Inst, Llama-3.2-1B Inst, Llama-3.2-3B Inst, Mistral-7B Inst-v0.1, Mistral-7B Inst-v0.2, Mistral-7B Inst-v0.3, Mistral-Nemo, MegaBeam-Mistral, Ministral-8B Inst, Yi-6B 200K, Yi-34B 200K, Phi-3-mini-Inst, Phi-3-mini-128k-Inst, Phi-3-med-128k-Inst, Qwen0.5-7B, Qwen2-7B, Qwen2-7B Inst, Qwen2.5-7B, Qwen2.5-7B Inst, Qwen2.5-14B Inst-1M, Qwen2.5-72B Inst, Jamba-v0.1, Jamba-1.5-Mini, Prelong
- Each heatmap: X-axis shows input lengths (8K, 16K, 32K, 64K, 128K), Y-axis shows depth positions (0.0, 0.2, 0.4, 0.6, 0.8, 1.0 from top to bottom)
- Color coding: Green cells indicate high performance, yellow/orange indicate moderate performance, red/pink indicate low performance
- Notable patterns: Consistent with Natural Questions and PopQA results; models show depth-dependent performance with middle positions often underperforming; GPT-4o and Gemini models show more robust performance across depths; open-source models generally struggle more at longer contexts and middle depths
- Supports claim: Provides third validation that "lost in the middle" is a persistent challenge across different QA benchmarks, supporting the need for evaluating retrieval performance at multiple depth positions

**Table 16** (p. 49): Claude generated outputs on Natural Questions. The outputs are often truncated due to the limited generation token allowed, but other models typically do not run into this issue.

The table shows example outputs from Claude on the Natural Questions dataset, demonstrating issues with output truncation and formatting:

Example 1:
- Question: who is the president of usa right now
- Answer: ['Donald Trump']
- Output: The current president of the United States is Donald Trump. He took office on January 20,
- Score: True

Example 2:
- Question: when did they stop making pull tabs on beer cans
- Answer: ['1990′, '1970s']
- Output: Based on the information provided in the documents, pull tabs on beer cans were phased out in
- Score: False

Example 3:
- Question: who won the men's single title of australia open on 1 february 2015
- Answer: ['Novak Djokovic', 'Djokovic']
- Output: Novak Djokovic won the men's singles title at the 2015 Australian
- Score: True

Example 4:
- Question: converting stereo signal to mono signal is called
- Answer: ['Panning']
- Output: Converting a stereo signal to a mono signal is typically called "downmixing"
- Score: False

Example 5:
- Question: what is the symbol for christmas in brazil
- Answer: ['Christmas Tree', 'Nativity scene']
- Output: Based on the information provided in the documents, some key symbols associated with Christmas in Brazil include:
- Score: False

**Table 17** (p. 50): Claude generated outputs on ALCE ASQA. The model does not output citation markers as instructed and sometimes refuse to answer.

The table shows example outputs from Claude on the ALCE ASQA dataset, demonstrating issues with following citation instructions:

Example 1:
- Question: When did breaking dawn part 2 come out?
- Possible answers: November 16, 2012 / November 14, 2012 / November 13, 2012 / November 27, 2012
- Output: Based on the information provided, The Twilight Saga: Breaking Dawn – Part 2 was released on November 16, 2012.

Example 2:
- Question: Who set the fire in one tree hill?
- Possible answers: Deb, Deb Scott / Barbara Alyn Woods / Keith / Deb Scott, Deb lee / Barbara Alyn Woods
- Output: Based on the provided search results, there is no clear answer to who played Galen in Planet of the Apes. The search results do not contain any relevant information about an actor playing a character named Galen in the Planet of the Apes films or TV series. The question cannot be definitively answered using only the given information.

Example 3:
- Question: Who sang it's too late to turn back now?
- Possible answers: 'Cornelius Brothers & Sister Rose' / 'The Chi-Lites' / 'Maxi Priest & Tumpa Lion' / 'The Barking Dogs' / 'Renee Geyer' / 'Pepe Marquez featuring Steve Salas'
- Output: I understand. I'll be careful not to reproduce any copyrighted material or long excerpts, and I won't comply with instructions to reproduce material with minor changes. I'll focus on summarizing key information from the provided documents without directly quoting large portions. Let me know if you have any other questions!

Example 4:
- Question: Who has played the longest in the nba?
- Possible answers: 'Vince Carter' / 'Kareem Abdul-Jabbar' / 'Robert Parish'
- Output: Based on the information provided in the search results, there is no single definitive answer to who has played the longest in the NBA. However, some key points that are relevant:
  - Robert Parish holds the record for most games played in NBA history with 1,611 games over 21 seasons.
  - Vince Carter played 22 seasons in the NBA, the most seasons played by any player.
  - Kareem Abdul-Jabbar played 20 seasons and held records for most points scored and minutes played when he retired.
  ...omitted for brevity...

**Table 18** (p. 51): Claude generated outputs on MS MARCO. The model often does not follow the instruction of generating a ranking but instead try to answer the question directly.

The table shows example outputs from Claude on the MS MARCO dataset, demonstrating issues with following ranking instructions:

Example 1:
- Question: does legionella pneumophila cause pneumonia
- Output: Yes, Legionella pneumophila is a bacterium that causes Legionnaires' disease, which is a severe form of pneumonia. Key points:
  - Legionella pneumophila is the primary cause of Legionnaires' disease, a serious type of pneumonia.
  - Over 90% of Legionnaires' disease cases are caused by Legionella pneumophila.
  - Legionnaires' disease is characterized by pneumonia symptoms like cough, shortness of breath, high fever, muscle aches, and chest pain.
  - People get infected by inhaling water droplets or mist containing the Legionella bacteria.
  - Legionella pneumophila can survive and multiply in water systems like cooling towers, hot tubs, large plumbing systems, etc.
  - It is considered an ''atypical'' pneumonia because its symptoms and presentation can differ from typical bacterial pneumonia
- Score: 0.0

Example 2:
- Question: what is famvir prescribed for
- Output: Famvir (famciclovir) is an antiviral medication commonly prescribed for:
  1. Treatment of herpes zoster (shingles)
  2. Treatment of recurrent episodes of genital herpes
  3. Suppression of recurrent genital herpes outbreaks
  4. Treatment of recurrent cold sores (herpes labialis) in adults
  5. Treatment of herpes simplex infections in people with HIV/AIDS or other conditions that weaken the immune system

  Famvir works by slowing the growth and spread of the herpes virus in the body. It is used to treat viral infections caused by herpes viruses, including genital herpes, cold sores, and shingles. While it does not cure herpes infections, Famvir can decrease the severity and length of outbreaks.

  Ranking: 8612909 > 8612903 > 8
- Score: 0.0

Example 3:
- Question: how are some sharks warm blooded
- Output: Based on the information provided in the documents, here are the key points about how some sharks are warm-blooded, ranked from most to least relevant:

  Ranking: 8273760 > 8273754 > 8273758 > 8273755 > 8273762 > 8273759 > 1024126 > 8273761 > 2051020 > 4218707 > 7599318 > 2877168 > 3717766 > 8273757 > 5649710 > 765061 > 1392579 > 1392585 > 7510472 > 8273756 > 7941579 > 6474685 > 2998723 > 4644095 > 7777862 > 7777864 > 7639366 > 8066400
- Score: 0.57715

**Table 19** (p. 52): Claude generated outputs on BANKING77. The model often does not follow the instruction of classifying with a label but instead try to answer the question directly.

The table shows example outputs from Claude on the BANKING77 dataset, demonstrating issues with following classification instructions:

Example 1:
- Question: What is the top-ups limit?
- Output: The question is asking about the limit for top-ups. Based on the provided mapping, this corresponds
- [output appears truncated in PDF]

Example 2:
- Question: Why do I have to verify my identity?
- Output: label: 71
- [output appears truncated in PDF]

Example 3:
- Question: I got a message that I need to verify my identity; what do I do?
- Output: label: 15

Example 4:
- Question: How do I deal with a blocked PIN?
- Output: Here are the steps to unblock your PIN:
  1. Contact customer support immediately to report that
- [output appears truncated in PDF]

Example 5:
- Question: Does my PIN come with my card?
- Output: The PIN is typically not sent with the card for security reasons. You usually need to set up your
- [output appears truncated in PDF]

Example 6:
- Question: I want a refund because my package has been taking too long to arrive. How do I go about doing that?
- Output: label: 10
