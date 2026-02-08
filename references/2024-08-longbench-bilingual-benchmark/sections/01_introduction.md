# 1 Introduction [p. 1-2]

[p. 1] The field of NLP has long sought to endow machines with the ability to understand and reason over long context. Tasks such as summarization and question answering based on books, reports, and documents, and code generation at the repository level demand the ability to model long context sequences that span thousands or even tens of thousands of tokens in length. However, many of today's large language models can only comprehend and generate texts a few thousand tokens long, leaving room for potential improvements in processing longer contexts.

Recent methods to improve LLM capabilities on long context understanding include:
- Extending the context window (Press et al., 2022; Chen et al., 2023)
- Utilizing recurrent memory (Dai et al., 2019; Bulatov et al., 2023)
- Using sparsed attention (Ding et al., 2023; Mohtashami and Jaggi, 2023)
- Augmenting with an external memory (Liang et al., 2023; Zhou et al., 2023)

However, unlike in short context where a multitude of multi-task benchmarks are available for multi-aspect evaluation (Hendrycks et al., 2021; Srivastava et al., 2023), there is no such benchmark on longer context.

[p. 1-2] The authors propose **LongBench**, described as the first bilingual, multi-task benchmark tailored for long context understanding. Key characteristics:
- Composed of 6 major task categories and 21 different tasks
- Covers multi-document QA, single-document QA, summarization, few-shot learning, code completion, and synthetic tasks
- Includes both Chinese and English languages
- Contains 4,750 test instances
- Average length of 6,711 words (English) and 13,386 characters (Chinese)
- Overview statistics shown in Figure 1

[p. 2] All 21 datasets are standardized into a unified format. Of these, 6 are directly extracted from original datasets provided by previous studies, 10 are built based on original datasets and processed for long context evaluation, and 5 are created and annotated by the authors.

Evaluation uses fully automated methods with automatic metrics such as ROUGE-L and F1 to measure similarity of outputs to ground-truth answers.

The authors conduct a comprehensive evaluation of 8 models on LongBench. Key findings:
- The multi-task capability of current models in terms of long context comprehension is assessed
- **LongBench-E** is constructed with a more *even* length distribution, suited for gauging each model's capability across various context lengths
- Results on LongBench-E reveal that although some models are trained or fine-tuned on longer contexts, they still experience a significant decline in performance as context length increases
- Retrieval-based and summarization-based context compression techniques are beneficial only to models that exhibit weaker capability on long contexts
