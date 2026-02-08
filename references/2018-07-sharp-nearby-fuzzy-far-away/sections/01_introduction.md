# 1 Introduction [p. 1-2]

Neural language models (NLMs) (Graves, 2013; Jozefowicz et al., 2016; Grave et al., 2017a; Dauphin et al., 2017; Melis et al., 2018; Yang et al., 2018) have consistently outperformed classical n-gram models, an improvement often attributed to their ability to model long-range dependencies in faraway context. Yet how NLMs use context is largely unexplained. [p. 1]

Recent studies on LSTM-encoded information show that LSTMs can remember sentence lengths, word identity, and word order (Adi et al., 2017), capture some syntactic structures such as subject-verb agreement (Linzen et al., 2016), and model certain kinds of semantic compositionality such as negation and intensification (Li et al., 2016). However, all previous work studies LSTMs at the sentence level, even though they can potentially encode longer context. [p. 1]

The authors' goal is to complement prior work by providing a richer understanding of the role of context, in particular long-range context beyond a sentence. They aim to answer three questions: [p. 1]

1. How much context is used by NLMs, in terms of the number of tokens?
2. Within this range, are nearby and long-range contexts represented differently?
3. How do copy mechanisms help the model use different regions of context?

They investigate these questions via ablation studies on a standard LSTM language model (Merity et al., 2018) on two benchmark language modeling datasets: Penn Treebank and WikiText-2. Given a pretrained language model, they perturb the prior context in various ways *at test time* to study how much the perturbed information affects model performance. Specifically, they alter context length, permute tokens to test word order sensitivity in both local and global contexts, and drop and replace target words to test the copying abilities of LSTMs with and without an external copy mechanism such as the neural cache (Grave et al., 2017b). [p. 1]

The cache operates by first recording target words and their context representations seen in the history, then encouraging the model to copy a word from the past when the current context representation matches that word's recorded context vector. [p. 1-2]

## Key findings (stated as contributions) [p. 2]

- The LSTM is capable of using about 200 tokens of context on average, with no observable differences from changing the hyperparameter settings.
- Within this context range, word order is only relevant within the 20 most recent tokens or about a sentence. In long-range context, order has almost no effect on performance, suggesting the model maintains a high-level, rough semantic representation of faraway words.
- LSTMs can regenerate some words seen in the nearby context, but heavily rely on the cache to help them copy words from the long-range context.
