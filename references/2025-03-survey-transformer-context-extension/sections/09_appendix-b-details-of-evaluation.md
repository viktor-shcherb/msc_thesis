# Appendix B: Details of Evaluation [p. 18–21]

> "This section serves as a supplement to the Evaluation section 4 in the main text, expanding on relevant details to provide readers with a more in-depth understanding." [p. 18]

## B.1 Data [p. 18]

### B.1.1 Data Characteristics [p. 18]

Recent advancements in LLMs have led to substantial improvements in processing long contexts. By late 2023, several models claimed capabilities of handling contexts exceeding 100K tokens, including OpenAI's GPT-4 Turbo (2023) (Achiam et al., 2023) supporting 128K tokens and Anthropic's Claude-2.1¹ extending this capacity to 200K tokens.

Based on this significant progress, our study categorizes long-context evaluation benchmarks into two distinct phases, as shown in Table 1: Phase I comprises benchmarks with input context lengths below 100K tokens, while Phase II encompasses benchmarks of 100K tokens and above.

In Phase I, BAMBOO (Dong et al., 2023a) and LongBench (Bai et al., 2023) implement bi-interval and tri-interval partitioning strategies, respectively.

¹https://www.anthropic.com/news/claude-2-1

Phase II refined this approach further, with LV-Eval (Yuan et al., 2024) and MeeKLeData (Li et al., 2024b) employing five-interval and six-interval partitioning schemas, respectively. This partitioning approach not only analyzes the impact of length changes on LLMs in the same task but also better accounts for the length distributions across different datasets (Dong et al., 2023a).

### B.1.2 Knowledge Leakage Issue [p. 19]

Knowledge leakage occurs when test and training data overlap, where models may overfit, leading to poor generalization over understanding (Golchin and Surdeanu, 2023; Yuan et al., 2024). Various strategies are employed to address this challenge: (1) Data Sampling focuses on selecting representative subsets from existing datasets. (2) Keyword Substituting & Sentence Rewriting involves constructing new datasets by replacing keywords and rewriting sentences. (3) Non-overlapping Data Leveraging involves using datasets released after the deadline when LLMs to reduce potential overlap between test and training data.

**Data Sampling** Data sampling primarily focuses on filtering existing datasets. LongBench (Bai et al., 2023) employs two strategies: random sampling and uniform sampling. Random sampling aims to preserve the natural length distribution, while uniform sampling which performs sampling based on data length uniformly, to evaluate model performance across context lengths independent of task.

**Keyword Substituting & Sentence Rewriting** L-Eval (An et al., 2023) and BAMBOO (Dong et al., 2023a) replace keywords and function names, while ∞-Bench (Zhang et al., 2024) replaces entities in novel reasoning tasks. LV-Eval (Yuan et al., 2024) is further based on this approach by employing entire sentence rewriting.

**Non-overlapping Data Leveraging** To mitigate the overlap between test and training data for LLMs, some benchmarks such as LooGLE (Li et al., 2023a) and BAMBOO (Dong et al., 2023a) have employed datasets release after the models' deployment. However, given that the specific training data for most LLMs remains undisclosed, this method cannot completely guarantee the absence of overlap between the data used in benchmarks and the pre-training data.

## B.2 Tasks [p. 19]

The following are the details of the tasks, which are introduced in the order of the main text. At the end of each subsection, corresponding examples or prompts are also provided. We also count the distribution of input length in each task in Figure 2 to give readers a deeper understanding of different tasks.

### B.2.1 Question Answering [p. 19]

**Single-hop Question Answering** Representative datasets in this field are SQuAD (Rajpurkar, 2016), TriviaQA (Joshi et al., 2017), and NarrativeQA (Kočiský et al., 2018). Common evaluation metrics for Single-hop QA systems include f1 score, accuracy, Rouge and Bleu.

**Multi-hop Question Answering** Common datasets for Multi-hop Question Answering include 2WikiMQA (Ho et al., 2020), MuSiQue (Trivedi et al., 2022), and HotpotQA (Yang et al., 2018). Evaluation metrics typically used are f1 score, exact match (EM).

