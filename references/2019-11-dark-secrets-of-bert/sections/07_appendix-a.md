# A Examples of full self-attention maps [p. 11]

[p. 11] This appendix presents examples of full self-attention maps of a set of fine-tuned models to provide a better illustration of different head patterns. All the maps are given for a randomly sampled example from a corresponding dataset.

## Figure 10 (p. 11)

**Figure 10** (p. 11): Full self-attention maps for fine-tuned BERT models on four GLUE tasks: MRPC, STS-B, SST-2, and MNLI.

Each panel shows a 12 (layers) x 12 (heads) grid of individual self-attention maps. Each individual map is a token-by-token attention heatmap for a randomly sampled example. The maps illustrate the five attention patterns described in Section 4.1:

- **Diagonal patterns** (attention to previous/following tokens) are visible throughout, especially in middle and later layers.
- **Vertical stripe patterns** (attention to [CLS] and [SEP] tokens) are prominently visible, particularly in later layers (layers 6-12).
- **Block patterns** are evident in tasks with two input sentences (MRPC, STS-B, MNLI), showing intra-sentence attention.
- **Heterogeneous patterns** appear sporadically, more so in earlier layers.

The figure supports the claim from Section 4.1 that a limited set of attention patterns are repeated across different heads and layers, demonstrating the overparametrization of the BERT model.
