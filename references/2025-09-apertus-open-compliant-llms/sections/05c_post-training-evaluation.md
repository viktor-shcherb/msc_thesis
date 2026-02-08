# 5.2 Post-training Evaluation [p. 39–41]

## Scope [p. 39]

[p. 39] In the post-training phase, a distinct set of capabilities that are refined through instruction tuning and alignment are evaluated. These include reasoning, mathematics, coding, instruction following, and key aspects of safety, alignment, and robustness. The focus is on how well the model generalizes to complex reasoning tasks, solves multi-step problems, and follows natural language instructions with precision and consistency. The model's responses to adversarial prompts and ambiguous queries are also examined to gauge its robustness and alignment with intended behavior. Taken together, these evaluations provide a comprehensive picture of the model's readiness for real-world interaction and downstream applications.

Compared to the pretraining evaluation, a mix of generation-based benchmarks is employed, which require instruction-following capabilities to format the final answer, and probabilistic evaluations. Both English and multilingual benchmarks are jointly considered, and the importance of analyzing them together is emphasized.

## Benchmarks [p. 39–40]

[p. 39–40] A suite of benchmarks in seven categories that capture complementary aspects of model capabilities is considered:

1. **Knowledge recall:** AGIeval (Zhong et al., 2024), MMLU (Hendrycks et al., 2021a), Global-MMLU (Singh et al., 2025), TruthfulQA (Lin et al., 2021), and TruthfulQA multilingual (Calvo Figueras et al., 2025).
2. **Instruction following:** IFEval (Zhou et al., 2023) and Multi-IFEval (Dussolle et al., 2025).
3. **Commonsense reasoning:** HellaSwag (English; Zellers et al., 2019; multilingual; Lai et al., 2023).
4. **Coding:** HumanEval (Chen et al., 2021) and MBPP (Austin et al., 2021).
5. **Mathematics:** GSM8K (Cobbe et al., 2021), GSM8K-Platinum, MATH (Hendrycks et al., 2021b), and MathQA (Amini et al., 2019).
6. **Reasoning:** ACPBench (Kokel et al., 2025), ARC Challenge (Clark et al., 2018), BBH (Suzgun et al., 2022), DROP (Dua et al., 2019), GPQA (Rein et al., 2024), MGSM (Shi et al., 2022), and MLogiQA (Liu et al., 2020).
7. **Cultural knowledge:** BLEnD (Myung et al., 2025), CulturalBench (Chiu et al., 2025), INCLUDE (Romanou et al., 2025), and custom SwitzerlandQA (Section K).

Benchmark details on the benchmark specifications are provided in Table 22. Benchmarks contained in Table 21 were held-out during model development and were not used for making decisions.

## Baseline Models [p. 40]

[p. 40] Models are compared against a range of instruction-tuned baselines, spanning both open-weight and fully open-source models with parameter sizes from 3B to 72B. These baselines include model families such as LLaMA, Qwen, OLMo, EuroLLM, and Gemma. The complete list of models is provided in Table 16.

---

**Table 16: Pretrained and Post-trained Baseline LLMs** [p. 40]

Compared with Apertus and Apertus-Instruct. **Fully-open** indicates whether the models provide open data, open weights, and open implementations.

