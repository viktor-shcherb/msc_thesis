# Appendix A: Ablation Study with Memory Constraints [p. 11]

Table 10 compares Transformer-XL with a baseline under the same GPU memory budget. Transformer-XL still outperforms the baseline even with a shorter backpropagation length. [p. 11]

**Table 10** (p. 11): Ablation study on WikiText-103 with the same GPU memory constraints.

| Backprop Len | Recurrence | Encoding | Loss | pplx best | pplx init | Attn Len |
|---|---|---|---|---|---|---|
| 128 | yes | Ours | Full | 26.77 | 27.02 | 500 |
| 128 | yes | Ours | Partial | 28.33 | 28.69 | 460 |
| 176 | no | Ours | Full | 27.98 | 28.43 | 400 |
| 172 | no | Ours | Partial | 28.83 | 28.83 | 120 |
