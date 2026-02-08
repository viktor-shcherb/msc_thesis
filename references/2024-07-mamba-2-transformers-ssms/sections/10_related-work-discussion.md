# 10 Related Work and Discussion [p. 33–36]

[p. 33] The state space duality framework bridges connections between SSMs, structured matrices, and attention. The authors discuss in more depth the relations between SSD and these concepts more broadly, using ideas from each of the viewpoints, and suggest some directions that the SSD framework can be extended in future work.

## 10.1 State Space Models

[p. 34] Structured state space models can be characterized along the axes of:
1. Whether it is time-invariant or time-varying.
2. The dimensionality of the system.
3. The structure on the recurrent transitions $A$.

SSD can be described as a selective SSM with SISO dimensions and scalar-identity structure.

**Time Variance (Selectivity).** The original structured SSMs (S4) were linear time-invariant (LTI) systems (Gu 2023; Gu, Goel, and Re 2022) motivated by continuous-time online memorization (Gu, Dao, et al. 2020; Gu, Johnson, Goel, et al. 2021; Gu, Johnson, Timalsina, et al. 2023). Many variants of structured SSMs have been proposed (Dao, D. Y. Fu, et al. 2023; Gu, Gupta, et al. 2022; Gupta, Gu, and Berant 2022; Ma et al. 2023; J. T. Smith, Warrington, and Linderman 2023), including several that drop the recurrence and focus on the convolutional representation of LTI SSMs (D. Y. Fu et al. 2023; Y. Li et al. 2023; Poli et al. 2023; Qin, Han, Weixuan Sun, B. He, et al. 2023).

SSD is a time-varying structured SSM, also known as a **selective SSM** introduced in Mamba (Gu and Dao 2023). Selective SSMs are closely related to gating mechanisms of RNNs, including classical RNNs such as the LSTM (Hochreiter and Schmidhuber 1997) and GRU (J. Chung et al. 2014) as well as more modern variants such as the QRNN (Bradbury et al. 2016), SRU (Lei 2021; Lei et al. 2017), RWKV (B. Peng, Alcaide, et al. 2023), HGRN (Qin, Yang, and Zhong 2023), and Griffin (Botev et al. 2024; De et al. 2024). These RNNs differ in their parameterizations in various ways, most importantly in the lack of a state expansion.

**Dimensionality and State Expansion.** An important characteristic of SSD, shared by previous SSMs in its lineage (S4, H3, Mamba), is that it is a **single-input single-output (SISO)** system where input channels are processed independently. This leads to a much larger effective state size of ND where N is the SSM state size (also called state expansion factor) and D is the standard model dimension. Traditional RNNs either have N = 1 or are multi-input multi-output (MIMO) with dense $B, C$ matrices, either of which leads to a smaller state. While MIMO SSMs have been shown to work well in some domains (Lu et al. 2023; Orvieto et al. 2023; J. T. Smith, Warrington, and Linderman 2023), Mamba showed that state expansion is crucial for information-dense domains such as language. One of the main advantages of SSD is allowing for even larger state expansion factors without slowing down the model. Many subsequent works have since adopted state expansion (Section 10.4).

**Structure.** Compared to previous structured SSMs, the main restriction of SSD is on the expressivity of the state transitions $A_t$. More general SSMs, such as the case of diagonal $A_t$, have the same theoretical efficiency as SSD, but are less hardware-friendly. This is because the dual quadratic form loses its attention-like interpretation and becomes more difficult to compute. Thus compared to Mamba, SSD differs only in a slightly more restrictive form of diagonal $A_t$, and trades off this expressivity for improved hardware efficiency (and ease of implementation).

> "We hypothesize that it may be possible to refine our structured matrix algorithms to improve to the general diagonal SSM case as well." [p. 34]

## 10.2 Structured Matrices

[p. 34] The first viewpoint of the state space duality adopts the viewpoint of these models as **matrix sequence transformations** or "matrix mixers": sequence transformations (Definition 2.1) that can be represented as matrix multiplication (by a T x T matrix) along the sequence dimension T.

Several such matrix mixers have been proposed before, where the primary axis of variation is the representation of the matrix. These include MLP-Mixer (Tolstikhin et al. 2021) (unstructured matrix), FNet (Lee-Thorp et al. 2021) (Fourier Transform matrix), M2 (Dao, B. Chen, et al. 2022; Dao, Gu, et al. 2019; Dao, Sohoni, et al. 2020; D. Fu et al. 2024) (butterfly/monarch matrix), Toeplitz matrices (Poli et al. 2023; Qin, Han, Weixuan Sun, B. He, et al. 2023), and even more exotic structures (De Sa et al. 2018; Thomas et al. 2018).

An important characterization is that efficient (sub-quadratic) matrix sequence transformations are exactly those which have **structured matrix mixers**. A core result of the SSD framework is viewing SSMs as matrix mixers with a particular structure -- semiseparable matrices (Section 3). The linear vs. quadratic duality then takes the form of structured matrix multiplication vs. naive matrix multiplication.

[p. 35] The structure matrix representation led to the efficient SSD algorithm through block decompositions of particular semiseparable matrices (Section 6). The authors note that semiseparable matrices are well-studied in the scientific computing literature, and incorporating those ideas may be a promising avenue for more improvements to state space models. They also suggest that focusing on the matrix mixer viewpoint can lead to more fruitful directions for sequence models, such as designing principled non-causal variants of Mamba, or finding ways to characterize and bridge the gap between softmax attention and sub-quadratic models through analyzing their matrix transformation structure.

