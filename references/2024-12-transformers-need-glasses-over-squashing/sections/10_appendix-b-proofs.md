# Appendix B: Proofs [p. 13-16]

We provide formal statements and proofs for the results shown in the main text. We follow the order in which they are presented in the main text. In Section B.1, we present the proofs on representational collapse (Section 4), in Section B.2 the proofs on over-squashing (Section 5) over-squashing, and finally in Section B.3 the proofs on counting (Section 6).

## B.1 Representational Collapse [p. 13]

We start by showing that adding a new element to a sequence results in the softmax value of a specific token to decrease. In particular, we consider the case in which the tokens are bounded and show that we can use this to construct an upper bound on the softmax value for any token.

**Lemma B.1.** Consider a vector a ∈ ℝⁿ⁻¹ and two scalars b,c ∈ ℝ. Let x = [a c]ᵀ ∈ ℝⁿ and x* = [a b c]ᵀ ∈ ℝⁿ⁺¹ with all entries bounded. Then, softmax(x)ₙ > softmax(x*)ₙ₊₁. Moreover for any ε > 0 we can find large enough n ∈ ℕ₊ such that |softmax(x)ₙ - softmax(x*)ₙ₊₁| < ε.

**Proof.** We directly compute:

softmax(x)ₙ = exp(c) / (Σₖ₌₁ⁿ⁻¹ exp(aₖ) + exp(c))

softmax(x*)ₙ₊₁ = exp(c) / (Σₖ₌₁ⁿ⁻¹ exp(aₖ) + exp(b) + exp(c))

As we assume that the entries are bounded, we have that Σⱼ₌₁ⁿ⁻¹ exp(aⱼ) + exp(c) < Σⱼ₌₁ⁿ⁻¹ exp(aⱼ) + exp(b) + exp(c), therefore softmax(x)ₙ > softmax(x*)ₙ₊₁.

For the second part of the statement, we compute:

|softmax(x)ₙ - softmax(x*)ₙ₊₁| = |exp(c)/(Σₖ₌₁ⁿ⁻¹ exp(aₖ) + exp(c)) - exp(c)/(Σₖ₌₁ⁿ⁻¹ exp(aₖ) + exp(b) + exp(c))|

≤ |exp(c)/(Σₖ₌₁ⁿ⁻¹ exp(aₖ) + exp(c))| + |exp(c)/(Σₖ₌₁ⁿ⁻¹ exp(aₖ) + exp(b) + exp(c))|

< ε

for some ε > 0, as in the last step the summands tend to 0 as n → ∞. We therefore have that |softmax(x)ₙ - softmax(x*)ₙ₊₁| → 0 as n → ∞ and for large enough n |softmax(x)ₙ - softmax(x*)ₙ₊₁| < ε for any ε > 0 due to the previous statement.

### Total variation [p. 13]

We now study a quantity known as the total variation between two distributions of interest. Given two categorical distributions μ, ν supported on the same space, we define their total variation δ(μ,ν) — or equivalently L₁ norm ‖μ - ν‖₁, as:

**Equation (2):**
δ(μ,ν) = Σₓ |μ(x) - ν(x)|

[p. 13]

The total variation is a distance between probability distributions. We note that oftentimes the quantity above is strictly called the L₁ norm, while 1/2 of such a quantity the total variation. For the scope of our work, the factor of 1/2 is not important so we ignore it and use the two terms synonymously. Interestingly, the total variation is intimately related to the KL-divergence, pointing towards potential connections to information theory. We leave such a connection to future work.

**Lemma B.2.** Consider two sequences x, x* ∈ ℝⁿ such that limₙ→∞ |xₙ - x*ₙ| = 0, with xᵢ, x*ᵢ bounded. Let y, y* ∈ ℝⁿ be the softmax of x and x* respectively. Then, as n → ∞ the total variation tends to 0, i.e. limₙ→∞ δ(y,y*) = 0.

**Proof.** [p. 14] Let Z = Σᵢ₌₁ⁿ eˣⁱ and Z* = Σᵢ₌₁ⁿ eˣ*ⁱ be the partition functions for x and x*, respectively. We start by bounding the quantity |Z - Z*|. In particular, let ε > 0, we first claim:

