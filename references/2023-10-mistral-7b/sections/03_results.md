# 3 Results [p. 3-4]

[p. 3] Mistral 7B is compared to Llama, with all benchmarks re-run using the authors' own evaluation pipeline for fair comparison. Performance is measured on a wide variety of tasks categorized as follows:

- **Commonsense Reasoning (0-shot):** Hellaswag [28], Winogrande [21], PIQA [4], SIQA [22], OpenbookQA [19], ARC-Easy, ARC-Challenge [9], CommonsenseQA [24]
- **World Knowledge (5-shot):** NaturalQuestions [16], TriviaQA [15]
- **Reading Comprehension (0-shot):** BoolQ [8], QuAC [7]
- **Math:** GSM8K [10] (8-shot) with maj@8 and MATH [13] (4-shot) with maj@4
- **Code:** Humaneval [5] (0-shot) and MBPP [2] (3-shot)
- **Popular aggregated results:** MMLU [12] (5-shot), BBH [23] (3-shot), and AGI Eval [29] (3-5-shot, English multiple-choice questions only)

[p. 3] Mistral 7B surpasses Llama 2 13B across all metrics, and outperforms Llama 1 34B on most benchmarks. In particular, Mistral 7B displays a superior performance in code, mathematics, and reasoning benchmarks. Since Llama 2 34B was not open-sourced, the authors report results for Llama 1 34B. [p. 3]

## Main Comparison

**Figure 4** (p. 4): "Performance of Mistral 7B and different Llama models on a wide range of benchmarks. All models were re-evaluated on all metrics with our evaluation pipeline for accurate comparison. Mistral 7B significantly outperforms Llama 2 7B and Llama 2 13B on all benchmarks. It is also vastly superior to Llama 1 34B in mathematics, code generation, and reasoning benchmarks."

Left panel: bar chart showing Accuracy (%) for MMLU, Knowledge, Reasoning, Comprehension across Mistral 7B, LLaMA 2 7B, LLaMA 2 13B, and LLaMA 1 34B. Mistral 7B leads on MMLU (~60%), Reasoning (~70+%), and Comprehension, and is competitive on Knowledge.
Right panel: bar chart showing Accuracy (%) for AGI Eval, Math, BBH, Code. Mistral 7B leads significantly on all four, particularly on Math and Code.

**Table 2: Comparison of Mistral 7B with Llama.** Mistral 7B outperforms Llama 2 13B on all metrics, and approaches the code performance of Code-Llama 7B without sacrificing performance on non-code benchmarks. [p. 4]

| Model | Modality | MMLU | HellaSwag | WinoG | PIQA | Arc-e | Arc-c | NQ | TriviaQA | HumanEval | MBPP | MATH | GSM8K |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LLaMA 2 7B | Pretrained | 44.4% | 77.1% | 69.5% | 77.9% | 68.7% | 43.2% | 24.7% | 63.8% | 11.6% | 26.1% | 3.9% | 16.0% |
| LLaMA 2 13B | Pretrained | 55.6% | **80.7%** | 72.9% | 80.8% | 75.2% | 48.8% | **29.0%** | **69.6%** | 18.9% | 35.4% | 6.0% | 34.3% |
| Code-Llama 7B | Finetuned | 36.9% | 62.9% | 62.3% | 72.8% | 59.4% | 34.5% | 11.0% | 34.9% | **31.1%** | **52.5%** | 5.2% | 20.8% |
| Mistral 7B | Pretrained | **60.1%** | **81.3%** | **75.3%** | **83.0%** | **80.0%** | **55.5%** | 28.8% | **69.9%** | 30.5% | 47.5% | **13.1%** | **52.2%** |

## Size and Efficiency

[p. 4] The authors computed "equivalent model sizes" of the Llama 2 family, aiming to understand Mistral 7B models' efficiency in the cost-performance spectrum (see Figure 5). When evaluated on reasoning, comprehension, and STEM reasoning (specifically MMLU), Mistral 7B mirrored performance that one might expect from a Llama 2 model with more than 3x its size. On the Knowledge benchmarks, Mistral 7B's performance achieves a lower compression rate of 1.9x, which is likely due to its limited parameter count that restricts the amount of knowledge it can store. [p. 4]

**Figure 5** (p. 5): "Results on MMLU, commonsense reasoning, world knowledge and reading comprehension for Mistral 7B and Llama 2 (7B/13B/70B). Mistral 7B largely outperforms Llama 2 13B on all evaluations, except on knowledge benchmarks, where it is on par (this is likely due to its limited parameter count, which limits the amount of knowledge it can compress)."

Four panels showing LLaMA 2 scaling curves (7B, 13B, 34B, 70B) with Mistral 7B plotted as a single point:
- MMLU (%): Mistral 7B (~60%) matches Effective LLaMA size 23B (3.3x)
- Reasoning (%): Mistral 7B (~70%) matches Effective LLaMA size 38B (5.4x)
- Knowledge (%): Mistral 7B (~65%) matches Effective LLaMA size 13B (1.9x)
- Comprehension (%): Mistral 7B (~66%) matches Effective LLaMA size 21B (3x)

## Evaluation Differences

[p. 4] On some benchmarks, there are differences between the authors' evaluation protocol and the one reported in the Llama 2 paper: 1) on MBPP, they use the hand-verified subset; 2) on TriviaQA, they do not provide Wikipedia contexts.
