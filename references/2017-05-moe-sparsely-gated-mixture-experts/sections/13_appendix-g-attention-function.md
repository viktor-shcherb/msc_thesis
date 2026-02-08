# Appendix G: Attention Function [p. 19]

[p. 19] The attention mechanism described in GNMT (Wu et al., 2016) involves a learned "Attention Function" A(x_i, y_j) which takes a "source vector" x_i and a "target vector" y_j, and must be computed for every source time step i and target time step j. In GNMT, the attention function is implemented as a feed forward neural network with a hidden layer of size n. It can be expressed as:

$$A_{GNMT}(x_i, y_j) = \sum_{d=1}^{n} V_d tanh((x_i U)_d + (y_j W)_d) \tag{21}$$

Where U and W are trainable weight matrices and V is a trainable weight vector.

[p. 19] For performance reasons, a slightly different attention function is used in the MoE models:

$$A(x_i, y_j) = \sum_{d=1}^{n} V_d tanh((x_i U)_d) tanh((y_j W)_d) \tag{22}$$

With this attention function, the attention can be simultaneously computed on multiple source time steps and multiple target time steps using optimized matrix multiplications. The authors found little difference in quality between the two functions.
