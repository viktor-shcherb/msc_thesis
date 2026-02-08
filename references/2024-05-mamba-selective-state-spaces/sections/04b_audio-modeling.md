# 4.4 Audio Modeling and Generation [p. 14–15]

[p. 14]

For the audio waveform modality, the authors compare primarily to the SaShiMi architecture and training protocols (Goel et al. 2022). This model comprises:

1. a U-Net backbone with two stages of pooling by a factor $p$ that doubles the model dimension $D$ per stage,
2. alternating S4 and MLP blocks in each stage.

The authors consider replacing the S4+MLP blocks with Mamba blocks. Experiment details are in Appendix E.4. [p. 14]

## 4.4.1 Long-Context Autoregressive Pretraining

[p. 14]

The authors evaluate pretraining quality (autoregressive next-sample prediction) on YouTubeMix (DeepSound 2017), a standard piano music dataset used by prior work consisting of 4 hours of solo piano music, sampled at a rate of 16000 Hz. Pretraining details largely follow the standard language modeling setup (Section 4.2). Figure 7 evaluates the effect of increasing training sequence lengths from $2^{13} = 8192$ to $2^{20} \approx 10^6$, while keeping computation fixed. (There are some slight edge cases to the way the data is curated, which may lead to kinks in the scaling curves. For example, only minute-long clips were available so the maximum sequence length is actually bounded by $60s \cdot 16000Hz = 960000$.) [p. 14]

> "**Both Mamba and the SaShiMi (S4+MLP) baseline improve consistently with longer context lengths; Mamba is better throughout, and the gap widens at longer lengths.**" The main metric is bits per byte (BPB), which is a constant factor $\log(2)$ of the standard negative log-likelihood (NLL) loss for pretraining other modalities. [p. 14]

The authors note one important detail: this is the only experiment in this paper in which they switched from the real parameterization to complex (Section 3.6). Additional ablations are shown in Appendix E.4. [p. 14]

## 4.4.2 Autoregressive Speech Generation

[p. 14]

SC09 is a benchmark speech generation dataset (Donahue, McAuley, and Puckette 2019; Warden 2018), consisting of 1-second clips sampled at 16000 Hz of the digits "zero" through "nine" with highly variable characteristics. The authors largely follow the autoregressive training setup and generation protocol of Goel et al. (2022). [p. 14]

Table 4 shows automated metrics of the Mamba-UNet model compared to a variety of baselines from Goel et al. (2022): WaveNet (Oord et al. 2016), SampleRNN (Mehri et al. 2017), WaveGAN (Donahue, McAuley, and Puckette 2019), DiffWave (Z. Kong et al. 2021), and SaShiMi. > "**A small Mamba model outperforms the state-of-the-art (and much larger) GAN- and diffusion-based models.**" A larger model parameter-matched to the baselines further improves on fidelity metrics dramatically. [p. 14]

Table 5 takes the small Mamba model and investigates combinations of different architectures for the outer stages and center stage. It shows that Mamba is consistently better than S4+MLP in the outer blocks, and Mamba > S4+MLP > MHA+MLP in the center blocks. [p. 14]

## Tables

**Table 4** (p. 15): "(**SC09**) Automated metrics for unconditional generation on a challenging dataset of fixed-length speech clips. (*Top to Bottom*) Autoregressive baselines, non-autoregressive baselines, Mamba, and dataset metrics."

| Model | Params | NLL ↓ | FID ↓ | IS ↑ | mIS ↑ | AM ↓ |
|-------|--------|-------|-------|------|-------|------|
| SampleRNN | 35.0M | 2.042 | 8.96 | 1.71 | 3.02 | 1.76 |
| WaveNet | 4.2M | 1.925 | 5.08 | 2.27 | 5.80 | 1.47 |
| SaShiMi | 5.8M | 1.873 | 1.99 | 5.13 | 42.57 | 0.74 |
| WaveGAN | 19.1M | – | 2.03 | 4.90 | 36.10 | 0.80 |
| DiffWave | 24.1M | – | 1.92 | 5.26 | 51.21 | 0.68 |
| + SaShiMi | 23.0M | – | 1.42 | 5.94 | 69.17 | 0.59 |
| **Mamba** | **6.1M** | **1.852** | **0.94** | **6.26** | **88.54** | **0.52** |
| **Mamba** | **24.3M** | **1.860** | **0.67** | **7.33** | **144.9** | **0.36** |
| Train | – | – | 0.00 | 8.56 | 292.5 | 0.16 |
| Test | – | – | 0.02 | 8.33 | 257.6 | 0.19 |

**Table 5** (p. 15): "(**SC09 Model Ablations**) Models with 6M parameters. In SaShiMi's U-Net backbone, there are 8 center blocks operating on sequence length 1000, sandwiched on each side by 8 outer blocks on sequence length 4000, sandwiched by 8 outer blocks on sequence length 16000 (40 blocks total). The architecture of the 8 center blocks are ablated independently of the rest. Note that Transformers (MHA+MLP) were not tested in the more important outer blocks because of efficiency constraints."

| Outer | Center | NLL ↓ | FID ↓ | IS ↑ | mIS ↑ | AM ↓ |
|-------|--------|-------|-------|------|-------|------|
| S4+MLP | MHA+MLP | 1.859 | 1.45 | 5.06 | 47.03 | 0.70 |
| S4+MLP | S4+MLP | 1.867 | 1.43 | 5.42 | 53.54 | 0.65 |
| S4+MLP | Mamba | 1.859 | 1.42 | 5.71 | 56.51 | 0.64 |
| Mamba | MHA+MLP | **1.850** | 1.37 | 5.63 | 58.23 | 0.62 |
| Mamba | S4+MLP | 1.853 | **1.07** | **6.05** | **73.34** | **0.55** |
| Mamba | Mamba | 1.852 | 0.94 | 6.26 | 88.54 | 0.52 |

## Figures

**Figure 7** (p. 14): "(**Audio Pretraining.**) Mamba improves performance over prior state-of-the-art (Sashimi) in autoregressive audio modeling, while improving up to minute-long context or million-length sequences (controlling for computation)."

The figure shows:
- x-axis: Sequence Length (log scale, from $10^4$ to $10^6$)
- y-axis: Bits Per Byte (ranging roughly from 1.300 to 1.475)
- Two models: S4+FFN (blue) and Mamba (orange)
- Both models improve (lower BPB) with increasing sequence length. Mamba achieves lower BPB than S4+FFN at every sequence length, and the gap widens at longer lengths. At the longest sequence lengths (~$10^6$), Mamba reaches approximately 1.300 BPB while S4+FFN is around 1.350 BPB.
