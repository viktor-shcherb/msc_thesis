# Attention Plasticity: Mathematical Framework

## 1. Score Difference Formulation

For a query $q$ and two keys $k_1, k_2$, the attention score difference is:

$$D = s(k_1; q) - s(k_2; q) = q^\top k_1 - q^\top k_2 = q^\top(k_1 - k_2) = q^\top \Delta k$$

where $\Delta k = k_1 - k_2$ is the key difference vector.

Key 1 "wins" (receives higher attention weight) when $D > 0$.

## 2. Query Model in Rotated Space

After applying an orthogonal rotation $H$ that aligns the positional trend with the first coordinate axis, queries decompose as:

$$q = \begin{pmatrix} q_1 \\ q_\perp \end{pmatrix}$$

where:
- **First component (positional)**: $q_1 = \alpha + \beta t + \varepsilon$, with $\varepsilon \sim \mathcal{N}(0, \sigma^2)$
- **Remaining components (semantic)**: $q_\perp \sim \mathcal{N}(\mu_b, \Sigma_b)$ (bucket-dependent)

Here:
- $t$ = token position
- $\alpha$ = intercept (baseline positional encoding)
- $\beta$ = slope (positional drift rate)
- $\sigma^2$ = residual variance in positional component
- $\mu_b, \Sigma_b$ = mean and covariance of semantic components for bucket $b$

**Assumption**: The noise $\varepsilon$ is independent of $q_\perp$.

## 3. Score Difference Distribution

Decomposing the key difference similarly:

$$\Delta k = \begin{pmatrix} \Delta k_1 \\ \Delta k_\perp \end{pmatrix}$$

The score difference becomes:

$$D = q^\top \Delta k = \Delta k_1 \cdot q_1 + \Delta k_\perp^\top q_\perp$$

Since both terms are linear combinations of Gaussians, $D$ is Gaussian:

$$D \mid t \sim \mathcal{N}(m(t), v)$$

### Conditional Mean

$$m(t) = \Delta k_1 \cdot (\alpha + \beta t) + \Delta k_\perp^\top \mu_b$$

This captures:
- Positional contribution: $\Delta k_1 \cdot (\alpha + \beta t)$
- Semantic contribution: $\Delta k_\perp^\top \mu_b$

### Conditional Variance

$$v = (\Delta k_1)^2 \sigma^2 + \Delta k_\perp^\top \Sigma_b \Delta k_\perp$$

This captures:
- Positional noise contribution: $(\Delta k_1)^2 \sigma^2$
- Semantic variability contribution: $\Delta k_\perp^\top \Sigma_b \Delta k_\perp$

**Note**: The variance is position-independent (homoscedastic).

## 4. Key Preference Probability

The probability that key 1 beats key 2 at position $t$:

$$p(t) = \Pr(D > 0 \mid t) = \Pr\left(\frac{D - m(t)}{\sqrt{v}} > \frac{-m(t)}{\sqrt{v}}\right) = \Phi\left(\frac{m(t)}{\sqrt{v}}\right)$$

where $\Phi$ is the standard normal CDF.

### Standardized Score (z-score)

$$z(t) = \frac{m(t)}{\sqrt{v}} = \frac{\Delta k_1(\alpha + \beta t) + \Delta k_\perp^\top \mu_b}{\sqrt{(\Delta k_1)^2\sigma^2 + \Delta k_\perp^\top \Sigma_b \Delta k_\perp}}$$

Thus: $p(t) = \Phi(z(t))$

## 5. Attention Plasticity Formula

For a single key pair at position $t$:

$$\boxed{\text{Plasticity}(t) = 4 \cdot p(t) \cdot (1 - p(t)) = 4 \cdot \Phi(z(t)) \cdot (1 - \Phi(z(t)))}$$

This is the **Bernoulli variance** formula scaled to $[0, 1]$:
- **Maximum** ($= 1.0$) when $p(t) = 0.5$ (i.e., $z(t) = 0$): maximum uncertainty
- **Minimum** ($\approx 0.0$) when $p(t) \approx 0$ or $p(t) \approx 1$: deterministic outcome

### Interpretation

| $z(t)$ | $p(t) = \Phi(z)$ | Plasticity | Meaning |
|--------|------------------|------------|---------|
| $-\infty$ | 0 | 0 | Key 2 always wins |
| $-2$ | 0.023 | 0.09 | Key 2 usually wins |
| $-1$ | 0.159 | 0.53 | Key 2 often wins |
| $0$ | 0.5 | 1.0 | Maximally uncertain |
| $1$ | 0.841 | 0.53 | Key 1 often wins |
| $2$ | 0.977 | 0.09 | Key 1 usually wins |
| $+\infty$ | 1 | 0 | Key 1 always wins |

