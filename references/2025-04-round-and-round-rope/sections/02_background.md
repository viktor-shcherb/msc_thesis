# Background [p. 2–3]

## Attention Mechanism Notation [p. 2]

We denote by xi ∈ ℝd the d-dimensional token embedding of the i-th token. Query and key vectors take the form qi = WQxi and ki = WKxi, respectively, given query and key matrices WQ, WK ∈ ℝd×d. The attention mechanism¹ performs the following computation:

```
αi,j = exp(ai,j) / Σj'∈i exp(ai,j'), with ai,j = k(qi, kj)
```
(1)

where k is a kernel function which in our work takes the form of either a simple dot product, i.e. No Positional Encoding (NoPE) (Haviv et al., 2022; Kazemnejad et al., 2024), or RoPE [p. 2–3].

We focus on the case in which the attention mechanism is of the most common type of attention used in LLMs today. In a causal mechanism, we have that αi,j = 0 when j > i and Σj:j≤i αi,j = 1. We also note that we assume ai,j to be finite, as it is always the case in practice, such that 0 < αi,j < 1, when j ≤ i. We call ai,j the 'activation' or 'logit', while we call αi,j the 'attention coefficient' between i and j. It is sometimes useful to view the attention coefficients in matrix-form, which in our specific case results in a lower triangular row-stochastic matrix [p. 3].

## Special Case: No Positional Encoding [p. 3]

We highlight an important special case for k which we call kNoPE, i.e. no positional encoding: kNoPE(qi, kj) = qi⊤kj, where qi⊤ denotes the transpose of qi. In other words, in NoPE the kernel function computes simply the dot product, without providing any positional information to the Transformer. It has been shown that Transformers can still perform well, especially out of distribution, with NoPE (Kazemnejad et al., 2024). In particular, Kazemnejad et al. (2024) prove that the Transformers could in principle recover absolute positional information through the causal mask; however, the proof relies on the universal approximation theorem, which we believe is a practical limitation [p. 3].

---

¹We ignore here the 1/√d scaling factor introduced by Vaswani et al. (2017) for ease of notation.