## 10.3 (Linear) Attention

[p. 35] Compared to standard (causal) attention, SSD has only two main differences.

First, SSD does not use the softmax activation of standard attention (Bahdanau, Cho, and Bengio 2015; Vaswani et al. 2017), which is what gives attention its quadratic complexity. When the softmax is dropped, the sequence can be computed with linear scaling through the linear attention framework (Katharopoulos et al. 2020).

Second, SSD multiplies the logits matrix by an input-dependent 1-semiseparable mask. Thus this mask can be viewed as replacing the softmax in standard attention.

This semiseparable mask can also be viewed as providing positional information. The elements $a_t$ act as "gates" in the RNN sense, or a "selection" mechanism (see discussion in Mamba paper), and their cumulative products $a_{j:i}$ control how much interaction is allowed between positions $i$ and $j$. Positional embeddings (e.g. sinusoidal (Vaswani et al. 2017), AliBi (Press, N. Smith, and Lewis 2022), and RoPE (Su et al. 2021)) are an important component of Transformers that are often viewed as heuristics, and the 1-SS mask of SSD can be seen as a more principled form of relative positional embeddings. The authors note that this view was also posited concurrently by GateLoop (Katsch 2023).

The second viewpoint of state space duality is a special case of the more general structured masked attention (SMA) framework, where the duality is revealed as different contraction orderings on a simple 4-way tensor contraction. SMA is a strong generalization of linear attention that is much more general than SSD as well; other forms of structured masks may lead to more variants of efficient attention with different properties than SSD.

Beside leading to new models, these connections to attention can lead to other directions for understanding SSMs. For example, the authors are curious whether the phenomenon of attention sinks (Darcet et al. 2024; Xiao et al. 2024) exist for Mamba models, and more broadly whether interpretability techniques can be transferred to SSMs (Ali, Zimerman, and Wolf 2024).

Finally, many other variants of linear attention have been proposed (Arora, Eyuboglu, Zhang, et al. 2024; Arora, Eyuboglu, Timalsina, et al. 2024; Choromanski et al. 2021; H. Peng et al. 2021; Qin, Han, Weixuan Sun, Dongxu Li, et al. 2022; Qin, Weixuan Sun, et al. 2022; Schlag, Irie, and Schmidhuber 2021; Zhang et al. 2024; Zheng, C. Wang, and Kong 2022) (see Section 4.1.3 for descriptions of several of these), and the authors expect that many techniques can be transferred to SSMs (e.g. Section 7.3).

> "We emphasize that SSD **does not generalize standard softmax attention**, or any other transformation on the attention kernel matrix that does not have a finite feature map $\psi$." [p. 35]

Compared to general attention, SSD's advantage is having a controllable state expansion factor N that compresses the history, compared to quadratic attention's cache of the entire history scaling with sequence length T >> N. Concurrent work has started studying the tradeoffs of these representations, for example on copying and in-context learning tasks (Akyurek et al. 2024; Grazzi et al. 2024; Jelassi et al. 2024; Park et al. 2024). The authors note that Mamba-2 significantly improves on Mamba on some of these capabilities (e.g. as demonstrated by MQAR results in Section 9.1), but more remains to be understood.

## 10.4 Related Models

[p. 35–36] The authors highlight a growing body of recent and concurrent work that have developed sequence models very similar to Mamba and Mamba-2.

- **RetNet** (Y. Sun et al. 2023) and **TransNormerLLM** (Qin, Dong Li, et al. 2023) generalize Linear Attention using decay terms instead of a cumulative sum, and propose dual parallel/recurrent algorithms as well as a hybrid "chunkwise" mode. These algorithms can be seen as an instantiation of SSD where $A_t$ is time-invariant (constant for all $t$); in the SMA interpretation, the mask matrix $L$ would be a decay matrix $L_{i,j} = \gamma^{i-j}$. These models also differ architecturally in various ways. For example, since they were derived from an attention-centric perspective they preserve the multi-head attention (MHA) pattern; since Mamba-2 was derived from an SSM-centric pattern it preserves the multi-value attention (MVA) or multi-expand SSM (MES) pattern, which the authors show to be better (Section 9.4).

- **GateLoop** (Katsch 2023) concurrently proposed using input-dependent decay factors $A_t$, and developed the same dual quadratic form as in SSD which they call a "surrogate attention" form.

- **Gated Linear Attention (GLA)** (Yang et al. 2024) proposed a variant of linear attention with data-dependent gates, along with efficient algorithms to compute a chunkwise mode and hardware-aware implementations.

- **HGRN** (Qin, Yang, and Zhong 2023) introduced an RNN with input-dependent gates, which was improved to incorporate state expansion in HGRN2 (Qin, Yang, Weixuan Sun, et al. 2024).

- **Griffin** (De et al. 2024) and **RecurrentGemma** (Botev et al. 2024) showed that an RNN with input-dependent gating, combined with local attention, can be very competitive with strong modern Transformers. Jamba also showed that combining Mamba with a few layers of attention performs very well on language modeling (Lieber et al. 2024).

- **xLSTM** (Beck et al. 2024) improves the xLSTM by adopting the idea of state expansion and other gating, normalization, and stabilization techniques.

- **RWKV(-4)** (B. Peng, Alcaide, et al. 2023) is an RNN based on a different linear attention approximation (the attention-free Transformer (S. Zhai et al. 2021)). It has recently been improved to the RWKV-5/6 (Eagle and Finch) architectures (B. Peng, Goldstein, et al. 2024) by adopting the ideas of selectivity and state expansion.
