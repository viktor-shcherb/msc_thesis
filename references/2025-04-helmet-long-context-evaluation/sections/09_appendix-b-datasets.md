# Appendix B: Datasets [p. 31]

## B.1 Retrieval-Augmented Generation [p. 31]

**Natural Questions (NQ)** [p. 31]
Natural Questions (NQ; Kwiatkowski et al., 2019) is a large-scale dataset for open-domain question answering featuring real user queries [p. 31].

**TriviaQA (TQA)** [p. 31]
TriviaQA (TQA; Joshi et al., 2017) comprises trivia questions and their corresponding answers [p. 31].

**HotpotQA** [p. 31]
HotpotQA (Yang et al., 2018) contains questions that require multi-passage reasoning [p. 31].

The authors source these datasets from KILT (Petroni et al., 2021), which provides annotations linking each query to its corresponding gold passages containing the answer [p. 31].

**PopQA** [p. 31]
PopQA (Mallen et al., 2023) consists of questions about long-tail entities [p. 31]. To minimize the impact of pre-training memorization, the authors filter the dataset to include only subject entities with popularity scores below 1000 [p. 31]. Since gold passages are not available for PopQA, they classify retrieved passages as positive or negative by checking for the presence of the ground truth answer [p. 31].

Notably, the authors populate the context with hard negative passages, retrieved from the same corpus as the positive passages using a real retriever [p. 31]. This approach presents a significantly greater challenge than using randomly sampled passages [p. 31]. This design choice better reflects real-world retrieval-augmented generation tasks, where models must effectively distinguish between relevant and irrelevant information [p. 31-32].

## B.2 Generation with Citations [p. 32]

Generation with citations represents a crucial task for enhancing language model trustworthiness and verifiability (Bohnet et al., 2022; Gao et al., 2023; Asai et al., 2024b) [p. 32]. The authors employ ALCE to assess models' capability to generate properly cited text [p. 32]. Following the original methodology, they utilize Wikipedia as the retrieval corpus and GTR (Ni et al., 2022) as the retriever [p. 32]. They omit MAUVE-based fluency evaluation since models typically generate fluent text, and in cases where they don't, the other metrics already approach zero [p. 32]. Instead, they focus on correctness and citation quality, reporting their average [p. 32].

## B.3 Passage Re-ranking [p. 32]

The authors evaluate models' passage re-ranking capabilities (Sun et al., 2023) using the MS MARCO passage ranking dataset (Bajaj et al., 2018) [p. 32]. Their evaluation uses annotated datasets from the TREC Passage Re-ranking challenge (Craswell et al., 2020) [p. 32]. Each dataset instance consists of a query and a list of passages with associated relevance scores [p. 32]. The dataset combines Bing user queries with passages retrieved via BM25 from web pages [p. 32]. Passages are labeled as perfect, highly relevant, or not relevant [p. 32]. For each input length L, they determine the maximum number of passages k that can be included [p. 32]. To eliminate positional bias, they balance the label distribution and randomize passage order [p. 32]. They create three different permutations of the k passages for each input length [p. 32]. The final performance metric is reported in NDCG@10 [p. 32]. While higher values of k are possible for NDCG evaluation, the computational cost of generating numerous passage IDs during inference leads them to maintain NDCG@10 as their metric [p. 32].

## B.4 In-context Learning [p. 32]

For in-context learning, the authors implement a label mapping strategy that compels models to utilize in-context examples rather than relying on prior knowledge for classification tasks [p. 32]. Each label is randomly mapped to an integer ℓ ∈ {0, 1, . . . , n − 1}, where n represents the number of unique labels in the dataset, following established practices (Dai et al., 2023) [p. 32]. They replace all label texts with their corresponding integer mappings throughout the dataset [p. 32]. Following Li et al. (2024c), they organize examples into demonstration rounds, placing all round containing examples in randomized order [p. 32]. The input is constructed by concatenating these demonstration rounds until reaching the target input length L [p. 32]. Unlike other task categories where they evaluate 100 samples, for ICL datasets they evaluate 500 samples [p. 32]. They balance the label distribution among the evaluation set [p. 32].

