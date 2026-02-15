# 1 Introduction [p. 1-2]

[p. 1] The paper frames a scaling bottleneck in mechanistic interpretability: existing circuit-discovery workflows require heavy manual inspection, which does not scale to larger models or behaviors composed of many interacting sub-circuits.

[p. 1] The authors position mechanistic interpretability as reverse-engineering model components into human-understandable algorithms, and define circuits as computational subgraphs with distinct functionality.

[p. 1-2] Core contributions stated in the introduction:

1. A systematized workflow used across prior mechanistic interpretability papers.
2. A new algorithm, **Automatic Circuit DisCovery (ACDC)**, to automate the edge-selection stage of circuit extraction.
3. Adaptations of Subnetwork Probing (SP) and Head Importance Score for Pruning (HISP) for circuit extraction comparisons.
4. Quantitative evaluation metrics for subgraph recovery quality.

**Figure 1** (p. 2): "Automatically discovering circuits with ACDC"
- Left panel: GPT-2 Small computational graph with recovered IOI circuit edges highlighted.
- Right panel: compact recovered circuit with labeled nodes.
- Reported qualitative claim: all highlighted heads match the manually identified IOI circuit components from prior work.

[p. 2] The paper explicitly separates two activities:
- Discovering a compact causal subgraph (automated here).
- Interpreting the semantic function of recovered components (left largely to human analysis).
