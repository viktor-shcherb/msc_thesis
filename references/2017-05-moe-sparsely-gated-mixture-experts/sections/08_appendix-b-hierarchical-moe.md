# Appendix B: Hierarchical Mixture of Experts [p. 14]

[p. 14] If the number of experts is very large, the branching factor can be reduced by using a two-level hierarchical MoE. In a hierarchical MoE, a primary gating network chooses a sparse weighted combination of "experts", each of which is itself a secondary mixture-of-experts with its own gating network.^3

^3 The authors have not found the need for deeper hierarchies.

If the hierarchical MoE consists of a groups of b experts each, the primary gating network is denoted G_primary, the secondary gating networks by (G_1, G_2, ..., G_a), and the expert networks by (E_{0,0}, E_{0,1}, ..., E_{a,b}). The output of the MoE is given by:

$$y_H = \sum_{i=1}^{a} \sum_{j=1}^{b} G_{primary}(x)_i \cdot G_i(x)_j \cdot E_{i,j}(x) \tag{12}$$

## Hierarchical Importance and Load Metrics

[p. 14] The metrics of expert utilization change to the following:

$$Importance_H(X)_{i,j} = \sum_{x \in X} G_{primary}(x)_i \cdot G_i(x)_j \tag{13}$$

$$Load_H(X)_{i,j} = \frac{Load_{primary}(X)_i \cdot Load_i(X^{(i)})_j}{|X^{(i)}|} \tag{14}$$

Load_primary and Load_i denote the Load functions for the primary gating network and i^th secondary gating network respectively. X^(i) denotes the subset of X for which G_primary(x)_i > 0.

[p. 14] It would seem simpler to let Load_H(X)_{i,j} = Load_i(X_i)_j, but this would not have a gradient with respect to the primary gating network, so the formulation above is used.
