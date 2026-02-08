# 4 Experiments [p. 7-11]

[p. 7]

Section 4.1 benchmarks S4 against the LSSL and efficient Transformer models. Section 4.2 validates S4 on LRDs: the LRA benchmark and raw speech classification. Section 4.3 investigates whether S4 can be used as a general sequence model to perform effectively and efficiently in a wide variety of settings including image classification, image and text generation, and time series forecasting.

## 4.1 S4 Efficiency Benchmarks

[p. 7-8]

S4 can be trained quickly and efficiently, both compared to the LSSL, as well as efficient Transformer variants designed for long-range sequence modeling. As outlined in Section 3, S4 is theoretically much more efficient than the LSSL, and Table 2 confirms that the S4 is orders of magnitude more speed- and memory-efficient for practical layer sizes. S4's speed and memory use is competitive with the most efficient Transformer variants benchmarked by Tay et al. [40] -- Linear Transformer [22] and Performer [8] -- in a parameter-matched setting (Table 3, following the protocol of Tay et al. [40]).

### Table 2: Deep SSMs Efficiency

[p. 8]

**Table 2** (p. 8): "Deep SSMs: The S4 parameterization with Algorithm 1 is asymptotically more efficient than the LSSL."

|       | Training Step (ms) |       |       | Memory Alloc. (MB) |       |       |
|-------|--------------------|-------|-------|--------------------|-------|-------|
| Dim.  | 128                | 256   | 512   | 128                | 256   | 512   |
| LSSL  | 9.32               | 20.6  | 140.7 | 222.1              | 1685  | 13140 |
| S4    | 4.77               | 3.07  | 4.75  | 5.3                | 12.6  | 33.5  |
| Ratio | 1.9x               | 6.7x  | **29.6x** | 42.0x          | 133x  | **392x** |

### Table 3: Benchmarks vs. Efficient Transformers

[p. 8]

**Table 3** (p. 8): "Benchmarks vs. efficient Transformers"

|                | Length 1024 |        | Length 4096 |         |
|----------------|-------------|--------|-------------|---------|
|                | Speed       | Mem.   | Speed       | Mem.    |
| Transformer    | 1x          | 1x     | 1x          | 1x      |
| Performer      | 1.23x       | 0.43x  | 3.79x       | 0.086x  |
| Linear Trans.  | **1.58x**   | **0.37x** | **5.35x** | **0.067x** |
| S4             | **1.58x**   | 0.43x  | 5.19x       | 0.091x  |

## 4.2 Learning Long Range Dependencies

[p. 8-9]

As described in Sections 2.2 and 3.1, S4 uses a principled approach to address LRDs based on the HiPPO theory of continuous-time memorization. The goal in this section is to validate that S4 achieves high performance on difficult tasks that require long-range reasoning. The focus is on two problems: (i) the Long-Range Arena, a well-known benchmark designed to test efficient sequence models on LRDs, and (ii) a speech classification problem as a real-world test of LRDs.

### Long Range Arena (LRA)

[p. 8-9]

LRA [40] contains 6 tasks with lengths 1K-16K steps, encompassing modalities and objectives that require similarity, structural, and visuospatial reasoning. Table 4 compares S4 against the 11 Transformer variants from Tay et al. [40] as well as follow-up work. S4 substantially advances the SoTA, outperforming all baselines on all tasks and averaging 80.48% compared to less than 60% for every baseline. Notably, S4 solves the Path-X task, an extremely challenging task that involves reasoning about LRDs over sequences of length 128 x 128 = 16384. All previous models have failed (i.e. random guessing) due to memory or computation bottlenecks, or simply being unable to learn such long dependencies.

S4's performance on Path-X is analyzed by visualizing its learned representations, in particular 1-D convolution kernels **K-bar** which are the focus of the technical results in Section 3. Fig. 2 shows that S4 learns a variety of filters that display spatially consistent structure and demonstrate awareness of the 2-D nature of the data. In particular, the lower layers learn simple kernels that extract features from just a few rows of local context while ignoring the rest of the image. On the other hand, higher layers aggregate information globally across full columns of the image at varying spatial frequencies. Filters in these higher layers span the entire context (16384 pixels), confirming S4's ability to learn LRDs.

