# The SCROLLS Benchmark [p. 3-6]

[p. 3] SCROLLS aims to challenge a model's ability to process long texts in the wild, and therefore focuses on discourses that are *naturally* long, encompassing domains such as literature, TV show scripts, scientific articles, and more. The authors review datasets in existing literature, seeking ones that challenge models not only by the length of each input, but also by the need to process long-range dependencies across different sections. At the same time, they strive to maintain a diversity of tasks, covering summarization and query-based summarization, open ended and multiple-choice question answering, as well as natural language inference.

Through this curation process, 7 datasets are handpicked and processed into a uniform text-to-text format.

**Table 1** (p. 3): "An overview of the datasets in SCROLLS and their statistics. *Summ* refers to summarization, *QB-Summ* means query-based summarization, and *MC-QA* abbreviates multiple-choice question answering. The number of examples includes train, validation, and test sets."

| Dataset | Task | Domain | Metric | Avg #Words Input | Avg #Words Output | #Examples |
|---|---|---|---|---|---|---|
| GovReport (Huang et al., 2021) | Summ | Government | ROUGE | 7,886 | 492.5 | 19,402 |
| SummScreenFD (Chen et al., 2021) | Summ | TV | ROUGE | 5,598 | 99.6 | 4,348 |
| QMSum (Zhong et al., 2021) | QB-Summ | Meetings | ROUGE | 9,497 | 69.7 | 1,810 |
| Qasper (Dasigi et al., 2021) | QA | Science | F1 | 3,629 | 11.4 | 5,692 |
| NarrativeQA (Kočiský et al., 2018) | QA | Literature, Film | F1 | 51,653 | 4.6 | 71,187 |
| QuALITY (Pang et al., 2021) | MC-QA | Literature, Misc | EM | 4,193 | 10.3 | 6,737 |
| ContractNLI (Koreeda and Manning, 2021) | NLI | Legal | EM | 1,706 | 1.4 | 10,319 |

## 3.1 Datasets

[p. 3] The authors survey the 7 datasets in SCROLLS and elaborate how the original data was collected.

### GovReport

(Huang et al., 2021): A summarization dataset of reports addressing various national policy issues published by the Congressional Research Service and the U.S. Government Accountability Office, where each document is paired with an expert-written executive summary. The reports and their summaries are longer than their equivalents in other popular long-document summarization datasets; for example, GovReport's documents are approximately 1.5 and 2.5 times longer than the documents in arXiv and PubMed (Cohan et al., 2018), respectively.

### SummScreenFD

[p. 3-4] (Chen et al., 2021): A summarization dataset in the domain of TV shows (e.g. Friends, Game of Thrones). Given a transcript of a specific episode, the goal is to produce the episode's recap. The original dataset is divided into two complementary subsets, based on the source of its community contributed transcripts. For SCROLLS, the ForeverDreaming (FD) subset is used, as it incorporates 88 different shows, making it a more diverse alternative to the TV MegaSite (TMS) subset, which has only 10 shows. Community-authored recaps for the ForeverDreaming transcripts were collected from English Wikipedia and TVMaze.

**Figure 2** (p. 4): "An example from the SummScreenFD summarization dataset, where the task is to generate the recap (top paragraph) given the episode's script. In this example, the information required to compose the third sentence in the recap (highlighted) is scattered across several snippets throughout the transcript."
- Shows a recap paragraph at the top with highlighted text, followed by a transcript excerpt with dialogue snippets from what appears to be a Big Bang Theory episode. Word count markers (e.g., "...[1,032 words]...", "...[40 words]...", "...[660 words]...", "...[766 words]...", "...[142 words]...") indicate large gaps between relevant snippets, demonstrating how information is spread across the long input.

### QMSum

[p. 4] (Zhong et al., 2021): A query-based summarization dataset, consisting of 232 meetings transcripts from multiple domains and their corresponding summaries. The corpus covers academic group meetings at the International Computer Science Institute (Janin et al., 2003), industrial product meetings for designing a remote control (Carletta et al., 2005), and committee meetings of the Welsh and Canadian Parliaments, dealing with a variety of public policy issues. Annotators were tasked with writing queries about the broad contents of the meetings, as well as specific questions about certain topics or decisions, while ensuring that the relevant text for answering each query spans at least 200 words or 10 turns.

### Qasper

[p. 4] (Dasigi et al., 2021): A question answering dataset over NLP papers filtered from the Semantic Scholar Open Research Corpus (S2ORC) (Lo et al., 2020). Questions were written by NLP practitioners after reading only the title and abstract of the papers, while another set of NLP practitioners annotated the answers given the entire document. Qasper contains abstractive, extractive, and yes/no questions, as well as unanswerable ones.

### NarrativeQA

[p. 4-5] (Kočiský et al., 2018): An established question answering dataset over entire books from Project Gutenberg and movie scripts from different websites. Annotators were given summaries of the books and scripts obtained from Wikipedia, and asked to generate question-answer pairs, resulting in about 30 questions and answers for each of the 1,567 books and scripts. They were encouraged to use their own words rather than copying, and avoid asking yes/no questions or ones about the cast. Each question was then answered by an additional annotator, providing each question with two reference answers (that may be identical).

### QuALITY

