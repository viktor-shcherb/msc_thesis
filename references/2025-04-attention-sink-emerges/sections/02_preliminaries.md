# Preliminaries on LMs and attention sink [p. 2-3]

## LM formulation [p. 2]

Let $f_θ$ be an auto-regressive LM with $L$ transformer decoder blocks and $\mathbf{X} \in \mathbb{R}^{T \times |\mathcal{V}|} := \{x_1, x_2, \ldots, x_T\}$ are the input tokens, where $x_i$ is a one-hot encoding and $|\mathcal{V}|$ is the vocabulary size of tokenizer $\mathcal{V}$. The LM output is also a sequence $\mathbf{Y} \in \mathbb{R}^{T \times |\mathcal{V}|} := \{y_1, y_2, \ldots, y_T\} = f_θ(\mathbf{X})$, where $y_t$ represents the predicted logits of $p(x_{t+1}|x_{\leq t})$ [p. 2].

## Transformer blocks [p. 2]

In the forward pass, $\mathbf{X}$ is first embedded as $\mathbf{H}^0 \in \mathbb{R}^{T \times d} := \mathbf{X}\mathbf{W}_E + \mathbf{P}$, where $\mathbf{W}_E \in \mathbb{R}^{|\mathcal{V}| \times d}$ is the learnable word embedding, $\mathbf{P} \in \mathbb{R}^{T \times d}$ is the positional embedding, and $d$ is the hidden dimension. We denote $\mathbf{H}^{l-1} \in \mathbb{R}^{T \times d} := \{h_1^l, h_2^l, \ldots, h_T^l\}$, $1 \leq l \leq L$ to be the output of the $l$-th block. Each block comprises a multi-head self-attention (MHSA) operation and a feed-forward network (FFN). The block has either a pre-norm or post-norm structure according to the location of layer normalization (LN) (Ba et al., 2016; Zhang & Sennrich, 2019). Most of LLMs consider a pre-norm block, as also shown in Figure 1(*Left*) [p. 2]:

$$\mathbf{H}^l = \text{FFN}(\text{LN}(\mathbf{O}^l + \mathbf{H}^{l-1})) + \mathbf{O}^l + \mathbf{H}^{l-1}, \quad \mathbf{O}^l = \text{MHSA}(\text{LN}(\mathbf{H}^{l-1})),$$
(2)

while the post-norm transformer block is

$$\mathbf{H}^l = \text{LN}(\text{FFN}(\text{LN}(\mathbf{O}^l + \mathbf{H}^{l-1})) + \text{LN}(\mathbf{O}^l + \mathbf{H}^{l-1})), \quad \mathbf{O}^l = \text{MHSA}(\mathbf{H}^{l-1}).$$
(3)

**Figure 1** (p. 2): "(*Left*) Architecture of pre-norm transformer block (we highlight the location of post-norm LN using dashed lines). We denote the output of MHSA as $\mathbf{O}^l$ and the output of FFN as $\mathbf{F}^l$. (*Right*) The packing strategy in the LM pre-training. All LM documents are concatenated with BOS (optional) and EOS tokens as the boundaries. Then it is chunked into equal-sized sequences with context length $C$."

Description: Architecture diagram showing transformer block structure
- Key elements: Left side shows pre-norm transformer block with FFN, MHSA, and layer normalization components; Right side shows document packing strategy with BOS/EOS tokens and chunking
- Notable patterns: Dashed lines indicate post-norm LN location; documents are concatenated and chunked into sequences of length C
- Supports claim: Illustrates the standard transformer architecture used in the experiments and the pre-training data packing methodology

## MHSA layers [p. 3]

In the MHSA layer, the input $\mathbf{H}^{l-1}$ are first transformed into keys, queries, and values: $\mathbf{K}^{l,h} = \mathbf{H}^{l-1}\mathbf{W}_K^{l,h}$, $\mathbf{Q}^{l,h} = \mathbf{H}^{l-1}\mathbf{W}_Q^{l,h}$, $\mathbf{V}^{l,h} = \mathbf{H}^{l-1}\mathbf{W}_V^{l,h}$ for each head $1 \leq h \leq H$ (we omit the notation of LN when considering pre-norm design for simplicity). Here $\mathbf{W}_K^{l,h}, \mathbf{W}_Q^{l,h}, \mathbf{W}_V^{l,h} \in \mathbb{R}^{d \times d_h}$, $d_h = d/H$. Then the attention output is computed as [p. 3]:

$$\mathbf{A}^{l,h} = \text{Softmax}(\mathbf{Q}^{l,h}\mathbf{K}^{l,h\top}/\sqrt{d_h} + \mathbf{M}), \quad \mathbf{O}^l = \text{Concat}_{h=1}^H(\mathbf{A}^{l,h}\mathbf{V}^{l,h})\mathbf{W}_O^l,$$
(4)

