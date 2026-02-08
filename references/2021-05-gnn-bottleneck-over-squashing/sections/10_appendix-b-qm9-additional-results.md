# B QM9 -- Additional Results [p. 13-15]

## B.1 Additional GNN Types

[p. 13] Because of space limitations, in Section 4.2 results were presented on the QM9 dataset only for R-GIN, R-GAT and GGNN. This section shows that additional GNN architectures benefit from breaking the bottleneck using a fully-adjacent layer: GNN-MLP, R-GCN (Schlichtkrull et al., 2018) and GNN-FiLM (Brockschmidt, 2020).

All experiments were performed using the extensively-tuned implementation of Brockschmidt (2020) who experimented with over 500 hyperparameter configurations.

### Table 4

**Table 4** (p. 13): "Average error rates and standard deviations on the QM9 targets. Best result for every property in every GNN type is highlighted in bold. Results marked with dagger were previously reported by Brockschmidt (2020)."

| Property | MLP base$^\dagger$ | MLP +FA | R-GCN base$^\dagger$ | R-GCN +FA | GNN-FiLM base$^\dagger$ | GNN-FiLM +FA |
|----------|--------------------|---------|-----------------------|-----------|--------------------------|--------------|
| mu | 2.36$\pm$0.04 | **2.19**$\pm$0.04 | 3.21$\pm$0.06 | **2.92**$\pm$0.07 | 2.38$\pm$0.13 | **2.26**$\pm$0.06 |
| alpha | 4.27$\pm$0.36 | **1.92**$\pm$0.06 | 4.22$\pm$0.45 | **2.14**$\pm$0.08 | 3.75$\pm$0.11 | **1.93**$\pm$0.08 |
| HOMO | 1.25$\pm$0.04 | **1.19**$\pm$0.04 | 1.45$\pm$0.01 | **1.37**$\pm$0.02 | 1.22$\pm$0.07 | **1.11**$\pm$0.01 |
| LUMO | 1.35$\pm$0.04 | **1.20**$\pm$0.05 | 1.62$\pm$0.04 | **1.41**$\pm$0.01 | 1.30$\pm$0.05 | **1.21**$\pm$0.05 |
| gap | 2.04$\pm$0.05 | **1.82**$\pm$0.05 | 2.42$\pm$0.14 | **2.03**$\pm$0.03 | 1.96$\pm$0.06 | **1.79**$\pm$0.07 |
| R2 | 14.86$\pm$1.62 | **12.40**$\pm$0.84 | 16.38$\pm$0.49 | **13.55**$\pm$0.50 | 15.59$\pm$1.38 | **11.89**$\pm$0.73 |
| ZPVE | 12.00$\pm$1.66 | **4.68**$\pm$0.29 | 17.40$\pm$3.56 | **5.81**$\pm$0.61 | 11.00$\pm$0.74 | **4.68**$\pm$0.49 |
| U0 | 5.55$\pm$0.38 | **1.71**$\pm$0.13 | 7.82$\pm$0.80 | **1.75**$\pm$0.18 | 5.43$\pm$0.96 | **1.60**$\pm$0.12 |
| U | 6.20$\pm$0.88 | **1.72**$\pm$0.12 | 8.24$\pm$1.25 | **1.88**$\pm$0.22 | 5.95$\pm$0.46 | **1.75**$\pm$0.08 |
| H | 5.96$\pm$0.45 | **1.70**$\pm$0.08 | 9.05$\pm$1.21 | **1.85**$\pm$0.18 | 5.59$\pm$0.57 | **1.93**$\pm$0.42 |
| G | 5.09$\pm$0.57 | **1.53**$\pm$0.15 | 7.00$\pm$1.51 | **1.76**$\pm$0.15 | 5.17$\pm$1.13 | **1.77**$\pm$0.05 |
| Cv | 3.38$\pm$0.20 | **1.69**$\pm$0.08 | 3.93$\pm$0.48 | **1.90**$\pm$0.07 | 3.46$\pm$0.21 | **1.64**$\pm$0.10 |
| Omega | 0.84$\pm$0.02 | **0.63**$\pm$0.04 | 1.02$\pm$0.05 | **0.75**$\pm$0.04 | 0.98$\pm$0.06 | **0.69**$\pm$0.05 |
| Relative: | | -40.33% | | -43.40% | | -39.53% |

[p. 14] Table 4 contains additional results for GGNN, R-GCN and R-GIN. As shown in Table 4, adding an FA layer significantly improves results across all GNN architectures, for all properties.

## B.2 Alternative Solutions

[p. 14] Table 5 shows additional experiments, all performed using GCN. $base^\dagger$ is the original model of Brockschmidt (2020) as in Table 4. $+FA$ is the model that was re-trained with the last layer modified to an FA layer.

$2 \times d$ is a model that was trained with a doubled hidden dimension size, $d = 256$ instead of $d = 128$ as in the base model. Doubling the hidden dimension size leads to a small improvement of only 5.5% reduction in error. In comparison, the +FA model used the original dimension sizes and achieves a much larger improvement of 43.40%.

