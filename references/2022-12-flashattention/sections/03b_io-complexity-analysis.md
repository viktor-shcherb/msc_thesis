# 3.2 Analysis: IO Complexity of FlashAttention [p. 5-6]

[p. 5-6]

The IO complexity of FlashAttention is analyzed, showing significant reduction in HBM accesses compared to standard attention. A lower bound is also provided, proving that no exact attention algorithm can asymptotically improve on HBM accesses over all SRAM sizes. Proofs are in Appendix C.

## Theorem 2

> Let $N$ be the sequence length, $d$ be the head dimension, and $M$ be the size of SRAM with $d \leq M \leq Nd$. Standard attention (Algorithm 0) requires $\Theta(Nd + N^2)$ HBM accesses, while FlashAttention (Algorithm 1) requires $\Theta(N^2 d^2 M^{-1})$ HBM accesses. [p. 6]

For typical values of $d$ (64-128) and $M$ (around 100KB), $d^2$ is many times smaller than $M$, and thus FlashAttention requires many times fewer HBM accesses than standard attention. This leads to both faster execution and lower memory footprint, which is validated in Section 4.3.

## Proof Sketch

The main idea of the proof is that given the SRAM size of $M$, blocks of **K**, **V** of size $\Theta(M)$ can be loaded each (Algorithm 1 line 6). For each block of **K** and **V**, iteration over all blocks of **Q** (Algorithm 1 line 8) computes the intermediate values, resulting in $\Theta(NdM^{-1})$ passes over **Q**. Each pass loads $\Theta(Nd)$ elements, which amounts to $\Theta(N^2 d^2 M^{-1})$ HBM accesses. The backward pass of standard attention requires $\Theta(Nd + N^2)$ HBM accesses while the backward pass of FlashAttention requires $\Theta(N^2 d^2 M^{-1})$ HBM accesses (Appendix B).

## Proposition 3 (Lower Bound)

> Let $N$ be the sequence length, $d$ be the head dimension, and $M$ be the size of SRAM with $d \leq M \leq Nd$. There does not exist an algorithm to compute exact attention with $o(N^2 d^2 M^{-1})$ HBM accesses for all $M$ in the range $[d, Nd]$. [p. 6]

The proof relies on the fact that for $M = \Theta(Nd)$ any algorithm must perform $\Omega(N^2 d^2 M^{-1}) = \Omega(Nd)$ HBM accesses. This type of lower bound over a subrange of $M$ is common in the streaming algorithms literature [88]. Proving parameterized complexity [27] lower bounds in terms of $M$ is left as exciting future work.

## Empirical Validation

[p. 6]

The number of HBM accesses is the main determining factor of attention run-time.

**Figure 2** (p. 6): "Left: Forward + backward runtime of standard attention and FlashAttention for GPT-2 medium (seq. length 1024, head dim. 64, 16 heads, batch size 64) on A100 GPU. HBM access is the primary factor affecting runtime. Middle: Forward runtime of FlashAttention (seq. length 1024, head dim. 64, 16 heads, batch size 64) on A100 GPU. Fewer HBM accesses result in faster runtime, up to a point. Right: The runtime (for seq. length 4K) of block-sparse FlashAttention is faster than FlashAttention by a factor proportional to the sparsity."

The figure contains three panels and a table:

**Left panel table:**

| Attention | Standard | FlashAttention |
|-----------|----------|----------------|
| GFLOPs | 66.6 | 75.2 |
| HBM R/W (GB) | 40.3 | 4.4 |
| Runtime (ms) | 41.7 | 7.3 |

**Middle panel:** Plot of HBM Accesses (GB) vs Block Size (x-axis: 64, 128, 256, 512). Shows two lines: HBM Accesses (decreasing from ~8 to ~1 GB as block size increases) and Runtime (decreasing from ~6 to ~2 ms as block size increases, then leveling off around 256-512).

**Right panel:** "Sparsity Speedup" plot showing Fwd + Bwd runtime (ms) vs % Non-Zero Blocks (x-axis: 20, 60). Three lines: Dense (standard attention, dashed, flat at ~150ms), FlashAttention (dotted, flat at ~100ms), and Block-Sparse FlashAttention (solid line, increasing roughly linearly from ~30ms at 20% to ~100ms at 60%).
