# C. Encouraging Exploration Across Experts [p. 29-30]

[p. 29]

At each expert-layer, the router determines to which expert to send the token. This is a discrete decision over the available experts, conditioned on information about the token's representation. Based on the incoming token representation, the router determines the best expert, however, it receives no counterfactual information about how well it would have done selecting an alternate expert. As in reinforcement learning, a classic exploration-exploitation dilemma arises (Sutton and Barto, 2018). These issues have been similarly noted and addressed differently by Rosenbaum et al. (2017) which demonstrated success in multi-task learning. This particular setting most closely matches that of a contextual bandit (Robbins, 1952). Deterministically selecting the top expert always amounts to an exploitative strategy -- the authors consider balancing exploration to seek better expert assignment.

To introduce exploration, several approaches are considered: 1) deterministic or argmax 2) sampling from the softmax distribution 3) input dropout on the incoming representation 4) multiplicative jitter noise on the incoming representation. The resulting impact on model quality is reported in Table 11. Throughout this work, the authors use input jitter to inject noise as they have found it to empirically perform the best.

[p. 30]

**Table 11: Router Exploration Strategies** (p. 30)

Quality of the Switch Transformer, measured by the negative log perplexity, under different randomness-strategies for selecting the expert (lower is better). There is no material speed performance difference between the variants.

| Model | Quality (Neg. Log Perp.) (up) |
|---|---|
| Argmax | -1.471 |
| Sample softmax | -1.570 |
| Input dropout | -1.480 |
| Input jitter | **-1.468** |
