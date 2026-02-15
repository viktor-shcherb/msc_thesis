# Related Work [p. 2-3]

## Training Length-Extrapolatable Models

[p. 2] Length extrapolation: handling longer sequences than seen during training (Press et al., 2021). Referenced positional schemes include ALiBi (Press et al., 2021), xPos (Sun et al., 2023), and NoPos (Haviv et al., 2022).

[p. 2-3] RandPos (Ruoss et al., 2023) is positioned as similar in spirit (simulate longer sequence positions) but different in objective and setup:
- RandPos: encoder-only, pre-training-from-scratch setting, discontinuous adjacent-token positions.
- PoSE: decoder-only LLM fine-tuning for context extension, continuous intra-chunk positions to stay closer to pre-training positional structure.

## Fine-tuning LLMs for Longer Context

[p. 3] Direct long-context fine-tuning is reported to progress slowly (Chen et al., 2023a).

[p. 3] Position interpolation (PI) strategies cited for stabilization include:
- Linear interpolation (Chen et al., 2023a; kaiokendev, 2023)
- NTK interpolation (Peng and Quesnelle, 2023)
- YaRN (Peng et al., 2023)
- LongLoRA (Chen et al., 2023b)

[p. 3] PoSE is differentiated by **decoupling train and target lengths**, using only original context length during fine-tuning.

## Memory Transformer Alternatives

[p. 3] Two memory lines are discussed:
- Recurrence-based memory (Dai et al., 2019; Bulatov et al., 2022)
- Retrieval-based memory (Wu et al., 2022; Wang et al., 2023; Tworkowski et al., 2023)

[p. 3] Landmark Attention (Mohtashami and Jaggi, 2023) is cited for random access over long contexts. The paper contrasts PoSE as retaining full attention mechanism access over the entire input without modifying attention.
