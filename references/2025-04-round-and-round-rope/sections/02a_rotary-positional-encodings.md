# 2.1 Rotary Positional Encodings (RoPE) [p. 3]

## RoPE Structure and Notation

For simplicity of notation in this work we assume that query are key vectors are d-dimensional, with d ⩾ 2 being an even number. We decompose queries and keys into 2-dimensional chunks qi = ⊕k=1...d/2 qi(k,k+1) = ⊕k=1...d/2 qi(k), where ⊕ denotes direct sum (concatenation). In other words, we denote by qi(k) ∈ ℝ² the k-th 2-dimensional chunk of the query vector of the i-th token, using analogous notation for the key vector [p. 3].

## Rotation Matrices and Frequencies

RoPE considers a sequence of angles G = (gk = θ^(-2(k-1)/d) : k = 1,..., d/2)², where g1 = 1 is the fastest rotating component at 1 radian per token and gd/2 = θ^(-(d-2)/d) ≈ θ^(-1) the slowest rotating component at approximately 1/θ rotations per token. The parameter θ is called the base wavelength, which by default is 10,000 (Su et al., 2024), although works have explored increasing it to, for instance, 500,000 (Xiong et al., 2023; Roziere et al., 2023; Dubey et al., 2024). We denote by ρ(gk) the matrix form of gk [p. 3]:

```
ρ(gk) = [cos(gk)  -sin(gk)]
        [sin(gk)   cos(gk)]
```
(2)

highlighting that ρ(gk) is a 2-dimensional orthogonal transformation (rotation). One can view ρ(gk) as a "unit rotation" by gk radians [p. 3].

## Block-Diagonal Matrix Construction

The RoPE technique amounts to the construction of a block-diagonal matrix R^i = ⊕k=1...d/2 ρ(gk), where each 2 × 2 block on the diagonal is a rotation by a different frequency of RoPE. The R^i denotes in fact matrix exponentiation by an integer i which is the position of xi³. We can exploit a nice property of rotation matrices, i.e. that ρ(gk)^i = ρ(igk) to avoid the computational cost of the matrix power. As this matrix is block diagonal, computing R·qi means that the rotations act only on 2-dimensional chunks of the query (or key), i.e. R·qi = ⊕k=1...d/2 ρ(igk)qi(k) [p. 3].

## RoPE Kernel Function

This leads to the RoPE kernel [p. 3]:

```
kRoPE(qi, kj) = (R^i qi)^⊤(R^j kj) = qi^⊤ R^j-i kj = Σ(k=1...d/2) (qi(k))^⊤ ρ(gk)^j-i kj(k)
```
(3)

where we use the fact that (ρ(gk)^i)^⊤ρ(gk)^j = ρ(gk)^-i ρ(gk)^j = ρ(gk)^j-i. We highlight how the block diagonal structure of R allows one to decompose the dot product into the sum of dot products of 2-dimensional chunks, with each key vector chunk rotated at a frequency dictated by gk [p. 3].

---

²We denote the angles gk instead of θk as we opt for more of a group theoretic perspective of RoPE.

³For clarity, i and j have nothing to do with √-1, but instead denote the positions i and j of the tokens in the sequence.
