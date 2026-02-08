# How Does NoPE Represent Positions? [p. 5-6]

[p. 5] The surprising performance of the NoPE model suggests that it captures useful positional information that can also generalize. The question is how it does so. The authors provide theoretical and empirical analysis towards answering this question.

## 5.1 NoPE can theoretically represent both absolute and relative PEs

[p. 5-6] Let $f_\theta$ be a NoPE decoder-only Transformer model, where $\theta$ denotes the model parameters. $f_\theta$ processes the input sequence $\mathbf{x} = [\langle\text{bos}\rangle, x_1, \ldots, x_T]$ by applying a series of layers. Note that since $f_\theta$ does not have any PE, the input $\mathbf{x}$ is not augmented with positional information (e.g. $[1, 2, \ldots, T]$). Each layer $l$, consisting of self-attention heads and a feed-forward sub-layer, reads the previous hidden state $\mathbf{H}^{(l-1)}$ and produces the hidden state at layer $l$: $\mathbf{H}^l$. Each head is parameterized by a query $\mathbf{W}_Q$, key $\mathbf{W}_K$, value $\mathbf{W}_V$, and output $\mathbf{W}_O$ matrices, where $\mathbf{W}_Q, \mathbf{W}_K, \mathbf{W}_V \in \mathbb{R}^{h \times d}$ and $\mathbf{W}_O \in \mathbb{R}^{d \times h}$, $d$ and $h$ are the model's hidden state size and attention dimension, respectively. $\mathbf{W}_1, \mathbf{W}_2 \in \mathbb{R}^{d \times k \cdot d}$ are the weight matrices of the feed-forward sub-layer.

**Theorem 1 (Absolute Encoding).** *Let $\mathbf{x}$ be an input sequence of length $T + 1$ to the model. Then, the first layer of $f_\theta$ can recover absolute positions $[1, \ldots, T + 1]$ in the hidden state $\mathbf{H}^{(1)}$. That is, there exist $\mathbf{W}_Q$, $\mathbf{W}_K$, $\mathbf{W}_V$, $\mathbf{W}_O$, $\mathbf{W}_1$, and $\mathbf{W}_2$ such that the self-attention and feedforward operations in the first layer compute absolute positions and write it to the next hidden state.* [p. 6]

The complete proof is in Appendix C.1. This theorem shows that stochastic gradient descent (SGD) can potentially learn to recover absolute positions in NoPE Transformers.

**Theorem 2 (Relative Encoding).** *Suppose that the hidden state $\mathbf{H}^{(1)}$ contains absolute positional information, as stated in Theorem 1, and assume that it is not overwritten by any subsequent layers. Then, the self-attention in all subsequent layers can implement a relative positional encoding: there exists a parameterization of $f_\theta$ such that, for $l \geq 2$, the attention dot product between query $\mathbf{q}_n$ and key $\mathbf{k}_m$ at positions $n$ and $m$ can be expressed as:*

$$\langle \mathbf{q}_n, \mathbf{k}_m \rangle = f_{\text{cnt}}(\mathbf{q}, \mathbf{k}) + f_{\text{rel}}(n - m) \tag{1}$$

*where $f_{\text{cnt}}$ is a function of their content, and $f_{\text{rel}}$ is a function of their relative distance.* [p. 6]

Appendix C.2 provides the complete proof of Theorem 2. The theoretical results suggest that SGD can choose between relative and absolute encoding in NoPE Transformers. But, what mechanism SGD learns in practice is not clear.

## 5.2 NoPE learns to use relative PE in practice

[p. 6] To explore the mechanisms that NoPE employs in practice, the authors conduct a quantitative analysis by comparing its attention pattern to models trained with different positional encoding techniques. The hypothesis is that if NoPE utilizes a similar algorithm to other PEs, then the attention patterns of these models should be quite similar.

To this end, the same input is fed to both models and, at layer $l$, the minimum distance between the attention distribution of any heads in the first model and any head in the second model is computed. Formally, let $\mathrm{P}_t = p(\mathbf{k}|\mathbf{q}_l)$ be a probability distribution produced by a causal self-attention head for query at position $t$, over the keys $\mathbf{k} \in [\mathbf{k}_1, \ldots \mathbf{k}_t]$ in a given transformer layer. Over a sequence of length $T$, the similarity between two heads P and Q is defined as $D_{\text{AT}}(\mathrm{P}, \mathrm{Q}) = \frac{1}{T} \sum_{t=1}^{T} D_{\text{JSD}}(\mathrm{P}_t \| \mathrm{Q}_t)$ which averages the Jensen-Shannon divergence (JSD) between the two heads over all positions. For the distance of two models $A$ and $B$ at layer $l$, the minimum distance is taken.

**Figure 4** (p. 6): "Distance of NoPE attention patterns with other positional encoding schemes measured across instances of SCAN dataset. The left figure shows the distance per layer, and the right figure shows the average distance across all layers. NoPE* denotes NoPE trained with a different seed."

The figure has two panels. The left panel contains 4 subplots (Layer #01 through Layer #04), each showing $D(\text{NoPE}, M)$ (y-axis, 0 to ~1.5) vs Example Length (x-axis, 0 to 50) for five PE methods: NoPE* (another seed), T5's Relative PE, ALiBi, Rotary, and Absolute Position Embedding. The right panel shows Average $D(\text{NoPE}, M)$ (y-axis, 0 to ~1.5) vs Example Length (x-axis, 0 to 50). Key observation: NoPE is closest to NoPE* (a different seed) and T5's Relative PE across all layers, while it is most distant from APE and Rotary. This supports the claim that NoPE learns attention patterns similar to T5's Relative PE in practice.

---
[p. 7 continued]

between all pairs of attention heads in the corresponding layer:

$$D^{(l)}(A, B) = \min_{(\mathrm{P}, \mathrm{Q}) \in A_l \times B_l} D_{\text{AT}}(\mathrm{P}, \mathrm{Q}) \tag{2}$$

where $A_l$ and $B_l$ are the attention heads in layer $l$ of models $A$ and $B$ respectively.

The authors empirically measure the distance between NoPE and other positional encoding schemes after training. Specifically, examples are sampled from each length bucket and fed (the concatenation of gold input and output) to compute the attention maps, with the distance calculated using Equation (2). The distance between different seeds of NoPE is also considered as a baseline.

Figure 4 shows the distance per layer for the first four layers (later layers show similar trends, Figure F.7). NoPE's attention patterns are most similar to that of T5's Relative PE, and least similar to APE and Rotary. The same trend can be observed across all layers and length buckets, and even when averaged across all layers.

> These results potentially suggest that a Transformer model without positional encoding, trained with stochastic gradient descent learns to represent positions in a way similar to T5's Relative PE, which is a relative positional encoding scheme. [p. 7]
