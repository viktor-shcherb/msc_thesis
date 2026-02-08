# 4 Results [p. 3-4]

[p. 3] Table 1 compares the performance of training LMs with different position encoding methods. NoPos LMs approach the performance of the other models, with gaps of 0.55 (WikiText-103) and 0.05 (The Pile) perplexity from models with *learned* positional embeddings. In the Pile setting, performance differences between *NoPos*, *Learned*, and *Sinusoidal* are small both in absolute terms and with respect to their difference with *ALiBi*. In the WikiText-103 setting, performance gaps are wider but still modest with respect to random seed variance.

Footnote 2: For context, Press et al. (2020) report that training the sinusoidal model with inputs of length 3072 on WikiText-103 with 5 different seeds can result in gaps of up to 0.9 perplexity between runs (0.34 standard deviation).

**Table 1** (p. 3): Validation set perplexity of transformer language models trained with various positional encoding methods. The WikiText-103 setting (Merity et al., 2017) uses the model of Baevski and Auli (2019) on sequences of 512 tokens, while the Pile settings (Gao et al., 2020) uses a more recent 1.3B parameter architecture (Brown et al., 2020) over 1024 token sequences.

|                | WikiText-103 | The Pile |
|----------------|-------------|----------|
| NoPos          | 20.97       | 13.10    |
| Learned        | 20.42       | 13.05    |
| Sinusoidal     | 20.16       | 12.93    |
| ALiBi          | 19.71       | 12.51    |

[p. 3] These results strongly suggest that training transformer language models without explicit positional encoding is indeed possible.

Table 2 explores the effects of scaling the number of parameters in the Pile setting. While smaller models benefit from fixed, non-parametric positional encodings (*Sinusoidal* and *ALiBi*), these performance gaps narrow in larger models.

**Table 2** (p. 3): Validation set perplexity on the Pile, as a function of positional encoding method and model size. All models operate on sequences of 1024 tokens. Smaller models benefit from fixed, non-parametric positional encodings (*Sinusoidal* and *ALiBi*), but these performance gaps diminish as the models scale up.

| Model Size  | 125M  | 350M  | 760M  | 1.3B  |
|-------------|-------|-------|-------|-------|
| NoPos       | 22.15 | 16.87 | 14.29 | 13.10 |
| Learned     | 22.04 | 16.84 | 14.21 | 13.05 |
| Sinusoidal  | 21.49 | 16.58 | 14.04 | 12.93 |
| ALiBi       | 19.94 | 15.66 | 13.53 | 12.51 |

Table 3 shows the effect of varying the sequence length in the same setting. The gaps between *NoPos*, *Learned*, and *Sinusoidal* remain almost constant, while the benefit of using *ALiBi* increases as sequences become longer.

**Table 3** (p. 3): Validation set perplexity on the Pile, as a function of positional encoding method and sequence length. All models have 1.3B parameters. The performance differences between *NoPos*, *Learned*, and *Sinusoidal* are consistently small, while *ALiBi* slowly becomes more beneficial as sequences become longer.

| Seq Length  | 256   | 512   | 1024  | 2048  |
|-------------|-------|-------|-------|-------|
| NoPos       | 14.98 | 13.82 | 13.10 | 12.87 |
| Learned     | 14.94 | 13.77 | 13.05 | 12.72 |
| Sinusoidal  | 14.84 | 13.66 | 12.93 | 12.62 |
| ALiBi       | 14.65 | 13.37 | 12.51 | 12.06 |

[p. 3] Overall, the authors show that transformer language modeling without explicit positional encoding is robust to the selection of corpus, model size, and sequence length.

As training models at the 1.3B parameter scale is resource-intensive, the authors publicly release their trained models for future research and analysis.

Footnote 3: https://github.com/adihaviv/NoPos

[p. 4] In a concurrent work, Scao et al. (2022) makes a similar observation in one of their ablation experiments and further show that NoPos models gain competitive performances for downstream tasks as well. Specifically, they evaluated 27 diverse downstream tasks. They showed that the NoPos model reached an average accuracy of 41.23% over all tasks, comparing to *Learned* and *ALiBi* who gained 41.72% and 43.70% respectively.

**Figure 1** (p. 1): "Transformer language models trained without explicitly encoding positional information (*NoPos*) approach the performance of models trained with various positional encoding methods. All models have 1.3B parameters, and are trained on an excerpt of the Pile."

Bar chart showing validation set perplexity for four methods: NoPos (13.10), Learned (13.05), Sinusoidal (12.93), ALiBi (12.51). Y-axis is perplexity (range ~10-14). All bars are close in height, demonstrating that NoPos is competitive. Supports the main claim that models without positional encoding achieve near-parity with position-aware models.
