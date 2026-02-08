# 6 Clustering Attention Heads [p. 8-9]

The authors investigate whether attention heads in the same layer are similar to each other and whether attention heads can be clearly grouped by behavior. They compute the distances between all pairs of attention heads. [p. 8]

## Distance metric

Formally, the distance between two heads H_i and H_j is measured as:

$$\sum_{\text{token} \in \text{data}} JS(H_i(\text{token}), H_j(\text{token}))$$

Where JS is the Jensen-Shannon Divergence between attention distributions. [p. 8]

## Visualization

Using these distances, the authors visualize the attention heads by applying multidimensional scaling (Kruskal, 1964) to embed each head in two dimensions such that the Euclidean distance between embeddings reflects the Jensen-Shannon distance between the corresponding heads as closely as possible. [p. 8]

## Results

**Figure 6** (p. 8): "BERT attention heads embedded in two-dimensional space. Distance between points approximately matches the average Jensen-Shannon divergences between the outputs of the corresponding heads. Heads in the same layer tend to be close together. Attention head 'behavior' was found through the analysis methods discussed throughout this paper."

The figure contains two panels:
- **Top panel (Behaviors):** Color-coded by behavior type. Identified clusters include: attend broadly (green squares), attend to next (orange triangles), attend to prev. (blue left-triangles), attend to [CLS] (dark squares), attend to [SEP] (dark circles), and attend to period/comma (gray circles). Named behavioral clusters are labeled: "Coreference," "Object of prep.," "Direct object," "Possessive," "Determiner," and "Passive auxiliary." [p. 8]
- **Bottom panel (Colored by Layer):** Same embedding colored by layer number (1-12). Heads within the same layer are often fairly close to each other, meaning heads within the layer have similar attention distributions. [p. 8]

Key findings: [p. 8-9]
- There are several clear clusters of heads that behave similarly, often corresponding to behaviors discussed earlier in the paper (e.g., attending to next token, attending to [SEP], specific syntactic relations).
- Heads within the same layer are often fairly close to each other, meaning that heads within the layer have similar attention distributions.
- This finding is a bit surprising given that Tu et al. (2018) show that encouraging attention heads to have different behaviors can improve Transformer performance at machine translation.
- One possibility for the apparent redundancy in BERT's attention heads is the use of attention dropout, which causes some attention weights to be zeroed-out during training. [p. 9]