**Equation (3):**
|Z - Z*| ≤ Σᵢ₌₁ⁿ |eˣⁱ - eˣ*ⁱ| ≤ ε min(Z, Z*)

[p. 14]

Consider some n₀ ≥ 1 such that |1 - eˣ*ⁱ⁻ˣⁱ| ≤ ε/2. We note that this always possible as |x*ᵢ - xᵢ| → 0 by assumption. We compute:

Σᵢ₌₁ⁿ |eˣⁱ - eˣ*ⁱ| = Σᵢ₌₁ⁿ⁰⁻¹ |eˣⁱ - eˣ*ⁱ| + Σᵢ₌ₙ₀ⁿ |eˣⁱ - eˣ*ⁱ|

= Σᵢ₌₁ⁿ⁰⁻¹ |eˣⁱ - eˣ*ⁱ| + Σᵢ₌ₙ₀ⁿ eˣⁱ |1 - eˣ*ⁱ⁻ˣⁱ|

≤ Σᵢ₌₁ⁿ⁰⁻¹ |eˣⁱ - eˣ*ⁱ| + (ε/2) Σᵢ₌ₙ₀ⁿ eˣⁱ

≤ Σᵢ₌₁ⁿ⁰⁻¹ |eˣⁱ - eˣ*ⁱ| + (ε/2)Z

≤ εZ

Where the last step comes from the observation that the first sum is fixed and Z is unbounded with n. Therefore, for n large enough, we can also bound the left summand by Zε/2. The same argument also holds when bounding with Z* instead of Z, leading to the claim in Equation 3.

We now proceed with the following computation:

[p. 15]

δ(y,y*) = Σᵢ₌₁ⁿ |eˣⁱ/Z - eˣ*ⁱ/Z*|

= Σᵢ₌₁ⁿ |Z*eˣⁱ - Zeˣ*ⁱ|/(ZZ*)

= Σᵢ₌₁ⁿ |Z*eˣⁱ - Zeˣⁱ + Zeˣⁱ - Zeˣ*ⁱ|/(ZZ*)

≤ Σᵢ₌₁ⁿ |Z*eˣⁱ - Zeˣⁱ|/(ZZ*) + |Zeˣⁱ - Zeˣ*ⁱ|/(ZZ*)

= Σᵢ₌₁ⁿ |Z* - Z|eˣⁱ/(ZZ*) + Z|eˣⁱ - eˣ*ⁱ|/(ZZ*)

= |Z* - Z|/(ZZ*) · Z + Σᵢ₌₁ⁿ |eˣⁱ - eˣ*ⁱ|/Z*

≤ ε min(Z,Z*)/Z* + ε min(Z,Z*)/Z*

≤ 2ε

which concludes the proof.

### Theorem B.3: Representational Collapse [p. 15]

We are now ready to show the main result on representational collapse. In particular, we show that given two sequences of length n and n+1 where the second sequence is the same as the first with a final repeated token, their representations become arbitrarily close. Importantly, we require that the information from the positional encodings decays to 0 as the distance grows between tokens. The final token repetition is important as otherwise the residual connection in the Transformer would not make the representations necessarily converge.

**Theorem B.3 (Representational Collapse).** Let x ∈ ℝⁿ⁻¹ˣᵈ be an underlying growing token sequence. Let v⁽⁰⁾ = [v vₐ]ᵀ ∈ ℝⁿˣᵈ and v*⁽⁰⁾ = [v vₐ vₐ]ᵀ ∈ ℝⁿ⁺¹ˣᵈ be two sequences for a final repeated token xₐ ∈ ℝᵈ, with all token representations bounded. Further, assume that the positional encodings decay with distance to 0. Then, for large enough n ∈ ℕ₊, we have that the representations are under any ε:

‖v⁽ᴸ⁾ₙ - v*⁽ᴸ⁾ₙ₊₁‖₁ < ε.

**Proof.** We note that since the sequences are identical up to the n-th element, it is sufficient to only check the representations of the final elements in both sequences. We therefore compare the n-th element of z⁽⁰⁾ with the n+1-th element of z*⁽⁰⁾:

