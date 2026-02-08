# Appendix E: FLOPs Estimation [p. 83–84]

[p. 83] To estimate the FLOPs used for pretraining, the authors use a short Python script that accounts for all major operations in the Transformer architecture, provided in Figure E.2. Plugging in the 70B configuration (Table 1) at a sequence length of 4096, this results in an estimate of 6.74 * 10^24 FLOPs.

## Figure E.2

**Figure E.2** (p. 84): **FLOPs computation.** Instead of the common approximation of 6=ND, the authors use more detailed calculations for the FLOPs estimation based on the Transformer model configuration. They provide the Python code.

The figure shows a Python script with the following functions:

- `attention_gqa_flops(seq_len, d_model, key_size, num_heads, num_kv_heads)`: Computes FLOPs for grouped-query attention. Calculates q_proj, k_proj, v_proj, qk dot product, qk_norm, softmax, attn_v, and out_proj.
- `dense_mlp(seq_len, d_model, ffw_size, swiglu=False)`: Computes MLP FLOPs. Returns `2 * seq_len * (2 * d_model * ffw_size)` without SwiGLU, or `2 * seq_len * (3 * d_model * ffw_size)` with SwiGLU.
- `qk_norm_flops(seq_len, key_size, num_heads, num_kv_heads)`: Computes QK normalization FLOPs as `4 * vectors * key_size` where `vectors = seq_len * (num_heads + num_kv_heads)`.
- `rmsnorm(seq_len, d_model)`: Returns `4 * seq_len * d_model`.
- `final_logits(seq_len, d_model, vocab_size)`: Returns `2 * seq_len * d_model * vocab_size`.
- `get_flops(n_layers, seq_len, vocab_size, d_model, key_size, num_heads, num_kv_heads, ffw_size, swiglu=False)`: Aggregates all components: `n_layers * (attention_gqa_flops + dense_mlp + 2 * rmsnorm) + final_logits`.
