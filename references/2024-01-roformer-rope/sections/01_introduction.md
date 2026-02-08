# Introduction [p. 1–2]

[p. 1] The sequential order of words is of great value to natural language understanding. Recurrent neural networks (RNNs) encode tokens' order by recursively computing a hidden state along the time dimension. Convolution neural networks (CNNs) were typically considered position-agnostic (Gehring et al. [2017]), but recent work (Islam et al. [2020]) has shown that the commonly used padding operation can implicitly learn position information. Recently, pre-trained language models (PLMs), built upon the transformer (Vaswani et al. [2017]), have achieved state-of-the-art performance on various NLP tasks, including context representation learning (Devlin et al. [2019]), machine translation (Vaswani et al. [2017]), and language modeling (Radford et al. [2019]). Unlike RNNs and CNNs-based models, PLMs utilize the self-attention mechanism to semantically capture the contextual representation of a given corpus. PLMs achieve a significant improvement in terms of parallelization over RNNs and improve the modeling ability of longer intra-token relations compared to CNNs.

Footnote 1: A stack of multiple CNN layers can also capture longer intra-token relation; here the paper considers only the single layer setting. [p. 1]

[p. 2] The self-attention architecture of current PLMs has shown to be position-agnostic (Yun et al. [2020]). Various approaches have been proposed to encode position information into the learning process:

- **Absolute position encoding (additive):** generated through a pre-defined function (Vaswani et al. [2017]) added to contextual representations, or as a trainable absolute position encoding (Gehring et al. [2017], Devlin et al. [2019], Lan et al. [2020], Clark et al. [2020], Radford et al. [2019], Radford and Narasimhan [2018]).
- **Relative position encoding:** previous work (Parikh et al. [2016], Shaw et al. [2018], Huang et al. [2018], Dai et al. [2019], Yang et al. [2019], Raffel et al. [2020], Ke et al. [2020], He et al. [2020], Huang et al. [2020]) encodes relative position information into the attention mechanism.
- **Other approaches:** Liu et al. [2020] model the dependency of position encoding from the perspective of Neural ODE, Chen et al. [2018a] model position in complex space, Wang et al. [2020] also model position in complex space.

Despite the effectiveness of these approaches, they commonly add the position information to the context representation and thus render them unsuitable for the linear self-attention architecture. [p. 2]

## Contributions

The paper introduces Rotary Position Embedding (RoPE) to leverage positional information in PLMs. RoPE encodes the absolute position with a rotation matrix and meanwhile incorporates the explicit relative position dependency in self-attention formulation. The proposed RoPE is prioritized over existing methods through valuable properties including: sequence length flexibility, decaying inter-token dependency with increasing relative distances, and the capability of equipping linear self-attention with relative position encoding. [p. 2]

Three-fold contributions stated: [p. 2]

1. Investigated existing approaches to relative position encoding and found they are mostly built on decomposing the addition of position encoding to context representations. Introduce RoPE: the key idea is to encode relative position by multiplying context representations with a rotation matrix with a clear theoretical interpretation.

2. Study the properties of RoPE and show it decays with relative distance increased, which is desired for natural language encoding. Argue that previous relative position encoding approaches are not compatible with linear self-attention.

3. Evaluate RoFormer on various long text benchmark datasets, showing it consistently achieves better performance compared to alternatives. Pre-trained language models available on GitHub: https://github.com/ZhuiyiTechnology/roformer.

## Paper Organization

The paper establishes a formal description of the position encoding problem in self-attention architecture and revisits previous works in Section 2. The rotary position encoding (RoPE) and its properties are described in Section 3. Experiments are reported in Section 4. The paper concludes in Section 5. [p. 2]
