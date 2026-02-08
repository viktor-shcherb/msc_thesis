# Appendix B: Efficient Computation of the Attention with Relative Positional Embedding [p. 11–13]

As discussed in section 3.3, the naive way of computing **W**_{k,R} **R**_{i-j} for all pairs (i, j) is subject to a quadratic cost. Here, a simple method with only a linear cost is presented. [p. 11]

## Key observation

The relative distance i - j can only be integer from 0 to M + L - 1, where M is the memory length and L is the segment length. Hence, the rows of the matrix: [p. 11]

$$\mathbf{Q} \coloneqq \begin{bmatrix} \mathbf{R}_{M+L-1}^\top \\ \mathbf{R}_{M+L-2}^\top \\ \vdots \\ \mathbf{R}_1^\top \\ \mathbf{R}_0^\top \end{bmatrix} \mathbf{W}_{k,R}^\top = \begin{bmatrix} [\mathbf{W}_{k,R} \mathbf{R}_{M+L-1}]^\top \\ [\mathbf{W}_{k,R} \mathbf{R}_{M+L-2}]^\top \\ \vdots \\ [\mathbf{W}_{k,R} \mathbf{R}_1]^\top \\ [\mathbf{W}_{k,R} \mathbf{R}_0]^\top \end{bmatrix} \in \mathbb{R}^{(M+L) \times d}$$

consist of all possible vector outputs of **W**_{k,R} **R**_{i-j} for any (i, j). Note that **Q** has been defined in a reversed order, i.e., **Q**_k = **W**_{k,R} **R**_{M+L-1-k}, to make further discussion easier. [p. 11]

## Computing term (b)

Collect term (b) for all possible i, j into the following L x (M + L) matrix **B**: [p. 12]

$$\mathbf{B} = \begin{bmatrix} q_0^\top \mathbf{W}_{k,R} \mathbf{R}_M & \cdots & q_0^\top \mathbf{W}_{k,R} \mathbf{R}_0 & 0 & \cdots & 0 \\ q_1^\top \mathbf{W}_{k,R} \mathbf{R}_{M+1} & \cdots & q_1^\top \mathbf{W}_{k,R} \mathbf{R}_1 & q_1^\top \mathbf{W}_{k,R} \mathbf{R}_0 & \cdots & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ q_{L-1}^\top \mathbf{W}_{k,R} \mathbf{R}_{M+L-1} & \cdots & q_{L-1}^\top \mathbf{W}_{k,R} \mathbf{R}_{M+L-1} & q_{L-1}^\top \mathbf{W}_{k,R} \mathbf{R}_{L-1} & \cdots & q_{L-1}^\top \mathbf{W}_{k,R} \mathbf{R}_0 \end{bmatrix}$$

This can be re-expressed in terms of **Q**: [p. 12]

$$\mathbf{B} = \begin{bmatrix} q_0^\top \mathbf{Q}_{L-1} & \cdots & q_0^\top \mathbf{Q}_{M+L-1} & 0 & \cdots & 0 \\ q_1^\top \mathbf{Q}_{L-2} & \cdots & q_1^\top \mathbf{Q}_{M+L-2} & q_1^\top \mathbf{Q}_{M+L-1} & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots & \ddots & \vdots \\ q_{L-1}^\top \mathbf{Q}_0 & \cdots & q_{L-1}^\top \mathbf{Q}_M & q_{L-1}^\top \mathbf{Q}_{M+1} & \cdots & q_{L-1}^\top \mathbf{Q}_{M+L-1} \end{bmatrix}$$

Then, define: [p. 12]

$$\widetilde{\mathbf{B}} = \mathbf{q} \mathbf{Q}^\top = \begin{bmatrix} q_0^\top \mathbf{Q}_0 & \cdots & q_0^\top \mathbf{Q}_M & q_0^\top \mathbf{Q}_{M+1} & \cdots & q_0^\top \mathbf{Q}_{M+L-1} \\ q_1^\top \mathbf{Q}_0 & \cdots & q_1^\top \mathbf{Q}_M & q_1^\top \mathbf{Q}_{M+1} & \cdots & q_1^\top \mathbf{Q}_{M+L-1} \\ \vdots & \vdots & \ddots & \vdots & \ddots & \vdots \\ q_{L-1}^\top \mathbf{Q}_0 & \cdots & q_{L-1}^\top \mathbf{Q}_M & q_{L-1}^\top \mathbf{Q}_{M+1} & \cdots & q_{L-1}^\top \mathbf{Q}_{M+L-1} \end{bmatrix}$$

The i-th row of **B** is simply a left-shifted version of the i-th row of **B-tilde**. Hence, the computation of **B** only requires a matrix multiplication **qQ**^T to compute **B-tilde** and then a set of left-shifts. [p. 12]

## Computing term (d)

Similarly, collect all term (d) for all possible i, j into another L x (M + L) matrix **D**: [p. 12]

$$\mathbf{D} = \begin{bmatrix} v^\top \mathbf{Q}_{L-1} & \cdots & v^\top \mathbf{Q}_{M+L-1} & 0 & \cdots & 0 \\ v^\top \mathbf{Q}_{L-2} & \cdots & v^\top \mathbf{Q}_{M+L-2} & v^\top \mathbf{Q}_{M+L-1} & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots & \ddots & \vdots \\ v^\top \mathbf{Q}_0 & \cdots & v^\top \mathbf{Q}_M & v^\top \mathbf{Q}_{M+1} & \cdots & v^\top \mathbf{Q}_{M+L-1} \end{bmatrix}$$

Then, define: [p. 13]

$$\widetilde{\mathbf{d}} = [\mathbf{Q} v]^\top = \begin{bmatrix} v^\top \mathbf{Q}_0 & \cdots & v^\top \mathbf{Q}_M & v^\top \mathbf{Q}_{M+1} & \cdots & v^\top \mathbf{Q}_{M+L-1} \end{bmatrix}$$

Again, each row of **D** is simply a left-shift version of **d-tilde**. Hence, the main computation cost comes from the matrix-vector multiplication **d-tilde** = [**Q** v]^T, which is not expensive any more. [p. 13]

## Summary

Both terms (b) and (d) can be computed in linear cost by:
1. Computing the full product (**qQ**^T for term b, **Qv** for term d)
2. Applying left-shifts to extract the correct relative-distance entries for each query position
