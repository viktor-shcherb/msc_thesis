# 2. An Improved Gemini 1.5 Pro [p. 4-5]

[p. 4] Since the initial release in February, Gemini 1.5 Pro has undergone a number of pre-training and post-training iterations. These iterations have led to significant improvement in performance across the spectrum of model capabilities. On average, more than 10% relative improvement in evals over the previous version of 1.5 Pro.

## Benchmark improvements (Feb 2024 to May 2024)

[p. 4-5] On reasoning benchmarks:
- MATH (Hendrycks et al., 2021b): improved from 58.5% to 67.7%
- GPQA (Rein et al., 2023): improved from 41.5% to 46.2%

On multimodal tasks, 1.5 Pro improves on all image understanding benchmarks and most video understanding benchmarks:
- MathVista (Lu et al., 2023): improved from 52.1% to 63.9%
- InfographicVQA (Mathew et al., 2022): improved from 72.7% to 81.0%
- EgoSchema (Mangalam et al., 2023): improved from 65.1% to 72.2%

Gemini 1.5 Pro now achieves state-of-the-art results on several multimodal benchmarks including AI2D, MathVista, ChartQA, DocVQA, InfographicVQA and EgoSchema. [p. 5]

**Figure 2** (p. 5): "Comparison of Gemini 1.5 Pro (May 2024) to the initial version (Feb 2024) across several benchmarks. The latest Gemini 1.5 Pro makes improvements across all reasoning, coding, vision and video benchmarks; with audio and translation performance remaining neutral. Note that for FLEURS a lower score is better."

The figure is a grouped bar chart comparing Feb 2024 (light blue) vs May 2024 (dark blue) scores across benchmarks. Values read from the chart:

| Benchmark | Feb 2024 | May 2024 | Improvement |
|---|---|---|---|
| MATH | 58.5 | 67.7 | +9.2 |
| GPQA | 41.5 | 46.2 | +4.7 |
| BigBench-Hard | 84.0 | 89.2 | +5.2 |
| MMLU | 81.9 | 85.9 | +4.0 |
| HumanEval | 71.9 | 84.1 | +12.2 |
| Natural2Code | 77.7 | 82.6 | +4.9 |
| WMT23 | 75.2 | 75.3 | +0.1 |
| V* Bench | 48.0 | 71.7 | +23.7 |
| MathVista | 54.7 | 63.9 | +9.2 |
| MMMU | 58.5 | 62.2 | +3.7 |
| FLEURS (lower is better) | 6.6 | 6.5 | -0.1 |
| EgoSchema | 65.1 | 72.2 | +7.1 |
