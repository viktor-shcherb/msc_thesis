# 1 Introduction and Related Work [p. 1-3]

## 1.1 Conditional Computation [p. 1]

[p. 1] Exploiting scale in both training data and model size has been central to deep learning success. When datasets are sufficiently large, increasing the capacity (number of parameters) of neural networks can give much better prediction accuracy, shown in domains such as text (Sutskever et al., 2014; Bahdanau et al., 2014; Jozefowicz et al., 2016; Wu et al., 2016), images (Krizhevsky et al., 2012; Le et al., 2012), and audio (Hinton et al., 2012; Amodei et al., 2015).

For typical deep learning models where the entire model is activated for every example, this leads to a roughly quadratic blow-up in training costs, as both model size and number of training examples increase. Advances in computing power and distributed computation fall short of meeting such demand.

[p. 1] Various forms of conditional computation have been proposed to increase model capacity without proportional increase in computational costs (Davis & Arel, 2013; Bengio et al., 2013; Eigen et al., 2013; Ludovic Denoyer, 2014; Cho & Bengio, 2014; Bengio et al., 2015; Almahairi et al., 2015). In these schemes, large parts of a network are active or inactive on a per-example basis. Gating decisions may be binary or sparse and continuous, stochastic or deterministic. Various forms of reinforcement learning and back-propagation are proposed for training the gating decisions.

[p. 2] **Figure 1** (p. 2): "A Mixture of Experts (MoE) layer embedded within a recurrent language model. In this case, the sparse gating function selects two experts to perform computations. Their outputs are modulated by the outputs of the gating network."
- Left side shows a recurrent language model with two stacked MoE layers between LSTM layers.
- Right side shows the internal structure of a single MoE layer: input goes into a Gating Network, which produces gate values G(x)_2 and G(x)_{n-1} for the selected experts (Expert 1 through Expert n). The selected expert outputs are multiplied by their gate values and summed to produce the layer output.

[p. 2] While these ideas are promising in theory, no work to date has demonstrated massive improvements in model capacity, training time, or model quality. The authors blame this on a combination of the following challenges:

- Modern computing devices, especially GPUs, are much faster at arithmetic than at branching. Most prior works propose turning on/off large chunks of the network with each gating decision.
- Large batch sizes are critical for performance, as they amortize the costs of parameter transfers and updates. Conditional computation reduces the batch sizes for the conditionally active chunks of the network.
- Network bandwidth can be a bottleneck. A cluster of GPUs may have computational power thousands of times greater than the aggregate inter-device network bandwidth. To be computationally efficient, the relative computational versus network demands of an algorithm must exceed this ratio. Embedding layers, which can be seen as a form of conditional computation, are handicapped by this very problem. Since the embeddings generally need to be sent across the network, the number of (example, parameter) interactions is limited by network bandwidth instead of computational capacity.
- Depending on the scheme, loss terms may be necessary to achieve the desired level of sparsity per-chunk and/or per example. Bengio et al. (2015) use three such terms. These issues can affect both model quality and load-balancing.
- Model capacity is most critical for very large data sets. The existing literature on conditional computation deals with relatively small image recognition data sets consisting of up to 600,000 images. It is hard to imagine that the labels of these images provide a sufficient signal to adequately train a model with millions, let alone billions of parameters.

> "In this work, we for the first time address all of the above challenges and finally realize the promise of conditional computation. We obtain greater than 1000x improvements in model capacity with only minor losses in computational efficiency and significantly advance the state-of-the-art results on public language modeling and translation data sets." [p. 2]

## 1.2 Our Approach: The Sparsely-Gated Mixture-of-Experts Layer [p. 2-3]

[p. 2-3] The approach is to introduce a new type of general purpose neural network component: a Sparsely-Gated Mixture-of-Experts Layer (MoE). The MoE consists of a number of experts, each a simple feed-forward neural network, and a trainable gating network which selects a sparse combination of the experts to process each input (see Figure 1). All parts of the network are trained jointly by back-propagation.

While the technique is generic, the paper focuses on language modeling and machine translation tasks, which benefit from very large models. A MoE is applied convolutionally between stacked LSTM layers (Hochreiter & Schmidhuber, 1997), as in Figure 1. The MoE is called once for each position in the text, selecting a potentially different combination of experts at each position. The different experts tend to become highly specialized based on syntax and semantics (see Appendix E, Table 9). On both language modeling and machine translation benchmarks, they improve on best published results at a fraction of the computational cost.

## 1.3 Related Work on Mixtures of Experts [p. 3]

[p. 3] The mixture-of-experts approach has been the subject of much research since its introduction more than two decades ago (Jacobs et al., 1991; Jordan & Jacobs, 1994). Different types of expert architectures have been proposed:
- SVMs (Collobert et al., 2002)
- Gaussian Processes (Tresp, 2001; Theis & Bethge, 2015; Deisenroth & Ng, 2015)
- Dirichlet Processes (Shahbaba & Neal, 2009)
- Deep networks

Other work has focused on different expert configurations:
- Hierarchical structure (Yao et al., 2009)
- Infinite numbers of experts (Rasmussen & Ghahramani, 2002)
- Adding experts sequentially (Aljundi et al., 2016)

Garmash & Monz (2016) suggest an ensemble model in the format of mixture of experts for machine translation. The gating network is trained on a pre-trained ensemble NMT model.

The works above concern top-level mixtures of experts where the mixture of experts is the whole model. Eigen et al. (2013) introduce the idea of using multiple MoEs with their own gating networks as parts of a deep model. It is intuitive that this latter approach is more powerful, since complex problems may contain many sub-problems each requiring different experts. They also allude in their conclusion to the potential to introduce sparsity, turning MoEs into a vehicle for computational computation.

[p. 3] The current work builds on using MoEs as a general purpose neural network component. While Eigen et al. (2013) uses two stacked MoEs allowing for two sets of gating decisions, this paper's convolutional application of the MoE allows for different gating decisions at each position in the text. They also realize sparse gating and demonstrate its use as a practical way to massively increase model capacity.