| Model | Open-weight | Fully-open | Multilingual Focus |
|---|---|---|---|
| **Pretrained Baselines** | | | |
| OLMo2-7B (OLMo et al., 2024) | Yes | Yes | No |
| OLMo2-32B (OLMo et al., 2024) | Yes | Yes | No |
| EuroLLM-1.7B (Martins et al., 2024) | Yes | Yes | Yes |
| EuroLLM-9B (Martins et al., 2024) | Yes | Yes | Yes |
| SmolLM2-1.7B (HuggingFaceTB, 2025) | Yes | Yes | Yes |
| SmolLM3-3B (HuggingFaceTB, 2025) | Yes | Yes | Yes |
| Llama3.1-8B (Dubey et al., 2024) | Yes | No | Yes |
| Llama3.3-70B (Dubey et al., 2024) | Yes | No | Yes |
| Llama4-Scout-16x17B (Meta AI, 2025) | Yes | No | Yes |
| Qwen2.5-7B (Yang et al., 2025b) | Yes | No | Yes |
| Qwen2.5-72B (Yang et al., 2025b) | Yes | No | Yes |
| Qwen3-32B (Yang et al., 2025b) | Yes | No | Yes |
| GPT-OSS-20B (OpenAI et al., 2025) | Yes | No | Yes |
| **Post-trained Baselines** | | | |
| ALLaM-7B-Instruct-preview (Bari et al., 2024) | Yes | Yes | Yes |
| EuroLLM-22B-Instruct-Preview (Martins et al., 2024) | Yes | Yes | Yes |
| EuroLLM-9B-Instruct (Martins et al., 2024) | Yes | Yes | Yes |
| K2-Chat (Liu et al., 2025c) | Yes | Yes | Yes |
| Llama-3.1-8B-Instruct (Dubey et al., 2024) | Yes | No | Yes |
| Llama-3.3-70B-Instruct (Dubey et al., 2024) | Yes | No | Yes |
| gemma-3-12b-it (Team et al., 2025) | Yes | No | Yes |
| gemma-3-27b-it (Team et al., 2025) | Yes | No | Yes |
| marin-8b-instruct (Community, 2025) | Yes | Yes | No |
| Minerva-7B-instruct-v1.0 (NLP, 2024) | Yes | Yes | Yes |
| OLMo-2-0325-32B-Instruct (OLMo et al., 2024) | Yes | Yes | No |
| OLMo-2-0325-32B-SFT (OLMo et al., 2024) | Yes | Yes | No |
| OLMo-2-1124-7B-Instruct (OLMo et al., 2024) | Yes | Yes | No |
| OLMo-2-1124-7B-SFT (OLMo et al., 2024) | Yes | Yes | No |
| Qwen2.5-72B-Instruct (Qwen et al., 2024) | Yes | No | Yes |
| Qwen3-32B (Yang et al., 2025b) | Yes | No | Yes |
| Qwen3-8B (Yang et al., 2025b) | Yes | No | Yes |
| salamandra-7b-instruct (Gonzalez-Agirre et al., 2025) | Yes | Yes | Yes |
| SmolLM3-3B (HuggingFaceTB, 2025) | Yes | Yes | Yes |
| Teuken-7B-instruct-v0.6 (Ali et al., 2024) | Yes | Yes | Yes |

## Evaluation Setup [p. 40–41]

[p. 40–41] Consistent with the evaluation approach used during pretraining, the *lm-evaluation-harness* framework is employed in the post-training phase, shifting to open-generation mode to better assess the model's generative capabilities. The framework's existing benchmark implementations are relied upon while extending it with additional tasks not natively supported, carefully adhering to the original task definitions, prompt formats, and evaluation protocols specified in their respective publications. To ensure methodological fairness and consistency, particularly when evaluating smaller models, simplified prompting strategies are adopted and additional extraction filters are applied to standardize response parsing and improve evaluation reliability. Moreover, pretraining competencies are tracked throughout post-training (see Section 5.1), extending probabilistic evaluation of pretraining benchmarks to zero-shot and zero-shot chain-of-thought (CoT) generation. This enables a more nuanced analysis of how foundational skills evolve under alignment.

## Post-training Evaluation Results [p. 41]

[p. 41] Evaluation results are presented across different capability categories: Knowledge recall, Instruction following, and Commonsense reasoning in Table 17; Coding and Math in Table 18; Reasoning in Table 19; and Cultural knowledge in Table 20. Results on the held-out test suite spanning Knowledge, Reasoning, and Math are reported in Table 21.

