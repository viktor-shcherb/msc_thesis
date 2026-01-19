# QK-Sniffer: Approach and Methodology

## Key Architectural Principles

### 1. Non-Intrusive Instrumentation

Uses Python module patching to inject capture hooks into transformer models without modifying the original HF transformers library. Local copies of model files in `models/` directory are aliased into `transformers.models.*` namespace at runtime.

### 2. Deterministic Sampling

Three sampling strategies ensure reproducible, configurable capture rates:

#### Log-Uniform Sampler (Default)
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
- Bucket ID = 0 for all tokens

### 3. Deduplication

- Maintains in-memory cache of `(example_id, position)` pairs per layer/head/kind
- Prevents duplicate captures across runs
- Enables incremental data collection

### 4. Bucket-Based Organization

Vectors are stored with bucket IDs reflecting temporal position pattern:
- Enables queries like "all vectors from the first 128 tokens"
- Supports geometric position range queries

### 5. Thread-Safe Writing

- Background worker thread with queue-based batching
- Isolates disk I/O from capture compute
- Prevents inference slowdown

## Determinism Implementation

Samplers use fixed seeds based on:
- `example_id`
- `layer_idx`
- `head_idx`
- `vector_kind` (query or key)

Uses SplitMix64 hash mixing and XOR combination for determinism. The exact same tokens are sampled across runs—critical for reproducible research datasets.
