# B Theoretical Results and Details [p. 21-24]

## B.1 Proofs

[p. 21]

**Proof of Proposition 3.1.**

> *A discrete $L$-by-$L$ operator is causal if it is lower triangular, i.e., when there is no leakage of future input information to the output. The Hyena operator $\mathsf{H}$ is the product of alternating diagonal and Toeplitz matrices. Thus, if all the Toeplitz matrices $\mathsf{S}_h^n$ are lower triangular then $\mathsf{H}$ is lower triangular. In turn, each $\mathsf{S}_h^n$ is lower triangular if and only if the filter $h$ is causal, concluding the proof.* [p. 21]

## B.2 Analysis of Data-Controlled Mechanisms

[p. 22-24]

The authors discuss the surrogate attention mechanism of Hyena-2: $q, k, v \mapsto y$:

$$z_t = k_t(\varphi * v)_t$$
$$y_t = q_t(\psi * z)_t \tag{8}$$

If $\varphi$ and $\psi$ are convolutions parametrized via state-space models (SSMs), the above resembles the H3 mechanism (Dao et al., 2022c). The authors investigate the effect of the convolutional kernels $\varphi$ and $\psi$ on the attention layer. They introduce a matrix representation of the layer and isolate the *attention matrix* $\mathsf{A}_\varphi^\psi(q, k)$ such that:

$$y = \mathsf{A}_\varphi^\psi(q, k) v. \tag{9}$$

### Isolating the surrogate attention matrix

[p. 22]

In the case of length-$L$ discrete sequences:

$$z_t = k_t \sum_{m=0}^{L-1} \varphi_{t-m} v_m$$
$$y_t = q_t \sum_{m=0}^{L-1} \psi_{t-m} z_m \tag{10}$$

Therefore they rewrite (8) as:

$$y_t = q_t \sum_{m=0}^{L-1} \psi_{t-m} k_m \sum_{n=0}^{L-1} \varphi_{m-n} v_n$$
$$= q_t \sum_{m=0}^{L-1} \sum_{n=0}^{L-1} \psi_{t-m} k_m \varphi_{m-n} v_n \qquad \text{Move } \psi, k \text{ inside inner sum}$$
$$= q_t \sum_{n=0}^{L-1} \sum_{m=0}^{L-1} \psi_{t-m} k_m \varphi_{m-n} v_n \qquad \text{Index shift} \tag{11}$$
$$= \sum_{n=0}^{L-1} q_t \sum_{m=0}^{L-1} \psi_{t-m} k_m \varphi_{m-n} v_n$$

[p. 23]

And one can define the surrogate attention matrix $\mathsf{A}_\varphi^\psi(q, k)$:

$$[\mathsf{A}_\varphi^\psi(q, k)]_{t,t'} = q_t \sum_{m=0}^{L-1} \psi_{t-m} k_m \varphi_{m-t'}. \tag{12}$$

### Continuous Signals

[p. 23]

The authors also consider the case of continuous signals on a group $G$. The convolutions in (8) expand as:

$$(\varphi * v)_t = \int_G \varphi_{t-g} v_g \, \mathrm{d}g, \qquad (\psi * z)_t = \int_G \psi_{t-g} z_g \, \mathrm{d}g \tag{13}$$

This allows rewriting (8) as:

$$y_t = q_t (\psi * k(\varphi * v))_t$$
$$= q_t \int_G \psi_{t-g} \left[ k_g \int_G \varphi_{g-\tau} v_\tau \, \mathrm{d}\tau \right] \mathrm{d}g$$
$$= q_t \int_G \left[ \int_G \psi_{t-g} k_g \varphi_{g-\tau} v_\tau \, \mathrm{d}g \right] \mathrm{d}\tau$$
$$= q_t \int_G \left[ \int_G \psi_{t-g} k_g \varphi_{g-\tau} v_\tau \, \mathrm{d}g \right] \mathrm{d}\tau \qquad \text{Variable swap} \tag{14}$$
$$= \int_G \left[ q_t \int_G \psi_{t-g} k_g \varphi_{g-\tau} v_\tau \, \mathrm{d}g \right] \mathrm{d}\tau \qquad \text{Pull } q_t \text{ in } \tau \text{ integral}$$
$$= \int_G \left[ q_t \int_G \psi_{t-g} k_g \varphi_{g-\tau} \, \mathrm{d}g \right] v_\tau \, \mathrm{d}\tau \qquad \text{Pull } v_\tau \text{ out of } g \text{ integral.}$$

