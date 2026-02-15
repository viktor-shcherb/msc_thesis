# Introduction [p. 1-2]

[p. 1-2] The paper asks where factual associations are stored in GPT-like autoregressive transformers and proposes that they are implemented as localized computations that can be directly edited.

[p. 1] Example motivating prompt: "The Space Needle is located in the city of" -> "Seattle".

[p. 1] The authors position the work against prior factual probing and knowledge editing work in both autoregressive and masked LMs, emphasizing that GPT's unidirectional attention/generation setup motivates separate analysis from BERT-style studies.

[p. 1-2] Two-step program introduced:

1. **Causal tracing** of hidden-state activations to identify decisive internal computations for factual recall.
2. **Rank-One Model Editing (ROME)** to edit factual associations in weights and test the causal hypothesis.

[p. 2] Claimed empirical summary:

- ROME is competitive on zsRE model-editing benchmarks.
- On the new COUNTERFACT benchmark, ROME maintains both specificity and generalization better than compared baselines.
- Mid-layer MLP modules are implicated as key factual-association sites.

**Figure 1** (p. 2): "Causal Traces compute the causal effect of neuron activations..."
- Description: pipeline diagram comparing clean run, corrupted run, and corrupted-with-restoration run.
- Key elements: subject corruption at embedding stage; selective hidden-state patching; output recovery measurement.
- Supports claim: factual recall can be localized causally to specific hidden-state pathways.
