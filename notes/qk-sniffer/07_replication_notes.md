# QK-Sniffer: Notes for Replication

## Key Insights

### 1. Module Patching is Critical

The system works by inserting local model files into Python's `sys.modules` before importing transformers. This requires:
- `PYTHONPATH=.` or
- `pip install -e .`

### 2. Position Tracking for RoPE

Modern models use Rotary Positional Embeddings (RoPE) with `cache_position` tracking during generation. The `compute_positions()` utility handles cache resizing/expansion to match query/key shapes.

### 3. Deduplication is Incremental

- Position caches are loaded from existing Parquets on saver startup
- Enables safe re-runs without duplicates
- Position cache key is `(example_id, position)` regardless of layer/head

### 4. Determinism is Enforced

Samplers use fixed seeds based on:
- `(example_id, layer_idx, head_idx, vector_kind)`

This ensures exact same tokens are sampled across runs—critical for reproducible research datasets.

### 5. Thread Safety for Performance

- Background writer thread decouples capture from disk I/O
- Queue buffers up to `queue_size` batches before blocking capture
- Flushes in bulk at `write_batch_size` intervals

### 6. Configuration Flexibility

Every major parameter is exposed:
- batch_size, max_length
- sampler type, base_rate, min_bucket_size
- layers, heads filters

Allows experiments from "capture everything" to "sample 1% of long-context tokens."

### 7. Hub Integration is Transparent

- System pulls the repo if it exists
- Syncs captures in-place
- Pushes back with a single commit
- `.sniff_snapshot.json` file tracks repo SHA to avoid redundant pulls

### 8. Dataset Card Auto-Generation

README front matter is regenerated every run:
- Keeps `configs` and `models` lists in sync with actual Parquet files
- Enables immediate use via `load_dataset()`

## Running the Tool

```bash
# Basic usage
python sniff.py --config configs/my_config.yaml

# With environment setup
PYTHONPATH=. python sniff.py --config configs/qwen3.yaml
```

## Loading Captured Data

```python
from datasets import load_dataset

# Load specific layer/head/vector type
ds = load_dataset("viktoroo/sniffed-qk", "l00h00q")

# Access vectors
for row in ds["train"]:
    bucket = row["bucket"]
    position = row["position"]
    vector = row["vector"]  # List of floats (head_dim)
```