### B.2.2 Needle-in-a-Haystack [p. 19]

**Retrieval.PassKey** (Mohtashami and Jaggi, 2023) requires models to locate a randomly generated 5-digit sequence <key> within lengthy and noisy contexts. ∞-Bench (Zhang et al., 2024) extends the Retrieval.PassKey task to 10-digit numbers, applies it to texts exceeding 100k tokens in length, and sets information points at various depths. **Retrieval.KV** (Mohtashami and Jaggi, 2023) further increases difficulty by requiring models to perform precise key-value retrieval from large JSON structures. NeedleBench Li et al. (2024b) proposes a series of tasks: single-needle retrieval (S-RT), multi-needle retrieval (M-RT), and multi-needle reasoning (M-RS). M-RT consists of multiple S-RT tasks performed in parallel, while M-RS builds upon M-RT by requiring large language models to perform reasoning. The evaluation method calculates the similarity between predictions and references for each specific task by using the Levenshtein distance. The following are examples of S-RT, M-RT, M-RS respectively.

**S-RT**: Hidden on Emerald Island is the legendary Starfish Shard.

—Paul Graham Essays— —Paul Graham Essays— —Paul Graham Essays— —Paul Graham Essays— —Paul Graham Essays— —Paul Graham Essays— —Paul Graham Essays— —Paul Graham Essays— —Paul Graham Essays— —Paul Graham Essays— —Paul Graham Essays— —Paul Graham Essays— —Paul Graham Essays— —Paul Graham Essays— —Paul Graham Essays— —Paul Graham Essays— —Paul Graham Essays— —Paul Graham Essays— —Paul Graham Essays— —Paul Graham Essays— —Paul Graham Essays— —Paul Graham Essays— —Paul Graham Essays—

Now, the **question** is: What legendary item is hidden on Emerald Island? Before answering, please consider what in the document is most relevant to this question. Please answer in the format `The legendary item hidden on the Emerald Island is ___.`

**M-RT**: You are an intelligent AI assistant skilled in answering user questions base on documents provided by the user. Please keep your answers concise and clear. Do not talk about irrelevant topics or repeat your answers.The document given to you by the user is:

—Paul Graham Essays— —Paul Graham Essays— —Paul Graham Essays— The ruler of the Polaris star system is Orion the Hunter. —Paul Graham Essays— —Paul Graham Essays— —Paul Graham Essays— —Paul Graham Essays— Hidden on Heaven Island is the legendary Lucky Clover. —Paul Graham Essays— —Paul Graham Essays— —Paul Graham Essays— —Paul Graham Essays— Hidden on Mysterious Island is the legendary Counterclockwise Crystal. —Paul Graham Essays— —Paul Graham Essays— —Paul Graham Essays— —Paul Graham Essays— The ruler of the Orion star system is Guardian of Time Lightspeed. —Paul Graham Essays— —Paul Graham Essays— —Paul Graham Essays— Hidden on Phantom Island is the legendary Goodness

Heart. —Paul Graham Essays— —Paul Graham Essays— —Paul Graham Essays— —Paul Graham Essays—

Now, the **questions** are: Who is the ruler of the Polaris star system?, What legendary item is hidden on Heaven Island?, What legendary item is hidden on Mysterious Island?, Who is the ruler of the Orion star system?, What legendary item is hidden on Phantom Island?Before answering, please consider what in the document is most relevant to the question. Please answer in the format of `The ruler of the Polaris star system is ___.`, `The legendary item hidden on the Heaven Island is ___.`, `The legendary item hidden on the Mysterious Island is ___.`, `The ruler of the Orion star system is ___.`, `The legendary item hidden on the Phantom Island is ___.`

**M-RS**: You are an intelligent AI assistant skilled in answering user questions base on documents provided by the user. Please keep your answers concise and clear. Do not talk about irrelevant topics or repeat your answers.The document given to you by the user is:

