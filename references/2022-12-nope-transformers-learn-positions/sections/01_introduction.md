# 1 Introduction [p. 1-2]

[p. 1] The attention mechanism (Bahdanau et al., 2015) of the transformer (Vaswani et al., 2017) is agnostic to the position and order of tokens in the input sequence. It is therefore common practice to inject positional information via absolute positional embeddings (Vaswani et al., 2017; Radford et al., 2018) or relative bias factors (Shaw et al., 2018; Raffel et al., 2020; Press et al., 2022).

The authors demonstrate that transformer language models *without* any explicit positional information can and do learn an implicit notion of absolute positions that is sufficient to achieve competitive performance.

They compare the performance of language models trained with no explicit positional information (*NoPos* language models) to those trained with three different position-aware mechanisms: sinusoidal embeddings (Vaswani et al., 2017), learned embeddings (Gehring et al., 2017), and ALiBi (Press et al., 2022). Results show that NoPos models are competitive with position-aware models consistently across datasets, model sizes, and input sequence lengths (e.g., Figure 1). [p. 1]

[p. 1-2] To shed light on their findings, the authors probe the position-awareness of NoPos language models, compared to models that use *relative* or *absolute* position mechanisms. Specifically, they train classifiers to predict the position of a token given its representation across different layers in the network. The NoPos model achieves similar mean absolute distance between the predicted and the expected positions, as a model with learned absolute position embeddings.

The authors hypothesize that this surprising behavior is tied to the *causal* attention mask, which implicitly injects positional information into the self-attention layer in order to preserve the autoregressive nature of language models. Intuitively, a model that is able to count the predecessors of a given token can essentially infer its absolute position. [p. 2] To test this hypothesis, they run similar experiments for masked language models (MLM) (Devlin et al., 2019), which use order-invariant attention (since no causal mask is applied). Indeed, bidirectional models fail to converge when position information is absent, substantiating their hypothesis.

## Contributions

The authors state their main contributions as: [p. 2]

- Demonstrating the robustness of the NoPos model (compared to position-aware models) with respect to model size, dataset, and sequence length.
- Providing an analysis of the trained NoPos model, showing that it encoded absolute positions.
- Showing that the success of NoPos models is unique to *causal* language models.
