# QK-Sniffer: Configuration Reference

## Sampler Configuration

| Parameter | Description | Default |
|-----------|-------------|---------|
| `type` | Sampling strategy: `log_uniform`, `uniform`, `all` | `log_uniform` |
| `base_rate` | Sampling rate (1.0 = 100%, 0.5 = 50%) | 1.0 |
| `min_bucket_size` | Minimum bucket width (log) or fixed width (uniform) | 128 |

## Capture Configuration

| Parameter | Description | Default |
|-----------|-------------|---------|
| `capture_queries` | Capture query vectors | true |
| `capture_keys` | Capture key vectors | true |
| `layers` | Layer indices to capture (null = all) | null |
| `heads` | Head indices to capture (null = all) | null |
| `max_rows_per_batch` | Downsample limit per (layer, head, kind) | - |
| `queue_size` | Background writer thread queue length | - |

## Output Configuration

| Parameter | Description |
|-----------|-------------|
| `data_root` | Local directory and clone target for Hub repo |
| `readme_path` | Path to dataset card |
| `hf_repo_id` | Hub dataset repo (e.g., viktoroo/sniffed-qk) |
| `private` | Dataset privacy flag |
| `write_batch_size` | Rows to accumulate before flushing to Parquet |

## Example YAML Config

```yaml
dataset:
  path: "longbench2-128k-plus"
  split: "test"
  text_column: "context"
  id_column: "id"
  max_samples: 2048

model:
  name: "Qwen/Qwen3-8B"
  dtype: "bfloat16"
  device_map: "auto"

tokenizer:
  name: null  # uses model name
  max_length: 131072
  padding: "max_length"

inference:
  batch_size: 1
  autocast_dtype: "bfloat16"

capture:
  capture_queries: true
  capture_keys: true
  layers: null
  heads: null
  sampler:
    type: "uniform"
    base_rate: 3.0
    min_bucket_size: 2048

output:
  data_root: "./data"
  hf_repo_id: "viktoroo/sniffed-qk"
  private: false
  write_batch_size: 10000
```
