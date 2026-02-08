# Hyena: Definition and Properties [p. 5-6]

[p. 5]

The authors define Hyena, a class of *data-controlled* operators consisting of a recurrence of multiplicative gating interactions and long convolutions. Instead of seeking an approximation to attention, the design is guided by intentionally incorporating key computational properties of attention, including the decoupling of sequence length and parameter counts.

## Hyena Recurrences

[p. 5-6]

At a high level, Hyena consists of the following steps (setting $D = 1$ for clarity):

*i.* Compute a set of $N + 1$ linear projections of the input, similarly to attention. The number of projections $(v_t, x_t^1, \ldots, x_t^N)$ need not be three. One projection takes the role of value, such that a linear input-output function can be defined as $y = \mathsf{H}(u)v$ for some $\mathsf{H}(u)$.

[p. 6]

*ii.* The matrix $\mathsf{H}(u)$ is defined by interleaving implicit long convolutions and element-wise multiplication with one projection $x^i$ at a time, until all projections are exhausted. Evaluation of $\mathsf{H}(u)v$ is done efficiently **without materializing** $\mathsf{H}(u)$. By doing so, they implicitly define a data-controlled operator as a factorization of a matrix. The long convolutions forming $\mathsf{H}(u)$ are parametrized implicitly to retain sublinear parameter scaling in sequence length.

**Definition 3.1** (Order-$N$ Hyena Operator). *Let $(v, x^1, \cdots, x^N)$ be projections of the input and let $h^1, \ldots, h^N$ be a set of learnable filters. The* Hyena$_N$ *operator is defined by the recurrence:*

$$z_t^1 = v_t$$
$$z_t^{n+1} = x_t^n (h^n * z^n)_t \quad n = 1, \ldots, N \tag{4}$$
$$y_t = z_t^{N+1}$$

**Remark 3.1.** *The time complexity of a Hyena recurrence is $\mathcal{O}(NL \log_2 L)$. The input-output map can be rewritten as*

$$y = x^N \cdot (h^N * (x^{N-1} \cdot (h^{N-1} * (\cdots))))$$

*where each convolution is performed through the Fourier domain in $\mathcal{O}(L \log_2 L)$.* [p. 6]

Interestingly, the element-wise product in time domain corresponds to convolution in frequency domain, i.e.

$$x_t u_t = (\hat{x} * \hat{u})_t,$$

where $\hat{x}, \hat{u}$ denote the DFT of $x$ and $u$, respectively. Thus, Hyena is alternatively applying convolutions in the time and then the frequency domain (or alternatively applying element-wise products in the time and frequency domain). One potential explanation for the effectiveness of this procedure is that the convolution in the time domain (element-wise multiplication in the frequency domain) increases the memory length, allowing for a broader context to be taken into account. On the other hand, the element-wise multiplication in the time domain (convolution in the frequency domain) allows for more fine-grained selection of specific frequency components of the signal. [p. 6]

## Hyena Matrices

[p. 6]

Hyena operators build on the H3 mechanism developed by (Dao et al., 2022c). For clarity, the SISO case ($D = 1$) is considered. Let $\mathsf{D}_q$ and $\mathsf{D}_k$ be the $L$-by-$L$ diagonal matrices whose respective main diagonal entries are the respective entries of $q$ and $k$. H3 realizes a surrogate attention matrix with a data-controlled, parametrized decomposition in four terms:

$$\mathsf{A}(q, k) = \mathsf{D}_q \mathsf{S}_\psi \mathsf{D}_k \mathsf{S}_\varphi \tag{5}$$

$$\text{H3}(q, k, v) = \mathsf{A}(q, k) v$$

