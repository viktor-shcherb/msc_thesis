# Differential Transformer [p. 2]

The authors propose Differential Transformer (a.k.a. DIFF Transformer) as a foundation architecture for sequence modeling, such as large language models (LLMs) [p. 2]. They take a decoder-only model as an example to describe the architecture [p. 2].

The model is stacked with L DIFF Transformer layers [p. 2]. Given an input sequence x = x₁ ⋯ xₙ, they pack the input embeddings into X⁰ = [x₁, ⋯ ,xₙ] ∈ ℝᴺˣᵈᵐᵒᵈᵉˡ, where dₘₒdₑₗ represents the hidden dimension of the model [p. 2]. The input is further contextualized to obtain the output Xᴸ, i.e., Xˡ = Decoder(Xˡ⁻¹), ∀ l ∈ [1, L] [p. 2]. Each layer consists of two modules: a differential attention module followed by a feed-forward network module [p. 2].

Compared to Transformer (Vaswani et al., 2017), the novel part of the architecture is the replacement of traditional softmax attention with differential attention while the macro layout is kept the same [p. 2]. The authors also adopt pre-RMSNorm (Zhang & Sennrich, 2019; Ramachandran et al., 2017) as improvements following LLaMA (Touvron et al., 2023) [p. 2].
