# Appendix G: Gradient Flow of DIFF Transformer [p. 20-21]

They show that the gradient flow in differential attention is similar to that of conventional softmax attention [p. 20]. With this property, the same hyperparameters used in Transformer can be applied directly to the corresponding DIFF Transformer without concerns about training instability [p. 20].

For differential attention, they select a single head in the proof and expand Equation (1) and Equation (3) as follows [p. 20]. They have X ∈ ℝ^(N×d_model) as the input, Q₁, Q₂, K₁, K₂ ∈ ℝ^(N×d), V ∈ ℝ^(N×2d), and O ∈ ℝ^(N×d_model) as the output [p. 20]:

```
[Q₁; Q₂] = [XW^Q₁; XW^Q₂],   [K₁; K₂] = [XW^K₁; XW^K₂],   V = XW^V

A₁ = softmax(Q₁K₁ᵀ/√d),   A₂ = softmax(Q₂K₂ᵀ/√d)                    (6)

O = GroupNorm((A₁ - λA₂)V)W^O
```

where W^Q₁, W^Q₂, W^K₁, W^K₂ ∈ ℝ^(d_model×d), W^V ∈ ℝ^(d_model×2d), W^O ∈ ℝ^(2d×d_model) are parameters, λ is a learnable scalar, and GroupNorm has a fixed multiplier as scale: γ = 1 - λ_init [p. 20]. For a token x in (A₁ - λA₂)V, they have ∂GN(x)/∂x = Θ(||x||₂/||x||₂) = Θ(1) as √(2d/√2d) = Θ(1 - λ_init) at the early training stage [p. 20]. With this formulation and given the gradient of O as ∂L/∂O, they formulate gradients of parameters as [p. 20]:

```
∂L/∂W^O = ∂L/∂O ∂O/∂W^O
        = ((A₁ - λA₂)V)ᵀ ∂L/∂O

∂L/∂W^V = ∂L/∂O∂V ∂V/∂W^V
        = Xᵀ(A₁ - λA₂)ᵀ ∂L/∂O (W^O)ᵀ

∂L/∂W^Q₁ = ∂L/∂O ∂O/∂A₁ ∂Q₁/∂W^Q₁
         = 1/√d Xᵀ[A₁ ⊙ (∂L/∂O (W^O)ᵀVᵀ - (A₁ ⊙ ∂L/∂O (W^O)ᵀVᵀ)J)]K₁
                                                                          (7)
∂L/∂W^Q₂ = ∂L/∂O ∂O/∂A₂ ∂Q₂/∂W^Q₂
         = -λ/√d Xᵀ[A₂ ⊙ (∂L/∂O (W^O)ᵀVᵀ - (A₂ ⊙ ∂L/∂O (W^O)ᵀVᵀ)J)]K₂

∂L/∂W^K₁ = ∂L/∂O ∂O/∂A₁ ∂K₁/∂W^K₁
         = 1/√d Xᵀ[A₁ ⊙ (∂L/∂O (W^O)ᵀVᵀ - (A₁ ⊙ ∂L/∂O (W^O)ᵀVᵀ)J)]ᵀQ₁

∂L/∂W^K₂ = ∂L/∂O ∂O/∂A₂ ∂K₂/∂W^K₂
         = -λ/√d Xᵀ[A₂ ⊙ (∂L/∂O (W^O)ᵀVᵀ - (A₂ ⊙ ∂L/∂O (W^O)ᵀVᵀ)J)]ᵀQ₂
```

where J ∈ ℝ^(N×N) is an all-one matrix [p. 20].

---
[p. 21 continued]

As a comparison, they reformulate conventional softmax attention [p. 21]. For attention with 2d dimension, they have X ∈ ℝ^(N×d_model) as the input, Q₁, Q₂, K₁, K₂ ∈ ℝ^(N×d), V ∈ ℝ^(N×2d), and O ∈ ℝ^(N×d_model) as the output [p. 21]:

```
[Q₁; Q₂] = [XW^Q₁; XW^Q₂],   [K₁; K₂] = [XW^K₁; XW^K₂],   V = XW^V

A = softmax((Q₁K₁ᵀ + Q₂K₂ᵀ)/√(2d))                                    (8)

O = (AV)W^O
```

where W^Q₁, W^Q₂, W^K₁, W^K₂ ∈ ℝ^(d_model×d), W^V ∈ ℝ^(d_model×2d), W^O ∈ ℝ^(2d×d_model) are parameters [p. 21]. Denote the gradient of O as ∂L/∂O, they formulate gradients of parameters via [p. 21]:

```
∂L/∂W^O = ∂L/∂O ∂O/∂W^O
        = (AV)ᵀ ∂L/∂O

∂L/∂W^V = ∂L/∂O∂V ∂V/∂W^V
        = XᵀAᵀ ∂L/∂O (W^O)ᵀ

∂L/∂W^Q₁ = ∂L/∂O ∂O/∂A ∂Q₁/∂W^Q₁
         = 1/√(2d) Xᵀ[A ⊙ (∂L/∂O (W^O)ᵀVᵀ - (A ⊙ ∂L/∂O (W^O)ᵀVᵀ)J)]K₁
                                                                          (9)
∂L/∂W^Q₂ = ∂L/∂O ∂O/∂A ∂Q₂/∂W^Q₂
         = 1/√(2d) Xᵀ[A ⊙ (∂L/∂O (W^O)ᵀVᵀ - (A ⊙ ∂L/∂O (W^O)ᵀVᵀ)J)]K₂

∂L/∂W^K₁ = ∂L/∂O ∂O/∂A ∂K₁/∂W^K₁
         = 1/√(2d) Xᵀ[A ⊙ (∂L/∂O (W^O)ᵀVᵀ - (A ⊙ ∂L/∂O (W^O)ᵀVᵀ)J)]ᵀQ₁

∂L/∂W^K₂ = ∂L/∂O ∂O/∂A ∂K₂/∂W^K₂
         = 1/√(2d) Xᵀ[A ⊙ (∂L/∂O (W^O)ᵀVᵀ - (A ⊙ ∂L/∂O (W^O)ᵀVᵀ)J)]ᵀQ₂
```

With the property of softmax, they have A ≐ A₁ ≐ A₂ ≐ A₁ − λA₂, considering gradient magnitude [p. 21]. Therefore, the gradients of the corresponding parameters of attention and differential attention are equivalent in magnitude, differing by some constant factors, as shown in Equation (7) and Equation (9) [p. 21]. When using an optimizer that is invariant to gradient magnitude, such as AdamW (Loshchilov & Hutter, 2019), parameter updates in DIFF Transformer are similar to those of Transformer [p. 21]. This allows them to reuse Transformer hyperparameters without risking training instability [p. 21].
