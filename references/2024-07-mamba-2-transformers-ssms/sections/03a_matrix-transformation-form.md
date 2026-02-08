# 3 State Space Models are Structured Matrices / 3.1 The Matrix Transformation Form of State Space Models [p. 7]

[p. 7] This section explores different perspectives of the state space model as a sequence transformation, and outlines properties and algorithms of such maps. The main results of this section are about the equivalence between state space models and a family of structured matrices called semiseparable matrices, which imply new efficiency results (Theorems 3.5 and 3.7).

## 3.1 The Matrix Transformation Form of State Space Models

Recall that the definition of an SSM is defined as a parameterized map defined through (2). The theoretical framework starts by simply writing this transformation as a matrix multiplication mapping the vectors $x \in \mathbb{R}^{\mathsf{T}} \mapsto y \in \mathbb{R}^{\mathsf{T}}$.

By definition, $h_0 = B_0 x_0$. By induction,

$$h_t = A_t \ldots A_1 B_0 x_0 + A_t \ldots A_2 B_1 x_1 + \cdots + A_t A_{t-1} B_{t-2} x_{t-2} + A_t B_{t-1} x_{t-1} + B_t x_t$$

$$= \sum_{s=0}^{t} A_{t:s}^{\times} B_s x_s.$$

Multiplying by $C_t$ to produce $y_t$ and vectorizing the equation over $t \in [\mathsf{T}]$, the matrix transformation form of SSMs is derived:

$$y_t = \sum_{s=0}^{t} C_t^{\top} A_{t:s}^{\times} B_s x_s$$
$$y = \text{SSM}(A, B, C)(x) = Mx \tag{3}$$
$$M_{ji} \coloneqq C_j^{\top} A_j \cdots A_{i+1} B_i$$
