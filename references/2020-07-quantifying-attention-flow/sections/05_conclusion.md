# 5 Conclusion [p. 5]

[p. 5] Translating embedding attentions to token attentions can provide better explanations about models' internals. Yet, one should be cautious about interpretation of these weights, because many simplifying assumptions are being made when approximating information flow in a model with the attention weights.

The ideas are simple and task/architecture agnostic. The paper insists on sticking with simple ideas that only require attention weights and can be easily employed in any task or architecture that uses self-attention.

**Important caveat:** All analysis in the paper is for a Transformer encoder, with no causal masking. In a Transformer decoder, future tokens are masked, so naturally there is more attention toward initial tokens in the input sequence, and both attention rollout and attention flow will be biased toward these tokens. To apply these methods on a Transformer decoder, one should first normalize based on the receptive field of attention.

## Future directions

[p. 5] Two future directions are suggested:
1. Building the attention graph with effective attention weights (Brunner et al., 2020) instead of raw attentions
2. A new method that adjusts the attention weights using gradient-based attribution methods (Ancona et al., 2019)
