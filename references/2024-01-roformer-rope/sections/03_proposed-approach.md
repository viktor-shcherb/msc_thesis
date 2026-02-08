# Proposed approach [p. 4–6]

[p. 4] This section discusses the proposed rotary position embedding (RoPE). The relative position encoding problem is first formulated in Section 3.1, RoPE is derived in Section 3.2, and its properties are investigated in Section 3.3.

## Formulation

[p. 4] Transformer-based language modeling usually leverages the position information of individual tokens through a self-attention mechanism. As can be observed in Equation (2), $\boldsymbol{q}_m^\intercal \boldsymbol{k}_n$ typically enables knowledge conveyance between tokens at different positions. In order to incorporate relative position information, the inner product of query $\boldsymbol{q}_m$ and key $\boldsymbol{k}_n$ is required to be formulated by a function $g$, which takes only the word embeddings $\boldsymbol{x}_m$, $\boldsymbol{x}_n$, and their relative position $m - n$ as input variables. In other words, the inner product should encode position information only in the relative form:

$$\langle f_q(\boldsymbol{x}_m, m), f_k(\boldsymbol{x}_n, n) \rangle = g(\boldsymbol{x}_m, \boldsymbol{x}_n, m - n). \qquad (11)$$

The ultimate goal is to find an equivalent encoding mechanism to solve the functions $f_q(\boldsymbol{x}_m, m)$ and $f_k(\boldsymbol{x}_n, n)$ to conform the aforementioned relation. [p. 4]

## Rotary position embedding

### A 2D case

[p. 4] Beginning with a simple case with dimension $d = 2$, making use of the geometric property of vectors on a 2D plane and its complex form to prove (refer Section 3.4.1 for more details) that a solution to the formulation in Equation (11) is:

$$f_q(\boldsymbol{x}_m, m) = (\boldsymbol{W}_q \boldsymbol{x}_m)e^{im\theta}$$
$$f_k(\boldsymbol{x}_n, n) = (\boldsymbol{W}_k \boldsymbol{x}_n)e^{in\theta} \qquad (12)$$
$$g(\boldsymbol{x}_m, \boldsymbol{x}_n, m - n) = \text{Re}[(\boldsymbol{W}_q \boldsymbol{x}_m)(\boldsymbol{W}_k \boldsymbol{x}_n)^* e^{i(m-n)\theta}]$$

where $\text{Re}[\cdot]$ is the real part of a complex number and $(\boldsymbol{W}_k \boldsymbol{x}_n)^*$ represents the conjugate complex number of $(\boldsymbol{W}_k \boldsymbol{x}_n)$. $\theta \in \mathbb{R}$ is a preset non-zero constant. [p. 4]

$f_{\{q,k\}}$ can be written as a multiplication matrix:

$$f_{\{q,k\}}(\boldsymbol{x}_m, m) = \begin{pmatrix} \cos m\theta & -\sin m\theta \\ \sin m\theta & \cos m\theta \end{pmatrix} \begin{pmatrix} W_{\{q,k\}}^{(11)} & W_{\{q,k\}}^{(12)} \\ W_{\{q,k\}}^{(21)} & W_{\{q,k\}}^{(22)} \end{pmatrix} \begin{pmatrix} x_m^{(1)} \\ x_m^{(2)} \end{pmatrix} \qquad (13)$$

where $(x_m^{(1)}, x_m^{(2)})$ is $\boldsymbol{x}_m$ expressed in the 2D coordinates. Similarly, $g$ can be viewed as a matrix and thus enables the solution of formulation in Section 3.1 under the 2D case. Specifically, incorporating the relative position embedding is straightforward: simply rotate the affine-transformed word embedding vector by amount of angle multiples of its position index and thus interprets the intuition behind *Rotary Position Embedding*. [p. 4]

### General form

