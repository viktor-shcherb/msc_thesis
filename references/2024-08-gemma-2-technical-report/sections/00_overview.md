# Overview

**Title:** Gemma 2: Improving Open Language Models at a Practical Size

**Authors:** Gemma Team, Google DeepMind

**Affiliations:** Google DeepMind (see Contributions and Acknowledgments section for full author list)

**Venue:** arXiv preprint (arXiv:2408.00118v3)

**Date:** 2024-06-27 (arXiv revised 2024-10-02)

## Abstract

> "In this work, we introduce Gemma 2, a new addition to the Gemma family of lightweight, state-of-the-art open models, ranging in scale from 2 billion to 27 billion parameters. In this new version, we apply several known technical modifications to the Transformer architecture, such as interleaving local-global attentions (Beltagy et al., 2020a) and group-query attention (Ainslie et al., 2023). We also train the 2B and 9B models with knowledge distillation (Hinton et al., 2015) instead of next token prediction. The resulting models deliver the best performance for their size, and even offer competitive alternatives to models that are 2-3x bigger. We release all our models to the community." [p. 1]

## Section Headings

1. Introduction
2. Model Architecture
3. Pre-training
   - 3.1. Training Data
   - 3.2. Knowledge Distillation
   - 3.3. Compute Infrastructure
   - 3.4. Carbon Footprint
4. Post-Training
5. Ablations
6. Evaluation
   - 6.1. Pre-training Evaluations
   - 6.2. Post-training Evaluations
7. Memorization and Privacy
8. Responsibility, Safety, Security
   - 8.1. Impact Assessment
   - 8.2. Safety Policies and Train-time Mitigations
   - 8.3. External Benchmark Evaluations
   - 8.4. Assurance Evaluations
   - 8.5. Our approach to responsible open models
9. Discussion and Conclusion
10. Contributions and Acknowledgments
References
