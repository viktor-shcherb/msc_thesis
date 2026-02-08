# 3 The ZeroSCROLLS Benchmark [p. 2–5]

[p. 2] ZeroSCROLLS is a zero-shot benchmark containing test sets of ten natural language tasks, each one requiring reasoning over a different type of long text. To ensure affordability, every task is limited to a maximum of 500 examples.

## 3.1 Tasks

The benchmark includes ten datasets: six adapted from Shaham et al. (2022) and four new tasks. Table 1 provides an overview. [p. 2]

**Table 1** (p. 3): "An overview of the data statistics in ZeroSCROLLS. *QB-Summ* means query-based summarization, *MC-QA* abbreviates multiple-choice question answering. *ES* refers to exponential similarity index. SpaceDigest data is from on the Space dataset (Angelidis et al., 2021) and BookSumSort data is from the BookSum dataset (Kryscinski et al., 2022)."

| Dataset | Task | Domain | Metric | Avg #Words | #Examples |
|---|---|---|---|---|---|
| GovReport (Huang et al., 2021) | Summarization | Government | ROUGE | 7,273 | 500 |
| SummScreenFD (Chen et al., 2022) | Summarization | TV | ROUGE | 5,663 | 337 |
| QMSum (Zhong et al., 2021) | QB-Summ | Meetings | ROUGE | 10,839 | 281 |
| SQuALITY (Wang et al., 2022) | QB-Summ | Literature | ROUGE | 4,971 | 260 |
| Qasper (Dasigi et al., 2021) | QA | Science | F1 | 3,531 | 500 |
| NarrativeQA (Kociský et al., 2018) | QA | Literature, Film | F1 | 49,384 | 500 |
| QuALITY (Pang et al., 2022) | MC-QA | Literature, Misc | Accuracy | 4,248 | 500 |
| MuSiQue (Trivedi et al., 2022) | QA | Wikipedia | F1 | 1,749 | 500 |
| SpaceDigest (New) | Aggregation | Reviews | ES | 5,481 | 500 |
| BookSumSort (New) | Aggregation | Literature | C_idx | 6,840 | 500 |

### 3.1.1 Summarization

[p. 2–3] The benchmark adopts three summarization datasets from SCROLLS (GovReport, SummScreenFD, and QMSum), and adds a fourth (SQuALITY). GovReport and SummScreenFD are full-document summarization tasks, while QMSum and SQuALITY are query-focused.

**GovReport** (Huang et al., 2021) contains long reports by the Congressional Research Service and the U.S. Government Accountability Offices, with their expert written summaries. [p. 2]

**SummScreenFD** (Chen et al., 2022) contains episode scripts from TV shows with community contributed recaps that were collected from Wikipedia and TVMaze as their summaries. [p. 3]

**QMSum** (Zhong et al., 2021) is a query-based summarization dataset over meetings transcripts. It contains academic meetings, industrial product meetings, and Welsh and Canadian parliament transcripts. Alongside the meeting transcript, each instance contains a query, which aims to focus the summary on a particular topic. [p. 3]

**SQuALITY** (Wang et al., 2022) is a question-focused summarization dataset, where given a story from Project Gutenberg, the task is to produce a summary of the story or aspects of it based on a guiding question. The questions and summaries are original and crowdsourced; experienced writers were told to design questions that require reading significant parts of the story to answer correctly. [p. 3]

### 3.1.2 Question Answering

[p. 3] The benchmark adopts three question answering datasets from SCROLLS (Qasper, NarrativeQA, and QuALITY), and adds MuSiQue, which focuses on multi-hop question answering.

**Qasper** (Dasigi et al., 2021) contains NLP papers from the Semantic Scholar Open Research Corpus (S2ORC) (Lo et al., 2020). NLP practitioners provided questions based on the abstracts, and another set of practitioners answered given the articles. [p. 3]

**NarrativeQA** (Kociský et al., 2018) contains questions and answers over books from Project Gutenberg and movie scripts from various websites. To create questions, annotators were provided summaries of the books and movies from Wikipedia, and each question was answered by one or more annotators. [p. 3]

