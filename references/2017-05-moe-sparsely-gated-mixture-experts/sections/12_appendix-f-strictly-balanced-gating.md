# Appendix F: Strictly Balanced Gating [p. 18–19]

[p. 18] Due to some peculiarities in the infrastructure which have since been fixed, at the time of running some of the machine translation experiments, the models ran faster if every expert received exactly the same batch size. To accommodate this, a different gating function is used, described below.

## Softmax Gating (Recall)

[p. 18] The softmax gating function is defined as:

$$G_\sigma(x) = Softmax(x \cdot W_g) \tag{15}$$

## Sparse Gating (Alternate Formulation)

[p. 18–19] To obtain a sparse gating vector, G_sigma(x) is multiplied component-wise with a sparse mask M(G_sigma(x)) and the output is normalized. The mask itself is a function of G_sigma(x) and specifies which experts are assigned to each input example:

$$G(x)_i = \frac{G_\sigma(x)_i M(G_\sigma(x))_i}{\sum_{j=1}^{n} G_\sigma(x)_j M(G_\sigma(x))_j} \tag{16}$$

## Top-K Mask

[p. 19] To implement top-k gating in this formulation, M(v) = TopK(v, k), where:

$$TopK(v, k)_i = \begin{cases} 1 & \text{if } v_i \text{ is in the top } k \text{ elements of } v \\ 0 & \text{otherwise} \end{cases} \tag{17}$$

## Batchwise Mask

[p. 19] To force each expert to receive the exact same number of examples, an alternative mask function, M_batchwise(X, m), is introduced, which operates over batches of input vectors. Instead of keeping the top k values per example, the top m values per expert are kept across the training batch, where m = k|X|/n, so that each example is sent to an average of k experts.

$$M_{batchwise}(X, m)_{j,i} = \begin{cases} 1 & \text{if } X_{j,i} \text{ is in the top } m \text{ values for to expert } i \\ 0 & \text{otherwise} \end{cases} \tag{18}$$

[p. 19] As the experiments suggest and also observed in (Ioffe & Szegedy, 2015), using a batchwise function during training (such as M_batchwise) requires modifications to the inference when there may not be a large batch of examples. The solution is to train a vector T of per-expert threshold values to approximate the effects of the batchwise mask. The following mask is used at inference time:

$$M_{threshold}(x, T)_i = \begin{cases} 1 & \text{if } x_i > T_i \\ 0 & \text{otherwise} \end{cases} \tag{19}$$

[p. 19] To learn the threshold values, an additional loss is applied at training time which is minimized when the batchwise mask and the threshold mask are identical:

$$L_{batchwise}(X, T, m) = \sum_{j=1}^{|X|} \sum_{i=1}^{n} (M_{threshold}(x, T)_i - M_{batchwise}(X, m)_{j,i})(X_{j,i} - T_i) \tag{20}$$
