# Ada-LEval [p. 4-5]

[p. 4] This section outlines the construction process of Ada-LEval, detailing both the collection methodology of source data and the building procedure of test cases. Table 1 demonstrates the data statistics of Ada-LEval.

## Task Definition [p. 4]

**TSort.** TSort provides LLMs with N shuffled text segments, extracted from contiguous chapters of a long book. The task for models is to sort these segments into their original sequence. A response is regarded accurate only if it precisely reinstates the segments' initial order. To simplify the challenge and minimize possible confusion, LLMs are supplied with adjacent paragraphs from before and after the specified chapters to serve as contextual hints.

**BestAnswer.** Each test case in BestAnswer contains one question and a large amount of possible answers to this question. The answer designated by the original inquirer is considered the most helpful answer, while LLMs are required to identify this optimal answer among all possible candidates.

## Source Data Collection [p. 4]

**TSort.** Initial data sourced from Booksum (Kryściński et al., 2021), a text summarization dataset derived from the Project Gutenberg, a public book repository consisting of over 60,000 free eBooks spanning various literary genres including novels, plays, short stories, and more. Genres like epistolary literature and poetry are excluded in the construction of the TSort benchmark due to their non-sequential nature. To prevent LLMs from exploiting superficial cues, they meticulously remove identifiers such as chapter numbers and annotations from the content.

**BestAnswer.** Constructed using threads from Stack Overflow, a platform renowned for its extensive range of programming-related questions and answers. Stack Overflow questions are categorized by multiple tags, indicating thematic similarity. To ensure quality and diversity, they choose 23 different tags, including javascript, python, C++, *etc.*, and collect top 2500 questions from each tag based on popularity.

## Test Case Building [p. 4-5]

For both tasks, test cases are constructed according to their token length (measured by GPT-4 tokenizer). Token lengths between 1,000 to 16,000 are regarded as **long-context** settings and text lengths exceeding 16,000 are regarded as **ultra-long-context** settings.

**TSort long-context settings:** Cases span test cases with 2k, 4k, 8k, and 16k tokens. For each length, the segment number N=4 and the length upper limit for each text segment and adjacent paragraphs before and after these contiguous chapters are fixed. Each text segment contains complete paragraphs (no paragraph is sliced in the middle). To build test cases with different contents, they set stride between beginning paragraphs of test cases during construction. After prepending the instructions, they further filter test cases that exceed the token upper bound.

**BestAnswer long-context settings:** Test cases with 1k, 2k, 4k, 6k, 8k, 12k, and 16k tokens. Test cases contain distractor answers under corresponding question and adaptable number of distractor answers from other similar questions under each length setting. To make evaluation results directly comparable across different length settings, the questions within the BestAnswer benchmark remain unchanged, regardless of the case length. The most helpful answer is defined as the answer explicitly accepted by the inquirer, adopted as the "groundtruth answer". For integrity reasons, they exclude all questions where the corresponding most helpful answer is not text-only.

[p. 5] When choosing the distractors, they only consider answers that are provided prior to the accepted answer under corresponding question. Besides, they incorporate answers from other questions with similar tags to the original question to serve as distractor answers.

**Ultra-long-context settings:** Under ultra-long-context settings, they build test cases with 32k, 64k, and 128k tokens for both tasks. The construction paradigm is similar to the long-context setting. For BestAnswer, since the number of similar questions and the corresponding answers are limited, they relax tag similarity constraints and allow answers of questions with less similar tags to serve as the distractor answers.

**Figure 1** (p. 1): "The demonstration of two tasks: **TSort** and **BestAnswer** introduced in Ada-LEval. Understanding and reasoning over the full text are required to solve these two tasks."
- Top panel (TSort Task): Shows a document being split into N text segments, then shuffled. The LLM is asked "What is the correct order of the segments? Answer with the list of segment indices." Example LLM Answer: "N, 1, N-1, ..., 2."
- Bottom panel (BestAnswer Task): Shows golden answer tagged by the question asker (A_g), intra-question distractors (A_ij), and inter-question distractors (A_ij from different questions under different tags like Python, Java, Linux, Ruby). The LLM is asked "Which is the best answer for Question Q_i?" with multiple choices, and the example LLM Answer is "A3."

**Table 1** (p. 4): The data statistics of TSort and BestAnswer. GPT-4 tokenizer CL100K used to calculate token numbers. A subset of all built cases used for evaluation.

| | | **TSort** | |
|---|---|---|---|
| Setting | Total #Cases Built | Max #Tokens | Avg #Tokens |
| 2k | 5123 | 2000 | 1816 |
| 4k | 5451 | 4000 | 3724 |
| 8k | 5324 | 8000 | 7663 |
| 16k | 4957 | 16000 | 15662 |
| 32k | 2206 | 32000 | 31226 |
| 64k | 1658 | 64000 | 62407 |
| 128k | 782 | 127800 | 121488 |

| | | **BestAnswer** | |
|---|---|---|---|
| Setting | Total #Cases Built | Max #Tokens | Avg #Tokens |
| 1k | 7526 | 1128 | 955 |
| 2k | 7526 | 2154 | 1983 |
| 4k | 7526 | 4215 | 3994 |
| 6k | 7526 | 6268 | 6012 |
| 8k | 7526 | 7790 | 7518 |
| 12k | 7526 | 12389 | 12091 |
| 16k | 7526 | 15964 | 15646 |
| 32k | 200 | 32974 | 32329 |
| 64k | 200 | 64216 | 63274 |
| 128k | 200 | 127059 | 126098 |
