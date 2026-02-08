# Gemma 1.0 IT results [p. 17]

The core of the paper presents the results of the Gemma 1.1 IT models. The results of the previous Gemma 1.0 IT models are kept for comparison in this appendix. Side-by-side evaluations of Gemma 1.0 IT against Mistral 7b v0.2 can be found in Table 9. Safety academic benchmark results of version 1.0 can be found in Table 10. [p. 17]

**Table 9** (p. 17): Win rate of Gemma 1.0 IT models versus Mistral 7B v0.2 Instruct with 95% confidence intervals. Breakdowns of wins, ties, and losses are reported. Ties are broken evenly in the final win rate.

| Model                | Safety          | Instruction Following |
|----------------------|-----------------|------------------------|
| **Gemma 7B IT**      | **58%**         | **51.7%**              |
| *95% Conf. Interval* | [55.9%, 60.1%] | [49.6%, 53.8%]         |
| *Win / Tie / Loss*   | 42.9% / 30.2% / 26.9% | 42.5% / 18.4% / 39.1% |
| **Gemma 2B IT**      | **56.5%**       | **41.6%**              |
| *95% Conf. Interval* | [54.4%, 58.6%] | [39.5%, 43.7%]         |
| *Win / Tie / Loss*   | 44.8% / 22.9% / 32.3% | 32.7% / 17.8% / 49.5% |

**Table 10** (p. 17): Safety academic benchmark results of Gemma 1.0 IT models, compared to similar size open models. Evaluations run by the authors. Note that due to restrictive licensing, no evaluations on LLaMA-2 could be run; previously-published numbers for LLaMA-2 on TruthfulQA are not reported, because different, non-comparable evaluation set-ups are used: MC2 for Gemma, where LLaMA-2 uses GPT-Judge.

| Benchmark     | metric        | Mistral v0.2 7B* | Gemma IT 2B | Gemma IT 7B |
|---------------|---------------|-------------------|-------------|-------------|
| RealToxicity  | avg           | 8.44              | **6.86**    | 7.90        |
| BOLD          |               | 46.0              | 45.57       | **49.08**   |
| CrowS-Pairs   | top-1        | 32.76             | 45.82       | **51.33**   |
| BBQ Ambig     | 1-shot, top-1 | **97.53**         | 62.58       | 92.54       |
| BBQ Disambig  | top-1         | **84.45**         | 54.62       | 71.99       |
| Winogender    | top-1         | **64.3**          | 51.25       | 54.17       |
| TruthfulQA    |               | **48.54**         | 31.81       | 44.84       |
| Winobias 1_2  |               | **65.72**         | 56.12       | 59.09       |
| Winobias 2_2  |               | 84.53             | 91.1        | **92.23**   |
| Toxigen       |               | 61.77             | **29.77**   | 39.59       |
