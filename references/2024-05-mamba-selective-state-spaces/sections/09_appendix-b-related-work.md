# Appendix B: Related Work [p. 24–26]

[p. 24]

The authors overview several prior works related to their methods. They mention that some of the most closely related models include recurrent layers such as S4, S5, and quasi-RNNs; as well as end-to-end architectures such as H3, RetNet, and RWKV.

## B.1 S4 Variants and Derivatives

[p. 25]

A brief overview of structured SSMs from past work, particularly those with a relation to the authors' method:

- **S4** (Gu, Goel, and Re 2022; Gu, Johnson, Goel, et al. 2021) introduced the first structured SSM, describing diagonal structure and diagonal plus low-rank (DPLR). It focused on efficient convolutional algorithms for DPLR SSMs due to a connection to continuous-time online memorization (HIPPO) (Gu, Dao, et al. 2020).

- **DSS** (Gupta, Gu, and Berant 2022) first discovered the empirical effectiveness of diagonal structured SSMs by approximating the HIPPO initialization. This was expanded on theoretically in S4D (Gu, Gupta, et al. 2022).

- **S5** (Smith, Warrington, and Linderman 2023) independently discovered the diagonal SSM approximation, and is the first S4 model to be computed recurrently with the parallel scan. However, this required lowering the effective state dimension, which they accomplished by switching the SSM dimensions from a SISO (single-input single-output) to MIMO (multi-input multi-output) formulation. The proposed S6 differs by (i) keeping the SISO dimensions, which provides a larger effective recurrent state, (ii) using a hardware-aware algorithm to overcome the computation issue, (iii) adding the selection mechanism.

- **Lu et al. (2023)** applied S5 to meta-RL in order to handle resetting the SSM state between episode trajectories. Their mechanism can be viewed as a particular hard-coded instance of a selection mechanism, where $\overline{A}$ is manually set to 0, instead of the authors' learnable mechanism that depends on the input. It would be interesting to apply selective SSMs generically to this setting and probe if the model has learned to automatically reset its state on episode boundaries.

- **Mega** (Ma et al. 2023) introduced a simplification of S4 to be real- instead of complex-valued, giving it an interpretation of being an exponential moving average (EMA). They additionally make an interesting connection of the discretization step of SSMs to an EMA *damping* term. Contrary to findings in the original S4 papers, this was the first model to show that real-valued SSMs are empirically effective in certain settings or when combined with different architectural components.

- **Liquid S4** (Hasani et al. 2023) is also motivated by augmenting S4 with an input-dependent state transition. From this perspective it shares similarity to selection mechanisms, although in a limited form which is still computed convolutionally and close to LTI.

- **SGConv** (Y. Li et al. 2023), **Hyena** (Poli et al. 2023), **LongConv** (Fu et al. 2023), **MultiresConv** (J. Shi, K. A. Wang, and Fox 2023), and **Toeplitz Neural Network** (Qin, Han, W. Sun, B. He, et al. 2023) all focus on the convolutional representation of S4 and create global or long convolution kernels with different parameterizations. However, these methods cannot do fast autoregressive inference directly.

Notably, all of these methods, and all other structured SSMs that the authors are aware of, have been non-selective and usually strictly LTI (linear time invariant). [p. 25]

## B.2 SSM Architectures

[p. 25]

SSM architectures or state space neural networks (SSNN) refer to deep neural network architectures incorporating one of the previous SSMs as a black box layer:

- **GSS** (Mehta et al. 2023) was the first gated neural network architecture incorporating SSMs. It is motivated by the gated attention unit (GAU) of Hua et al. (2022) and looks quite similar to the Mamba block, except with additional projections. Most importantly, its projection *contracts* the model dimension to reduce the state size of the SSM, while Mamba's *expands* the model dimension in order to increase the state size, based on the motivation in Section 3.1.

- **Mega** (Ma et al. 2023) combined the EMA simplification of S4 described above into a hybrid architecture using an efficient attention approximation.

- **H3** (Dao, Fu, Saab, et al. 2023) is motivated by combining S4 with linear attention (Katharopoulos et al. 2020). It is the first to generalize this formulation of linear attention to more general recurrences, which is also the basis of later architectures.

- **Selective S4** (J. Wang et al. 2023) incorporates S4 as a black box to generate a binary mask which is multiplied on the input. While sharing the "selection" name, the authors consider this an architectural modification that is closer to architectural gating than a selection mechanism (Appendix A). For example, they hypothesize that it would not solve the Selective Copying task because simply masking out the irrelevant inputs does not affect the spacing between the relevant ones (indeed, the Selective Copying task can even be viewed as coming pre-masked if the noise tokens are embedded to 0). [p. 25–26]

- **RetNet** (Y. Sun et al. 2023) is also based on Linear Attention and very similar to H3, but reduces the inner S4 layer to a special case where the state dimension is $N = 1$. Although not framed as such, its recurrence can be viewed as a special case of a linear SSM. Its primary source of improvement is using a linear attention with large *head dimension*, which can be viewed as another method to perform input-dependent state expansion. Using a larger head dimension in the context of linear attention variants was first done by H3, but not extensively used since this requires a proportional amount of extra computation. RetNet avoids this with an alternate way to parallelize the computation with a variant of standard multi-head attention instead of convolutions, made feasible by their particular special case of SSMs which acts as a simple EMA. [p. 26]

