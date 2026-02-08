# 4 Related Work [p. 8-9]

## 4.1 Efficient Transformers [p. 8]

The pervasiveness of Transformer models, along with its well-known trait of being memory intensive, has spurred on a large number of innovations on this front. Early work in this area has typically considered a fixed pattern (local window) approach (Liu et al., 2018; Parmar et al., 2018). More advanced models have been proposed recently, including combined patterns (Child et al., 2019; Ho et al., 2019; Beltagy et al., 2020; Zaheer et al., 2020), learned patterns (Kitaev et al., 2020; Roy et al., 2020), and recent models based on kernels (Katharopoulos et al., 2020; Choromanski et al., 2020a) or low-rank approximations (Wang et al., 2020). The authors refer interested readers to (Tay et al., 2020c) for a detailed survey of this line of research.

## 4.2 Existing Benchmarks [p. 8-9]

### Generative Modeling / Language Modeling [p. 8-9]

[p. 8] This generative modeling task requires predicting the next character, word, or pixel and is a staple in xformer evaluations (Roy et al., 2020; Kitaev et al., 2020). However, it has been debated how much long-range signal such tasks actually encode (Rae & Razavi, 2020).

[p. 9] LSTM language models augmented with attention have been shown to rarely attend beyond seven preceding words of context (Daniluk et al., 2017) and samples from LSTM language models are known to quickly devolve into generic text. On the other hand, recent models such as the Transformer-XL (Dai et al., 2019) have been observed to be sensitive to a context of around 900 tokens and samples from large-scale models (Radford et al., 2019) maintain a consistent theme over much longer sequences. Even such recent models, however, can be improved by limiting the range of attention (Rae & Razavi, 2020). In sum, while standard language modelling datasets contain *some* long-range signal, which is required to perform long-range coreference resolution, reasoning with events, discourse understanding, etc. (Ruder et al., 2019) it seems to be overshadowed by the much stronger signal of short-term word co-occurrences and is thus difficult to evaluate.^5

Footnote 5 [p. 9]: Datasets such as LAMBADA (Paperno et al., 2016) more explicitly test for context understanding but are still restricted to comparatively short contexts of five sentences on average.

### Question Answering [p. 9]

Another commonly used evaluation task is question answering (QA; Zaheer et al., 2020). Open-domain QA in particular typically requires the model to answer questions based on long contexts such as entire Wikipedia documents (Joshi et al., 2017; Kwiatkowski et al., 2019) or even books (Kocisk\u00fd et al., 2018). Other datasets are explicitly designed to require multiple 'hops' of reasoning (Welbl et al., 2018; Yang et al., 2018). Successful approaches are often highly engineered, computationally expensive approaches that require pre-training and a separate retrieval model (Lee et al., 2019; Guu et al., 2020).

### Natural Language Understanding / GLUE tasks [p. 9]

Evaluation on natural language understanding (NLU) tasks is also common (Wang et al., 2020). Examples in most of these datasets such as MultiNLI (Williams et al., 2018) and SST (Socher et al., 2013) consist of single sentences and less than 100 tokens on average.