Overall, comparisons between models on development metrics align well with results from the held-out evaluation suite (Table 21). The Apertus-Instruct models achieve solid performance across the diverse set of benchmarks considered, particularly in comparison to other fully open models of similar sizes. Notably, Apertus-8B is competitive with the strongest fully open models in knowledge recall, instruction following, and commonsense reasoning, while performing less strongly in math, coding, and reasoning. At the same time, it stands out in cultural knowledge, where it leads among fully open models and approaches the strongest models in its size class, such as Qwen3-8B. Performance in math and coding is comparatively weaker for both Apertus models, though most other models have undergone additional RL training (*e.g.*, RLVR), which is known to enhance these capabilities but has not yet been applied to Apertus. The performance gap between the 8B and 70B models is smaller than typically observed in other model families.

---

**Table 17: Post-training Evaluation** [p. 41]

Performance (%) of Apertus models across **knowledge recall** and **commonsense reasoning**. Performance is reported on benchmarks for both English and multilingual settings. The arrows (up/down) show the desired direction for each benchmark.

| Model | Avg (up) | MMLU (up) | Global-MMLU (up) | TruthQA (up) | TruthQA Multilingual (up) | HellaSwag (up) | HellaSwag Multilingual (up) |
|---|---|---|---|---|---|---|---|
| **Fully Open Models** | | | | | | | |
| **Apertus-70B-Instruct** | **63.4** | **69.6** | **62.7** | **61.2** | **53.7** | **78.1** | **55.3** |
| **Apertus-8B-Instruct** | **58.8** | **60.9** | **55.7** | **56.7** | **52.4** | **74.6** | **52.7** |
| ALLaM-7B-Instruct-preview | 53.7 | 62.9 | 50.6 | 47.5 | 43.7 | 75.3 | 42.0 |
| EuroLLM-22B-Instruct-Preview | 58.3 | 65.5 | 56.9 | 56.6 | 49.8 | 73.0 | 48.1 |
| EuroLLM-9B-Instruct | 53.8 | 58.4 | 52.0 | 49.7 | 46.5 | 69.8 | 46.3 |
| K2-Chat | 56.8 | 65.7 | 49.8 | 56.5 | 49.2 | 74.9 | 44.7 |
| marin-8b-instruct | 54.5 | 65.5 | 48.4 | 55.2 | 47.6 | 72.0 | 38.1 |
| Minerva-7B-instruct-v1.0 | 40.8 | 30.7 | 28.5 | 44.0 | 47.2 | 63.3 | 31.2 |
| OLMo-2-0325-32B-Instruct | 68.0 | 77.9 | 61.3 | 73.2 | 56.4 | 86.0 | 53.0 |
| OLMo-2-1124-7B-Instruct | 53.7 | 60.0 | 42.8 | 56.5 | 46.5 | 77.5 | 38.7 |
| salamandra-7b-instruct | 52.0 | 52.4 | 43.1 | 51.0 | 48.4 | 71.4 | 45.9 |
| SmolLM3-3B | 54.4 | 61.7 | 51.2 | 54.3 | 50.0 | 69.0 | 40.4 |
| Teuken-7B-instruct-v0.6 | 48.9 | 49.0 | 39.9 | 46.4 | 48.1 | 67.8 | 42.2 |
| **Open-Weight Models** | | | | | | | |
| gemma-3-12b-it | 60.8 | 78.8 | 69.6 | 60.8 | 56.1 | 53.7 | 45.6 |
| gemma-3-27b-it | 63.8 | 83.6 | 75.3 | 64.4 | 54.8 | 54.9 | 49.8 |
| Llama-3.1-8B-Instruct | 59.2 | 72.4 | 57.1 | 55.1 | 50.8 | 72.5 | 47.0 |
| Llama-3.3-70B-Instruct | 68.4 | 87.5 | 77.8 | 66.1 | 55.2 | 70.1 | 53.8 |
| Qwen2.5-72B-Instruct | 68.8 | 86.6 | 77.7 | 69.7 | 58.6 | 68.8 | 51.5 |
| Qwen3-32B | 64.1 | 83.7 | 74.8 | 58.6 | 50.7 | 68.8 | 48.0 |
| Qwen3-8B | 57.8 | 79.1 | 64.0 | 53.4 | 51.4 | 58.6 | 40.4 |

