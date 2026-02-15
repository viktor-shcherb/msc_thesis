# Appendix I: tracr tasks details and qualitative evidence [p. 30]

[p. 30] Two toy compiled-transformer tasks are analyzed:
- `tracr-xproportion`
- `tracr-reverse`

Setup note:
- Corrupted inputs are generated via random permutations without fixed points.
- Positional embedding randomization in corrupted inputs is required to recover some position-dependent circuit elements.

[p. 30] The appendix reports clean recovery behavior on these small compiled models, and includes visualizations at finer granularity (including neuron/residual-component views) for interpretability of recovered subgraphs.