[p. 5] In order to generalize the results in 2D to any $\boldsymbol{x}_i \in \mathbb{R}^d$ where $d$ is even, the d-dimension space is divided into $d/2$ sub-spaces and combined in the merit of the linearity of the inner product, turning $f_{\{q,k\}}$ into:

$$f_{\{q,k\}}(\boldsymbol{x}_m, m) = \boldsymbol{R}_{\Theta,m}^d \boldsymbol{W}_{\{q,k\}} \boldsymbol{x}_m \qquad (14)$$

where

$$\boldsymbol{R}_{\Theta,m}^d = \begin{pmatrix} \cos m\theta_1 & -\sin m\theta_1 & 0 & 0 & \cdots & 0 & 0 \\ \sin m\theta_1 & \cos m\theta_1 & 0 & 0 & \cdots & 0 & 0 \\ 0 & 0 & \cos m\theta_2 & -\sin m\theta_2 & \cdots & 0 & 0 \\ 0 & 0 & \sin m\theta_2 & \cos m\theta_2 & \cdots & 0 & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & 0 & 0 & \cdots & \cos m\theta_{d/2} & -\sin m\theta_{d/2} \\ 0 & 0 & 0 & 0 & \cdots & \sin m\theta_{d/2} & \cos m\theta_{d/2} \end{pmatrix} \qquad (15)$$

is the rotary matrix with pre-defined parameters $\Theta = \{\theta_i = 10000^{-2(i-1)/d}, i \in [1, 2, ..., d/2]\}$. [p. 5]

**Figure 1** (p. 5): "Implementation of Rotary Position Embedding(RoPE)."
The figure shows a graphic illustration of RoPE in two parts. The top portion (labeled $d=2$) shows the 2D case: a query/key vector $(x_1, x_2)$ at position $m$ with a constant angle $\theta_1$ is rotated by $m\theta_1$ to produce a position-encoded query/key $(x'_1, x'_2)$. The bottom portion shows the general-dimensional case ("Enhanced Transformer with Rotary Position Embedding"): the query/key vector is divided into pairs of dimensions, each pair associated with its own angle parameter $\theta_1, \theta_2, \ldots, \theta_{d/2}$, and each pair is independently rotated by the corresponding angle multiplied by the position index. The left side shows the original query/key and the position indices (1 through 6), and the right side shows the resulting position-encoded query/key vectors.

Applying RoPE to self-attention in Equation (2), we obtain:

$$\boldsymbol{q}_m^\intercal \boldsymbol{k}_n = (\boldsymbol{R}_{\Theta,m}^d \boldsymbol{W}_q \boldsymbol{x}_m)^\intercal (\boldsymbol{R}_{\Theta,n}^d \boldsymbol{W}_k \boldsymbol{x}_n) = \boldsymbol{x}^\intercal \boldsymbol{W}_q \boldsymbol{R}_{\Theta,n-m}^d \boldsymbol{W}_k \boldsymbol{x}_n \qquad (16)$$

where $\boldsymbol{R}_{\Theta,n-m}^d = (\boldsymbol{R}_{\Theta,m}^d)^\intercal \boldsymbol{R}_{\Theta,n}^d$. Note that $\boldsymbol{R}_\Theta^d$ is an orthogonal matrix, which ensures stability during the process of encoding position information. In addition, due to the sparsity of $\boldsymbol{R}_\Theta^d$, applying matrix multiplication directly as in Equation (16) is not computationally efficient; the paper provides another realization in theoretical explanation. [p. 5]

In contrast to the additive nature of position embedding methods adopted in previous works (Equations (3) to (10)), this approach is multiplicative. RoPE naturally incorporates relative position information through rotation matrix product instead of altering terms in the expanded formulation of additive position encoding when applied with self-attention. [p. 5]

## Properties of RoPE

[p. 5] **Long-term decay:** Following Vaswani et al. [2017], set $\theta_i = 10000^{-2i/d}$. One can prove that this setting provides a long-term decay property (refer to Section 3.4.3 for more details), which means the inner-product will decay when the relative position increases. This property coincides with the intuition that a pair of tokens with a long relative distance should have less connection.

