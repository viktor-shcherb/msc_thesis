# Overview

**Title:** Ministral 3

**Authors:** Alexander H. Liu, Kartik Khandelwal, Sandeep Subramanian, Victor Jouault, et al.

**Affiliation:** Mistral AI

**Venue:** arXiv preprint (arXiv:2601.08584v1)

**Date:** 2026-01-13

## Abstract

> "We introduce the Ministral 3 series, a family of parameter-efficient dense language models designed for compute and memory constrained applications, available in three model sizes: 3B, 8B, and 14B parameters. For each model size, we release three variants: a pretrained base model for general-purpose use, an instruction finetuned, and a reasoning model for complex problem-solving. In addition, we present our recipe to derive the Ministral 3 models through Cascade Distillation, an iterative pruning and continued training with distillation technique. Each model comes with image understanding capabilities, all under the Apache 2.0 license." [p. 1]

## Section Headings

1. Introduction
2. Model Architecture
3. Training Recipe
   - 3.1 Pretraining
   - 3.2 Post-Training: Ministral Instruct
   - 3.3 Post-Training: Ministral Reasoning
4. Results
   - 4.1 Pretraining Results
   - 4.2 Post-training Results
5. Discussions
   - 5.1 Choice of Teacher Model for Distillation
   - 5.2 Model Verbosity
   - 5.3 ODPO for Ministral 3 Reasoning
6. Conclusion
References
