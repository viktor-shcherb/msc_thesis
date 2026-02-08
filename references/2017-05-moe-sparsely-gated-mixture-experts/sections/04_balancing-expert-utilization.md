# 4 Balancing Expert Utilization [p. 5-6]

[p. 5] The gating network tends to converge to a state where it always produces large weights for the same few experts. This imbalance is self-reinforcing, as the favored experts are trained more rapidly and thus are selected even more by the gating network. Eigen et al. (2013) describe the same phenomenon, and use a hard constraint at the beginning of training to avoid this local minimum. Bengio et al. (2015) include a soft constraint on the batch-wise average of each gate.

The authors take a soft constraint approach. They define the importance of an expert relative to a batch of training examples to be the batchwise sum of the gate values for that expert. They define an additional loss L_importance, which is added to the overall loss function for the model. This loss is equal to the square of the coefficient of variation of the set of importance values, multiplied by a hand-tuned scaling factor w_importance. This additional loss encourages all experts to have equal importance.

$$Importance(X) = \sum_{x \in X} G(x) \tag{6}$$

$$L_{importance}(X) = w_{importance} \cdot CV(Importance(X))^2 \tag{7}$$

[p. 5-6] Bengio et al. (2015) also include two additional losses. One controls per-example sparsity, which is not needed here since it is enforced by the fixed value of k. A third loss encourages diversity of gate values. In the authors' experiments, they find that the gate values naturally diversify as the experts specialize (in a virtuous cycle), and they do not need to enforce diversity of gate values.

[p. 6] While the importance loss function can ensure equal importance, experts may still receive very different numbers of examples. For example, one expert may receive a few examples with large weights, and another may receive many examples with small weights. This can cause memory and performance problems on distributed hardware. To solve this problem, they introduce a second loss function, L_load, which ensures balanced loads. Appendix A contains the definition of this function, along with experimental results.