*All FA* is a model that was trained with *all* GNN layers converted into FA layers, practically ignoring the graph topology. This led to much worse results of more than 1500% higher error. This shows that the graph topology is important in this benchmark, and that a direct interaction between nodes (as in a single FA layer) must be performed in addition to considering the topology.

$2 \times FA$ is a model where the last layer was modified into an FA layer, and an additional FA layer was stacked on top of it. This led to results that are very similar to +FA.

*Penultimate FA* is a model where the FA layer is the penultimate layer (the $K - 1$-th), followed by a standard GNN layer as the $K$-th layer. This led to results that are even slightly better than +FA.

### Table 5

**Table 5** (p. 14): "Average error rates and standard deviations on the QM9 targets with GCN using alternative solutions."

| Property | base$^\dagger$ | +FA | $2 \times d$ | All FA | $2 \times$FA | Penultimate FA |
|----------|---------------|-----|-------------|--------|-------------|----------------|
| mu | 3.21$\pm$0.06 | 2.92$\pm$0.07 | 2.99$\pm$0.08 | 11.52 | 2.89$\pm$0.08 | **2.80**$\pm$0.08 |
| alpha | 4.22$\pm$0.45 | **2.14**$\pm$0.08 | 3.57$\pm$0.40 | 9.19 | 2.23$\pm$0.04 | **2.14**$\pm$0.10 |
| HOMO | 1.45$\pm$0.01 | 1.37$\pm$0.02 | 1.36$\pm$1.87 | 9.95 | 1.39$\pm$0.02 | **1.34**$\pm$0.03 |
| LUMO | 1.62$\pm$0.04 | 1.41$\pm$0.01 | 1.43$\pm$0.04 | 19.13 | 1.42$\pm$0.04 | **1.37**$\pm$0.02 |
| gap | 2.42$\pm$0.14 | 2.03$\pm$0.03 | 2.33$\pm$0.23 | 24.62 | 2.06$\pm$0.05 | **2.00**$\pm$0.03 |
| R2 | 16.38$\pm$0.49 | 13.55$\pm$0.50 | 18.4$\pm$0.76 | 168.09 | 13.97$\pm$0.56 | **12.92**$\pm$0.11 |
| ZPVE | 17.40$\pm$3.56 | 5.81$\pm$0.61 | 15.8$\pm$2.59 | 591.33 | 5.79$\pm$0.50 | **4.53**$\pm$0.62 |
| U0 | 7.82$\pm$0.80 | **1.75**$\pm$0.18 | 7.60$\pm$2.07 | 188.59 | 1.90$\pm$0.1 | 1.98$\pm$0.25 |
| U | 8.24$\pm$1.25 | 1.88$\pm$0.22 | 7.65$\pm$1.51 | 189.72 | **1.71**$\pm$0.16 | 2.05$\pm$0.23 |
| H | 9.05$\pm$1.21 | 1.85$\pm$0.18 | 8.67$\pm$1.10 | 191.11 | 1.83$\pm$0.11 | **1.73**$\pm$0.14 |
| G | 7.00$\pm$1.51 | **1.76**$\pm$0.15 | 2.90$\pm$1.15 | 173.68 | 1.93$\pm$0.11 | 1.96$\pm$0.42 |
| Cv | 3.93$\pm$0.48 | 1.90$\pm$0.07 | 3.99$\pm$0.07 | 64.18 | 1.90$\pm$0.14 | **1.83**$\pm$0.11 |
| Omega | 1.02$\pm$0.05 | 0.75$\pm$0.04 | 1.03$\pm$0.54 | 23.89 | 0.69$\pm$0.01 | **0.67**$\pm$0.01 |
| relative | 0.0% | -43.40% | -5.50% | +1520% | -43.30% | **-45.2%** |

## B.3 Partial-FA Layers

[p. 14-15] The authors also examined whether instead of adding a "full fully-adjacent layer", one can randomly sample only a fraction of these edges. They randomly sampled only {0.25, 0.5, 0.75} of the edges in the full FA layer in every example, and trained the model for each target property 5 times. Table 6 shows the results of these experiments using GCN. $base^\dagger$ is the original model of Brockschmidt (2020) as in Table 4. $+FA$ is the model that was re-trained with the last layer modified to an FA layer. {0.25, 0.5, 0.75} $\times$ FA are the models where only a fraction of the edges in the FA layer were used.

### Table 6

**Table 6** (p. 14): "Average error rates and standard deviations on the QM9 targets with GCN, where we use only a fraction of the edges in the FA layer."

| | base$^\dagger$ | 0.25$\times$ FA | 0.5$\times$ FA | 0.75$\times$ FA | +FA (as in Table 4) |
|------------------------------|---------------|-----------------|----------------|-----------------|---------------------|
| Avg. error compared to base$^\dagger$ | -0% | -8.4% | -31.5% | -37.1% | -43.4% |

[p. 15] As shown in Table 6, the full FA layer achieves the largest reduction in error (-43.4%), but even adding a fraction of the edges improves the results over the base model. For example, using only *half* of the edges ($0.5 \times FA$) reduces the error by 31.5%. Overall, the percentage of used edges in the partial-FA layer is correlated with its reduction in error.
