# 3 Experiment Setup [p. 2-3]

[p. 2] The authors compared the validation set perplexity of models trained from scratch with no explicit positional information (denoted as *NoPos*) to those trained with the various positional encoding methods discussed in Section 2. They investigated the canonical WikiText-103 setting (Merity et al., 2017; Baevski and Auli, 2019), as well as a newer, large-scale setting based on the Pile corpus (Gao et al., 2020) on model architectures inspired by Brown et al. (2020), covering a spectrum of model sizes and sequence lengths.

## The Canonical Setting (WikiText-103)

[p. 2] The WikiText-103 corpus (Merity et al., 2017) consists of over 100 million words extracted from a set of high-quality Wikipedia articles. The corpus is tokenized at the word level, resulting in a vocabulary of over 267K tokens. For this corpus, the authors used the adaptive embedding transformer model of Baevski and Auli (2019), which contains:

- 16 transformer layers
- 1024 model dimensions
- 4096 feed-forward dimensions
- 8 attention heads
- 247M parameters in total

They trained with the exact optimization hyperparameters as implemented in fairseq (Ott et al., 2019), with the exception of the input sequence length, which was shortened to 512 tokens (instead of 3072), as in Press et al. (2022). See App. C for detailed hyperparameters.

## The Large-Scale Setting (The Pile)

[p. 2-3] The Pile (Gao et al., 2020) is an 800GB English text dataset composed of Common Crawl and 22 other diverse sources. For the experiments, the authors used 2 out of 30 shards; they filtered out the GitHub and DM Mathematics sources and removed the shortest 1% and longest 1% of examples from each source to reduce noise. They used GPT-2's tokenizer (Radford et al., 2019) to convert the text into token sequences over a vocabulary of 50K tokens. They randomly sampled a validation set of 2000 documents (2.6M tokens) from the corpus, while the remaining 15M documents (21B tokens) comprised the training set.

Footnote 1: Shards 00 and 01 can be downloaded from: https://the-eye.eu/public/AI/pile/train/

[p. 3] The baseline model in this setting follows the 1.3B parameter architecture of Brown et al. (2020), also known as GPT-3 XL:

- 24 transformer layers
- 2048 model dimensions
- 8192 feed-forward dimensions
- 32 attention heads
- Default input sequence length: 1024 tokens

See App. C for detailed hyperparameters.

## Scaling Experiments

[p. 3] To demonstrate the consistency of results across different settings, two scaling experiments are performed:

1. **Model size scaling:** Experimenting with the small (125M parameters), medium (350M parameters), large (760M parameters) and the XL (1.3B parameters) variants of the Brown et al. (2020) architecture on the Pile settings.

2. **Sequence length scaling:** Evaluating the effect of varying the sequence length using the XL (1.3B parameter) model. Experiments with sequences of lengths {256, 512, 1024, 2048}.

Additionally, to shed light on differences between the NoPos model and other methods, the authors compare the model's performance on different parts of the sequence. Details and results are given in App. A.