---

**Table 18: Post-training Evaluation** [p. 42]

Performance (%) of Apertus models on **coding and mathematical reasoning** tasks. The arrows (up/down) show the desired direction for each benchmark.

| Model | Avg (up) | HumanEval (Pass@10) (up) | MBPP (Pass@1) (up) | GSM8K (up) | MGSM (up) | Hendrycks Math (up) | MathQA (up) |
|---|---|---|---|---|---|---|---|
| **Fully Open Models** | | | | | | | |
| **Apertus-70B-Instruct** | **54.4** | **73.0** | **47.0** | **77.6** | **64.3** | **30.8** | **33.9** |
| **Apertus-8B-Instruct** | **44.2** | **67.0** | **36.2** | **62.9** | **48.5** | **18.2** | **32.1** |
| ALLaM-7B-Instruct-preview | 38.5 | 56.7 | 39.0 | 58.2 | 29.1 | 15.6 | 32.3 |
| EuroLLM-22B-Instruct-Preview | 53.0 | 75.2 | 43.0 | 75.5 | 50.7 | 38.0 | 35.4 |
| EuroLLM-9B-Instruct | 42.9 | 65.3 | 41.0 | 62.9 | 36.1 | 19.2 | 32.7 |
| K2-Chat | 59.5 | 87.7 | 56.2 | 84.8 | 49.1 | 40.7 | 38.7 |
| marin-8b-instruct | 51.7 | 85.8 | 41.2 | 80.6 | 42.8 | 31.3 | 28.6 |
| Minerva-7B-instruct-v1.0 | 14.5 | 25.0 | 17.2 | 13.6 | 2.8 | 3.5 | 24.7 |
| OLMo-2-0325-32B-Instruct | 56.7 | 69.0 | 41.8 | 88.2 | 67.3 | 44.3 | 29.6 |
| OLMo-2-1124-7B-Instruct | 45.8 | 65.2 | 32.0 | 83.5 | 36.9 | 31.1 | 26.0 |
| salamandra-7b-instruct | 19.4 | 28.4 | 22.2 | 22.7 | 9.6 | 5.2 | 28.6 |
| SmolLM3-3B | 58.5 | 89.7 | 52.8 | 83.6 | 45.2 | 51.8 | 27.7 |
| Teuken-7B-instruct-v0.6 | 27.7 | 44.6 | 25.6 | 38.1 | 19.2 | 11.4 | 27.1 |
| **Open-Weight Models** | | | | | | | |
| gemma-3-12b-it | 71.1 | 88.0 | 72.0 | 89.9 | 68.9 | 68.4 | 39.3 |
| gemma-3-27b-it | 73.1 | 89.3 | 72.8 | 90.4 | 71.7 | 71.1 | 43.1 |
| Llama-3.1-8B-Instruct | 60.0 | 86.7 | 60.6 | 84.5 | 67.7 | 36.3 | 24.4 |
| Llama-3.3-70B-Instruct | 74.3 | 95.8 | 75.6 | 94.8 | 86.0 | 60.3 | 33.5 |
| Qwen2.5-72B-Instruct | 74.6 | 95.4 | 74.6 | 88.6 | 76.2 | 67.8 | 44.8 |
| Qwen3-32B | 76.3 | 97.0 | 73.6 | 93.6 | 74.0 | 69.2 | 50.5 |
| Qwen3-8B | 68.8 | 95.6 | 66.8 | 89.5 | 52.0 | 66.8 | 41.8 |

