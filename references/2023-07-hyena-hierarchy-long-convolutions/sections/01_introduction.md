# Introduction [p. 1-3]

[p. 1]

Large Transformers have enabled breakthrough advances in modeling language, vision, audio, biology and numerous other domains (Vaswani et al., 2017), (Dosovitskiy et al., 2020), (Radford et al., 2022), (Cramer, 2021). Much of their success is powered by the attention operator (Vaswani et al., 2017), which relies on scaling properties (Hoffmann et al., 2022) and the emergence of in-context learning (Garg et al., 2022), allowing generalization to unseen data and tasks given context as input.

The Transformer block is powerful but has a key limitation: computational cost scales quadratically with the length $L$ of the input sequence, placing a strict limit on the amount of context the model can consider. Breaking the quadratic barrier would enable new possibilities such as using entire textbooks as context, generating long-form music, or processing gigapixel scale images. [p. 1]

Efforts to reduce the computational cost of attention primarily involve linearized, low-rank, and sparse approximations (Child et al., 2019; Wang et al., 2020; Kitaev et al., 2020; Zhai et al., 2021; Roy et al., 2021; Schlag et al., 2021; Tu et al., 2022). These approaches introduce a trade-off between expressivity and speed, requiring hybridization with standard attention layers to reach Transformer quality (Mehta et al., 2022; Dao et al., 2022c). [p. 1]

A growing amount of evidence suggests that attention mechanisms only utilize a small portion of their quadratic capabilities for language processing (Olsson et al., 2022; Dao et al., 2022c), leading the authors to ask:

> "*Are there subquadratic operators that can match the quality of attention at scale?*" [p. 1]

[p. 2]

**Figure 1.1** (p. 2): "The Hyena operator is defined as a recurrence of two efficient subquadratic primitives: an implicit long convolution $h$ (i.e. Hyena filters parameterized by a feed-forward network) and multiplicative element-wise gating of the (projected) input. The depth of the recurrence specifies the size of the operator. Hyena can equivalently be expressed as a multiplication with *data-controlled* (conditioned by the input $u$) diagonal matrices $\mathsf{D}_x$ and Toeplitz matrices $\mathsf{S}_h$. In addition, Hyena exhibits sublinear parameter scaling (in sequence length) and unrestricted context, similar to attention, while having lower time complexity."

The figure shows the Hyena Recurrence as a pipeline: input $u$ passes through a Dense projection to produce $v$, then alternates through Toeplitz matrices $\mathsf{S}_h^1, \mathsf{S}_h^2, \ldots, \mathsf{S}_h^N$ and diagonal matrices $\mathsf{D}_x^1, \ldots, \mathsf{D}_x^N$ to produce output $y$. Filters $h^1, h^2, \ldots, h^N$ are each produced by Dense layers. The right panel shows Hyena Filters $h^n$ as produced via a pipeline of Window, FFN, and PositionalEncoding.

The authors obtain a positive answer based on a composition of efficient subquadratic primitives: *element-wise multiplication* (gating) and *long convolutions* (i.e., convolutions with filter sizes as long as the input). They rely on targeted reasoning tasks, grounded in work on *mechanistic interpretability* (Elhage et al., 2021; Power et al., 2022; Olsson et al., 2022; Zhang et al., 2022), such as recall and induction, to distill three properties of attention correlated with its performance and the quality gap with existing subquadratic approaches: [p. 2]

*a.* **Data control:** Attention implements an expressive *data-controlled* (Massaroli et al., 2020) linear operator, encoding an entire family of linear functions in a single block. (Footnote 1: Self-attention can be expressed as $y = \mathsf{A}(k, q)v$ where $\mathsf{A}$ is the *attention matrix* conditioned by linear projections $k, q$ of the input and multiplied by $v$, another projection.)

*b.* **Sublinear parameter scaling:** Parameter counts of attention layers are decoupled from sequence length, allowing Transformers to allocate more parameters elsewhere e.g., the *feed-forward neural networks* (FFNs) between attention layers.

*c.* **Unrestricted context:** For a given input, attention has an unrestricted context i.e., it can approximate dependencies between any two inputs, without arbitrary restrictions such as locality (except in cases using masking such as autoregressive models). [p. 2]

## The Hyena Hierarchy

[p. 2]

Guided by these findings, the authors introduce the Hyena hierarchy, an operator defined by a recurrence of two efficient subquadratic primitives: **a long convolution and element-wise multiplicative gating** (see Figure 1.1). A specified depth (i.e., number of steps) of the recurrence controls the size of the operator. For short recurrences, existing models are recovered as special cases (Mehta et al., 2022; Dao et al., 2022c). By mapping each step in the Hyena recurrence to its corresponding matrix form, the authors reveal Hyena operators to be equivalently defined as a decomposition of a *data-controlled* matrix i.e., a matrix whose entries are functions of the input. Furthermore, Hyena operators can be evaluated efficiently without materializing the full matrix, by leveraging fast convolution algorithms (Selesnick and Burrus, 2017). Empirically, Hyena operators significantly shrink the quality gap with attention at scale, reaching similar perplexity and downstream performance with a smaller computational budget (Section 4.2) and **without hybridization** of attention. [p. 2]

## Narrowing the Capabilities Gap

[p. 2-3]

The design of Hyena is motivated by a quality gap between standard dense attention and alternative subquadratic operators, which the authors identify by focusing on reasoning tasks correlated with language modeling performance at scale. They extend the suite of basic mechanistic interpretability benchmarks (*induction* and *recall*) with additional tasks that probe how quickly model performance degrades when task complexity increases (e.g. vocabulary size grows). They also investigate the optimal parameterization of long convolutions in Hyena. In the most challenging settings with hundreds of thousands of tokens, their implicit parameterization scheme improves over other operators leveraging state spaces (Gu et al., 2021), frequency-domain parametrizations (Li et al., 2020), or standard convolutions by over 50% accuracy. [p. 2-3]

## Scaling in Language and Vision

[p. 3]

The authors test Hyena on autoregressive language modeling at the sub-billion parameter scale, setting a new state-of-the-art for dense-attention-free architectures in standard datasets (WikiText103 and The Pile) and matching Transformer quality. On The Pile at the 335M parameter scale, they match Transformer perplexity with a 20% reduction in the total count of *floating point operations* (FLOPs). As an extension, they investigate the generality of Hyena operators by testing on large-scale image recognition, replacing attention in the Vision Transformer (ViT) (Dosovitskiy et al., 2020). In image classification, Hyena is able to match attention in accuracy when training on ImageNet-1k from scratch. [p. 3]

## Toward Much Longer Context

[p. 3]

The authors benchmark the efficiency of Hyena on long sequences. They measure 5x speedups over dense self-attention at length 8192 -- 2x over highly optimized FlashAttention (Dao et al., 2022b) -- and 100x speedup over FlashAttention at sequence lengths of 64k, where standard attention implementation in PyTorch runs out of memory. (Footnote 2: FlashAttention is already 2-4x faster than a standard attention implementation in PyTorch.) [p. 3]
