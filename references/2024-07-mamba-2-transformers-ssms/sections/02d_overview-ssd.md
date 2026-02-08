# 2.4 Overview: Structured State Space Duality [p. 5-6]

[p. 5] While the paper develops a much richer framework of connections between SSMs, attention, and structured matrices, this subsection provides a brief summary of the main method, which is actually quite self-contained and simple algorithmically.

## Recurrent (Linear) Form

The state space dual (SSD) layer can be defined as a special case of the selective SSM (2). The standard computation of an SSM as a recurrence (or parallel scan) can be applied, which has linear complexity in sequence length. Compared to the version used in Mamba, SSD has two minor differences:

- The structure on $A$ is further simplified from diagonal to *scalar times identity* structure. Each $A_t$ can also be identified with just a scalar in this case.
- A larger head dimension P is used, compared to $P = 1$ used in Mamba. Typically $P = \{64, 128\}$ is chosen which is similar to conventions for modern Transformers.

Compared to the original selective SSM, these changes can be viewed as slightly decreasing the expressive power in return for significant training efficiency improvements. In particular, the new algorithms will allow the use of matrix multiplication units on modern accelerators.

## Dual (Quadratic) Form

[p. 6] The dual form of SSD is a quadratic computation closely related to attention, defined as:

$$(L \circ QK^\top) \cdot V$$

$$L_{ij} = \begin{cases} a_i \times \cdots \times a_{j+1} & i \geq j \\ 0 & i < j \end{cases}$$

where $a_i$ are input-dependent scalars bounded in $[0, 1]$.

Compared to standard softmax attention, there are two main differences:

- The softmax is dropped.
- The attention matrix is multiplied elementwise by an additional mask matrix $L$.

Both of these changes can be viewed as addressing problems in vanilla attention. For example, the softmax has been recently observed to cause problems in attention scores, such as the "attention sink" phenomenon (Darcet et al. 2024; Xiao et al. 2024). More importantly, the mask matrix $L$ can be viewed as replacing the heuristic positional embeddings of Transformers with a different *data-dependent positional mask* that controls how much information is transferred across time.

More broadly, this form is an instance of the **structured masked attention** generalization of linear attention, defined in Section 4.

## Matrix Form and SSD Algorithm

[p. 6] The various forms of SSD are connected through a unified matrix representation, by showing that SSMs have a matrix transformation form $Y = MX$ for a matrix $M_\theta \in \mathbb{R}^{(T,T)}$ that depends on $\theta = (A, B, C)$. In particular, the dual form of SSD is equivalent to naive (quadratic-time) multiplication by the matrix $M$, and the recurrent form is a particular efficient (linear-time) algorithm that leverages the structure in $M$.

Going beyond these, *any* algorithm for multiplication by $M$ can be applied. The proposed hardware-efficient SSD algorithm (Section 6) is a new structured matrix multiplication method that involves block decompositions of $M$, which obtains better efficiency tradeoffs than either the pure linear or quadratic forms. It is relatively simple and easy-to-implement compared to general selective SSMs (Gu and Dao 2023); Listing 1 provides a complete implementation in a few lines of code.

**Figure 1** (p. 2): "(Structured State-Space Duality.) This paper fleshes out the relationship between state space models and attention through the bridge of structured matrices."

The figure shows a diagram with bidirectional arrows connecting several concepts: "Semiseparable Matrices" connects to "State Space Models (SSM)" via Sec. 3, and "Structured Masked Attention (SMA)" connects to "Attention" via Sec. 4. SSM and Attention are connected through "State Space Duality (SSD)" via Sec. 5. "Structured Matrices" sits at the top, connecting down to both Semiseparable Matrices and SMA, and upward to "Efficient Algorithms" via Sec. 6. At the bottom, SSD connects down to "Mamba-2" via Sec. 7.
