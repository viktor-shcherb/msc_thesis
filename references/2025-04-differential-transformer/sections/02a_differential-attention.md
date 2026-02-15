# 2.1 Differential Attention [p. 2–3]

## Core Mechanism [p. 2]

The differential attention mechanism maps query, key, and value vectors to outputs [p. 2]. The authors use query and key vectors to compute attention scores, and then compute a weighted sum of value vectors [p. 2].

The critical design is that they use a pair of softmax functions to cancel the noise of attention scores [p. 2]. Specifically, given input X ∈ ℝᴺˣᵈᵐᵒᵈᵉˡ, they first project them to query, key, and value Q₁, Q₂, K₁, K₂ ∈ ℝᴺˣᵈ, V ∈ ℝᴺˣ²ᵈ [p. 2]. Then the differential attention operator DiffAttn(·) computes outputs via:

$$[Q_1; Q_2] = XW^Q, \quad [K_1; K_2] = XW^K, \quad V = XW^V$$

$$\text{DiffAttn}(X) = (\text{softmax}(\frac{Q_1 K_1^T}{\sqrt{d}}) - \lambda \text{softmax}(\frac{Q_2 K_2^T}{\sqrt{d}}))V$$

(Equation 1)

where W^Q, W^K, W^V ∈ ℝᵈᵐᵒᵈᵉˡˣ²ᵈ are parameters, and λ is a learnable scalar [p. 2].

## Scalar λ Re-parameterization [p. 2]

In order to synchronize the learning dynamics, the authors re-parameterize the scalar λ as:

$$\lambda = \exp(\lambda_{q_1} \cdot \lambda_{k_1}) - \exp(\lambda_{q_2} \cdot \lambda_{k_2}) + \lambda_{\text{init}}$$

(Equation 2)

where λ_{q₁}, λ_{k₁}, λ_{q₂}, λ_{k₂} ∈ ℝᵈ are learnable vectors, and λᵢₙᵢₜ ∈ (0, 1) is a constant used for the initialization of λ [p. 2]. The authors empirically find that the setting λᵢₙᵢₜ = 0.8 − 0.6 × exp(−0.3 ⋅ (l − 1)) works well in practice, where l ∈ [1, L] represents layer index [p. 3]. It is used as the default strategy in their experiments [p. 3].

The authors also explore using the same λᵢₙᵢₜ (e.g., 0.8) for all layers as another initialization strategy [p. 3]. As shown in the ablation studies (Section 3.8), the performance is relatively robust to different initialization strategies [p. 3].

## Analogy to Differential Amplifiers [p. 3]

Differential attention takes the difference between two softmax attention functions to eliminate attention noise [p. 3]. The idea is analogous to differential amplifiers (Laplante et al., 2018) proposed in electrical engineering, where the difference between two signals is used as output, so that we can null out the common-mode noise of the input [p. 3]. Naderi et al. (2024) also prove that differential attention makes the spectral distribution of attention matrices more balanced, which effectively resolves rank collapse [p. 3].

In addition, the design of noise-canceling headphones is based on a similar idea [p. 3]. The authors can directly reuse FlashAttention (Dao et al., 2022) as described in Appendix A, which significantly improves model efficiency [p. 3].

## Multi-Head Differential Attention [p. 3]

The authors also use the multi-head mechanism (Vaswani et al., 2017) in Differential Transformer [p. 3]. Let h denote the number of attention heads [p. 3]. They use different projection matrices W_i^Q, W_i^K, W_i^V, i ∈ [1, h] for the heads [p. 3]. The scalar λ is shared between heads within the same layer [p. 3]. Then the head outputs are normalized and projected to outputs as follows:

$$\text{head}_i = \text{DiffAttn}(X; W_i^Q, W_i^K, W_i^V, \lambda)$$

$$\widehat{\text{head}}_i = (1 - \lambda_{\text{init}}) \cdot \text{LN}(\text{head}_i)$$

$$\text{MultiHead}(X) = \text{Concat}(\widehat{\text{head}}_1, \cdots, \widehat{\text{head}}_h)W^O$$

(Equation 3)

where λᵢₙᵢₜ is the constant scalar in Equation (2), W^O ∈ ℝᵈᵐᵒᵈᵉˡˣᵈᵐᵒᵈᵉˡ is a learnable projection matrix, LN(·) uses RMSNorm (Zhang & Sennrich, 2019) as in Transformer [p. 3], and Concat(·) concatenates the heads together along the channel dimension [p. 3].

The authors use a fixed multiplier (1 − λᵢₙᵢₜ) as the scale of LN(·) to align the gradients with Transformer [p. 3]. Appendix G proves that the overall gradient flow remains similar to that of Transformer [p. 3]. The nice gradient property allows DIFF to directly inherit similar hyperparameters and ensures training stability [p. 3]. They set the number of heads h = dₘₒdₑₗ/2d, where d is equal to the head dimension of Transformer [p. 3]. So the parameter counts and computational complexity remain the same [p. 3].

## Headwise Normalization [p. 3]

Figure 2 uses GroupNorm(·) (Wu & He, 2018) to emphasize that LN(·) is applied to each head independently [p. 3]. As differential attention tends to have a sparser pattern, statistical information is more diverse between heads [p. 3]. The LN(·) operator normalizes each head before concatenation to improve gradient statistics (Wang et al., 2023; Qin et al., 2022) [p. 3].

**Figure 2** (p. 3): "Multi-head differential attention. Each head takes the difference between two softmax attention maps to cancel out attention noise. λ is a learnable scalar that is initialized to λᵢₙᵢₜ. GroupNorm applies normalization to each head independently. A fixed multiplier (1 − λᵢₙᵢₜ) is used after GroupNorm, which aligns the gradient flow with Transformer. The code implementation is available at https://aka.ms/Diff-Transformer."

Description: Architecture diagram with accompanying pseudocode
- Left side: Shows the computational flow with boxes and arrows
  - Input X at bottom
  - Three parallel Linear layers producing Q₁, Q₂, K₁, K₂ pairs and V
  - Two softmax operations on Q₁K₁ᵀ and Q₂K₂ᵀ
  - Subtraction with λ scaling
  - Multiplication with V and h Heads
  - GroupNorm with (1 − λᵢₙᵢₜ) multiplier
  - Concat operation
  - Linear projection to output
- Right side: Two code blocks showing Python-style implementation
  - `DiffAttn(X, W_q, W_k, W_v, λ)`: Implements the basic differential attention
  - `MultiHead(X, W_qi, W_ki, W_vi, W_o, λ)`: Implements multi-head version with GroupNorm
- Key elements: Shows how two separate softmax maps are computed and subtracted, then scaled by learnable λ
- Supports claim: Illustrates the complete differential attention mechanism with normalization strategy
