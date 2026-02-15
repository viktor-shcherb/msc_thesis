# QK-Sniffer: Data Flow

## Inference Pipeline

```
1. YAML Config Load
   ↓
2. Patch Module System (local models/ → transformers.models.*)
   ↓
3. Pull Dataset Repo (if hf_repo_id set)
   ↓
4. Load HF Dataset → Create DataLoader Batches
   ↓
5. Load Model (AutoModelForCausalLM) & Tokenizer
   ↓
6. Activate Sniffer Context → Initialize sampler, saver
   ↓
7. For Each Batch:
   - Set example_ids (normalized: int or Blake2b hash of string)
   - Set sequence_lengths (actual tokens after attention_mask)
   - Tokenize texts → (input_ids, attention_mask)
   - Call model backbone directly (model.model(), skipping lm_head)
     with use_cache=False, attention_mask dropped
   ↓
   During Attention Blocks (for each layer):
   - compute_positions(): Map cache_position or arange to absolute positions
   - get_active_sniffer().capture():
     * Compute bucket IDs on CPU (log₂ or floor division)
     * Generate sampling mask on CPU (deterministic per layer/example/vector_kind)
     * Gather selected vectors for all active heads: (n_heads, K, dim) on GPU
     * Store as _PendingChunk with shared positions/buckets across heads
   ↓
   After each forward pass:
   - flush_batch(): Transfer GPU→CPU (one copy per (layer, kind) chunk)
   - Append to _AccumulatedCapture (per (layer, kind), vectors stay (n_heads, K, dim))
   ↓
8. Close Sniffer → Concatenate accumulated data along K axis
   → Write per-head Parquet files (expand shared metadata per head)
   ↓
9. Push Dataset Repo (if hf_repo_id set, uses hf_branch for branch-per-model)
```

## Storage Layout

Each model is stored on its own branch (`hf_branch` config field):

```
data/attention-plasticity/          # data_root from config
├── l00h00q/
│   └── data.parquet                # Queries from layer 0, head 0
├── l00h00k/
│   └── data.parquet                # Keys from layer 0, head 0
├── l00h01q/
│   └── data.parquet
...
├── l31h31k/
│   └── data.parquet
└── README.md                       # Auto-generated dataset card
```

To load a specific model's data, specify `revision`:
```python
ds = load_dataset("viktoroo/sniffed-qk", "l00h00q",
                   revision="qwen3-8b-longbench-pro-128k-plus")
```

## Parquet Schema

| Column | Type | Description |
|--------|------|-------------|
| `bucket` | int32 | Bucketing ID (log exponent or chunk index) |
| `example_id` | int32 | Batch example identifier |
| `position` | int32 | Token position within sequence |
| `vector` | FixedSizeList[float32] | Attention vector (head_dim floats) |
| `sliding_window` | int32 or null | Sliding window size (local attention) or null (global) |
| `token_str` | string or null | Token string (when `capture_token_strings: true`) |

## Position Tracking for RoPE

Modern models use Rotary Positional Embeddings (RoPE) with `cache_position` tracking during generation. The `compute_positions()` utility handles cache resizing/expansion to match query/key shapes.
