# Eagle/Finch Architecture [p. 5–6]

[p. 5] We refine the RWKV architecture in two steps, and observe significant modeling improvements with each. Compared to the baseline RWKV-4, Eagle adds matrix-valued attention states, LayerNorm over the attention heads, SiLU gated gating, and improved initialization. It also removes the Sigmoid activation of receptance. Finch further applies data-dependence to the decay schedule and token-shift.

[p. 5–6] The core architecture remains similar to that of RWKV-4, consisting of a series of stacked residual blocks shaped like a traditional Transformer. Following notation from (Tolstikhin et al., 2021), each block contains one Pre-LayerNorm Time-Mixing sub-layer followed by one Pre-LayerNorm Channel-Mixing sub-layer, as depicted in Figure 1, left. These correspond to the traditional Attention and Feed Forward Network sub-layers of the Transformer. See Appendix B for more details on our training implementation and the differences from RWKV-4, and Section 9 for speed and memory benchmarks.

## Figure 1 [p. 6]

**Figure 1:** RWKV architecture overview. **Left:** time-mixing and channel-mixing blocks; **top-right:** RWKV time-mixing block as RNN cell; **center-bottom:** token-shift module in FeedForward module and Eagle time-mixing; **bottom-right:** token-shift module in Finch time-mixing. All shape annotations assume a single head for simplicity. Dashed arrows (left, top-right) indicate a connection in Finch, but not in Eagle.

The figure shows:
- The overall RWKV architecture with Time Mixing and Channel Mixing blocks, each preceded by LayerNorm
- The Time Mixing block contains SiLU, G, R, K, V, W components, with a WKV gate mechanism
- The RNN cell representation showing how states are updated: h_{t-1:R^h} and x_{t-1:R^h} as inputs, producing h_{t:R^h} and x_{t:R^h}
- Token Shift modules showing different designs for FeedForward/Eagle vs Finch
- For Eagle: simple linear interpolation with μ-R^h parameter between x_{t-1:R^h} and x_{t:R^h}
- For Finch: more complex token shift with learnable parameters λ_□, A_□, B_□ using tanh and other operations
