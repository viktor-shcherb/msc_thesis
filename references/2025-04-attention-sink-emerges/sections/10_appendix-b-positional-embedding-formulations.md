# Appendix B: Detailed formulations of positional embedding [p. 16]

In this section, we provide detailed formulations of positional embedding (PE) in LMs. PEs could be classified into two categories: NoPE, absolute positional embedding, and learnable positional embedding belong to the same category since they are added to the initial hidden states: $\mathbf{H}^0 = \mathbf{X}\mathbf{W}_E + \mathbf{P}$. Here $\mathbf{P} = \{p_1, p_2, \cdots, p_T\} \in \mathbb{R}^{T \times d}$. Meanwhile, the dot product between each query and key is computed as $\langle q_i, k_j \rangle = q_i k_j^\top$.

## NoPE

NoPE (Kazemnejad et al., 2024) refers to no positional embedding. Therefore, $\mathbf{P} = \mathbf{0}$.

## Absolute PE

Each position vector $p_t$ in absolute positional embedding is a periodic function of token position $t$ following Vaswani et al. (2017):

$$
p_t = [\sin(\omega_1 t) \quad \cos(\omega_1 t) \quad \sin(\omega_2 t) \quad \cos(\omega_2 t) \quad \cdots \quad \sin(\omega_{d/2} t) \quad \cos(\omega_{d/2} t)], \quad (5)
$$

where $\omega_i = 1/10000^{2(i-1)/d}$.

## Learnable PE

Each position vector $p_t$ in learnable positional embeddings is a learnable parameter. Relative positional embedding, ALiBi, and rotary embeddings belong to another category since they consider the relative distance among tokens. Therefore, the initial hidden states are $\mathbf{H}^0 = \mathbf{X}\mathbf{W}_E$ but how to compute the dot product between each query and key is modified.

## Relative PE

The relative positional embeddings are adopted in T5 models (Raffel et al., 2020). A bias term is adopted for the dot product: $\langle q_i, k_j \rangle = q_i k_j^\top + g(i - j)$, where the definition for distance function $g(\cdot)$ is:

$$
g(i - j) = \begin{cases}
i - j & \text{if } i - j < B/2 \\
\frac{B}{2} + \lfloor \log(\frac{i-j}{B/2}) \rfloor \times \frac{B}{2} & \text{if } B/2 \leq i - j < D \\
B - 1 & \text{if } i - j \geq D
\end{cases} \quad (6)
$$

Here $B$ and $D$ refer to the number of buckets and maximum distance, respectively. In T5 models, $B = 32$ and $D = 128$.

## ALiBi

Similarly, ALiBi (Press et al., 2021) also adds a bias term to the dot product: $\langle q_i, k_j \rangle = q_i k_j^\top + g(i - j)$, where $g(i - j) = -(i - j) \cdot m$. $m$ is a head-specific slope fixed:

$$
m = 2^{-h/2^{-\log_2 H+3}}, \quad (7)
$$

where $1 \leq h \leq H$ is the head index and $H$ is the number of heads in the multi-head self-attention (MHSA). This slope $m$ is a geometric sequence. For instance, when $H = 8$, the sequence is $\frac{1}{2^1}, \frac{1}{2^2}, \cdots, \frac{1}{2^8}$. When $H = 16$, the sequence is $\frac{1}{2^{0.5}}, \frac{1}{2^1}, \cdots, \frac{1}{2^8}$.

## Rotary

Rotary (Su et al., 2024) is the most adopted position encoding approach in the LLM community. It projects queries and keys into another space through rotations:

$$
\langle q_i, k_j \rangle = (q_i \mathbf{R}_{\Theta, i}) (k_j \mathbf{R}_{\Theta, j})^\top = q_i \mathbf{R}_{\Theta, i} \mathbf{R}_{\Theta, j}^\top k_j^\top = q_i \mathbf{R}_{\Theta, i-j} k_j^\top, \quad (8)
$$

where $\mathbf{R}_{\Theta,(\cdot)}$ is a pre-defined rotation matrix:

$$
\mathbf{R}_{\Theta,m} = \begin{pmatrix}
\cos m\omega_1 & -\sin m\omega_1 & 0 & 0 & \cdots & 0 & 0 \\
\sin m\omega_1 & \cos m\omega_1 & 0 & 0 & \cdots & 0 & 0 \\
0 & 0 & \cos m\omega_2 & -\sin m\omega_2 & \cdots & 0 & 0 \\
0 & 0 & \sin m\omega_2 & \cos m\omega_2 & \cdots & 0 & 0 \\
\vdots & \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\
0 & 0 & 0 & 0 & \cdots & \cos m\omega_{d_h/2} & -\sin m\omega_{d_h/2} \\
0 & 0 & 0 & 0 & \cdots & \sin m\omega_{d_h/2} & \cos m\omega_{d_h/2}
\end{pmatrix}.
$$

Here $\omega_i = 1/10000^{2(i-1)/d_h}$ and $d_h = d/H$ is the hidden dimension in each head. From the above definition, it is noted that the rotation matrix $\mathbf{R}_{\Theta,m}^{\top}$ satisfies $\mathbf{R}_{\Theta,m}^{\top} = \mathbf{R}_{\Theta,-m}$ and $\mathbf{R}_{\Theta,i}\mathbf{R}_{\Theta,j} = \mathbf{R}_{\Theta,i+j}$.

---
[p. 16 end - Appendix B complete]
