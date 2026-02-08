# 3.2 Semiseparable Matrices [p. 7-9]

[p. 7] $M$ in equation (3) is a particular representation of a class of matrices known as semiseparable matrices. Semiseparable matrices are a fundamental matrix structure. This subsection first defines these matrices and their properties.

## Definition 3.1

> **Definition 3.1.** *A (lower triangular) matrix $M$ is* N*-semiseparable if every submatrix contained in the lower triangular portion (i.e. on or below the diagonal) has rank at most* N*. We call* N *the order or rank of the semiseparable matrix.* [p. 7]

Definition 3.1, and other forms of related "separable" structure (e.g. quasiseparable matrices and other definitions of semiseparable matrices) are sometimes called **structured rank matrices** (or rank-structured matrices) because they are characterized by rank conditions on their submatrices. Semiseparable matrices have many structured representations including the hierarchical semiseparable (HSS), sequential semiseparable (SSS), and Bruhat forms (Pernet and Storjohann 2018). The paper primarily uses the SSS form.

## 3.2.1 The Sequentially Semiseparable (SSS) Representation

> **Definition 3.2.** *A lower triangular matrix $M \in \mathbb{R}^{(\mathsf{T},\mathsf{T})}$ has a* N*-sequentially semiseparable (SSS) representation if it can be written in the form*
>
> $$M_{ji} = C_j^{\top} A_j \cdots A_{i+1} B_i \tag{4}$$
>
> *for vectors $B_0, \ldots, B_{\mathsf{T}-1}, C_0, \ldots, C_{\mathsf{T}-1} \in \mathbb{R}^{\mathsf{N}}$ and matrices $A_0, \ldots, A_{\mathsf{T}-1} \in \mathbb{R}^{(\mathsf{N},\mathsf{N})}$.* [p. 7]

The operator SSS is defined so that $M = \text{SSS}(A_{0:\mathsf{T}}, B_{0:\mathsf{T}}, C_{0:\mathsf{T}})$.

[p. 8] A fundamental result of semiseparable matrices is that they are exactly equivalent to matrices with SSS representations. One direction can be deduced with a simple constructive proof.

**Lemma 3.3.** *An* N*-SSS matrix $M$ with representation (4) is* N*-semiseparable.*

*Proof.* Consider any off-diagonal block $M_{j':j, i':i}$ where $j' > j \geq i > i'$. This has an explicit rank-N factorization as

$$\begin{bmatrix} C_j^{\top} A_{j:i'}^{\times} B_{i'} & \cdots & C_j^{\top} A_{j:i-1}^{\times} B_{i-1} \\ \vdots & & \vdots \\ C_{j'-1}^{\top} A_{j'-1:i'}^{\times} B_{i'} & \cdots & C_{j'-1}^{\top} A_{j'-1:i-1}^{\times} B_{i-1} \end{bmatrix} = \begin{bmatrix} C_j^{\top} A_{j:j}^{\times} \\ \vdots \\ C_{j'-1}^{\top} A_{j'-1:j}^{\times} \end{bmatrix} A_{j:i-1}^{\times} \begin{bmatrix} A_{i-1:i'}^{\times} B_{i'} & \cdots & A_{i-1:i-1}^{\times} B_{i-1} \end{bmatrix}. \tag{5}$$

Equation (5) will be used extensively in deriving fast algorithms for sequence models. The other direction is well-established in the literature on semiseparable matrices.

**Proposition 3.4.** *Every* N*-semiseparable matrix has a* N*-SSS representation.*

[p. 8] Furthermore, note that although Definition 3.2 involves $O(\mathsf{N}^2 \mathsf{T})$ parameters for the representation (in particular to store the $A$ matrices), it can actually be compressed down to $O(\mathsf{N}\mathsf{T})$ parameters, which is asymptotically tight (Pernet, Signargout, and Villard 2023). Therefore in the rest of this paper the authors conflate the structured matrix class (Definition 3.1) and a particular representation of it (Definition 3.2); they always use this representation instead of other candidates. In turn N-SS is used to refer to an N-semiseparable matrix in SSS form.

Semiseparable matrices are a fundamental matrix structure and have many important properties. They are deeply related to recurrences at large, and can be defined by multiple characterizations (e.g. Definitions 3.1 and 3.2) which reveal different connections and efficient algorithms for them. Other properties are mentioned in Appendix C.1.

