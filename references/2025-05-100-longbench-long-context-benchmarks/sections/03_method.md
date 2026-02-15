# 3 How to truly evaluate Language Models' long-context capability? [p. 3-6]

[p. 3] To address the two identified problems, the authors 1) construct a length-controllable long-context benchmark to reduce performance variance across lengths, and 2) introduce LongScore, a new metric designed to accurately evaluate long-context capabilities by disentangling the model's baseline abilities.

In detail, the authors restructure the long-context datasets, based on LongBench, L-EVAL, and other benchmarks. The authors then design a new pipeline to generate controllable-length long contexts by combining different articles. Additionally, the authors introduce a filtering mechanism in QA-related tasks to mitigate prior knowledge. Subsequently, the authors propose a new metric to isolate a model's long-text capability from Base Ability (performance on short texts).

## 3.1 Construct a new long-context benchmark [p. 3-4]

[p. 3] The authors categorize tasks into four types with different levels of difficulty, resulting in a total of eight tasks. The types and their corresponding tasks are:

- **Key Retrieval** (including **KV Retrieval** and **Counting Stars**)
- **Information Retrieval** (including **Passage Retrieval** and **Passage Count**)
- **Information Comprehension** (including **Single-doc QA** and **Multi-doc QA**)
- **Information Summarization** (including **Single-doc Sum** and **Multi-doc Sum**)

Table 2 provides details for each task, including: Real Context Sources (the context sources of the question used in the task), Noisy Context Sources (the source of additional context that may contain irrelevant or distracting information) and Evaluation Metric (the metric used to assess model performance for each task). All of these datasets are from other benchmarks like LongBench, etc. Detailed information on context construction, question setup, and evaluation metrics, are in Appendix A.2.

### How to generate a controllable-length context

[p. 3] In 🏀-LongBench, the context length for each task is controllable, such as generating a context of approximately 128k tokens. To achieve this, the authors first randomly select one article from Real Context Sources as the ground truth article. Then, the authors randomly sample a number of articles from Noisy Context Sources as distractor articles. These distractor articles are combined with the ground truth article to construct the whole context, ensuring that the total context length is close to but less than 128k. Finally, the order of all articles is shuffled to create the context. Figure 3 illustrates the data generation process for Single-Doc QA task, showing how questions, answers, and contexts are prepared.

**Figure 3** (p. 3): "Illustration of the Data Generation Process for the Single-Doc QA Task"

Description: Flow diagram showing the data generation pipeline
- Key elements: Shows progression from Real Context (ground truth article with question) and Noisy Context (distractor articles) through combination to final context with embedded ground truth
- Process flow:
  1. Real Context: Select ground truth article and question
  2. Noisy Context: Sample distractor articles
  3. Combination: Merge and shuffle articles
  4. Final: Context with question "What is in ChatGLM3D approach?"
- Notable patterns: Illustrates how controllable-length contexts are created by combining real and noisy sources
- Supports claim: Method for generating length-controlled contexts while maintaining task relevance

**Table 2: Details of dataset construction for each task** [p. 4]

To generate a context of a specified length like 128k, the authors randomly select multiple articles from the Noisy Context Source datasets as distractor articles. A single article is randomly chosen from Real Context Source datasets as the ground truth article. Distractor articles and the ground truth article are combined to form the whole context, ensuring that the whole context length is less than 128k and the order of all articles is shuffled. The bottom of the table contains different datasets from other benchmarks. N/A indicates that the task does not use the corresponding source because the questions are synthetic rather than derived from a dataset. More details about how to construct each task are in Appendix A.2.

| Task Name | Real Context Sources | Noisy Context Sources | Evaluation Metric |
|-----------|---------------------|----------------------|-------------------|
| KV Retrieval | N/A | ①②③④⑤⑥⑦⑧ | Accuracy |
| Counting Stars | N/A | ①②④⑤⑥⑦⑧ | Accuracy |
| Passage Retrieval | ⑨⑩⑪⑫⑬⑭⑮ | ⑨⑩⑪⑫⑬⑭⑮ | Accuracy |
| Passage Count | ①②③④⑤⑥⑦⑧ | N/A | Accuracy |
| Single-doc QA | ①②③④⑤⑥⑦⑧ | ①②③④⑤⑥⑦⑧ | LLM-based Metric |
| Multi-doc QA | ⑯⑰⑱⑲ | ①②③④⑤⑥⑦⑧ | LLM-based Metric |
| Single-doc Sum | ①⑯⑰⑱⑲ | ①⑯⑰⑱⑲ | LLM-based Metric |
| Multi-doc Sum | ㉑ | ①⑯⑰⑱⑲ | LLM-based Metric |