[p. 5–6] **RoPE with linear attention:** The self-attention can be rewritten in a more general form.

$$\text{Attention}(\boldsymbol{Q}, \boldsymbol{K}, \boldsymbol{V})_m = \frac{\sum_{n=1}^{N} \text{sim}(\boldsymbol{q}_m, \boldsymbol{k}_n) \boldsymbol{v}_n}{\sum_{n=1}^{N} \text{sim}(\boldsymbol{q}_m, \boldsymbol{k}_n)}. \qquad (17)$$

The original self-attention chooses $\text{sim}(\boldsymbol{q}_m, \boldsymbol{k}_n) = \exp(\boldsymbol{q}_m^\intercal \boldsymbol{k}_n / \sqrt{d})$. Note that the original self-attention should compute the inner product of query and key for every pair of tokens, which has a quadratic complexity $\mathcal{O}(N^2)$. Following Katharopoulos et al. [2020], the linear attentions reformulate Equation (17) as:

$$\text{Attention}(\boldsymbol{Q}, \boldsymbol{K}, \boldsymbol{V})_m = \frac{\sum_{n=1}^{N} \phi(\boldsymbol{q}_m)^\intercal \varphi(\boldsymbol{k}_n) \boldsymbol{v}_n}{\sum_{n=1}^{N} \phi(\boldsymbol{q}_m)^\intercal \varphi(\boldsymbol{k}_n)}, \qquad (18)$$

where $\phi(\cdot)$, $\varphi(\cdot)$ are usually non-negative functions. The authors of Katharopoulos et al. [2020] have proposed $\phi(x) = \varphi(x) = \text{elu}(x) + 1$ and first computed the multiplication between keys and values using the associative property of matrix multiplication. A softmax function is used in Shen et al. [2021] to normalize queries and keys separately before the inner product, which is equivalent to $\phi(\boldsymbol{q}_i) = \text{softmax}(\boldsymbol{q}_i)$ and $\varphi(\boldsymbol{k}_j) = \exp(\boldsymbol{k}_j)$. [p. 6]

Since RoPE injects position by rotation, which keeps the norm of hidden representations unchanged, RoPE can be combined with linear attention by multiplying the rotation matrix with the outputs of the non-negative functions:

$$\text{Attention}(\boldsymbol{Q}, \boldsymbol{K}, \boldsymbol{V})_m = \frac{\sum_{n=1}^{N} \left(\boldsymbol{R}_{\Theta,m}^d \phi(\boldsymbol{q}_m)\right)^\intercal \left(\boldsymbol{R}_{\Theta,n}^d \varphi(\boldsymbol{k}_n)\right) \boldsymbol{v}_n}{\sum_{n=1}^{N} \phi(\boldsymbol{q}_m)^\intercal \varphi(\boldsymbol{k}_n)}. \qquad (19)$$

It is noteworthy that the denominator is kept unchanged to avoid the risk of dividing zero, and the summation in the numerator could contain negative terms. Although the weights for each value $\boldsymbol{v}_i$ in Equation (19) are not strictly probabilistic normalized, the authors argue that the computation can still model the importance of values. [p. 6]

## Theoretical Explanation

### Derivation of RoPE under 2D

[p. 6] Under the case of $d = 2$, consider two-word embedding vectors $\boldsymbol{x}_q$, $\boldsymbol{x}_k$ corresponding to query and key and their position $m$ and $n$, respectively. According to eq. (1), their position-encoded counterparts are:

$$\boldsymbol{q}_m = f_q(\boldsymbol{x}_q, m), \qquad (20)$$
$$\boldsymbol{k}_n = f_k(\boldsymbol{x}_k, n),$$

where the subscripts of $\boldsymbol{q}_m$ and $\boldsymbol{k}_n$ indicate the encoded positions information. Assume that there exists a function $g$ that defines the inner product between vectors produced by $f_{\{q,k\}}$:

$$\boldsymbol{q}_m^\intercal \boldsymbol{k}_n = \langle f_q(\boldsymbol{x}_m, m), f_k(\boldsymbol{x}_n, n) \rangle = g(\boldsymbol{x}_m, \boldsymbol{x}_n, n - m), \qquad (21)$$

we further require the below initial condition to be satisfied:

$$\boldsymbol{q} = f_q(\boldsymbol{x}_q, 0), \qquad (22)$$
$$\boldsymbol{k} = f_k(\boldsymbol{x}_k, 0),$$

which can be read as the vectors with empty position information encoded. Given these settings, the paper attempts to find a solution of $f_q$, $f_k$. First, taking advantage of the geometric meaning of vector in 2D and its complex counter part, decompose functions in Equations (20) and (21) into:

$$f_q(\boldsymbol{x}_q, m) = R_q(\boldsymbol{x}_q, m)e^{i\Theta_q(\boldsymbol{x}_q, m)},$$
$$f_k(\boldsymbol{x}_k, n) = R_k(\boldsymbol{x}_k, n)e^{i\Theta_k(\boldsymbol{x}_k, n)}, \qquad (23)$$
$$g(\boldsymbol{x}_q, \boldsymbol{x}_k, n - m) = R_g(\boldsymbol{x}_q, \boldsymbol{x}_k, n - m)e^{i\Theta_g(\boldsymbol{x}_q, \boldsymbol{x}_k, n - m)},$$

where $R_f$, $R_g$ and $\Theta_f$, $\Theta_g$ are the radical and angular components for $f_{\{q,k\}}$ and $g$, respectively. Plugging them into Equation (21), we get the relation:

$$R_q(\boldsymbol{x}_q, m) R_k(\boldsymbol{x}_k, n) = R_g(\boldsymbol{x}_q, \boldsymbol{x}_k, n - m), \qquad (24)$$
$$\Theta_k(\boldsymbol{x}_k, n) - \Theta_q(\boldsymbol{x}_q, m) = \Theta_g(\boldsymbol{x}_q, \boldsymbol{x}_k, n - m),$$

with the corresponding initial condition as:

$$\boldsymbol{q} = \|\boldsymbol{q}\|e^{i\theta_q} = R_q(\boldsymbol{x}_q, 0)e^{i\Theta_q(\boldsymbol{x}_q, 0)},$$
$$\boldsymbol{k} = \|\boldsymbol{k}\|e^{i\theta_k} = R_k(\boldsymbol{x}_k, 0)e^{i\Theta_k(\boldsymbol{x}_k, 0)}, \qquad (25)$$

where $\|\boldsymbol{q}\|$, $\|\boldsymbol{k}\|$ and $\theta_q$, $\theta_k$ are the radial and angular part of $\boldsymbol{q}$ and $\boldsymbol{k}$ on the 2D plane. [p. 7]

Next, setting $m = n$ in Equation (24) and taking into account initial conditions in Equation (25):

$$R_q(\boldsymbol{x}_q, m) R_k(\boldsymbol{x}_k, m) = R_q(\boldsymbol{x}_q, 0) R_k(\boldsymbol{x}_k, 0) = \|\boldsymbol{q}\|\|\boldsymbol{k}\|, \qquad (26a)$$
$$\Theta_k(\boldsymbol{x}_k, m) - \Theta_q(\boldsymbol{x}_q, m) = \Theta_k(\boldsymbol{x}_k, 0) - \Theta_q(\boldsymbol{x}_q, 0) = \theta_k - \theta_q. \qquad (26b)$$

On one hand, from a straightforward solution of $R_f$ could be formed from Equation (26a):