There is a linear operator $\mathcal{A} : v \mapsto y = \mathcal{A}v$ which is interpreted as the surrogate attention operator. $\mathcal{A}$ is conditioned on the *query* $q$, *key* $k$ and filters $\varphi$ and $\psi$, $\mathcal{A} = \mathcal{A}_\varphi^\psi(q, k)$. The kernel $\mathcal{K}$ of the operator is given by:

$$\mathcal{K}(t, t') = q_t \int_G \psi_{t-g} k_g \varphi_{g-t'} \, \mathrm{d}g \tag{15}$$

### Operator decomposition of the surrogate attention matrix

[p. 23]

The linear map $v \mapsto y$; $y = \mathsf{A}_\varphi^\psi(q, k)v$ can be decomposed into a sequence of factors, each dependent on a projection of the input: $\mathsf{A}_\varphi^\psi(q, k) = \mathsf{A}^\psi(q)\mathsf{A}_\varphi(k)$. Let $\mathsf{D}_q$ and $\mathsf{D}_k$ be the $L$-by-$L$ diagonal matrices whose respective main diagonal entries are the respective entries of $q$ and $k$. Then:

$$\mathsf{A}^\psi(q) = \mathsf{D}_q \mathsf{S}_\psi, \qquad \mathsf{D}_q = \mathrm{diag}(q),$$
$$\mathsf{A}_\varphi(k) = \mathsf{D}_k \mathsf{S}_\varphi, \qquad \mathsf{D}_k = \mathrm{diag}(k). \tag{16}$$

The matrix has been decomposed into two terms $\mathsf{A}^\psi(q)$ and $\mathsf{A}_\varphi(k)$ constructed by multiplying the diagonal matrices $\mathsf{D}_q$ and $\mathsf{D}_k$ with the Toeplitz matrices $\mathsf{S}_\psi$ and $\mathsf{S}_\varphi$. $\mathsf{S}_\psi$ and $\mathsf{S}_\varphi$ are the kernels of the convolution operators with filter's impulse responses $\psi$ and $\varphi$ respectively. In the current applications of interest, $\psi$ and $\varphi$ are chosen to be causal, i.e. $\psi[t] = 0$ for $t < 0$ and $\varphi[t] = 0$ for $t < 0$. This results in $\mathsf{S}_\psi$ and $\mathsf{S}_\varphi$ being lower triangular matrices:

$$\mathsf{S}_\psi = \begin{bmatrix} \psi_0 & 0 & \cdots & 0 \\ \psi_1 & \psi_0 & \cdots & 0 \\ \vdots & \ddots & \ddots & \vdots \\ \psi_{L-1} & \psi_{L-2} & \cdots & \psi_0 \end{bmatrix}, \qquad \mathsf{S}_\varphi = \begin{bmatrix} \varphi_0 & 0 & \cdots & 0 \\ \varphi_1 & \varphi_0 & \cdots & 0 \\ \vdots & \ddots & \ddots & \vdots \\ \varphi_{L-1} & \varphi_{L-2} & \cdots & \varphi_0 \end{bmatrix}. \tag{17}$$

The surrogate attention matrix is then given by:

$$\mathsf{A}_\varphi^\psi(q, k) = \mathsf{D}_q \mathsf{S}_\psi \mathsf{D}_k \mathsf{S}_\varphi \tag{18}$$

[p. 24]

