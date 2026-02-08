# References

References cited in the section notes. Citation keys use the paper's author-year format.

## Cited references

### Allamanis et al. (2018)
- Miltiadis Allamanis, Marc Brockschmidt, and Mahmoud Khademi. Learning to represent programs with graphs. In *International Conference on Learning Representations*, 2018.
- Cited in 04c_programs-varmisuse.md as the source of the VARMISUSE dataset and splits.
- Cited in 06_related-work.md for designing program analyses with 16 "shortcut" edge types to avoid over-squashing.
- Cited in 12_appendix-d-data-statistics.md for the VARMISUSE dataset statistics.

### Barcelo et al. (2020)
- Pablo Barcelo, Egor V. Kostylev, Mikael Monet, Jorge Perez, Juan Reutter, and Juan Pablo Silva. The logical expressiveness of graph neural networks. In *International Conference on Learning Representations*, 2020.
- Cited in 04_evaluation.md discussing under-reaching as an alternative explanation.
- Cited in 06_related-work.md for finding that GNN expressiveness captures only a small fragment of first-order logic.

### Borgwardt et al. (2005)
- Karsten M Borgwardt, Cheng Soon Ong, Stefan Schonauer, SVN Vishwanathan, Alex J Smola, and Hans-Peter Kriegel. Protein function prediction via graph kernels. *Bioinformatics*, 21(suppl_1):i47-i56, 2005.
- Cited in 04b_biological-benchmarks.md as the source of the ENZYMES dataset.
- Cited in 12_appendix-d-data-statistics.md for ENZYMES dataset statistics.

### Brockschmidt (2020)
- Marc Brockschmidt. Gnn-film: Graph neural networks with feature-wise linear modulation. *Proceedings of the 36th International Conference on Machine Learning*, ICML, 2020.
- Cited in 04_evaluation.md as the source of the QM9 model implementations and hyperparameter tuning (searched over 500 configurations).
- Cited in 04c_programs-varmisuse.md as the source of the VARMISUSE model implementations and hyperparameter tuning.
- Cited in 10_appendix-b-qm9-additional-results.md as the source of baseline models and hyperparameter configurations for QM9 additional results and alternative solutions.
- Cited in 12_appendix-d-data-statistics.md for QM9 and VARMISUSE dataset statistics.

### Chen et al. (2018)
- Cited in 03_gnn-bottleneck.md for the result that the receptive field size grows as $\mathcal{O}(\exp(K))$.

### Chen et al. (2020a)
- Cited in 01_introduction.md as one of the works demonstrating over-smoothing in short-range tasks.

### Chen et al. (2020b)
- Cited in 01_introduction.md as one of the works demonstrating over-smoothing in short-range tasks.

### Cho et al. (2014a,b)
- Cited in 01_introduction.md in the analogy between GNN bottleneck and seq2seq RNN bottleneck.

### Duvenaud et al. (2015)
- David K Duvenaud, Dougal Maclaurin, Jorge Iparraguirre, Rafael Bombarell, Timothy Hirzel, Alan Aspuru-Guzik, and Ryan P Adams. Convolutional networks on graphs for learning molecular fingerprints. In *Advances in neural information processing systems*, pages 2224-2232, 2015.
- Cited in 01_introduction.md as an example of growing GNN popularity.

### Errica et al. (2020)
- Federico Errica, Marco Podda, Davide Bacciu, and Alessio Micheli. A fair comparison of graph neural networks for graph classification. In *International Conference on Learning Representations*, 2020.
- Cited in 04b_biological-benchmarks.md as the source of the biological benchmark implementations, 10-fold splits, and training procedure.
- Cited in 11_appendix-c-biological-training.md for biological benchmark training procedure details.
- Cited in 12_appendix-d-data-statistics.md for biological dataset statistics.

### Fey and Lenssen (2019)
- Cited in 04_evaluation.md as the PyTorch Geometric framework used for implementation.

### Garg et al. (2020)
- Cited in 04_evaluation.md regarding the tree-like view of a node's receptive field.

### Gilmer et al. (2017)
- Justin Gilmer, Samuel S Schoenholz, Patrick F Riley, Oriol Vinyals, and George E Dahl. Neural message passing for quantum chemistry. In *Proceedings of the 34th International Conference on Machine Learning-Volume 70*, pages 1263-1272. JMLR. org, 2017.
- Cited in 01_introduction.md for viewing GNN layers as message-passing steps.
- Cited in 03_gnn-bottleneck.md and 04_evaluation.md regarding molecular property prediction and QM9.
- Cited in 06_related-work.md for adding "virtual edges" to shorten long distances as a means to avoid over-squashing.

### Gori et al. (2005)
- Cited in 00_overview.md and 01_introduction.md as one of the original GNN proposals.

### Hamilton et al. (2017)
- Cited in 01_introduction.md as an example of growing GNN popularity.
- Cited in 02_preliminaries.md for the normalization factor variant in GCN.

### Kipf and Welling (2017)
- Thomas N Kipf and Max Welling. Semi-supervised classification with graph convolutional networks. In *ICLR*, 2017.
- Cited in 01_introduction.md as a GNN variant.
- Cited in 03_gnn-bottleneck.md noting that short-range problems can use $K=2$ layers.
- Cited in 04_evaluation.md regarding GCN training accuracy at $r=4$.
- Cited in 06_related-work.md regarding empirical optimality of $K=2$ layers in short-range tasks.
- Cited in 09_appendix-a-tree-neighborsmatch-training.md as one of the GNN types used in the Tree-NeighborsMatch experiments.

### Klicpera et al. (2018)
- Cited in 01_introduction.md as one of the works demonstrating over-smoothing in short-range tasks.

