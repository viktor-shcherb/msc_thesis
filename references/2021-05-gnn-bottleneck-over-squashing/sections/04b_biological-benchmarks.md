# 4.3 Biological Benchmarks [p. 7-8]

## Data

[p. 7] The NCI1 dataset (Wale et al., 2008) contains 4110 graphs with ~30 nodes on average, and its task is to predict whether a biochemical compound contains anti-lung-cancer activity. ENZYMES (Borgwardt et al., 2005) contains 600 graphs with ~36 nodes on average, and its task is to classify an enzyme to one out of six classes. The same 10-folds and split as Errica et al. (2020) are used.

## Models

[p. 7] The authors used the implementation of Errica et al. (2020) who performed a fair and thorough comparison between GNNs. The final reported result is the average of 30 test runs (10 folds x 3 random seeds). Additional training details are provided in Appendix C.

In ENZYMES, Errica et al. found that a baseline that does not use the graph topology *at all* ("*No Struct*") performs better than all GNNs. In NCI1, GIN performed best. The authors converted the last layer into an FA layer by modifying the implementation of Errica et al., and repeated the same training procedure. They compare the "base" models from Errica et al. with their re-trained "+FA" models.

## Results

[p. 7-8] Results are shown in Table 2. The main results are as follows: (a) in NCI1, GIN+FA improves by 1.5% over GIN-base, which was previously the best performing model; (b) in ENZYMES, where Errica et al. (2020) found that none of the GNNs exploit the topology of the graph, the authors find that GIN+FA *does* exploit the structure and improves by 8.1% over GIN-base and by 2.5% over *No Struct*.

[p. 8] On average, models with FA layers relatively reduce the error rate by 12% in ENZYMES and by 4.8% in NCI1. These experiments clearly show evidence for a bottleneck in the original GNN models.

## Table 2

**Table 2** (p. 7): "Average accuracy (30 runs +/- stdev) on the biological datasets. dagger -- previously reported by Errica et al. (2020)."

| Model | | NCI1 | ENZYMES |
|-------|------|------|---------|
| No Struct$^\dagger$ | | 69.8$\pm$2.2 | 65.2$\pm$6.4 |
| DiffPool | base$^\dagger$ | 76.9$\pm$1.9 | 59.5$\pm$5.6 |
| | +FA | **77.6**$\pm$1.3 | **65.7**$\pm$4.8 |
| GraphSAGE | base$^\dagger$ | 76.0$\pm$1.8 | 58.2$\pm$6.0 |
| | +FA | **77.7**$\pm$1.8 | **60.8**$\pm$4.5 |
| DGCNN | base$^\dagger$ | 76.4$\pm$1.7 | 38.9$\pm$5.7 |
| | +FA | **76.8**$\pm$1.5 | **42.8**$\pm$5.3 |
| GIN | base$^\dagger$ | 80.0$\pm$1.4 | 59.6$\pm$4.5 |
| | +FA | **81.5**$\pm$1.2 | **67.7**$\pm$5.3 |
