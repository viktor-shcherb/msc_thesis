# B Data Collection and Annotation for L-Eval [p. 20–26]

[p. 20] In their pursuit of diverse, comprehensive, and relevant data, the authors sourced datasets from a wide array of platforms and sources. These datasets represent various facets of everyday life and specialized fields and present different challenges for LCLMs. They leveraged resources from previous open-source datasets, Coursera subtitles, earning call transcripts from corporate websites, GitHub, etc. The instruction styles in L-Eval include multiple-choice questions, school math with many examples, key topics retrieval from lengthy dialogues, text summarization, and abstractive question answering, encompassing a wide range of tasks.

## B.1 TOFEL (English Tests) [p. 20]

[p. 20] This dataset is sourced from the TOEFL Practice Online and the data is collected from TOEFL-QA (Tseng et al., 2016; Chung et al., 2018). All lectures from a single TPO have been consolidated into one lengthy lecture. After the consolidation, they select the top 15 longest lectures.

**Example 1:**
```
Input: <Multiple long lectures> \n\n
Question: why did Frantzen go to the sales barn
A. to study human form and movement
B. to earn money by painting portraits
C. to paint farm animals in an outdoor setting
D. to meet people who could model for her painting
\n\n Answer:
Ground truth: A
```

## B.2 GSM (16-shot) (Grade School Math) [p. 20]

