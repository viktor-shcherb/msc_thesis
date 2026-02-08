# 2 The Structure of the Mixture-of-Experts Layer [p. 3-4]

[p. 3] The Mixture-of-Experts (MoE) layer consists of a set of n "expert networks" E_1, ..., E_n, and a "gating network" G whose output is a sparse n-dimensional vector. Figure 1 shows an overview of the MoE module. The experts are themselves neural networks, each with their own parameters. Although in principle they only require that the experts accept the same sized inputs and produce the same-sized outputs, in their initial investigations they restrict themselves to the case where the models are feed-forward networks with identical architectures, but with separate parameters.

Let G(x) and E_i(x) denote the output of the gating network and the output of the i-th expert network for a given input x. The output y of the MoE module can be written as:

$$y = \sum_{i=1}^{n} G(x)_i E_i(x) \tag{1}$$

Computation is saved based on the sparsity of G(x). Wherever G(x)_i = 0, we need not compute E_i(x). In experiments, they have up to thousands of experts, but only need to evaluate a handful of them for every example.

If the number of experts is very large, the branching factor can be reduced by using a two-level hierarchical MoE. In a hierarchical MoE, a primary gating network chooses a sparse weighted combination of "experts", each of which is itself a secondary mixture-of-experts with its own gating network. More details on hierarchical MoEs are in Appendix B.

[p. 3-4] The implementation is related to other models of conditional computation. A MoE whose experts are simple weight matrices is similar to the parameterized weight matrix proposed in (Cho & Bengio, 2014). A MoE whose experts have one hidden layer is similar to the block-wise dropout described in (Bengio et al., 2015), where the dropped-out layer is sandwiched between fully-activated layers.

## 2.1 Gating Network [p. 4]

**Softmax Gating:** A simple choice of non-sparse gating function (Jordan & Jacobs, 1994) is to multiply the input by a trainable weight matrix W_g and then apply the Softmax function.

$$G_\sigma(x) = Softmax(x \cdot W_g) \tag{2}$$

**Noisy Top-K Gating:** Two components are added to the Softmax gating network: sparsity and noise. Before taking the softmax function, tunable Gaussian noise is added, then only the top k values are kept, setting the rest to -infinity (which causes the corresponding gate values to equal 0). The sparsity serves to save computation. While this form of sparsity creates some theoretically scary discontinuities in the output of the gating function, they have not yet observed this to be a problem in practice. The noise term helps with load balancing, as discussed in Appendix A. The amount of noise per component is controlled by a second trainable weight matrix W_noise.

$$G(x) = Softmax(KeepTopK(H(x), k)) \tag{3}$$

$$H(x)_i = (x \cdot W_g)_i + StandardNormal() \cdot Softplus((x \cdot W_{noise})_i) \tag{4}$$

$$KeepTopK(v, k)_i = \begin{cases} v_i & \text{if } v_i \text{ is in the top } k \text{ elements of } v. \\ -\infty & \text{otherwise.} \end{cases} \tag{5}$$

**Training the Gating Network:** [p. 4] The gating network is trained with simple back-propagation, along with the rest of the model. If k > 1, the gate values for the top k experts have nonzero derivatives with respect to the weights of the gating network. This type of occasionally-sensitive behavior is described in (Bengio et al., 2013) with respect to noisy rectifiers. Gradients also back-propagate through the gating network to its inputs. The method differs from (Bengio et al., 2015) who use boolean gates and a REINFORCE-style approach to train the gating network.