**QuALITY** (Pang et al., 2022) contains stories and articles from Project Gutenberg, the Open American National Corpus, and more. Each instance contains a story and a multiple choice question; question writers were guided to write questions that require reading large portions of the story to answer correctly. [p. 3]

**MuSiQue** (Trivedi et al., 2022) is a multi-hop question answering dataset, where the inputs are 20 Wikipedia paragraphs and a question that requires multiple hops between different paragraphs. In the original dataset, each question also has an unanswerable twin question, where the correct answer is not present in the paragraphs. The authors randomly sample 100 unanswerable and 400 answerable questions for ZeroSCROLLS. [p. 3]

### 3.1.3 Aggregation

[p. 3–4] The authors create two new tasks that, by construction, require contextualizing and aggregating information from different parts of the input. Despite the inherent complexity required to solve these tasks, evaluation is designed to be simple and accurate.

**SpaceDigest** is a new sentiment aggregation task. Given 50 hotel reviews (without their ratings) from the Space dataset (Angelidis et al., 2021), the task is to determine the percentage of positive reviews. One example (50 reviews) is created per hotel from the 500 most rated hotels in the original dataset, keeping only strictly positive (rating 5 or 4) or negative (rating 2 or 1) reviews, discarding ones with an ambivalent rating of 3. [p. 3–4]

[p. 4] To verify that humans perform this task well, the authors gave 5 human annotators a shortened version of the examples (containing 10 reviews per example) and asked them to write the percentage of positive reviews. Each annotator was assigned 10 examples (100 reviews per annotator, 500 overall). The annotators aggregated their individual predictions perfectly, and had a total of 8 single-review classification errors out of the 500 reviews seen (~98.4% accuracy). [p. 4]

**BookSumSort** is a new task based on the BookSum dataset (Kryscinski et al., 2022), which contains summaries of chapters (or parts) of novels, plays, and long poems from various sources. Given a shuffled list of chapter summaries, the task is to reorder them according to the original order of summaries in BookSum. The task is created by manually selecting the summaries of 125 books from BookSum, retaining only high-quality instances. Each summary is manually edited to remove introductions, prefaces, overviews, and so forth, as well as any other information that may indicate the exact position of a summary; for example, > "Chapter 8 begins with Jane describing..." is replaced with "This Chapter begins with Jane describing..." and "As the play opens, Hippolytus announces..." becomes "Hippolytus announces...". [p. 4]

Each list of summaries contains between 3 and 86 chapter summaries, with a median of 15 and an average of 18.8 chapters per instance. 4 random permutations of each list are selected to create 500 instances. [p. 4]

## 3.2 Prompting

[p. 4] ZeroSCROLLS tests the ability to reason over long texts without any explicit training examples (zero-shot). Each data instance is complemented with an instruction that defines both the task and the desired output format (Efrat and Levy, 2020), without in-context demonstrations. The authors invest effort in designing the canonical prompts for ZeroSCROLLS, but the benchmark is open to further zero-shot prompt engineering (Radford et al., 2019; Schick and Schütze, 2021a,b), such as prompts that encourage chain-of-thought reasoning (Wei et al., 2022b). Table 5 contains the prompts for the summarization tasks and Table 6 contains prompts for question answering and aggregation tasks. [p. 4]

**Prompt Structure** [p. 4] Figure 3 illustrates an example from the benchmark. A prompt is manually crafted for each dataset, following a generic template composed of *instruction*, *context*, *query*, and *response*. The instruction describes the task and ends with the desired output format (e.g. "Answer the query in one or more sentences." for QMSum). When the total input size is too long for a model's context window, the context is trimmed and a string is appended explicitly stating that the rest of the context is trimmed, to inform the model that it cannot see the entire context. The context is then concatenated with a header describing what kind of context it is, e.g. "Report:", "Reviews:", etc. For tasks that have queries, the query is appended with an appropriate header. The prompt ends with a header indicating the response type (e.g. "Answer:" or "Summary:"). [p. 4–5]

