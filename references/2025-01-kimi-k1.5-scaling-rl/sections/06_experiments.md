# 3 Experiments [p. 11]

## 3.1 Evaluation [p. 11]

Since k1.5 is a multimodal model, the authors conducted comprehensive evaluation across various benchmarks for different modalities. The detailed evaluation setup can be found in Appendix C [p. 11].

The benchmarks primarily consist of the following three categories [p. 11]:

**Text Benchmark:**
- MMLU (Hendrycks et al. 2020)
- IF-Eval (J. Zhou et al. 2023)
- CLUEWSC (L. Xu et al. 2020)
- C-EVAL (Y. Huang et al. 2023)

**Reasoning Benchmark:**
- HumanEval-Mul
- LiveCodeBench (Jain et al. 2024)
- Codeforces
- AIME 2024
- MATH-500 (Lightman et al. 2023)

**Vision Benchmark:**
- MMMU (Yue, Ni, et al. 2024)
- MATH-Vision (K. Wang et al. 2024)
- MathVista (Lu et al. 2023)

## 3.2 Main Results [p. 12]

### K1.5 long-CoT model [p. 12]

The performance of the Kimi k1.5 long-CoT model is presented in Table 2 [p. 12]. Through long-CoT supervised fine-tuning (described in Section 2.2) and vision-text joint reinforcement learning (discussed in Section 2.3), the model's long-term reasoning capabilities are enhanced significantly. The test-time computation scaling further strengthens its performance, enabling the model to achieve state-of-the-art results across a range of modalities [p. 12]. The evaluation reveals marked improvements in the model's capacity to reason, comprehend, and synthesize information over extended contexts, representing an advancement in multi-modal AI capabilities [p. 12].

**Table 2: Performance of Kimi k1.5 long-CoT and flagship open-source and proprietary models** [p. 12]

|                          |                            | Language-only Model |            | Vision-Language Model |         |         |
|--------------------------|----------------------------|---------------------|------------|-----------------------|---------|---------|
| Benchmark (Metric)       |                            | QwQ-32B Preview    | OpenAI o1-mini | QVQ-72B Preview      | OpenAI o1 | Kimi k1.5 |
| **Reasoning**           | MATH-500 (EM)              | 90.6               | 90.0       | -                     | 94.8    | **96.2** |
|                          | AIME 2024 (Pass@1)         | 50.0               | 63.6       | -                     | 74.4    | **77.5** |
|                          | Codeforces (Percentile)    | 62                 | 88         | -                     | **94**  | **94**   |
|                          | LiveCodeBench (Pass@1)     | 40.6               | 53.1       | -                     | **67.2**| 62.5     |
| **Vision**              | MathVista-Test (Pass@1)    | -                  | -          | 71.4                  | 71.0    | **74.9** |
|                          | MMMU-Val (Pass@1)          | -                  | -          | 70.3                  | **77.3**| 70.0     |
|                          | MathVision-Full (Pass@1)   | -                  | -          | 35.9                  | -       | **38.6** |

The k1.5 long-CoT model achieves:
- **96.2 EM on MATH-500**, outperforming OpenAI o1 (94.8) and QwQ-32B Preview (90.6) [p. 12, Table 2]
- **77.5 Pass@1 on AIME 2024**, surpassing OpenAI o1 (74.4) and QwQ-32B Preview (50.0) [p. 12, Table 2]
- **94th percentile on Codeforces**, matching OpenAI o1 [p. 12, Table 2]
- **74.9 Pass@1 on MathVista-Test**, exceeding QVQ-72B Preview (71.4) and OpenAI o1 (71.0) [p. 12, Table 2]
- **38.6 Pass@1 on MathVision-Full**, outperforming QVQ-72B Preview (35.9) [p. 12, Table 2]

### K1.5 short-CoT model [p. 12]

The performance of the Kimi k1.5 short-CoT model is presented in Table 3 [p. 12]. This model integrates several techniques, including traditional supervised fine-tuning (discussed in Section 2.5.2), reinforcement learning (explored in Section 2.3), and long-to-short distillation (outlined in Section 2.4) [p. 12]. The results demonstrate that the k1.5 short-CoT model delivers competitive or superior performance compared to leading open-source and proprietary models across multiple tasks [p. 12]. These include text, vision, and reasoning challenges, with notable strengths in natural language understanding, mathematics, coding, and logical reasoning [p. 12].

**Table 3: Performance of Kimi k1.5 short-CoT and flagship open-source and proprietary models** [p. 12]

