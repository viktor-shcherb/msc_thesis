# A Simplified SSM Architecture [p. 7–8]

## Section 3.4

[p. 7]

As with structured SSMs, selective SSMs are standalone sequence transformations that can be flexibly incorporated into neural networks. The H3 architecture is the basis for the most well-known SSM architectures (Section 2), which are generally comprised of a block inspired by linear attention interleaved with an MLP (multi-layer perceptron) block. The authors simplify this architecture by combining these two components into one, which is stacked homogenously (Figure 3). This is inspired by the gated attention unit (GAU) (Hua et al. 2022), which did something similar for attention.

This architecture involves expanding the model dimension $D$ by a controllable expansion factor $E$. For each block, most of the parameters ($3ED^2$) are in the linear projections ($2ED^2$ for input projections, $ED^2$ for output projection) while the inner SSM contributes less. The number of SSM parameters (projections for $\Delta$, $\boldsymbol{B}$, $\boldsymbol{C}$, and the matrix $\boldsymbol{A}$) are much smaller in comparison. This block is repeated, interleaved with standard normalization and residual connections, to form the Mamba architecture. [p. 7]

The authors always fix $E = 2$ in their experiments and use two stacks of the block to match the $12D^2$ parameters of a Transformer's interleaved MHA (multi-head attention) and MLP blocks. [p. 7]

Activation function: SiLU / Swish (Hendrycks and Gimpel 2016; Ramachandran, Zoph, and Quoc V Le 2017), motivated so that the Gated MLP becomes the popular "SwiGLU" variant (Chowdhery et al. 2023; Dauphin et al. 2017; Shazeer 2020; Touvron et al. 2023). [p. 7]

An optional normalization layer is additionally used (the authors choose LayerNorm (J. L. Ba, Kiros, and Hinton 2016)), motivated by RetNet's usage of a normalization layer in a similar location (Y. Sun et al. 2023). [p. 7]

## Figures

**Figure 3** (p. 8): "(**Architecture.**) Our simplified block design combines the H3 block, which is the basis of most SSM architectures, with the ubiquitous MLP block of modern neural networks. Instead of interleaving these two blocks, we simply repeat the Mamba block homogenously. Compared to the H3 block, Mamba replaces the first multiplicative gate with an activation function. Compared to the MLP block, Mamba adds an SSM to the main branch. For $\sigma$ we use the SiLU / Swish activation (Hendrycks and Gimpel 2016; Ramachandran, Zoph, and Quoc V Le 2017)."

The figure shows three block diagrams side by side with an arrow indicating the transformation from H3 + Gated MLP to the Mamba block:
- **H3 block** (left): Input feeds into a linear projection that splits into two branches. The main branch goes through Conv then SSM, followed by a multiplicative gate (×) with the other branch. Output goes through a linear projection.
- **Gated MLP** (middle): Input feeds into a linear projection that splits into two branches. One branch applies an activation function $\sigma$, then both are combined with a multiplicative gate (×). Output through linear projection.
- **Mamba block** (right): Input feeds into a linear projection that splits into two branches. The main branch goes through Conv, then an activation $\sigma$, then SSM, and is combined via multiplicative gate (×) with the second branch (which also passes through $\sigma$). Output through linear projection.

A legend indicates: white rectangles = Linear projection, dark rectangles = Sequence transformation, circled × = Nonlinearity (activation or multiplication).
