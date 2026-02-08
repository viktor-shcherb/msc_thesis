# Appendix B: Additional Architecture Details (continued) [p. 31]

### Figure 10: Eagle Overall Architecture [p. 31]

**Figure 10:** Eagle Overall Architecture.

The figure shows a detailed architecture diagram with:
- **Input Embedding** at the bottom
- **RWKV Block × L** (repeated L times) containing:
  - **Layer Norm** with w, b parameters
  - **Time Mix** block (green section) containing:
    - Layer Norm with components I_j, b_j and WKV Header
    - Multiple pathways with parameters W_k, W_o_j, W_k_j, W_v_j
    - Token shift components with μ_r, μ_v, μ_k, μ_w parameters
    - State management (dim 64×64)
    - Various connection points labeled x'_i-1 and x'_i
  - **Channel Mix** block (beige section) containing:
    - Parameters W'_k, W'_v
    - Components μ'_r, μ'_k
    - Multiplication and addition operations
- **Layer Norm** between blocks
- **Output Embedding** at the top with dimension d'
- **Softmax** operation at the very top

The diagram shows signal flow from bottom to top, with residual connections (⊕) between blocks.