### Figure 2

**Figure 2** (p. 8): "Visualizations of a trained S4 model on LRA Path-X. SSM convolution kernels **K-bar** in R^{16,384} are reshaped into a 128 x 128 image. (*Left*) Example from the Path-X task, which involves deducing if the markers are connected by a path (*Top*) Filters from the first layer (*Bottom*) Filters from the last layer."

The figure shows: (Left) a Path-X input image with dashed paths connecting markers on a dark background. (Middle, Top row) First-layer filters reshaped to 128x128 showing local, horizontally-banded patterns that capture nearby context. (Middle and Right, Bottom row) Last-layer filters showing global, vertically-oriented columnar patterns spanning the full image, indicating the model learns to aggregate information across the entire 16384-length sequence.

### Table 4: Long Range Arena

[p. 8]

**Table 4** (p. 8): "(Long Range Arena) (*Top*) Original Transformer variants in LRA. Full results in Appendix D.2. (*Bottom*) Other models reported in the literature. *Please read Appendix D.5 before citing this table.*"

| Model           | ListOps | Text  | Retrieval | Image | Pathfinder | Path-X | Avg   |
|-----------------|---------|-------|-----------|-------|------------|--------|-------|
| Transformer     | 36.37   | 64.27 | 57.46     | 42.44 | 71.40      | X      | 53.66 |
| Reformer        | 37.27   | 56.10 | 53.40     | 38.07 | 68.50      | X      | 50.56 |
| BigBird         | 36.05   | 64.02 | 59.29     | 40.83 | 74.87      | X      | 54.17 |
| Linear Trans.   | 16.13   | 65.90 | 53.09     | 42.34 | 75.30      | X      | 50.46 |
| Performer       | 18.01   | 65.40 | 53.82     | 42.77 | 77.05      | X      | 51.18 |
| FNet            | 35.33   | 65.11 | 59.61     | 38.67 | 77.80      | X      | 54.42 |
| Nystromformer   | 37.15   | 65.52 | 79.56     | 41.58 | 70.94      | X      | 57.46 |
| Luna-256        | 37.25   | 64.57 | 79.29     | 47.38 | 77.72      | X      | 59.37 |
| **S4**          | **59.60** | **86.82** | **90.90** | **88.65** | **94.20** | **96.35** | **86.09** |

X denotes failure on the task (random guessing or inability to run).

### Raw Speech Classification

[p. 9]

Speech is a typical real-world time series domain, involving signals sampled from an underlying physical process at high frequency. Speech classification is performed using the SC10 subset of the *Speech Commands* dataset [47] (see Appendix D.5). While most sequence models for speech rely on extensive preprocessing (e.g. to MFCC features), raw speech (length-16000) is classified following Romero et al. [35]. S4 achieves 98.3% accuracy, higher than all baselines that use the 100x shorter MFCC features, and validates that a powerful LRD model is able to extract more information from the raw data and outperform hand-crafted pre-processing. Additionally, a baseline CNN specifically designed for raw speech is included, the discriminator from the WaveGAN model [11], which performs worse than S4 while having 90x more parameters and incorporating many more architectural heuristics (Appendix D.2).

### Table 5: SC10 Speech Classification

[p. 9]

**Table 5** (p. 9): "(SC10 classification) Transformer, CTM, RNN, CNN, and SSM models. (*MFCC*) Standard preprocessed MFCC features (length 161). (*Raw*) Unprocessed signals (length 16000). (*0.5x*) Frequency change at test time. X denotes not applicable or computationally infeasible on single GPU. *Please read Appendix D.5 before citing this table.*"