‖z⁽⁰⁾ₙ - z*⁽⁰⁾ₙ₊₁‖₁ = ‖Σᵢ<ₙ α⁽⁰⁾ₙ,ᵢ v⁽⁰⁾ᵢ + α⁽⁰⁾ₙ,ₙ v⁽⁰⁾ₐ - (Σᵢ<ₙ α*⁽⁰⁾ₙ₊₁,ᵢ v⁽⁰⁾ᵢ + (α*⁽⁰⁾ₙ₊₁,ₙ + α*⁽⁰⁾ₙ₊₁,ₙ₊₁) v⁽⁰⁾ₐ)‖₁

= ‖Σᵢ<ₙ (α⁽⁰⁾ₙ,ᵢ - α*⁽⁰⁾ₙ₊₁,ᵢ) v⁽⁰⁾ᵢ + (α⁽⁰⁾ₙ,ₙ - α*⁽⁰⁾ₙ₊₁,ₙ - α*⁽⁰⁾ₙ₊₁,ₙ₊₁) v⁽⁰⁾ₐ‖₁

≤ Σᵢ<ₙ |α⁽⁰⁾ₙ,ᵢ - α*⁽⁰⁾ₙ₊₁,ᵢ| + |α⁽⁰⁾ₙ,ₙ - α*⁽⁰⁾ₙ₊₁,ₙ - α*⁽⁰⁾ₙ₊₁,ₙ₊₁|

≤ Σᵢ<ₙ |α⁽⁰⁾ₙ,ᵢ - α*⁽⁰⁾ₙ₊₁,ᵢ| + |α⁽⁰⁾ₙ,ₙ - α*⁽⁰⁾ₙ₊₁,ₙ| + |α*⁽⁰⁾ₙ₊₁,ₙ₊₁|

= δ(α⁽⁰⁾ₙ,₍:₎, α*⁽⁰⁾ₙ,₍:₎ₙ) + α*⁽⁰⁾ₙ₊₁,ₙ₊₁ < ε

[p. 16] We assume for simplicity that the values are unit norm. This is not crucial as otherwise one would equivalently just need to consider additional constant factors as we assume the token representations are bounded. We note that the term δ(α⁽⁰⁾ₙ,₍:₎, α*⁽⁰⁾ₙ,₍:₎ₙ) goes to 0 with n → ∞ thanks to Lemma B.2 and our assumptions on the positional encodings. Similarly, the term α*⁽⁰⁾ₙ₊₁,ₙ₊₁ goes to 0 due to Lemma B.1. We have also used the fact that v⁽⁰⁾ₙ = v*⁽⁰⁾ₙ₊₁ by construction to ignore the residual connection. As v⁽ℓ⁺¹⁾ᵢ = ψ⁽ℓ⁾(norm⁽ℓ⁾₂(z⁽ℓ⁾ᵢ)) + v⁽ℓ⁾ᵢ, the sequences will have arbitrarily close final token representations when entering the next layer. The result then follows via a simple inductive approach on the layers.

### Proposition B.4: Negative decay result [p. 16]

We also highlight a negative decay result which highlights why the assumption on the positional encodings is important. In particular, we show that given two sequences x = (1 0 1 0...) and x* = (0 1 0 1...), the total variation of the softmax does not decay to 0. This implies that there may be solutions to representational collapse depending on how the positional encodings are chosen.

**Proposition B.4.** Consider two sequences x = (1 0 1 0...) ∈ ℝⁿ and x* = (0 1 0 1...) ∈ ℝⁿ for n even. Let y and y* be the softmax of x and x*, respectively. Then the total variation δ(y,y*) does not tend to 0 as n → ∞.

**Proof.** Let Z = Σᵢ₌₁ⁿ eˣⁱ and Z* = Σᵢ₌₁ⁿ eˣ*ⁱ be the partition functions for x and x*, respectively. We directly compute:

limₙ→∞ δ(y,y*) = limₙ→∞ Σᵢ₌₁ⁿ |yᵢ/Z - y*ᵢ/Z*|

= limₙ→∞ Σᵢ₌₁ⁿ |yᵢ/(n/2·e + n/2) - y*ᵢ/(n/2·e + n/2)|

= limₙ→∞ Σᵢ₌₁ⁿ |(e-1)/(n/2·e + n/2)|

= limₙ→∞ n(e-1)/(ne+1)/2

