# Post-RoPE Q/K Capture Protocol (Attention-Plasticity Sweep)

## Purpose
This document specifies the exact Q/K capture setup used in the attention-plasticity experiments so results are reproducible.

## Infrastructure
- **GPU**: NVIDIA B200 rented on Vast.ai
- **Source code**: https://github.com/viktor-shcherb/qk-sniffer
- **Dataset**: `viktoroo/longbench-pro-128k-plus` — 500 examples from LongBench Pro with 128k+ context length

## Fixed Capture Setup
All configs in `configs/attention-plasticity/` use the same capture policy:

- Dataset: `viktoroo/longbench-pro-128k-plus` (`test` split, 500 examples)
- Capture tensors: queries and keys (`capture_queries: true`, `capture_keys: true`)
- Attention scope: full-attention layers only (`full_attention_only: true`)
- RoPE stage: post-RoPE only (`capture_pre_rope: false`)
- Head sampling: `count: 300`, `seed: 0`
- Token-position sampling: `sampler.type: uniform`, `min_bucket_size: 8192`, `base_rate: 1.0`
- Dtype: `model.dtype: bfloat16`, `inference.autocast_dtype: bfloat16`
- Inference: `batch_size: 1`
- Tokenizer: `max_length: 131072`, `padding: longest`

### Effective per-token sampling probability
With uniform sampling:
- `bucket = floor(position / 8192)`
- `p_keep = min(1, base_rate / 8192) = 1.0 / 8192 ≈ 0.000122`

## Model Set
### Ministral 3
- `mistralai/Ministral-3-3B-Base-2512`
- `mistralai/Ministral-3-8B-Base-2512`
- `mistralai/Ministral-3-14B-Base-2512`

### Llama 3.2
- `meta-llama/Llama-3.2-1B`
- `meta-llama/Llama-3.2-3B`
- `meta-llama/Llama-3.2-11B-Vision`

### Qwen 3
- `Qwen/Qwen3-0.6B`
- `Qwen/Qwen3-1.7B`
- `Qwen/Qwen3-4B`
- `Qwen/Qwen3-8B`
- `Qwen/Qwen3-14B`

Qwen3 configs additionally set YaRN RoPE scaling:

```yaml
config_overrides:
  rope_scaling:
    rope_type: yarn
    factor: 4.0
    original_max_position_embeddings: 32768
```

### SmolLM3 3B (Training Checkpoints)

Source: `HuggingFaceTB/SmolLM3-3B-checkpoints` — each checkpoint is stored as a separate branch.

SmolLM3 uses a **NoPE (No Position Embedding)** pattern: 3 out of every 4 layers apply RoPE, while the 4th layer has no positional encoding (`no_rope_layers` config). All layers use full attention (no sliding window in the checkpointed configs).

Configs are in `configs/attention-plasticity/smollm3-checkpoints/`.

**Stage 1 (pre-training)** — 4 checkpoints spanning steps 40K–3.44M:
- `stage1-step-40000` (first)
- `stage1-step-1200000` (~1/3)
- `stage1-step-2400000` (~2/3)
- `stage1-step-3440000` (last)

**Stage 2 (continued pre-training)** — 1 checkpoint:
- `stage2-step-4200000` (last)

**Stage 3 (continued pre-training)** — 1 checkpoint:
- `stage3-step-4720000` (last)

Stages 1–3 all have `max_position_embeddings: 4096`, `rope_theta: 50000`. Tokenizer `max_length` is set to 4096 and `min_bucket_size` to 256 (= 4096/16).

**Long-context extension: 4K→32K** — 2 checkpoints:
- `lc-4k-to-32k-step-4000` (first)
- `lc-4k-to-32k-step-20000` (last)

These have `max_position_embeddings: 32768`, `rope_theta: 2000000`. Tokenizer `max_length: 32768`, `min_bucket_size: 2048`.

**Long-context extension: 32K→64K** — 2 checkpoints:
- `lc-32k-to-64k-step-4000` (first)
- `lc-32k-to-64k-step-20000` (last)

These have `max_position_embeddings: 65536`, `rope_theta: 5000000`. Tokenizer `max_length: 65536`, `min_bucket_size: 4096`.

