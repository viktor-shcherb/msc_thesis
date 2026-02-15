# Relationship Between QK-Sniffer and Attention-Plasticity

## Overview

**QK-Sniffer** and **Attention-Plasticity** form a two-stage research pipeline:

```
┌────────────────────┐         ┌────────────────────────┐
│    QK-Sniffer      │         │  Attention-Plasticity  │
│  (Data Collection) │ ──────▶ │     (Analysis)         │
└────────────────────┘         └────────────────────────┘
      Upstream                        Downstream
```

- **QK-Sniffer**: Captures query/key vectors from transformer models during inference
- **Attention-Plasticity**: Analyzes those vectors to quantify positional vs. semantic attention patterns

## Data Flow

### QK-Sniffer Output = Attention-Plasticity Input

QK-Sniffer produces Parquet files with this schema:

| Column | Type | Description |
|--------|------|-------------|
| `bucket` | int32 | Position bucket (log₂ or uniform) |
| `example_id` | int32 | Document/sequence identifier |
| `position` | int32 | Token position in sequence |
| `vector` | list[float32] | Q or K embedding vector |
| `sliding_window` | int32/null | Context window constraint |

Attention-Plasticity consumes this exact format:
- Reads `l{layer}h{head}q/data.parquet` for queries
- Reads `l{layer}h{head}k/data.parquet` for keys

### Storage Layout Compatibility

Each model's data lives on its own Hub branch (`hf_branch`):

```
data/attention-plasticity/          # data_root
├── l00h00q/data.parquet    ← QK-Sniffer writes, Attention-Plasticity reads
├── l00h00k/data.parquet
├── l00h01q/data.parquet
├── l00h01k/data.parquet
...
└── README.md
```

To load a specific model's data:
```python
ds = load_dataset("viktoroo/sniffed-qk", "l00h00q",
                   revision="qwen3-8b-longbench-pro-128k-plus")
```

Both tools use identical path conventions for seamless integration.

## Bucket Systems

### QK-Sniffer: Bucket Assignment

During capture, QK-Sniffer assigns buckets based on sampling strategy:

**Log-Uniform Sampler** (default):
$$\text{bucket}_i = \max(i_{\min}, \lfloor \log_2(p + 1) \rfloor)$$

This creates geometrically-spaced buckets: [1], [2-3], [4-7], [8-15], ...

**Uniform Sampler** (used in production):
$$\text{bucket}_i = \lfloor p / \text{bucket\_size} \rfloor$$

Production config: `min_bucket_size: 8192`, `base_rate: 1.0`

### Attention-Plasticity: Bucket Usage

Plasticity computation uses buckets for:

1. **Causal masking**: Query bucket $j$ can only attend to key buckets $c < j$
2. **Statistics aggregation**: Per-bucket mean $\mu_j$ and covariance $\Sigma_j$
3. **Sliding window filtering**: If `sliding_window` is set, only eligible key buckets are considered

## Sliding Window Handling

Models with local attention (e.g., Ministral with sliding window) have limited context windows.

**QK-Sniffer**: Records `sliding_window` column per vector
**Attention-Plasticity**: Uses this to filter key buckets:

```python
# For query at position p with sliding_window w:
# Only consider keys at positions in [p - w, p]
eligible_key_buckets = [c for c in key_buckets if within_window(c, q_bucket, window)]
```

This ensures plasticity is computed only for valid attention pairs.

## Example ID Semantics

**QK-Sniffer**: Assigns `example_id` per document/sequence (via hash or integer ID)

**Attention-Plasticity**: Uses `example_id` for:
- **Key pair sampling**: Only pairs keys from the *same* sequence
- This ensures comparisons are within-document (semantically meaningful)

```python
# In plasticity.py:
# Sample key pairs (k1, k2) where example_id[k1] == example_id[k2]
```

## Grouped Query Attention (GQA)

**QK-Sniffer**: Captures sampled query heads and their corresponding key heads
- Queries: `l{L}h{Q}q` for each sampled query head Q
- Keys: `l{L}h{K}k` for each corresponding key head K (fewer in GQA)

**Attention-Plasticity**: Maps query heads to key heads:
```python
k_head = q_head // (num_q_heads // num_k_heads)
```

Example (Qwen3-8B: 32 query heads, 8 key heads):
- Query heads 0-3 all use key head 0
- Query heads 4-7 all use key head 1
- etc.

## Configuration Alignment

### QK-Sniffer Config (capture)
```yaml
capture:
  sampler:
    type: uniform
    base_rate: 1.0
  min_bucket_size: 8192
  capture_queries: true
  capture_keys: true
  head_sampling:
    count: 300
    seed: 0
  full_attention_only: true
  capture_pre_rope: false
```

### Attention-Plasticity Config (analysis)
```yaml
analysis:
  dataset_name: viktoroo/sniffed-qk  # Same as QK-Sniffer output
  num_layers: 32
  num_q_heads: 32
  num_k_heads: 8  # Must match QK-Sniffer model
```

## Pipeline Execution Order

```
1. Run QK-Sniffer on corpus (B200 GPU on Vast.ai)
   └── sniff-qk --config configs/attention-plasticity/qwen3-8b.yaml
   └── Output: data/attention-plasticity/*.parquet uploaded to HF Hub (model's branch)

2. Run Attention-Plasticity analysis
   └── python analyze.py --config configs/model.yaml
   └── Input: Downloads from HF Hub (same dataset, specific branch/revision)
   └── Output: CSV files with plasticity metrics
```

## Shared Dependencies

Both projects use:
- **PyArrow/Parquet**: Columnar storage format
- **Hugging Face Hub**: Dataset hosting and versioning (branch-per-model)
- **NumPy**: Array operations
- **Bucket conventions**: Uniform bucketing (production)

## Summary Table

| Aspect | QK-Sniffer | Attention-Plasticity |
|--------|------------|---------------------|
| **Role** | Data collection | Data analysis |
| **Input** | Text corpus + transformer model | Parquet files from QK-Sniffer |
| **Output** | Parquet files (Q/K vectors) | CSV files (plasticity metrics) |
| **Bucket use** | Sampling probability | Statistics aggregation |
| **example_id use** | Document tracking | Same-sequence key pairing |
| **sliding_window use** | Recorded per vector | Filters valid attention pairs |
| **Execution** | During inference (B200 GPU) | Post-hoc analysis |

## Key Insight

The division enables:
1. **One-time capture**: Run QK-Sniffer once per model/corpus
2. **Repeated analysis**: Run Attention-Plasticity with different parameters without re-capturing
3. **Community sharing**: Published datasets can be analyzed by anyone

This separation of concerns makes the research pipeline modular and reproducible.