## B.5 Synthetic Tasks [p. 32-33]

For RULER tasks, the authors generate data using the original authors' scripts (Hsieh et al., 2024), employing the Llama-2 tokenizer (Touvron et al., 2023) to standardize input text across all models [p. 32]. The RULER suite comprises the following tasks [p. 32]:

**NIAH Single (three variants):** [p. 32]
- NIAH (variant 2): Most similar to the original NIAH (Kamradt, 2024) [p. 32]
- NIAH Single Repeat (variant 1): Uses repeated phrases instead of Paul Graham essays as context [p. 32]
- NIAH Single UUID (variant 3): Similar to variant 2 but uses UUIDs as retrieval values [p. 32]

**NIAH MultiKey (MK, three variants):** [p. 32]
- NIAH MK Essay (variant 1): Involves retrieving one gold key among three irrelevant keys, using Paul Graham Essays as context [p. 32]
- NIAH MK Needle (variant 2): Uses needle-based context structure [p. 32]
- NIAH MK UUID (variant 3): Similar to variant 2 but employs UUIDs as retrieval values for all needles [p. 32]

**NIAH MultiValue (MV):** Requires retrieving four different numbers associated with a single key from irrelevant essay context [p. 33]

**NIAH MultiQuery (MQ):** Involves retrieving correct values for four distinct keys from irrelevant essay context [p. 33]

**Variable Tracking (VT):** Requires tracking variable values through sequential operations [p. 33]

**Word Extraction Tasks:** [p. 33]
- Common word extraction (CWE) [p. 33]
- Frequent word extraction (FWE) [p. 33]
- Both tasks require identifying the most frequently occurring words [p. 33]

**Question Answering Tasks:** [p. 33]
- SQuAD (variant 1; Rajpurkar et al., 2016) [p. 33]
- HotpotQA (variant 2; Yang et al., 2018) [p. 33]
- Notable distinction: Their implementation uses retrieved passages rather than random samples, making the task more realistic and challenging [p. 33]

For comprehensive details, please refer to the original paper (Hsieh et al., 2024) [p. 33].

For JSON KV tasks, the authors generate a JSON dictionary containing randomly generated UUIDs as both keys and values, similar to Liu et al. (2023) [p. 33]. For each dictionary, they construct six queries, asking the model to retrieve the value for each key at six evenly spaced positions within the context [p. 33].

## B.6 Model-based Evaluation [p. 33-34]

Automatic evaluation metrics, such as ROUGE, are known to be unreliable and uncorrelated with human judgments (Goyal et al., 2023; Chang et al., 2024a) [p. 33]. However, existing long-context benchmarks still largely rely on these metrics (Bai et al., 2024; Zhang et al., 2024b) [p. 33]. In this work, the authors seek to more reliably evaluate language models at long context by employing LLMs as judges, inspired by previous works (Zheng et al., 2023) [p. 33]. For all model-based evaluations, they use GPT-4o-2024-05-13 as the judge [p. 33].

**Long-document question answering** [p. 33]

For NarrativeQA, the authors found that the models can often output answers that are correct but have little textual overlap with the ground truth answers in preliminary experiments, resulting in lower-than-expected performance [p. 33]. This is often due to the long lengths of the ground truth answers, which gives more possibilities of how to write it than a simple named entity that is often the case of other QA datasets [p. 33].

Therefore, they employ an LLM to judge if the model output is fluent and semantically similar to the ground truth [p. 33]. Given the question, the ground truth answer, and the model-generated output, they ask the LLM to judge if (1) the model output is fluent and (2) the generated output is correct and relevant to the question with the ground truth as a reference [p. 33]. The detailed prompts, precise definitions, and instructions are found in Table 10 [p. 33].

**Table 10:** Model-based evaluation prompt for long-document question answering [p. 35].

