# QK-Sniffer: Approach and Methodology

## Key Architectural Principles

### 1. Non-Intrusive Instrumentation

Uses Python module patching to inject capture hooks into transformer models without modifying the original HF transformers library. Local copies of model files in `models/` directory are aliased into `transformers.models.*` namespace at runtime.

### 2. Deterministic Sampling

Three sampling strategies ensure reproducible, configurable capture rates:

#### Log-Uniform Sampler
- Groups tokens by log₂(position) buckets
- Samples uniformly within each bucket
- Base rate controls overall capture percentage
- Formula: For position p, bucket_i = max(i_min, floor(log₂(p+1)))
- Within bucket i (spanning [2^i, 2^{i+1})): sample with probability = min(1, base_rate / 2^i)

#### Uniform Sampler
- Fixed-width bucketing (e.g., every N tokens)
- Samples deterministically within chunks
- Bucket_i = floor(position / bucket_size)
- Fixed probability = min(1, base_rate / bucket_size) across all buckets

#### All Sampler
- Captures every token with no subsampling
- Bucket ID = floor(position / bucket_size)

### 3. CPU-Side Sampling

All sampling and position selection happens on CPU to avoid GPU synchronization:
- Position masks generated on CPU (instant `nonzero()`)
- Only small index tensors transferred to GPU asynchronously
- Vectors gathered for all active heads at once as a dense `(n_heads, K, dim)` tensor
- Single async GPU→CPU copy per (layer, kind) per batch

### 4. Bucket-Based Organization

Vectors are stored with bucket IDs reflecting temporal position pattern:
- Enables queries like "all vectors from the first 128 tokens"
- Supports geometric position range queries

### 5. In-Memory Accumulation

- All captures accumulate in RAM during inference — no disk writes until the end
- Data stored per (layer, kind) with shared positions/buckets across heads
- Parquet files written in one shot after inference completes
- Sampling ensures dataset sizes stay small enough for in-memory accumulation

### 6. Backbone-Only Forward Pass

- Calls `model.model()` (transformer backbone) instead of `model()`, skipping the lm_head
- Passes `use_cache=False` to avoid KV cache accumulation
- Drops `attention_mask` from inputs to prevent O(n²) 4D causal mask expansion (right-side padding with causal attention is sufficient)

## Determinism Implementation

Samplers use a shared seed per capture call based on:
- `example_id`
- `layer_idx`
- `vector_kind` (query or key)

A single position mask is generated and shared across all heads within a (layer, kind) pair. This ensures identical positions are sampled for every head, which is correct since positions don't vary by head.
