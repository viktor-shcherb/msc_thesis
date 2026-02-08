# 4 How much context is used? [p. 3-4]

LSTMs are designed to capture long-range dependencies in sequences (Hochreiter and Schmidhuber, 1997). In practice, LSTM language models are provided an infinite amount of prior context (as long as the test sequence goes). However, it is unclear how much of this history has a direct impact on model performance. This section investigates how many tokens of context achieve a similar loss (or 1-2% difference in model perplexity) to providing the model infinite context. They consider this the *effective context size*. [p. 3]

**LSTM language models have an effective context size of about 200 tokens on average.** They determine the effective context size by varying the number of tokens fed to the model. At test time, they feed the model the most recent $n$ tokens: [p. 3]

$$\delta_{\text{truncate}}(w_{t-1}, \ldots, w_1) = (w_{t-1}, \ldots, w_{t-n}), \quad (1)$$

where $n > 0$ and all tokens farther away from the target $w_t$ are dropped. Words at the beginning of the test sequence with fewer than $n$ tokens in the context are ignored for loss computation. [p. 3]

They compare the dev loss (NLL) from truncated context to that of the infinite-context setting where all previous words are fed to the model. The resulting increase in loss indicates how important the dropped tokens are for the model. [p. 3]

**Figure 1a** (p. 4): Shows the difference in dev loss between truncated- and infinite-context variants as $n$ increases from 5 to 1000. The difference gradually diminishes. A 1% increase in perplexity is seen when moving beyond a context of 150 tokens on PTB and 250 tokens on Wiki. This provides empirical evidence that LSTM language models do, in fact, model long-range dependencies without help from extra context vectors or caches. [p. 3]

- X-axis: Context Size (number of tokens), log scale from 5 to 1000
- Y-axis: Increase in Loss (absolute increase in NLL)
- Two curves: PTB and Wiki, both monotonically decreasing
- Loss increase drops to near zero around 200-500 tokens

**Changing hyperparameters does not change the effective context size.** NLM performance has been shown to be sensitive to hyperparameters such as the dropout rate and model size (Melis et al., 2018). To investigate if these hyperparameters affect the effective context size as well, they train separate models by varying: (1) number of timesteps for truncated back-propagation, (2) dropout rate, (3) model size (hidden state size, number of layers, and word embedding size). [p. 3]

**Figure 1b** (p. 4): Shows that while different hyperparameter settings result in different perplexities in the infinite-context setting, the trend of how perplexity changes as context is reduced remains the same. [p. 3]

- X-axis: Context Size (number of tokens), log scale from 10 to 1000
- Y-axis: Perplexity, range roughly 60-110
- Multiple curves for PTB variants: Default Model, LSTM hidden 375 (vs. 1150), 2 layers (vs. 3), Word Emb 200 (vs. 400), No LSTM layer dropout (vs. 0.25), No recurrent dropout (vs. 0.5), BPTT 100 (vs. 70), BPTT 10 (vs. 70)
- All curves converge around 200-500 tokens

## 4.1 Do different types of words need different amounts of context? [p. 3-4]

The effective context size determined in the previous section is aggregated over the entire corpus, which ignores the type of the upcoming word. Boyd-Graber and Blei (2009) have previously investigated the differences in context used by different types of words and found that function words rely on less context than content words. [p. 3]

The authors investigate whether effective context size varies across different types of words, categorizing them based on either frequency or parts-of-speech. They vary the number of context tokens and aggregate loss over words within each class separately. [p. 3]

**Infrequent words need more context than frequent words.** Words appearing at least 800 times in the training set are categorized as *frequent*, the rest as *infrequent*. [p. 3]

**Figure 1c** (p. 4): The loss of frequent words is insensitive to missing context beyond the 50 most recent tokens, which holds across both datasets. Infrequent words, on the other hand, require more than 200 tokens. [p. 3]

- X-axis: Context Size (number of tokens), log scale from 5 to 1000
- Y-axis: Increase in Loss
- Four curves: infrequent words PTB, frequent words PTB, infrequent words Wiki, frequent words Wiki
- Infrequent word curves are higher and decay more slowly

**Content words need more context than function words.** *Content words* are defined as nouns, verbs and adjectives. *Function words* are defined as prepositions and determiners. POS tags obtained using Stanford CoreNLP (Manning et al., 2014). [p. 3]

**Figure 1d** (p. 4): The loss of nouns and verbs is affected by distant context, whereas when the target word is a determiner, the model only relies on words within the last 10 tokens. [p. 3]

- X-axis: Context Size (number of tokens), log scale from 5 to 1000
- Y-axis: Increase in Loss
- Five curves for Wiki: NN (nouns), JJ (adjectives), VB (verbs), IN (prepositions), DT (determiners)
- NN curve is highest/slowest to decay; DT curve drops to near zero fastest

**Discussion.** The model's effective context size is dynamic, depending on the target word, consistent with linguistic knowledge (e.g., determiners require less context than nouns) (Boyd-Graber and Blei, 2009). These findings are also consistent with those previously reported for different language models and datasets (Hill et al., 2016; Wang and Cho, 2016). [p. 4]
