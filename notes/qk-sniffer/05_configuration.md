# QK-Sniffer: Configuration Reference

## Sampler Configuration

| Parameter | Description | Default |
|-----------|-------------|---------|
| `type` | Sampling strategy: `log_uniform`, `uniform`, `all` | `log_uniform` |
| `base_rate` | Sampling rate (1.0 = 100%, 0.5 = 50%) | 1.0 |

## Capture Configuration

| Parameter | Description | Default |
|-----------|-------------|---------|
| `capture_queries` | Capture query vectors | true |
| `capture_keys` | Capture key vectors | true |
| `layers` | Layer indices to capture (null = all) | null |
| `heads` | Head indices to capture (null = all) | null |
| `min_bucket_size` | Minimum bucket width (log) or fixed width (uniform) | 128 |
| `head_sampling.count` | Randomly sample this many query heads across all layers | null |
| `head_sampling.seed` | Deterministic seed for head sampling | 0 |
| `full_attention_only` | Skip sliding-window attention layers | false |
| `capture_pre_rope` | Capture Q/K before rotary embedding | false |
| `capture_token_strings` | Include token strings in output | false |

## Output Configuration

| Parameter | Description |
|-----------|-------------|
| `data_root` | Local directory for Parquet files |
| `readme_path` | Path to dataset card |
| `hf_repo_id` | Hub dataset repo (e.g., viktoroo/sniffed-qk) |
| `hf_branch` | Branch name (one branch per model) |
| `private` | Dataset privacy flag |

## Example YAML Config (Production)

```yaml
dataset:
  path: viktoroo/longbench-pro-128k-plus
  split: test
  text_column: text
  id_column: id
  max_samples: null

model:
  name: Qwen/Qwen3-8B
  dtype: bfloat16
  device_map: auto

tokenizer:
  name: Qwen/Qwen3-8B
  max_length: 131072
  padding: longest

inference:
  batch_size: 1
  autocast_dtype: bfloat16

capture:
  capture_queries: true
  capture_keys: true
  head_sampling:
    count: 300
    seed: 0
  full_attention_only: true
  capture_pre_rope: false
  min_bucket_size: 8192
  sampler:
    type: uniform
    base_rate: 1.0

output:
  data_root: data/attention-plasticity
  hf_repo_id: viktoroo/sniffed-qk
  hf_branch: qwen3-8b-longbench-pro-128k-plus
```