```
Please act as an impartial judge and evaluate the quality of the
provided answer which attempts to answer the provided question based on
a provided context. Although you are given the context, you will be
given a set of correct answers that achieves full scores on all metrics,
and you need to assess the provided answers using the correct answers.

Below is your grading rubric:

Fluency: - Score 0 (incoherent, repetitive, or incomplete): Incoherent
sentences, repetitive sentences (even if not by exact words), incomplete
answers, or gibberish. Note that even if the answer is coherent, if it
is repetitive or incomplete, it should be given a score of 0. Score 1
(coherent, non-repetitive answer): Coherent, non-repetitive, fluent,
grammatically correct answers.

Correctness: - Score 0 (Incorrect): The answer does not agree with the
provided correct answers at all. - Score 1 (partly correct): Partly
agree with one of the provided correct answers (for example, the
question asks for a date and a person; the answer gets the date right
but the person wrong). - Score 2 (correct, but not fully relevant):
Fully agrees with one of the provided correct answers but mentions other
completely irrelevant information. Note that extra information provided in
the answer, even if not mentioned in the correct answers, should NOT be
seen as irrelevant as long as they are relevant to the question to a
reasonable extend. - Score 3 (correct and relevant): Fully agrees with
one of the provided correct answers and only provides information
relevant to the question. Note that if the answer is longer than the
correct answer, as long as it is relevant to the question in the answer to a
question, it should still be given score 3. For example, if the correct
answer is ''the North Pole'' and the answer is ''They are headed for the
North Pole'', it should still be given a score of 3.

Now, read the following question, answer, and correct answers. First
think step-by-step and provide your reasoning and assessment on the
answer. Then output your score in the following json format:
{[''fluency'': 0, ''correctness'': 1]}.

Question: {question}
Correct answers: {correct_answers}
Answer: {parsed_output}
```

In Table 14, they also find that model evaluation can be useful in catching extremely cases [p. 33]. For example, Claude scores low in terms of F1 due to its tendency to output extra, assistant-like text, which is penalized by the n-gram overlap metric, and appears to be worse than the much smaller Llama-3.2-3B-Inst model [p. 33]. However, the model-based evaluation is able to catch this issue, and Claude scores higher than Llama-3.2-3B-Inst, which users might have expected given the model sizes [p. 33].

**Summarization** [p. 33-34]

At a high level, they ask the model to check for three properties: fluency, precision, and recall [p. 34]. Fluency can take on a value of either 0 (incoherent, incomplete, and/or repetitive) or 1 (fluent and coherent) [p. 34]. Precision is the percentage of model-generated sentences that are supported by the gold summary (they use the long summary from Multi-LexSum here) [p. 34]. Recall is the percentage of the key points that are supported by the model-generated output [p. 34]. They calculate the F1 score from precision and recall and multiply it with the fluency score for the final score [p. 34].

They first ask the model to generate a list of key points or atomic claims from the gold summary, following previous works that show that LLMs can accurately decompose long texts (Kamoi et al., 2023; Gao et al., 2023) [p. 34]. They manually checked 105 claims originating from 25 Multi-LexSum summaries and found that the claims were all factually correct [p. 34]. Although they found one out of 25 instances where the model missed a possible piece of information from the summary, they found that GPT-4o is almost always reliable for the decomposition task [p. 34]. For Multi-LexSum, they use the short summary to obtain the key point as the annotation contains both a long and a short summary [p. 34]. These key points are then saved for Multi-LexSum and ∞BENCH Sum [p. 34].

They show the detailed prompts for the summarization tasks in Table 11, 12, and 13, which are modeled after previous works (Kamoi et al., 2024; Chang et al., 2024; Kim et al., 2024) [p. 34]. These previous works have shown that LLMs can effectively judge model outputs (Zheng et al., 2023), but they conduct human analysis to further verify with their metric [p. 34].

**Table 11:** Model-based evaluation prompt for summarization fluency score [p. 36].