Tokenizer is loaded from `HuggingFaceTB/SmolLM3-3B` (main model repo) because the checkpoints repo's `main` branch has no tokenizer files and `prepare_tokenizer` does not support `revision`.

## Post-RoPE Capture Guarantee
Capture happens after rotary embedding is applied when `capture_pre_rope=false`.

Implementation points:
- Llama: `models/llama/modeling_llama.py:270`, then capture at `models/llama/modeling_llama.py:272`
- Mllama: `models/mllama/modeling_mllama.py:68`, then capture at `models/mllama/modeling_mllama.py:70`
- Ministral: `models/ministral/modeling_ministral.py:188`, then capture at `models/ministral/modeling_ministral.py:190`
- Qwen3: `models/qwen3/modeling_qwen3.py:234`, then capture at `models/qwen3/modeling_qwen3.py:236`

The pre-RoPE branch exists but is disabled by config (`capture_pre_rope: false`) in all attention-plasticity YAMLs.

### SmolLM3 NoPE Layer Handling
SmolLM3 has a per-layer `use_rope` flag (derived from `no_rope_layers` config). For NoPE layers (`use_rope=0`), no rotary embedding is applied — Q/K are captured directly after linear projection. This means for these layers the captured vectors are inherently "pre-RoPE" (since there is no RoPE to apply). The `capture_pre_rope` flag still controls timing: when false, capture happens after the conditional RoPE block regardless.

## Family-Specific Tensor Particularities (within this protocol)

### Llama path
- Q/K are captured post-RoPE from projected query/key states.

Reference:
- `models/llama/modeling_llama.py:245`
- `models/llama/modeling_llama.py:266`

### Mllama path (Llama-3.2-11B-Vision)
- Q/K are captured post-RoPE from text self-attention (`MllamaTextSelfAttention`).
- Capture hook is applied via the local patch module `models/mllama/modeling_mllama.py`.

Reference:
- `models/mllama/modeling_mllama.py:39`
- `models/mllama/modeling_mllama.py:68`
- `models/mllama/modeling_mllama.py:70`

### Ministral path
- Q/K are captured post-RoPE from projected query/key states.

Reference:
- `models/ministral/modeling_ministral.py:148`
- `models/ministral/modeling_ministral.py:196`

### Qwen3 path
- Q/K are RMS-normalized per head before RoPE (`q_norm`, `k_norm`).
- Captured tensors are post-RoPE (and therefore post q/k normalization).

Reference:
- `models/qwen3/modeling_qwen3.py:192`
- `models/qwen3/modeling_qwen3.py:209`
- `models/qwen3/modeling_qwen3.py:242`

### SmolLM3 path
- Q/K are captured post-RoPE for RoPE layers, and directly after linear projection for NoPE layers.
- NoPE layers (every 4th layer, `no_rope_layers[i] == 0`) skip `apply_rotary_pos_emb` entirely.
- `sliding_window` is `None` for all layers in the checkpoint configs (no sliding window).

Reference:
- `models/smollm3/modeling_smollm3.py` — `SmolLM3Attention.forward()`

## Head-Sampling Definition Used Here
Head sampling is query-head driven:
- Sample up to 300 query heads globally across eligible layers using seed 0.
- Key heads are derived from selected query heads using grouped-query mapping:
  - `queries_per_key = num_query_heads / num_key_value_heads`
  - `key_head = floor(query_head / queries_per_key)`

## Output Schema Used in This Sweep
Each kept vector row includes:
- `bucket`
- `example_id`
- `position`
- `vector` (float32 in saved parquet)
- `sliding_window` (int32 or null)

Data is stored on per-model branches (`hf_branch`) with configs named `lXXhYYq` / `lXXhYYk`.

## Hub Organization
Each model's data is pushed to its own branch:
- `qwen3-8b-longbench-pro-128k-plus`
- `llama-3.2-1b-longbench-pro-128k-plus`
- etc.

This keeps the main branch clean and allows independent model updates.

## Reproducibility Checklist
1. Use configs from `configs/attention-plasticity/` as committed.
2. Verify each file has `capture_pre_rope: false`.
3. Run with `sniff-qk --config <file>`.
4. Keep `transformers` patching from this repo enabled (default in `run_inference`).
5. Do not change model revisions, sampling parameters, or tokenizer max length.