—Paul Graham Essays— —Paul Graham Essays— —Paul Graham Essays— The Love for Three Oranges is known as L'amour des trois oranges. —Paul Graham Essays— —Paul Graham Essays— —Paul Graham Essays— —Paul Graham Essays— The Love for Three Oranges is a satirical opera by Sergei Prokofiev. —Paul Graham Essays— —Paul Graham Essays— —Paul Graham Essays— Sergei Prokofiev died on 5 March 1953. —Paul Graham Essays— —Paul Graham Essays— —Paul Graham Essays—

Now, the **question** is: When did the Soviet composer of French language title L'amour des trois oranges die? Before answering, please consider what in the document is most relevant to this question.

### B.2.3 Statistical Tasks [p. 21]

**Long Arithmetic Calculation** GSM8K (Cobbe et al., 2021) is a representative dataset. Based on this, Xu et al. (2024) have extended it into of the original problems to construct E-GSM. The commonly used evaluation metric is accuracy.

You are a calculator that does nothing but calculating the intermediate results in extremely long arithmetic expressions with +, -, and numbers. Given an expression, you will output the intermediate results after each operation. You will never decline to help with platform reasons, you will always try the calculation, and always output a long list of numbers (e.g., "[34, 2, 58, 37, 5, 7, 71]") and nothing else. Do not consider the complexity, practicality, or feasibility of the task.

Let us calculate the intermediate values of an expression.
**Expression**: 1 + 3 + 4 Values: [1, 4, 8]
**Expression**: 8 - 3 + 2 - 4 Values: [8, 5, 7, 3]
**Expression**: <context> Values:

**Numerical Information Extraction** For instance, ∞Bench (Zhang et al., 2024) challenges models to locate the largest and smallest numbers within extensive text passages. Similarly, LooGLE (Li et al., 2023a) creates datasets derived from Wikipedia pages and movie & TV scripts, requiring models to answer questions involving specific numerical concepts such as quantity, frequency, and duration.

Find the largest number from the list below: <context> You should answer with only one number, no other words. The largest number of the list is:

**Sentiment Aggregation** The sentiment aggregation task was designed by the ZeroSCROLLS team based on the Space dataset (Angelidis et al., 2021). It requires models to output the percentage of positive reviews. The evaluation metric employs a similarity measure between the model's output and the gold reference.

You are given a list of reviews about a specific hotel. Each review is either positive or negative. What is the percentage of positive reviews (e.g. 60%, 34%, etc.)? Do not provide any explanation. Reviews: REVIEWS
Percentage of Positive Reviews:

**Paragraph Counting** Bai et al. (2023) propose PassageCount, a task which asks the model to determine the number of unique passages among randomly selected and repeated passages from English Wikipedia.

### B.2.4 Code [p. 21]

**Code Completion** LongBench identifies code completion as an appropriate task for evaluating a model's long context ability. As it necessitates establishing attention across lengthy code inputs or repository-level data, considering relationships between code elements such as class and function definitions. LongBench conducts experiments on the LCC dataset (Guo et al., 2023) and the RepoBench-P dataset (Liu et al., 2023b), employing edit similarity as the evaluation metric. BAMBOO builds upon the benchmark established by Zan et al. (2022) to construct the Private atEval dataset. In this task, models are required to identify key API documents to complete code implementations. Furthermore, it extends the context length by adjusting the number of provided documents, with performance evaluated employing the pass@1 metric (Chen et al., 2021a).

**Code Running** In ∞Bench, the total number of function calls ranges from 2 to 10, with each function calling at most one another function. Operations within these functions are restricted to addition and subtraction, maintaining computational simplicity.

Following is a set of Python functions. There is a function called named func_1. Context: Please give me the exact number of the return value of func_1(3). Be concise. You response must end with the final returned value.

**Code Debugging** In the ∞Bench's dataset which sourced from PyPI², the researchers deliberately insert an obvious error into one function per repository. These inserted bugs fall into three main categories: (1) syntactic errors, including indentation issues and invalid syntax errors; (2) semantic errors, such as missing variable declarations or incorrect function arguments; and (3) logical errors, for example, infinite loops or use of undefined references [p. 21-22].