[p. 5] (Pang et al., 2021): A multiple-choice question answering dataset over stories and articles sourced from Project Gutenberg, the Open American National Corpus (Fillmore et al., 1998; Ide and Suderman, 2004), and more. Experienced writers wrote questions and distractors, and were incentivized to write answerable, unambiguous questions such that in order to correctly answer them, human annotators must read large portions of the given document. To measure the difficulty of their questions, Pang et al. conducted a speed validation process, where another set of annotators were asked to answer questions given only a short period of time to skim through the document. As a result, 50% of the questions in QuALITY are labeled as *hard*, i.e. the majority of the annotators in the speed validation setting chose the wrong answer.

**Figure 3** (p. 4-5): "An example from the QuALITY dataset, where the task is to answer multiple-choice questions about a given story or document. In this example, answering the question correctly requires reasoning over four different snippets that are separated by long token sequences."
- Shows a multiple-choice question: "The text says 'The expert frowned horribly.' What makes the expert's smile so horrible?" with four answer options (A-D).
- Below the question is a story excerpt with word count markers ("...[607 words]...", "...[257 words]...", "...[1,366 words]...", "...[33 words]...", "...[1,808 words]...") showing how relevant snippets are dispersed across the long input, demonstrating the need for long-range reasoning.

### ContractNLI

[p. 5] (Koreeda and Manning, 2021): A natural language inference dataset in the legal domain. Given a non-disclosure agreement (NDA, the premise), the task is to predict whether a particular legal statement (the hypothesis) is entailed, not entailed (neutral), or cannot be entailed (contradiction) from the contract. The NDAs were manually picked after simple filtering from the Electronic Data Gathering, Analysis, and Retrieval system (EDGAR) and Google. The dataset contains a total of 607 contracts and 17 unique hypotheses, which were combined to produce the dataset's 10,319 examples.

## 3.2 Preprocessing

### Data Cleansing

[p. 5] As part of the curation process, each dataset is examined and cleaned or filtered to ensure high quality data:
- **GovReport:** Discard all examples where the report's length (in words) is less than twice the summary, or more than 1,000 times the summary, as well as examples where the summary exists verbatim in the report. This process removes 64 examples from the original dataset.
- **Qasper:** Discard all papers that have less than 8,192 characters, removing a total of 176 questions over 63 papers, which appear to be of lower quality.
- **NarrativeQA:** Locate markers indicating the start and end of the actual story, and use them to remove excess metadata such as licenses, HTML headers, etc.

### Unified Format

[p. 5] Every dataset in SCROLLS is reformulated as a sequence-to-sequence task to allow for a simple unified input-output format. When a query is given in addition to the raw text (as in QMSum, Qasper, NarrativeQA, QuALITY, and ContractNLI), it is prepended to the text, using two newlines as a natural separator. For the multiple-choice dataset QuALITY, all four answer candidates are also provided as part of the query. For the summarization datasets, GovReport and SummScreenFD, only the original documents are used as input.

Some datasets (Qasper and NarrativeQA) contain multiple target outputs for each input; they are split into separate instances for training and development. For test, each prediction is scored with every valid answer independently, and then the scores of identical inputs are merged by taking the maximum of those scores. Table 5 in Appendix A provides an example from each SCROLLS dataset.

## 3.3 Evaluation

[p. 5-6] Each dataset is split into training, validation, and test sets based on the original dataset splits. In SCROLLS, test set outputs are kept private, and only the inputs are publicly available. When evaluating a model, users must submit their model's outputs for *all* test sets via the SCROLLS website. Once a model is submitted, the average performance metric across all datasets is computed to provide the submission with a single aggregate SCROLLS score.

Three different evaluation metrics are employed across SCROLLS datasets:
- **ROUGE** for summarization tasks (GovReport, SummScreenFD, and QMSum)
- **Unigram overlap (F1)** for question answering (Qasper and NarrativeQA)
- **Exact match (EM)** for multiple-choice (QuALITY) and classification (ContractNLI) tasks

The official evaluation script is available online.

### ROUGE

(Lin, 2004): Three flavors of ROUGE are used to measure the overlap between the system-generated output and the reference: unigram overlap (ROUGE-1), bigram overlap (ROUGE-2), and the longest overlapping subsequence (ROUGE-L). Both system output and reference are normalized by lowercasing and converting all non-alphanumeric characters to whitespaces, followed by whitespace tokenization. The geometric mean of the three scores (ROUGE-1/2/L) is computed to produce a single score per dataset, which is used to calculate the final SCROLLS score.

### F1

Similar to ROUGE-1, the F1 metric calculates unigram overlap. The key difference is that both reference and system output strings are normalized slightly differently; in addition to lowercasing and punctuation removal, stopwords are also discarded, following the practice of SQuAD (Rajpurkar et al., 2016) and other question-answering datasets (Fisch et al., 2019). Both Qasper and NarrativeQA contain questions with more than one reference answer; for each such example, the maximal F1 score over all of its reference answers is taken.

### EM

[p. 6] Exact match normalizes the output strings using the same procedure as F1 (lowercasing, removing punctuation and stopwords, and normalizing whitespaces), and then compares whether the two normalized strings are identical. For QuALITY, EM is calculated over the entire test set (EM-T), and also EM over its subset of *hard* questions (EM-H), as defined in the original dataset. For computing the final SCROLLS score, however, only the EM value calculated over the full test set (EM-T) is used.
