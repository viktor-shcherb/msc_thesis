# QK-Sniffer: Experiments and Evaluation

## Datasets and Models

### Instrumented Models
- Gemma 3
- GLM & GLM-4
- Llama 3
- Ministral
- Mllama (Llama 3.2 Vision)
- Qwen 2 & 3
- SmolLM3

### Dataset
- `viktoroo/longbench-pro-128k-plus` (`test` split, 500 examples with 128k+ context)

## Sampling Strategies Tested

### 1. Log-Uniform
- Config: `min_bucket_size=128`, `base_rate=1.0`
- Samples uniformly within log₂ buckets
- Captures position diversity across sequence lengths

### 2. Uniform (Production)
- Config: `min_bucket_size=8192`, `base_rate=1.0`
- Fixed-size chunks of 8192 tokens
- `p_keep = min(1, 1.0 / 8192) ≈ 0.000122`
- Used in all attention-plasticity production configs

### 3. All
- Captures every token with no subsampling
- Bucket ID = floor(position / bucket_size)

## Evaluation Metrics

### Tracked in Dataset
- **Bucket Distribution**: Counter of samples per bucket ID per model (in README)
- **Coverage**:
  - Layer count: how many layers have captures
  - Query head count: how many (layer, head) pairs captured queries
  - Key head count: how many (layer, head) pairs captured keys
- **Metadata**:
  - Source dataset name/split
  - Sampling strategy and parameters

## Test Coverage

### test_sniffer.py
- Capture correctness (buckets, positions, batch handling)
- Cache position integration (RoPE position tracking)
- Sampler determinism (same seed produces same mask)
- Head/layer filtering
- Query/key selective capture
- In-memory accumulation and dense tensor storage

### test_saver.py
- Parquet writes and reads (including `write_config_data()` one-shot path)
- README generation with configs and models
- Bucket counting and metadata persistence

### test_smollm3.py
- Sniffer capture invocation (RoPE layer)
- NoPE layer capture (use_rope=0 still triggers sniffer)
- Pre-RoPE capture mode
- Sliding window value propagation to sniffer
- Forward pass without active sniffer
- End-to-end with real sniffer: mixed RoPE/NoPE layers → parquet output

### test_cli_workflow.py
- Full end-to-end: config → inference → capture → save
- Hub pull/push order validation
- ID normalization (string hashing)
- Sequence length masking
