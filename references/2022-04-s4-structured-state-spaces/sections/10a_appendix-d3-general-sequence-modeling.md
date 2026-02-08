# D.3 General Sequence Modeling [p. 27–30]

[p. 27]

This subsection corresponds to the experiments in Section 4.3. Because of the number of experiments in this section, subsubsection dividers for different tasks are used: CIFAR-10 density estimation (Appendix D.3.1), WikiText-103 language modeling (Appendix D.3.2), autoregressive generation (Appendix D.3.3), sequential image classification (Appendix D.3.4), and time-series forecasting (Appendix D.3.5).

## D.3.1 CIFAR Density Estimation

[p. 28]

This task used a different backbone than the rest of the experiments. Blocks of alternating S4 layers and position-wise feed-forward layers (in the style of Transformer blocks) were used. Each feed-forward intermediate dimension was set to 2x the hidden size of the incoming S4 layer. Similar to Salimans et al. [39], a UNet-style backbone consisting of $B$ identical blocks followed by a downsampling layer was used. The downsampling rates were 3, 4, 4 (the 3 chosen because the sequence consists of RGB pixels). The base model had $B = 8$ with starting hidden dimension 128, while the large model had $B = 16$ with starting hidden dimension 192.

Both the mixture of logistics from [39] as well as a simpler 256-way categorical loss were experimented with. The simpler softmax loss along with using input embeddings was found to be pretty close and was used.

The LAMB optimizer with learning rate 0.005 was used. The base model had no dropout, while the large model had dropout 0.1 before the linear layers inside the S4 and FF blocks.

## D.3.2 WikiText-103 Language Modeling

[p. 28]

The RNN baselines included in Table 8 are the AWD-QRNN [27], an efficient linear gated RNN, and the LSTM + Cache + Hebbian + MbPA [33], the best performing pure RNN in the literature. The CNN baselines are the CNN with GLU activations [9], the TrellisNet [4], Dynamic Convolutions [49], and TaLK Convolutions [26].

The Transformer baseline is [2], which uses Adaptive Inputs with a tied Adaptive Softmax. This model is a standard high-performing Transformer baseline on this benchmark, used for example by Lioutas and Guo [26] and many more.

The S4 model uses the same Transformer backbone as in [2]. The model consists of 16 blocks of S4 layers alternated with position-wise feedforward layers, with a feature dimension of 1024. Because the S4 layer has around 1/4 the number of parameters as a self-attention layer with the same dimension, two modifications were made to match the parameter count better: (i) a GLU activation was used after the S4 linear layer (Section 3.4); (ii) two S4 layers per block were used. Blocks use Layer Normalization in the pre-norm position. The embedding and softmax layers were the Adaptive Embedding from [2] with standard cutoffs 20000, 40000, 200000.

Evaluation was performed similarly to the basic setting in [2], Table 5, which uses sliding non-overlapping windows. Other settings are reported in [2] that include more context at training and evaluation time and improve the score. Because such evaluation protocols are orthogonal to the basic model, they are not considered, and the base score from [2] Table 5 is reported.

Instead of SGD+Momentum with multiple cosine learning rate annealing cycles, the S4 model was trained with the simpler AdamW optimizer with a single cosine learning rate cycle with a maximum of 800000 steps. The initial learning rate was set to 0.0005. 8 A100 GPUs were used with a batch size of 1 per gpu and context size 8192. No gradient clipping was used and a weight decay of 0.1 was applied. Unlike [2] which specified different dropout rates for different parameters, a constant dropout rate of 0.25 was used throughout the network, including before every linear layer and on the residual branches.

## D.3.3 Autoregressive Generation Speed

[p. 28–29]

**Protocol.** To account for different model sizes and memory requirements for each method, generation speed is benchmarked by throughput, measured in images per second (Table 7) or tokens per second (Table 8). Each model generates images on a single A100 GPU, maximizing batch size to fit in memory. (For CIFAR-10 generation, memory was limited to 16Gb, to be more comparable to the Transformer and Linear Transformer results reported from [22].)

### Table 12: Pixel-Level Image Classification

**Table 12** (p. 29): "(Pixel-level image classification.) Citations refer to the original model; additional citation indicates work from which this baseline is reported."

| Model                       | sMNIST | pMNIST | sCIFAR |
|-----------------------------|--------|--------|--------|
| Transformer [42] [44]       | 98.9   | 97.9   | 62.2   |
| CKConv [35]                 | 99.32  | 98.54  | 63.74  |
| TrellisNet [4]              | 99.20  | 98.13  | 73.42  |
| TCN [3]                     | 99.0   | 97.2   | -      |
| LSTM [17] [21]              | 98.9   | 95.11  | 63.01  |
| r-LSTM [42]                 | 98.4   | 95.2   | 72.2   |
| Dilated GRU [5]             | 99.0   | 94.6   | -      |
| Dilated RNN [5]             | 98.0   | 96.1   | -      |
| IndRNN [25]                 | 99.0   | 96.0   | -      |
| expRNN [24]                 | 98.7   | 96.6   | -      |
| UR-LSTM                     | 99.28  | 96.96  | 71.00  |
| UR-GRU [17]                 | 99.27  | 96.51  | 74.4   |
| LMU [45]                    | -      | 97.15  | -      |
| HiPPO-RNN [16]              | 98.9   | 98.3   | 61.1   |
| UNIcoRNN [38]               | -      | 98.4   | -      |
| LMUFFT [7]                  | -      | 98.49  | -      |
| LipschitzRNN [13]           | 99.4   | 96.3   | 64.2   |
| **S4**                      | **99.63** | **98.70** | **91.13** |

**Baselines.** The Transformer and Linear Transformer baselines reported in Table 7 are the results reported directly from Katharopoulos et al. [22]. Note that the Transformer number is the one in their Appendix, which implements the optimized cached implementation of self-attention.

[p. 29]

For all other baseline models, open source implementations of the models were used to benchmark generation speed. For the PixelCNN++, the fast cached version by Ramachandran et al. [34] was used, which sped up generation by orders of magnitude from the naive implementation. This code was only available in TensorFlow, which may have slight differences compared to the rest of the baselines which were implemented in PyTorch.

The Sparse Transformer [6] model could not be run due to issues with their custom CUDA implementation of the sparse attention kernel.

The Transformer baseline from Table 8 was run using a modified GPT-2 backbone from the HuggingFace repository, configured to recreate the architecture reported in [2]. These numbers are actually slightly favorable to the baseline, as the timing of the embedding or softmax layers was not included, whereas the number reported for S4 is the full model.

## D.3.4 Pixel-Level Sequential Image Classification

[p. 29]

Models were trained with the AdamW optimizer for up to 200 epochs. Hyperparameters for the CIFAR-10 model are reported in Table 11.

For comparisons against ResNet-18, the main differences between the base models are that S4 uses LayerNorm by default while ResNet uses BatchNorm. The last ablation in Section 4.3 swaps the normalization type, using BatchNorm for S4 and LayerNorm for ResNet, to ablate this architectural difference. The experiments with augmentation take the base model and train with mild data augmentation: horizontal flips and random crops (with symmetric padding).