| Model        | MFCC   | Raw    | 0.5x   |
|--------------|--------|--------|--------|
| Transformer  | 90.75  | X      | X      |
| Performer    | 80.85  | 30.77  | 30.68  |
| ODE-RNN      | 65.9   | X      | X      |
| NRDE         | 89.8   | 16.49  | 15.12  |
| ExpRNN       | 82.13  | 11.6   | 10.8   |
| LipschitzRNN | 88.38  | X      | X      |
| CKConv       | **95.3** | 71.66 | 65.96  |
| WaveGAN-D    | X      | 96.25  | X      |
| LSSL         | 93.58  | X      | X      |
| **S4**       | 93.96  | **98.32** | **96.30** |

## 4.3 S4 as a General Sequence Model

[p. 9-10]

A key goal of sequence modeling research is to develop a single model that can be applied in many domains (e.g. images, audio, text, time-series) with a broad range of capabilities (e.g. efficient training, fast generation, handling irregularly sampled data). As a fundamental scientific model, SSMs are a promising candidate that come with a range of capabilities, and S4's strong results on LRD benchmarks spanning images, text, and speech are evidence of S4's potential as a general sequence model. This section focuses on understanding this question in more depth by highlighting key strengths of S4 in settings that usually require specialized models.

### Large-scale Generative Modeling

[p. 10]

The scalability, flexibility, and efficiency of S4 are investigated on two well-studied image and text benchmarks. These tasks require much larger models than previous tasks -- up to 250M parameters.

**CIFAR density estimation:** CIFAR density estimation is a popular benchmark for autoregressive models, where images are flattened into a sequence of 3072 RGB subpixels that are predicted one by one. Table 7 shows that *with no 2D inductive bias*, S4 is competitive with the best models designed for this task.

**WikiText-103 language modeling:** WikiText-103 is an established benchmark for language modeling, an important task for large-scale sequence models where tokens are predicted sequentially based on past context. Although RNNs were the model of choice for many years, Transformers are now the dominant model in such applications that contain data that is inherently discrete. The authors show that alternative models to Transformers can still be competitive in these settings. By simply taking a strong Transformer baseline [2] and replacing the self-attention layers, S4 substantially closes the gap to Transformers (within 0.8 ppl), setting SoTA for attention-free models by over 2 ppl.

### Table 7: CIFAR-10 Density Estimation

[p. 10]

**Table 7** (p. 10): "(CIFAR-10 density estimation) As a generic sequence model, S4 is competitive with previous autoregressive models (in bits per dim.) while incorporating no 2D inductive bias, and has fast generation through its recurrence mode."

| Model          | bpd   | 2D bias          | Images / sec        |
|----------------|-------|------------------|---------------------|
| Transformer    | 3.47  | **None**         | 0.32 (1x)           |
| Linear Transf. | 3.40  | **None**         | 17.85 (56x)         |
| PixelCNN       | 3.14  | 2D conv.         | -                    |
| Row PixelRNN   | 3.00  | 2D BiLSTM        | -                    |
| PixelCNN++     | 2.92  | 2D conv.         | 19.19 (59.97x)      |
| Image Transf.  | 2.90  | 2D local attn.   | 0.54 (1.7x)         |
| PixelSNAIL     | **2.85** | 2D conv. + attn. | 0.13 (0.4x)      |
| Sparse Transf. | 2.80  | 2D sparse attn.  | -                    |
| **S4** (base)  | 2.92  | **None**         | **20.84 (65.1x)**   |
| **S4** (large) | **2.85** | **None**     | 3.36 (10.5x)        |

### Table 8: WikiText-103 Language Modeling

[p. 10]

**Table 8** (p. 10): "(WikiText-103 language modeling) S4 approaches the performance of Transformers with much faster generation. (*Top*) Transformer baseline which our implementation is based on, with attention replaced by S4. (*Bottom*) Attention-free models (RNNs and CNNs)."

| Model          | Params | Test ppl. | Tokens / sec   |
|----------------|--------|-----------|----------------|
| Transformer    | 247M   | **20.51** | 0.8K (1x)      |
| GLU CNN        | 229M   | 37.2      | -              |
| AWD-QRNN       | 151M   | 33.0      | -              |
| LSTM + Hebb.   | -      | 29.2      | -              |
| TrellisNet     | 180M   | 29.19     | -              |
| Dynamic Conv.  | 255M   | 25.0      | -              |
| TaLK Conv.     | 240M   | 23.3      | -              |
| **S4**         | 249M   | **20.95** | **48K (60x)**  |

