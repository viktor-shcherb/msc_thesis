# Appendix A: Ablation of Text Contained Within Each Chunk [p. 13]

[p. 13] Appendix A studies strategies for selecting chunk content offset `v_i` in Equation (5):
- `v_i ~ U({v_{i-1}, ..., Lx-Lc})` (default PoSE)
- `v_i = 0`
- `v_i = u_i`

[p. 13] Setup follows main experiments for extending LLaMA-7B from 2k to 16k.

**Table 4** (p. 13): "Comparison of different methods for choosing v_i."

| Method | Gov 2k | Gov 4k | Gov 8k | Gov 16k | Proof 2k | Proof 4k | Proof 8k | Proof 16k |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `v_i ~ U(...)` | 4.84 | 4.68 | 4.60 | 4.60 | 2.95 | 2.74 | 2.61 | 2.60 |
| `v_i = 0` | 4.85 | 4.72 | 4.64 | 4.68 | 2.96 | 2.75 | 2.63 | 2.61 |
| `v_i = u_i` | 4.84 | 4.68 | 4.60 | 4.60 | 2.95 | 2.73 | 2.60 | 2.56 |

[p. 13] Claimed result: different `v_i` assignment rules have relatively small impact on outcomes.