---

**Table 19: Post-training Evaluation** [p. 42]

Performance (%) of Apertus models on general and logical **reasoning** tasks and **instruction following**. The arrows (up/down) show the desired direction for each benchmark.

| Model | Avg (up) | BBH (up) | DROP (up) | ACP-Bench Bool (up) | ACP-Bench MCQ (up) | IFEval (up) | Multi-IFEval (up) |
|---|---|---|---|---|---|---|---|
| **Fully Open Models** | | | | | | | |
| **Apertus-70B-Instruct** | **61.8** | **64.2** | **50.8** | **62.9** | **43.0** | **75.2** | **74.7** |
| **Apertus-8B-Instruct** | **56.0** | **55.9** | **49.7** | **58.4** | **31.2** | **71.7** | **68.9** |
| ALLaM-7B-Instruct-preview | 53.6 | 46.3 | 55.4 | 58.9 | 41.7 | 65.4 | 54.0 |
| EuroLLM-22B-Instruct-Preview | 58.8 | 56.3 | 47.5 | 60.9 | 43.3 | 72.8 | 72.0 |
| EuroLLM-9B-Instruct | 51.3 | 53.1 | 45.0 | 51.6 | 34.0 | 62.8 | 61.3 |
| K2-Chat | 53.9 | 70.7 | 57.3 | 58.6 | 41.7 | 48.4 | 47.0 |
| marin-8b-instruct | 55.9 | 61.5 | 60.3 | 49.9 | 33.0 | 68.8 | 62.1 |
| Minerva-7B-instruct-v1.0 | 27.5 | 28.2 | 29.5 | 44.7 | 23.3 | 19.4 | 19.8 |
| OLMo-2-0325-32B-Instruct | 75.1 | 64.1 | 77.9 | 79.0 | 63.1 | 86.0 | 80.6 |
| OLMo-2-1124-7B-Instruct | 55.9 | 50.1 | 60.3 | 57.1 | 36.3 | 71.0 | 60.6 |
| salamandra-7b-instruct | 37.7 | 43.6 | 37.5 | 49.7 | 28.2 | 33.6 | 33.7 |
| SmolLM3-3B | 59.9 | 68.4 | 47.3 | 63.2 | 38.1 | 72.3 | 70.1 |
| Teuken-7B-instruct-v0.6 | 35.7 | 42.4 | 35.9 | 46.2 | 28.0 | 31.6 | 29.9 |
| **Open-Weight Models** | | | | | | | |
| gemma-3-12b-it | 75.2 | 70.8 | 70.3 | 77.1 | 73.0 | 80.0 | 80.2 |
| gemma-3-27b-it | 76.9 | 89.3 | 71.1 | 82.9 | 75.4 | 81.3 | 80.0 |
| Llama-3.1-8B-Instruct | 63.9 | 72.0 | 62.4 | 56.2 | 42.8 | 78.6 | 71.3 |
| Llama-3.3-70B-Instruct | 83.8 | 86.6 | 72.0 | 82.6 | 82.1 | 90.8 | 88.7 |
| Qwen2.5-72B-Instruct | 79.4 | 82.7 | 64.4 | 81.6 | 77.6 | 86.3 | 83.8 |
| Qwen3-32B | 80.8 | 86.1 | 65.2 | 85.1 | 77.1 | 87.2 | 84.4 |
| Qwen3-8B | 73.3 | 53.6 | 60.6 | 82.1 | 74.2 | 86.5 | 82.8 |

---

**Table 20: Post-training Evaluation** [p. 43]

Performance (%) of Apertus models on **cultural knowledge**, measuring cultural and factual knowledge across multiple languages. The arrows (up/down) show the desired direction for each benchmark.

