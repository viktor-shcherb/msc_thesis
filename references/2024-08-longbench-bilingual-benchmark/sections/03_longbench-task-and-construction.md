# 3 LongBench: Task and Construction [p. 3-6]

## 3.1 Problem Definition [p. 3]

The problem of long context understanding is formalized as: Given the input and context sequences (I, C), the model is expected to output the answer A. For instance, in a QA task, the input I would be the question, context C refers to the document, and A denotes the answer to the question. Generally, in LongBench, I and A tend to be short, while C represents a long sequence up to thousands of tokens in length. The instantiation of (I, C, A) for each task is listed in Table 7.

## 3.2 Dataset Construction [p. 3-6]

### 3.2.1 Data Collection and Annotation [p. 3-5]

**Single-Doc QA** [p. 3]: Focus on instances with longer documents.
- *NarrativeQA*: extracted from Kočiský et al. (2018), consists of long stories with questions posed to test reading comprehension.
- *Qasper*: sampled from Dasigi et al. (2021), features QA over NLP papers, annotated by NLP practitioners.
- *MultiFieldQA* (English and Chinese): manually curated by the authors. Documents and articles collected from multiple sources including legal documents, government reports, encyclopedias, academic papers, etc. Three Ph.D. students annotated the question and answer for each article, with definitive answers as much as possible for ease of automated evaluation. During annotation, the placement of evidence is fairly random to avoid biases such as answer-related statements being frequently found at the beginning or the end, as mentioned in Liu et al. (2023a).

**Multi-Doc QA** [p. 3-4]: Requires models to extract and combine information from several documents; usually more challenging than single-doc QA.

English test samples built from three Wikipedia-based multi-hop QA datasets:
- *HotpotQA* (Yang et al., 2018): 2-hop questions directly written by native speakers given two related paragraphs.
- *2WikiMultihopQA* (Ho et al., 2020): up to 5-hop questions synthesized through manually designed templates to ensure they cannot be solved through shortcuts.
- *MuSiQue* (Trivedi et al., 2022): questions carefully composed from simple questions involving up to 4-hop reasoning, then paraphrased by annotators to both avoid shortcuts and ensure linguistic naturalness. Each question in the original datasets is supplemented by 2-4 supporting paragraphs and several distracting paragraphs.

To tailor for long-context evaluation, the authors use complete Wikipedia passages encompassing the supporting or distracting paragraphs as context. Supporting passages are included within the context, then distracting passages are added until total length reaches a maximum length. Passages are randomly ordered to form the multi-document context.

- *DuReader* (Chinese): based on He et al. (2018), developed on Baidu Search and Baidu Zhidao, comprising 200K questions and 1M related documents. Adapted for long context by providing several documents related to each question plus arbitrarily selected distractors from the total set, until each question is associated with 20 documents.

**Summarization** [p. 4]: Demands a more global understanding of the whole context compared to QA tasks.
- *GovReport*: extracted from Huang et al. (2021), a large-scale collection of detailed reports from the U.S. Government Accountability Office and Congressional Research Service, each with a human-written summary.
- *QMSum*: sampled from Zhong et al. (2021), query-summary pairs annotated over 232 meetings across multiple domains including product, academic, and committee meetings. Query treated as input I, meeting content as context C, summary as answer A.
- *MultiNews*: derived from the original multi-document summarization dataset in Fabbri et al. (2019). Features clusters of 2-10 news articles discussing the same event or topic, each paired with a human-written summary. In LongBench, "Document i" is included before the i-th news article and concatenated into context C.
- *VCSUM* (Wu et al., 2023): a large-scale Chinese meeting summarization dataset of 239 real-life meetings with over 230 hours of duration, with versatile annotations. In LongBench, the long segments from VCSUM are selected.

**Few-shot Learning** [p. 4-5]: Few-shot in-context learning identified as a practical setting requiring long context understanding, especially when the number of examples increases (Ainslie et al., 2023). Tasks incorporate classification, summarization, and reading comprehension in the few-shot scenario.

Classification datasets:
- *TREC* (Li and Roth, 2002): question classification task involving 50 fine classes.
- *LSHT* (NLPCC, 2014): Chinese news classification task with 24 classes.

Summarization task:
- *SAMSum* (Gliwa et al., 2019): messenger-like conversations with human-annotated summaries.

Reading comprehension:
- *TriviaQA* (Joshi et al., 2017): question-answer pairs labeled with evidence passages. Filtered to passages with less than 1,000 words to be examples.

For each dataset adapted for LongBench, a random integer is selected within a range as the number of examples, then the corresponding number of samples is randomly drawn from the training set and concatenated to form context C. Ranges: TREC [100, 600], LSHT [10, 40], SAMSum [10, 100], TriviaQA [2, 24].

**Synthetic Task** [p. 5]: Unlike standard tasks, synthetic tasks are meticulously designed to test the model's ability on specific scenarios and patterns. Three synthetic tasks designed:

- *PassageRetrieval-en* and *PassageRetrieval-zh*: constructed based on English Wikipedia and the Chinese sections of the C4 dataset (Raffel et al., 2020). For each data entry, 30 passages are randomly sampled, one is selected for summarization using GPT-3.5-Turbo. The task asks the model to identify the original paragraph to which the crafted summary corresponds.

- *PassageCount*: tests a situation where the model is required to utilize the full context. Several passages from English Wikipedia are randomly selected, each paragraph repeated at random several times, then shuffled. The task asks the model to determine the number of unique passages. Specifically, M is randomly selected from [17, 50] as the upper limit for the number of passages. N unique passages is randomly selected from [2, M]. Random sampling with replacement from the set of N unique passages produces the final M passages.