$$R_q(\boldsymbol{x}_q, m) = R_q(\boldsymbol{x}_q, 0) = \|\boldsymbol{q}\|$$
$$R_k(\boldsymbol{x}_k, n) = R_k(\boldsymbol{x}_k, 0) = \|\boldsymbol{k}\| \qquad (27)$$
$$R_g(\boldsymbol{x}_q, \boldsymbol{x}_k, n - m) = R_g(\boldsymbol{x}_q, \boldsymbol{x}_k, 0) = \|\boldsymbol{q}\|\|\boldsymbol{k}\|$$

which interprets the radial functions $R_q$, $R_k$ and $R_g$ are independent from the position information. On the other hand, as can be noticed in Equation (26b), $\Theta_q(\boldsymbol{x}_q, m) - \theta_q = \Theta_k(\boldsymbol{x}_k, m) - \theta_k$ indicates that the angular functions does not dependent on query and key, we set them to $\Theta_f := \Theta_q = \Theta_k$ and term $\Theta_f(\boldsymbol{x}_{\{q,k\}}, m) - \theta_{\{q,k\}}$ is a function of position $m$ and is independent of word embedding $\boldsymbol{x}_{\{q,k\}}$, we denote it as $\phi(m)$, yielding:

$$\Theta_f(\boldsymbol{x}_{\{q,k\}}, m) = \phi(m) + \theta_{\{q,k\}}, \qquad (28)$$

Further, by plugging $n = m + 1$ to Equation (24) and consider the above equation, we can get:

$$\phi(m + 1) - \phi(m) = \Theta_g(\boldsymbol{x}_q, \boldsymbol{x}_k, 1) + \theta_q - \theta_k, \qquad (29)$$

Since RHS is a constant irrelevant to $m$, $\phi(m)$ with continuous integer inputs produce an arithmetic progression:

$$\phi(m) = m\theta + \gamma, \qquad (30)$$

where $\theta, \gamma \in \mathbb{R}$ are constants and $\theta$ is non-zero. To summarize the solutions from Equations (27) to (30):

$$f_q(\boldsymbol{x}_q, m) = \|\boldsymbol{q}\|e^{i\theta_q + m\theta + \gamma} = \boldsymbol{q}e^{i(m\theta + \gamma)},$$
$$f_k(\boldsymbol{x}_k, n) = \|\boldsymbol{k}\|e^{i\theta_k + n\theta + \gamma} = \boldsymbol{k}e^{i(n\theta + \gamma)}. \qquad (31)$$

Note that we do not apply any constrains to $f_q$ and $f_k$ of Equation (22), thus $f_q(\boldsymbol{x}_m, 0)$ and $f_k(\boldsymbol{x}_n, 0)$ are left to choose freely. To make our results comparable to Equation (3), we define:

$$\boldsymbol{q} = f_q(\boldsymbol{x}_m, 0) = \boldsymbol{W}_q \boldsymbol{x}_n,$$
$$\boldsymbol{k} = f_k(\boldsymbol{x}_n, 0) = \boldsymbol{W}_k \boldsymbol{x}_n. \qquad (32)$$

Then, we simply set $\gamma = 0$ in Equation (31) of the final solution:

$$f_q(\boldsymbol{x}_m, m) = (\boldsymbol{W}_q \boldsymbol{x}_m)e^{im\theta},$$
$$f_k(\boldsymbol{x}_n, n) = (\boldsymbol{W}_k \boldsymbol{x}_n)e^{in\theta}. \qquad (33)$$

### Computational efficient realization of rotary matrix multiplication

[p. 7] Taking advantage of the sparsity of $\boldsymbol{R}_{\Theta,m}^d$ in Equation (15), a more computational efficient realization of a multiplication of $R_\Theta^d$ and $\boldsymbol{x} \in \mathbb{R}^d$ is:

