# 2.4 Ablations [p. 13]

### Table 3

**Table 3** (p. 13): **Apertus Architecture and Recipe Ablations.** For each major design choice, a separate ablation experiment is run on a 1.5B model scale with 100B tokens of the main datamix. The baseline is a standard Llama-style decoder with AdamW and a tuned cosine learning rate schedule. After verification, all successful changes are merged into a 3B model with 100B tokens, for which loss curves are provided in Figure 2. The loss values in the right column include a link to WandB report of the respective ablation experiment.

| Model | Modification | Loss |
|---|---|---|
| Baseline 1.5B | - | 2.037 |
| Baseline 1.5B | Prevent Cross Document Attention | 2.037 |
| Baseline 1.5B | Cosine -> WSD, Max LR 3e-4 -> 1.5e-4, 1-sqrt | 2.033 |
| Baseline 1.5B | AdamW -> AdEMAMix | 2.002 |
| Baseline 1.5B | SwiGLU -> xIELU, Hidden Dim 8192 -> 12288 | 1.997 |
| Baseline 3B | - | 1.906 |
| Apertus 3B | xIELU, AdEMAMix, QK-Norm, WSD & lower LR, Goldfish | **1.843** |

### Figure 2

**Figure 2** (p. 13): **Baseline Comparison with Final Apertus Architecture.** The authors merge all successful and intended changes to architecture and optimizer (xIELU activation, QK-Norm, AdEMAMix, WSD schedule with 1-sqrt annealing, cross-document attention, goldfish loss) into a 3B model, which they train for 100B tokens. Compared to a well-tuned baseline of a standard Llama model with cosine annealing, they achieve notable improvements in stability and gradient norms (right panel). Simultaneously, the model matches the final training loss of the baseline with 30-40% fewer tokens.

- Left panel ("3B Ablation: Loss Curves"): x-axis is Consumed Tokens (0.0B to 100.0B), y-axis is Loss (roughly 1.8 to 2.3). Apertus (blue) converges faster than Baseline (red), reaching roughly equal final loss (~1.84 vs ~1.91).
- Right panel ("3B Ablation: Gradient Norms"): x-axis is Consumed Tokens (0.0B to 100.0B), y-axis is Gradient Norms (0.0 to 0.6). Baseline (red) shows larger gradient norms especially early in training (~0.5), while Apertus (blue) maintains much lower and more stable gradient norms throughout (~0.1-0.2).

## Baseline

[p. 13]

To validate choices w.r.t. architecture and optimization recipe, the authors start from a well-tuned baseline of a 1.5B decoder transformer identical to standard Llama architecture (Grattafiori et al., 2024), trained on their main datamix with a cosine schedule. They use 100B tokens, which corresponds to roughly 48,000 steps at sequence length 4,096 and a batch size of 504 (2M tokens).

## Results

[p. 13]

The loss comparison of the main ablation runs is provided in Table 3. Compared to the baseline, which achieves a training loss of approximately 2.037, the changes to the cross document attention and the learning rate schedule match or slightly improve loss values. The most notable improvements are achieved individually by AdEMAMix (2.002) and xIELU (1.997).

After individually validating the changes, the authors merge all those that improve upon the baseline into a single model and training run to evaluate on a 3B scale. In summary, these changes include xIELU, QK-norms, the WSD schedule with a lower learning rate and a 1-sqrt cooldown, the cross-document attention masking, the Goldfish loss and the AdEMAMix optimizer. The resulting comparison is shown in Figure 2. Beyond stability improvements and lower gradient norms, the model achieves the same training loss with 30-40% fewer tokens, which thus becomes their final choice for pretraining.

## Evaluation of Recipe Performance with OLMo2

[p. 14]

### Table 4

**Table 4** (p. 14): **Apertus and OLMo2 Architecture Differences and Loss Comparison After 20k steps.** The authors compare to the OLMo2 architecture and training by replaying the exact same data of the first 20k steps with matching hyperparameters. Apertus achieves a similar loss with 46% and 30% fewer training tokens, respectively. The loss values contain links to the respective WandB reports.

| Model | Activation | Loss | Normalization | Optimizer | CE Loss after first 20k steps (1B) | CE Loss after first 20k steps (7B) |
|---|---|---|---|---|---|---|
| Apertus | xIELU | Goldfish | Pre Norm | AdEMAMix | ~2.75 | ~2.51 |
| OLMo2 | SwiGLU | Z-Loss | Reordered Norm | AdamW | ~2.84 | ~2.56 |

To evaluate their model architecture and training recipe beyond their own data and baselines, the authors compare Apertus against OLMo2's 1B and 7B models (OLMo et al., 2025) in a setup identical to their training. Specifically, to ensure a fair comparison, they match several hyperparameters, including model dimension, number of layers, batch size, cosine LR schedule, and multi-head attention. The key differences for this analysis are listed in Table 4. Because Apertus uses the xIELU activation, which is not a gated linear unit, they scale the MLP hidden dimension by 1.5x to match the compute and parameter count.

To reuse the exact tokenized sequences from OLMo2, they first run its data-loading pipeline and save the resulting tokens for training Apertus. The loss values after 20,000 iterations of replay with their recipe (40B tokens for 1B models, 80B tokens for 7B models) are shown in Table 4. Notably, the 1B variant of Apertus matches the loss of OLMo2 1B with 46% fewer tokens, while the 7B variant matches the loss of OLMo2 7B with 30% fewer tokens (loss curves not shown). The hyperparameters for this comparison are stable for OLMo2 7B, but lead to several loss spikes during warmup for Apertus 7B. Lowering the max LR with the AdEMAMix optimizer would reduce the number of loss spikes and further improve performance. The vocabulary size for Apertus runs (131k) had not been lowered to the OLMo2 value (100k), which is more favorable to the OLMo2 models since the larger vocabulary would lead to a higher average cross-entropy loss.
