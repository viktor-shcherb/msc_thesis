# 2.1 Structured State Space Models [p. 3-4]

[p. 3] Structured state space sequence models (S4) are a recent class of sequence models for deep learning that are broadly related to RNNs, CNNs, and classical state space models. They are inspired by a particular continuous system (1) that maps a 1-dimensional sequence $x \in \mathbb{R}^T \mapsto y \in \mathbb{R}^T$ through an implicit latent state $h \in \mathbb{R}^{(T,N)}$.

A general discrete form of structured SSMs takes the form of equation (1):

**LTI (time-invariant) form:**

$$h_t = A h_{t-1} + B x_t \quad (1a)$$
$$y_t = C^\top h_t \quad (1b)$$

where $A \in \mathbb{R}^{(N,N)}$, $B \in \mathbb{R}^{(N,1)}$, $C \in \mathbb{R}^{(N,1)}$.

**Selective (time-varying) form:**

$$h_t = A_t h_{t-1} + B_t x_t \quad (2a)$$
$$y_t = C_t^\top h_t \quad (2b)$$

Structured SSMs are so named because the $A$ matrix controlling the temporal dynamics must be *structured* in order to compute this sequence-to-sequence transformation efficiently enough to be used in deep neural networks. The original structures introduced were diagonal plus low-rank (DPLR) (Gu, Goel, and Ré 2022) and diagonal (Gu, Gupta, et al. 2022; Gupta, Gu, and Berant 2022; J. T. Smith, Warrington, and Linderman 2023), which remains the most popular structure.

In this work, the term state space model (SSM) is used to refer to structured SSMs. There are many flavors of such SSMs, with deep ties to several major paradigms of neural sequence models such as continuous-time, recurrent, and convolutional models (Gu, Johnson, Goel, et al. 2021). The authors refer to prior work for more context and details (Gu 2023; Gu and Dao 2023).

## Continuous-time Models

[p. 3-4] The original structured SSMs originated as continuous-time maps on functions $x(t) \in \mathbb{R} \mapsto y(t) \in \mathbb{R}$, rather than operating directly on sequences. In the continuous-time perspective, in equation (1a) the matrices $(A, B)$ are not directly learned but generated from underlying parameters $(\tilde{A}, \tilde{B})$, along with a parameterized step size $\Delta$. The "continuous parameters" $(\Delta, \tilde{A}, \tilde{B})$ are converted to "discrete parameters" $(A, B)$ through fixed formulas $A = f_A(\Delta, \tilde{A})$ and $B = f_B(\Delta, \tilde{B})$, where the pair $(f_A, f_B)$ is called a **discretization rule**.

**Remark 1.** *While our main models adopt the same parameterization and discretization step as prior work (see Gu and Dao (2023) for details), for simplifying exposition and notation we omit it in the rest of this paper. We note that prior work on structured SSMs referred to the continuous parameters $(\tilde{A}, \tilde{B})$ and discrete parameters $(A, B)$ as $(A, B)$ and $(\bar{A}, \bar{B})$ instead; we have changed notation to simplify the presentation and focus directly on the discrete parameters, which govern the main SSM recurrence.* [p. 3-4]

## Recurrent Models

[p. 4] Equations (1) and (2) take the form of a recurrence which is linear in its input $x$. Structured SSMs can therefore be viewed as types of recurrent neural networks (RNNs), where the linearity endows them with additional properties and allows them to avoid the sequential computation of traditional RNNs. Conversely, despite this simplification, SSMs are still fully expressive as sequence transformations (in the sense of universal approximation) (Kaul 2020; Orvieto et al. 2023; Shida Wang and Xue 2023).

## Convolutional Models

[p. 4] When the SSM's dynamics are constant through time as in equation (1), the model is called **linear time-invariant (LTI)**. In this case, they are equivalent to convolutions. Thus, SSMs can also be viewed as types of CNNs, but where (i) the convolution kernels are implicitly parameterized through the SSM parameters $(A, B, C)$ and (ii) the convolution kernels are generally global instead of local. Conversely, through classical signal processing theory all sufficiently well-behaved convolutions can be represented as SSMs.

Commonly, previous LTI SSMs would use the convolutional mode for efficient parallelizable training (where the whole input sequence is seen ahead of time), and switched into recurrent mode (1) for efficient autoregressive inference (where the inputs are seen one step at a time).

## Selective State Space Models

[p. 4] The form (2) where the parameters $(A, B, C)$ can also vary in time was introduced in Mamba as the **selective SSM**. Compared to the standard LTI formulation (1), this model can selectively choose to focus on or ignore inputs at every timestep. It was shown to perform much better than LTI SSMs on information-dense data such as language, especially as its state size N increases allowing for more information capacity. However, it can only be computed in recurrent instead of convolutional mode, and requires a careful hardware-aware implementation to be efficient. Even so, it is still less efficient than hardware-friendly models such as CNNs and Transformers because it does not leverage matrix multiplication units, which modern accelerators such as GPUs and TPUs are specialized for.

While *time-invariant* SSMs are closely related to continuous, recurrent, and convolutional sequence models, they are not directly related to attention. This paper shows a deeper relationship between *selective* SSMs and attention, and uses it to significantly improve the training speed of SSMs while simultaneously allowing for much larger state sizes N.

## Structured SSMs as Sequence Transformations

[p. 4] **Definition 2.1.** *We use the term **sequence transformation** to refer to a parameterized map on sequences $Y = f_\theta(X)$ where $X, Y \in \mathbb{R}^{(T,P)}$ and $\theta$ is an arbitrary collection of parameters. T represents the sequence or time axis; subscripts index into the first dimension, e.g. $X_t, Y_t \in \mathbb{R}^P$.*

Sequence transformations (e.g. SSMs, or self-attention) are the cornerstone of deep sequence models, where they are incorporated into neural network architectures (e.g. Transformers). The SSM in (1) or (2) is a sequence transformation with $P = 1$; it can be generalized to $P > 1$ by simply broadcasting across this dimension (in other words, viewing the input as P independent sequences and applying the SSM to each). One can think of P as a **head dimension**, elaborated on in Section 7.

**Definition 2.2.** *We define the **SSM operator** $\text{SSM}(A, B, C) = \text{SSM}(A_{0:T}, B_{0:T}, C_{0:T})$ as the sequence transformation $X \in \mathbb{R}^{(T,P)} \mapsto Y \in \mathbb{R}^{(T,P)}$ defined by equation (2).*

In SSMs, the N dimension is a free parameter called the **state size** or state dimension. It is also called the **state expansion factor**, because it expands the size of the input/output by a factor of N, with implications for the computational efficiency of these models.

**Definition 2.3.** *We call a sequence transformation $Y = f_\theta(X)$ a **matrix transformation** if it can be written in the form $Y = M_\theta X$ where $M$ is a matrix depending on the parameters $\theta$. We identify the sequence transformation with the matrix $M$, and often drop the dependence on $\theta$ when clear from context.* [p. 4]
