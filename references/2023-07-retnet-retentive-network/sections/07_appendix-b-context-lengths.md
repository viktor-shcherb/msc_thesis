# B Grouped Results of Different Context Lengths [p. 14]

As shown in Table 8, language modeling results with different context lengths are reported. In order to make the numbers comparable, 2048 text chunks are used as evaluation data and perplexity is computed only for the last 128 tokens. Experimental results show that RetNet outperforms Transformer across different context lengths. Besides, RetNet can utilize longer context for better results. [p. 14]

**Table 8** (p. 14): "Language modeling perplexity of RetNet and Transformer with different context length. The results show that RetNet has a consistent advantage across sequence length."

| Model | 512 | 1024 | 2048 |
|---|---|---|---|
| Transformer | 13.55 | 12.56 | 12.35 |
| RetNet | 13.09 | 12.14 | 11.98 |
