# 1 Introduction [p. 1-3]

## Motivation

[p. 1] Transformers, in particular decoder-only models (e.g. GPT (Brown et al. 2020), Llama (Touvron, Lavril, et al. 2023)), process input sequences causally and are the main driver of modern deep learning's success. Numerous approaches attempt to approximate the core attention layer to address its efficiency issues (Tay et al. 2022), which scale quadratically in sequence length during training and require a cache of size linear in sequence length during autoregressive generation.

In parallel, structured state-space models (SSMs) have emerged with linear scaling in sequence length during training and constant state size during generation. They show strong performance on long-range tasks (e.g. S4 (Gu, Goel, and Ré 2022)) and recently matched or beat Transformers on language modeling (e.g. Mamba (Gu and Dao 2023)) at small to moderate scale.

However, the development of SSMs has appeared disjoint from the community's collective effort to improve Transformers, both theoretically and in terms of hardware optimization. It is more difficult to understand and experiment with SSMs compared to Transformers, and it remains challenging to train SSMs as efficiently as Transformers from both an algorithmic and systems perspective.

## Main Goal

[p. 1] The main goal is to develop a rich body of theoretical connections between structured SSMs and variants of attention. This will allow transferring algorithmic and systems optimizations originally developed for Transformers to SSMs, towards building foundation models that perform better than Transformers while scaling more efficiently in sequence length.

A milestone contribution in this direction was the **Linear Attention (LA)** framework (Katharopoulos et al. 2020), which derived a connection between autoregressive attention and linear RNNs by showing the equivalence between "dual forms" of quadratic kernelized attention and a particular linear recurrence. This duality allows new capabilities such as the ability to have both efficient parallelizable training and efficient autoregressive inference.

> "In the same spirit, this paper provides multiple viewpoints connecting linear-complexity SSMs with quadratic-complexity forms to combine the strengths of SSMs and attention." [p. 1]

Footnote 1: The title is an homage to Katharopoulos et al. (2020), which first showed that "Transformers are RNNs".

## Contributions

### State Space Duality

[p. 2] The framework connecting structured SSMs and variants of attention is called **structured state space duality (SSD)**, made through the abstractions of **structured matrices**: matrices with subquadratic parameters and multiplication complexity. Two broad frameworks for representing sequence models are developed: one as matrix transformations and one as tensor contractions, which each reveal different perspectives of the duality. Technical contributions include:

- An equivalence between state space models and a well-studied family of structured matrices called **semiseparable matrices** (Section 3). This connection is at the heart of the framework. A central message of the paper is that *different methods of computing state space models can be reframed as various matrix multiplication algorithms on structured matrices*.

- Significantly improving the theory of linear attention (Katharopoulos et al. 2020). First providing an incisive proof of its recurrent form through the language of tensor contractions, then generalizing it to a new family of **structured masked attention (SMA)** (Section 4).

- Connecting SSMs and SMA, showing that they have a large intersection that are duals of each other, possessing both SSM-like linear and attention-like quadratic forms (Section 5). Also proving that any kernel attention method possessing a fast recurrent form must be an SSM.

### Efficient Algorithms

[p. 2] The framework exposes new efficient and easily-implementable algorithms for computing SSMs (Section 6). A new **SSD algorithm** is introduced, based on block decompositions of semiseparable matrices, that takes advantage of both the linear SSM recurrence and quadratic dual form, obtaining optimal tradeoffs on all main efficiency axes (training and inference compute, memory usage, and ability to leverage matrix multiplication units on modern hardware).

A dedicated implementation of SSD is 2-8x faster than the optimized selective scan implementation of Mamba, while simultaneously allowing for much larger recurrent state sizes (8x the size of Mamba or even higher, with minimal slowdown). SSD is highly competitive with optimized implementations of softmax attention (FlashAttention-2 (Dao 2024)), crossing over at sequence length 2K and 6x faster at sequence length 16K.

### Architecture Design

[p. 2] One major obstacle to adopting new architectures such as SSMs is the ecosystem tailored to Transformers, such as hardware-efficient optimization and parallelism techniques for large-scale training. The framework allows using established conventions and techniques for attention to build a vocabulary of architecture design choices for SSMs, and further improve them (Section 7). The analog of heads from multi-head attention (MHA) to SSMs is introduced. The Mamba architecture is shown to be a **multi-input SSM (MIS)** that turns out to be analogous to **multi-value attention (MVA)**, and other variants of Mamba with different head structures are compared.

Slight modifications to the Mamba block allow tensor parallelism to be implemented (e.g. in the style of Megatron (Shoeybi et al. 2019)). The main ideas include introducing grouped-value attention (GVA) head structure, and moving all data-dependent projections to occur in parallel at the beginning of the block.

The combination of the modified parallel Mamba block, together with using SSD as the inner SSM layer, results in the **Mamba-2** architecture.

[p. 3] The authors investigate Chinchilla scaling laws for Mamba-2 in the same setting as Mamba, finding that it Pareto dominates Mamba and Transformer++ in both perplexity and wall-clock time. They additionally train a family of Mamba-2 models at varying sizes on the Pile, showing that it matches or outperforms Mamba and open source Transformers on standard downstream evaluations. For example, Mamba-2 with 2.7B parameters trained on 300B tokens on the Pile outperforms Mamba-2.8B, Pythia-2.8B and even Pythia-6.9B trained on the same dataset.

### Systems Optimizations

[p. 3] The SSD framework connects SSMs and Transformers, allowing leverage of a rich body of work on systems optimizations developed for Transformers (Section 8):

- Tensor Parallelism (TP) is an important model parallelism technique to train large Transformer models by splitting each layer across GPUs on the same node. Mamba-2 is designed to be TP-friendly, reducing the number of synchronization points per block by half.

- For very long sequences whose activations do not fit on one device, sequence parallelism has been developed for the attention blocks. The authors describe how to train SSMs in general and Mamba-2 in particular with sequence parallelism, by passing the recurrent states between devices.

- For finetuning with examples of different lengths, for best efficiency, Transformer requires sophisticated techniques to remove padding tokens and perform attention on variable length sequences. The authors show how Mamba-2 can be trained with variable sequence lengths efficiently, requiring no padding tokens.

## Paper Structure

[p. 3] Section 9 empirically validates Mamba-2 on language modeling, training efficiency, and a difficult multi-query associative recall task (Arora, Eyuboglu, Zhang, et al. 2024). Section 10 provides extended related work and discusses potential research directions.

Model code and pre-trained checkpoints are open-sourced at https://github.com/state-spaces/mamba.
