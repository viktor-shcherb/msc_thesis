# Appendix A: Comparison with Other Benchmarks [p. 29-30]

## Overview [p. 29]

Due to the lack of large-scale human studies on long-context language models, discerning the true rankings of LCLMs remains challenging [p. 29]. The authors rely on previous works and empirical observations to guide expectations [p. 29]. Specifically, the Gemini-1.5 report demonstrates that larger models consistently outperform smaller ones at handling long contexts—both qualitatively and quantitatively across the Gemini, GPT, and Claude model families (Section 1.3 Team et al., 2024b) [p. 29]. Although their evaluation suite is not publicly available, these results align with commonly observed patterns in language model performance [p. 29]. Given that obtaining ground truth rankings through human evaluation is prohibitively expensive and practically infeasible, relying on such well-established patterns in language model performance is reasonable [p. 29]. In this section, the authors further examine HELMET's improvements over existing benchmarks through direct comparisons of model rankings and performance, supported by careful ablation studies [p. 29].

## A.1 Results [p. 29-30]

### Benchmark Comparison [p. 29]

The authors build upon previous datasets and refine evaluation settings to better reflect model capabilities [p. 29]. Specifically, they evaluate models on ∞BENCH—a popular benchmark that evaluates long-context at 128K tokens [p. 29]. The results reproduced from the original authors' code are shown in Table 6 [p. 29]. The numerical results for Figure 1 are presented in Table 5 [p. 29].

**Table 5:** Results with 128k input length across different benchmarks [p. 29].

| Model | Claimed Length | NIAH | RULER | ∞BENCH | HELMET |
|-------|---------------|------|-------|---------|---------|
| GPT-4o-mini | 128000 | 100.0 | 80.8 | 51.9 | 54.1 |
| GPT-4o-08 | 128000 | 100.0 | 93.3 | 57.1 | 63.8 |
| Gemini-1.5-Flash | 1048576 | 100.0 | 86.6 | 50.8 | 50.7 |
| Gemini-1.5-Pro | 2097152 | 45.3 | 65.3 | 60.8 | 62.7 |
| Llama-3.1-8B-Inst | 131072 | 100.0 | 81.3 | 44.1 | 47.0 |
| Llama-3.1-70B-Inst | 131072 | 100.0 | 75.8 | 39.7 | 49.3 |

### Performance Discrepancy Analysis [p. 29-30]

Upon closer inspection, the authors find that a set of open-sourced models' ranking and performance on HELMET and ∞BENCH in Table 9 [p. 29]. In addition to the previously noted performance discrepancy between Llama-3.1-8B-Instruct and Llama-3.2 models, they observe that these models degenerate in performance on ∞BENCH at input length 128K [p. 29]. However, on HELMET, the Llama-3.2 models, especially Llama-3.2-3B-Instruct, rank well against other open-source models [p. 29]. Upon qualitative examination, the authors find that the Llama-3.2 models are able to produce coherent and useful generation at long contexts with better prompting strategies from HELMET, such as adding in-context learning examples [p. 29-30].

### Ablation Study on Few-shot Learning [p. 30]

The ablation study on few-shot demonstrations in Table 8 shows that 2-shot demonstrations substantially improve base model performance, better reflecting real-world usage patterns [p. 30]. As shown in Table 7, improved instructions and prompting enable smaller Llama-3.2 models to compete effectively with larger models [p. 30]. Thus, HELMET provides a better and more realistic reflection of how these models would be used in practice over previous benchmarks [p. 30]. These results demonstrate that HELMET provides a more accurate and practical assessment of model capabilities compared to previous benchmarks [p. 30].

**Table 6:** Results on ∞BENCH(Zhang et al., 2024b). The authors report numbers from running the original authors' repo: https://github.com/OpenBMB/InfiniteBench [p. 30]. The original code did not support evaluation of the Gemini and Llama 3 models at the time of access, so they evaluate them by following the script and template for GPT-4 and open-source models, respectively [p. 30]. They exclude coding tasks from the evaluation suite since it is out of the scope for general long-context language modeling tasks [p. 30].

