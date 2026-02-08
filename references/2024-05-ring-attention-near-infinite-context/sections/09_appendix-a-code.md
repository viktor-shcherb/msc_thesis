# A Code [p. 14-15]

[p. 14] The implementation of Ring Attention in Jax is provided in Figure 4. The authors use `defvjp` function to define both the forward and backward passes, and use collective operation `jax.lax.ppermute` to facilitate the exchange of key-value blocks among a ring of hosts. The complete code is available at https://github.com/lhao499/llm_large_context.

For large scale end-to-end training on TPU or on GPU cluster with high bandwidth inter connection, the authors recommend using FSDP to shard large models and using Ring Attention to achieve large context. The degree of parallelism can be adjusted using the `mesh_dim` parameter within the codebase. To illustrate, consider a setup with 512 devices, such as 512x A100. If the model size is 30B, you can shard it across 8 devices and allocate the remaining 32 devices for Ring Attention. This setup allows the context size to be expanded 32 times more than if you didn't use Ring Attention. Conversely, for models sized 7B or 3B, there is no need for FSDP. This means you can utilize all 512 devices exclusively to expand the context using Ring Attention by 512 times. Building upon the result that our approach allows for a 256K context size when using 8x A100 GPUs, it suggests that by employing 512 A100 GPUs, the potential context size can be expanded to 16 million.

**Figure 4** (p. 15): "Key parts of the implementation of Ring Attention in Jax. We use collective operation lax.ppermute to send and receive key value blocks between previous and next hosts."

The figure shows a code listing of three Jax functions:
- `_ring_attention_fwd(q, k, v, attn_bias, axis_name, float32_logits, blockwise_kwargs)`: The forward pass. Initializes numerator and denominator accumulators, defines an inner `scan_kv_block` function that iterates over key-value blocks. Uses `lax.dynamic_slice_in_dim` for attention bias slicing, computes blockwise attention forward for each block, and uses `map(lambda x: lax.ppermute(...))` to rotate key-value blocks to the next host. Uses `lax.scan` to iterate through all blocks. Returns output normalized by denominator.
- `_ring_attention_bwd(axis_name, float32_logits, blockwise_kwargs, res, g)`: The backward pass. Similar structure with `scan_kv_block` iterating over key-value blocks, computing `_blockwise_attention_bwd` for gradients dq, dk, dv. Also uses `lax.ppermute` to rotate key-value blocks and accumulate gradients.
- `ring_attention(q, k, v, attn_bias, axis_name, float32_logits, blockwise_kwargs)`: The main entry point, decorated with `@partial(jax.custom_vjp, nondiff_argnums=[4, 5, 6])`. Calls the forward function and returns the output. Uses `ring_attention.defvjp(_ring_attention_fwd, _ring_attention_bwd)` to register the custom forward and backward passes.

Key implementation details visible in the code:
- Block size is `q_len` (assumes input is pre-sharded inside `shard_map`)
- `axis_size = lax.psum(1, axis_name)` determines the number of devices in the ring
- The scan iterates `axis_size` times, once for each device's key-value block
- Permutation pattern: `perm=[(i, (i + 1) % axis_size) for i in range(axis_size)]` sends each device's block to the next device in the ring
- Gradients are accumulated in float32 (`jnp.float32`) regardless of input dtype
- The forward pass tracks `max_score`, `numerator`, and `denominator` for numerically stable softmax rescaling across blocks
