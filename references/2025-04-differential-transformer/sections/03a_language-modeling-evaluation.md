# 3.1 Language Modeling Evaluation [p. 4]

## Setup [p. 4]

The authors train 3B-size DIFF Transformer language models on 1T tokens and compare with previous well-trained Transformer-based models (Geng & Liu, 2023; Liu et al., 2023; Tow, 2023; Tow et al., 2023) in various downstream tasks [p. 4]. As described in Appendix B, they follow the same setting to train a 3B-size Transformer language model on 350B tokens [p. 4]. The checkpoints are also used in the following experiments and analysis to ensure fair comparisons [p. 4].

The authors follow a similar recipe as StableLM-3B-4E1T (Tow et al., 2023) [p. 4]. They set hidden size to 3072 [p. 4]. The number of layers is 28 [p. 4]. The head dimension d is 128 [p. 4]. The number of heads is 24 for Transformer and 12 for DIFF Transformer, to align computation FLOPs and model size [p. 4]. The total parameter count is about 2.8B [p. 4]. The training sequence length is 4096 [p. 4]. The batch size is 4M tokens [p. 4].

They train the models with 1T tokens [p. 4]. They use AdamW (Loshchilov & Hutter, 2019) optimizer with β = 0.9, 0.95 [p. 4]. The maximal learning rate is 3.2e-4 with 1000 warmup steps and linearly decays to 1.28e-5 [p. 4]. The training corpus also follows StableLM-3B-4E1T (Tow et al., 2023) [p. 4]. They employ tiktoken-cl100k_base tokenizer (OpenAI) [p. 4]. Detailed hyperparameters are in Appendix D [p. 4].

## Results [p. 4]

Table 1 reports the zero-shot results on the LM Eval Harness benchmark (Gao et al., 2023) [p. 4]. The authors compare DIFF Transformer with well-trained Transformer-based language models, including OpenLLaMA-v2-3B (Geng & Liu, 2023), StableLM-base-alpha-3B-v2 (Tow, 2023), and StableLM-3B-4E1T (Tow et al., 2023) [p. 4]. OpenLLaMA-v2-3B and StableLM-base-alpha-3B-v2 are also trained with 1T tokens [p. 4]. The 1T results of StableLM-3B-4E1T are taken from its technical report (Tow et al., 2023) [p. 4].

Experimental results show that DIFF Transformer achieves favorable performance compared to previous well-tuned Transformer language models [p. 4]. In addition, Appendix B shows that DIFF Transformer outperforms Transformer across various tasks, where they use the same setting to train the 3B-size language models for fair comparisons [p. 4].

| Model | ARC-C | ARC-E | BoolQ | HellaSwag | OBQA | PIQA | WinoGrande | Avg |
|-------|-------|-------|-------|-----------|------|------|------------|-----|
| *Training with 1T tokens* | | | | | | | | |
| OpenLLaMA-3B-v2 (Geng & Liu, 2023) | 33.9 | 67.6 | 65.7 | 70.0 | 26.0 | 76.7 | 62.9 | 57.5 |
| StableLM-base-alpha-3B-v2 (Tow, 2023) | 32.4 | 67.3 | 64.6 | 68.6 | 26.4 | 76.0 | 62.1 | 56.8 |
| StableLM-3B-4E1T (Tow et al., 2023) | - | 66.6 | - | - | - | 76.8 | 63.2 | - |
| DIFF-3B | 37.8 | 72.9 | 69.0 | 71.4 | 29.0 | 76.8 | 67.1 | 60.6 |

Table 1: Eval Harness (Gao et al., 2023) accuracy compared with well-trained Transformer language models (Tow et al., 2023; Tow, 2023; Geng & Liu, 2023) [p. 4]. The authors scale the 3B model to 1 trillion training tokens [p. 4]. The 1T results of StableLM-3B-4E1T are taken from its technical report Tow et al. (2023) [p. 4].
