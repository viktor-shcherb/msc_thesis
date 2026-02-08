# D Experiment Details and Full Results [p. 25-26]

[p. 25]

This section contains full experimental procedures and extended results and citations for the experimental evaluation in Section 4. Appendix D.1 corresponds to benchmarking results in Section 4.1, Appendix D.2 corresponds to LRD experiments (LRA and Speech Commands) in Section 4.2, and Appendix D.3 corresponds to the general sequence modeling experiments (generation, image classification, forecasting) in Section 4.3.

## D.1 Benchmarking

[p. 25]

Benchmarking results from Table 2 and Table 3 were tested on a single A100 GPU.

### Benchmarks against LSSL

For a given dimension $H$, a single LSSL or S4 layer was constructed with $H$ hidden features. For LSSL, the state size $N$ was set to $H$ as done in [18]. For S4, the state size $N$ was set to parameter-match the LSSL, which was a state size of $\frac{N}{2}$ due to differences in the parameterization. Table 2 benchmarks a single forward+backward pass of a single layer.

### Benchmarks against Efficient Transformers

Following [40], the Transformer models had 4 layers, hidden dimension 256 with 4 heads, query/key/value projection dimension 128, and batch size 32, for a total of roughly 600k parameters. The S4 model was parameter tied while keeping the depth and hidden dimension constant (leading to a state size of $N = 256$).

The relative orderings of these methods can vary depending on the exact hyperparameter settings.

## D.2 Long-Range Dependencies

[p. 26]

This section includes information for reproducing the experiments on the Long-Range Arena and Speech Commands long-range dependency tasks.

### Long Range Arena

Table 10 contains extended results table with all 11 methods considered in [40].

For the S4 model, hyperparameters for all datasets are reported in Table 11. For all datasets, the AdamW optimizer with a constant learning rate schedule with decay on validation plateau was used. However, the learning rate on HiPPO parameters (in particular $\boldsymbol{A}$, $\boldsymbol{P}$, $\boldsymbol{Q}$, $\boldsymbol{B}$, $\boldsymbol{C}$, $\Delta$) were reduced to a maximum starting LR of 0.001, which improves stability since the HiPPO equation is crucial to performance.

The S4 state size was always fixed to $N = 64$.

As S4 is a sequence-to-sequence model with output shape (batch, length, dimension) and LRA tasks are classification, mean pooling along the length dimension was applied after the last layer.

Most of these results were trained for far longer than what was necessary to achieve SotA results (e.g., the **Image** task reaches SotA in 1 epoch). Results often keep improving with longer training times.

**Updated results.** The above hyperparameters describe the results reported in the original paper, shown in Table 10, which have since been improved. See Appendix D.5.

**Hardware.** All models were run on single GPU. Some tasks used an A100 GPU (notably, the Path-X experiments), which has a larger max memory of 40Gb. To reproduce these on smaller GPUs, the batch size can be reduced or gradients can be accumulated for two batches.

### Table 10: Full LRA Results

**Table 10** (p. 26): "Full results for the Long Range Arena (LRA) benchmark for long-range dependencies in sequence models. (Top): Original Transformer variants in LRA. (Bottom): Other models reported in the literature."

| Model            | ListOps | Text  | Retrieval | Image | Pathfinder | Path-X | Avg   |
|------------------|---------|-------|-----------|-------|------------|--------|-------|
| Random           | 10.00   | 50.00 | 50.00     | 10.00 | 50.00      | 50.00  | 36.67 |
| Transformer      | 36.37   | 64.27 | 57.46     | 42.44 | 71.40      | X      | 53.66 |
| Local Attention  | 15.82   | 52.98 | 53.39     | 41.46 | 66.63      | X      | 46.71 |
| Sparse Trans.    | 17.07   | 63.58 | 59.59     | 44.24 | 71.71      | X      | 51.03 |
| Longformer       | 35.63   | 62.85 | 56.89     | 42.22 | 69.71      | X      | 52.88 |
| Linformer        | 35.70   | 53.94 | 52.27     | 38.56 | 76.34      | X      | 51.14 |
| Reformer         | 37.27   | 56.10 | 53.40     | 38.07 | 68.50      | X      | 50.56 |
| Sinkhorn Trans.  | 33.67   | 61.20 | 53.83     | 41.23 | 67.45      | X      | 51.23 |
| Synthesizer      | 36.99   | 61.68 | 54.67     | 41.61 | 69.45      | X      | 52.40 |
| BigBird          | 36.05   | 64.02 | 59.29     | 40.83 | 74.87      | X      | 54.17 |
| Linear Trans.    | 16.13   | 65.90 | 53.09     | 42.34 | 75.30      | X      | 50.46 |
| Performer        | 18.01   | 65.40 | 53.82     | 42.77 | 77.05      | X      | 51.18 |
| FNet             | 35.33   | 65.11 | 59.61     | 38.67 | 77.80      | X      | 54.42 |
| Nystromformer    | 37.15   | 65.52 | 79.56     | 41.58 | 70.94      | X      | 57.46 |
| Luna-256         | 37.25   | 64.57 | 79.29     | 47.38 | 77.72      | X      | 59.37 |
| **S4** (original)| 58.35   | 76.02 | 87.09     | 87.26 | 86.05      | 88.10  | 80.48 |
| **S4** (updated) | **59.60** | **86.82** | **90.90** | **88.65** | **94.20** | **96.35** | **86.09** |

