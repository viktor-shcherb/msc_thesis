# D Data Statistics [p. 15-16]

## D.1 Synthetic Dataset: Tree-NeighborsMatch

[p. 15] Statistics of the synthetic TREE-NEIGHBORSMATCH dataset are shown in Table 7.

### Table 7

**Table 7** (p. 15): "The number of examples, in our experiments and combinatorially, for every value of $depth$."

| $depth$ | # Training examples sampled | Total combinatorial: $(2^{depth}!) \cdot 2^{depth}$ |
|---------|----------------------------|----------------------------------------------------|
| 2 | 96 | 96 |
| 3 | 8000 | $> 3 \cdot 10^5$ |
| 4 | 16,000 | $> 3 \cdot 10^{14}$ |
| 5 | 32,000 | $> 10^{36}$ |
| 6 | 32,000 | $> 10^{90}$ |
| 7 | 32,000 | $> 10^{217}$ |
| 8 | 32,000 | $> 10^{509}$ |

## D.2 Quantum Chemistry: QM9

[p. 15] Statistics of the quantum chemistry QM9 dataset, as used in Brockschmidt (2020) are shown in Table 8.

### Table 8

**Table 8** (p. 15): "Statistics of the QM9 chemical dataset (Ramakrishnan et al., 2014) as used by Brockschmidt (2020)."

| | Training | Validation | Test |
|------------------------------|----------|------------|--------|
| # examples | 110,462 | 10,000 | 10,000 |
| # nodes - average | 18.03 | 18.06 | 18.09 |
| # nodes - standard deviation | 2.9 | 2.9 | 2.9 |
| # edges - average | 18.65 | 18.67 | 18.72 |
| # edges - standard deviation | 3.1 | 3.1 | 3.1 |

## D.3 Biological Benchmarks

[p. 15-16] Statistics of the biological datasets, as used in Errica et al. (2020), are shown in Table 9.

### Table 9

**Table 9** (p. 16): "Statistics of the biological datasets, as used by Errica et al. (2020)."

| | NCI1 (Wale et al., 2008) | ENZYMES (Borgwardt et al., 2005) |
|------------------------------|--------------------------|----------------------------------|
| # examples | 4110 | 600 |
| # classes | 2 | 6 |
| # nodes - average | 29.87 | 32.63 |
| # nodes - standard deviation | 13.6 | 15.3 |
| # edges - average | 32.30 | 64.14 |
| # edges - standard deviation | 14.9 | 25.5 |
| # node labels | 37 | 3 |

## D.4 VarMisuse

[p. 16] Statistics of the VARMISUSE dataset, as used in Allamanis et al. (2018) and Brockschmidt (2020), are shown in Table 10.

### Table 10

**Table 10** (p. 16): "Statistics of the VARMISUSE dataset (Allamanis et al., 2018) as used by Brockschmidt (2020)."

| | Training | Validation | UnseenProject Test | SeenProject Test |
|---------------------|----------|------------|-------------------|-----------------|
| # graphs | 254360 | 42654 | 117036 | 59974 |
| # nodes - average | 2377 | 1742 | 1959 | 3986 |
| # edges - average | 7298 | 7851 | 5882 | 12925 |
