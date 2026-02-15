# Discussions [p. 8-10]

## 5.1 Choice of teacher model for distillation [p. 8-9]

### Figure 3 [p. 8]

**Figure 3** (p. 8): "Ministral 3 14B pretraining ablations comparing distillation from Mistral Small 3.1 and Mistral Medium 3 teachers. Despite Mistral Medium 3 being larger and more capable, distillation from Mistral Small 3.1 consistently yields stronger downstream performance across different benchmarks."

Description:
- Ablation plot comparing two teacher choices for 14B pretraining.
- Direction of effect in caption/text: Smaller teacher (MS3.1) outperforms stronger teacher (Medium 3) for this stage.

### Figure 4 [p. 9]

**Figure 4** (p. 9): "Ministral 3 3B pretraining ablations comparing distillation from base and post-trained (instruct/reasoning) variants of Mistral Small 3.1. The instruct teacher yields stronger performance on STEM benchmarks, while achieving comparable results on knowledge and multimodal evaluations."

Description:
- Base-vs-instruct/reasoning teacher ablation for 3B pretraining.
- Text interpretation emphasizes stronger gains on math/code and smaller effects on knowledge tasks.

Key discussion claims [p. 8-9]:

1. **Stronger teacher is not always better for pretraining distillation.**
2. **Post-training distillation benefits from stronger teacher models.**
3. **Teacher variant matters:** post-trained teacher beats base teacher during student pretraining.
4. **Preference-tuned teachers outperform SFT-only teachers for student SFT distillation.**

## 5.2 Model verbosity [p. 9-10]

### Figure 5 [p. 9]

**Figure 5** (p. 9): "Verbosity (in terms of number of output tokens) v.s. accuracy on GPQA Diamond with Ministral 3 instruction-following and reasoning."

Description:
- Scatter/curve-style comparison between response length (verbosity) and GPQA accuracy.
- Used to motivate a tradeoff between long-chain reasoning behavior and chat naturalness.

The paper reports that adding larger fractions of long CoT traces in SFT improves STEM performance but can induce undesirable general-chat behavior (reflection loops, internal monologues, backtracking) [p. 10].

Example snippet included in paper [p. 10]:

- A long, self-reflective solution trace ending with: `21 + 49 = 70`.

## 5.3 ODPO for Ministral 3 reasoning [p. 10]

### Figure 6 [p. 10]

**Figure 6** (p. 10): "Impact of ODPO on chat benchmarks for Ministral 3 reasoning models, applied on top of GRPO-trained checkpoints. ODPO delivers substantial gains across all benchmarks for the 14B and 8B variants."

Description:
- Post-RL alignment comparison before/after ODPO.
- Clear gain claim for 14B and 8B.
- 3B shows weaker public-benchmark gains, with authors noting improvement in internal human evaluation.

Additional note [p. 10, footnote 4]:
- 3B is more sensitive to fine-tuning hyperparameters than 8B/14B.