X denotes failure on the task (random guessing or inability to run due to memory/compute).

---
[p. 27 continued]

### Table 11: Best Hyperparameters for Classification Datasets

**Table 11** (p. 27): "The values of the best hyperparameters found for classification datasets; LRA (Top) and images/speech (Bottom). LR is learning rate and WD is weight decay. BN and LN refer to Batch Normalization and Layer Normalization."

| Task                   | Depth | Features $H$ | Norm | Pre-norm | Dropout | LR     | Batch Size | Epochs | WD   | Patience |
|------------------------|-------|---------------|------|----------|---------|--------|------------|--------|------|----------|
| ListOps                | 6     | 128           | BN   | False    | 0       | 0.01   | 100        | 50     | 0.01 | 5        |
| Text                   | 4     | 64            | BN   | True     | 0       | 0.001  | 50         | 20     | 0    | 5        |
| Retrieval              | 6     | 256           | BN   | True     | 0       | 0.002  | 64         | 20     | 0    | 20       |
| Image                  | 6     | 512           | LN   | False    | 0.2     | 0.004  | 50         | 200    | 0.01 | 20       |
| Pathfinder             | 6     | 256           | BN   | True     | 0.1     | 0.004  | 100        | 200    | 0    | 10       |
| Path-X                 | 6     | 256           | BN   | True     | 0.0     | 0.0005 | 32         | 100    | 0    | 20       |
| CIFAR-10               | 6     | 1024          | LN   | False    | 0.25    | 0.01   | 50         | 200    | 0.01 | 20       |
| Speech Commands (MFCC) | 4     | 256           | LN   | False    | 0.2     | 0.01   | 100        | 50     | 0    | 5        |
| Speech Commands (Raw)  | 6     | 128           | BN   | True     | 0.1     | 0.01   | 20         | 150    | 0    | 10       |

### Speech Commands

[p. 27]

Details of sweeps run for baseline methods run by the authors are provided -- numbers for all others are taken from Gu et al. [18]. The best hyperparameters used for S4 are included in Table 11.

**Transformer [44]:** For MFCC, the number of model layers {2, 4}, dropout {0, 0.1} and learning rates {0.001, 0.0005} were swept. 8 attention heads, model dimension 128, prenorm, positional encodings were used, and training was for 150 epochs with a batch size of 100. For Raw, the Transformer model's memory usage made training impossible.

**Performer [8]:** For MFCC, the number of model layers {2, 4}, dropout {0, 0.1} and learning rates {0.001, 0.0005} were swept. 8 attention heads, model dimension 128, prenorm, positional encodings were used, and training was for 150 epochs with a batch size of 100. For Raw, a model dimension of 128, 4 attention heads, prenorm, and a batch size of 16 were used. The number of model layers was reduced to 4 so the model would fit on a single GPU. Training was for 100 epochs with a learning rate of 0.001 and no dropout.

**ExpRNN [24]:** For MFCC, hidden sizes {256, 512} and learning rates {0.001, 0.002, 0.0005} were swept. Training was run for 200 epochs, with a single layer model using a batch size of 100. For Raw, hidden sizes {32, 64} and learning rates {0.001, 0.0005} were swept (however, ExpRNN failed to learn).

**LipschitzRNN [13]:** For MFCC, hidden sizes {256, 512} and learning rates {0.001, 0.002, 0.0005} were swept. Training was run for 150 epochs, with a single layer model using a batch size of 100. For Raw, LipschitzRNN was too slow to train on a single GPU (requiring a full day for 1 epoch of training alone).

**WaveGAN Discriminator [11]:** The WaveGAN-D in Table 5 is actually an improved version of the discriminator network from the recent WaveGAN model for speech [11]. This CNN did not work well out-of-the-box, and several features were added to help it perform better. The final model is highly specialized compared to S4, and includes:
- Downsampling or pooling between layers, induced by strided convolutions, that decrease the sequence length between layers.
- A global fully-connected output layer; thus the model only works for one input sequence length and does not work on MFCC features or the frequency-shift setting in Table 5.
- Batch Normalization is essential, whereas S4 works equally well with either Batch Normalization or Layer Normalization.
- Almost 90x as many parameters as the S4 model (26.3M vs. 0.3M).