**Code Completion** [p. 5]: A critical task for auto-completion systems. Recognized as suitable for evaluating long context modeling ability because models need to establish attention across long-range sequences according to relationships within code elements.

- *LCC*: sampled from the original Long Code Completion dataset (Guo et al., 2023). Constructed by filtering code within one file from GitHub based on length. A long piece of preceding lines of code as context, and the next line of code as the answer.

- *RepoBench-P*: adapted from Liu et al. (2023b). Collected from GitHub repositories, constructed by retrieving relevant code snippets from other files based on module import statements. These snippets are concatenated with the preceding lines of code within the current file as context and used to predict the next line of code. The most challenging XF-F (Cross-File-First) setting is selected, where the in-file context gives no prior usage of the module to aid the prediction. Cross-file code snippets are shuffled and combined into context C. Preceding lines of code are input I, and the next line of code is answer A.

### 3.2.2 Data Extraction [p. 5-6]

[p. 5-6] To avoid test leakage (since LLMs may have been trained on collected public datasets), data is extracted from the test sets of public datasets, with the exception of VCSUM due to insufficient data in its test set.

Two extraction strategies:
1. **Random sampling**: maintains a natural length distribution to more accurately mimic real scenarios, producing LongBench.
2. **Uniform sampling**: based on length, to study the model's capabilities across varying context lengths within each task. Uses word count as the length metric and samples a comparable quantity of data from length ranges of 0-4k, 4k-8k, and 8k+. The resulting data is compiled into **LongBench-E** (statistics in Table 8).

[p. 6] For LongBench-E, 13 English datasets are chosen: Qasper, MultiFieldQA-en, HotpotQA, 2WikiMultihopQA, GovReport, Multi-news, TREC, TriviaQA, SAMSum, PassageCount, PassageRetrieval-en, LCC, and RepoBench-P, which offer broader coverage on data length.

## Figure 1 [p. 2]

**Figure 1** (p. 2): "Left: Number of data in each type of task within LongBench. Right: Length distribution for English and Chinese data in LongBench, measured by the number of words and characters."

Left panel: A donut/pie chart showing the number of data points per task category:
- Single-Doc QA: 750
- Multi-Doc QA: 800
- Summarization: 600
- Few-shot: 800
- Synthetic: 600
- Code: 1000

Right panel: A histogram showing length distribution. X-axis: Length (0 to 40000+). Y-axis: Count (0 to ~1000). Both English (blue) and Chinese (green/teal) distributions are shown. The distribution is heavily right-skewed, with the majority of instances concentrated at shorter lengths (0-10000), and a long tail extending to 40000+.

## Table 1 [p. 4]

**Table 1** (p. 4): "An overview of the dataset statistics in LongBench. Chinese datasets are highlighted. 'Source' denotes the origin of the context. 'Avg len' (average length) is computed using the number of words for the English (code) datasets and the number of characters for the Chinese datasets. 'Accuracy (CLS)' refers to classification accuracy, while 'Accuracy (EM)' refers to exact match accuracy."

| Dataset | ID | Source | Avg len | Metric | Language | #data |
|---|---|---|---|---|---|---|
| *Single-Document QA* | | | | | | |
| NarrativeQA | 1-1 | Literature, Film | 18,409 | F1 | English | 200 |
| Qasper | 1-2 | Science | 3,619 | F1 | English | 200 |
| MultiFieldQA-en | 1-3 | Multi-field | 4,559 | F1 | English | 150 |
| MultiFieldQA-zh | 1-4 | Multi-field | 6,701 | F1 | Chinese | 200 |
| *Multi-Document QA* | | | | | | |
| HotpotQA | 2-1 | Wikipedia | 9,151 | F1 | English | 200 |
| 2WikiMultihopQA | 2-2 | Wikipedia | 4,887 | F1 | English | 200 |
| MuSiQue | 2-3 | Wikipedia | 11,214 | F1 | English | 200 |
| DuReader | 2-4 | Baidu Search | 15,768 | Rouge-L | Chinese | 200 |
| *Summarization* | | | | | | |
| GovReport | 3-1 | Government report | 8,734 | Rouge-L | English | 200 |
| QMSum | 3-2 | Meeting | 10,614 | Rouge-L | English | 200 |
| MultiNews | 3-3 | News | 2,113 | Rouge-L | English | 200 |
| VCSUM | 3-4 | Meeting | 15,380 | Rouge-L | Chinese | 200 |
| *Few-shot Learning* | | | | | | |
| TREC | 4-1 | Web question | 5,177 | Accuracy (CLS) | English | 200 |
| TriviaQA | 4-2 | Wikipedia, Web | 8,209 | F1 | English | 200 |
| SAMSum | 4-3 | Dialogue | 6,258 | Rouge-L | English | 200 |
| LSHT | 4-4 | News | 22,337 | Accuracy (CLS) | Chinese | 200 |
| *Synthetic Task* | | | | | | |
| PassageCount | 5-1 | Wikipedia | 11,141 | Accuracy (EM) | English | 200 |
| PassageRetrieval-en | 5-2 | Wikipedia | 9,289 | Accuracy (EM) | English | 200 |
| PassageRetrieval-zh | 5-3 | C4 Dataset | 6,745 | Accuracy (EM) | Chinese | 200 |
| *Code Completion* | | | | | | |
| LCC | 6-1 | Github | 1,235 | Edit Sim | Python/C#/Java | 500 |
| RepoBench-P | 6-2 | Github repository | 4,206 | Edit Sim | Python/Java | 500 |
