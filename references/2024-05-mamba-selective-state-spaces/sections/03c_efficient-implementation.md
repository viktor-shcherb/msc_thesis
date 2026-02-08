# Efficient Implementation of Selective SSMs [p. 6]

## Section 3.3

[p. 6]

Hardware-friendly primitives such as convolutions (Krizhevsky, Sutskever, and Hinton 2012) and attention (Bahdanau, Cho, and Bengio 2015; Vaswani et al. 2017) enjoy widespread application. The authors aim to make selective SSMs efficient on modern hardware (GPUs) as well. The selection mechanism is quite natural, and earlier works attempted to incorporate special cases of selection, such as letting $\Delta$ vary over time in recurrent SSMs (Gu, Dao, et al. 2020). However, as previously mentioned a core limitation in the usage of SSMs is their computational efficiency, which was why S4 and all derivatives used LTI (non-selective) models, most commonly in the form of global convolutions.

## 3.3.1 Motivation of Prior Models

[p. 6]

The authors first revisit the motivation and overview their approach to overcome limitations of prior methods:

- At a high level, recurrent models such as SSMs always balance a tradeoff between expressivity and speed: as discussed in Section 3.1, models with larger hidden state dimension should be more effective but slower. Thus the goal is to *maximize hidden state dimension without paying speed and memory costs*.

- Note that the recurrent mode is more flexible than the convolution mode, since the latter (3) is derived from expanding the former (2) (Gu, Goel, and Re 2022; Gu, Johnson, Goel, et al. 2021). However, this would require computing and materializing the latent state $h$ with shape $(B, L, D, N)$, which is much larger (by a factor of $N$, the SSM state dimension) than the input $x$ and output $y$ of shape $(B, L, D)$. Thus the more efficient convolution mode was introduced which could bypass the state computation and materializes a convolution kernel (3a) of size only $(B, L, D)$.

- Prior LTI state space models leverage the dual recurrent-convolutional forms to increase the effective state dimension by a factor of $N$ ($\approx 10 - 100$), much larger than traditional RNNs, without efficiency penalties.

---
[p. 7 continued]

## 3.3.2 Overview of Selective Scan: Hardware-Aware State Expansion

The selection mechanism is designed to overcome the limitations of LTI models; at the same time, it requires revisiting the computation problem of SSMs. The authors address this with three classical techniques: kernel fusion, parallel scan, and recomputation. Two main observations: [p. 7]

- The naive recurrent computation uses $O(BLDN)$ FLOPs while the convolutional computation uses $O(BLD \log(L))$ FLOPs, and the former has a lower constant factor. Thus for long sequences and not-too-large state dimension $N$, the recurrent mode can actually use fewer FLOPs.

- The two challenges are the sequential nature of recurrence, and the large memory usage. To address the latter, just like the convolutional mode, the authors attempt to not actually materialize the full state $h$.

The main idea is to leverage properties of modern accelerators (GPUs) to materialize the state $h$ only in more efficient levels of the memory hierarchy. In particular, most operations (except matrix multiplication) are bounded by memory bandwidth (Dao, Fu, Ermon, et al. 2022; Ivanov et al. 2021; Williams, Waterman, and Patterson 2009). This includes the scan operation, and kernel fusion is used to reduce the amount of memory IOs, leading to a significant speedup compared to a standard implementation. [p. 7]

Concretely, instead of preparing the scan input $(\overline{\boldsymbol{A}}, \overline{\boldsymbol{B}})$ of size $(B, L, D, N)$ in GPU HBM (high-bandwidth memory), the SSM parameters $(\Delta, \boldsymbol{A}, \boldsymbol{B}, \boldsymbol{C})$ are loaded directly from slow HBM to fast SRAM, the discretization and recurrence are performed in SRAM, and then the final outputs of size $(B, L, D)$ are written back to HBM. [p. 7]

To avoid the sequential recurrence, the authors observe that despite not being linear it can still be parallelized with a work-efficient parallel scan algorithm (Blelloch 1990; Martin and Cundy 2018; Smith, Warrington, and Linderman 2023). [p. 7]

Finally, to avoid saving the intermediate states (which are necessary for backpropagation), the classic technique of recomputation is applied to reduce memory requirements: the intermediate states are not stored but recomputed in the backward pass when the inputs are loaded from HBM to SRAM. As a result, the fused selective scan layer has the same memory requirements as an optimized transformer implementation with FlashAttention. [p. 7]

Details of the fused kernel and recomputation are in Appendix D. The full Selective SSM layer and algorithm is illustrated in Figure 1. [p. 7]
