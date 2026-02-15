# Appendix I: Parameter Initializations [p. 38–40]

[p. 38] Throughout this section, we use l to denote the layer index (layer l = 0 accepts input embeddings and layer l = L−1 produces output), and i the dimension index (i = 0, 1, ⋯, D−1). We set r₀ = l/(L-1) and r₁ = 1 − l/L as two parameters for simplicity.

[p. 38] The initialization of Eagle is provided as follows:

• In the Time Mixing module:
  - The token-shift coefficients of receptance and gate, μᵣ and μ_g, are initialized to 1 − (i/D)^{r₁/2} for i over dimension indices.
  - The token-shift of key μₖ is initialized to 1 − (i/D)^{r₁}.
  - The token-shift of value μᵥ is initialized to 1 − (i/D)^{r₁} − 0.3r₀.
  - The time_decay w is initialized to −6 + 5(i/(D-1))^{0.7+1.3r₀}.
  - The "time-first" u is initialized to r₀(1 − i/(D-1)) + 0.1((i + 1) mod 3).
  - The Time Mixing output matrix is initialized to 0.

[p. 40] - The WKV GroupNorm weights are initialized with constant value ((1 + l)/L)^{0.7}.
  - Two-dimensional parameters with the first dimension being larger than the second dimension are initialized with and orthogonal initialization of gain equal to the size of the first dimension divided by the size of the second dimension.
  - Other parameters are initialized according to PyTorch default.

• In the Channel Mixing module:
  - The token-shift of both key μₖ and receptance μᵣ are initialized to 1 − (i/D)^{r₁}.
  - The value and receptance matrices W_v, W_r are initialized to 0.
  - Two-dimensional parameters with the first dimension being larger than the second dimension are initialized with and orthogonal initialization of gain equal to the size of the first dimension divided by the size of the second dimension.
  - All other parameters are initialized according to PyTorch default.

• The input embedding is initialized with a uniform distribution of U(−maxLR, maxLR), the maximum learning rate.

• The output head is initialized with an orthogonal initialization of gain 0.5.

• Bias is set to False for all linear layers.

[p. 40] In the Finch architecture, most of the parameters are initialized to the same as Eagle, except for a few changes.

[p. 40] In the Time Mixing block, there are several additional parameters initialized as follows:

• The token shift of input μₓ and time decay μ_w are initialized to 1 − (i/D)^{r₁}.
• The lora weights of A and B are initialized to uniform distribution of U(−10⁻⁴, 10⁻⁴).
