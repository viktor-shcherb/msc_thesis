# A Dataset Details [p. 13-14]

[p. 13] Table 7 lists the instantiation of (I, C, A) for each dataset in LongBench. Table 8 reports the number of data on each task that falls in the length range of 0-4k, 4k-8k, and 8k+ in LongBench-E.

## Table 7 [p. 13]

**Table 7** (p. 13): "Instantiation of (I, C, A) for each task in LongBench."

| Dataset | Input *I* | Context *C* | Answer *A* |
|---|---|---|---|
| *Single-Document QA* | | | |
| NarrativeQA | Question | Document | Answer |
| Qasper | Question | Document | Answer |
| MultiFieldQA-en | Question | Document | Answer |
| MultiFieldQA-zh | Question | Document | Answer |
| *Multi-Document QA* | | | |
| HotpotQA | Question | Multiple documents | Answer |
| 2WikiMultihopQA | Question | Multiple documents | Answer |
| MuSiQue | Question | Multiple documents | Answer |
| DuReader | Question | Multiple documents | Answer |
| *Summarization* | | | |
| GovReport | - | Document | Summary |
| QMSum | Query | Document | Summary |
| MultiNews | - | Document | Summary |
| VCSUM | - | Document | Summary |
| *Few-shot Learning* | | | |
| TREC | Question | Few-shot examples | Class label |
| TriviaQA | Passage&Question | Few-shot examples | Answer |
| SAMSum | Dialogue | Few-shot examples | Summary |
| LSHT | News document | Few-shot examples | Class label |
| *Synthetic Task* | | | |
| PassageCount | - | Multiple passages | Count |
| PassageRetrieval-en | Summary | Multiple passages | Title of the passage |
| PassageRetrieval-zh | Summary | Multiple passages | Title of the passage |
| *Code Completion* | | | |
| LCC | - | Preceding lines of code | Next line of code |
| RepoBench-P | Preceding lines of code | Cross-file code snippets | Next line of code |

## Table 8 [p. 14]

**Table 8** (p. 14): "Data length distributions in LongBench-E."

| Dataset | #data in 0-4k | #data in 4-8k | #data in 8k+ |
|---|---|---|---|
| *Single-Document QA* | | | |
| Qasper | 100 | 100 | 24 |
| MultiFieldQA-en | 67 | 70 | 13 |
| *Multi-Document QA* | | | |
| HotpotQA | 100 | 100 | 100 |
| 2WikiMultihopQA | 100 | 100 | 100 |
| *Summarization* | | | |
| GovReport | 100 | 100 | 100 |
| MultiNews | 100 | 100 | 94 |
| *Few-shot Learning* | | | |
| TREC | 100 | 100 | 100 |
| TriviaQA | 100 | 100 | 100 |
| SAMSum | 100 | 100 | 100 |
| *Synthetic Task* | | | |
| PassageCount | 100 | 100 | 100 |
| PassageRetrieval-en | 100 | 100 | 100 |
| *Code Completion* | | | |
| LCC | 100 | 100 | 100 |
| RepoBench-P | 100 | 100 | 100 |

## Details of MultiFieldQA Document Sources [p. 13]

[p. 13] The sources of the documents in MultiFieldQA include:

- **Arxiv** (for academic papers): open-accessed and can be downloaded freely by anyone.
- **C4 Dataset**: publicly available dataset with ODC-BY license.
- **WuDaoCorpora**: open-accessed dataset.
- **Chinese Judgements Online** (for Chinese legal documents): open Chinese judgements download website.
- **Wikipedia** (for encyclopedias): grants free access and licensed under CC BY-SA.
- **Chinese Government Website** (for Chinese government report): open Chinese government report download website.

## Annotation Guidelines for MultiFieldQA [p. 13-14]

[p. 13-14] The annotation guidelines provided to annotators:

> "Please propose one question and a groundtruth answer for each of the following documents. Requirements: 1. Questions should be as clear as possible and have definitive and relatively short answers. 2. The distribution of the evidence paragraphs should be as random as possible throughout the article. 3. Ensure that the questions have varied types, including, but not limited to, information-extracting questions (e.g., the time of an event, the date of birth of a person, etc.), summarizing questions (e.g., which people do the article mainly describes), and multi-hop reasoning questions." [p. 13-14]

The average time taken to annotate each data sample in MultiFieldQA is around 5 minutes. The annotators involved in this process are Ph.D. students with extensive research experience in the field of NLP, positioning them as expert annotators. Cross-validation among annotators shows a 100% accuracy rate of the annotated answers. [p. 14]
