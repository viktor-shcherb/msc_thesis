# Appendix B: Comparison of Compressed Memory Sizes [p. 15]

[p. 15] The authors compare the best test perplexity obtained for the Compressive Transformer trained on WikiText-103 and Enwik8 across a range of compressed memory sizes. For both models, the best model used a 1D convolution compression network with a compression rate of 3.

## Enwik8 model details
- Embedding size: 1024
- Attention heads: 8
- Layers: 24
- MLP hidden size: 3072
- Sequence window size: 768
- Memory size: 768
- Best compressed memory size: 3,072 (total attention window of 3,840)

**Table 8** (p. 15): Compressed memory size vs test performance for Enwik8

| Compressed Memory Size | 512  | 1024 | 2048 | 3072 | 4096 |
|---|---|---|---|---|---|
| Enwik8 BPC             | 1.01 | 0.99 | 0.98 | 0.97 | 1.00 |

## WikiText-103 model details
- Embedding size: 1024
- Adaptive inputs using the same parameters as Sukhbaatar et al. (2019)
- Attention heads: 16
- Layers: 18
- MLP hidden size: 4096
- Sequence window size: 512
- Memory size: 512
- Best compressed memory size: 1536 (total attention window of c. 2048)

**Table 9** (p. 15): Compressed memory size vs test performance for WikiText-103

| Compressed Memory Size       | 256  | 512  | 1024 | 1536 | 2048 |
|---|---|---|---|---|---|
| WikiText-103 Perplexity      | 18.2 | 17.9 | 17.6 | 17.1 | 17.7 |