**Dataset legend:**
- ① qasper ② multifieldqa_en ③ narrativeqa ④ multidoc_qa ⑤ legal_contract_qa
- ⑥ financial_qa ⑦ natural_question ⑧ scientific_qa ⑨ cnn_dailymail ⑩ gov_report
- ⑪ qmsum ⑫ patent_summ ⑬ tv_show_summ ⑭ review_summ ⑮ meeting_summ
- ⑯ hotpotqa ⑰ 2wikimqa ⑱ musique ⑲ rag-mini-bioasq ⑳ multi_news_e

### QA Filtering Mechanism

[p. 3-4] **QA Filtering Mechanism**. For Multi-Doc QA and Single-Doc QA tasks, the authors introduce a filtering mechanism to eliminate the influence of the model's inherent prior knowledge. When evaluating a model's long-context capabilities, prior knowledge is often overlooked. For instance, in question-answering (QA) tasks, the model might memorize the answers to certain questions during pretraining. As shown in Figure 4, the model accurately answers questions based on its prior knowledge even without any contexts. In such cases, the model's response is not derived from the provided context but from its memorized knowledge. This oversight can lead to inflated performance metrics, misrepresenting the model's actual success and comprehend long contexts.

To filter out the model's prior knowledge, the authors introduce a QA filtering mechanism. In a long-context QA task, if the model's response score exceeds a certain threshold, it indicates that the model is relying on prior knowledge, showing the data should be filtered.

**Figure 4** (p. 4): "One sample in Question Answering where models provide accurate answers regardless of context"

Description: Two-panel illustration showing QA filtering mechanism
- Left panel: Shows two questions about Miryai with answers derived from context
- Right panel: Shows same questions with "This Doc dynasty" placeholder text, demonstrating answers still provided without proper context
- Key elements: Questions in boxes, document icon in center, QA Answer boxes on right showing correct answers despite lack of context
- Notable patterns: Model can answer correctly even without relevant context, indicating reliance on prior knowledge
- Supports claim: Need for QA filtering mechanism to remove questions answerable from prior knowledge

### Real-life Reflective Design

[p. 4] Although the length-controlled datasets are synthetically constructed, they are carefully designed to better reflect real-world usage scenarios, which the authors called as real-life reflective. Specifically, each instance is composed by selecting a task-relevant example as the *source* (e.g., a summarization prompt and document), and padding it with additional samples that belong to the same domain or task type (e.g., other documents suitable for summarization). This construction ensures that all components of the input are contextually aligned and task-compatible, mimicking common usage patterns in long-context settings, such as concatenated inputs in retrieval-augmented generation pipelines.

## 3.2 LongScore: a new long-context metric [p. 4-5]

[p. 4] As illustrated in Figure 2, directly using a model's scores across various text lengths to assess its long-context capability introduces inherent biases. To address this limitation, the authors propose a new metric that disentangles a model's base ability from its long-context capability, allowing for a more accurate and comprehensive evaluation.

### Base Ability

[p. 4] **Base Ability**. It refers to the model's score when conducting short-context tasks. To estimate Base Ability, the authors sample N instances from short text lengths (like 2k, 4k, 6k). For each length, N/3 samples are selected, and the model's average score across these lengths is computed:

$$\text{Base Ability} = \frac{S_{2k} + S_{4k} + S_{6k}}{3}$$ (1)

where $S_{*k}$ represents the performance of model with the $* = k$ length.

### LongScore

[p. 4-5] **LongScore (LC_l)** is the authors' proposed metric. For longer lengths (e.g., 8k, 16k, 32k), the authors calculate the score on N instances for each length. LC_l at a given length l is then defined as:

$$\text{LC}_l = \frac{S_l - \text{Base Ability}}{\text{Base Ability}}$$ (2)

LongScore separates the model's Base Ability from Long-context Capability. The authors' metric focuses on the relative improvement or decline at longer lengths and provides a more precise assessment of long-context capabilities without being influenced by the model's Base Ability. It enables consistent and unbiased comparisons of long-context capabilities across different models and datasets.
