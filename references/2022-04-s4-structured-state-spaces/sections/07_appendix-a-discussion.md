# A Discussion [p. 16]

[p. 16]

## Related Work

The work is most closely related to a line of work originally motivated by a particular biologically-inspired SSM, which led to mathematical models for addressing LRDs. Voelker et al. [45] and Voelker [46] derived a non-trainable SSM motivated from approximating a neuromorphic spiking model, and Chilkuri and Eliasmith [7] showed that it could be sped up at train time with a convolutional view. Gu et al. [16] extended this special case to a general continuous-time function approximation framework with several more special cases of **A** matrices designed for long-range dependencies. However, instead of using a true SSM, all of these works fixed a choice of **A** and built RNNs around it. Most recently, Gu et al. [18] used the full (1) explicitly as a deep SSM model, exploring new conceptual views of SSMs, as well as allowing **A** to be trained. As mentioned in Section 1, their method used a naive instantiation of SSMs that suffered from an additional factor of N in memory and N^2 in computation.

Beyond this work, the technical contributions (Section 3) on the S4 parameterization and algorithms are applicable to a broader family of SSMs including those investigated in prior works, and the techniques for working with these models may be of independent interest.

## Implementation

The computational core of S4's training algorithm is the Cauchy kernel discussed in Sections 3.2 and 3.3 and Appendix C.3. As described in Appendix C.3 Proposition 5, there are many algorithms for it with differing computational complexities and sophistication. The current implementation of S4 actually uses the naive O(NL) algorithm which is easily parallelized on GPUs and has more easily accessible libraries allowing it to be implemented; they leverage the `pykeops` library for memory-efficient kernel operations. However, this library is a much more general library that may not be optimized for the Cauchy kernels used here, and the authors believe that a dedicated CUDA implementation can be more efficient. Additionally, as discussed in this work, there are asymptotically faster and numerically stable algorithms for the Cauchy kernel (Proposition 5). However, these algorithms are currently not implemented for GPUs due to a lack of previous applications that require them. The authors believe that more efficient implementations of these self-contained computational kernels are possible, and that S4 (and SSMs at large) may have significant room for further improvements in efficiency.

## Limitations and Future Directions

The authors show that S4 can address a wide variety of data effectively. However, it may not necessarily be the most suitable model for all types of data. For example, Table 8 still found a gap compared to Transformers for language modeling. An interesting future direction is exploring combinations of S4 with other sequence models to complement their strengths. The authors are excited about other directions, including continuing to explore the benefits of S4 on audio data (e.g. pre-training or generation settings), and generalizing HiPPO and S4 to higher-dimensional data for image and video applications.
