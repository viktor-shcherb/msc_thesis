# 2 Multi-Document Question Answering [p. 3-6]

The goal is to better understand how language models use their input context. To this end, the authors analyze model performance on multi-document question answering, which requires models to find relevant information within an input context and use it to answer the question. The authors make controlled changes to the length of the input context and the position of the relevant information and measure changes in task performance. [p. 3]

## 2.1 Experimental Setup [p. 3-4]

In the multi-document question answering task, the model inputs are (i) a question to answer and (ii) *k* documents (e.g., passages from Wikipedia), where *exactly one* of the documents contains the answer to the question and *k - 1* "distractor" documents do not. This task requires the model to access the document that contains the answer within its input context and use it to answer the question. Figure 2 presents an example. [p. 3]

The task is instantiated with data from NaturalQuestions-Open (Lee et al., 2019; Kwiatkowski et al., 2019), which contains historical queries issued to the Google search engine, coupled with human-annotated answers extracted from Wikipedia. The authors take the 2655 queries where the annotated long answer is a paragraph (as opposed to a list or a table). Passages (chunks of at most 100 tokens) from Wikipedia are used as documents within the input contexts. For each of the queries, a document that contains the answer and *k - 1* distractor documents that do not contain the answer are needed. To obtain a document that answers the question, the Wikipedia paragraph that contains the answer from the NaturalQuestions annotations is used. [p. 3]

To collect *k - 1* distractor documents that do not contain the answer, a retrieval system (Contriever, fine-tuned on MS-MARCO; Izacard et al., 2021) is used to retrieve the *k - 1* Wikipedia chunks that are most relevant to the query and do not contain any of the NaturalQuestions-annotated answers.^{2,3} In the input context, the distractor documents are presented in order of decreasing relevance.^4 [p. 3]

To modulate the position of relevant information within the input context, the order of the documents is adjusted to change the position of the document that contains the answer (Figure 3). To modulate the input context length, the number of retrieved documents that do not contain the answer is increased or decreased (Figure 4). [p. 3-4]

Following Kandpal et al. (2022) and Mallen et al. (2023), accuracy is used as the primary evaluation metric, judging whether any of the correct answers (as taken from the NaturalQuestions annotations) appear in the predicted output. [p. 4]

^2 Ambiguity in NaturalQuestions-Open means that a small number of distractor passages may contain a reasonable answer. Additional experiments on a subset of unambiguous questions were run, finding similar results and conclusions; see Appendix A. [p. 3]

^3 Random documents as distractors were also explored, see Appendix B for more details. [p. 3]

^4 Since there might be a prior over "search results" appearing in ranked order, randomly ordering the *k - 1* distractor documents and mentioning that the documents are randomly ordered in the task description was explored, but the same trends were found. See Appendix C for more details. [p. 3]

The experimental setup is similar to the needle-in-a-haystack experiments of Ivgi et al. (2023), who compare question answering performance when the relevant paragraph is placed (i) at the beginning of the input or (ii) a random position within the input. They find that encoder-decoder models have significantly higher performance when relevant information is placed at the start of the input context. In contrast, the present study examines finer-grained changes in the position of relevant information. [p. 4]

**Figure 2** (p. 4): "Example of the multi-document question answering task, with an input context and the desired model answer. The document containing the answer is bolded within the input context here for clarity."

The figure shows an input context with a prompt asking to write a high-quality answer for a given question using only the provided search results. Three documents are shown: Document [1] (Title: Asian Americans in science and technology), Document [2] (Title: List of Nobel laureates in Physics) which is bolded as it contains the answer, and Document [3] (Title: Scientist). The question is "who got the first nobel prize in physics" and the desired answer is "Wilhelm Conrad Rontgen."

**Figure 3** (p. 4): "Modulating the position of relevant information within the input context for the multi-document question answering example presented in Figure 2. Re-ordering the documents in the input context does not affect the desired output."

Two side-by-side examples showing the same question with documents reordered. In the left example, Document [1] (Title: List of Nobel laureates in Physics) is bolded as the answer-containing document (first position, 3 total documents). In the right example, Document [2] (Title: List of Nobel laureates in Physics) is bolded as the answer-containing document (second position out of five documents). The desired answer remains "Wilhelm Conrad Rontgen" in both cases.

**Figure 4** (p. 4): "Modulating the input context length of the multi-document question answering example presented in Figure 2. Adding documents that do not contain the answer increases the length of the input context, but does not affect the desired output."

Shows a version with 5 documents (vs. 3 in Figure 2), where the answer-containing document is Document [2]. Additional distractor documents (Document [4]: Norwegian Americans, Document [5]: Maria Goeppert Mayer) are added. The desired answer is still "Wilhelm Conrad Rontgen."

## 2.2 Models [p. 4-5]

Several state-of-the-art open and closed language models are analyzed. Greedy decoding is used when generating outputs; exploration of other decoding methods is left to future work. A standard set of prompts for each model is used (Figure 2). [p. 4]