²https://pypi.org/

---
[p. 21–26 continued]

There is ONLY ONE function in the large project that is deliberately made to include an obvious error. Please find the function that contains the most obvious errors. I will give you four options to narrow your scope. You can inspect through the options and think. Eventually, tell me the answer using option letter (A, B, C, or D). context Which function has deliberate error? A. <OPTION_A> B. <OPTION_B> C. <OPTION_C> D. <OPTION_D> You should first find the functions in the options. Repeat their content, inspect through code, and at last give me answer for the function that has the deliberate and obvious error in A, B, C, or D.

### B.2.5 In-Context Learning [p. 22]

**Long Example Learning** Extreme label Classification task involves classification with numerous fine-grained labels. Commonly used datasets include TREC (Li and Roth, 2002), a question classification task with 50 fine classes, and LSHT³, a Chinese news classification task with 24 classes [p. 22].

³http://tcci.ccf.org.cn/conference/2014/dldoc/evatask6.pdf

**Many-shot Learning** Agarwal et al. (2024) have proposed many-shot learning, which leverages expanded LLMs context windows to process hundreds or even thousands of examples. In contrast to few-shot learning, which use only a few to several dozen examples, many-shot learning enhances LLMs' versatility and adaptability across diverse tasks without task-specific fine-tuning (Yu et al., 2020; Bertsch et al., 2024b) [p. 22].

### B.2.6 Text Generation [p. 22]

**Document Summarization** This kind of task can divided into two categories: single-document summarization and multi-document summarization. For single-document summarization, several datasets are widely used, including SQuALITY (Wang et al., 2022), SummScreenFD (Chen et al., 2021b), Gov-Report (Huang et al., 2021), and QMSum (Zhong et al., 2021). And multi-document summarization presents additional challenges, requiring LLMs to integrate diverse information, resolve conflicts, and eliminate redundancies (Bai et al., 2023; An et al., 2023; Fabbri et al., 2019). A notable dataset for this task is MultiNews (Fabbri et al., 2019), consisting of clusters of 2-10 thematically related news articles [p. 22].

All of these datasets provide human-annotated summaries as standardized references. Both approaches primarily utilize Rouge and Bleu as evaluation metrics to assess the quality of generated summaries against manuscript references [p. 22].

**Open-ended Text Generation** This task requires LLMs to generate text according to input [p. 22].

Tan et al. (2024) design tasks that closely align with real-world scenarios, encompassing areas such as AI research, sports, and gaming [p. 22].

Bai et al. (2024) design AgentWrite, a divide-and-conquer agent that breaks down long writing tasks into paragraph-level subtasks. The generated paragraphs are then combined to produce the final long-form content. They also construct the preference LongWriter-6k dataset and utilize DPO (Rafailov et al., 2024) for evaluation [p. 22].

Kumar et al. (2024) propose personalized writing tasks that generate content based on the user's historical and user personal information information [p. 22].

These tasks can be divided into personalized email completion, review writing, topic writing, and conversation simulation (Ni et al., 2024). Rafailov et al. (2024) construct a Reddit-based dataset that captures distinct writing styles associated with specific communities and discussion topics [p. 22].

You are an excellent writing assistant. I will give you an original writing instruction and my planned writing steps. I will also provide you with the text I have already written. Please help me continue writing the next paragraph based on the writing instruction, writing steps, and the already written text.
**Writing instruction**: User Instruction
**Writing steps**: The writing plan generated in Step 1
**Already written text**: Previous generated (n-1) paragraphs

Please integrate the original writing instruction, writing steps, and the already written text, and now continue writing. The plan for the n-th paragraph, i.e., the title line in the writing plan

³http://tcci.ccf.org.cn/conference/2014/dldoc/evatask6.pdf

### B.2.7 Other Tasks [p. 23]