| Model | MC | QA | Sum | Diag | Calc | Find | Number | PassKey | KV | Avg. |
|-------|----|----|-----|------|------|------|---------|---------|-----|------|
| GPT4 | 75.9 | 23.7 | 10.7 | 18.5 | 0.0 | 47.1 | 100.0 | 100.0 | 58.8 | 44.9 |
| GPT-4o-05 | 88.2 | 37.9 | 23.7 | 28.5 | 0.0 | 58.6 | 100.0 | 100.0 | 94.2 | 55.4 |
| GPT-4o-08 | 86.5 | 26.0 | 21.5 | 51.0 | 0.0 | 58.9 | 100.0 | 100.0 | 99.8 | 57.1 |
| GPT-4o-mini | 78.2 | 19.1 | 24.8 | 21.5 | 0.0 | 69.7 | 100.0 | 100.0 | 80.4 | 51.9 |
| Gemini-1.5-Flash | 76.0 | 42.1 | 30.0 | 55.8 | 0.0 | 47.4 | 100.0 | 100.0 | 31.4 | 50.8 |
| Gemini-1.5-Pro | 77.5 | 27.7 | 29.0 | 97.5 | 0.0 | 58.0 | 100.0 | 100.0 | 70.4 | 60.3 |
| Llama-3.1-8B | 56.8 | 8.8 | 14.3 | 0.5 | 0.0 | 22.0 | 99.7 | 100.0 | 18.8 | 33.0 |
| Llama-3.1-8B-Inst | 67.2 | 15.5 | 26.7 | 23.0 | 0.0 | 33.1 | 99.5 | 100.0 | 55.0 | 44.1 |
| Llama-3.1-70B | 66.4 | 9.2 | 17.5 | 8.5 | 0.0 | 32.3 | 100.0 | 100.0 | 13.4 | 35.1 |
| Llama-3.1-70B-Inst | 75.5 | 23.3 | 31.3 | 18.0 | 0.0 | 43.1 | 99.7 | 100.0 | 2.6 | 39.7 |
| Llama-3.2-1B | 2.2 | 1.4 | 8.6 | 4.5 | 0.0 | 0.0 | 1.5 | 0.0 | 0.0 | 2.0 |
| Llama-3.2-1B-Instruct | 3.5 | 1.4 | 12.5 | 5.5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.4 |
| Llama-3.2-3B | 1.3 | 1.2 | 7.6 | 4.5 | 0.0 | 0.0 | 1.7 | 0.0 | 0.0 | 1.9 |
| Llama-3.2-3B-Instruct | 2.2 | 1.6 | 13.3 | 4.5 | 0.0 | 0.0 | 1.7 | 1.7 | 0.0 | 2.8 |

**Table 7:** Comparison of the results on ∞BENCH multiple-choice (MC) and question answering (QA) tasks between the original authors and HELMET [p. 30]. In their implementation, they leverage refined prompts and carefully crafted parsing scripts to ensure robust and fair evaluation [p. 30]. For example, they find that Llama-3.2 models are actually much better long-context language models than ∞BENCH would suggest [p. 30].

|  | Original |  | HELMET |  |
|-------|---------------|-----|-----|-----|
| Model | Claimed Length | MC | QA | MC | QA |
| GPT-4o-mini | 128000 | 78.2 | 19.1 | 71.0 | 44.5 |
| GPT-4o-05 | 128000 | 88.2 | 37.9 | 76.0 | 53.0 |
| GPT-4o-08 | 128000 | 86.5 | 26.0 | 73.0 | 47.9 |
| Gemini-1.5-Flash | 1048576 | 76.0 | 42.1 | 79.1 | 51.7 |
| Gemini-1.5-Pro | 2097152 | 77.5 | 27.7 | 83.3 | 50.9 |
| Llama-3.1-8B | 131072 | 56.8 | 8.8 | 34.0 | 38.8 |
| Llama-3.1-8B-Inst | 131072 | 67.2 | 15.5 | 49.0 | 40.3 |
| Llama-3.2-1B | 131072 | 2.2 | 1.4 | 21.0 | 17.6 |
| Llama-3.2-1B-Inst | 131072 | 3.5 | 1.4 | 16.0 | 13.3 |
| Llama-3.2-3B | 131072 | 1.3 | 1.2 | 36.0 | 31.0 |
| Llama-3.2-3B-Inst | 131072 | 2.2 | 1.6 | 42.0 | 20.6 |

