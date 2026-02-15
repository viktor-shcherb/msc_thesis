# Introduction [p. 1-2]

## Problem framing [p. 1]

The paper introduces **Ministral 3**, a family of dense models designed for compute- and memory-constrained applications. The authors position their work against large pretraining budgets, stating that Qwen3 and Llama3 are trained on approximately **36T** and **15T** tokens, respectively, while Ministral 3 models are trained with **1T-3T** tokens by leveraging distillation from Mistral Small 3.1 (24B) [Yang et al., 2025; Dubey et al., 2024].

The model family includes three parameter scales (3B, 8B, 14B) and three variants per scale:

1. Base
2. Instruct
3. Reasoning

All variants include image understanding, and base/instruct models support context lengths up to **256K** tokens (reasoning models: **128K**) [p. 1].

## High-level claim [p. 1]

The main efficiency claim is that cascade pruning + distillation can produce models competitive with stronger-budget systems:

- Ministral 3 14B Base is described as "more than 40% smaller" than Mistral Small 3.1 Base while remaining close in quality [p. 1].
- Post-trained variants are compared to similarly sized open-weight models from Gemma 3 and Qwen 3 [Kamath et al., 2025; Yang et al., 2025; Bai et al., 2025].

## Stated contributions [p. 2]

The paper lists three explicit contributions:

1. A public release of **9 dense open-weight models** (3 sizes x 3 variants) under Apache 2.0.
2. A compute-efficient pretraining recipe (**Cascade Distillation**) that reduces cost versus separate pretraining runs from scratch.
3. Replication/confirmation of prior distillation observations:
   - stronger teacher can hurt pretraining distillation,
   - post-trained teacher can be better than base teacher during pretraining distillation,
   - preference-tuned teacher can outperform SFT-only teacher for student post-training [p. 2].

## Key citations introduced in this section

- [Yang et al., 2025] Qwen3 technical report
- [Dubey et al., 2024] Llama 3 technical report
- [Kamath et al., 2025] Gemma 3 technical report
- [Bai et al., 2025] Qwen3-VL technical report