### Leskovec and Mcauley (2012)
- Cited in 03_gnn-bottleneck.md as an example of a short-range social network domain.

### Levy et al. (2018)
- Cited in 04_evaluation.md regarding the hypothesis that GRU cells in GGNNs perform element-wise attention.

### Li et al. (2016)
- Yujia Li, Daniel Tarlow, Marc Brockschmidt, and Richard Zemel. Gated graph sequence neural networks. In *International Conference on Learning Representations*, 2016.
- Cited in 01_introduction.md as a GNN variant (GGNN).
- Cited in 02_preliminaries.md regarding weighted sum readout functions.
- Cited in 01_introduction.md as being less susceptible to over-squashing than GCN/GIN.
- Cited in 09_appendix-a-tree-neighborsmatch-training.md as one of the GNN types (GGNN) used in the Tree-NeighborsMatch experiments.

### Li et al. (2018)
- Qimai Li, Zhichao Han, and Xiao-Ming Wu. Deeper insights into graph convolutional networks for semi-supervised learning. In *Thirty-Second AAAI Conference on Artificial Intelligence*, 2018.
- Cited in 01_introduction.md as one of the works demonstrating over-smoothing in short-range tasks.
- Cited in 06_related-work.md as one of the works identifying over-smoothing.

### Micheli (2009)
- Cited in 01_introduction.md as one of the early GNN works.

### Oono and Suzuki (2020)
- Kenta Oono and Taiji Suzuki. Graph neural networks exponentially lose expressive power for node classification. In *International Conference on Learning Representations*, 2020.
- Cited in 01_introduction.md as one of the works demonstrating over-smoothing in short-range tasks.
- Cited in 06_related-work.md as one of the works identifying over-smoothing.

### Ramakrishnan et al. (2014)
- Raghunathan Ramakrishnan, Pavlo O Dral, Matthias Rupp, and O Anatole Von Lilienfeld. Quantum chemistry structures and properties of 134 kilo molecules. *Scientific data*, 1:140022, 2014.
- Cited in 03_gnn-bottleneck.md and 04_evaluation.md regarding molecular property prediction and QM9.
- Cited in 12_appendix-d-data-statistics.md for QM9 dataset statistics.

### Rong et al. (2020)
- Cited in 01_introduction.md as one of the works demonstrating over-smoothing in short-range tasks.

### Scarselli et al. (2008)
- Franco Scarselli, Marco Gori, Ah Chung Tsoi, Markus Hagenbuchner, and Gabriele Monfardini. The graph neural network model. *IEEE Transactions on Neural Networks*, 20(1):61-80, 2008.
- Cited in 00_overview.md and 01_introduction.md as one of the original GNN proposals.
- Cited in 06_related-work.md for adding "supersource nodes" as a means to avoid over-squashing.

### Schlichtkrull et al. (2018)
- Michael Schlichtkrull, Thomas N Kipf, Peter Bloem, Rianne Van Den Berg, Ivan Titov, and Max Welling. Modeling relational data with graph convolutional networks. In *European Semantic Web Conference*, pages 593-607. Springer, 2018.
- Cited in 02_preliminaries.md regarding typed edges in graphs.
- Cited in 10_appendix-b-qm9-additional-results.md as the source of R-GCN architecture.

### Sen et al. (2008)
- Cited in 01_introduction.md for paper subject classification as a short-range task.
- Cited in 03_gnn-bottleneck.md as a citation network domain (short-range).

### Shchur et al. (2018)
- Cited in 01_introduction.md for product category classification as a short-range task.
- Cited in 03_gnn-bottleneck.md as a product recommendation domain (short-range).

### Sutskever et al. (2014)
- Cited in 01_introduction.md in the analogy between GNN bottleneck and seq2seq RNN bottleneck.

### Velickovic et al. (2018)
- Petar Velickovic, Guillem Cucurull, Arantxa Casanova, Adriana Romero, Pietro Lio, and Yoshua Bengio. Graph attention networks. In *International Conference on Learning Representations*, 2018.
- Cited in 01_introduction.md as a GNN variant (GAT), less susceptible to over-squashing than GCN/GIN.
- Cited in 09_appendix-a-tree-neighborsmatch-training.md as one of the GNN types (GAT) used in the Tree-NeighborsMatch experiments.

### Wale et al. (2008)
- Nikil Wale, Ian A Watson, and George Karypis. Comparison of descriptor spaces for chemical compound retrieval and classification. *Knowledge and Information Systems*, 14(3):347-375, 2008.
- Cited in 04b_biological-benchmarks.md as the source of the NCI1 dataset.
- Cited in 12_appendix-d-data-statistics.md for NCI1 dataset statistics.

### Wu et al. (2018)
- Cited in 04_evaluation.md regarding the QM9 dataset.

### Wu et al. (2020)
- Cited in 01_introduction.md for the over-smoothing explanation.
- Cited in 06_related-work.md as one of the works identifying over-smoothing.

### Xu et al. (2018)
- Cited in 04_evaluation.md regarding the tree-like view of a node's receptive field.

### Xu et al. (2019)
- Keyulu Xu, Weihua Hu, Jure Leskovec, and Stefanie Jegelka. How powerful are graph neural networks? In *International Conference on Learning Representations*, 2019.
- Cited in 01_introduction.md as a GNN variant (GIN), more susceptible to over-squashing.
- Cited in 02_preliminaries.md for the GIN update rule.
- Cited in 09_appendix-a-tree-neighborsmatch-training.md as one of the GNN types (GIN) used in the Tree-NeighborsMatch experiments.

### Zhao and Akoglu (2020)
- Cited in 01_introduction.md as one of the works demonstrating over-smoothing in short-range tasks.