where $\mathsf{S}_\varphi, \mathsf{S}_\psi$ are the Toeplitz matrices of learnable **causal** filters $\varphi, \psi$ parametrized via SSMs (Footnote 4: For consistency with the authors' discussion, they have swapped $k$ and $v$ compared to the notation in (Dao et al., 2022c)). Alongside the $qkv$-projections the filters constitute the degrees of freedom in the layer design. This decomposition allows evaluation of (8) in just $\mathcal{O}(L \log_2 L)$ time (two FFT convolutions and two element-wise products), i.e.

$$z_t = k_t(\varphi * v)_t$$
$$y_t = q_t(\psi * z)_t \tag{6}$$

Hyena represents a generalization of (8) for an arbitrary number of projections -- not limited to three -- and with implicit free-form long filters for the convolutions. The resulting recurrence (4) can be also represented in matrix form $y = \mathsf{H}(u)v$. Let $\mathsf{D}_x^n = \text{diag}(x^n) \in \mathbb{R}^{L \times L}$ and let $\mathsf{S}_h^n$ be the Toeplitz matrix corresponding to filter $h^n$. The resulting Hyena recurrence is linear in $v$ and can be rewritten in matrix form:

$$y = \mathsf{H}(u)v = \mathsf{D}_x^N \mathsf{S}_h^N \cdots \mathsf{D}_x^2 \mathsf{S}_h^2 \mathsf{D}_x^1 \mathsf{S}_h^1 v$$

Figure 2.1 visualizes an example decomposition. [p. 6]

---
[p. 7 continued]

**Figure 3.1** (p. 7): "[Top]: Example of long convolution parametrization for Hyena operators, with a decay Window$(t) = \exp\{-\alpha t\}$. Parameter $\alpha$ is modified across the independent channels of Hyena to regularize filters to be of different lengths. In practice, we add a bias term to our window, so that the filters are not constrained to be zeros after a length determined by the decay rate."

The figure shows three panels labeled FFN$(t)$, Window, and Window $\circ$ FFN$(t)$, each plotted against Sequence Length. The FFN$(t)$ panel shows a high-frequency oscillating signal. The Window panel shows a smooth exponential decay envelope. The Window $\circ$ FFN$(t)$ panel shows the product: a decaying oscillating signal. This illustrates how the window function modulates the FFN-generated filter to produce the final Hyena filter with exponential decay.

**Remark 3.2** (Hyena generalizes H3 and GSS). *The H3 mechanism (Dao et al., 2022c) corresponds to* Hyena$_2$ *and GSS (Mehta et al., 2022) is* Hyena$_1$*, with a particular choice of parametrization for the long convolutions (SSMs).* [p. 7]

Analysis of the H3 mechanism as a decomposition $\mathsf{D}_q \mathsf{S}_\psi \mathsf{D}_k \mathsf{S}_\varphi$ of its surrogate attention matrix (Footnote 5: Some of this analysis is reported in the Appendix) clarifies a connection to fast evaluation algorithms for matrix-vector multiplications. In particular, the generalization of (8) to an arbitrary order is inspired by fast evaluation algorithms for structured dense matrices based on *butterfly* decompositions (Li et al., 2015; Dao et al., 2019, 2022a), with length of the decomposition closely tied to its expressivity (in the classes of matrices it can represent). The Hyena operator blends data control with a special case of butterfly decomposition. [p. 7]

**Remark 3.3.** Hyena *operators have unbounded context. Namely, they are not artificially restricted by e.g., locality, and can learn long-range dependencies between any of the elements of $v$ via long convolutions, which we discuss next.* [p. 7]

## Hyena Filters

[p. 7]

The convolution parametrization represents the filters of each Hyena operator as a map from the time (or space) domain $t$ to values $h_t$, learned with a shallow feed-forward neural network (FFN):

$$h_t = \text{Window}(t) \cdot (\text{FFN} \circ \text{PositionalEncoding})(t) \tag{7}$$

This approach builds on the neural implicit representation literature (Mildenhall et al., 2021; Sitzmann et al., 2020), which has found application in long convolution layers (Romero et al., 2021b,a). One advantage of (7) is given by the decoupling of filter length and parameter cost. [p. 7]

**Specializing filters in Hyena.** The window and positional encoding functions are used to specialize filters in Hyena operators, biasing them towards a specific type. Figure 3.1 provides an important example: at least one of the convolutions in Hyena is shaped towards exponential decay, mirroring the findings of (Li et al., 2022) in other applications. The authors find that long exponentially decaying filters display synergy with high-frequency filters, as they enable the operator to select specific inputs at specific steps (Footnote 6: This observation finds mirrors in the parametrization of the convolutions in H3 (Dao et al., 2022c) as a shift SSM and a diagonal SSM). Similarly to (Romero et al., 2021b), they use high-frequency periodic activations (sine) in the FFN. This allows (7) to learn filters with high-frequency content, addressing the low-frequency bias of neural networks (Basri et al., 2020). Owing to the FFN, the parametrization in (7) can approximate filters obtained through other means, such as S4 (Gu et al., 2020, 2021), CKConv (Romero et al., 2021b), SGConv (Li et al., 2022) and *Fourier Neural Operator* (FNO) (Li et al., 2020). [p. 7]

**Preserving causality.** Causality is necessary to train autoregressive language models, in order for the output at a given position to depend only on the past. For example, Transformers mask the attention matrix to be lower triangular. In the case of Hyena, causality can be guaranteed by parametrizing causal convolutions:

**Proposition 3.1** (Causal Hyenas). *If each filter $h^n$, $n = 1, \ldots, N$ is causal, then the corresponding* Hyena$_N$ *operator is causal.* [p. 8]

In practice, there is no need to constrain the learning of the filter (7) to ensure its *numerical* causality. If FFT-based convolution algorithms are used, all that is needed is to evaluate the filter at $t = 0, \ldots, L - 1$ and zero-pad the input and filter sequences to $2L - 1$ before taking FFT. [p. 8]

**Efficiency.** One bottleneck of long convolution models can be their low utilization of hardware accelerators, especially when they involve iterative numerical methods to materialize the filter (Footnote 7: In contrast, deep learning primitives are designed for high GPU utilization, with FFNs and attention usually reaching 50-70% or higher, if optimized). Evaluation of (7) is fast, since it involves a single forward pass of an FFN, and can be performed in parallel across sequence length and all orders of an Hyena operator as displayed in Algorithm 2, increasing hardware utilization. An additional source of low utilization is the FFT, which is also shared by other long convolutional layers. This bottleneck can be partially addressed by blocking (Selesnick and Burrus, 2017), and optimization of the underlying routines (Dao et al., 2022c). Runtime is benchmarked in Section 4.5. [p. 8]

## Hyena Algorithm

[p. 8]

A forward pass of Hyena is summarized below.

**Algorithm 1** Projection
**Require:** Input sequence $u \in \mathbb{R}^{L \times D}$
1. In parallel across $L$: $\hat{z} = \text{Linear}(u)$, Linear : $\mathbb{R}^D \to \mathbb{R}^{(N+1)D}$
2. In parallel across $D$: $z = \text{DepthwiseConv1d}(h, \hat{z})$, $h$ is a short convolution filter
3. Reshape and split $z$ into $x^1, \ldots, x^N, v$. Dimensions of one element are $x^n \in \mathbb{R}^{D \times L}$
Return $x^1, \ldots, x^N, v, x^n$

**Algorithm 2** Hyena Filter
**Require:** Sequence length $L$, positional embedding dimension $D_e$
1. $t = \text{PositionalEncoding}(L)$, $t \in \mathbb{R}^{L \times D_e}$
2. In parallel across $N, L$: $\hat{h} = \text{FFN}(t)$, FFN : $\mathbb{R}^{D_e} \to \mathbb{R}^{ND}$, $\hat{h} \in \mathbb{R}^{L \times ND}$
3. Reshape to $\hat{h} \in \mathbb{R}^{N \times D \times L}$
4. $h = \hat{h} \cdot \text{Window}(t)$, $h \in \mathbb{R}^{N \times D \times L}$
5. Split $h$ into $h^1, \ldots, h^N$
Return $h^1, \ldots, h^N$

**Algorithm 3** Forward pass of Hyena
**Require:** Input sequence $u \in \mathbb{R}^{L \times D}$, order $N$, model width $D$, sequence length $L$, positional embedding dimension $D_e$
1. $x^1, \ldots, x^N, v = \text{Projection}(u)$
2. $h^1, \ldots, h^N = \text{HyenaFilter}(L, D_e)$
**for** $n = 1, \ldots, N$ **do**
  3. In parallel across $D$: $v_t \leftarrow x_t^n \cdot \text{FFTConv}(h^n, v)_t$
**end for**
Return $y = v$

**Proposition 3.2** (Computational Complexity). *The computational cost of processing an input $u \in \mathbb{R}^{L \times D}$ with an order-$N$ Hyena operator is*

$$\mathcal{O}(NDL(\log_2 L + D))$$

[p. 8]
