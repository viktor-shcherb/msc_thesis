# 2 Background and Related Work [p. 2-4]

## 2.1 Rotary Position Embeddings [p. 2-3]

The basis of the work is the Rotary Position Embedding (RoPE) introduced in [34]. The authors work on a hidden layer where the set of hidden neurons are denoted by $D$. Given a sequence of vectors $\mathbf{x}_1, \cdots, \mathbf{x}_L \in \mathbb{R}^{|D|}$, following the notation of [34], the attention layer first converts the vectors into query vectors and key vectors: [p. 2]

$$\mathbf{q}_m = f_q(\mathbf{x}_m, m) \in \mathbb{R}^{|D|}, \quad \mathbf{k}_n = f_k(\mathbf{x}_n, n) \in \mathbb{R}^{|D|}. \tag{1}$$

Equation (1): Query and key vector computation from input vectors at positions $m$ and $n$.

Next, the attention weights are calculated as: [p. 2]

$$\text{softmax}\left(\frac{\mathbf{q}_m^T \mathbf{k}_n}{\sqrt{|D|}}\right). \tag{2}$$

Equation (2): Scaled dot-product attention weight computation.

Here $\mathbf{q}_m, \mathbf{k}_n$ are considered as column vectors so that $\mathbf{q}_m^T \mathbf{k}_n$ is simply the Euclidean inner product. In RoPE, $|D|$ is assumed to be even and the embedding space and hidden states are identified as complex vector spaces: [p. 2-3]

$$\mathbb{R}^{|D|} \cong \mathbb{C}^{|D|/2}$$

where the inner product $\mathbf{q}^T \mathbf{k}$ becomes the real part of the standard Hermitian inner product $\text{Re}(\mathbf{q}^* \mathbf{k})$. The isomorphisms interleave the real part and the complex part: [p. 3]

$$\big((\mathbf{x}_m)_1, \cdots, (\mathbf{x}_m)_{|D|}\big) \mapsto \big((\mathbf{x}_m)_1 + i(\mathbf{x}_m)_2, \cdots, ((\mathbf{x}_m)_{|D|-1} + i(\mathbf{x}_m)_{|D|})\big), \tag{3}$$

$$\big((\mathbf{q}_m)_1, \cdots, (\mathbf{q}_m)_{|D|}\big) \mapsto \big((\mathbf{q}_m)_1 + i(\mathbf{q}_m)_2, \cdots, ((\mathbf{q}_m)_{|D|-1} + i(\mathbf{q}_m)_{|D|})\big). \tag{4}$$

Equations (3)-(4): Isomorphisms mapping real-valued vectors to complex-valued vectors by pairing adjacent dimensions.

To convert embeddings $\mathbf{x}_m, \mathbf{x}_n$ into query and key vectors, $\mathbb{R}$-linear operators are first given: [p. 3]

$$\mathbf{W}_q, \mathbf{W}_k : \mathbb{R}^{|D|} \to \mathbb{R}^{|D|}.$$

In complex coordinates, the functions $f_q, f_k$ are given by: [p. 3]

$$f_q(\mathbf{x}_m, m) = e^{im\theta} \mathbf{W}_q \mathbf{x}_m, \quad f_k(\mathbf{x}_n, n) = e^{in\theta} \mathbf{W}_k \mathbf{x}_n, \tag{5}$$

where $\theta = \text{diag}(\theta_1, \cdots, \theta_{|D|/2})$ is the diagonal matrix with $\theta_d = b^{-2d/|D|}$ and $b = 10000$. This way, RoPE associates each (complex-valued) hidden neuron with a separate frequency $\theta_d$. [p. 3]

Equation (5): RoPE query and key functions in complex coordinates, applying position-dependent rotation via $e^{im\theta}$.

The benefit of RoPE is that the dot product between the query vector and the key vector only depends on the relative distance $m - n$: [p. 3]

$$\langle f_q(\mathbf{x}_m, m), f_k(\mathbf{x}_n, n) \rangle_{\mathbb{R}} \tag{6}$$

$$= \text{Re}(\langle f_q(\mathbf{x}_m, m), f_k(\mathbf{x}_n, n) \rangle_{\mathbb{C}}) \tag{7}$$

$$= \text{Re}(\mathbf{x}_m^* \mathbf{W}_q^* \mathbf{W}_k \mathbf{x}_n e^{i\theta(m-n)}) \tag{8}$$

$$= g(\mathbf{x}_m, \mathbf{x}_n, m - n). \tag{9}$$

Equations (6)-(9): Derivation showing the RoPE inner product depends only on relative position $m - n$.

In real coordinates, the RoPE can be written using the following function: [p. 3]

