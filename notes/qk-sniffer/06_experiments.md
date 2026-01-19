# QK-Sniffer: Experiments and Evaluation

## Datasets and Models

### Instrumented Models
- Llama 3
- Gemma 3
- Qwen 2 & 3
- GLM & GLM-4

### Example Datasets
- longbench2-128k-plus (Qwen 3 config: 2048 samples max)
- viktoroo/example (generic example dataset)
- Arbitrary HF datasets (configurable via YAML)

## Sampling Strategies Tested

### 1. Log-Uniform (Default)
- Config: `min_bucket_size=128`, `base_rate=1.0`
- Samples uniformly within log buckets
- Captures position diversity across sequence lengths

### 2. Uniform
- Config: `min_bucket_size=2048` (Qwen3), `base_rate=3.0`
- Fixed-size chunks
- Higher base_rate compensates for longer context

### 3. All
- Captures every token for ground truth
- Used when max_length < actual dataset sequence length

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
  - Deduplication efficiency

## Test Coverage

### test_sniffer.py
- Capture correctness (buckets, positions, batch handling)
- Cache position integration (RoPE position tracking)
- Sampler determinism (same seed produces same mask)
- Head/layer filtering
- Query/key selective capture

### test_saver.py
- Deduplication (within-session, across-session)
- Parquet writes and reads
- README generation with configs and models
- Bucket counting and metadata persistence

### test_cli_workflow.py
- Full end-to-end: config → inference → capture → save
- Hub pull/push order validation
- ID normalization (string hashing)
- Sequence length masking
