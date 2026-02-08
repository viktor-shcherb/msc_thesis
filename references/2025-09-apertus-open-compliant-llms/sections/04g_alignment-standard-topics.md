# 4.3.1 Alignment for Standard Topics [p. 33–34]

[p. 33] Existing preference datasets, reward models, and reward benchmarks broadly reflect quality criteria like correctness, helpfulness, and harmlessness (*e.g.*, Zhou et al., 2025a). For most topics, these dimensions of quality are uncontroversial, and previously-aggregated prompt datasets and reward models are drawn upon.

## Reward Model [p. 33]

[p. 33–34] For the non-controversial prompt-completion pairs (Section 4.1.4 above), rewards are assigned with a pretrained reward model. Specifically, `Skywork-Reward-V2-Llama-3.1-8B` (Liu et al., 2025a) is used, an 8B-parameter Llama 3.1 decoder finetuned on 26M preference pairs curated with a human-AI annotation pipeline. As of summer 2025, it ranks highly on reward model benchmarks (Liu et al., 2025a).

[p. 34] The model is applied to the dataset of non-controversial prompts with associated completions. The outputted rewards and associated rankings are then brought in to align Apertus using QRPO in an offline/off-policy regime.
