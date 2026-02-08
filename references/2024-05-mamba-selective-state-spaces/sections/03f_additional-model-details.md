# Additional Model Details [p. 9]

## Section 3.6

[p. 9]

**Real vs. Complex.** Most prior SSMs use complex numbers in their state $h$, which is necessary for strong performance on many tasks in perceptual modalities (Gu, Goel, and Re 2022). However, it has been empirically observed that completely real-valued SSMs seem to work fine, and possibly even better, in some settings (Ma et al. 2023). The authors use real values as the default, which work well for all but one of their tasks; they hypothesize that the complex-real tradeoff is related to the continuous-discrete spectrum in data modalities, where complex numbers are helpful for continuous modalities (e.g. audio, video) but not discrete (e.g. text, DNA). [p. 9]

**Initialization.** Most prior SSMs also suggest special initializations, particularly in the complex-valued case, which can help in several settings such as low-data regimes. The default initialization for the complex case is S4D-Lin and for the real case is S4D-Real (Gu, Gupta, et al. 2022), which is based on the HIPPO theory (Gu, Dao, et al. 2020). These define the $n$-th element of $\boldsymbol{A}$ as $-1/2 + ni$ and $-(n + 1)$ respectively. However, the authors expect many initializations to work fine, particularly in the large-data and real-valued SSM regimes; some ablations are considered in Section 4.6. [p. 9]

**Parameterization of $\Delta$.** The selective adjustment to $\Delta$ was defined as $s_\Delta(x) = \text{Broadcast}_D(\text{Linear}_1(x))$, which was motivated by the mechanics of $\Delta$ (Section 3.5). The authors observe that it can be generalized from dimension 1 to a larger dimension R. They set this to be a small fraction of D, which uses a negligible number of parameters compared to the main Linear projections in the block. They additionally note that the broadcasting operation can instead be viewed as another Linear projection, initialized to a specific pattern of 1's and 0's; if this projection is trainable, this leads to the alternative $s_\Delta(x) = \text{Linear}_D(\text{Linear}_R(x))$, which can be viewed as a low-rank projection. [p. 9]

In the experiments, the $\Delta$ parameter (which can be viewed as a bias term) is initialized to $\tau_\Delta^{-1}(\text{Uniform}([0.001, 0.1]))$, following prior work on SSMs (Gu, Johnson, Timalsina, et al. 2023). [p. 9]

**Remark 3.1.** *For brevity in our experimental results, we sometimes abbreviate selective SSMs as S6 models, because they are S4 models with a selection mechanism and computed with a scan.* [p. 9]