$$f_{\mathbf{W}}(\mathbf{x}_m, m, \theta_d) = \begin{pmatrix} \cos m\theta_1 & -\sin m\theta_1 & 0 & 0 & \cdots & 0 & 0 \\ \sin m\theta_1 & \cos m\theta_1 & 0 & 0 & \cdots & 0 & 0 \\ 0 & 0 & \cos m\theta_2 & -\sin m\theta_2 & \cdots & 0 & 0 \\ 0 & 0 & \sin m\theta_2 & \cos m\theta_2 & \cdots & 0 & 0 \\ 0 & 0 & 0 & 0 & \cdots & \cos m\theta_l & -\sin m\theta_l \\ 0 & 0 & 0 & 0 & \cdots & \sin m\theta_l & \cos m\theta_l \end{pmatrix} \mathbf{W}\mathbf{x}_m,$$

so that $f_q = f_{\mathbf{W}_q}$, $f_k = f_{\mathbf{W}_k}$.

This is the block-diagonal rotation matrix form of RoPE in real coordinates, where each 2x2 block rotates a pair of dimensions by $m\theta_d$.

## 2.2 Position Interpolation [p. 3]

As language models are usually pre-trained with a fixed context length, it is natural to ask how to extend the context length by fine-tuning on relatively less data. For language models using RoPE, Chen et al. [9], and concurrently kaiokendev [21] proposed the Position Interpolation (PI) to extend the context length beyond the pre-trained limit. [p. 3]

While a direct extrapolation does not perform well on sequences $w_1, \cdots, w_L$ with $L$ larger than the pre-trained limit, they discovered that interpolating the position indices within the pre-trained limit works well with a small amount of fine-tuning. Specifically, given a pre-trained language model with RoPE, they modify the RoPE by: [p. 3]

$$f'_{\mathbf{W}}(\mathbf{x}_m, m, \theta_d) = f_{\mathbf{W}}\left(\mathbf{x}_m, \frac{mL}{L'}, \theta_d\right), \tag{10}$$

where $L' > L$ is a new context window beyond the pre-trained limit. With the original pre-trained model plus the modified RoPE formula, they fine-tuned the language model further on several orders of magnitude fewer tokens (a few billion in Chen et al. [9]) and successfully achieved context window extension. [p. 3]

Equation (10): Position Interpolation formula -- scales position $m$ by the ratio $L/L'$ to compress positions into the original range.

## 2.3 Additional Notation [p. 4]

The ratio between the extended context length and the original context length is the *scale factor* $s$: [p. 4]

$$s = \frac{L'}{L}, \tag{11}$$

Equation (11): Definition of the scale factor $s$ as the ratio of new context window $L'$ to original $L$.

The authors rewrite and simplify Eq. 10 into the following general form: [p. 4]

$$f'_{\mathbf{W}}(\mathbf{x}_m, m, \theta_d) = f_{\mathbf{W}}(\mathbf{x}_m, g(m), h(\theta_d)), \tag{12}$$

where $g(m), h(\theta_d)$ are method-dependent functions. For PI, $g(m) = m/s$, $h(\theta_d) = \theta_d$. In subsequent sections, when introducing a new interpolation method, the authors sometimes only specify the functions $g(m)$ and $h(\theta_d)$. [p. 4]

Equation (12): Generalized interpolation form, parameterized by a position function $g(m)$ and a frequency function $h(\theta_d)$.

Additionally, the *wavelength* $\lambda_d$ of the RoPE embedding at $d$-th hidden dimension is defined as: [p. 4]

$$\lambda_d = \frac{2\pi}{\theta_d} = 2\pi b^{\frac{2d}{|D|}}. \tag{13}$$

Equation (13): Wavelength of RoPE at dimension $d$. The wavelength is the length of tokens needed for the RoPE embedding at dimension $d$ to perform a full rotation ($2\pi$).

The authors classify interpolation methods that do not care about the wavelength of the dimensions as "blind" interpolation methods (e.g., PI), while those that do (e.g., YaRN) are classified as "targeted" interpolation methods. [p. 4]

## 2.4 Related work [p. 4]

**ReRoPE [33]:** Also aims to extend the context size of existing models pre-trained with RoPE, and claims "infinite" context length without needing any fine-tuning. This claim is backed by a monotonically decreasing loss with increasing context length up to 16k on the Llama 2 13B model. It achieves context extension by modifying the attention mechanism and thus is not purely an embedding interpolation method. Since it is currently not compatible with Flash Attention 2 [13] and requires two attention passes during inference, the authors do not consider it for comparison. [p. 4]

**LM-Infinite [16]:** Concurrently proposes similar ideas to YaRN, but focuses on "on-the-fly" length generalization for non-fine-tuned models. Since they also modify the attention mechanism of the models, it is not an embedding interpolation method and is not immediately compatible with Flash Attention 2. [p. 4]
