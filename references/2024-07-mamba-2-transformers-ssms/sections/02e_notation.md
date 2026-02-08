# 2.5 Notation [p. 6]

[p. 6] The paper prefers precise notation that can be mapped to code.

## Matrices and Vectors

Lower case is used to denote vectors (tensors with a single axis) and upper case to denote matrices (tensors with more than one axes). Matrices are not bolded. Sometimes, if a matrix is tied or repeated along one axis (and hence can also be viewed as a vector), either upper or lower case may be used. The operator $\cdot$ denotes scalar or matrix multiplication while $\circ$ denotes Hadamard (elementwise) multiplication.

## Indexing

Python-style indexing is used, e.g. $i : j$ refers to the range $(i, i+1, \ldots, j-1)$ when $i < j$ and $(i, i-1, \ldots, j+1)$ when $i > j$. For any symbol $v$, $v_{j:i}$ for $j \geq i$ denotes the sequence $(v_j, \ldots, v_{i+1})$. $[i]$ is equivalent to $0 : i = (0, \ldots, i-1)$. For shorthand, $v_{j:i}^\times$ denotes the product $v_j \times \cdots \times v_{i+1}$.

Footnote 3: In some contexts, it is always clear that the notation $a_{i:j}$ or $A_{i:j}$ means $a_{i:j}^\times$, and the superscript is omitted.

## Dimensions

Capital letters in typewriter fonts (e.g. D, N, T) are often used to denote dimensions and tensor shapes. Instead of the traditional notation $M \in \mathbb{R}^{T \times T}$ they frequently use $M \in \mathbb{R}^{(T,T)}$ to reflect tensor shapes in code.

Footnote 2: In this work, this happens only with the $A$ parameter of SSMs.

## Tensor Contractions

The paper will heavily rely on **tensor contraction** or **einsum** notation both for clarity and as a central tool in stating and proving results. The reader is assumed to be familiar with this notation, which is commonly used in modern tensor libraries such as numpy.

---
[p. 7 continued]

For example, `contract(MN, NK → MK)` denotes the matrix-matrix multiplication operator, and in this notation `contract(MN, NK → MK)(X, Y)` (which is equivalent to $X \cdot Y$) can be translated to code as `numpy.einsum('mn, nk → mk', X, Y)`.

A large glossary of notation is included in Appendix A.
