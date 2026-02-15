# SmolLM3 Checkpoint Sniffing: Attention Plasticity Across Training

## Motivation

All other models in the attention-plasticity sweep are sniffed at their final checkpoint only. The SmolLM3 checkpoint experiment adds a **temporal dimension**: how does attention plasticity evolve during pre-training and long-context extension?

This answers questions like:
- Do heads start with high or low plasticity?
- Does plasticity increase, decrease, or stay constant during training?
- How does long-context extension (RoPE theta scaling) affect plasticity?
- Do NoPE (no positional embedding) layers behave differently from RoPE layers over training?

## Source Repository

`HuggingFaceTB/SmolLM3-3B-checkpoints` — 132 branches total, each containing a full model checkpoint. We selected 10 representative checkpoints across the training pipeline.

## SmolLM3 Architecture Notes

- **Model type**: `smollm3` (custom, registered in transformers)
- **Parameters**: 3B
- **Layers**: 36
- **Attention**: GQA with 16 query heads, 4 key value heads (group size = 4)
- **Head dim**: 128 (= 2048 / 16)
- **NoPE pattern**: Every 4th layer has `no_rope_layers[i] = 0` (no RoPE). Layers 3, 7, 11, 15, 19, 23, 27, 31, 35 are NoPE. The remaining 27 layers apply RoPE.
- **Sliding window**: None (all layers are `full_attention`)

## Checkpoint Selection

### Pre-training (stages 1–3)

Steps increment by 40K. Stage boundaries are defined by the branch naming convention.

| Config | Branch | Step | Position in stage |
|--------|--------|------|-------------------|
| `stage1-step-40000` | `stage1-step-40000` | 40K | First (stage 1) |
| `stage1-step-1200000` | `stage1-step-1200000` | 1.2M | ~1/3 (stage 1) |
| `stage1-step-2400000` | `stage1-step-2400000` | 2.4M | ~2/3 (stage 1) |
| `stage1-step-3440000` | `stage1-step-3440000` | 3.44M | Last (stage 1) |
| `stage2-step-4200000` | `stage2-step-4200000` | 4.2M | Last (stage 2) |
| `stage3-step-4720000` | `stage3-step-4720000` | 4.72M | Last (stage 3) |

All six share: `max_position_embeddings=4096`, `rope_theta=50000`.

### Long-context extension

| Config | Branch | Step | Context |
|--------|--------|------|---------|
| `lc-4k-to-32k-step-4000` | `lc-4k-to-32k-step-4000` | 4K | 4K→32K (first) |
| `lc-4k-to-32k-step-20000` | `lc-4k-to-32k-step-20000` | 20K | 4K→32K (last) |
| `lc-32k-to-64k-step-4000` | `lc-32k-to-64k-step-4000` | 4K | 32K→64K (first) |
| `lc-32k-to-64k-step-20000` | `lc-32k-to-64k-step-20000` | 20K | 32K→64K (last) |

Context extension changes RoPE theta and max position embeddings:
- 4K→32K: `rope_theta=2000000`, `max_position_embeddings=32768`
- 32K→64K: `rope_theta=5000000`, `max_position_embeddings=65536`

## Capture Configuration Differences from Other Models

| Parameter | Other models | SmolLM3 (stages 1–3) | SmolLM3 (lc 4k→32k) | SmolLM3 (lc 32k→64k) |
|-----------|-------------|----------------------|----------------------|----------------------|
| `max_length` | 131072 | 4096 | 32768 | 65536 |
| `min_bucket_size` | 8192 | 256 | 2048 | 4096 |
| `model.revision` | `main` | checkpoint branch | checkpoint branch | checkpoint branch |
| `tokenizer.name` | same as model | `HuggingFaceTB/SmolLM3-3B` | `HuggingFaceTB/SmolLM3-3B` | `HuggingFaceTB/SmolLM3-3B` |

The `min_bucket_size` is set to `max_length / 16` for each stage, matching the ratio used for other models (8192 = 131072 / 16).

The tokenizer points to the main model repo (`HuggingFaceTB/SmolLM3-3B`) because `prepare_tokenizer()` does not pass a `revision` parameter, and the `main` branch of the checkpoints repo contains only a README.

## Implementation: models/smollm3/

The SmolLM3 sniffer integration follows the same pattern as other models (Llama, Qwen3, etc.) but handles the NoPE layer pattern:

```python
# In SmolLM3Attention.forward():

# 1. Q/K projection
query_states = self.q_proj(hidden_states).view(hidden_shape).transpose(1, 2)
key_states = self.k_proj(hidden_states).view(hidden_shape).transpose(1, 2)

# 2. Pre-RoPE capture (if configured)
sniffer = get_active_sniffer()
if sniffer is not None and capture_pre_rope:
    sniffer.capture(...)

# 3. Conditional RoPE — skipped for NoPE layers
if self.use_rope:
    query_states, key_states = apply_rotary_pos_emb(query_states, key_states, cos, sin)

# 4. Post-RoPE capture (default)
if sniffer is not None and not capture_pre_rope:
    sniffer.capture(...)
```

For NoPE layers, step 3 is skipped, so the "post-RoPE" capture at step 4 captures the raw projected vectors (identical to pre-RoPE). This is correct behavior — these layers genuinely have no positional encoding applied to Q/K.

## Analysis Considerations

When analyzing SmolLM3 plasticity results, keep in mind:

1. **NoPE vs RoPE layers**: 9 of 36 layers have no positional encoding. These layers' plasticity should be compared separately from RoPE layers — they lack the positional component entirely, which affects the regression fit in `attention_plasticity`.

2. **Context length mismatch**: Pre-training checkpoints have 4K context but are evaluated on 128K+ texts (truncated to 4K). Long-context checkpoints see more of each document. This means bucket counts and position distributions differ across stages.

3. **Bucket granularity**: With `min_bucket_size=256` and `max_length=4096`, pre-training checkpoints have at most 16 buckets. Long-context checkpoints (32K, 64K) have 16 buckets as well (32768/2048 = 16, 65536/4096 = 16), maintaining comparable granularity.

4. **Cross-stage comparability**: Plasticity values across stages are comparable for the same layer/head, since the model architecture stays constant — only weights and RoPE parameters change.