**Table 8:** Evaluation of the performance of models on a subset of HELMET tasks with 0-shot and 2-shot demonstrations at 128k input length, showing the impact of ICL on model performance, averaged across three random seeds [p. 31]. The standard deviation across three runs are shown in the subscript [p. 31]. The authors observe that the performance is generally higher for 2-shot demonstrations compared to 0-shot demonstrations [p. 31]. Crucially, the 2-shot examples enable base models to achieve higher results that reflect the model's long-context capabilities in realistic settings, such as for MSMARCO and JSON KV [p. 31]. *denotes base models [p. 31].

| | JSON KV | | MSMARCO | | ∞BENCH MC | | ∞BENCH QA | |
|-------|---------|---------|----------|----------|-----------|----------|-----------|----------|
| Model | 0 shot | 2 shot | 0 shot | 2 shot | 0 shot | 2 shot | 0 shot | 2 shot | 0 shot | 2 shot |
| GPT-4o-mini | 92.3₁.₆ | 93.7₂.₁ | 57.8₁.₁ | 61.4₂.₉ | 24.8₀.₇ | 31.4₁.₁ | 72.0₀.₆ | 69.3₄.₇ | 28.8₁.₉ | 27.1₄.₄ |
| GPT-4o-05 | 99.3₀.₆ | 30.7₇.₁ | 59.1₄.₀ | 63.9₀.₃ | 24.7₀.₆ | 46.8₁.₃ | 75.7₀.₉ | 76.3₀.₆ | 49.1₁.₆ | 51.3₄.₄ |
| GPT-4o-08 | 100.0 | 100.0 | 63.5₄.₅ | 70.1₁.₅ | 27.4₀.₇ | 37.1₃.₂ | 75.5₀.₈ | 78.3₀.₈ | 51.3₂.₀ | 50.8₂.₃ |
| Gemini-1.5-Flash | 98.3₀.₆ | 99.0₁.₀ | 53.7₁.₉ | 51.6₁.₅ | 44.9₀.₆ | 49.9₀.₆ | 73.9₀.₃ | 77.1₁.₅ | 48.2₄.₉ | 49.9₂.₆ |
| Gemini-1.5-Pro | 97.7₀.₆ | 93.7₂.₁ | 62.2₂.₉ | 69.2₀.₅ | 57.1₀.₆ | 58.4₀.₃ | 85.0₀.₄ | 83.4₀.₇ | 46.4₀.₄ | 47.2₁.₂ |
| Llama-3.1-8B* | 77.3₂.₁ | 95.0₁.₀ | 45.7₂.₁ | 44.9₁.₀ | 0.1₀.₀ | 7.5₀.₅ | 55.3₀.₅ | 53.3₀.₇ | 30.1₂.₀ | 36.6₂.₁ |
| Llama-3.1-8B-Inst | 96.0₁.₀ | 95.7₀.₆ | 48.3₁.₄ | 45.9₁.₉ | 5.4₀.₀ | 18.8₀.₁ | 49.7₁.₁ | 52.9₁.₆ | 29.1₂.₀ | 37.9₂.₆ |
| Llama-3.2-1B* | 34.0₀.₅ | 34.3₃.₁ | 25.1₀.₇ | 23.2₂.₄ | 0.3₀.₀ | 4.8₀.₅ | 23.0₁.₆ | 22.7₁.₅ | 18.9₂.₃ | 18.9₁.₃ |
| Llama-3.2-1B-Inst | 6.3₁.₅ | 9.3₁.₂ | 23.3₃.₄ | 22.9₁.₃ | 0.0₀.₀ | 16.9₁.₃ | 16.0₀.₉ | 16.2₃.₅ | 12.0₀.₃ | 12.7₀.₃ |
| Llama-3.2-3B* | 30.3₂.₁ | 54.0₀.₉ | 40.2₂.₀ | 42.3₁.₁ | 0.1₀.₀ | 6.0₁.₃ | 43.0₀.₀ | 40.7₅.₂ | 31.3₁.₁ | 31.6₂.₂ |
| Llama-3.2-3B-Inst | 31.3₂.₃ | 50.7₂.₅ | 44.2₁.₆ | 42.8₃.₁ | 0.2₀.₀ | 0.9₀.₆ | 50.0₀.₀ | 40.0₅.₀ | 17.8₁.₂ | 19.7₆.₉ |

