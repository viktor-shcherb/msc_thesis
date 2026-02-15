# QK-Sniffer: Notes for Replication

## Key Insights

### 1. Module Patching is Critical

The system works by inserting local model files into Python's `sys.modules` before importing transformers. This requires:
- `PYTHONPATH=.` or
- `pip install -e .`

### 2. Position Tracking for RoPE

Modern models use Rotary Positional Embeddings (RoPE) with `cache_position` tracking during generation. The `compute_positions()` utility handles cache resizing/expansion to match query/key shapes.

### 3. Determinism is Enforced

Samplers use fixed seeds based on:
- `(example_id, layer_idx, vector_kind)`

A single position mask is generated and shared across all heads within a (layer, kind) pair. This ensures identical positions are sampled for every head, which is correct since positions don't vary by head.

### 4. In-Memory Accumulation

- All captures accumulate in RAM during inference — no disk writes until the end
- Data stored per (layer, kind) with shared positions/buckets across heads
- Vectors stored as dense `(n_heads, K, dim)` tensors
- Parquet files written in one shot after inference completes via `write_config_data()`

### 5. Backbone-Only Forward Pass

- Calls `model.model()` (transformer backbone) instead of `model()`, skipping the lm_head
- `use_cache=False` avoids KV cache accumulation
- `attention_mask` dropped to prevent O(n²) 4D causal mask expansion

### 6. Configuration Flexibility

Every major parameter is exposed:
- batch_size, max_length
- sampler type, base_rate, min_bucket_size
- layers, heads filters
- head_sampling (random subset of query heads)
- full_attention_only, capture_pre_rope

### 7. Hub Integration (Branch-per-Model)

- System pulls the repo if it exists (on the model's branch via `hf_branch`)
- Writes Parquet files in-place
- Pushes back with a single commit
- Each model gets its own branch, keeping the main branch clean

### 8. Dataset Card Auto-Generation

README front matter is regenerated every run:
- Keeps `configs` and `models` lists in sync with actual Parquet files
- Enables immediate use via `load_dataset()`

## Infrastructure

- **GPU**: NVIDIA B200 rented on Vast.ai
- **Source code**: https://github.com/viktor-shcherb/qk-sniffer

## Running the Tool

```bash
sniff-qk --config configs/attention-plasticity/qwen3-8b.yaml
```

## Loading Captured Data

```python
from datasets import load_dataset

# Load specific layer/head/vector type from a specific model branch
ds = load_dataset(
    "viktoroo/sniffed-qk",
    "l00h00q",
    revision="qwen3-8b-longbench-pro-128k-plus",
)

# Access vectors
for row in ds["train"]:
    bucket = row["bucket"]
    position = row["position"]
    vector = row["vector"]  # List of floats (head_dim)
```
