# Appendix A: Load-Balancing Loss [p. 13]

[p. 13] As discussed in Section 4, for load-balancing purposes the authors define an additional loss function to encourage experts to receive roughly equal numbers of training examples. The number of examples received by an expert is a discrete quantity, so it cannot be used in backpropagation. Instead, they define a smooth estimator Load(X) of the number of examples assigned to each expert for a batch X of inputs. The smoothness allows back-propagating gradients through the estimator. This is the purpose of the noise term in the gating function.

## Smooth Load Estimator

[p. 13] P(x, i) is defined as the probability that G(x)_i is nonzero, given a new random choice of noise on element i, but keeping the already-sampled choices of noise on the other elements. To compute P(x, i), note that G(x)_i is nonzero if and only if H(x)_i is greater than the k^th-greatest element of H(x) excluding itself. The probability works out to be:

$$P(x, i) = Pr\Big((x \cdot W_g)_i + StandardNormal() \cdot Softplus((x \cdot W_{noise})_i) > kth\_excluding(H(x), k, i)\Big) \tag{8}$$

Where kth_excluding(v, k, i) means the kth highest component of v, excluding component i. Simplifying, we get:

$$P(x, i) = \Phi\Big(\frac{(x \cdot W_g)_i - kth\_excluding(H(x), k, i)}{Softplus((x \cdot W_{noise})_i)}\Big) \tag{9}$$

Where Phi is the CDF of the standard normal distribution.

$$Load(X)_i = \sum_{x \in X} P(x, i) \tag{10}$$

## Load Loss

[p. 13] The load loss is defined as the square of the coefficient of variation of the load vector, multiplied by a hand-tuned scaling factor w_load:

$$L_{load}(X) = w_{load} \cdot CV(Load(X))^2 \tag{11}$$

## Initial Load Imbalance

[p. 13] To avoid out-of-memory errors, the network needs to be initialized in a state of approximately equal expert load (since the soft constraints need some time to work). To accomplish this, the matrices W_g and W_noise are initialized to all zeros, which yields no signal and some noise.

## Experiments on Balancing Losses

[p. 13] The authors trained a set of models with identical architecture (the MoE-256 model described in Appendix C), using different values of w_importance and w_load. Each model was trained for 10 epochs, then test perplexity was measured on the test set. They also measured the coefficients of variation in Importance and Load, as well as ratio of the load on the most overloaded expert to the average load. This last value is significant for load balancing purposes on distributed hardware. All metrics were averaged over several training batches.

**Table 6** (p. 13): Experiments with different combinations of losses.

| w_importance | w_load | Test Perplexity | CV(Importance(X)) | CV(Load(X)) | max(Load(X)) / mean(Load(X)) |
|---|---|---|---|---|---|
| 0.0 | 0.0 | 39.8 | 3.04 | 3.01 | 17.80 |
| 0.2 | 0.0 | **35.6** | 0.06 | 0.17 | 1.47 |
| 0.0 | 0.2 | 35.7 | 0.22 | 0.04 | 1.15 |
| 0.1 | 0.1 | **35.6** | 0.06 | 0.05 | 1.14 |
| 0.01 | 0.01 | 35.7 | 0.48 | 0.11 | 1.37 |
| 1.0 | 1.0 | 35.7 | 0.03 | 0.02 | **1.07** |

[p. 14] **Results:** All the combinations containing at least one of the two losses led to very similar model quality, where having no loss was much worse. Models with higher values of w_load had lower loads on the most overloaded expert.
