# 1 Introduction [p. 3-4]

## Figures

**Figure 1** (p. 3): "Helpfulness human evaluation results for Llama 2-Chat compared to other open-source and closed-source models."

Horizontal stacked bar chart showing % Win Rate (Win / Tie / Loss) for human evaluations on ~4k prompts (single and multi-turn). 95% confidence intervals between 1% and 2%. Results:

| Comparison | Win | Tie | Loss |
|---|---|---|---|
| Llama-2-70b-chat vs. ChatGPT-0301 | 35.9 | 31.5 | 32.5 |
| Llama-2-70b-chat vs. PaLM-Bison | 53.0 | 24.6 | 22.4 |
| Llama-2-34b-chat vs. Falcon-40b-instruct | 76.3 | 14.6 | 9.1 |
| Llama-2-34b-chat vs. Vicuna-33b-v1.3 | 37.2 | 31.6 | 31.2 |
| Llama-2-13b-chat vs. Vicuna-13b-v1.1 | 45.4 | 29.8 | 24.9 |
| Llama-2-7b-chat vs. MPT-7b-chat | 61.1 | 20.9 | 18.0 |

The authors note human evaluations can be noisy due to limitations of the prompt set, subjectivity of review guidelines, subjectivity of individual raters, and inherent difficulty of comparing generations. More details in Section 3.4.2.

**Figure 2** (p. 3): "Win-rate % for helpfulness and safety between commercial-licensed baselines and Llama 2-Chat, according to GPT-4."

Scatter plot with Helpfulness Win Rate (judge: GPT-4) on x-axis (0-60%) and Safety Win Rate on y-axis (0-60%). Green area indicates where Llama 2 is better. To remove ties, they used win/(win + loss). Model response orders presented to GPT-4 are randomly swapped to alleviate bias. Data points shown:
- ChatGPT-0301 vs. Llama 2 (70b): approximately 35% helpfulness, 45% safety
- PaLM-Bison vs. Llama 2 (70b): approximately 25% helpfulness, 20% safety
- Falcon-40b-instruct vs. Llama 2 (70b): approximately 10% helpfulness, 10% safety
- Llama 2-Chat models appear in the green (Llama 2 is better) region for most comparisons

Complements the human evaluation by using a more capable model (GPT-4), not subject to the authors' own guidance.

**Figure 3** (p. 4): "Safety human evaluation results for Llama 2-Chat compared to other open-source and closed-source models."

Bar chart showing Violation % (lower is safer) across ~2,000 adversarial prompts (single and multi-turn). Results (approximate from chart):
- Llama-2 7b-chat: ~4%
- Llama-2 13b-chat: ~4%
- Llama-2 34b-chat: ~4%
- Llama-2 70b-chat: ~4%
- MPT 7b-chat: ~20%
- Vicuna 13b-v1.1: ~25%
- Vicuna 33b-v1.3: ~37%
- Falcon 40b-instruct: ~20%
- PaLM Bison: ~7%
- ChatGPT 0301: ~30%

The authors caveat these safety results with the inherent bias of LLM evaluations due to limitations of the prompt set, subjectivity of review guidelines, and subjectivity of individual raters. Additionally, safety evaluations are performed using content standards that are likely to be biased towards the Llama 2-Chat models. More details in Section 4.4.

## Context and motivation

[p. 3] LLMs have shown great promise as highly capable AI assistants that excel in complex reasoning tasks requiring expert knowledge across a wide range of fields, including programming and creative writing. They enable interaction with humans through intuitive chat interfaces, leading to rapid and widespread adoption.

[p. 3] Auto-regressive transformers are pretrained on extensive self-supervised data, then aligned with human preferences via techniques such as RLHF. High computational requirements have limited LLM development to a few players. There have been public releases of pretrained LLMs (BLOOM (Scao et al., 2022), LLaMA-1 (Touvron et al., 2023), Falcon (Penedo et al., 2023)) that match closed pretrained competitors like GPT-3 (Brown et al., 2020) and Chinchilla (Hoffmann et al., 2022), but none are suitable substitutes for closed "product" LLMs such as ChatGPT, BARD, and Claude. The closed product LLMs are heavily fine-tuned to align with human preferences, which greatly enhances usability and safety. This step can require significant costs in compute and human annotation, and is often not transparent or easily reproducible.

## Contributions

[p. 3] The authors develop and release Llama 2, a family of pretrained and fine-tuned LLMs, Llama 2 and Llama 2-Chat, at scales up to 70B parameters. On the series of helpfulness and safety benchmarks tested, Llama 2-Chat models generally perform better than existing open-source models. They also appear to be on par with some of the closed-source models, at least on the human evaluations performed (see Figures 1 and 3). The paper contributes a thorough description of the fine-tuning methodology and approach to improving LLM safety. The authors also share novel observations made during development, such as the emergence of tool usage and temporal organization of knowledge.

## What is being released

[p. 4] Two model families are released for research and commercial use:

1. **Llama 2** -- an updated version of Llama 1, trained on a new mix of publicly available data. Pretraining corpus increased by 40%, context length doubled, and grouped-query attention adopted (Ainslie et al., 2023). Variants released: 7B, 13B, and 70B parameters. A 34B variant was also trained and reported on but not released.
2. **Llama 2-Chat** -- a fine-tuned version of Llama 2 optimized for dialogue use cases. Variants: 7B, 13B, and 70B parameters.

[p. 4] The 34B model release was delayed due to a lack of time to sufficiently red team.

## Safety and responsible release

[p. 4] The authors believe open release of LLMs, when done safely, will be a net benefit to society. They acknowledge Llama 2 carries potential risks (Bender et al., 2021b; Weidinger et al., 2021; Solaiman et al., 2023). Testing has been conducted in English and has not -- and could not -- cover all scenarios. Developers should perform safety testing and tuning tailored to specific applications. A responsible use guide and code examples are provided. Responsible release strategy detailed in Section 5.3.

## Paper structure

[p. 4] The remainder of the paper describes: pretraining methodology (Section 2), fine-tuning methodology (Section 3), approach to model safety (Section 4), key observations and insights (Section 5), relevant related work (Section 6), and conclusions (Section 7).