$$\boldsymbol{R}_{\Theta,m}^d \boldsymbol{x} = \begin{pmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \\ \vdots \\ x_{d-1} \\ x_d \end{pmatrix} \otimes \begin{pmatrix} \cos m\theta_1 \\ \cos m\theta_1 \\ \cos m\theta_2 \\ \cos m\theta_2 \\ \vdots \\ \cos m\theta_{d/2} \\ \cos m\theta_{d/2} \end{pmatrix} + \begin{pmatrix} -x_2 \\ x_1 \\ -x_4 \\ x_3 \\ \vdots \\ -x_d \\ x_{d-1} \end{pmatrix} \otimes \begin{pmatrix} \sin m\theta_1 \\ \sin m\theta_1 \\ \sin m\theta_2 \\ \sin m\theta_2 \\ \vdots \\ \sin m\theta_{d/2} \\ \sin m\theta_{d/2} \end{pmatrix} \qquad (34)$$

where $\otimes$ denotes element-wise product. This avoids the full matrix multiplication and is more computationally efficient. [p. 7]

### Long-term decay of RoPE

[p. 8] We can group entries of vectors $\boldsymbol{q} = \boldsymbol{W}_q \boldsymbol{x}_m$ and $\boldsymbol{k} = \boldsymbol{W}_k \boldsymbol{x}_n$ in pairs, and the inner product of RoPE in Equation (16) can be written as a complex number multiplication.

$$(\boldsymbol{R}_{\Theta,m}^d \boldsymbol{W}_q \boldsymbol{x}_m)^\intercal (\boldsymbol{R}_{\Theta,n}^d \boldsymbol{W}_k \boldsymbol{x}_n) = \text{Re}\left[\sum_{i=0}^{d/2-1} \boldsymbol{q}_{[2i:2i+1]} \boldsymbol{k}_{[2i:2i+1]}^* e^{i(m-n)\theta_i}\right] \qquad (35)$$

where $\boldsymbol{q}_{[2i:2i+1]}$ represents the $2i^{th}$ to $(2i+1)^{th}$ entries of $\boldsymbol{q}$. Denote $h_i = \boldsymbol{q}_{[2i:2i+1]} \boldsymbol{k}_{[2i:2i+1]}^*$ and $S_j = \sum_{i=0}^{j-1} e^{i(m-n)\theta_i}$, and let $h_{d/2} = 0$ and $S_0 = 0$, we can rewrite the summation using Abel transformation

$$\sum_{i=0}^{d/2-1} \boldsymbol{q}_{[2i:2i+1]} \boldsymbol{k}_{[2i:2i+1]}^* e^{i(m-n)\theta_i} = \sum_{i=0}^{d/2-1} h_i(S_{i+1} - S_i) = -\sum_{i=0}^{d/2-1} S_{i+1}(h_{i+1} - h_i). \qquad (36)$$

Thus,

$$\left|\sum_{i=0}^{d/2-1} \boldsymbol{q}_{[2i:2i+1]} \boldsymbol{k}_{[2i:2i+1]}^* e^{i(m-n)\theta_i}\right| = \left|\sum_{i=0}^{d/2-1} S_{i+1}(h_{i+1} - h_i)\right|$$
$$\leq \sum_{i=0}^{d/2-1} |S_{i+1}||(h_{i+1} - h_i)| \qquad (37)$$
$$\leq \left(\max_i |h_{i+1} - h_i|\right) \sum_{i=0}^{d/2-1} |S_{i+1}|$$

Note that the value of $\frac{1}{d/2} \sum_{i=1}^{d/2} |S_i|$ decay with the relative distance $m - n$ increases by setting $\theta_i = 10000^{-2i/d}$, as shown in Figure 2. [p. 8]

**Figure 2** (p. 8): "Long-term decay of RoPE."
The figure shows a line plot with "relative distance" on the x-axis (ranging from 0 to approximately 275) and "relative upper bound" on the y-axis (ranging from approximately 6 to 22). The curve starts high (around 20) at small relative distances and exhibits an oscillating but overall decaying trend as relative distance increases, settling to around 6-8 at large distances. This demonstrates the long-term decay property of RoPE: the upper bound on the inner product decreases as the relative distance between tokens increases.