| Model | Avg (up) | INCLUDE (up) | INCLUDE V2 (up) | BLEnD (up) | Cultural Bench (up) | Switzerland QA (up) |
|---|---|---|---|---|---|---|
| **Fully Open Models** | | | | | | |
| **Apertus-70B-Instruct** | **61.5** | **58.2** | **41.6** | **66.3** | **74.2** | **67.2** |
| **Apertus-8B-Instruct** | **58.6** | **54.3** | **39.2** | **63.6** | **72.8** | **63.1** |
| ALLaM-7B-Instruct-preview | 55.2 | 44.4 | 34.6 | 66.4 | 74.4 | 56.0 |
| EuroLLM-22B-Instruct-Preview | 57.0 | 53.7 | 36.0 | 63.6 | 70.2 | 61.6 |
| EuroLLM-9B-Instruct | 54.3 | 49.3 | 36.8 | 62.7 | 61.4 | 61.2 |
| K2-Chat | 56.3 | 44.3 | 33.8 | 68.2 | 73.3 | 62.0 |
| marin-8b-instruct | 52.5 | 38.9 | 34.4 | 61.9 | 73.4 | 53.7 |
| Minerva-7B-instruct-v1.0 | 39.1 | 25.6 | 28.0 | 40.4 | 64.0 | 37.4 |
| OLMo-2-0325-32B-Instruct | 58.1 | 52.9 | 39.5 | 61.2 | 74.5 | 62.2 |
| OLMo-2-1124-7B-Instruct | 49.7 | 36.3 | 31.3 | 60.8 | 72.8 | 47.2 |
| salamandra-7b-instruct | 52.8 | 42.1 | 33.0 | 58.6 | 70.5 | 59.6 |
| SmolLM3-3B | 52.7 | 41.4 | 31.3 | 61.6 | 72.6 | 56.6 |
| Teuken-7B-instruct-v0.6 | 49.7 | 39.7 | 31.5 | 53.8 | 70.7 | 53.0 |
| **Open-Weight Models** | | | | | | |
| gemma-3-12b-it | 63.4 | 62.7 | 42.8 | 69.5 | 76.8 | 65.1 |
| gemma-3-27b-it | 67.7 | 67.9 | 46.9 | 74.2 | 78.4 | 71.0 |
| Llama-3.1-8B-Instruct | 58.2 | 53.4 | 34.0 | 67.3 | 76.2 | 60.0 |
| Llama-3.3-70B-Instruct | 69.6 | 71.9 | 45.8 | 75.1 | 81.0 | 74.3 |
| Qwen2.5-72B-Instruct | 66.8 | 70.0 | 42.2 | 75.4 | 76.3 | 70.0 |
| Qwen3-32B | 65.9 | 70.6 | 45.8 | 72.0 | 75.5 | 65.6 |
| Qwen3-8B | 60.4 | 60.7 | 38.7 | 65.9 | 75.8 | 60.7 |

---

**Table 21: Post-training Evaluation** [p. 43]

Performance (%) of Apertus models on **test benchmarks**. Results are reported on held-out benchmarks, with no feedback used during training or hyperparameter tuning. The arrows (up/down) show the desired direction for each benchmark.

