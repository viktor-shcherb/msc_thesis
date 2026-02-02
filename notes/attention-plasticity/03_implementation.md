# Attention Plasticity: Implementation Details

## Project Structure

```
attention-plasticity/
├── analyze.py                      # CLI entry point, parallel execution orchestrator
├── attention_plasticity/           # Core analysis module
│   ├── config.py                   # RunnerConfig dataclass, YAML loading
│   ├── head_analysis.py            # Per-head analysis pipeline
│   ├── plasticity.py               # Core plasticity computation
│   └── statistics.py               # Linear regression, rotation, normality tests
├── configs/                        # Model-specific YAML configurations
│   ├── smollm2_135m.yaml
│   ├── qwen3_8b.yaml
│   └── ...
├── scripts/                        # Visualization scripts
│   ├── plot_plasticity.py
│   ├── plot_bucket_heatmap.py
│   └── plot_component_weights.py
└── tests/                          # Test suite
```

## Core Components

### 1. Configuration (`config.py`)

**RunnerConfig** dataclass parameters:

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `model_dir` | str | — | Base dataset directory |
| `num_layers` | int | — | Transformer layers to analyze |
| `num_q_heads` | int | — | Query heads per layer |
| `num_k_heads` | int | — | Key heads per layer (GQA support) |
| `max_tokens_per_head` | int | 50000 | Token sampling cap |
| `normality_max_dims` | int | 64 | Max dims for KS tests |
| `p_alpha` | float | 0.01 | Significance level |
| `seed` | int | 0 | RNG seed |
| `output_csv` | str | `head_metrics.csv` | Per-head metrics output |
| `bucket_csv` | str | `head_bucket_plasticity.csv` | Per-bucket output |
| `component_csv` | str | `head_component_information.csv` | Component weights output |
| `max_workers` | int | CPU count | Parallelism |
| `dataset_name` | str | `viktoroo/sniffed-qk` | HF dataset ID |

### 2. Head Analysis Pipeline (`head_analysis.py`)

**Function**: `analyze_head(layer, q_head, k_head, ...)`

**Pipeline Steps**:

1. **Data Loading**
   - Query: `l{layer:02d}h{q_head:02d}q/data.parquet`
   - Key: `l{layer:02d}h{k_head:02d}k/data.parquet`
   - Supports GQA: query heads map to key heads via `floor(q_head / group_size)`

2. **Orientation Alignment**
   - `orientation_from_keys()`: Per-dimension sign alignment using key bucket means
   - Ensures canonical orientation across runs

3. **Position → Query Regression**
   - Fit: $X_q = \alpha + \beta \cdot \text{position} + R$
   - Output: $\alpha$, $\beta$, per-component $R^2$, overall $R^2$

4. **Rotation to Positional Basis**
   - Construct $H$ via Householder reflection on $\beta$
   - Apply: $X_q^{\text{rot}} = X_q H$, $X_k^{\text{rot}} = X_k H$

5. **Residual Analysis** (rotated space)
   - Refit regression in rotated space
   - Compute residual variance per dimension
   - Test normality of first component and semantic subspace

6. **Plasticity Computation**
   - Call `compute_attention_plasticity()` with rotated embeddings and fitted parameters

7. **Component Weights**
   - Positive-clipped $R^2$: $R^2_+ = \max(R^2_d, 0)$
   - Normalize: $w_d = R^2_d^+ / \sum_d R^2_d^+$

### 3. Plasticity Computation (`plasticity.py`)

**Function**: `compute_attention_plasticity(p_q, b_q, X_q_rot, alpha_rot, beta_rot, resid_var, p_k, b_k, example_ids_k, X_k_rot, num_pairs_per_bucket, bucket_window_limits)`

**Algorithm**:

```python
# 1. Compute bucket statistics
for each query_bucket j > 0:
    tau_j = mean(positions in bucket j)
    mu_j = mean(semantic components in bucket j)  # dims 1:
    Sigma_j = covariance(semantic components) + epsilon * I

# 2. For each (query_bucket, key_bucket) pair
for q_bucket in query_buckets:
    for k_bucket in eligible_key_buckets:  # k_bucket < q_bucket, within window

        # 3. Sample key pairs from same example
        pairs = sample_key_pairs(k_bucket, num_pairs_per_bucket)

        for (k1, k2) in pairs:
            # 4. Compute key difference
            delta_k = k1 - k2
            delta_k1 = delta_k[0]      # positional component
            delta_k_perp = delta_k[1:]  # semantic components

            # 5. Compute mean and variance
            mu = delta_k1 * (alpha + beta * tau_j) + delta_k_perp @ mu_j
            var = delta_k1**2 * sigma**2 + delta_k_perp @ Sigma_j @ delta_k_perp

            # 6. Standardize and compute plasticity
            z = mu / sqrt(var)
            p = Phi(z)  # normal CDF
            plasticity = 4 * p * (1 - p)

        # 7. Average over pairs
        bucket_plasticity = mean(plasticities)

# 8. Aggregate to head level
head_plasticity = weighted_average(bucket_plasticities, weights=bucket_sizes)
```