**Open models.** [p. 4-5]
- **MPT-30B-Instruct:** Maximum context length of 8192 tokens. Initially pre-trained on 1 trillion tokens using 2048-token sequences, followed by an additional sequence length adaptation pre-training phase on 50 billion tokens using 8192-token sequences. Uses ALiBi (Press et al., 2022) to represent positional information.
- **LongChat-13B (16K)** (Li et al., 2023): Extends the LLaMA-13B (Touvron et al., 2023a) context window from 2048 to 16384 tokens by using condensed rotary positional embeddings before fine-tuning with 16384-token sequences.

**Closed models.** [p. 5]
- **GPT-3.5-Turbo:** Maximum context length of 4K tokens. (0613 OpenAI model version.)^5
- **GPT-3.5-Turbo (16K):** Extended maximum context length of 16K tokens. (0613 OpenAI model version.)^5
- **Claude-1.3:** Maximum context length of 8K tokens. Evaluated with the Anthropic API.
- **Claude-1.3 (100K):** Extended context length of 100K tokens. Evaluated with the Anthropic API.

^5 The 0613 OpenAI model versions were used. [p. 5]

^6 GPT-4 (8K) was also evaluated on a subset of multi-document QA experiments, finding similar results and trends as other models (though GPT-4 has higher absolute performance). Evaluating GPT-4 on the full multi-document QA and key-value retrieval experiments would cost upwards of $6000. See Appendix D for GPT-4 results and discussion. [p. 5]

## 2.3 Results and Discussion [p. 5-6]

Experiments use input contexts containing 10, 20, and 30 total documents. Figure 5 presents multi-document question answering performance when varying the position of relevant information within the input context. The authors also evaluate on the closed-book and oracle settings (Table 1). In the closed-book setting, models are not given any documents in their input context, and must rely on their parametric memory to generate the correct answer. In the oracle setting, language models are given the single document that contains the answer and must use it to answer the question. [p. 5]

**Table 1** (p. 5): Closed-book and oracle accuracy of language models on the multi-document question answering task.

| Model | Closed-Book | Oracle |
|---|---|---|
| LongChat-13B (16K) | 35.0% | 83.4% |
| MPT-30B-Instruct | 31.5% | 81.9% |
| GPT-3.5-Turbo | 56.1% | 88.3% |
| GPT-3.5-Turbo (16K) | 56.0% | 88.6% |
| Claude-1.3 | 48.3% | 76.1% |
| Claude-1.3 (100K) | 48.2% | 76.4% |

**Figure 1** (p. 1): "Changing the location of relevant information (in this case, the position of the passage that answers an input question) within the language model's input context results in a U-shaped performance curve -- models are better at using relevant information that occurs at the very beginning (primacy bias) or end of its input context (recency bias), and performance degrades significantly when models must access and use information located in the middle of its input context."

The figure shows accuracy (y-axis, ranging from approximately 55% to 75%) vs. position of document with the answer (x-axis, 1st to 20th) for GPT-3.5-Turbo-0613 with 20 total retrieved documents (~4K tokens). The solid line shows the U-shaped curve: performance starts at ~75% when the answer is in the 1st document, drops to ~55% around the 10th position, then rises back to ~60-65% at the 20th position. A dashed red line at ~56% shows the closed-book baseline performance of GPT-3.5-Turbo-0613.

**Figure 5** (p. 5): "The effect of changing the position of relevant information (document containing the answer) on multi-document question answering performance. Lower positions are closer to the start of the input context. Performance is highest when relevant information occurs at the very start or end of the context, and rapidly degrades when models must reason over information in the middle of their input context."

Three panels showing results for 10, 20, and 30 total retrieved documents (~2K, ~4K, ~6K tokens respectively). Each panel plots accuracy (y-axis, ~50-75%) vs. position of document with the answer (x-axis). Six models are shown: claude-1.3, claude-1.3-100k, gpt-3.5-turbo-0613, gpt-3.5-turbo-16k-0613, mpt-30b-instruct, and longchat-13b-16k. All models exhibit the U-shaped pattern across all document counts.

### Model performance is highest when relevant information occurs at the beginning or end of its input context [p. 5]

As illustrated in Figure 5, changing the position of relevant information in the input leads to substantial decreases in model performance. A distinctive U-shaped performance curve is observed -- models are often much better at using relevant information that occurs at the very beginning (primacy bias) and very end of contexts (recency bias), and suffer degraded performance when forced to use information within the middle of its input context. For example, GPT-3.5-Turbo's multi-document QA performance can drop by more than 20% -- in the worst case, performance in 20- and 30-document settings is lower than performance without *any* input documents (i.e., closed-book performance; 56.1%). These results indicate that current models cannot effectively reason over their entire context window when prompted for downstream tasks. [p. 5]

### Extended-context models are not necessarily better at using input context [p. 5-6]

When the input context fits in the context window of both a model and its extended-context counterpart, performance between them is nearly identical. For example, the 10- and 20-document settings both fit in the context window of GPT-3.5-Turbo and GPT-3.5-Turbo (16K), and their performance as a function of position of relative information is nearly superimposed (solid purple and dashed brown series in Figure 5). These results indicate that extended-context models are not necessarily better than their non-extended counterparts at using their input context. [p. 5-6]
