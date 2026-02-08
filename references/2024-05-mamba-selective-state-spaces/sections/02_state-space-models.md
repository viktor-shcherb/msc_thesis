# State Space Models [p. 2-4]

[p. 2-3]

Structured state space sequence models (S4) are a recent class of sequence models for deep learning that are broadly related to RNNs, and CNNs, and classical state space models. They are inspired by a particular continuous system (1) that maps a 1-dimensional function or sequence $x(t) \in \mathbb{R} \mapsto y(t) \in \mathbb{R}$ through an implicit latent state $h(t) \in \mathbb{R}^N$.

Concretely, S4 models are defined with four parameters $(\Delta, \boldsymbol{A}, \boldsymbol{B}, \boldsymbol{C})$, which define a sequence-to-sequence transformation in two stages.

**Continuous form:**

$$h'(t) = \boldsymbol{A}h(t) + \boldsymbol{B}x(t) \quad (1a)$$

The continuous latent state dynamics: $\boldsymbol{A}$ governs the state transition and $\boldsymbol{B}$ maps the input into the state.

$$y(t) = \boldsymbol{C}h(t) \quad (1b)$$

The output equation: $\boldsymbol{C}$ maps the state to the output.

**Discrete form (after discretization):**

$$h_t = \overline{\boldsymbol{A}} h_{t-1} + \overline{\boldsymbol{B}} x_t \quad (2a)$$

The discrete recurrence: the discretized state transition.

$$y_t = \boldsymbol{C} h_t \quad (2b)$$

The discrete output equation.

**Convolution form:**

$$\overline{\boldsymbol{K}} = (\boldsymbol{C}\overline{\boldsymbol{B}}, \boldsymbol{C}\overline{\boldsymbol{A}}\overline{\boldsymbol{B}}, \dots, \boldsymbol{C}\overline{\boldsymbol{A}}^k\overline{\boldsymbol{B}}, \dots) \quad (3a)$$

The SSM convolution kernel, unrolled from the recurrence.

$$y = x * \overline{\boldsymbol{K}} \quad (3b)$$

The output computed as a global convolution of input with kernel $\overline{\boldsymbol{K}}$.

## Discretization

[p. 3]

The first stage transforms the "continuous parameters" $(\Delta, \boldsymbol{A}, \boldsymbol{B})$ to "discrete parameters" $(\overline{\boldsymbol{A}}, \overline{\boldsymbol{B}})$ through fixed formulas $\overline{\boldsymbol{A}} = f_A(\Delta, \boldsymbol{A})$ and $\overline{\boldsymbol{B}} = f_B(\Delta, \boldsymbol{A}, \boldsymbol{B})$, where the pair $(f_A, f_B)$ is called a *discretization rule*. Various rules can be used such as the zero-order hold (ZOH) defined in equation (4).

$$\overline{\boldsymbol{A}} = \exp(\Delta \boldsymbol{A}) \qquad \overline{\boldsymbol{B}} = (\Delta \boldsymbol{A})^{-1}(\exp(\Delta \boldsymbol{A}) - \boldsymbol{I}) \cdot \Delta \boldsymbol{B} \quad (4)$$

Zero-order hold (ZOH) discretization rule transforming continuous parameters to discrete parameters.

Discretization has deep connections to continuous-time systems which can endow them with additional properties such as resolution invariance (Nguyen, Goel, et al. 2022) and automatically ensuring that the model is properly normalized (Gu, Johnson, Timalsina, et al. 2023; Orvieto et al. 2023). It also has connections to gating mechanisms of RNNs (Gu, Gulcehre, et al. 2020; Tallec and Ollivier 2018) which will be revisited in Section 3.5. However, from a mechanical point of view discretization can simply be viewed as the first step of the computation graph in the forward pass of an SSM. Alternate flavors of SSMs can bypass the discretization step and parameterize $(\overline{\boldsymbol{A}}, \overline{\boldsymbol{B}})$ directly instead (Zhang et al. 2023), which may be easier to reason about. [p. 3]

## Computation

After the parameters have been transformed from $(\Delta, \boldsymbol{A}, \boldsymbol{B}, \boldsymbol{C}) \mapsto (\overline{\boldsymbol{A}}, \overline{\boldsymbol{B}}, \boldsymbol{C})$, the model can be computed in two ways, either as a **linear recurrence** (2) or a **global convolution** (3). [p. 3]

Commonly, the model uses the convolutional mode (3) for efficient parallelizable training (where the whole input sequence is seen ahead of time), and switched into recurrent mode (2) for efficient autoregressive inference (where the inputs are seen one timestep at a time). [p. 3]

## Linear Time Invariance (LTI)

[p. 3-4]

An important property of equations (1) to (3) is that the model's dynamics are constant through time. In other words $(\Delta, \boldsymbol{A}, \boldsymbol{B}, \boldsymbol{C})$, and consequently $(\overline{\boldsymbol{A}}, \overline{\boldsymbol{B}})$ as well, are fixed for all time-steps. This property is called *linear time invariance (LTI)*, which is deeply connected to recurrence and convolutions. Informally, LTI SSMs are equivalent to any linear recurrence (2a) or convolution (3b), and LTI is used as an umbrella term for these classes of models. [p. 3-4]

