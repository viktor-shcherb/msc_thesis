# 3 Methodology [p. 2-3]

## Research questions

[p. 2] The paper poses three research questions:

1. What are the common attention patterns, how do they change during fine-tuning, and how does that impact the performance on a given task? (Sec. 4.1, 4.3)
2. What linguistic knowledge is encoded in self-attention weights of the fine-tuned models and what portion of it comes from the pre-trained BERT? (Sec. 4.2, 4.4, 4.5)
3. How different are the self-attention patterns of different heads, and how important are they for a given task? (Sec. 4.6)

## Model

[p. 2] All experiments with pre-trained BERT use the PyTorch implementation of BERT (bert-base-uncased, 12-layer, 768-hidden, 12-heads, 110M parameters).

> "We chose this smaller version of BERT because it shows competitive, if not better, performance while having fewer layers and heads, which makes it more interpretable." [p. 2]

## GLUE tasks used for fine-tuning

[p. 2-3] The following subset of GLUE tasks (Wang et al., 2018) is used:

- *MRPC*: the Microsoft Research Paraphrase Corpus (Dolan and Brockett, 2005)
- *STS-B*: the Semantic Textual Similarity Benchmark (Cer et al., 2017)
- *SST-2*: the Stanford Sentiment Treebank, two-way classification (Socher et al., 2013)
- *QQP*: the Quora Question Pairs dataset
- *RTE*: the Recognizing Textual Entailment datasets
- *QNLI*: Question-answering NLI based on the Stanford Question Answering Dataset (Rajpurkar et al., 2016)
- *MNLI*: the Multi-Genre Natural Language Inference Corpus, matched section (Williams et al., 2018)

[p. 3] Two tasks were excluded: CoLa and the Winograd Schema Challenge. The latter was excluded due to small dataset size. CoLa (predicting linguistic acceptability judgments) was excluded because human performance is only 66.4, which is explained by problems with the underlying methodology (Schutze, 1996). CoLa is also not included in the upcoming version of GLUE (Wang et al., 2019).

## Fine-tuning setup

[p. 3] All fine-tuning experiments follow the parameters reported in the original study: batch size of 32 and 3 epochs (see Devlin et al. (2018)).

## Self-attention maps

[p. 3] For a given input, self-attention weights are extracted for each head in every layer. This results in a 2D float array of shape *L* x *L*, where *L* is the length of an input sequence. These arrays are referred to as *self-attention maps*. Analysis of individual self-attention maps allows determining which target tokens are attended to the most as the input is processed token by token. The authors use these experiments to analyze how BERT processes different kinds of linguistic information, including the processing of different parts of speech (nouns, pronouns, and verbs), syntactic roles (objects, subjects), semantic relations, and negation tokens.
