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
6. Activate Sniffer Context → Initialize sampler, saver, writer thread
   ↓
7. For Each Batch:
   - Set example_ids (normalized: int or Blake2b hash of string)
   - Set sequence_lengths (actual tokens after attention_mask)
   - Tokenize texts → (input_ids, attention_mask)
   - Run model forward pass
   ↓
   During Attention Blocks (for each layer):
   - compute_positions(): Map cache_position or arange to absolute positions
   - get_active_sniffer().capture():
     * Compute bucket IDs (log₂ or floor division)
     * Apply sampler mask (deterministic per layer/head/vector_kind)
     * Call sniffer._capture_tensor() for Q and K separately
     * For each head: apply sampler, downsample if needed, enqueue CaptureBatch
   ↓
8. Close Sniffer → Flush all pending, stop writer thread
   ↓
9. Push Dataset Repo (if hf_repo_id set)
```

## Storage Layout

```
data/
└── {sanitized_model_name}/          # e.g., meta_llama3_8b
    ├── l00h00q/
    │   └── data.parquet             # Queries from layer 0, head 0
    ├── l00h00k/
    │   └── data.parquet             # Keys from layer 0, head 0
    ├── l00h01q/
    │   └── data.parquet
    ...
    └── l31h31k/
        └── data.parquet
└── README.md                        # Dataset card (updated each run)
```

## Parquet Schema

| Column | Type | Description |
|--------|------|-------------|
| bucket | int32 | Bucketing ID (log exponent or chunk index) |
| example_id | int32 | Batch example identifier |
| position | int32 | Token position within sequence |
| vector | FixedSizeList[float32] | Attention vector (head_dim floats) |
| sliding_window | int32 or null | Sliding window size (local attention) or null (global) |

## Position Tracking for RoPE

Modern models use Rotary Positional Embeddings (RoPE) with `cache_position` tracking during generation. The `compute_positions()` utility handles cache resizing/expansion to match query/key shapes.