= 2(e-1)/(e+1) > 0.

## B.2 Over-squashing [p. 16]

We now present our results on over-squashing. In our derivations, we assume that the attention coefficients are independent of the values and that we can summarise the effect of the layer norms via a constant factor. These assumptions are not necessary for the same derivation process to hold, but they greatly simplify the obtained bound and help more clearly point out the main takeaways.

**Theorem B.5 (Over-squashing in Transformers).** Consider an input sequence v⁽⁰⁾₁,...,v⁽⁰⁾ₙ (including CoT). Let σ_ψ be the maximal Lipschitz constant of any ψ⁽ℓ⁾, and ᾱ⁽ℓ⁾ⱼ,ᵢ = 1/β⁽ℓ⁾(α⁽ℓ⁾ⱼ,ᵢ + δⱼ,ᵢ) the normalized attention coefficient, then:

**Equation (4):**
‖∂yₙ/∂v⁽⁰⁾ᵢ‖ ≤ σᴸ_ψ Σₖ₁≥ᵢ ... Σₖₗ≥ₖₗ₋₁ ᾱ⁽ᴸ⁻¹⁾ₙ,ₖₗ ∏ℓ₌₂ᴸ⁻¹ ᾱ⁽ℓ⁻¹⁾ₖℓ,ₖℓ₋₁ ᾱ⁽⁰⁾ₖ₁,ᵢ

[p. 16]

**Proof.** Note that for j ≥ i we have:

[proof continues beyond page 16]

---
[p. 16–19 continued]

‖∂v⁽ℓ⁺¹⁾ⱼ/∂v⁽ℓ⁾ᵢ‖ = ‖∂/∂v⁽ℓ⁾ⱼ [ψ⁽ℓ⁾(norm⁽ℓ⁾₂(z⁽ℓ⁾ⱼ)) + z⁽ℓ⁾ⱼ]‖

≤ (σ_ψ⁽ℓ⁾/β⁽ℓ⁾₂ + 1) ∂z⁽ℓ⁾ⱼ/∂v⁽ℓ⁾ᵢ

= (σ_ψ⁽ℓ⁾/β⁽ℓ⁾₂ + 1) ∂/∂v⁽ℓ⁾ᵢ [Σⱼ≤ᵢ α⁽ℓ⁾ᵢⱼ norm⁽ℓ⁾₁(v⁽ℓ⁾ᵢ) + v⁽ℓ⁾ᵢ]

= (σ_ψ⁽ℓ⁾/β⁽ℓ⁾₂ + 1) (α⁽ℓ⁾ⱼ,ᵢ/β⁽ℓ⁾₁ + δⱼ,ᵢ)

where we let β⁽ℓ⁾ᵢ represent the effect of layer normalization i at the ℓ-th layer and σ_ψ⁽ℓ⁾ the Lipschitz constant of ψ⁽ℓ⁾. For the case when j < i due to the causal mechanism we have that ∂v⁽ℓ⁾ⱼ/∂v⁽ℓ⁻¹⁾ᵢ = 0. We compute the following bound:

‖∂yₙ/∂v⁽⁰⁾ᵢ‖ = ‖1/β₃ Σₖ₁...Σₖₗ ∂v⁽ᴸ⁾ₙ/∂v⁽ᴸ⁻¹⁾ₖₗ ∏ℓ₌₂ᴸ⁻¹ ∂v⁽ℓ⁾ₖₗ/∂v⁽ℓ⁻¹⁾ₖₗ₋₁ ∂v⁽¹⁾ₖ₁/∂v⁽⁰⁾ᵢ‖

= ‖1/β₃ Σₖ₁≥ᵢ...Σₖₗ≥ₖₗ₋₁ ∂v⁽ᴸ⁾ₙ/∂v⁽ᴸ⁻¹⁾ₖₗ ∏ℓ₌₂ᴸ⁻¹ ∂v⁽ℓ⁾ₖₗ/∂v⁽ℓ⁻¹⁾ₖₗ₋₁ ∂v⁽¹⁾ₖ₁/∂v⁽⁰⁾ᵢ‖