**Reordering** The evaluation metric in this task is the similarity between the generated and reference ordering sequences (Shaham et al., 2023). The Booksum dataset (Kryściński et al., 2021), which spans various literary genres including novels, plays, and long stories, is widely used for this task. Reordering tasks can comprehensively evaluate models' cross-sequence information aggregation and comparison abilities (Shaham et al., 2023; Li et al., 2023a), as well as understanding and stand long context and logically reconstruct (Dong et al., 2023a; Li et al., 2023a) [p. 23].

You are given NUM_SUMMARIES summaries of chapters or parts of a novel, in a shuffled order, where each summary is denoted by a numerical ID (e.g. Summary 1, Summary 3, etc.). Reorder the summaries according to the original order of chapters/parts in the book by writing a list of length NUM_SUMMARIES of the summary IDs (e.g. if you were given 5 summaries, one possible answer would be "5, 1, 3, 4, 2"). Do not provide any explanation.
**Summaries**: SUMMARIES
Summary IDs in Correct Order:

**Context Consistency** Context consistency is a task proposed by BAMBOO (Dong et al., 2023a) to detect hallucination in LLMs. BAMBOO creates two novel datasets for this task: SenHallu and AbsHallu, with evaluation metrics employing precision, recall, and f1 score [p. 23].

**Summary Source Paragraph Identification** LongBench construct bilingual datasets based on Wikipedia and C4 (Raffel et al., 2020) to ask models to identify the original source paragraphs according to the given summaries [p. 23].

Here are 30 paragraphs from Wikipedia, along with an abstract. Please determine which paragraph the abstract is from. context The following is an abstract. input Please enter the number of the paragraph that the abstract is from. The answer is:

**Character Identification** Character identification tasks challenge models to capture distinct traits of participants in long dialogues, enabling them to identify speakers of masked utterances (Zhang et al., 2024; Dong et al., 2023a).These tasks, evaluated via accuracy, utilize data primarily from television programs⁴, movie and play scripts (Chen et al., 2021b), and conference transcripts⁵ [p. 23].