**Remark 2.** *The notion of semiseparability is very broad and many similar but subtlely different definitions appear in the literature; our definitions may differ slightly from other conventions. First, because we are primarily concerned with causal or autoregressive settings in this paper, we have restricted the definition of semiseparability to the triangular case; Definition 3.1 more formally might be called* (N, 0)*-semiseparability by some authors. Some authors may also instead refer to it as a form of quasiseparability (Eidelman and Gohberg 1999; Pernet 2016). See Vandebril et al. (2005) for a brief survey.* [p. 8]

## 3.2.2 1-Semiseparable Matrices: the Scalar SSM Recurrence

[p. 8] The special case of 1-SS matrices is singled out. In this case, the $C_j$ and $B_i$ are scalars, and can be factored out of the SSS representation (4) (lower-case is used to emphasize that the parameters are scalars in this case):

$$\text{SSS}(a, b, c) = \text{diag}(c) \cdot M \cdot \text{diag}(b) \qquad \text{where} \qquad M_{ji} = a_{j:i}^{\times}.$$

Since diagonal matrices are easy to handle (e.g. multiplication by a diagonal matrix is the same as elementwise scalar multiplication), these terms can be ignored. Thus the basic representation of a 1-SS matrix is $M_{ji} = a_{j:i}^{\times}$ or

$$M = \text{1SS}(a_{0:\mathsf{T}}) \coloneqq \begin{bmatrix} 1 & & & \\ a_1 & 1 & & \\ a_2 a_1 & a_2 & 1 & \\ \vdots & \vdots & \ddots & \ddots \\ a_{\mathsf{T}-1} \ldots a_1 & a_{\mathsf{T}-1} \ldots a_2 & \cdots & a_{\mathsf{T}-1} & 1 \end{bmatrix}. \tag{6}$$

[p. 8-9] The importance of 1-SS matrices lies in their equivalence to the minimal form of a scalar recurrence -- the case of a degenerate SSM with state dimension $\mathsf{N} = 1$ and no $(B, C)$ projections. Note that multiplication $y = Mx$ can be computed by the recurrence

$$y_t = a_{t:0} x_0 + \cdots + a_{t:t} x_t$$
$$= a_t (a_{t-1:0} x_0 + \cdots + a_{t-1:t-1} x_{t-1}) + a_{t:t} x_t \tag{7}$$
$$= a_t y_{t-1} + x_t.$$

**Figure 2** (p. 9): "(**State Space Models are Semiseparable Matrix Transformations.**) As sequence transformations, state space models can be represented as a matrix transformation $M \in \mathbb{R}^{(\mathsf{T},\mathsf{T})}$ acting on the sequence dimension T, sharing the same matrix for each channel in a head (*Left*). This matrix is a semiseparable matrix (*Right*), which is a rank-structured matrix where every submatrix contained on-and-below the diagonal (*Blue*) has rank at most N, equal to the SSM's state dimension."

The figure shows two parts: (*Left*) A diagram of the sequence transformation with Inputs $X$ at bottom, Outputs $Y$ at top, Head dimension P on the vertical axis and Sequence dimension T on the horizontal axis, with a heatmap of the Sequence Transformation Matrix $M$ in between. (*Right*) The explicit matrix entries $M_{ji} = C_j^{\top} A_{j} \cdots A_{i+1} B_i$ displayed in a lower-triangular matrix form, with a blue-shaded submatrix illustrating the rank constraint.

[p. 9] Matrix multiplication by 1-SS matrices is also referred to as the **scalar SSM recurrence** or the `cumprodsum` (cumulative product sum; a generalization of cumulative product and cumulative sum) operator. As the fundamental form of recurrence, multiplication by 1-SS matrices is important as a building block for the main algorithms.

> "one of the central themes of this paper is that *many algorithms on sequence models can be reduced to structured matrix multiplication algorithms*." [p. 9]

1-SS matrices exemplify this connection: there are many fast algorithms for computing the primitive scalar recurrence or `cumprodsum` operator, and all of them turn out to be equivalent to different structured factorization of 1-SS matrices. Appendix B is dedicated to these algorithms for 1-SS matrix multiplication.
