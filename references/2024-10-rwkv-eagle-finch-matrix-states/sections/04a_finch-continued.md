# Method - Finch (continued) [p. 7–8]

[p. 7–8] where μ_□ and each λ_□ introduce a trainable vector of dimension D and each A_□ ∈ R^{D×32}, B_□ ∈ R^{32×D} introduce new trainable weight matrices. For the special case of LoRA_□ seen below we introduce double-sized trainable matrices A_□ ∈ R^{D×64}, B_□ ∈ R^{64×D}. A schematic representation can be found in Figure 1, bottom-right. Please note that future 7B and larger Finch models are expected to further increase the size of these weight matrices by double or more.

[p. 8] This new form of Token Shift enhanced with data-dependence is intended to expand the abilities of the model beyond the RWKV-4/Eagle style of Token Shift so that the amount of new and old data allocated per channel now depends on the input at both current and prior time steps.

### 4.2.2 Finch Time Mixing

[p. 8] The Finch Time Mixing equations are:

$$\square_i = \text{ddlerp}_{\square}(x_i, x_{i-1})W_{\square}, \quad \square \in \{r, k, v, g\}$$ (16)

$$d_i = \text{lora}_d(\text{ddlerp}_d(x_i, x_{i-1}))$$ (17)

$$w_i = \exp(-\exp(d_i))$$ (18)

$$wkv_t = \text{diag}(u) \cdot k_t^T \cdot v_t + \sum_{i=1}^{t-1} \text{diag}\left(\bigodot_{j=i+1}^{t-1} w_j\right) \cdot k_i^T \cdot v_i \in \mathbb{R}^{(D/h) \times (D/h)}$$ (19)

$$o_i = \text{concat}(\text{SiLU}(g_i) \odot \text{LayerNorm}(r_i \cdot wkv_i)) W_o \in \mathbb{R}^D$$ (20)

[p. 8] The wkv_i attention calculation can alternatively be written in a recurrent manner:

$$wkv' = s + \text{diag}(u) \cdot k^T \cdot v$$ (21)

$$s' = \text{diag}(w) \cdot s + k^T \cdot v$$ (22)

[p. 8] Unlike in Eagle, w_i here is not static across the sequence (dashed arrows in Figure 1, left and top-right). This is the core change to decay in Finch, as each channel of w_i can now vary independently over time, in a data-dependent manner, whereas previously it was a fixed learned vector.

[p. 8] The new LoRA mechanisms above are used on the learned vectors, as seen in Eagle, and inexpensively augment them with additional offsets determined by the incoming input. Note that the LoRA process itself uses an Eagle style Token-Shift on a just the latest token. The new time-varying decay w_i goes one step further, applying LoRA again afterward. Intuitively, this is a second-order variant of Token-Shifting, allowing each channel of w_i to vary based on a mix of the current and prior tokens, with the mix itself determined by aspects of both tokens.