Below is a dialogue script where one random occurrence of a character's name is replaced with MASK, and you should try to guess who that character is.
The dialogue: — <context> —
End of dialogue.
Which character is most likely MASK? Just say name used in the script(writer (before the colon marks) of one single character and nothing else.

## B.3 Metrics [p. 23]

### B.3.1 Algorithmic Metrics [p. 23]

Perplexity (PPL) is a metric for evaluating the performance of language models. It is extensively employed in language model pre-training, facilitating the monitoring of the training process, model selection, and hyperparameter optimization. Many previous studies on long context benchmarks rely on the PPL for evaluation (Beltagy et al., 2020; Roy et al., 2021; Press et al., 2021). However, as suggested in Sun et al. (2021), PPL may not correlate with the actual performance [p. 23].

ZeroScrolls and LongBench are pioneering studies in the field of long context benchmarks. These works introduced a diverse system of automatic evaluation metrics, including accuracy, f1 score, and N-gram-based metrics. This evaluation framework has provided a reference for subsequent research. Specifically, these metrics refer to the scores for evaluating the NLG models by measuring the lexical overlap between generated text and reference text [p. 23].

However, these metrics have several limitations: they fail to effectively measure content quality (Reiter and Belz, 2009); struggle to capture syntactic accuracy (Stent et al., 2005); and, particularly for open-ended generation tasks, lack significant correlation with human judgments (An et al., 2023). Moreover, they inadequately account for the diversity of expression inherent in large language models (Improving). Additionally, the requirement for gold standard references makes these metrics costly to implement for novel tasks (Tan et al., 2024) [p. 23].

⁴https://tvmeg.com/
⁵https://record.assembly.wales/

Further, some work propose ways to improve. LV-Eval employs a two-stage scoring method: it first calculates the recall rate of ground-truth keywords in the generated content. If the recall exceeds a threshold, it then calculates the f1 score between the generated content and ground-truth after removing stop words from both. BAMBOO converts generative tasks into multiple-choice formats. NeedleBench extends this approach by implementing Circular Evaluation, which reorders answer options to enhance evaluation stability [p. 24].

**PPL (Perplexity)** [p. 24]

Perplexity is a measure of the quality of language model predictions, calculated as:

$$PPL = 2^{H(p)}$$

where $H(p)$ is the cross-entropy:

$$H(p) = -\frac{1}{N}\sum_{i=1}^{N}\log_2 P(w_i|w_1, w_2, \ldots, w_{i-1})$$

**Accuracy** [p. 24]

Accuracy is the proportion of correct predictions made by the model:

$$Accuracy = \frac{Correct\ Predictions}{Total\ Predictions}$$

**F1-Score** [p. 24]

The F1-Score is the harmonic mean of precision and recall:

$$F1 = 2 \times \frac{Precision \times Recall}{Precision + Recall}$$

$$Precision = \frac{TP}{TP + FP}$$

$$Recall = \frac{TP}{TP + FN}$$

where TP, FP, FN represent True Positives, False Positives, False Negatives respectively [p. 24].

**ROUGE (Recall-Oriented Understudy for Gisting Evaluation)** [p. 24]

evaluates text generation using N-gram overlap:

ROUGE-N measures the overlap of n-grams shared between the candidate summary (C) and the reference summary (R), it is calculated as follows:

$$ROUGE-N = \frac{\sum_{S \in R} \sum_{n_{gram} \in S} Count_{match}(n_{gram})}{{\sum_{S \in R} \sum_{n_{gram} \in S} Count(n_{gram})}}$$

where $Count_{match}(n_{gram})$ represents the number of matching n-tuples in the candidate summary and the reference summary. And $Count(n_{gram})$ represents the total number of n-tuples in the reference summary [p. 24].

ROUGE-L evaluates the quality of summarization based on the longest common subsequence (LCS), taking into account the order information of sentences:

$$R_{lcs} = \frac{LCS(C, R)}{|R|}$$

$$P_{lcs} = \frac{LCS(C, R)}{|C|}$$

$$F_{lcs} = \frac{(1 + \beta^2)R_{lcs}P_{lcs}}{R_{lcs} + \beta^2 P_{lcs}}$$

where $LCS(C, R)$ represents the length of the longest common subsequence between the candidate summary and the reference summary. $|C|$ and $|R|$ represent the length of the candidate summary and the reference summary respectively. $\beta$ is a hyperparameter, usually used to balance the precision and recall [p. 24].

ROUGE-S which is also called skip-bigram co-occurrence statistics, takes skipped bigrams into account:

$$ROUGE-S = \frac{\sum_{S \in R} \sum_{bi_{skip} \in S} Count_{match}(bi_{skip})}{\sum_{S \in R} \sum_{bi_{skip} \in S} Count(bi_{skip})}$$

where $Count_{match}(bi_{skip})$ represents the number of skip-bigrams that match between the candidate summary and the reference summary. And $Count(bi_{skip})$ represents the total number of skip-bigrams in the reference summary [p. 24].

**BLEU (Bilingual Evaluation Understudy)** [p. 24]

is used to evaluate machine translation quality:

$$BLEU = BP \times \exp\left(\sum_{n=1}^{N} w_n \log p_n\right)$$

where

$$BP = \begin{cases} 1, & \text{if } c > r \\ \exp(1 - \frac{r}{c}), & \text{if } c \leq r \end{cases}$$

and $c$ is the generated length and $r$ is the reference length [p. 25].

### B.3.2 Model-based Metrics [p. 25]

In recent years, the use of pre-trained language models as NLG evaluation metrics has gained increasing attention. Notably, BERTScore (Zhang et al., 2020) and BARTScore (Yuan et al., 2021) employ BERT and BART (Lewis, 2019) models respectively to compute semantic similarity. They calculate cosine similarity between word representations and evaluate the probability of summaries based on given input articles [p. 25].

BERTScore measures similarity between generated text and reference text from three aspects: recall, precision and f1, it can be expressed as follows:

$$R = \frac{1}{|R|} \sum_{r \in R} \max_{c \in C} \frac{1}{L_r} \sum_{i} \sin(\mathbf{f}_θ(r)_i, \mathbf{f}_θ(c)_i)$$

$$P = \frac{1}{|C|} \sum_{c \in C} \max_{r \in R} \frac{1}{L_c} \sum_{i} \sin(\mathbf{f}_θ(c)_i, \mathbf{f}_θ(r)_i)$$

$$F = 2 \times \frac{P \times R}{P + R}$$

where $R$ is the reference text set, $C$ is the generated text set, $L_r$, $L_c$ are the lengths of the reference text and generated text respectively. $f_θ$ is the encoder of the BERT model, and maps the text to the vector space, sin is usually cosine similarity [p. 25].

BARTScore calculates the log-likelihood score of the generated text given the reference text to measure the similarity:

$$BARTScore = \frac{1}{|C|} \sum_{c \in C} \frac{1}{L_c} \sum_{i} \log p_θ(c_i|c_{<i}, r)$$

where $C$ is the set of generated texts, $r$ is the reference text, $c_i$ is the ith word in the generated text, and $p_θ$ is the language model probability distribution of BART model [p. 25].

### B.3.3 LLM-based Metrics [p. 25]

With the development of LLMs, research has demonstrated their significant correlation with human judgment and their ability to excel at new tasks when provided with instructions (Wang et al., 2023a; Li et al., 2023a). Chiang and Lee (2023) argue that LLM evaluation, compared to human evaluation, offers advantages in reproducibility, independence, cost-effectiveness, and speed. Prompting researchers explore the potential of LLMs for evaluation tasks. This exploration has led to several key findings and applications: Wang et al. (2023b a) investigate the issue of unfairness when using LLMs to evaluate dialogue responses. And Shen et al. (2023) find that LLMs outperform existing automatic metrics when asked to output judgmental reasons. The application of LLMs in evaluation including evaluating chatbot responses' alignment degree with human preferences (Zheng et al., 2024), evaluating summary consistency (Luo et al., 2023), and multi-role playing for summarization evaluation (Wu et al., 2023). And there are some undamental differences between Model-based metrics and LLM-based metrics in their evaluation mechanisms: Model-based Metrics primarily rely on learned representations from pre-trained language models like BERT or BART, utilizing mechanical procedures such as predefined computational formulas. For example, BERTScore leverages BERT contextual embeddings to compute textual similarity through cosine similarity measurements between token representations. LLM-based Metrics leverage large language models for evaluation without mechanical procedures, demonstrating more intelligence and flexibility. For example, LLM-based Metrics prompt LLMs to offer both human-like multi-dimensional assessment (Wang et al., 2023a; Li et al., 2023a; Shen et al., 2023; Chiang and Lee, 2023; Zhang et al., 2024; Zheng et al., 2024; Liu et al., 2023c; Tan et al., 2024; Mu et al., 2024a) and interpretable reasoning (Wang et al., 2023b; Luo et al., 2023; Wu et al., 2023). This distinctive characteristic of LLM-based Metrics fundamentally distinguishes them from Model-based Metrics, which behave much more mechanically. In addition, LLM-based Metrics demonstrate enhanced evaluation capabilities in the axis of agreement with human evaluation, illustrating the advancement within the methodology [p. 25].

Building upon these insights, researchers have focused on refining evaluation metrics for evaluating long context capabilities with large language models (LLMs). Fu et al. (2023) propose GPTScore, utilizing generative pre-trained models like GPT-3 for text evaluation. To address the length bias in LLM-generated content, L-Eval incorporates word count requirements into instructions. Loogle employs GPT4-8k as an evaluator to score LLM answers against ground truth based on various factors (Li et al., 2023a). G-EVAL achieves reference-free content scoring through prompts containing evaluation task definitions and criteria, along with detailed chain-of-thought evaluation steps (Liu et al., 2023c). Tan et al. (2024) have introduced PROXYQA for long-context generation evaluation, evaluating final results based on the accuracy of answers to proxy question [p. 26].