[p. 20] This dataset is derived from 100-grade school math problems in the GSM8k dataset (Cobbe et al., 2021). Increasing the number of high-quality and complex examples usually has a positive effect on solving math problems. The authors construct 16 in-context examples with lengthy Chain-of-thought for this task where 8 examples come from *chain-of-thought-hub* (footnote 17: https://github.com/FranxYao/chain-of-thought-hub/blob/main/gsm8k/lib_prompt/prompt_hardest.txt) using the hardest prompt and the remaining 8 examples are constructed by the authors. They selected 8 questions from GSM8k based on their difficulty and annotated the solving process. Models with 2k or 4k context length face difficulties while encoding the 16 examples. They experiment with the newly constructed examples and it performs better than only encoding 8 examples. Concretely, the accuracy rises from 79 (8-shot) to 84 (16-shot) when using turbo-16k-0613 as the base model. [p. 20]

**Example 2:**
```
Input: <example 1> \n\n <example 2> \n\n ... <example n> \n\n
Question: Janet's ducks lay 16 eggs per day. She eats three for breakfast every
morning and bakes muffins for her friends every day with four. She sells the remainder
at the farmers' market daily for $2 per fresh duck egg. How much in dollars does she
make every day at the farmers' market? \n\n
Let's think step by step
Ground truth: 18
```

## B.3 QuALITY (Gutenberg) [p. 20–21]

[p. 20–21] This dataset is sourced from the multiple choice QA dataset QuALITY (Pang et al., 2022) which contains multiple-choice questions derived from the literature on Gutenberg. The authors filter 20 long stories and 202 questions and correct/delete questions with annotation errors. They found that most questions in QuALITY can be solved by extracting paragraphs from long texts. They further enhance some synthesis questions that need a global understanding of the document. Examples of the annotated synthesis questions are as follows: [p. 21]

1. *What can we infer from the longest sentence in the story?*
2. *The longest dialogue is spoken by whom?*
3. *Extract names mentioned in the longest sentence in the story.*
4. *How many words are there in the story?*
5. *How many sentences are there in the story?*

The reference source sentences are automatically located and the ground truth answers are manually annotated by the authors.

**Example 3:**
```
Input: <A long story>\n\n
Instruction: Why did Syme accept the mission with Tate?
(A) He needed a way back to Earth
(B) He felt he would collect a reward along the way
(C) He respected Tate
(D) He had no plan for his life, so he jumped on the adventure
Ground truth: (B) He felt he would collect a reward along the way
```

## B.4 Coursera (Advanced Lectures) [p. 21]

[p. 21] This dataset originates from the Coursera website (footnote 18: https://coursera.org/). The authors selected and completed 4 courses:

1. *Ask Questions to Make Data-Driven Decisions*
2. *Data Scientist's Toolbox*
3. *Process data from dirty to clean*
4. *Improving Deep Neural Networks: Hyperparameter Tuning, Regularization and Optimization*

The input long document is the subtitles of the videos and they merge courses in one week into one single long lecture. Questions and the ground truth answers are labeled by the authors. The instruction style of Coursera takes the format of multiple choice. In order to increase the difficulty of the task, they have set **multiple correct options**. Failure to select all correct choices will result in receiving only a quarter of the total points for that question. [p. 21]

**Example 4:**
```
Input: <A long lecture>\n\n
Question: When working with a new team, which of the following actions can help you to
adapt to different communication expectations? Select all that apply.
A. Ask questions when you are unsure of something
B. Learn the team's preferred communication style
C. Observe how teammates communicate with each other
D. Ignore the team's communication preferences and use your own style
\n\n Answer:
Ground truth: ABC
```

## B.5 SFiction (Scientific Fictions) [p. 21–22]

[p. 21–22] This sub-task is annotated to test the loyalty of the LCLM to the input context. LLMs have acquired many commonsense in their pertaining corpus known as parametric knowledge (Wang et al., 2023). However, the authors argue that in LCLMs, contextual knowledge is more crucial than parametric knowledge. In real-world applications, many long documents are private and can never be seen during pretraining. It may contain new knowledge or describe a new world which may be opposite to the pretraining knowledge. The language model should follow contextual knowledge instead of parametric knowledge. To simulate this scenario, they annotate a science fiction dataset consisting of True or False questions. The original works are sourced from SFGram (footnote 19: https://github.com/nschaetti/SFGram-dataset). They manually select documents that fit their experimental conditions and annotate them with questions and corresponding answers. Most of the answers to these questions contradict real-world principles and do not comply with actual physical laws, such as the statement: *Humans have invented the time machine*. As a result, open-source models have very serious hallucination problems which in turn help them acquire a high score on this dataset. So they also give the answer based on real-world knowledge, and the final accuracy is calculated by the average of loyalty and factuality. [p. 22]

**Example 5:**
```
Input: <A scientific fiction>\n\n
Question: We cannot get to the centre of the Earth, True or False? Answer this
question based on the world described in the document.
Ground truth: False

Question: We cannot get to the centre of the Earth, True or False? Answer this
question based on the real-world knowledge and facts up until your last training.
Ground truth: True
```

## B.6 CodeU (Python) [p. 22]

[p. 22] This dataset is used to test the capability of understanding long code. Given a lengthy code base, the model will call some functions defined in the codebase and the model should infer the final output of the program. They mainly use source code from Numpy (footnote 20: https://github.com/numpy/numpy). They also write a string processing codebase containing more than 100 functions that take a string as input such as extracting the email address from an input string. To prevent LLMs from answering the question based on their parametric knowledge, they replace the original function name defined in Numpy with `Op1`, `Op2`..., `OpN`. The Language Model (LLM) should first identify where the function is called and determine which functions are invoked, ultimately ascertaining the results of the operations. CodeU represents the most challenging task within L-Eval. Even the most potent model, GPT-4-32k, achieves an accuracy of only 25.55%. [p. 22]

**Example 6:**
```
Input: <The beginning of a lengthy Python program>
def Op1(): ...
def Op2(): ...
args = [4,5,6]
output = Op1(args)
print(output)
<The rest of the program>\n\n
Instruction: What is the output of this program? Please carefully read through these
code snippets and comments. You should first identify where the functions are defined
and then figure out what they do.
\n\n let's think step by step:
Ground truth: [1,2,3]
```

## B.7 TopicRet (Lengthy Conversation) [p. 22–23]

[p. 22–23] This dataset comes from the LongChat repository (Li et al., 2023a) (footnote 21: https://github.com/DachengLi1/LongChat), and its task style focuses on retrieving topics from extensive chat histories. Recent studies show that language models are good at retrieving information from the very beginning or end of its input context but are usually lost in the middle (Liu et al., 2023). To make the task more challenging, they enhance the original task by asking the model to extract **the second and the third** topic. [p. 22]

**Example 7:**
```
Input: <A long conversation > \n\n
Question: What is the second topic we discussed? Only give me the topic name. Do not
summarize yourself.
Ground truth: The future of space tourism
```

## B.8 LongFQA (Finance) [p. 23]

[p. 23] The authors find that there is a lack of long open-ended QA datasets in finance. The long context finance dataset is derived from earnings call transcripts obtained from the *Investor Relations* section of the company websites. They annotate 6 transcripts from 6 different incorporations: Lumentum, Oclaro (footnote 22: https://investor.lumentum.com/overview/default.aspx), Theragenics (footnote 23: https://www.sec.gov/Archives/edgar/data/), FS KKR Capital Corp (footnote 24: https://www.fskkradvisor.com/investor-relations/), LaSalle Incorporated (footnote 25: https://ir.jll.com/overview/default.aspx), Renewable Energy Group (footnote 26: https://www.regi.com/resources/press-releases) with 54 questions based on these transcripts. [p. 23]

**Example 8:**
```
Input: <A long document>\n\n
Instruction: You are asked to act as a member of the Financial Results Conference Call
and answer the question: What major actions has Greg Dougherty, the CEO of Oclaro,
highlighted as being undertaken by the company for its restructuring plan? \n Answer
this question with xx words.
Ground truth: Oclaro has been implementing a significant restructuring plan, which
includes closing our second major...
```

## B.9 CUAD (Law) [p. 23]

[p. 23] Questions on the Legal domain are drawn from the CUAD (Contract Understanding Atticus Dataset) dataset (Hendrycks et al., 2021b) designed for supporting NLP research for automating legal contract review. They manually filter 20 documents with annotated QA pairs from CUAD. [p. 23]

**Example 9:**
```
Input: <Legal contracts> \n\n
Instruction: Highlight the parts (if any) of this contract related to Expiration
DateThat should be reviewed by a lawyer. Details: On what date will the contract's
initial term expire? \n Answer this question with xx words.
Ground truth: The term of this Agreement shall commence on the Effective Date and
shall continue in full force and effect for an initial period of five (5) years.
```

## B.10 MultiDoc2Dial (Dialogues over Multi-Documents) [p. 23]

[p. 23] This dataset is sampled from the MultiDoc2Dial dataset (Feng et al., 2021) which aims to model goal-oriented dialogues grounded in multiple documents. It contains dialogues from 4 different domains: Finance, Travel, Entertainment, and Shopping. Each dialogue in the dataset is grounded in 2-5 relevant documents covering different topics within the domain. [p. 23]

**Example 10:**
```
Input: <Multiple long documents> \n\n
Instruction: How long will Driver's Ed courses be valid for? \n Answer this question
with xx words.
Ground truth: For roughly 1 one year. Maybe longer depending on the course.
```

## B.11 Natural Questions (Wikipedia) [p. 24]

[p. 24] They filter 20 wikipedia long documents from Natural Question (Kwiatkowski et al., 2019) on Google Research datasets. Questions can be answered with the same documents are merged, and duplicate questions are removed. [p. 24]

**Example 11:**
```
Input: <Documents from Wiki>\n\n
Instruction: when did season 2 of handmaid's tale start? \n Answer this question with
xx words.
Ground truth: April 25, 2018
```

## B.12 NarrativeQA (Narratives) [p. 24]

[p. 24] This dataset is collected from NarrativeQA (Kocisky et al., 2017) which has the longest document length in L-Eval. The original question-answering dataset was created using entire books from Project Gutenberg (footnote 27: https://www.gutenberg.org) and movie scripts from various websites. Summaries of the books and scripts were taken from Wikipedia and given to annotators. The authors' work focuses on correcting the annotation error; for example, there are some issues where the main character in the question does not even appear in the input document at all. [p. 24]

**Example 12:**
```
Input: <A long novel>\n\n
Instruction: Why did Mary pay off the debt for Ann's family? \n Answer this question
with xx words.
Ground truth: Mary was in love with Ann.
```

## B.13 Qasper (Papers) [p. 24]

[p. 24] This dataset is filtered from the Qasper dataset (Dasigi et al., 2021), which is a question-answering resource focused on NLP papers. The dataset was constructed using NLP papers that were extracted from the Semantic Scholar Open Research Corpus (S2ORC). After filtering, they remove the unanswerable questions and the extractive version answers. They also discovered instances where identical questions yielded contradictory answers. They addressed this issue by meticulously reviewing the paper and rectifying the incorrect responses. [p. 24]

**Example 13:**
```
Input: <A long paper>\n\n
Instruction: How did they obtain the dataset? \n Answer this question with xx words.
Ground truth: public resources where suspicious Twitter accounts were annotated, list
with another 32 Twitter accounts from BIBREF19 that are considered trustworthy.
```

## B.14 OpenReview (Papers) [p. 24–25]

[p. 24–25] This task aims to help researchers working on scientific papers by dealing with tasks like correcting grammar errors or typos and writing some sections. They include 3 tasks in the paper writing assistant task of L-Eval: 1) writing an Abstract section, (2) writing a Related Work section, and (3) finally giving a review of this paper including valuable suggestions and questions. Notably, they discourage reviewers from using large models for reviews. Their aim is to assist authors in further improving their papers. Therefore, they ask the model to give some valuable suggestions and raise some questions for authors. They filter 20 papers with well-written reviews for L-Eval. They use the processed PDF files from Yuan et al. (2021). [p. 24–25]

**Example 14:**
```
Input: <A long paper>\n\n
1. Instruction: Please generate the Abstract section for this paper. \n Answer this
question with xx words.
2. Instruction: Please summarize related work and you should include the following
works [a list of papers]. \n Answer this question with xx words.
3. Instruction: Please write a review for this paper and you should provide some
suggestions and raise some questions in your review. \n Answer this question with xx
words.
Ground truth: Conventional out-of-distribution (OOD) detection schemes based on
variational autoencoder or Random Network Distillation (RND) have been observed to
assign ...
```

## B.15 GovReport (Government Reports) [p. 25]

[p. 25] This dataset is filtered from the government report summarization dataset (Huang et al., 2021), the dataset consists of long reports written by U.S. government research agencies such as the Congressional Research Service and Government Accountability Office. The documents and summaries in this dataset are longer compared to other long document summarization datasets. They manually filter 13 documents with human-written summaries from the original dataset. [p. 25]

**Example 15:**
```
Input: <A government report>\n\n
Instruction: Please help me summarize this government report. \n Answer this question
with xx words.
Ground truth: The President of the United States has available certain powers that
may be exercised in the event that the nation is threatened by crisis, exigency, or
emergency circumstances...
```

## B.16 QMSum (Meetings) [p. 25]

[p. 25] This dataset sourced from the QMSum (Zhong et al., 2021), this dataset contains query-based meeting summarizations. Query-based summarization aims to summarize the document given a specific aspect. They selected 20 meeting transcripts accompanied by queries, specifically choosing those that could not be easily addressed through retrieval methods. [p. 25]

**Example 16:**
```
Input: <Meeting transcripts>\n\n
Instruction: What was agreed upon on sample transcripts? \n Answer this question with
xx words.
Ground truth: To save time, speaker mn005 will only mark the sample of transcribed
data for regions of overlapping speech, as opposed to marking all acoustic events...
```

## B.17 SPACE (Reviews) [p. 25–26]

[p. 25–26] The review (opinion) summarization aims to summarize the reviews from customs reviews on a restaurant or hotel. They obtain 20 samples from the validation and test set of SPACE (Angelidis et al., 2021) where human-written abstractive summaries are created for 50 hotels based on 100 input reviews each. SPACE consists of customer reviews of hotels from TripAdvisor, with 1.1 million training reviews for 11,000 hotels. The original task asks the model to summarize hotels from multiple aspects: food, location, cleanliness, etc. They construct the instructions for review summarization with GPT-4 and some examples. [p. 25–26]

**Example 17:**
```
Input: <Multiple reviews>\n\n
Instruction: Give a broad summary of guest impressions about Doubletree by Hilton
Seattle Airport. \n Answer this question with xx words.
Ground truth: The staff are friendly and exceptional. Every room (lobby included) was
very clean. They are spacious, very quiet, and come with a coffee maker...
```

## B.18 Multi-News (News) [p. 26]

[p. 26] This dataset is sourced from the Multi-News (Fabbri et al., 2019). The original Multi-News dataset contains news articles as well as human-written summaries of those articles, compiled from the website newser.com where each article consists of multiple short news articles. They select 10 articles for the L-Eval benchmark. [p. 26]

**Example 18:**
```
Input: <News articles>\n\n
Instruction: Please summarize these news articles. \n Answer this question with xx
words.
Ground turth: Why did Microsoft buy Nokia's phone business? We now know Microsoft's
answer: The computing giant released a 30-slide presentation today arguing that the
move will improve Microsoft...
```

## B.19 BigPatent (Patents) [p. 26]

[p. 26] This dataset is derived from the BigPatent (Sharma et al., 2019) project, which consists of 1.3 million records of U.S. patent documents along with human-written abstractive summaries. They select 13 patent patents from the original dataset. [p. 26]

**Example 19:**
```
Input: <A long patent>\n\n
Instruction: You are a patent examiner. Please write a summary of this patent. \n
Answer this question with xx words.
Ground truth: The invention provides a method and system for cleaning pet paws by
providing a bounded container containing...
```

## B.20 SummScreen (TV Show) [p. 26]

[p. 26] This dataset originates from the SummScreen (Chen et al., 2022), the original dataset is an abstractive summarization dataset combining TV series transcripts and episode recaps. SummScreen is constructed from fan-contributed websites. They use 13 of these transcripts in L-Eval. [p. 26]

**Example 20:**
```
Input: <TV series transcripts> \n\n
Instruction: Write a summary of the scene. \n Answer this question with xx words.
Ground turth: Feeling guilty over Phoebe missing out on London, the gang plans a
weekend trip to Atlantic City, but just as they are about to leave...
```
