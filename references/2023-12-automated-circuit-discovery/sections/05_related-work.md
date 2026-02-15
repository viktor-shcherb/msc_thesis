# 5 Related work [p. 8-9]

[p. 8-9] The section connects ACDC to four literatures:

## Mechanistic interpretability and circuits
- Feature/circuit discovery in vision and language models.
- Transformer-specific mathematical circuit framework and path decomposition.
- Circuit-level analyses used for editing/testing hypotheses in models.

## Pruning and subnetworks
- Classical pruning/compression targets speed/storage.
- ACDC is contrasted as an interpretability-first objective (task-conditioned causal subgraphs), not model compression for deployment.

## Causal interpretation and interventions
- Causal inference framing for language-model internals.
- Activation/path patching viewed as intervention-based attribution.
- ACDC framed as **finding** candidate circuits; separate methods can test rich causal hypotheses.

## Computational subgraph viewpoints
- Residual-path and component-level decomposition work supports subgraph reasoning.
- The paper positions ACDC as an operational search procedure over those subgraphs.