≤ 1/β₃ ∏ℓ₌₁ᴸ (σ_ψ/β⁽ℓ⁾₂ + 1) Σₖ₁≥ᵢ...Σₖₗ≥ₖₗ₋₁ ᾱ⁽ᴸ⁻¹⁾ₙ,ₖₗ ∏ℓ₌₂ᴸ⁻¹ ᾱ⁽ℓ⁻¹⁾ₖₗ,ₖₗ₋₁ ᾱ⁽⁰⁾ₖ₁,ᵢ

= C Σₖ₁≥ᵢ...Σₖₗ≥ₖₗ₋₁ ᾱ⁽ᴸ⁻¹⁾ₙ,ₖₗ ∏ℓ₌₂ᴸ⁻¹ ᾱ⁽ℓ⁻¹⁾ₖₗ,ₖₗ₋₁ ᾱ⁽⁰⁾ₖ₁,ᵢ

where we let ᾱ⁽ℓ⁾ⱼ,ᵢ = α⁽ℓ⁾ⱼ,ᵢ/β⁽ℓ⁾₁ + δⱼ,ᵢ and C = 1/β₃ ∏ℓ₌₁ᴸ (σ_ψ/β⁽ℓ⁾₂ + 1).

[p. 17] We note that in this derivation, we use simplifying assumptions on the layer norms and attention coefficients, more specifically we assume that they are independent of the vᵢs. Of course, there is nothing stopping us from avoiding such assumptions and pushing the partial derivatives inside these components as well. The drawback is that this would add a great deal of additional complexity to the result and potentially distract from what we believe are the two key takeaways: (1) the position of the token matters, and (2) the attention coefficients matter.

### Connection to the spectral theory of Markov chains [p. 17]

We now show some results on the spectral theory of matrices which relate to causal attention mechanisms. We emphasize that in this work, we view causal attention mechanisms as triangular row-stochastic matrices. We show that these matrices have interesting spectral properties.

**Lemma B.6.** A row-stochastic triangular matrix A has 1 as its largest eigenvalue. Moreover, such eigenvalue has multiplicity 1 if each row except the first has at least 2 non-zero entries.

**Proof.** We start by showing that A cannot have eigenvalues λ > 1. We then provide an eigenvector with eigenvalue 1. We finally show that such an eigenvector is unique if each row has at least 2 non-zero entries.

Assume λ > 1 for some eigenvector φ, we then have that Aφ = λφ. Consider φᵢ = maxₖ φₖ > 0. Now (Aφ)ᵢ = Σⱼ≤ᵢ Aᵢⱼφⱼ = λφᵢ. As the sum is a convex combination, the result cannot be larger than the already maximal element φᵢ. As λ > 1, we however have that λφᵢ > φᵢ which is a contradiction and we conclude that λ ≤ 1.

[p. 18] It is easy to find an eigenvector that always has eigenvalue 1. Consider a vector x which is a constant vector of 1s. Then (Ax)ᵢ = Σⱼ≤ᵢ Aᵢⱼ = xᵢ, therefore x is an eigenvector with eigenvalue 1.

Finally, we show that when each row is non-zero, the only eigenvector is the constant-valued eigenvector. Consider the largest entry yᵢ > 0, then we have that (Ay)ᵢ = Σⱼ≤ᵢ Aᵢⱼyⱼ = yᵢ. Again, as this defines a convex combination, we must have that all tokens that i points to (i.e. the non-zero entries) are also equal to yᵢ. The condition that each row has at least two non-zero entries is important as it means that the condition yᵢ = yⱼ is true for all tokens.

**Lemma B.7.** The product of two row-stochastic matrices is again row-stochastic. Moreover, the product of two triangular row-stochastic matrices is a triangular row-stochastic matrix.

**Proof.** Let A, B ∈ ℝⁿˣⁿ be two row-stochastic matrices. We compute:

Σⱼ (AB)ᵢⱼ = Σⱼ Σₖ AᵢₖBₖⱼ = Σₖ Aᵢₖ Σⱼ Bₖⱼ = 1

The final statement follows immediately from the fact that the product of two triangular matrices is triangular.

We now show that under specific conditions, our over-squashing bound converges to a steady state in which the final token yₙ only depends on the initial input token v⁽⁰⁾₁ as the number layers tends to infinity, i.e. L → ∞.

