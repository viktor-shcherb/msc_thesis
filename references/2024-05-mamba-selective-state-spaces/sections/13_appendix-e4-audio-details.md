# E.4 Audio Details [p. 34–35]

## E.4.1 YouTubeMix Audio Pretraining

[p. 34]

**Model.** A model with 3 blocks per stage ($3 \times 5 = 15$ total Mamba blocks), pooling factor $p = 16$, and outer dimension $D = 64$, for about 3.5M parameters.

**Dataset.** The data is mu-law encoded at 8 bits, so the model is modeling discrete tokens with a vocab size of 256.

The dataset consists of clips of up to 1 minute long, or length 960000, which is subsampled and divided into segments of any desired sequence length. Since the architecture involves two stages of pooling by a factor of 16, and the resulting sequence length must be a multiple of 8 for hardware efficiency, the longest possible sequence is $468 \times 2048 = 958464$. The rest of the sequence lengths are defined by successively halving this and rounding up to the nearest multiple of 2048.

**Table 14:** YouTubeMix length scaling sequence lengths and batch sizes. [p. 34]

| Sequence Length | Batch Size | Tokens / Batch |
|-----------------|------------|----------------|
| $468 \times 2048 = 958464$ | 1 | 958464 |
| $234 \times 2048 = 479232$ | 2 | 958464 |
| $117 \times 2048 = 239616$ | 4 | 958464 |
| $59 \times 2048 = 120832$ | 8 | 966656 |
| $30 \times 2048 = 61440$ | 16 | 983040 |
| $15 \times 2048 = 30720$ | 32 | 983040 |
| $8 \times 2048 = 16384$ | 64 | 1048576 |
| $4 \times 2048 = 8192$ | 128 | 1048576 |

Table 14 lists the specifications used in Figure 7. Beyond the varying batch sizes, the number of valid segments in the training set varied between different sequence lengths (e.g. the number of training steps per epoch was not constant for different points in the graph), which may have contributed to kinks in the scaling curves.

**Training.** Models were trained for $200K$ training steps with a maximum learning rate of 0.002, $20K$ (10%) warmup steps, and weight decay 0.1 (similar to the general pretraining recipe across domains).

**Additional Ablations: SSM Parameterizations.** SSM parameterizations on long-form audio waveform pretraining in the setting of Figure 7 are investigated. The setting is modified slightly to use larger models (8 layers and $D = 64$ for 6M params, the SaShiMi default), shorter sequences ($2^{11} = 2048$ to $2^{18} = 262144$ instead of $2^{13}$ to $2^{20}$), lower LR (0.001 from 0.002), and shorter training cycles (100K instead of 200K steps).

**Figure 10** (p. 35): (Audio Pretraining (YouTubeMix) Ablations.) As a uniformly-sampled "continuous" signal modality, audio waveforms actually benefit from LTI models which have matching inductive bias. (*Left*) Homogenous models (all blocks have the same parameterization). Y-axis: Bits Per Byte. X-axis: Sequence Length (log scale). Lines shown: S4+MLP, Mamba (S6), +complex, +selective B/C, +selective $\Delta$, (Mamba-S4). The S4+MLP baseline performs best at longer sequences; the change from S4 to S6 (the selection mechanism) is not always beneficial on long-form audio waveforms. (*Right*) Only the center U-Net blocks are ablated; the outer blocks are Mamba-S4. Purple line is same as figure on left. Y-axis: Bits Per Byte. X-axis: Sequence Length (log scale). Lines shown: Mamba (S6), +complex, +selective B/C, +selective $\Delta$, (Mamba-S4). Performance differences shrink dramatically when only inner layers are ablated.

[p. 35]

Figure 10 shows that the change from S4 $\to$ S6 (i.e. the selection mechanism) is not always beneficial. On long-form audio waveforms, it in fact significantly hampers performance, which may be intuitive from the point of view that audio is uniformly sampled and very smooth, and therefore benefits from continuous linear time-invariant (LTI) methods. After ablating away the selection mechanism, note that the resulting model is the S4 layer inside the Mamba block. To disambiguate, this is called Mamba-S4 as opposed to the default Mamba architecture Mamba-S6.

However, on the right side, the outer layers of the U-Net Mamba-S4 are kept and only the inner layers are ablated. The performance differences shrink dramatically; this reinforces the hypothesis that layers closer to the *raw* audio signal should be LTI, but once they are "tokenized" and compressed by the outer layers, the inner layers no longer need to be LTI. In this setting however, the real-valued SSM still underperforms the complex-valued one.

## E.4.2 SC09 Speech Generation

[p. 35]

Autoregressive training largely followed the autoregressive language modeling protocol, such as:

- Weight decay 0.1
- Learning rate warmup for 10% of total steps
- AdamW optimizer with $\beta = (0.9, 0.95)$
- Gradient clip value 0.1

A learning rate of 0.002 and 200000 training steps at a batch size of 16 were used.

The large Mamba model in Table 4 has 15 layers per stage with an outer dimension of $D = 96$ and pooling factor 4. Note that this dataset is small (training went through 100 epochs) and for this large model, there was significant overfitting of the BPB or NLL. However, automated metrics of generated samples continually improving throughout training.

The models in the architecture ablations in Table 5 all have 8 layers per stage with an outer dimension of $D = 64$ and pooling factor 4. The S4+MLP block has roughly $2D^2 + 4D^2$ parameters (expansion factor 2 in the MLP). The Transformer block has $4D^2 + 2D^2$ parameters (expansion factor 1 in the MLP). The Mamba block has the usual $\approx 6D^2$ parameters. All models have roughly 6M total parameters.
