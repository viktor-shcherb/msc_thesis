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

```
data/{model_name}/
├── l00h00q/data.parquet    ← QK-Sniffer writes, Attention-Plasticity reads
├── l00h00k/data.parquet
├── l00h01q/data.parquet
├── l00h01k/data.parquet
...
└── README.md
```

Both tools use identical path conventions for seamless integration.

## Bucket Systems

### QK-Sniffer: Bucket Assignment

During capture, QK-Sniffer assigns buckets based on sampling strategy:

**Log-Uniform Sampler** (default):
$$\text{bucket}_i = \max(i_{\min}, \lfloor \log_2(p + 1) \rfloor)$$

This creates geometrically-spaced buckets: [1], [2-3], [4-7], [8-15], ...

**Uniform Sampler**:
$$\text{bucket}_i = \lfloor p / \text{bucket\_size} \rfloor$$

### Attention-Plasticity: Bucket Usage

Plasticity computation uses buckets for:

1. **Causal masking**: Query bucket $j$ can only attend to key buckets $c < j$
2. **Statistics aggregation**: Per-bucket mean $\mu_j$ and covariance $\Sigma_j$
3. **Sliding window filtering**: If `sliding_window` is set, only eligible key buckets are considered

## Sliding Window Handling

Models with local attention (e.g., Qwen with ALiBi) have limited context windows.

**QK-Sniffer**: Records `sliding_window` column per query token
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

**QK-Sniffer**: Captures all query heads and all key heads separately
- Queries: `l{L}h{Q}q` for each query head Q
- Keys: `l{L}h{K}k` for each key head K (fewer in GQA)

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
    type: log_uniform
    base_rate: 0.1
    min_bucket: 0
  capture_queries: true
  capture_keys: true
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
1. Run QK-Sniffer on corpus
   └── python sniff.py --config configs/model.yaml
   └── Output: data/{model}/*.parquet uploaded to HF Hub

2. Run Attention-Plasticity analysis
   └── python analyze.py --config configs/model.yaml
   └── Input: Downloads from HF Hub (same dataset)
   └── Output: CSV files with plasticity metrics
```

## Shared Dependencies

Both projects use:
- **PyArrow/Parquet**: Columnar storage format
- **Hugging Face Hub**: Dataset hosting and versioning
- **NumPy**: Array operations
- **Bucket conventions**: Log-uniform or uniform bucketing

## Summary Table

| Aspect | QK-Sniffer | Attention-Plasticity |
|--------|------------|---------------------|
| **Role** | Data collection | Data analysis |
| **Input** | Text corpus + transformer model | Parquet files from QK-Sniffer |
| **Output** | Parquet files (Q/K vectors) | CSV files (plasticity metrics) |
| **Bucket use** | Sampling probability | Statistics aggregation |
| **example_id use** | Document tracking | Same-sequence key pairing |
| **sliding_window use** | Recorded per token | Filters valid attention pairs |
| **Execution** | During inference | Post-hoc analysis |

## Key Insight

The division enables:
1. **One-time capture**: Run QK-Sniffer once per model/corpus
2. **Repeated analysis**: Run Attention-Plasticity with different parameters without re-capturing
3. **Community sharing**: Published datasets can be analyzed by anyone

This separation of concerns makes the research pipeline modular and reproducible.
