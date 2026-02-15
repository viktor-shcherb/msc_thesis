# 3 Experiments [p. 3-4]

## 3.1 Datasets [p. 3]

To evaluate language models on the "Lost in the Middle" problem in the multi-hop setting, we utilize existing Multi-hop Question Answering datasets (Table 1). These datasets allow us to systematically position documents containing relevant information at various locations within the context, interspersed with distractor documents, to analyze how positional biases affect model performance.

| Dataset | Hops | Questions |
|---------|------|-----------|
| HotpotQA | 2 | 3703 |
| 2WikiMultihopQA¹ | 2, 4 | 6288 |
| MuSiQue-Ans | 2, 3, 4 | 1209 |

**Table 1** (p. 3): "Multi-hop datasets we use to evaluate the Lost in the Middle problem. We use the 2nd half of the validation sets due to private test set labels."

¹As 2WikiMultihopQA contains only 10 documents per question, we retrieve an additional 10 distractor documents using a contriever setup as in Liu et al. (2024).

Since the official test sets for all three datasets are private and reserved for leaderboard purposes, we create our own splits by dividing the existing validation sets in half. The first half serves as our validation data, while the second half is used as our test set for reporting results.

### 3.1.1 Models [p. 3]

To investigate the effects of the distance and position of evidence documents within a context on long-context language models, we experiment with a combination of popular open-source and closed-source models. Specifically, we use:

- **MPT-7b-8k-instruct:** An instruction-tuned model trained with ALiBi (Press et al., 2022), which replaces traditional positional embeddings.

- **Llama-2-7b-longlora-8k-ft** (Chen et al., 2023): A fine-tuned version of Llama 2 (Touvron et al., 2023) designed to support long contexts, without instruction tuning.

- **GPT-3.5-turbo-1106:** One of the latest versions of OpenAI's GPT-3.5 Turbo, offering a context window of 16k tokens and newly reproducible outputs.

These models, representing a mix of open- and closed-source architectures, allow us to assess the generalizability of our findings across different LLMs.

### 3.1.2 Metrics [p. 4]

Following Liu et al. (2024), Kandpal et al. (2023), and Mallen et al. (2022), we adopt best-subspan accuracy as our evaluation metric. This metric assigns a score of 1 if the model's response contains the annotated answer (or any of the alternative answers, in the case of the MuSiQue dataset), and 0 otherwise.

### 3.1.3 Context Reduction Methods [p. 4]

To investigate the relationship between context size and the "Lost in the Middle" problem, we extend our evaluation by applying two document size reduction methods:

1. **Knowledge Graph Triple Extraction:** A technique that condenses documents into structured triples, capturing key facts while minimizing extraneous information.

2. **Document Summarization:** A method that generates concise summaries of documents, preserving their core content while reducing their overall length.

By incorporating these reduction techniques, we aim to explore how modifying context size impacts the manifestation of the "Lost in the Middle" problem.

**Knowledge Graph Triple Extraction** For extracting knowledge graph triples, we employ an instruction-tuned approach using a 7-billion-parameter version of LLaMA 2 (Touvron et al., 2023). The model is prompted to extract triples from each individual document in the QA datasets, with the aim of capturing key factual relationships in a structured format.

**Summarization** To summarize the documents in our datasets, we use BART-large-CNN (Lewis et al., 2019), a pre-trained sequence-to-sequence model fine-tuned on the CNN/DailyMail news summarization dataset (Hermann et al., 2015). Each document is processed independently, with the maximum generation length capped at 50 tokens to ensure concise summaries.

| Dataset | Full | Summ. | KG |
|---------|------|-------|-----|
| HotpotQA | 69 | 29 | 33 |
| 2WikiMultihopQA | 45 | 21 | 29 |
| MuSiQue-Ans | 85 | 32 | 35 |

**Table 2** (p. 4): "Average document-wise word counts for each dataset and context-reduction method we use."
