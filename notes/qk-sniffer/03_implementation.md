# QK-Sniffer: Implementation Details

## Project Structure

```
qk-sniffer/
├── sniff.py                    # CLI entry point, config loading, inference loop
├── sniffer/                    # Core capture engine
│   ├── core.py                 # Sniffer class: capture hooks, in-memory accumulation
│   ├── samplers.py             # Deterministic sampling strategies
│   └── utils.py                # compute_positions() for RoPE position tracking
├── saver/                      # Parquet file management
│   ├── dataset.py              # DatasetSaver: writes Parquet, tracks metadata
│   └── readme.py               # DatasetReadme: generates dataset card
├── models/                     # Instrumented model files
│   ├── gemma3/modeling_gemma3.py
│   ├── glm/modeling_glm.py
│   ├── glm4/modeling_glm4.py
│   ├── llama/modeling_llama.py
│   ├── ministral/modeling_ministral.py
│   ├── mllama/modeling_mllama.py
│   ├── qwen2/modeling_qwen2.py
│   ├── qwen3/modeling_qwen3.py
│   └── smollm3/modeling_smollm3.py
├── configs/                    # YAML config files
│   ├── sample.yaml
│   └── attention-plasticity/   # Production configs for the experiment sweep
└── tests/                      # Test suite
```

## Key Components

### sniff.py - CLI and Configuration

**SniffConfig** dataclass holds all settings:
- `DatasetSettings`: Dataset path, split, text/id columns, max_samples, streaming
- `ModelSettings`: Model name, dtype (float16/bfloat16), device mapping, config_overrides
- `TokenizerSettings`: Tokenizer name, max_length, padding strategy
- `InferenceSettings`: batch_size, autocast_dtype, debug_logging
- `CaptureSettings`: capture_queries/keys flags, layer/head filters, head_sampling, sampler config
- `OutputSettings`: data_root, readme_path, hf_repo_id, hf_branch

**Main Functions**:
- `run_inference()`: Orchestrates full pipeline — calls backbone directly with `use_cache=False`, drops attention_mask
- `patch_modeling_modules()`: Python module aliasing system
- `pull_remote_dataset()` / `push_remote_dataset()`: Hub sync (branch-per-model)
- `batch_iter()`: Yields batches with text and normalized example IDs
- `resolve_head_filters()`: Deterministic head sampling across layers

### sniffer/core.py - Capture Engine

**Data Structures**:
- `_PendingChunk`: One batch item's data — vectors `(n_heads, K, dim)` on GPU + shared CPU positions/buckets/example_id
- `_PendingCapture`: Collects chunks for a (layer, kind) pair within one forward pass
- `_AccumulatedCapture`: Accumulates across all forward passes — vectors `(n_heads, K_i, dim)` per chunk, positions/buckets shared across heads

**Sniffer Class**:
- `capture()`: Called from model attention hooks
  - Input shapes: `query_states, key_states`: (batch, num_heads, seq_len, head_dim)
  - `positions`: (batch, seq_len) - absolute token positions
  - Computes bucket IDs on CPU, samples on CPU, gathers vectors on GPU
- `flush_batch()`: After each forward pass, transfers GPU→CPU, appends to accumulated data
- `close()`: Concatenates all accumulated data, writes per-head Parquet via saver
- `set_example_ids()` / `set_sequence_lengths()`: Called before each batch

### sniffer/samplers.py - Sampling Strategies

- `LogUniformSampler`: Log₂ bucketing with geometric sampling
- `UniformSampler`: Fixed-width chunks
- `AllSampler`: No subsampling
- `sample_positions_batch()`: Returns a shared `(seq_len,)` boolean mask for all heads

### saver/dataset.py - Storage

**DatasetSaver Class**:
- `write_config_data()`: Writes pre-concatenated numpy arrays directly to Parquet in one shot
- `add_batch()`: Row-by-row API (used by tests, not by the optimized path)
- Tracks config names and bucket counts for README generation

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
- **Python-dotenv**: HF_TOKEN loading