**Numerical Stability**:
- Covariance regularization: $\Sigma + 10^{-12} I$
- Variance floor: if $v \leq 0$, set $v = 10^{-12}$
- Skip buckets with < 2 samples (no covariance)

### 4. Statistics Utilities (`statistics.py`)

**Linear Regression**: `fit_multioutput_linear_regressor(t, X)`
- Vectorized OLS for all dimensions simultaneously
- Returns: $\alpha$, $\beta$, per-component $R^2$, overall $R^2$

**Rotation Matrix**: `make_pos_rotation(beta)`
- Householder reflection mapping $\beta/\|\beta\|$ to $e_1$
- Returns orthogonal matrix $H$

**Normality Tests**:
- `compute_first_component_residual_stats()`: skewness, kurtosis, KS p-value for first dimension
- `compute_noise_normality_stats()`: median statistics across semantic dimensions

**Position Predictability**: `compute_scalar_position_predictability(p, X, beta)`
- Projects onto $\beta$ direction, predicts $\log_2(p+1)$
- Returns $R^2$, baseline MAE, projection MAE

## Execution Flow

```
┌─────────────────────────────────────────────────────────────┐
│                      analyze.py (CLI)                       │
│  - Load config, resolve paths                               │
│  - Download dataset from HF Hub                             │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│         ProcessPoolExecutor (max_workers processes)         │
│  For each (layer, q_head, k_head):                          │
│    Submit analyze_head() to worker pool                     │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│              Per-Worker: analyze_head()                     │
│  1. Load Q/K parquet files                                  │
│  2. Subsample if > max_tokens_per_head                      │
│  3. Fit regression, rotate, compute plasticity              │
│  4. Return: row dict, bucket rows, component rows           │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                  Collect & Write Results                    │
│  - head_metrics.csv: 1 row per head                         │
│  - head_bucket_plasticity.csv: per-bucket breakdown         │
│  - head_component_weights.csv: positional info weights      │
└─────────────────────────────────────────────────────────────┘
```

## Output Schema

### head_metrics.csv

| Column | Description |
|--------|-------------|
| `layer`, `q_head`, `k_head` | Head identifier |
| `n_q_tokens`, `n_k_tokens` | Token counts |
| `d_model` | Embedding dimension |
| `q_R2_pos` | Overall $R^2$ of position → query regression |
| `q_R2_scalar` | $R^2$ of scalar projection predictability |
| `q_mae_baseline`, `q_mae_proj`, `q_mae_ratio` | MAE comparison |
| `q_resid0_skew`, `q_resid0_kurt`, `q_resid0_ks_p` | First-component normality |
| `q_noise_med_abs_skew`, `q_noise_med_abs_kurt` | Semantic subspace normality |
| `q_noise_med_ks_p`, `q_noise_frac_ks_p_lt_alpha` | KS test results |
| `ap_overall` | **Head-level attention plasticity** |

### head_bucket_plasticity.csv

| Column | Description |
|--------|-------------|
| `layer`, `q_head`, `k_head` | Head identifier |
| `q_bucket`, `k_bucket` | Bucket pair |
| `plasticity` | Bucket-level plasticity |
| `n_pairs` | Number of key pairs sampled |

### head_component_weights.csv

| Column | Description |
|--------|-------------|
| `layer`, `q_head`, `k_head` | Head identifier |
| `component` | Dimension index |
| `weight` | Share of positional information |

## Seeding Strategy

Deterministic seeds ensure reproducibility:

- **Token subsampling**: `seed` (from config)
- **Normality dimension selection**: `seed`
- **Plasticity key pair sampling**: `seed + 10007*layer + 379*q_head`

## GQA (Grouped Query Attention) Support

For models with fewer key heads than query heads:

```python
group_size = num_q_heads // num_k_heads
k_head = q_head // group_size
```

Example: Qwen3-8B has 32 query heads, 8 key heads → group size = 4
- Query heads 0-3 → Key head 0
- Query heads 4-7 → Key head 1
- etc.