```
Please act as an impartial judge and evaluate the fluency of the
provided text. The text should be coherent, non-repetitive, fluent, and
grammatically correct.

Below is your grading rubric: - Score 0 (incoherent, repetitive, or
incomplete): Incoherent sentences, repetitive sentences (even if not by
exact words), incomplete answers, or gibberish. Note that even if the
answer is coherent, if it is repetitive or incomplete, it should be
given a score of 0. - Examples: - ''Summary: The Plaintiff the the the the
the the the the the the the the the the the the the the the the Repetitive:
''Summary: The U.S. government brought a criminal case against four
defendants. Summary: The U.S. government brought a criminal case
against four defendants. Summary: The U.S. government brought a criminal case
against four defendants. Summary: The U.S. government brought a
criminal case against four defendants.''

- Score 1 (coherent, non-repetitive answer): Coherent, non-repetitive,
fluent, grammatically correct answers. If the text is coherent,
non-repetitive, and fluent, but the last sentence is truncated, it
should still be given a score of 1. - Examples: - ''This case is about
an apprenticeship test that had disparate impact on Black
apprenticeship applicants. The Equal Employment Opportunity Commission
(EEOC) filed this lawsuit in December 17, 2004, in the U.S. District Court
for the Southern District of Ohio.'' - ''The plaintiffs sought
declaratory and injunctive relief, as well as attorneys' fees and costs,
under the Americans with Disabilities Act, the Rehabilitation Act of
1973, the Social Security Act, and the Ohio Nursing Home Reform Act. The
case was certified as a class action on behalf of all Medicaid-eligible
adults with disabilities in Cook County, Illinois, who are living, or may
in the future be, unnecessarily confined to nursing facilities and with
appropriate supports and services may be able to live in a community
setting. The defendants denied the allegations and argued that the
plaintiffs' claims were not typical of the class and that the class
definition was too broad. The case is ongoing, with discovery and
expert testimony scheduled for the fall of''

Now, read the provided text, and evaluate the fluency using the rubric.
Then output your score in the following json format: {[''fluency'':
1]}.

Text: ''{text}''
```

From qualitative analysis, they found that the model is consistently able to distinguish between fluent and non-fluent outputs, where they agree with the model judgments 100% of the time for randomly sampled Multi-LexSum and ∞BENCH Sum summaries [p. 34]. They then check if the GPT-4o judgments for precision and recall agree with human judgments [p. 34]. To this end, they sample 10 generated summaries for Multi-LexSum and ∞BENCH Sum each (five from Gemini and five from Llama-3.1-8B-Inst) and check five key point evaluations for each summary [p. 34]. They follow a similar procedure where they check if the model output supports the key point [p. 34]. They find a Cohen's κ = 0.76 for ∞BENCH Sum and κ = 0.72 for Multi-LexSum, suggesting substantial agreement [p. 34]. For precision, they conduct a similar human evaluation, and found a κ = 0.91 for ∞BENCH Sum and κ = 0.83 for Multi-LexSum, suggesting near-perfect agreement [p. 34].

Inspecting the disagreements, they find that that most of them arise from the partially supported cases [p. 34]. For instance, the key point may contain small details, such as the names of government departments or Court Justices' names, that are not explicitly mentioned in the generated summary, and the model judge is typically more lenient while humans are more strict [p. 34]. However, this is also subjective to the preference of the human [p. 34].

Qualitatively, they find that model-based evaluation can catch cases where the model is overly repetitive and scores high ROUGE-L score as a result, such as for Mistral-7B-Inst-v0.3 on ∞BENCH Sum [p. 34]. For instance, the Mistral model may generate an output consisted of the sentence "The author's object is to show that the study of grammar is necessary part of education" repeated for hundreds of times [p. 34]. This summary would receive an ROUGE-L score of 12.3 while the GPT-4o judge would penalize the model for being overly repetitive and incoherent and assign the output a final score of 0.0 [p. 34]. Thus, their GPT-4o judge penalizes the model for being overly repetitive, and the final metric reflects this issue [p. 34].