The matrix multiplications in (16) can be expanded in the case of causal filters $\varphi$ and $\psi$ as:

$$\begin{bmatrix} q_0 & & \\ & q_1 & \\ & & \ddots & \\ & & & q_{L-1} \end{bmatrix} \begin{bmatrix} \psi_0 & & \\ \psi_1 & \psi_0 & \\ \vdots & \ddots & \ddots \\ \psi_{L-1} & \psi_{L-2} & \cdots & \psi_0 \end{bmatrix} \begin{bmatrix} k_0 & & \\ & k_1 & \\ & & \ddots & \\ & & & k_{L-1} \end{bmatrix} \begin{bmatrix} \varphi_0 & & \\ \varphi_1 & \varphi_0 & \\ \vdots & \ddots & \ddots \\ \varphi_{L-1} & \varphi_{L-2} & \cdots & \varphi_0 \end{bmatrix}$$

$$= \begin{bmatrix} q_0\psi_0 & & \\ q_1\psi_1 & q_1\psi_0 & \\ \vdots & \ddots & \ddots \\ q_{L-1}\psi_{L-1} & q_{L-1}\psi_{L-2} & \cdots & q_{L-1}\psi_0 \end{bmatrix} \begin{bmatrix} k_0\varphi_0 & & \\ k_1\varphi_1 & k_1\varphi_0 & \\ \vdots & \ddots & \ddots \\ k_{L-1}\varphi_{L-1} & k_{L-1}\varphi_{L-2} & \cdots & k_{L-1}\varphi_0 \end{bmatrix} \tag{19}$$

The first product is labeled $\mathsf{A}_\psi(q)$ and the second $\mathsf{A}_\varphi(k)$.

### Fourier decomposition of convolution operators

[p. 24]

The kernels of the convolution operators $\mathsf{S}_\psi$ and $\mathsf{S}_\varphi$ are diagonalized by the Fourier transform matrix $\mathsf{W} \in \mathbb{C}^{L \times L}$, $\mathsf{W}_{nm} = z^m$, $z = e^{j2\pi n / L}$. The Fourier transform of the convolution operator $\mathsf{S}_\psi$ is given by:

$$\mathsf{S}_\psi = \mathsf{W}^* \mathsf{D}_\Psi \mathsf{W}, \quad \mathsf{S}_\Phi = \mathsf{W}^* \mathsf{D}_\Phi \mathsf{W} \tag{20}$$

where $\mathsf{D}_\Psi, \mathsf{D}_\Phi \in \mathbb{C}^{L \times L}$ are diagonal matrices constructed from the frequency responses (the *discrete Fourier transform*) $\Psi = \mathsf{W}\psi$, $\Phi = \mathsf{W}\varphi$, respectively. This decomposition can be used to simplify the matrix multiplication in (19):

$$\mathsf{A} = \mathsf{D}_q \mathsf{S}_\psi \mathsf{D}_k \mathsf{S}_\varphi = \mathsf{D}_q \mathsf{W}^* \mathsf{D}_\Psi \mathsf{W} \mathsf{D}_k \mathsf{W}^* \mathsf{D}_\Phi \mathsf{W} \tag{21}$$

An important property of the above is the non-commutativity of $\mathsf{D}_q$ and $\mathsf{S}_k$ with $\mathsf{W}*$. If the two operators commuted, one would obtain:

$$\boxed{\mathsf{A} = \mathsf{D}_q \mathsf{W}^* \mathsf{D}_\Psi \mathsf{W} \mathsf{D}_k \mathsf{W}^* \mathsf{D}_\Phi \mathsf{W} = \mathsf{W}^* \mathsf{D}_q \mathsf{D}_\Psi \mathsf{D}_k \mathsf{D}_\Phi \mathsf{W}} \tag{22}$$

which reduces the entire layer to a simple convolution. The non-commutativity of the *gating* term acts as a non-linearity in chain of convolution operators. [p. 24]
