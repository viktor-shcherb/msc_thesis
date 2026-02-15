# 3.2 Causal Attention and Position Embedding Are The Cause of Position Bias [p. 4]

Feed-forward networks (FFNs), Query, Key, and Value (QKV) projections, and layer normalization in the Transformer architecture do not cause position bias, as they yield the same representations regardless of document positions [p. 4]. Rather, the attention computation that leads to the position bias:

$$\mathbf{Q}_{pos} = \text{PE}(\mathbf{Q}, \text{pos}_{\mathbf{Q}}), \mathbf{K}_{pos} = \text{PE}(\mathbf{K}, \text{pos}_{\mathbf{K}})$$

$$\mathbf{H} = \text{Softmax}\left(\mathbf{Q}_{pos}\mathbf{K}_{pos}^T / \sqrt{d}\right) \odot \mathbb{I}_{\text{causal}} \mathbf{V}$$
(1)

where Q, K, V ∈ ℝⁿˣᵈ are queries, keys, and values, PE denotes the position encoding, pos_Q and pos_K denote the position of queries and keys, ⊙_causal denotes the causal attention mask [p. 4].

Eq. 1 reveals that:
1. The PE function yields different representations for documents if their orders changes, therefore affecting the importance score Q_pos K_pos^T of hidden states [p. 4]
2. The ⊙_causal generates different attention masks for the input documents if they change their positions, resulting in different hidden states [p. 4]

To achieve inter-document position-invariant inference, **H must remain the same regardless of documents' orders** [p. 4].
