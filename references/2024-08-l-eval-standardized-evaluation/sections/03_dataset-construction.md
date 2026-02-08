# 3 Towards High-Quality and Diverse Long Context Datasets [p. 3-4]

[p. 3] This section highlights key procedures in L-Eval data construction: annotation, re-annotation, and manual filtering pipeline, along with statistics. Full annotation details and examples are in Appendix B.

## 3.1 Data Annotation from Scratch

[p. 3] There are 4 datasets annotated from scratch in L-Eval: Coursera, SFiction, CodeU, and LongFQA. The original resources are videos from Coursera, previous open-source datasets, source code from famous Python libraries, and public earning call transcripts, respectively.

**Coursera** -- This dataset originates from the Coursera website. To reduce the difficulty of annotation, four public courses related to big data and machine learning are chosen (Section B.4). The input long document is the subtitles of the videos. Questions and the ground truth answers are labeled by the authors. The instruction style of Coursera takes the format of multiple choice. To increase the difficulty of the task, **multiple correct options** have been set. To the best of the authors' knowledge, this is the first multi-choice dataset with multiple correct answers and it is more challenging than single-option questions (Table 3).

**SFiction** -- This sub-task tests the loyalty of the LCLM to the input context. The authors argue that in LCLMs, contextual knowledge (stored in long input) is more crucial than parametric knowledge (gained during pretraining). Practically, many long documents are private and can never be seen during pretraining. LLMs should follow the contextual knowledge instead of parametric knowledge in long context settings. To simulate this scenario, a science fiction dataset consisting of True or False questions is annotated. Most of the answers to these questions contradict real-world principles and do not comply with actual physical laws (Section B.5). Turbo-16k struggles on this task, which tends to answer questions relying on parametric knowledge (Table 3).

**CodeU** -- A code understanding dataset; it requires the LLM to infer the output of a lengthy Python program. Source code is mainly from Numpy, and a string processing codebase is constructed. To prevent LLMs from answering the question based on their parametric knowledge, original function names are replaced. LLMs should first locate where the function is called and determine which functions are invoked. CodeU is the most challenging task in L-Eval (Section B.6).

**LongFQA** -- The authors notice a lack of long context question answering datasets in the finance domain and annotate QA pairs based on public earning call transcripts from the Investor Relations section of 6 company websites (Section B.8).

## 3.2 Data Re-annotation from Public Datasets

[p. 3-4] Five publicly available datasets are re-annotated.

**GSM(16-shot)** is derived from 100-grade school math problems in the GSM8k dataset (Cobbe et al., 2021). If the LCLM maintains its reasoning ability on longer context, utilizing more high-quality examples will have a positive effect on solving math problems (Li et al., 2023b). 16 in-context examples with lengthy Chain-of-Thought are constructed, where 8 examples come from *chain-of-thought-hub* and 8 examples are constructed by the authors. With the newly constructed examples, the accuracy of Turbo-16k-0613 rises from 79 (8-shot) to 84 (16-shot).

New synthesis instructions are injected into **QuALITY** (Pang et al., 2022), such as *"What can we infer from the longest sentence in this story?"* and *"How many words are there in the story?"*. Given that these types of questions may rarely occur in real-world conversations, their proportion in L-Eval is extremely small. [p. 4]

The **Openreview** dataset contains papers collected from openreview.net. The model is asked to (1) write an Abstract section, (2) summarize the related work, and (3) finally give feedback including valuable suggestions and some questions for the authors. Papers with high-quality related work sections and helpful reviews written by human reviewers are selected to form this test set. [p. 4]

**SPACE** (Angelidis et al., 2021) is used to test the aspect-based review summarization task, with diverse instructions to prevent overfitting. [p. 4]

Previous work (Li et al., 2023a; Liu et al., 2023) has used retrieval tasks to test the ability of modeling long context dependency via retrieving something over lengthy context. L-Eval includes a popular first topic retrieval task **TopicRet** (Li et al., 2023a), formatted as: *"[topic-1] Chat History [instruction]"*. However, as can be seen from Figure 1, retrieving the first topic is too easy to distinguish the ability of different models. The task of retrieving the second and the third topics presents a significantly higher level of challenge. It is observed that nearly all open-source models struggle in task. So the task is enhanced with second/third topic retrieval. [p. 4]

**Figure 1** (p. 4): "Test Accuracy (%) of different models with retrieving the first topic and retrieving the second/third topic."
Bar chart showing accuracy (%) on the y-axis for different models on the x-axis. Two series are shown: "Second/Third Topic" and "First Topic". First topic retrieval accuracy is near 100% for most models (Claude-100k, Turbo-16k, Turbo-4k, ChatGLM2-6k, Llama2-13b-e, Vicuna-13b-16k, Longchat-13b-16k, Vicuna-7b-16k). Second/third topic retrieval accuracy is substantially lower, around 0-60% for most models, with Claude-100k and Turbo-16k performing best. This supports the claim that first topic retrieval is too easy and second/third topic retrieval is more discriminating.

## 3.3 Data Filtering and Correction