Thus far, all structured SSMs have been LTI (e.g. computed as convolutions) because of fundamental efficiency constraints, discussed in Section 3.3. However, a core insight of this work is that LTI models have fundamental limitations in modeling certain types of data, and the technical contributions involve removing the LTI constraint while overcoming the efficiency bottlenecks. [p. 4]

## Structure and Dimensions

[p. 4]

Structured SSMs are so named because computing them efficiently also requires imposing structure on the $\boldsymbol{A}$ matrix. The most popular form of structure is diagonal (Gu, Gupta, et al. 2022; Gupta, Gu, and Berant 2022; Smith, Warrington, and Linderman 2023), which the authors also use.

In this case, the $\boldsymbol{A} \in \mathbb{R}^{N \times N}, \boldsymbol{B} \in \mathbb{R}^{N \times 1}, \boldsymbol{C} \in \mathbb{R}^{1 \times N}$ matrices can all be represented by $N$ numbers. To operate over an input sequence $x$ of batch size $B$ and length $L$ with $D$ channels, the SSM is applied independently to each channel. Note that in this case, the total hidden state has dimension $DN$ per input, and computing it over the sequence length requires $O(BLDN)$ time and memory; this is the root of the fundamental efficiency bottleneck addressed in Section 3.3. [p. 4]

## General State Space Models

[p. 4]

The term *state space model* has a very broad meaning which simply represents the notion of any recurrent process with a latent state. It has been used to refer to many disparate concepts in different disciplines, including Markov decision processes (MDP) (reinforcement learning (Hafner et al. 2020)), dynamic causal modeling (DCM) (computational neuroscience (Friston, Harrison, and Penny 2003)), Kalman filters (controls (Kalman 1960)), hidden Markov models (HMM) and linear dynamical systems (LDS) (machine learning), and recurrent (and sometimes convolutional) models at large (deep learning).

Throughout this paper the authors use the term "SSM" to refer exclusively to the class of structured SSMs or S4 models (Gu, Goel, and Re 2022; Gu, Gupta, et al. 2022; Gupta, Gu, and Berant 2022; Hasani et al. 2023; Ma et al. 2023; Smith, Warrington, and Linderman 2023) and use these terms interchangeably. They may also include derivatives of such models, such as those focusing on either the linear-recurrence or global-convolution viewpoints (Y. Li et al. 2023; Orvieto et al. 2023; Poli et al. 2023), and clarify nuances when necessary. [p. 4]

## SSM Architectures

[p. 4]

SSMs are standalone sequence transformations that can be incorporated into end-to-end neural network architectures. (Also sometimes called SSM architectures SSNNs, which are to SSM layers as CNNs are to linear convolution layers.) The most well-known SSM architectures, many of which also serve as primary baselines:

- **Linear attention** (Katharopoulos et al. 2020) is an approximation of self-attention involving a recurrence which can be viewed as a degenerate linear SSM.
- **H3** (Dao, Fu, Saab, et al. 2023) generalized this recurrence to use S4; it can be viewed as an architecture with an SSM sandwiched by two gated connections (Figure 3). H3 also inserts a standard local convolution, which they frame as a shift-SSM, before the main SSM layer.
- **Hyena** (Poli et al. 2023) uses the same architecture as H3 but replaces the S4 layer with an MLP-parameterized global convolution (Romero et al. 2021).
- **RetNet** (Y. Sun et al. 2023) adds an additional gate to the architecture and uses a simpler SSM, allowing an alternative parallelizable computation path, using a variant of multi-head attention (MHA) instead of convolutions.
- **RWKV** (B. Peng et al. 2023) is a recent RNN designed for language modeling based on another linear attention approximation, the attention-free Transformer (S. Zhai et al. 2021). Its main "WKV" mechanism involves LTI recurrences and can be viewed as the ratio of two SSMs.

Other closely related SSMs and architectures are discussed further in extended related work (Appendix B). The authors highlight in particular S5 (Smith, Warrington, and Linderman 2023), QRNN (Bradbury et al. 2016), and SRU (Lei et al. 2017), which they view as the most closely related methods to their core selective SSM. [p. 4]

## Figures

**Figure 1** (p. 3): "(**Overview.**) Structured SSMs independently map each channel (e.g. $D = 5$) of an input $x$ to output $y$ through a higher dimensional latent state $h$ (e.g. $N = 4$). Prior SSMs avoid materializing this large effective state ($DN$, times batch size $B$ and sequence length $L$) through clever alternate computation paths requiring time-invariance: the ($\Delta, \boldsymbol{A}, \boldsymbol{B}, \boldsymbol{C}$) parameters are constant across time. Our selection mechanism adds back input-dependent dynamics, which also requires a careful hardware-aware algorithm to only materialize the expanded states in more efficient levels of the GPU memory hierarchy."

The figure shows the Selective State Space Model with Hardware-aware State Expansion. It depicts: on the left, input $x_t$ and previous hidden state $h_{t-1}$; in the middle, the selection mechanism projects the input to produce $B_t$, $\Delta_t$, and $C_t$ (input-dependent parameters), which pass through a "Discretize" step; on the right, the output $y_t$ and updated hidden state $h_t$. The matrix $\boldsymbol{A}$ connects states across time at the top. A GPU memory hierarchy diagram (GPU SRAM / GPU HBM) is shown on the far right, indicating the hardware-aware state expansion strategy.
