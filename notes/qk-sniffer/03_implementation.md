# QK-Sniffer: Implementation Details

## Project Structure

```
qk-sniffer/
├── sniff.py                    # CLI entry point and main inference orchestrator
├── sniffer/                    # Core capture engine
│   ├── core.py                 # Sniffer class: captures, buckets, deduplicates
│   ├── samplers.py             # Deterministic sampling strategies
│   └── utils.py                # compute_positions() for RoPE position tracking
├── saver/                      # Parquet file management
│   ├── dataset.py              # DatasetSaver: writes to Parquet, manages dedup cache
│   └── readme.py               # DatasetReadme: generates dataset card with metadata
├── models/                     # Instrumented model files
│   ├── llama/modeling_llama.py
│   ├── gemma3/modeling_gemma3.py
│   ├── qwen3/modeling_qwen3.py
│   ├── qwen2/modeling_qwen2.py
│   ├── glm4/modeling_glm4.py
│   └── glm/modeling_glm.py
├── configs/                    # YAML config files for different models/datasets
└── tests/                      # Comprehensive test suite
```

## Key Components

### sniff.py - CLI and Configuration

**SniffConfig** dataclass holds all settings:
- `DatasetSettings`: Dataset path, split, text/id columns, max_samples
- `ModelSettings`: Model name, dtype (float16/bfloat16), device mapping
- `TokenizerSettings`: Tokenizer name, max_length, padding strategy
- `InferenceSettings`: batch_size, autocast_dtype for CUDA
- `CaptureSettings`: capture_queries/keys flags, layer/head filters, sampler config
- `OutputSettings`: data_root, readme_path, hf_repo_id for Hub sync

**Main Functions**:
- `run_inference()`: Orchestrates full pipeline
- `patch_modeling_modules()`: Python module aliasing system
- `pull_remote_dataset()` / `push_remote_dataset()`: Hub sync
- `batch_iter()`: Yields batches with text and normalized example IDs
- `_normalize_example_ids()`: Handles int/string/tensor IDs, hashes strings to int64

### sniffer/core.py - Capture Engine

**Sniffer Class**:
- `capture()`: Called from model attention blocks
  - Input shapes: `query_states, key_states`: (batch, num_heads, seq_len, head_dim)
  - `positions`: (batch, seq_len) - absolute token positions
  - Computes bucket IDs, applies sampler mask, enqueues to writer thread
- `set_example_ids()` / `set_sequence_lengths()`: Called before each batch

**_CaptureWorker Class**: Background thread for async writes

### sniffer/samplers.py - Sampling Strategies

- `LogUniformSampler`: Log₂ bucketing with geometric sampling
- `UniformSampler`: Fixed-width chunks
- `AllSampler`: No subsampling
- `_seed()`: Deterministic hash function for reproducibility

### saver/dataset.py - Storage

**DatasetSaver Class**:
- Manages Parquet writes with deduplication
- Loads existing positions from Parquet headers on startup
- Maintains position cache: `(example_id, position)` pairs
- Flushes to ParquetWriter when pending reaches `write_batch_size`

### saver/readme.py - Dataset Card Generation

- Auto-generates HF dataset card YAML
- Tracks configs, models, bucket distributions
- Generates loading examples for users

## Dependencies

- **PyTorch**: Tensor operations, RNG for sampling
- **Transformers**: Model loading, tokenizer, AutoConfig
- **Datasets**: Dataset loading from Hub
- **PyArrow/Parquet**: Columnar storage
- **YAML**: Config parsing
- **HuggingFace Hub**: Dataset push/pull
- **Accelerate**: Multi-GPU support
- **Python-dotenv**: HF_TOKEN loading