### Fast Autoregressive Inference

[p. 10]

A prominent limitation of autoregressive models is inference speed (e.g. generation), since they require a pass over the full context for every new sample. Several methods have been specifically crafted to overcome this limitation such as the Linear Transformer, a hybrid Transformer/RNN that switches to a stateful, recurrent view at inference time for speed.

As a stateful model, SSMs automatically have this ability (Fig. 1). By switching to its recurrent representation (Section 2.3), S4 requires *constant memory and computation* per time step -- in contrast to standard autoregressive models which scale in the context length. On both CIFAR-10 and WikiText-103, the throughput of various models at generation time is reported, with S4 around 60x faster than a vanilla Transformer on both tasks (details in Appendix D.3.3).

### Sampling Resolution Change

[p. 10]

As a continuous-time model, S4 automatically adapts to data sampled at different rates, a challenging setting for time series with a dedicated line of work [10, 35, 37]. Without re-training, S4 achieves 96.3% accuracy at 0.5x the frequency on Speech Commands 10 (Table 5), simply by changing its internal step size Delta (Section 2.3).

### Learning with Weaker Inductive Bias

[p. 10-11]

Beyond results on speech (Section 4.2), S4 can be applied with minimal modifications on two domains that typically require specialized domain-specific preprocessing and architectures. First, S4 is compared to the Informer [50], a new Transformer architecture that uses a complex encoder-decoder designed for time-series forecasting problems. A simple application of S4 that treats forecasting as a masked sequence-to-sequence transformation (Fig. 5) outperforms the Informer and other baselines on 40/50 settings across 5 forecasting tasks. Notably, S4 is better on the longest setting in each task, e.g. reducing MSE by 37% when forecasting 30 days of weather data (Table 9).

[p. 11]

Second, S4 is evaluated on pixel-level sequential image classification tasks (Table 6), popular benchmarks which were originally LRD tests for RNNs [1]. Beyond LRDs, these benchmarks point to a recent effort of the ML community to solve vision problems with reduced domain knowledge, in the spirit of models such as Vision Transformers [12] and MLP-Mixer [41] which involve patch-based models that without 2-D inductive bias. Sequential CIFAR is a particularly challenging dataset where outside of SSMs, all sequence models have a gap of over 25% to a simple 2-D CNN. By contrast, S4 is competitive with a larger ResNet18 (7.9M vs. 11.0M parameters), both with (**93.16%** vs. 95.62%) or without (**91.12%** vs. 89.46%) data augmentation. Moreover, it is much more robust to other architectural choices (e.g. **90.46%** vs. 79.52% when swapping BatchNorm for LayerNorm).

### Table 6: Pixel-level 1-D Image Classification

[p. 9]

**Table 6** (p. 9): "(Pixel-level 1-D image classification) Comparison against reported test accuracies from prior works (Transformer, RNN, CNN, and SSM models). Extended results and citations in Appendix D."

| Model         | sMNIST | pMNIST | sCIFAR |
|---------------|--------|--------|--------|
| Transformer   | 98.9   | 97.9   | 62.2   |
| LSTM          | 98.9   | 95.11  | 63.01  |
| r-LSTM        | 98.4   | 95.2   | 72.2   |
| UR-LSTM       | 99.28  | 96.96  | 71.00  |
| UR-GRU        | 99.27  | 96.51  | 74.4   |
| HiPPO-RNN     | 98.9   | 98.3   | 61.1   |
| LMU-FFT       | -      | 98.49  | -      |
| LipschitzRNN  | 99.4   | 96.3   | 64.2   |
| TCN           | 99.0   | 97.2   | -      |
| TrellisNet    | 99.20  | 98.13  | 73.42  |
| CKConv        | 99.32  | 98.54  | 63.74  |
| LSSL          | 99.53  | **98.76** | 84.65 |
| **S4**        | **99.63** | 98.70 | **91.13** |
