# 3.3 State Space Models are Semiseparable Matrices [p. 9]

[p. 9] Recall that the definition of an SSM is defined as a parameterized map defined through Definition 2.1. The connection between SSMs and semiseparable matrices follows from simply writing this transformation as a matrix multiplication mapping the vectors $x \mapsto y \in \mathbb{R}^{\mathsf{T}}$.

Equation (3) directly establishes the link between state space models and the sequentially semiseparable representation, which in turn are equivalent to semiseparable matrices in general (Lemma 3.3 and Proposition 3.4).

**Theorem 3.5.** *The state space model transformation $y = \text{SSM}(A, B, C)(x)$ with state size* N *is identical to matrix multiplication by an* N*-SS matrix in sequentially semiseparable representation $y = \text{SSS}(A, B, C) \cdot x$.* [p. 9]

In other words the sequence transformation operator SSM (Definition 2.2) coincides with the matrix construction operator SSS (Definition 3.2), and they are used interchangeably (or sometimes SS as shorthand). Furthermore -- by a twist of fate -- structured state space models and sequentially semiseparable matrices have the same acronyms, underscoring their equivalence. Conveniently any of these acronyms can be used: SSM (state space model or semiseparable matrix), SSS (structured state space or sequentially semiseparable), or SS (state space or semiseparable) interchangeably to unambiguously refer to either concept. However, the paper generally uses the convention that SSM refers to state space model, SS refers to semiseparable, and SSS refers to sequentially semiseparable.

Figure 2 illustrates the sequence transformation perspective of state space models as semiseparable matrices.