## 6. Aggregation Hierarchy

### Bucket-Level Plasticity

For query bucket $j$ with representative position $\tau_j$, average over sampled key pairs:

$$\text{AP}_j = \frac{1}{|S_j|} \sum_{(k_1, k_2) \in S_j} 4 \cdot \Phi(z_j) \cdot (1 - \Phi(z_j))$$

where $S_j$ is the set of sampled key pairs for bucket $j$.

### Head-Level Plasticity

Weighted average across query buckets:

$$\text{AP}_{\text{head}} = \frac{\sum_j w_j \cdot \text{AP}_j}{\sum_j w_j}$$

where $w_j$ = number of queries in bucket $j$ (bucket size weight).

## 7. Rotation Construction

The orthogonal rotation matrix $H$ is constructed via **Householder reflection**:

Given the positional slope vector $\beta$ from linear regression $X \approx \alpha + \beta t$:

1. Normalize: $\hat{\beta} = \beta / \|\beta\|$
2. Target: first standard basis vector $e_1 = (1, 0, \ldots, 0)^\top$
3. Householder vector: $u = \hat{\beta} - e_1$
4. If $\|u\| \approx 0$: $H = I$ (identity)
5. Otherwise: $H = I - 2\frac{uu^\top}{\|u\|^2}$

This ensures $H\hat{\beta} = e_1$, so the positional direction becomes the first coordinate.

**Properties**:
- $H$ is orthogonal: $H^\top H = I$
- $H$ is symmetric: $H^\top = H$
- $H$ is involutory: $H^2 = I$

## 8. Linear Regression for Positional Parameters

Fit query embeddings to position:

$$X_{i,d} = \alpha_d + \beta_d \cdot t_i + R_{i,d}$$

### Ordinary Least Squares Solution

$$\beta_d = \frac{\sum_i (t_i - \bar{t})(X_{i,d} - \bar{X}_d)}{\sum_i (t_i - \bar{t})^2} = \frac{\text{Cov}(t, X_d)}{\text{Var}(t)}$$

$$\alpha_d = \bar{X}_d - \beta_d \bar{t}$$

### Residual Variance

$$\sigma^2_d = \frac{1}{n-2} \sum_i (X_{i,d} - \alpha_d - \beta_d t_i)^2$$

### Coefficient of Determination

$$R^2_d = 1 - \frac{\sum_i (X_{i,d} - \hat{X}_{i,d})^2}{\sum_i (X_{i,d} - \bar{X}_d)^2}$$

## 9. Bucket Statistics

For each query bucket $j$ with queries $\{q^{(i)}\}_{i \in B_j}$:

### Representative Position

$$\tau_j = \frac{1}{|B_j|} \sum_{i \in B_j} t_i$$

### Semantic Mean (dimensions 1:)

$$\mu_j = \frac{1}{|B_j|} \sum_{i \in B_j} q^{(i)}_\perp$$

### Semantic Covariance

$$\Sigma_j = \frac{1}{|B_j| - 1} \sum_{i \in B_j} (q^{(i)}_\perp - \mu_j)(q^{(i)}_\perp - \mu_j)^\top + \epsilon I$$

where $\epsilon = 10^{-12}$ is a regularization term for numerical stability.

## 10. Summary of Key Equations

| Concept | Formula |
|---------|---------|
| Score difference | $D = q^\top \Delta k$ |
| Query model (positional) | $q_1 = \alpha + \beta t + \varepsilon$, $\varepsilon \sim \mathcal{N}(0, \sigma^2)$ |
| Conditional mean | $m(t) = \Delta k_1(\alpha + \beta t) + \Delta k_\perp^\top \mu_b$ |
| Conditional variance | $v = (\Delta k_1)^2 \sigma^2 + \Delta k_\perp^\top \Sigma_b \Delta k_\perp$ |
| Standardized score | $z(t) = m(t) / \sqrt{v}$ |
| Key preference probability | $p(t) = \Phi(z(t))$ |
| **Plasticity** | $\text{AP}(t) = 4\Phi(z(t))(1 - \Phi(z(t)))$ |
| Bucket aggregation | $\text{AP}_j = \mathbb{E}[\text{AP}]$ over sampled pairs |
| Head aggregation | $\text{AP}_{\text{head}} = \sum_j w_j \text{AP}_j / \sum_j w_j$ |