**Accommodations for ChatBots** [p. 5] Chat LLMs, such as ChatGPT and Claude, are designed to interact with humans through a chat interface. The authors adapt their canonical prompts to accommodate these models. Specifically, they omit the response header (e.g. "Summary:" or "Answer:") as it is clear, in dialogue, that the input sequence has ended. They also append "Do not provide any explanation." to the instructions of question answering and aggregation tasks. For Claude, they wrap each prompt with "Human:" and "Assistant:" dialogue indicators, and for question answering and aggregation tasks also add the instruction to "please highlight your final answer with <{response_type}></{response_type}> tags" -- as recommended by Anthropic's documentation. [p. 5]

**Figure 3** (p. 4): "An example input in ZeroSCROLLS, taken from the QMSum dataset. The meeting transcript and the question are in *black*, and the ZeroSCROLLS prompt is in *blue*. In *copper* is a string we append to the trimmed context when the model's context window is too short to contain the entire input."

The figure shows a prompt structure with: instruction ("You are given a meeting transcript and a query containing a question or instruction. Answer the query in one or more sentences."), followed by "Transcript:" header with meeting content between User Interface and Industrial Designer participants, a note "[The rest of the transcript is omitted]", then "Query:" with the question "What did the group discuss about production costs of the product?", and finally "Answer:" as the response header.

## 3.3 Automatic Evaluation

[p. 5] ZeroSCROLLS evaluation is fully automatic. Given a model's response to every test instance, per-task automatic evaluation metrics are applied. These are then averaged across tasks to produce the model's ZeroSCROLLS score. For existing datasets, the authors follow Shaham et al. (2022) and use the metrics provided by each dataset's authors. For the newly proposed tasks (SpaceDigest and BookSumSort), two new automatic metrics are used.

**ROUGE** *(GovReport, SummScreenFD, QMSum, SQuALITY)* ROUGE (Lin, 2004) measures ngram overlap between generated and reference summaries. For each instance, ROUGE-1, ROUGE-2, and ROUGE-L are combined into a single score by computing their geometric mean. For SQuALITY, where there are multiple references, the maximal value of each ROUGE type is taken before computing the geometric mean. [p. 5]

**F1** *(Qasper, NarrativeQA, MuSiQue)* F1 computes unigram overlap between generated and reference answers, after normalizing white-spaces, lowercasing, omitting stopwords and punctuation (Rajpurkar et al., 2016), and transliterating any Unicode text to ASCII characters. For Qasper and NarrativeQA, where there are multiple reference answers, the maximal F1 score per instance is taken. [p. 5]

**Accuracy** *(QuALITY)* For multiple choice questions, the predicted letter (A, B, C, or D) is compared to the reference. The first valid option letter surrounded by word boundaries is used. [p. 5]

**Exponential Similarity** *(SpaceDigest)* Assuming that the output is a percentage, the exponential similarity between the gold reference percentage *p* and the predicted scalar p-hat is computed:

$$ES(p, \hat{p}) = d^{-c \cdot |p - \hat{p}|}$$

where *d* = 2 and *c* = 10, which means that, intuitively, the score gets cut by half for every 10 point deviation from the correct answer. If the output is not a percentage, the score is 0%. The first appearance of a percentage is parsed; e.g. for the output "Out of 50 reviews, 20 are positive and 30 are negative, so 40% of the reviews are positive 60% are negative." 40% is automatically parsed as the answer. [p. 5]

**Concordance Index** *(BookSumSort)* Assuming that the output is a permutation of the given chapter summary IDs, the amount of summary pairs that are in the right order is measured, divided by the total number of pairs C(n,2). The average random permutation scores 50% on this metric. If the output is not a permutation, the score is 0%. All characters except digits, commas, and white-spaces are discarded from the output string to eliminate any prefixes such as "Order:". [p. 5]