VLM model performance were obtained from the OpenCompass benchmark platform (https://opencompass.org.cn/) [p. 12].

|                          |                            | Language-only Model |                |            | Vision-Language Model |                    |            |         |
|--------------------------|----------------------------|---------------------|----------------|------------|-----------------------|--------------------|------------|---------|
| Benchmark (Metric)       |                            | Qwen2.5 72B-Inst.  | LLaMA-3.1 405B-Inst. | DeepSeek V3 | Qwen2-VL          | Claude-3.5-Sonnet-1022 | GPT-4o 0513 | Kimi k1.5 |
| **Text**                | MMLU (EM)                  | 85.3               | 88.6           | 88.5       | -                     | 88.3               | 87.2       | **87.4** |
|                          | IF-Eval (Prompt Strict)    | 84.1               | 86.0           | 86.1       | -                     | 86.5               | 84.3       | **87.2** |
|                          | CLUEWSC (EM)               | 91.4               | 84.7           | 90.9       | -                     | 85.4               | 87.9       | **91.7** |
|                          | C-Eval (EM)                | 86.1               | 61.5           | 86.5       | -                     | 76.7               | 76.0       | **88.3** |
| **Reasoning**           | MATH-500 (EM)              | 80.0               | 73.8           | 90.2       | -                     | 78.3               | 74.6       | **94.6** |
|                          | AIME 2024 (Pass@1)         | 23.3               | 23.3           | 39.2       | -                     | 16.0               | 9.3        | **60.8** |
|                          | HumanEval-Mul (Pass@1)     | 77.3               | 77.2           | **82.6**   | -                     | 81.7               | 80.5       | 81.5     |
|                          | LiveCodeBench (Pass@1)     | 31.1               | 28.4           | 40.5       | -                     | 36.3               | 33.4       | **47.3** |
| **Vision**              | MathVista-Test (Pass@1)    | -                  | -              | -          | 69.7                  | 65.3               | 63.8       | **70.1** |
|                          | MMMU-Val (Pass@1)          | -                  | -              | -          | 64.5                  | 66.4               | **69.1**   | 68.0     |
|                          | MathVision-Full (Pass@1)   | -                  | -              | -          | 26.6                  | **35.6**           | 30.4       | 31.0     |

The k1.5 short-CoT model achieves:
- **94.6 EM on MATH-500**, outperforming DeepSeek V3 (90.2), Qwen2.5 72B (80.0), Claude-3.5-Sonnet (78.3), and GPT-4o (74.6) by up to 27% [p. 12, Table 3]
- **60.8 Pass@1 on AIME 2024**, substantially exceeding DeepSeek V3 (39.2), Qwen2.5 72B (23.3), Claude-3.5-Sonnet (16.0), and GPT-4o (9.3) by up to 550% [p. 12, Table 3]
- **47.3 Pass@1 on LiveCodeBench**, surpassing DeepSeek V3 (40.5), Claude-3.5-Sonnet (36.3), and GPT-4o (33.4) [p. 12, Table 3]
- **88.3 EM on C-Eval**, outperforming DeepSeek V3 (86.5) and all compared models [p. 12, Table 3]

## 3.3 Long Context Scaling [p. 12]

The authors employ a mid-sized model to study the scaling properties of RL with LLMs [p. 12-13].

**Figure 5** (p. 13): "The changes on the training accuracy and length as train iterations grow. Note that the scores above come from an internal long-cot model with much smaller model size than k1.5 long-CoT model. The shaded area represents the 95% percentile of the response length."

Description: Multi-panel line chart showing 12 different benchmarks (total@temp_1.0, OMNI-MATH500, MATH500, AIMO2024, AIME2024, ChatGLMMath, GAOKAO, GPQA, Biology, Chemistry, Physics, KAOYAN)
- Key elements: Each panel shows accuracy (solid line, left y-axis) and token length (shaded area, right y-axis) over 150 training iterations
- Notable patterns: As training progresses, there is a concurrent increase in both response length and performance accuracy across all benchmarks. More challenging benchmarks (e.g., AIMO2024, AIME2024) exhibit a steeper increase in response length, suggesting that the model learns to generate more elaborate solutions for complex problems [p. 13]
- Supports claim: Long context scaling enables continued improvement on hard reasoning benchmarks

**Figure 6** (p. 13): "Model Performance Increases with Response Length"

Description: Multi-panel scatter plot showing 8 benchmarks (total@temp_1.0, OMNI-MATH500, MATH500, AIMO2024, AIME2024, ChatGLMMath, GAOKAO_bmk, GPQA)
- Key elements: Each panel shows accuracy (y-axis) vs. mean token length (x-axis) with trend lines and slope values
- Notable patterns: Strong positive correlation between model output context length and problem-solving capabilities across all benchmarks. Trend slopes range from 1.36e-05 (MATH500) to 4.24e-05 (GPQA) [p. 13]
- Supports claim: Figure 6 indicates a strong correlation between the model's output context length and its problem-solving capabilities. The final run of k1.5 scales to 128k context length and observes continued improvement on hard reasoning benchmarks [p. 13]