| Model | Avg (up) | AGIeval (up) | ARC Challenge Chat (up) | ARC Challenge Multilingual (up) | GPQA Main (up) | GSM8K Platinum (up) | MLogiQA (up) |
|---|---|---|---|---|---|---|---|
| **Fully Open Models** | | | | | | | |
| **Apertus-70B-Instruct** | **51.4** | **40.5** | **85.0** | **37.3** | **30.6** | **74.6** | **40.5** |
| **Apertus-8B-Instruct** | **45.1** | **38.7** | **77.6** | **36.8** | **27.0** | **61.6** | **29.0** |
| ALLaM-7B-Instruct-preview | 46.2 | 42.7 | 83.2 | 29.4 | 25.7 | 61.7 | 34.5 |
| EuroLLM-22B-Instruct-Preview | 50.2 | 39.9 | 86.4 | 33.3 | 29.0 | 77.3 | 35.4 |
| EuroLLM-9B-Instruct | 44.6 | 36.2 | 73.0 | 32.2 | 25.4 | 66.3 | 34.5 |
| K2-Chat | 49.7 | 43.5 | 79.1 | 32.6 | 29.9 | 77.8 | 35.5 |
| marin-8b-instruct | 47.7 | 36.5 | 82.6 | 25.5 | 29.9 | 79.1 | 32.8 |
| Minerva-7B-instruct-v1.0 | 23.8 | 28.2 | 27.7 | 21.6 | 27.0 | 12.1 | 26.2 |
| OLMo-2-0325-32B-Instruct | 58.3 | 51.2 | 91.5 | 38.6 | 35.0 | 89.5 | 43.9 |
| OLMo-2-1124-7B-Instruct | 47.1 | 36.0 | 79.0 | 26.0 | 29.5 | 81.1 | 31.2 |
| salamandra-7b-instruct | 34.7 | 32.6 | 64.9 | 31.3 | 27.2 | 24.2 | 28.0 |
| SmolLM3-3B | 49.2 | 38.5 | 83.5 | 27.1 | 34.2 | 75.2 | 37.0 |
| Teuken-7B-instruct-v0.6 | 36.4 | 33.0 | 63.4 | 26.7 | 25.0 | 39.5 | 31.1 |
| **Open-Weight Models** | | | | | | | |
| gemma-3-12b-it | 60.8 | 55.4 | 93.3 | 37.2 | 39.1 | 85.5 | 54.4 |
| gemma-3-27b-it | 63.5 | 61.3 | 93.8 | 39.8 | 45.1 | 86.7 | 54.5 |
| Llama-3.1-8B-Instruct | 50.3 | 38.1 | 83.7 | 32.0 | 28.3 | 78.8 | 40.9 |
| Llama-3.3-70B-Instruct | 65.8 | 54.2 | 95.7 | 42.9 | 59.6 | 84.0 | 58.1 |
| Qwen2.5-72B-Instruct | 64.9 | 64.1 | 96.2 | 39.2 | 46.9 | 87.3 | 55.9 |
| Qwen3-32B | 61.4 | 30.1 | 95.6 | 34.9 | 56.5 | 88.5 | 62.8 |
| Qwen3-8B | 56.0 | 29.9 | 93.3 | 30.2 | 42.6 | 89.4 | 50.4 |

---

**Table 22: Benchmark Specifications for Post-training Evaluations** [p. 44]

