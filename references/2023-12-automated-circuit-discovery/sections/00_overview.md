# Overview

**Title:** Towards Automated Circuit Discovery for Mechanistic Interpretability

**Authors:** Arthur Conmy, Augustine N. Mavor-Parker, Aengus Lynch, Stefan Heimersheim, Adrià Garriga-Alonso

**Affiliations:** Arthur Conmy (Independent); Augustine N. Mavor-Parker (UCL); Aengus Lynch (UCL); Stefan Heimersheim (University of Cambridge); Adrià Garriga-Alonso (FAR AI)

**Venue:** 37th Conference on Neural Information Processing Systems (NeurIPS 2023), *Advances in Neural Information Processing Systems* 36

**Published:** December 15, 2023

## Abstract

> Through considerable effort and intuition, several recent works have reverse-engineered nontrivial behaviors of transformer models. This paper systematizes the mechanistic interpretability process they followed. First, researchers choose a metric and dataset that elicit the desired model behavior. Then, they apply activation patching to find which abstract neural network units are involved in the behavior. By varying the dataset, metric, and units under investigation, researchers can understand the functionality of each component.
>
> We automate one of the process' steps: finding the connections between the abstract neural network units that form a circuit. We propose several algorithms and reproduce previous interpretability results to validate them. For example, the ACDC algorithm rediscovered 5/5 of the component types in a circuit in GPT-2 Small that computes the Greater-Than operation. ACDC selected 68 of the 32,000 edges in GPT-2 Small, all of which were manually found by previous work. Our code is available at https://github.com/ArthurConmy/Automatic-Circuit-Discovery. [p. 1]

## Section headings

- 1 Introduction [p. 1]
- 2 The Mechanistic Interpretability Workflow [p. 2-4]
  - 2.1 Step 1: Select a behavior, dataset, and metric [p. 3]
  - 2.2 Step 2: Divide the neural network into a graph of smaller units [p. 3]
  - 2.3 Step 3: Patch model activations to isolate the relevant subgraph [p. 4]
  - 2.4 Explaining the circuit components [p. 4]
- 3 Automating circuit discovery (Step 3) [p. 5]
- 4 Evaluating Subgraph Recovery Algorithms [p. 6-8]
  - 4.1 Grounded in previous work: area under ROC curves [p. 6-7]
  - 4.2 Stand-alone circuit properties with a test metric [p. 8]
- 5 Related work [p. 8-9]
- 6 Conclusion [p. 9]
- 7 Acknowledgements [p. 10]
- References [p. 10-14]
- Appendix A-N [p. 15-35]
