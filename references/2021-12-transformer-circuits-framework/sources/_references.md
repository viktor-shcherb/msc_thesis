# References

## Cited works

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* The original transformer architecture paper. The mathematical framework presented here is built entirely around analyzing the attention mechanism introduced in this work. The QK/OV circuit decomposition directly corresponds to the multi-head attention formulation from this paper.

- **Radford et al. (2019)** -- *Language Models are Unsupervised Multitask Learners (GPT-2).* The decoder-only autoregressive transformer architecture studied in the framework paper follows the GPT lineage. GPT-2's architecture (token embedding, residual blocks, unembedding) provides the concrete model structure being reverse-engineered.

- **Olah et al. (2020)** -- *Zoom In: An Introduction to Circuits.* The circuits framework for understanding neural networks, originally developed for vision models (convolutional networks). This work established the conceptual foundation of decomposing neural networks into interpretable circuits composed of features and weights. The transformer circuits framework extends this approach from vision to language models.

- **Olah et al. (2018)** -- *The Building Blocks of Interpretability.* Earlier interpretability work establishing methods for understanding individual neurons and their interactions in neural networks, laying groundwork for the circuits-based approach.

- **Black et al.** -- Work on polysemantic neurons and superposition. Referenced in the discussion of why the residual stream lacks a privileged basis and why MLP neurons respond to multiple unrelated features. The concept of features existing in "superposition" (more features than dimensions) is discussed as a key challenge for interpretability.
