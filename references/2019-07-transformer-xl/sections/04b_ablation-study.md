# 4.2 Ablation Study [p. 7-8]

Two sets of ablation studies examine the effects of two proposed techniques used in Transformer-XL: the recurrence mechanism and the new positional encoding scheme. [p. 7]

## Ablation 1: Encoding schemes on WikiText-103

[p. 7-8] The first study is performed on WikiText-103, which requires modeling long-term dependency. The results are reported in Table 6. Among the compared encoding schemes, Shaw et al. (2018) is relative, while Vaswani et al. (2017) and Al-Rfou et al. (2018) are absolute. "Full" and "half" losses refer to applying a cross entropy loss to all or the recent half positions in the segment. [p. 7]

The authors find that absolute encodings only work well with half losses because half losses exclude positions with very short attention lengths during training for better generalization. Table 6 shows that both the recurrence mechanism and the proposed encoding scheme are necessary to achieve the best performance, as well as generalizing to longer attention sequences during evaluation time. Although the backpropagation length during training is only 128, with the two techniques the attention length can be increased to 640 at test time. In the standard setting with 151M parameters, the perplexity decreases as the attention length increases. [p. 8]

Since the recurrence mechanism costs additional memory, Transformer-XL is also compared with baselines under the same GPU memory constraints. As shown in Table 10 in Appendix A, despite using a shorter backpropagation length, Transformer-XL remains superior to the baselines. [p. 8]

**Table 6** (p. 8): Ablation study on WikiText-103. For the first two blocks, a slightly smaller model (128M parameters) is used. dagger indicates that the corresponding row is reduced to the same setting as the Transformer network in Al-Rfou et al. (2018), except that two auxiliary losses are not implemented. "PPL init" refers to using the same length as training. "PPL best" indicates the perplexity obtained by using the optimal length. "Attn Len" is the shortest possible attention length during evaluation to achieve the corresponding result (PPL best). Increasing the attention length during evaluation improves performance only when the proposed positional encoding is used. The "Transformer-XL (151M)" setting uses a standard parameter budget as previous work (Merity et al., 2018), where a similar effect is observed when increasing the attention length during evaluation.

| Remark | Recurrence | Encoding | Loss | PPL init | PPL best | Attn Len |
|---|---|---|---|---|---|---|
| Transformer-XL (128M) | yes | Ours | Full | 27.02 | 26.77 | 500 |
| - | yes | Shaw et al. (2018) | Full | 27.94 | 27.94 | 256 |
| - | yes | Ours | Half | 28.69 | 28.33 | 460 |
| - | no | Ours | Full | 29.59 | 29.02 | 260 |
| - | no | Ours | Half | 30.10 | 30.10 | 120 |
| - | no | Shaw et al. (2018) | Full | 29.75 | 29.75 | 120 |
| - | no | Shaw et al. (2018) | Half | 30.50 | 30.50 | 120 |
| - | no | Vaswani et al. (2017) | Half | 30.97 | 30.97 | 120 |
| Transformer (128M)^dagger | no | Al-Rfou et al. (2018) | Half | 31.16 | 31.16 | 120 |
| Transformer-XL (151M) | yes | Ours | Full | 23.43 | 23.09 | 640 |
| - | - | - | - | - | 23.16 | 450 |
| - | - | - | - | - | 23.35 | 300 |

## Ablation 2: Recurrence on One Billion Word

[p. 8] The second study targets isolating the effects of resolving the context fragmentation problem from the benefit of capturing longer context length. A dataset that does not require long-term dependency is deliberately chosen, so that any improvement from establishing the recurrence can be attributed to solving the context fragmentation. Specifically, a controlled experiment is performed on the One Billion Word dataset, which can only benefit from removing the context fragmentation. A 20-layer Transformer-XL with ~0.3B parameters is trained for 400K steps. [p. 8]

As shown in Table 7, using segment-level recurrence substantially improves performance even when long-term dependency is not needed, which is consistent with the discussion that the recurrence mechanism resolves the context fragmentation problem. Moreover, the relative positional encodings are also superior to Shaw et al. (2018) on short sequences. [p. 8]

**Table 7** (p. 8): Ablation study on One Billion Word, a dataset without long-term dependency.

| Method | PPL |
|---|---|
| Ours | **25.2** |
| With Shaw et al. (2018) encodings | 25.7 |
| Without recurrence | 27.1 |
