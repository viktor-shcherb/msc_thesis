# 4.4 Programs: VarMisuse [p. 8]

## Data

[p. 8] VARMISUSE (Allamanis et al., 2018) is a node-prediction problem that depends on long-range information in computer programs. The same splits as Allamanis et al. (2018) are used.

## Models

[p. 8] The authors use the implementation of Brockschmidt (2020) who performed an extensive hyperparameter tuning by searching over 30 configurations for each GNN type. The best results were found using 6-10 layers, which hints that this problem requires long-range information. The last layer is modified to be an FA layer, and the resulting representations are used for node classification. The same best found configurations as Brockschmidt (2020) are used, and each model is re-trained five times.

## Results

[p. 8] Results are shown in Table 3. The main result is that adding an FA layer to all GNNs improves their SeenProjTest accuracy, obtaining a new state-of-the-art of 88.4%. In the *UnseenProjTest* set, adding an FA layer improves the results of some of most of the GNNs, obtaining a new state-of-the-art of 83.8%. These improvements are significant, especially since they were achieved on extensively tuned models, without any further tuning by the authors.

## Table 3

**Table 3** (p. 7): "Average accuracy (5 runs +/- stdev) on VARMISUSE. dagger -- previously reported by Brockschmidt (2020)."

| Model | | SeenProj | UnseenProj |
|-------|------|----------|------------|
| GGNN | base$^\dagger$ | 85.7$\pm$0.5 | **79.3**$\pm$1.2 |
| | +FA | **86.3**$\pm$0.7 | 79.1$\pm$1.1 |
| R-GCN | base$^\dagger$ | 88.3$\pm$0.4 | 82.9$\pm$0.8 |
| | +FA | **88.4**$\pm$0.7 | **83.8**$\pm$1.0 |
| R-GIN | base$^\dagger$ | 87.1$\pm$0.1 | 81.1$\pm$0.9 |
| | +FA | **87.5**$\pm$0.7 | **81.7**$\pm$1.2 |
| GNN-MLP | base$^\dagger$ | 86.9$\pm$0.3 | **81.4**$\pm$0.7 |
| | +FA | **87.3**$\pm$0.2 | 81.2$\pm$0.5 |
| R-GAT | base$^\dagger$ | 86.9$\pm$0.7 | 81.2$\pm$0.9 |
| | +FA | **87.9**$\pm$1.0 | **82.0**$\pm$1.9 |
