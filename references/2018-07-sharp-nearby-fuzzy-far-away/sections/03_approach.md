# 3 Approach [p. 2-3]

The goal is to investigate the effect of contextual features such as the length of context, word order, and more, on LSTM performance. They use ablation analysis during evaluation to measure changes in model performance in the absence of certain contextual information. [p. 2]

Typically, when testing a language model on a held-out sequence of words, all tokens prior to the target word are fed to the model; this is called the *infinite-context* setting. In this study, they observe the change in perplexity or NLL when the model is fed a perturbed context $\delta(w_{t-1}, \ldots, w_1)$ at test time. $\delta$ refers to the perturbation function. Perturbations include dropping tokens, shuffling/reversing tokens, and replacing tokens with other words from the vocabulary. [p. 2]

> "It is important to note that we do not train the model with these perturbations. This is because the aim is to start with an LSTM that has been trained in the standard fashion, and discover how much context it uses and which features in nearby vs. long-range context are important. Hence, the mismatch in training and test is a necessary part of experiment design, and all measured losses are upper bounds which would likely be lower, were the model also trained to handle such perturbations." [p. 2]

Code available at: https://github.com/urvashik/lm-context-analysis [p. 2]

## Model

They use a standard LSTM language model, trained and finetuned using the Averaging SGD optimizer (Merity et al., 2018). They also augment the model with a cache *only* for Section 6.2, to investigate why an external copy mechanism is helpful. Architecture and hyperparameters are listed in Appendix A. [p. 2]

Public release of LSTM code at: https://github.com/salesforce/awd-lstm-lm [p. 2]

## Datasets

Two datasets commonly used for language modeling: [p. 2-3]

- **Penn Treebank (PTB)** (Marcus et al., 1993; Mikolov et al., 2010): Wall Street Journal news articles with 0.9M tokens for training and a 10K vocabulary.
- **Wikitext-2 (Wiki)** (Merity et al., 2017): A larger and more diverse dataset, containing Wikipedia articles across many topics with 2.1M tokens for training and a 33K vocabulary.

**Table 1** (p. 2): Dataset statistics and performance relevant to experiments.

|                        | PTB Dev | PTB Test | Wiki Dev | Wiki Test |
|------------------------|---------|----------|----------|-----------|
| # Tokens               | 73,760  | 82,430   | 217,646  | 245,569   |
| Perplexity (no cache)  | 59.07   | 56.89    | 67.29    | 64.51     |
| Avg. Sent. Len.        | 20.9    | 20.9     | 23.7     | 22.6      |

Results are presented only on the dev sets to avoid revealing details about the test sets. All results are confirmed to be consistent with test sets. All experiments report averaged results from three models trained with different random seeds. [p. 3]