where $\mathbf{M} \in \mathbb{R}^{T \times T}$ is an attention mask. For vanilla causal attention, $M_{ij} = -\infty$ for $i < j$ and $M_{ij} = 0$ for $i \geq j$. Finally, the output of the last transformer block $\mathbf{H}^L$ is fed into an unembedding layer for prediction: $\mathbf{Y} = \text{LN}(\mathbf{H}^L)\mathbf{W}_{\text{cls}}$, where $\mathbf{W}_{\text{cls}} \in \mathbb{R}^{d \times |\mathcal{V}|}$ [p. 3].

## Positional embedding [p. 3]

NoPE (Kazemnejad et al., 2024) considered no explicit positional embedding (PE) in LMs, where $\mathbf{P} = \mathbf{0}$. When using absolute PE (Vaswani et al., 2017), $\mathbf{P}$ is a periodic function of token positions. Devlin et al. (2019); Brown et al. (2020) adopted a learnable PE, which means $\mathbf{P}$ is a learnable embedding of token positions. The dot product of queries and key meets $\langle q_i, k_j \rangle = q_i k_j^\top$ when using the above three PEs. While for relative PE (Raffel et al., 2020), ALiBi (Press et al., 2021), Rotary (Su et al., 2024), they have $\mathbf{P} = \mathbf{0}$. Instead, they modify the dot product $\langle q_i, k_j \rangle$. For relative PE and ALiBi, $\langle q_i, k_j \rangle = q_i k_j^\top - g(i - j)$, where $g(\cdot)$ is pre-defined function of the distance between two token positions. For Rotary, $\langle q_i, k_j \rangle = q_i \mathbf{R}_{\Theta_{i-j}} k_j^\top$, where $\mathbf{R}_{\Theta_{(\cdot)}}$ is a pre-defined rotation matrix. We include more formulations of the three PEs in Appendix B [p. 3].

## Auto-regressive objective [p. 3]

The pre-training objective of LMs is to maximize the likelihood of input data: $\theta^* = \arg\max_{\theta} \mathbb{E}_{\mathbf{X} \sim p_{\text{data}}} \left[\sum_{t=1}^T \log p_\theta(x_t | x_{<t})\right]$, where $p_{\text{data}}$ refers to the data distribution [p. 3].

## Packing documents in pre-training [p. 3]

Given a large corpus $\mathcal{D} = \{d_1, d_2, \cdots, d_{|\mathcal{D}|}\}$, where each $d_i$ represents a document containing a sequence of tokens. A packing strategy is adopted in the LM pre-training, as present in Figure 1(*Right*). All documents are concatenated and chunked into sequences with a context length of $C$. Each chunk could start with any token within one document or the BOS/EOS token. Then the empirical objective for each chunk is $\mathcal{L} = \sum_{t=2}^C \log p_\theta(x_t | x_{<t})$. We note that $p_\theta(x_1)$ is ignored since $y_1 = f_\theta(x_1)$ is the prediction for the next token $x_2$ [p. 3].

## LM inference [p. 3]

During the inference, a BOS token is fed into the model as the prefix for unconditional generation: $x_t' \sim p_\theta(x' | x_{<t}', x, \text{BOS})$, where $x$ is the $k$-th generated token, $x$ is the optional prompt. If there are no BOS tokens in the pre-training, the EOS token is considered as the BOS [p. 3].

## Attention sink [p. 3]

Xiao et al. (2023b) revealed that LLMs allocate significant attention scores to specific token positions, e.g. the first token (not necessary to be a BOS token), resulting in "vertical" attention patterns. To represent this, we have the attention scores $A_{i,1}^{l,h} \gg \text{mean}(A_{i,j \neq 1}^{l,h})$ [p. 3].

**Figure 2** (p. 3): "In LLaMA3-8B Base, (*Top*) the first token has significantly larger $\ell_2$-norm of hidden states, but much smaller $\ell_2$-norm of keys and values than the mean of other tokens; (*Bottom*) cosine similarity instead of norm product contributes to attention sink. We delay more visualizations to Appendix C.3."

Description: Heatmaps and line plots showing attention patterns and norms
- Key elements: Top row shows three line plots of $\ell_2$-norm for hidden states ($h_1^l$ vs $h_{l \neq 1}^l$), keys ($k_1^l$ vs $k_{l \neq 1}^l$), and values ($v_1^l$ vs $v_{l \neq 1}^l$) across blocks; Bottom row shows three heatmaps: $q_t^{l,h}k_1^{l,h\top}$ (marked "Sink"), $\cos(q_t^{l,h}, k_1^{l,h})$ (marked "Sink"), and $\|q_t^{l,h}\| \cdot \|k_1^{l,h}\|$ (marked "No Sink")
- Notable patterns: First token has significantly larger $\ell_2$-norm of hidden states (400 vs 240-320), but smaller norms for keys and values; cosine similarity shows high values leading to sink, while norm product does not
- Supports claim: Demonstrates that attention sink is driven by cosine similarity (angular alignment) rather than magnitude of key/query vectors