Benchmark name (with internal identifier in github.com/swiss-ai/lm-evaluation-harness), evaluation metric, task type, use of chain-of-thought (CoT), number of few-shot demonstrations (#Shots), use of chat template (Chat), whether demonstrations are formatted as a multi-turn conversation (Turns), and the number of languages (#Langs). INCLUDE V2 is a beta extension of the INCLUDE benchmark covering 45 more languages. In total, the evaluation covers 94 different languages.

| Benchmark (identifier) | Metric | Type | CoT | #Shots | Chat | Turns | #Langs |
|---|---|---|---|---|---|---|---|
| ACP-Bench Bool (acp_bench_mcl) | Exact Match | MCQ (Gen) | Yes | 2 | Yes | Yes | 1 |
| ACP-Bench MCQ (acp_bench_mcq) | Exact Match | MCQ (Gen) | Yes | 2 | Yes | Yes | 1 |
| AGIeval (agieval) | Acc. | MCQ (LH) | No | 0 | Yes | No | 2 |
| ARC Challenge Chat (arc_challenge_chat_cot) | Exact Match | MCQ (Gen) | Yes | 0 | Yes | No | 1 |
| ARC Challenge Multilingual (arc_multilingual) | Acc. | MCQ (LH) | No | 0 | Yes | No | 31 |
| BBH (bbh) | Exact Match | Gen | Yes | 3 | Yes | Yes | 1 |
| BBQ (bbq) | Acc. | MCQ (LH) | No | 0 | Yes | No | 1 |
| BLEND (blend_sample) | Acc. (norm) | MCQ (LH) | No | 0 | Yes | No | 1 |
| Cultural Bench (cultural_bench) | Acc. (norm) | MCQ (LH) | No | 0 | Yes | No | 1 |
| DROP (drop) | F1 | Gen | No | 3 | Yes | Yes | 1 |
| Global MMLU (global_mmlu_gen_0shot) | Exact Match | MCQ (Gen) | No | 0 | Yes | No | 15 |
| GPQA Main (gpqa_main_cot_zeroshot) | Exact Match | MCQ (Gen) | Yes | 0 | Yes | No | 1 |
| GSM8K (gsm8k_cot) | Exact Match | Gen | Yes | 8 | Yes | Yes | 1 |
| GSM8K Platinum (gsm8k_platinum_cot_zeroshot) | Exact Match | Gen | Yes | 0 | Yes | No | 1 |
| HarmBench (harmbench) | Score | Gen | No | 0 | Yes | No | 1 |
| HellaSwag (hellaswag) | Acc. (norm) | MCQ (LH) | No | 0 | Yes | No | 1 |
| HellaSwag Multilingual (hellaswag_multilingual) | Acc. (norm) | MCQ (LH) | No | 0 | Yes | No | 31 |
| Hendrycks Math (hendrycks_math) | Math Verify | Gen | Yes | 6 | Yes | Yes | 1 |
| HumanEval (humaneval_instruct) | Pass@10 | Gen | No | 0 | Yes | No | 1 |
| IFEval (ifeval) | Acc. (prompt-level; loose) | Gen | No | 0 | Yes | No | 1 |
| INCLUDE (include_base_44_gen_0shot) | Exact Match | MCQ (Gen) | No | 0 | Yes | No | 44 |
| INCLUDE V2 (include_base_new_45_gen_0shot) | Exact Match | MCQ (Gen) | No | 0 | Yes | No | 45 |
| MathQA (mathqa) | Acc. | MCQ (LH) | No | 0 | Yes | No | 1 |
| MBPP (mbpp_instruct) | Pass@1 | Gen | No | 3 | Yes | Yes | 1 |
| MGSM (mgsm_cot) | Exact Match | Gen | Yes | 0 | Yes | No | 11 |
| MLogiQA (mlogiqa_gen) | Exact Match | MCQ (Gen) | No | 0 | Yes | No | 10 |
| MMLU (mmlu_flan_cot_zeroshot) | Exact Match | MCQ (Gen) | Yes | 0 | Yes | No | 1 |
| Multi-IFEval (multi-if) | Acc. (prompt-level; loose) | Gen | No | 0 | Yes | No | 8 |
| RealToxicityPrompts LlaMA-Guard3 Subsampled (realtoxicityprompts3llama) | Score | Gen | No | 0 | Yes | No | 1 |
| Switzerland QA (switzerland_qa_0shot) | Exact Match | MCQ (Gen) | No | 0 | Yes | No | 5 |
| ToxiGen (toxigen) | Acc. | MCQ (LH) | No | 0 | Yes | No | 1 |
| TruthfulQA (truthfulqa_mc2) | Acc. | MCQ (LH) | No | 6 | Yes | No | 1 |
| TruthfulQA Multilingual (truthfulqa_multilingual_mc2) | Acc. | MCQ (LH) | No | 5 | Yes | No | 31 |

## Long Context Evaluation [p. 41]

[p. 41] The long context capabilities of Apertus-8B-Instruct and Apertus-70B-Instruct are evaluated on the RULER (Hsieh et al., 2024) benchmark with a configured context length of 4k, 8k, 16k, 32k, and 64k. The evaluation results are shown in Table 23.
