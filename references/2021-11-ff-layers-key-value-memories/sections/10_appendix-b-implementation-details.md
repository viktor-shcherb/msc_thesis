# B Implementation Details [p. 11]

[p. 11] Further implementation details are provided for reproducibility of experiments.

## Model

For all experiments, the language model of Baevski and Auli (2019) (247M parameters) trained on WikiText-103 (Merity et al., 2017) is used. Specifically, the model `transformer_lm.wiki103.adaptive` trained with the fairseq toolkit^6 is used.

## Dataset

WikiText-103^7 is a well known language modeling dataset and a collection of over 100M tokens extracted from Wikipedia. spaCy^8 was used to split examples into sentences (Section 3).

---

^6 https://github.com/pytorch/fairseq
^7 https://blog.einstein.ai/the-wikitext-long-term-dependency-language-modeling-dataset/
^8 https://spacy.io/