- **RWKV** (B. Peng et al. 2023) is another recent RNN designed for language modeling. It is based on AFT (attention-free Transformer (S. Zhai et al. 2021)), another variant of linear attention. Its main "WKV" mechanism involves LTI recurrences and can be seen as the ratio of two SSMs. [p. 26]

The authors also highlight the gated attention unit (GAU) from Hua et al. (2022), which was motivated by combining the Transformer's MHA and MLP blocks together and was an inspiration for their architecture (Section 3.4) combining the H3 and MLP blocks. [p. 26]

## B.3 Relationship to RNNs

[p. 26]

RNNs and SSMs are broadly related, as they both involve the concepts of *recurrence* on a latent *state*.

Several older RNNs such as the strongly typed RNN (Balduzzi and Ghifary 2016), quasi-RNN (QRNN) (Bradbury et al. 2016), and simple recurrent unit (SRU) (Lei 2021; Lei et al. 2017) involve forms of gated RNNs without time-wise nonlinearities. Because of the connections of gating mechanisms and selection mechanisms, these can be viewed as cases of selective SSMs, and are thus more powerful in a sense than the family of LTI structured SSMs above. The main differences are:

- They do not use state expansion ($N = 1$) or selective $\boldsymbol{B}, \boldsymbol{C}$ parameters, both of which are important for performance (Section 4.6).

- They use a heuristic gating mechanism, which the authors generalize as a consequence of the selection mechanism + discretization (Theorem 1). The connections to principled SSM theory provides better parameterizations and initializations (Section 3.6).

Additionally, older RNNs famously suffered from efficiency issues and the vanishing gradients problem (Hochreiter 1991; Hochreiter, Bengio, et al. 2001; Pascanu, Mikolov, and Bengio 2013), both caused by their sequential nature. The former could be solved for some of the above RNNs by leveraging the parallel scan (Martin and Cundy 2018), but the latter was difficult without theory later developed for SSMs. For example, modern structured SSMs differ in more careful parameterization of the recurrent dynamics inspired by classical SSM theory (e.g. through discretization (Gu, Johnson, Goel, et al. 2021; Gu, Johnson, Timalsina, et al. 2023)), or direct analysis (Gupta, Mehta, and Berant 2022; Kaul 2020; Orvieto et al. 2023)).

The authors also note a long line of work on orthogonal RNNs (Arjovsky, Shah, and Bengio 2016; Henaff, Szlam, and LeCun 2016; Lezcano-Casado and Martinez-Rubio 2019; Mhammedi et al. 2017; Vorontsov et al. 2017) which are motivated by constraining the $\overline{A}$ transition matrix to be orthogonal or unitary, in order to control its eigenvalues and prevent the vanishing gradient problem. However, these had other limitations; the authors believe that these stem from the fact that orthogonal/unitary RNNs are also LTI. For example, they are almost always evaluated on the Copying task which they can solve perfectly, but observed to struggle on the Selective Copying task (Jing et al. 2019). [p. 26]

## B.4 Linear Attention

[p. 26]

The Linear Attention (LA) (Katharopoulos et al. 2020) framework is an important result popularizing kernel attention and showing how it relates to recurrent autoregressive models. Many variants have proposed alternative kernels and other modifications. Random Feature Attention (RFA) (H. Peng et al. 2021) chooses the kernel feature map to approximate softmax attention (i.e. the exp feature map) using the random Fourier feature approximation of Gaussian kernels (Rahimi and Recht 2007). Performer (Choromanski et al. 2021) finds an approximation to the exponential kernel involving only positive features.

---
[p. 26–27 continued]

These features also allow the softmax normalization term. TransNormer (Qin, Han, W. Sun, D. Li, et al. 2022) showed that the LA denominator term can be unstable and proposed replacing it with a LayerNorm. cosFormer (Qin, W. Sun, et al. 2022) augments RFA with a cosine reweighting mechanism that incorporates positional information to emphasize locality. Linear Randomized Attention (Zheng, C. Wang, and L. Kong 2022) generalizes RFA from the perspective of importance sampling, and generalizes it to provide better estimates of the full softmax kernel (rather than just the exp-transformed numerator). [p. 27]

Aside from kernel attention, many other variants of efficient attention exist; the survey Tay, Dehghani, Bahri, et al. (2022) offers an extensive categorization of many of these.

## B.5 Long Context Models

[p. 27]

Long context has become a popular subject, and several recent models have claimed to scale to longer and longer sequences. However, these are often from a computational standpoint and have not been extensively validated. These include:

- **Recurrent Memory Transformer** (Bulatov, Kuratov, and Burtsev 2023), a lightweight wrapper around a Transformer backbone. It showed ability to generalize up to 1M sequences but only on synthetic memorization tasks; their main result is similar to the authors' Induction Heads extrapolation experiment (Table 2).

- **LongNet** (Ding et al. 2023), which claimed to scale to 1B length but only evaluated on length < 100K for actual tasks.

- **Hyena and HyenaDNA** (Nguyen, Poli, et al. 2023; Poli et al. 2023), which claimed to leverage up to 1M context. However, their experiments trained on proportionally more data at longer contexts, making it hard to conclude if quality improvements at 1M are due to context length or due to more data and computation.

- **Sparse Transformer** (Child et al. 2019) showed a proof-of-concept of using a strided sparse attention Transformer to model audio waveforms of length $2^{20} = 1048576$, although did not discuss performance tradeoffs when controlling for computation and model size.

In contrast, the authors believe this work presents one of the first approaches to meaningfully demonstrate increasing performance with longer context. [p. 27]