**Proposition B.8.** Let β⁽ℓ⁾₁, β⁽ℓ⁾₂ = 1, β₃¹/ᴸ = 4, σ_ψ = 1. Furthermore, for simplicity, let the attention coefficients be equal at each layer and such that each row except the first of the causal mechanism has at least two non-zero elements. Then, we have as L → ∞ that ∂yₙ/∂v⁽⁰⁾ᵢ = 0 when i ≠ 1 and ∂yₙ/∂v⁽⁰⁾ᵢ = 1 when i = 1. In other words, yₙ will only be sensitive to the first token.

**Proof.** Let the associated attention matrix be Λ. We start by re-writing the following:

‖∂yₙ/∂v⁽⁰⁾ᵢ‖ ≤ 1/β₃ ∏ℓ₌₁ᴸ (σ_ψ/β₂ + 1) Σₖ₁≥ᵢ...Σₖₗ≥ₖₗ₋₁ ᾱ⁽ᴸ⁻¹⁾ₙ,ₖₗ ∏ℓ₌₂ᴸ⁻¹ ᾱ⁽ℓ⁻¹⁾ₖₗ,ₖₗ₋₁ ᾱ⁽⁰⁾ₖ₁,ᵢ

= (∏ℓ₌₁ᴸ [1/β₃¹/ᴸ (σ_ψ/β₂ + 1) (1/β₁ Λ + I)])ₙ,ᵢ

= ([1/2(Λ + I)]ᴸ)ₙ,ᵢ

We now point out that Λ̃ = 1/2(Λ + I) is row-stochastic and with our assumptions is diagonalizable into Λ̃ = ΨΣΦ. In particular, by Lemma B.7, also Λ̃ᴸ is row-stochastic and each entry is non-negative. We now use the Perron-Frobenius theorem for non-negative matrices [23], which guarantees us that all eigenvalues λₖ of Λ̃ are bounded such that |λₖ| ≤ 1. In particular, thanks to Lemma B.6, we know that there is a unique eigenvector (the constant eigenvector ψₙ) with eigenvalue λₙ = 1. Denote the left eigenvectors by ψₖ and the right eigenvectors φₙ, we therefore have:

limₗ→∞ Λ̃ᴸ = Σₖ λₖᴸ ψₖφₖᵀ = ψₙφₙᵀ.

In particular, one can check that φₙᵀ = [1 0...0], meaning that ψₙφₙᵀ has as first column a constant vector of 1s and every other entry 0. This completes the proof.

## B.3 Counting [p. 19]

We finally show in this section our final results that apply specifically to counting tasks. We start by highlighting a potential difficulty that the softmax layer encounters when counting, namely that the normalisation used makes it hard for it to preserve a notion of magnitude present in the sequence.

**Proposition B.9.** A Transformer without positional encodings and a causal attention mechanism is immediately unable to solve the counting problem.

**Proof.** We show this statement by demonstrating that the only information preserved about the 'count' by the attention mechanism will be the ratio of the elements present in a sequence. In particular, sequences with the same ratio of tokens will be assigned the exact same representation — this applies as we specifically study an attention mechanism without positional encodings and causal masking. Of course, having the same ratio of elements does not mean that the count will be the same, for instance the sequences '10' and '1100' have the same ratio of digits but clearly different counts.

Consider a sequence of two values, v⁽⁰⁾_zero and v⁽⁰⁾_one, with n₀ and n₁ being the number of zeros and ones respectively. We ignore in our calculations the MLPs ψ and the normalizations norm as these don't affect the argument. As this specific attention mechanism is permutation equivariant, the initial zero tokens will all be mapped to:

z⁽¹⁾_zero = Σⱼ exp(q⁽⁰⁾ᵀ_zero k⁽⁰⁾ⱼ) / Σ_w exp(q⁽⁰⁾ᵀ_zero k⁽⁰⁾_w) v⁽⁰⁾ⱼ + v⁽⁰⁾_zero

