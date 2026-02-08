# 3.4 Computing State Space Models through Structured Matrix Algorithms [p. 10-11]

[p. 10] The reason Theorem 3.5 is important is that it allows the *reduction of the problem of efficient computation of SSMs (and other sequence models) into efficient algorithms for structured matrix multiplication*. A brief overview is provided, deferring the main new algorithm to Section 6, after showing the equivalence of SSMs to other sequence models in Sections 4 and 5.

As previously defined, semiseparable matrices (i.e. rank-structured matrices) are a classical type of structured matrix:

(i) They have compressed representations such as the SSS form which has only $O(\mathsf{T})$ instead of $O(\mathsf{T}^2)$ parameters.

(ii) They have fast algorithms operating directly on the compressed representation.

Furthermore, the parameterization and matrix multiplication cost can be tight in the semiseparable order.

**Proposition 3.6** (Pernet, Signargout, and Villard (2023)). *An* N*-SS matrix of size* T *can be represented in $O(\mathsf{N}\mathsf{T})$ parameters and has matrix-vector multiplication in time and space $O(\mathsf{N}\mathsf{T})$.* [p. 10]

For example, 1-SS matrices illustrate the essence of this connection. The matrix $M = \text{1SS}(a)$ is defined by exactly $\mathsf{T} - 1$ parameters $a_{0:\mathsf{T}-1} = a_1, \ldots, a_{\mathsf{T}-1}$, and can be computed in $O(\mathsf{T})$ time by following the scalar recurrence (7).

## 3.4.1 The Linear (Recurrent) Mode

[p. 10] Proposition 3.6 can be easily seen in the case of diagonal structured SSMs (S4D (Gu, Gupta, et al. 2022)), simply by leveraging the state space model formulation (2) and unrolling the recurrence. The formal tensor-contraction algorithm is provided in (8), where the dimension S is equal to T (Footnote 4: A different symbol is required for the contraction notation).

$$Z = \text{contract}(\mathsf{SP}, \mathsf{SN} \to \mathsf{SPN})(X, B) \qquad (\mathsf{S}, \mathsf{P}, \mathsf{N}) \tag{8a}$$

$$H = \text{contract}(\mathsf{TSN}, \mathsf{SPN} \to \mathsf{TPN})(L, Z) \qquad (\mathsf{T}, \mathsf{P}, \mathsf{N}) \tag{8b}$$

$$Y = \text{contract}(\mathsf{TN}, \mathsf{TPN} \to \mathsf{TP})(C, H) \qquad (\mathsf{T}, \mathsf{P}) \tag{8c}$$

Here, $L \in \mathbb{R}^{(\mathsf{T},\mathsf{T})}$ is defined as $\text{1SS}(A)$, or in other words $L_{0:\mathsf{T},0:\mathsf{T}} = \text{1SS}(A_{0:\mathsf{T}})$ for $i \in [\mathsf{N}]$. This algorithm involves three steps corresponding to (2):

(i) *expanding* the input $X$ by the input matrix $B$ (8a),

(ii) *unrolling* independent scalar SSM recurrences (8b), and

(iii) *contracting* the hidden state $H$ by the output matrix $C$ (8c).

Note that the equivalence between scalar SSMs and 1-SS matrices is used in step (8b).

**Remark 3.** *We note that (8) is a special case of the Mamba (S6) model. however, a naive implementation is slow because of the expanded tensors $Z$ and $H$ of size* (T, P, N)*; Gu and Dao (2023) introduced a hardware-aware implementation to avoid materializing these tensors.* [p. 10]

Surprisingly, Theorem 3.5 and Proposition 3.6 immediately imply that all SSMs have the same asymptotic efficiency as algorithm (8).

**Theorem 3.7.** *Any state space model (Definition 2.2) of state size* N *on sequence length* T *can be computed in time $O(\mathsf{T}\mathsf{N})$ (not accounting for potential preprocessing).* [p. 10]

[p. 10-11] This result is noted as new to the structured SSM literature. In particular, given dense unstructured $A_t$ matrices, the total representation alone seems to be of size $O(\mathsf{T}\mathsf{N}^2)$. Thus Theorem 3.7 states the non-trivial result that with a preprocessing step, even an unstructured SSM can be computed optimally efficiently, with upper bound matching the lower bound $O(\mathsf{T}\mathsf{N})$ given by the size of $B$ and $C$.

**Remark 4.** *Theorem 3.7 is perhaps not too surprising in light of the fact that almost all dense matrices over $\mathbb{R}^{(\mathsf{N},\mathsf{N})}$ are diagonalizable over $\mathbb{C}$, leading to the result that almost all dense real SSMs are equivalent to a diagonal complex SSM. This fact underlies the reason why diagonal SSMs are the most popular form of structured SSM (Gu, Gupta, et al. 2022; Gupta, Gu, and Berant 2022; J. T. Smith, Warrington, and Linderman 2023). However, Theorem 3.7 implies the much stronger result for all real SSMs (not just the diagonalizable ones), as well as dense SSMs over other fields (including $\mathbb{C}$ itself).* [p. 10-11]

[p. 11] In practice, efficiently computable SSMs still require additional structure on $A$, particularly to avoid the expensive preprocessing step (which both has order N extra FLOPs and involves hardware-inefficient operations such as singular value decompositions). These structures are the focus of past work on structured SSMs (e.g. S4(D) and Mamba) as well as the new algorithms. In particular, when slightly stronger structure is imposed on $A$, very hardware-efficient algorithms through block decompositions of the SSM matrix $M = \text{SSS}(A, B, C)$ will be designed in Section 6.

## 3.4.2 The Quadratic (Naive) Mode

[p. 11] There is another way to compute an SSM exposed by the new matrix point of view. A naive computation of the matrix SSM representation (3) involves simply materializing the sequence transformation matrix $M = \text{SSS}(A, B, C)$. This is a $(\mathsf{T}, \mathsf{T})$ matrix, and therefore this naive algorithm will scale quadratically in sequence length. However, when the sequence length T is short, this can actually be more efficient than the linear algorithm due to constant factors and the hardware-friendliness of the computation pattern (e.g. leveraging matrix-matrix multiplications). In fact, for a particular case of structured SSMs, this looks very similar to a quadratic attention computation (Section 5).

## 3.4.3 Summary

[p. 11] Many sequence models are explicitly motivated or defined as matrix sequence transformations -- most notably Transformers, where the matrix mixer is the attention matrix. On the other hand, RNNs and SSMs have not previously been described in this way. By providing an explicit *matrix transformation* form of state space models, new ways of understanding and using them are revealed. From a computational perspective, any method of computing the forward pass of a state space model can be viewed as a matrix multiplication algorithm on semiseparable matrices. The semiseparable matrix perspective provides one lens into state space duality (SSD), where the dual modes respectively refer to a linear-time semiseparable matrix multiplication algorithm and quadratic-time naive matrix multiplication.

Moreover, leveraging the rich structure of semiseparable matrices can lead to even better algorithms and more insights (e.g. Section 6 and Appendix B). In Appendix C.1, some additional properties of semiseparable matrices are described.
