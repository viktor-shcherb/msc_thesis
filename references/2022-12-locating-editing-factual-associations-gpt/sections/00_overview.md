# Overview [p. 1-35]

## Paper Metadata

- **Title:** Locating and Editing Factual Associations in GPT
- **Authors:** Kevin Meng, David Bau, Alex Andonian, Yonatan Belinkov
- **Affiliations:** MIT CSAIL; Northeastern University; Technion - IIT
- **Venue:** 36th Conference on Neural Information Processing Systems (NeurIPS 2022)
- **Pages:** 35

## Abstract (verbatim)

> We analyze the storage and recall of factual associations in autoregressive transformer language models, finding evidence that these associations correspond to localized, directly-editable computations. We first develop a causal intervention for identifying neuron activations that are decisive in a model's factual predictions. This reveals a distinct set of steps in middle-layer feed-forward modules that mediate factual predictions while processing subject tokens. To test our hypothesis that these computations correspond to factual association recall, we modify feed-forward weights to update specific factual associations using Rank-One Model Editing (ROME). We find that ROME is effective on a standard zero-shot relation extraction (zsRE) model-editing task, comparable to existing methods. To perform a more sensitive evaluation, we also evaluate ROME on a new dataset of counterfactual assertions, on which it simultaneously maintains both specificity and generalization, whereas other methods sacrifice one or another. Our results confirm an important role for mid-layer feed-forward modules in storing factual associations and suggest that direct manipulation of computational mechanisms may be a feasible approach for model editing. The code, dataset, visualizations, and an interactive demo notebook are available at https://rome.baulab.info/.

## Section Headings

- 1 Introduction
- 2 Interventions on Activations for Tracing Information Flow
- 2.1 Causal Tracing of Factual Associations
- 2.2 Causal Tracing Results
- 2.3 The Localized Factual Association Hypothesis
- 3 Interventions on Weights for Understanding Factual Association Storage
- 3.1 Rank-One Model Editing: Viewing the Transformer MLP as an Associative Memory
- 3.2 Evaluating ROME: Zero-Shot Relation Extraction (zsRE)
- 3.3 Evaluating ROME: Our COUNTERFACT Dataset
- 3.4 Confirming the Importance of Decisive States Identified by Causal Tracing
- 3.5 Comparing Generation Results
- 3.6 Human Evaluation
- 3.7 Limitations
- 4 Related Work
- 5 Conclusion
- 6 Ethical Considerations
- Acknowledgements
- References
- Appendix A: Solving for Lambda Algebraically
- Appendix B: Causal Tracing
- Appendix C: Details on the zsRE Evaluation Task
- Appendix D: Details on the COUNTERFACT Dataset
- Appendix E: Method Implementation Details
- Appendix F: Extended Quantitative Results
- Appendix G: Generation Examples
- Appendix H: Dataset Samples
- Appendix I: Are Attention Weight Interventions Effective?
- Appendix J: Human Evaluation