**Table 9:** Comparison of model rankings on HELMET and ∞BENCH [p. 31].

| Model | HELMET | Model | InfBench |
|-------|---------|-------|----------|
| Llama-3.1-70B-Inst | 49.3 | Llama-3.1-8B-Inst | 46.7 |
| Llama-3.1-8B-Inst | 47.0 | Llama-3.1-70B-Inst | 43.7 |
| Llama-3.1-70B | 41.3 | Yi-34B-200k | 43.1 |
| Yi-34B-200k | 38.3 | Llama-3.1-70B | 38.6 |
| Llama-3-3B-Inst | 36.9 | Yi-9B-200k | 37.6 |
| Llama-3.1-8B | 35.6 | Llama-3.1-8B | 35.7 |
| Yi-9B-200k | 33.0 | Yi-6B-200k | 32.0 |
| Llama-3.2-3B | 31.9 | Llama-3.2-3B-Inst | 2.8 |
| Yi-6B-200k | 26.3 | Llama-3.2-1B-Inst | 2.6 |
| Llama-3.2-1B-Inst | 24.6 | Llama-3.2-1B | 2.0 |
| Llama-3.2-1B | 21.2 | Llama-3.2-3B | 1.8 |

## A.2 Discussions [p. 29-30]

Many existing long-context language modeling benchmarks are studied in isolated settings, such as synthetic tasks (Hsieh et al., 2024; Li et al., 2024b; Levy et al., 2024; Laban et al., 2024), in-context learning (Anil et al., 2024; Bertsch et al., 2024; Li et al., 2024c; Agarwal et al., 2024), summarization (Chang et al., 2024; Kim et al., 2024), and retrieval-augmented settings (Lee et al., 2024) [p. 29]. However, these works lack a unified evaluation across diverse downstream tasks [p. 29].

There are also benchmarks that sought to unify different datasets, such as ∞BENCH (Zhang et al., 2024b), LongBench (Bai et al., 2024), L-Eval (An et al., 2024), LV-Eval (Yuan et al., 2024), and ZeroSCROLLS (Shaham et al., 2023) [p. 29-30]. Many of these benchmarks are still limited by the context length, evaluation metrics, or both [p. 30]. Most similar to the authors' work, ∞BENCHZhang et al. (2024b) also evaluates models at context lengths at 200K tokens [p. 30]. However, their evaluation settings are limited to a few domains—synthetic, QA, and summarization [p. 30]. Although they also evaluate coding tasks, the domain is limited to code-specialized benchmarks, which is outside the realm of general-purpose language models [p. 30]. Furthermore, their summarization evaluations lack robust evaluation and still rely on ROUGE scores [p. 30]. Similarly, LV-Eval (Yuan et al., 2024) evaluates long-context models across different lengths but is limited to the QA tasks [p. 30]. Furthermore, the authors are the first to evaluate existing LCLMs comprehensively—they evaluate 59 models of different sizes and architectures, which enables previously unavailable insights into the correlation across diverse tasks and the landscape of current models [p. 30].