[p. 4] The remaining 12 tasks originate from existing datasets following previous evaluation suites (Zhang et al., 2023). However, L-Eval involves more human labor after data collection because the annotation quality of previous long sequence datasets fluctuates severely and there are many unanswerable questions that are unrelated to the context. These mistakes can hardly be corrected using the automatic preprocessing scripts in previous works. In L-Eval, all samples are manually filtered and corrected after data collection. Specifically, Claude-100k is used as an assistant to filter mistaken QAs and unanswerable questions. First, the lengthy document is input into Claude and it is requested to provide the answer and offer an explanation. If Claude produces an answer greatly mismatching the ground truth or states that the answer cannot be deduced from the context, re-annotation is performed or the sample is simply removed.

## 3.4 Statistics

[p. 4-5] The statistics of L-Eval are shown in Table 1. The L-Eval contains various question styles such as multiple choice questions (TOFEL (Tseng et al., 2016), QuALITY, Coursera), true or false questions (SFiction), math problems (GSM), code understanding (CodeU), goal-oriented dialogues (MultiDoc2Dial (Feng et al., 2021)), extractive QA (CUAD (Hendrycks et al., 2021b), NQ (Kwiatkowski et al., 2019)), abstractive QA (LongFQA, NarrativeQA (Kociisky et al., 2017), Qasper (Dasigi et al., 2021)), single document summarization (GovReport (Huang et al., 2021), BigPatent (Sharma et al., 2019), SummScreen (Chen et al., 2022), QMSum (Zhong et al., 2021)), multi-document summarization (Multi-News (Fabbri et al., 2019), SPACE (Angelidis et al., 2021)), research writing (Openreview) and so on.

The long documents in L-Eval span many domains such as law, finance, academic papers, lectures, lengthy conversations, news, famous Python codebase, long-form novels, and meetings. The average input length in L-Eval ranges from 4k to 60k. The maximum sample in L-Eval contains nearly 200k tokens. This diversity represents real-world scenarios where different tasks may require different lengths of context and instructions. The length of reference in L-Eval also varies significantly across tasks. [p. 4-5]

**Table 1** (p. 5): "This table presents the statistics of the L-Eval suite where **Question-style** indicates the type of task or the style of instruction in the dataset, **#Doc** refers to the number of long documents, and **#Instr** denotes the number of instructions provided for each long input. **Avg/Max len** signifies the average/maximum length of the document inputs. We tokenize the raw text with Llama2 tokenizer and report the number of tokens."

| Dataset | Question-style | Domain | Avg len | Max len | #Instr | #Doc |
|---|---|---|---|---|---|---|
| | | *Closed-Ended Tasks* | | | | |
| TOEFL | Multiple choice | English test | 3,907 | 4,171 | 269 | 15 |
| GSM(16-shot)^ | Solving math problems | In-context examples | 5,557 | 5,638 | 100 | 100 |
| QuALITY^ | Multiple choice | Gutenberg | 7,169 | 8,560 | 202 | 15 |
| Coursera* | Multiple choice | Advanced courses | 9,075 | 17,185 | 172 | 15 |
| TopicRet^ | Retrieving topics | Conversation | 12,506 | 15,916 | 150 | 50 |
| SFiction* | True or False Questions | Scientific fictions | 16,381 | 26,918 | 64 | 7 |
| CodeU* | Deducing program outputs | Python Codebase | 31,575 | 36,309 | 90 | 90 |
| | | *Open-Ended Tasks* | | | | |
| MultiDoc2Dial | Goal-oriented dialogues | Grounded documents | 3,905 | 7888 | 136 | 20 |
| Qasper | QA on papers | NLP papers | 5,019 | 6,547 | 160 | 20 |
| LongFQA* | QA on earning call | Finance | 6,032 | 7824 | 52 | 6 |
| NQ | QA from Google Search | Wikipedia | 23,698 | 47,726 | 104 | 20 |
| CUAD | Extracting key information | Law | 30,966 | 68,625 | 130 | 20 |
| NarrativeQA | QA on narratives | Gutenberg | 62,335 | 210,541 | 182 | 20 |
| Multi-News | Multi-doc Summarization | Multiple News articles | 7,320 | 19,278 | 11 | 11 |
| GovReport | Single-doc Summarization | Government reports | 7,495 | 27,128 | 13 | 13 |
| BigPatent | Single-doc Summarization | Lengthy patents | 7,718 | 12,867 | 13 | 13 |
| SummScreen | Transcripts Summarization | TV series transcripts | 10,688 | 14,544 | 13 | 13 |
| Openreview^ | Paper writing & reviewing | Papers from Openreview | 11,170 | 33,303 | 60 | 20 |
| QMSum | Query-based summarization | Meeting transcripts | 16,692 | 33,310 | 156 | 20 |
| SPACE^ | Aspect-based summarization | Reviews on Hotels | 19,978 | 22,158 | 120 | 20 |

Datasets marked with * are annotated from scratch. Datasets marked with ^ (dagger in the paper) are re-annotated from public datasets.
