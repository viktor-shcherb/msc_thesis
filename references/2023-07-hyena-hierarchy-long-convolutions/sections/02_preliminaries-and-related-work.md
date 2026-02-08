# Preliminaries and Related Work [p. 3-5]

[p. 3]

A discrete convolution is a function of two arguments: an input $u$ signal of length $L$ and a learnable filter $h$. The linear (aperiodic) convolution of a (possibly infinitely long) measurable filter $h$ with a length-$L$ input signal $u$ is defined as

$$y_t = (h * u)_t = \sum_{n=0}^{L-1} h_{t-n} u_n. \tag{1}$$

(Footnote 3: In the $L^1(\mathbb{Z})$ sense: $\sum_{t=-\infty}^{\infty} |h_t| < \infty$.)

Generally, $u_t \in \mathbb{R}^D$ where $D$ is the width of the signal, or in deep learning parlance, the number of *channels*. Without loss of generality, the analysis is specialized to *single input single output* (SISO) layers, i.e. with $D = 1$. The *multiple input multiple output* (MIMO) case, canonical in standard convolutional layers, follows directly.

The input signal can be represented as a vector $u \in \mathbb{R}^L$ and the convolution as a matrix-vector product between the input and the Toeplitz kernel matrix $\mathsf{S}_h \in \mathbb{R}^{L \times L}$ induced by the filter $h$:

$$(h * u) = \begin{bmatrix} h_0 & h_{-1} & \cdots & h_{-L+1} \\ h_1 & h_0 & \cdots & h_{-L+2} \\ \vdots & \vdots & \ddots & \vdots \\ h_{L-1} & h_{L-2} & \cdots & h_0 \end{bmatrix} \begin{bmatrix} u_0 \\ u_1 \\ \vdots \\ u_{L-1} \end{bmatrix} \tag{2}$$

## Explicit and Implicit Convolutions

[p. 3-4]

Parametrizing and optimizing convolution filters $h_t$ is a standard procedure in deep learning and more broadly signal processing. The classical approach of *convolutional neural networks* (CNNs) (Fukushima and Miyake, 1982; LeCun et al., 1998; Ronneberger et al., 2015; He et al., 2016) is to optimize directly the values $h_t$ of the filter's response at $M$ prescribed steps, a parametrization called *explicit*. $M$ is referred to as the *filter size* and is typically much shorter than the input sequence length $M \ll L$. Such filters are denoted in signal processing as *finite impulse response* (FIR). [p. 3]

FIR filters are local and can capture dependencies separated by at most $M$ steps. Their main advantage is their speed, with complexity $\mathcal{O}(ML)$. However, the number of parameters of FIR filters scales linearly with filter size, which can be computationally prohibitive. To disentangle the parameter count from the filter size, one can instead represent the filter $h_t$ as a parametric function of the time step $t$, i.e. $h_t = \gamma_\theta(t)$, where $\theta$ are the parameters of the function $\gamma_\theta$. This parametrization is called *implicit*. The class of functions $\gamma_\theta$ is a design choice with a significant impact on the expressivity and computational complexity of the layer. [p. 3-4]

[p. 4]

One choice of implicit parametrization is to select $h$ as the response function of a linear state-space model (SSM) (Chen, 1984), described by the first-order difference equation:

$$x_{t+1} = \mathsf{A}x_t + \mathsf{B}u_t \quad \text{state equation}$$
$$y_t = \mathsf{C}x_t + \mathsf{D}u_t \quad \text{output equation}$$

Here, the convenient choice of $x_0 = 0$ renders the input-output map to a simple convolution

$$y_t = \sum_{n=0}^{t} \left(\mathsf{C}\mathsf{A}^{t-n}\mathsf{B} + \mathsf{D}\delta_{t-n}\right) u_n$$

where $\delta_t$ denotes the Kronecker delta. The filter $h$ can then be identified as

$$t \mapsto h_t = \begin{cases} 0 & t < 0 \\ \mathsf{C}\mathsf{A}^t\mathsf{B} + \mathsf{D}\delta_t & t \geq 0 \end{cases}$$

where the entries of $\mathsf{A}, \mathsf{B}, \mathsf{C}$ and $\mathsf{D}$ are the learned parameters of the filter. In terms of layer design, the degrees of freedom of SSMs are the dimension of the state and the structure of the matrices. SSMs are a canonical example of how long convolutions with sub-linear parameter counts can improve deep learning models for long sequences (Gu et al., 2020, 2021). Other implicit approaches include parametrizing filters as maps from (a positional encoding of) $t$ to the filter response i.e. $\gamma_\theta : t \mapsto h_t = \gamma_\theta(t)$, for example with feed-forward neural networks (Romero et al., 2021b,a). [p. 4]

### Long Convolutions and Memory

[p. 4]

> A crude proxy for *memory* of a single computational unit is how far in the past it can access information to produce the output at a certain step. This can be roughly quantified by the number of non-zero entries $\partial y_t / \partial u_{t-n}$ for $n = 0, \ldots, t$. The memory of CNNs filters is equivalent to the filter size $M$ since $\partial y_t / \partial u_{t-n} = h_n$. The total mnemonic capacity of an all-convolutions CNN therefore scales with the number of model's parameters. Implicit parametrizations, on the other hand, allow us to disentangle the memory of each filter from the parameter count and where the length of the filter is implicitly controlled by the learned parameters. In an SSM, $\partial y_t / \partial u_{t-n} = \mathsf{C}\mathsf{A}^n\mathsf{B}$ and the memory extent is solely determined by the spectral radius of $\mathsf{A}$ and can be finely tuned by the training process. On the other hand, the number of parameters controls the *expressivity* of the memory unit, e.g. the number of basis functions forming $h_t$. [p. 4]

