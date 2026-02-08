# 4.3 Evaluation [p. 17–19]

[p. 17] The CODE-QWEN models have been compared with both proprietary and open-source language models, as shown in Tables 10 and 11. These tables present the results of the evaluation on the test sets of HumanEval (Chen et al., 2021), MBPP (Austin et al., 2021), and the multi-lingual code generation benchmark HUMANEVALPACK (Muennighoff et al., 2023). The comparison is based on the pass@1 performance of the models on these benchmark datasets.

[p. 17] The analysis reveals that specialized models, specifically CODE-QWEN and CODE-QWEN-CHAT, significantly outperform previous baselines with similar parameter counts, such as OCTOGEEX (Muennighoff et al., 2023), InstructCodeT5+ (Wang et al., 2023d), and CodeGeeX2 (Zheng et al., 2023). In fact, these models even rival the performance of larger models like StarCoder (Li et al., 2023d).

[p. 17] When compared to some of the extremely large-scale closed-source models, CODE-QWEN and CODE-QWEN-CHAT demonstrate clear advantages in terms of pass@1. However, it is important to note that these models fall behind the state-of-the-art methods, such as GPT-4, in general. Nonetheless, with the continued scaling of both model size and data size, the authors believe that this gap can be narrowed in the near future.

[p. 17] It is crucial to emphasize that the evaluations mentioned previously are insufficient for grasping the full extent of the strengths and weaknesses of the models. In the authors' opinion, it is necessary to develop more rigorous tests to enable them to accurately assess their relative performance in comparison to GPT-4.

## Table 10: Results of pass@1 (%) on HumanEval and MBPP [p. 18]

Most scores are retrieved from the papers of StarCoder (Li et al., 2023d), CodeT5+ (Wang et al., 2023d), WizardCoder (Luo et al., 2023b) and CODE LLAMA (Roziere et al., 2023).

| Model | Params | HumanEval | MBPP |
|---|---|---|---|
| *Proprietary models* | | | |
| PaLM | 540B | 26.2 | 36.8 |
| PaLM-Coder | 540B | 36.0 | 47.0 |
| PaLM 2-S | - | 37.6 | 50.0 |
| Code-Cushman-001 | - | 33.5 | 45.9 |
| Code-Davinci-002 | - | 47.0 | 58.1 |
| GPT-3.5 | - | 73.2 | - |
| GPT-4 | - | 86.6 | - |
| *Open-source models* | | | |
| LLAMA 2 | 7B | 12.2 | 20.8 |
| | 13B | 20.1 | 27.6 |
| | 34B | 22.6 | 33.8 |
| | 70B | 30.5 | 45.4 |
| CodeGen-Multi | 16B | 18.3 | 20.9 |
| CodeGen-Mono | 16B | 29.3 | 35.3 |
| CodeGeeX2 | 6B | 35.9 | - |
| StarCoder-Prompted | 15B | 40.8 | 49.5 |
| CodeT5+ | 16B | 30.9 | - |
| InstructCodeT5+ | 16B | 35.0 | - |
| CODE LLAMA | 7B | 33.5 | 41.4 |
| | 13B | 36.0 | 47.0 |
| | 34B | 48.8 | 55.0 |
| CODE LLAMA-INSTRUCT | 7B | 34.8 | 44.4 |
| | 13B | 42.7 | 49.4 |
| | 34B | 41.5 | 57.0 |
| CODE LLAMA-PYTHON | 7B | 38.4 | 47.6 |
| | 13B | 43.3 | 49.0 |
| | 34B | 53.7 | 56.2 |
| UNNATURAL CODE LLAMA | 34B | 62.2 | 61.2 |
| WizardCoder-Python | 13B | 64.0 | **55.6** |
| | 34B | 73.2 | 61.2 |
| QWEN-CHAT | 7B | 37.2 | 35.8 |
| | 14B | 43.9 | 46.4 |
| CODE-QWEN | 7B | 40.2 | 41.8 |
| | 14B | 45.1 | 51.4 |
| CODE-QWEN-CHAT | 7B | 43.3 | 44.2 |
| | 14B | **66.4** | 52.4 |

## Table 11: Zero-shot pass@1 (%) performance on the HUMANEVALPACK (synthesize) benchmark [p. 19]

The baseline results are partly from OCTOPACK (Muennighoff et al., 2023).

| Model | Params | Python | JavaScript | Java | Go | C++ | Rust | Avg. |
|---|---|---|---|---|---|---|---|---|
| *Proprietary models* | | | | | | | | |
| GPT-4 | - | 86.6 | 82.9 | 81.7 | 72.6 | 78.7 | 67.1 | 78.3 |
| *Open-source models* | | | | | | | | |
| InstructCodeT5+ | 16B | 37.0 | 18.9 | 17.4 | 9.5 | 19.8 | 0.3 | 17.1 |
| StarChat-beta | 15B | 33.5 | 31.4 | 26.7 | 25.5 | 26.6 | 14.0 | 26.3 |
| StarCoder | 15B | 33.6 | 30.8 | 30.2 | 17.6 | 31.6 | 21.8 | 27.6 |
| CodeGeeX2 | 6B | 35.9 | 32.2 | 30.8 | 22.5 | 29.3 | 18.1 | 28.1 |
| OCTOGEEX | 6B | 44.7 | 33.8 | 36.9 | 21.9 | 32.3 | 15.7 | 30.9 |
| OCTOCODER | 15B | 46.2 | 39.2 | 38.2 | 30.4 | 35.6 | 23.4 | 35.5 |
| WizardCoder | 15B | 59.8 | 49.5 | 36.1 | 36.4 | 40.9 | 20.2 | 40.5 |
| QWEN-CHAT | 7B | 37.2 | 23.2 | 32.9 | 20.7 | 22.0 | 9.1 | 24.2 |
| | 14B | 43.9 | 38.4 | 42.7 | 34.1 | 24.4 | 18.9 | 33.7 |
| CODE-QWEN | 7B | 40.2 | 40.4 | 40.2 | 26.2 | 20.7 | 15.8 | 30.6 |
| | 14B | 45.1 | 51.8 | 57.3 | 39.6 | 18.2 | 20.7 | 38.8 |
| CODE-QWEN-CHAT | 7B | 43.3 | 41.5 | 49.4 | 29.3 | 32.9 | 20.1 | 36.1 |
| | 14B | **66.4** | **58.5** | **56.1** | **47.6** | **54.2** | **28.7** | **51.9** |