= n₀ exp(q⁽⁰⁾ᵀ_zero k⁽⁰⁾_zero) / [n₀ exp(q⁽⁰⁾ᵀ_zero k⁽⁰⁾_zero) + n₁ exp(q⁽⁰⁾ᵀ_zero k⁽⁰⁾_one)] v⁽⁰⁾_zero 
  + n₁ exp(q⁽⁰⁾ᵀ_zero k⁽⁰⁾_one) / [n₀ exp(q⁽⁰⁾ᵀ_zero k⁽⁰⁾_zero) + n₁ exp(q⁽⁰⁾ᵀ_zero k⁽⁰⁾_one)] v⁽⁰⁾_one + v⁽⁰⁾_zero

= exp(q⁽⁰⁾ᵀ_zero k⁽⁰⁾_zero) / [exp(q⁽⁰⁾ᵀ_zero k⁽⁰⁾_zero) + (n₁/n₀) exp(q⁽⁰⁾ᵀ_zero k⁽⁰⁾_one)] v⁽⁰⁾_zero 
  + exp(q⁽⁰⁾ᵀ_zero k⁽⁰⁾_one) / [(n₀/n₁) exp(q⁽⁰⁾ᵀ_zero k⁽⁰⁾_zero) + exp(q⁽⁰⁾ᵀ_zero k⁽⁰⁾_one)] v⁽⁰⁾_one + v⁽⁰⁾_zero

Similarly, the ones will be mapped to:

z⁽¹⁾_one = Σⱼ exp(q⁽⁰⁾ᵀ_one k⁽⁰⁾ⱼ) / Σ_w exp(q⁽⁰⁾ᵀ_one k⁽⁰⁾_w) v⁽⁰⁾ⱼ + v⁽⁰⁾_one

= n₀ exp(q⁽⁰⁾ᵀ_one k⁽⁰⁾_zero) / [n₀ exp(q⁽⁰⁾ᵀ_one k⁽⁰⁾_zero) + n₁ exp(q⁽⁰⁾ᵀ_one k⁽⁰⁾_one)] v⁽⁰⁾_zero 
  + n₁ exp(q⁽⁰⁾ᵀ_one k⁽⁰⁾_one) / [n₀ exp(q⁽⁰⁾ᵀ_one k⁽⁰⁾_zero) + n₁ exp(q⁽⁰⁾ᵀ_one k⁽⁰⁾_one)] v⁽⁰⁾_one + v⁽⁰⁾_one

= exp(q⁽⁰⁾ᵀ_one k⁽⁰⁾_zero) / [exp(q⁽⁰⁾ᵀ_one k⁽⁰⁾_zero) + (n₁/n₀) exp(q⁽⁰⁾ᵀ_one k⁽⁰⁾_one)] v⁽⁰⁾_zero 
  + exp(q⁽⁰⁾ᵀ_one k⁽⁰⁾_one) / [(n₀/n₁) exp(q⁽⁰⁾ᵀ_zero k⁽⁰⁾_zero) + exp(q⁽⁰⁾ᵀ_one k⁽⁰⁾_one)] v⁽⁰⁾_one + v⁽⁰⁾_one

[p. 20] Assuming that z⁽¹⁾_zero ≠ z⁽¹⁾_one (to avoid the trivial case), we notice that the attention mechanism alongside the MLP ψ define an isomorphism between sequences at different layers, updating all zeros and ones to a different value vector. The critical fact is that the representations only depend on the ratio between n₀ and n₁, meaning that sequences of different lengths (therefore different counts) will have the exact same representation. This is respected at each layer, meaning that the LLM after L layers will assign the same representation to different sequences as long as they have the same ratio. This points to a loss of representation for the counting problem.

**Corollary B.10.** Consider a task in which the goal is to count how many vₐ tokens there are in the sequence. Let v⁽⁰⁾ = [v vₐs]ᵀ ∈ ℝⁿˣᵈ and v*⁽⁰⁾ = [v vₐ vₐs]ᵀ ∈ ℝ⁽ⁿ⁺¹⁾ˣᵈ. Due to representational collapse, at least one sequence will be given the wrong count for large enough finite n.

**Proof.** This statement is a direct consequence of representational collapse. In particular, as yₙ and y*ₙ will be indistinguishable for large enough n, the Transformer will be forced to make a mistake for at least one of them. This points to an impossibility result of counting on certain sequences due to floating point error. This holds regardless of the positional encodings used (as long as they satisfy the required decay conditions) and causal mechanism.