(Footnote a: See e.g. Gu et al. (2020, 2021))

### Fast Methods for Convolutions

[p. 4]

One of the first applications of the Cooley-Tukey fast Fourier transform (FFT) algorithm was to implement convolution faster than the direct evaluation of (1). At first glance (1) comes with $\mathcal{O}(L^2)$ an asymptotic time complexity. A common approach to achieve *fast long convolutions* in subquadratic time is through the FFT algorithm. The method first converts the aperiodic convolution into a *circular convolution* (Selesnick and Burrus, 2017) by appropriate zero-padding of input and filter sequences. The resulting kernel $\hat{\mathsf{S}}_h$ is a circulant matrix and is diagonalized by the discrete Fourier basis

$$\hat{\mathsf{S}}_h = \mathsf{W}^{-1}\mathsf{D}_H\mathsf{W}$$

where $\mathsf{W}$ is the DFT matrix, $\mathsf{W}_{tt'} = z^{-t}, z = e^{i2\pi t'/L}$ and $H$ is the DFT of the padded filter $h$, $H = \mathsf{W}\text{pad}(h)$. Thus, the calculation of such convolutions is performed as

$$\text{pad}(y) = \hat{\mathsf{S}}_h \text{pad}(u)$$
$$= \mathsf{W}^{-1}\mathsf{D}_H\mathsf{W}\ \text{pad}(u)$$
$$= \text{iFFT}(\mathsf{D}_H \text{FFT}(\text{pad}(u)))$$

where $\mathsf{D}_H$ is the matrix with $Wh$ on its diagonal. The above is known as the convolution theorem of DFT (Oppenheim et al., 1997). In this FFTConv form the convolution can be performed **without materializing the operator** $\mathsf{S}_h$ with the same asymptotic cost $\mathcal{O}(L \log_2 L)$ of FFT. [p. 4]

## The Self-Attention Operator

[p. 5]

**Figure 2.1** (p. 5): "Comparison between data-controlled matrices: SelfAttention and Hyena."

The figure shows a visual comparison of the matrix decomposition for SelfAttention $y = \mathsf{A}(q, k)v$ versus Hyena $y = \mathsf{H}(u)v = \mathsf{D}_x^N \mathsf{S}_h^N \cdots \mathsf{D}_x^1 \mathsf{S}_h^1 v$. The SelfAttention matrix $\mathsf{A}(q, k)$ is shown as a dense lower-triangular matrix. The Hyena decomposition shows alternating diagonal matrices $\mathsf{D}_x^n$ (sparse, diagonal pattern) and Toeplitz matrices $\mathsf{S}_h^n$ (banded lower-triangular pattern), composed in sequence.

At the heart of Transformers is the *multi-head attention* (MHA) mechanism. Given a length-$L$ sequence $u \in \mathbb{R}^{L \times D}$, each *head* of *scaled self-attention* (Vaswani et al., 2017) is a map from $\mathbb{R}^{L \times D}$ to $\mathbb{R}^{L \times D}$ which performs the following operations

$$\mathsf{A}(u) = \text{SoftMax}\left(\frac{1}{\sqrt{D}} u\mathsf{M}_q \mathsf{M}_k^\top u^\top\right)$$

$$y = \text{SelfAttention}(u) = \mathsf{A}(u) u \mathsf{M}_v, \tag{3}$$

where $\mathsf{M}_q, \mathsf{M}_k, \mathsf{M}_v \in \mathbb{R}^{D \times D}$ are learnable linear projections and SoftMax is intended to be applied row-wise. Attention parametrizes a **family of dense linear operators** and for an input $u$, indexes through it via projections of $u$ i.e., $\mathsf{A}(u)$. The authors refer to operators of this type as *data-controlled*, as they encode a linear transformation $u \mapsto y$, that is, however, nonlinearly defined by $u$. This approach yields expressive nonlinear operators in $u$, and the authors hypothesize it contributes, together with other mechanisms (Olsson et al., 2022), to the ability of certain operators to learn *in-context* i.e., to adapt to unseen tasks by leveraging context. In deep learning, the projections take on specific names: *query* $q = u\mathsf{M}_q$, *key* $k = u\mathsf{M}_k$ and *value* $v = u\mathsf{M}_v$. The attention operator is often rewritten as $y = \mathsf{A}(q, k)v$. [p. 5]

**Remark 2.1.** *Similarly to implicit convolutions, SelfAttention does not entangle its ability to access distant information with the number of parameters: it looks at the whole sequence at the price of $\mathcal{O}(L^2)$ operations.* [p. 5]

### Subquadratic Operators

[p. 5]

Existing approaches to subquadratic alternatives to attention can be summarized by altering the way the data control is implemented i.e., how the operator is nonlinearly defined by $u$, and then applied to $v$. Examples:

- *Attention-Free Transformers* (AFTs) (Zhai et al., 2021) construct the operator through a combination of gating and SoftMax (AFT full) or gating and a single explicit convolution (AFT conv).
- *Gated State Spaces* (GSS) compose the operator via gating and a long convolution parametrized via SSMs.
- *Hungry Hungry Hippo (H3)* (Dao et al., 2022c), motivated by gaps of GSS on associative recall, extends the mechanism to include an additional gate and a short convolution obtained via a shift SSM.

Hyena generalizes this body of work by introducing a recurrence of gates and implicit long convolutions, evaluated efficiently. [p. 5]
