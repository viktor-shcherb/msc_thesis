# Appendix B: Additional Architecture Details [p. 29–30]

[p. 29] The WKV computations of Eagle and Finch can be parallelized across the time dimension using a variety of techniques including associative scan or the parallelization techniques used in FlashAttention. (Dao et al., 2022) The simplest of these, while highly parallel, prove inefficient due to repeated expensive memory transfers between fast SRAM and slower HBM. We take a different approach when training, choosing to parallelize over non-time dimensions only while using a custom CUDA implementation that carefully keeps state operations in fast SRAM, which is simpler yet provides enough breadth for a highly efficient implementation. See Section 9 for kernel experiments. We provide an additional pure PyTorch implementation with similar full-model speed characteristics that parallelizes over the time dimension using an algorithmic approach similar to GLA (Yang et al., 2023).

[p. 29] Unlike Transformers, RWKV's recurrence mechanism does not examine tokens more than one time-step old. This allows us to train on and provide inference for unbounded sequence lengths without requiring increased computing power or memory. Another significant advantage is that RWKV does not utilize explicit positional encoding, which allows RWKV to handle contexts of arbitrary length without modification.

## Finch Token Shift

[p. 29] Finch changes the token shift mechanism to become data-dependent. Intuitively, important information can effectively flag itself for inclusion using this mechanism, and less important information can flag itself to partially or fully avoid entering the data stream, leaving room for more important pre-existing data to remain. Viewed from the perspective of induction heads, we theorize that this could allow for potential misleading matches to be pre-filtered out up front if they are not deemed useful for a given task.

## Improved WKV (Weighted Key-Value State) Modules

[p. 30] The Eagle WKV attention sub-module is similar to the linear attention mechanism found in RetNet, but with learned per-channel decay rates replacing RetNet's static per-head decay rates. Our matrix-valued states feature a geometrically decaying K^T V ∈ R^{(D/h)×(D/h)} term. This term can be intuitively understood as a memory bank of values, with K acting as the eliminator gate that rows receiving the current token embedding's value. Each row of this state decays at its own rate via the learned parameter w.

[p. 30] In Finch, we augment the learned token-shift parameters μ_r, μ_k, μ_v, μ_w and decay rate parameter w with learned weight matrices. Inspired by Low-Rank Adaptation (LoRA) (Hu et al., 2022), we provide two new learned weight matrices for each such parameter y, computing y' = y + tanh(xA)B. This approach allows us to dynamically generate data-dependent token-shift amounts and decay rates with only modest increases in computational cost and model size.

## Extra SiLU Gating

[p. 30] We remove the Sigmoid activation of receptance in favor of a new SiLU gate on the output of our linear attention calculation. Our receptance term now functions much like the query term in linear attention.

## Eagle and Finch Linear Attention Formula, PyTorch Recurrent Implementation

[p. 30] Code snippet showing the recurrent implementation:

```python
# r, k, v parameter shape (B,H,1,D//H)
# w parameter of shape (1,H,1,D//H) for Eagle (RWKV-5),
#                       (B,H,1,D//H) for Finch (RWKV-6)
# u parameter of shape (1,H,1,D//H)
# wkv_state parameter of shape (B,H,D//H,D//H)
def rwkv_5_or_6_recurrent(r, k, v, w, u, wkv_state):
    kv = k.mT @ v
    out = r @ (wkv_state + u.mT * kv)
    wkv_state = w.mT * wkv_state + kv
    return out, wkv_state
```

## Evolution of RWKV Formula in Expanded form

[p. 30] Table 8 shows the expansion of terms at each sequence position to illustrate the progression of changes from RWKV-4 through RWKV-6. The main change from RWKV-4 to RWKV-5 is the elimination of denominator and incorporation of matrix states. RWKV-6 introduces the sequential dependence of w which becomes w_t.

### Table 8: Evolution of the RWKV Formula [p. 30]

| t | RWKV-4 u, w, k_t, v_t ∈ R^D, head size 1 |
|---|------------------------------------------|
| 0 | σ(r_0) ⊙ (u⊙k_0⊙v_0)/(u⊙k_0) |
| 1 | σ(r_1) ⊙ (w⊙k_0⊙v_0+u⊙k_1⊙v_1)/(w⊙k_0+u⊙k_1) |
| 2 | σ(r_2) ⊙ (w⊙k_0⊙v_0+k_1⊙(w+u⊙k_0)⊙v_0)/(w⊙k_1+k_1+u⊙k_0) |
| 3 | σ(r_3) ⊙ (u⊙k_0⊙v_0+k_0⊙(w+u⊙k_0)⊙v_1+w^2⊙k_0⊙v_0)/(w⊙k_0+k_1+w^2⊙k_0+u⊙k_3) |

| t | Eagle (RWKV-5) diag(u), diag(w), k_t, v_t ∈ R^{64×64} for each head, head size 64 |
|---|-----------------------------------------------------------------------------------|
| 0 | r_0·(diag(u)·k_0^T·v_0) |
| 1 | r_1·(diag(u)·k_1^T·v_1 + k_0^T·v_0) |
| 2 | r_2·(diag(u)·k_2^T·v_2 + k_1^T·v_1 + diag(w)·k_0^T·v_0) |
| 3 | r_3·(diag(u)·k_3^T·v_3 + k_2^T·v_2 + diag(w)·k_1^T·v_1 + diag(w^2)·k_0^T·v_0) |

| t | Finch (RWKV-6) diag(u), diag(w_t), k_t, v_t ∈ R^{64×64} for each head, head size 64 |
|---|------------------------------------------------------------------------------------|
| 0 | r_0·(diag(u)·k_0^T·v_0) |
| 1 | r_1·(diag(u)·k_1^T·v_1 + k_0^T·v_0) |
| 2 | r_2·(diag(u)·k_2^T·v_2 + k_1^T·v_1 + diag(w_1)·k_0^T·v_0) |
| 3 | r_3·(diag(u)·k_3^T·v_3 + k_2^T·v_2 + diag(w_2)·k_1^T·v_1 + diag(w_2 ⊙ w_1)·k_0^T·v_0) |

Caption: Evolution of the RWKV Formula
