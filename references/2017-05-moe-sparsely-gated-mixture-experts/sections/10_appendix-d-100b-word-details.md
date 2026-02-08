# Appendix D: 100 Billion Word Google News Corpus - Experimental Details [p. 16–17]

### Model Architecture

[p. 16] The models are similar in structure to the 8-million-operations-per-timestep models described in Appendix C.1. The number of experts is varied between models, using an ordinary MoE layer with 32 experts and hierarchical MoE layers with 256, 1024, 4096, 16384, 65536 and 131072 experts. For the hierarchical MoE layers, the first level branching factors are 32, 32, 64, 128, 256 and 256, respectively.

### Training

[p. 16] Models are trained on a cluster of 32 Tesla K40 GPUs, except for the last two models, which are trained on clusters of 64 and 128 GPUs so as to have enough memory for all the parameters. For all models, training batch sizes are approximately 2.5 million words. Models are trained once-through over about 100 billion words.

### Memory Optimizations

[p. 16] Several memory optimizations are implemented to fit up to 1 billion parameters per GPU:

1. The activations of the hidden layers of the experts are not stored; instead they are recomputed on the backwards pass.
2. The optimizer on the expert parameters is modified to require less auxiliary storage.

[p. 16] The Adam optimizer (Kingma & Ba, 2015) keeps first and second moment estimates of the per-parameter gradients, which triples the required memory. To avoid keeping a first-moment estimator, beta_1 is set to 0. To reduce the size of the second moment estimator, it is replaced with a factored approximation. For a matrix of parameters, instead of maintaining a full matrix of second-moment estimators, vectors of row-wise and column-wise averages of that matrix are maintained. At each step, the matrix of estimators is taken to be the outer product of those two vectors divided by the mean of either one. This technique could similarly be applied to Adagrad (Duchi et al., 2010).

### Results

**Table 8** (p. 16): Model comparison on 100 Billion Word Google News Dataset

| Model | Test Perplexity .1 epochs | Test Perplexity 1 epoch | ops/timestep (millions) | #Params excluding embed. & softmax (millions) | Total #Params (billions) | TFLOPS per GPU (observed) |
|---|---|---|---|---|---|---|
| Kneser-Ney 5-gram | 67.1 | 45.3 | 0.00001 | | 76.0 | |
| 4xLSTM-512 | 54.5 | 47.0 | 8.4 | 8.4 | 0.1 | **1.23** |
| MoE-32 | 48.5 | 40.4 | 8.4 | 37.8 | 0.1 | 0.83 |
| MoE-256-h | 42.8 | 35.3 | 8.4 | 272.9 | 0.4 | 1.11 |
| MoE-1024-h | 40.3 | 32.7 | 8.5 | 1079.0 | 1.2 | 1.14 |
| MoE-4096-h | 38.9 | 30.9 | 8.6 | 4303.4 | 4.4 | 1.07 |
| MoE-16384-h | **38.2** | 29.7 | 8.8 | 17201.0 | 17.3 | 0.96 |
| MoE-65536-h | **38.2** | **28.9** | 9.2 | 68791.0 | 68.9 | 0.72 |
| MoE-131072-h | 39.8 | 29.2 | 9.7 | 137577.6 | 137.7 | 0.30 |

[p. 16–17] **Results:** The model is evaluated using perplexity on a holdout dataset. Results are reported in Table 8. Perplexity after 100 billion training words is 39% lower for the 68-billion-parameter MoE model compared to the computationally matched baseline (4xLSTM-512).

[p. 17] It is notable that the measured computational efficiency of the largest model (0.30 TFLOPS/GPU) is very low compared to the other models. This is likely a result of the fact that, for purposes of comparison to the other models, they did not increase the training batch size proportionally to the number of GPUs. For comparison, they include results for a computationally matched baseline model consisting of 4 LSTMs, and for an unpruned 5-gram model with Kneser-Ney smoothing (Kneser & Ney, 1995).

**Footnote 4** [p. 17]: While the original size of the corpus was 130 billion words, the neural models were trained for a maximum of 100 billion words. The reported Kneser-Ney 5-gram models were trained over 13 billion and 130 billion words respectively, giving them a slight advantage over the other reported results.
