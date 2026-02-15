# 2.2 Overall Architecture [p. 4]

The overall architecture stacks L layers, where each layer contains a multi-head differential attention module, and a feed-forward network module [p. 4]. The authors describe the Differential Transformer layer as:

$$Y^l = \text{MultiHead}(\text{LN}(X^l)) + X^l$$

$$X^{l+1} = \text{SwiGLU}(\text{LN}(Y^l)) + Y^l$$

(Equations 4 and 5)

where LN(·) is RMSNorm (Zhang & Sennrich, 2019), SwiGLU(X) = (swish(XW^G) ⊙ XW₁)W₂, and W^G, W₁ ∈ ℝᵈᵐᵒᵈᵉˡˣ⁸/³ᵈᵐᵒᵈᵉˡ, W₂ ∈ ℝ⁸/³ᵈᵐᵒᵈᵉˡˣᵈᵐᵒᵈᵉˡ are learnable matrices [p. 4].
