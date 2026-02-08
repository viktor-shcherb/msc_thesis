# 2.3 Structured Matrices [p. 5]

[p. 5] General matrices $M \in \mathbb{R}^{(T,T)}$ require $T^2$ parameters to represent and $O(T^2)$ time to perform basic operations such as matrix-vector multiplication. **Structured matrices** are those that:

(i) can be represented in subquadratic (ideally linear) parameters through a compressed representation, and

(ii) have fast algorithms (most importantly matrix multiplication) by operating directly on this compressed representation.

Perhaps the most canonical families of structured matrices are sparse and low-rank matrices. However, there exist many other families, such as Toeplitz, Cauchy, Vandermonde, and butterfly matrices, which have all been used in machine learning for efficient models (Dao, Gu, et al. 2019; D. Fu et al. 2024; Gu, Gupta, et al. 2022; Thomas et al. 2018). Structured matrices are a powerful abstraction for efficient representations and algorithms. This work will show that SSMs are equivalent to another class of structured matrices that have not previously been used in deep learning, and use this connection to derive efficient methods and algorithms.
