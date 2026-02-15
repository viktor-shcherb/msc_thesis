# 4.2 Kimi-VL-A3B-Thinking: A Reasoning Extension of Kimi-VL [p. 16-18]

Furthermore, we conduct a reasoning extension to empower Kimi-VL to reason with CoT and present a long-thinking version of the model, Kimi-VL-Thinking, through SFT and reinforcement learning. We validate its superior performance on several image benchmarks, as shown in Table 4.

Kimi-VL-Thinking significantly improves upon the base Kimi-VL model, with gains of 2.6% on MathVista, 4.7% on MMMU, and 15.4% on MathVision, demonstrating its capability to leverage test-time computation for deeper reasoning and better handling of complex multimodal queries. In Table 4, Kimi-VL-Thinking further outperforms or rivals state-of-the-art thinking and non-thinking models on several key benchmarks. Specifically, it achieves 71.3% on MathVista, outperforming GPT-4o (63.8%) and GPT-4o-mini (56.7%); scoring 61.7% on MMMU, surpassing GPT-4o-mini (60.0%) and Qwen2.5-VL-7B (58.6%); and reaching 36.8% on MathVision, exceeding GPT-4o (30.4%) and Gemma-3-27B-IT (35.5%), even QVQ-72B (35.9%). While marginally behind some larger-scale models on select benchmarks, Kimi-VL-Thinking accomplishes these results with only 3B activated parameters -- orders of magnitude fewer than its counterparts -- underscoring its strong efficiency and effectiveness in multimodal reasoning.

**Figure 12** (p. 17): "Catching and understanding key details from an hour-long video course. Kimi-VL demonstrates its ability to comprehend and interpret instructional video content by analyzing lecture sequences and extracting conceptual progression over time. In this case, the model identifies a deepening of the traditional saying 'Teach a man to fish, and you feed him for a lifetime' into a more nuanced idea: 'Teach him the taste of fish and make him hungry.'"

Description: Two-panel video understanding example
- Key elements: Top panel shows "Instruction" with old Chinese saying and video frames from presentation. Bottom panel shows "Response" with detailed interpretation
- Notable patterns: Nine video frames showing presenter at different timestamps (00:00 to 35:55). Response explains requirement to teach taste of fish and make hungry, implying importance of inspiring and motivating learners to seek out new challenges
- Supports claim: Demonstrates ability to comprehend and interpret instructional video content over long duration, extracting conceptual progression

**Table 4** (p. 17): "Performance of Kimi-VL-Thinking and Kimi-VL-Thinking-2506 on multimodal reasoning benchmarks. The metrics evaluated include MathVista (mini), MMMU (val) and VideoMMMU, with results expressed in Pass@1. The Kimi-VL-Thinking-2506 performs well in most cases, showcasing the enhanced reasoning and processing capabilities of the 'thinking' variant across different domains and scales."

| Benchmark (Metric) | GPT-4o | GPT-4o-mini | Qwen2.5-VL-72B | Qwen2.5-VL-7B | Gemma-3-27B | Gemma-3-12B | o1-1217 | QVQ-72B-Preview | Kimi-k1.5 | Kimi-VL-A3B-Thinking | Kimi-VL-A3B-Thinking-2506 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| MathVision (full) (Pass@1) | 30.4 | - | 38.1 | 25.1 | 35.5 | 32.1 | - | 35.9 | 38.6 | 36.8 | **56.9** |
| MathVista (mini) (Pass@1) | 63.8 | 56.7 | 74.8 | 68.2 | 62.3 | 56.4 | 71.0 | 71.4 | 74.9 | 71.3 | **80.1** |
| MMMU (val) (Pass@1) | 69.1 | 60.0 | 74.8 | 58.6 | 64.8 | 59.6 | **77.3** | 70.3 | 70.0 | 61.7 | 64.0 |
| MMMU-Pro (avg) (Pass@1) | **51.7** | 37.6 | 51.1 | 38.1 | - | 32.1 | - | - | - | 43.0 | 46.3 |
| VideoMMMU (Pass@1) | 61.1 | - | 60.2 | 47.0 | 61.8 | 57.2 | - | - | - | 55.5 | **65.2** |

Our Kimi-VL-Thinking model also exhibits strong test-time scaling properties, as shown in Figure 13. Specifically, increasing the max thinking token length at inference time consistently improves test-time accuracy across all three benchmarks. For example, on **MathVision**, the accuracy rises steadily from 18.7% at 1k tokens to 36.8% at 16k tokens, and similar upward trend is also observed for MathVista, indicating that the model is able to utilize longer reasoning chains for better performance. However, not all benchmarks benefit equally from longer thinking lengths. On **MathVista**, performance saturates early, with accuracy reaching 70.9% at 4k tokens and showing no further significant gains as the token length increases to 16k. It suggests that for this task, the necessary reasoning depth is already captured within a relatively short context, and additional computation does not yield further improvements.

**Figure 13** (p. 18): "Test-time accuracy when scaling the max thinking token length of our Kimi-VL-Thinking model."

Description: Three scatter plots showing test-time scaling
- Key elements: Three separate plots for MathVision, MathVista, and MMMU. X-axis shows "Max Thinking Length (k tokens)" from 1 to 16. Y-axis shows "Best 1-T Test Accuracy (%)"
- Notable patterns: MathVision shows steady increase from 18.7% (1k) → 22.6% (2k) → 29.0% (4k) → 34.0% (8k) → 36.8% (16k). MathVista shows increase from 66.7% (1k) → 69.0% (2k) → 70.9% (4k) → 70.6% (8k) → 71.3% (16k) with early saturation around 4k. MMMU shows increase from 49.2% (1k) → 52.4% (2k) → 56.2% (4k) → 60.1% (8k) → 61.7% (16k)
- Supports claim: Demonstrates test-time scaling properties where longer thinking token lengths generally improve accuracy, though benefits vary by benchmark

## 4.3 Kimi-VL-A3B-Thinking-2506: From Reasoning Extension to Integrated Thinking Model [p. 18-19]

**Table 5** (p. 18): "Performance of Kimi-VL-A3B-Thinking-2506 on multimodal benchmarks that do not require extensive reasoning."

| Benchmark (Metric) | GPT-4o | Qwen2.5-VL-7B | Gemma3-12B-IT | Kimi-VL-A3B-Instruct | Kimi-VL-A3B-Thinking | Kimi-VL-A3B-Thinking-2506 |
|-------------------|--------|---------------|---------------|----------------------|----------------------|---------------------------|
| **General Multimodal** | | | | | | |
| MMBench-EN-v1.1 (Acc) | 83.1 | 83.2 | 74.6 | 82.9 | 76.0 | **84.4** |
| RealWorldQA (Acc) | 75.4 | 68.5 | 59.1 | 68.1 | 64.0 | **70.0** |
| OCRBench (Acc) | 815 | 864 | 702 | 864 | 864 | **869** |
| MMStar (Acc) | 64.0 | 63.0 | 56.1 | 61.7 | 64.2 | **70.4** |
| MMVet (Acc) | 69.1 | 67.1 | 64.9 | 66.7 | 69.5 | **78.1** |
| **Video** | | | | | | |
| MMVU_val (Pass@1) | 67.4 | 50.1 | 57.0 | 52.7 | 53.0 | **57.5** |
| Video-MME (w/ sub.) (Acc) | 77.2 | 71.6 | 62.1 | **72.7** | 66.0 | 71.9 |
| **OS-Agent Grounding** | | | | | | |
| ScreenSpot-Pro (Acc) | 0.8 | 29.0 | — | 35.4 | — | **52.8** |
| ScreenSpot-V2 (Acc) | 18.1 | 84.2 | — | **92.8** | — | 91.4 |
| OSWorld-G (Acc) | - | 31.5 | — | 41.6 | — | **52.5** |
| **Long Document** | | | | | | |
| MMLongBench-Doc (Acc) | 42.8 | 29.6 | 21.3 | 35.1 | 32.5 | **42.1** |

While Kimi-VL-A3B-Thinking shows excellent thinking abilities on hard reasoning tasks, we further provide the updated **Kimi-VL-A3B-Thinking-2506**², a new reasoning variant that is not only smarter, but integrates key abilities of Kimi-VL-A3B-Instruct (perception, video, long-document, and OS-agent abilities) into this thinking model.

Kimi-VL-Thinking-2506 significantly improves reasoning efficiency while reducing token consumption. As shown in Table 4, Kimi-VL-Thinking-2506 achieves 56.9% on MathVision (+20.1% improvement on original Kimi-VL-Thinking), 80.1% on MathVista (+8.4%), 46.3% on MMMU-Pro (+3.2%), and 64.0% on MMMU (+2.1%), demonstrating non-trivial gains across multiple reasoning benchmarks. Meanwhile, while solving these hard reasoning problems, the 2506 version reduces the average output token length by around 20% (*e.g.*, 2.9K → 2.4K on MMMU-val and 5.8K → 4.4K on MathVision), facilitating it to be more efficient and user-friendly for practical deployments.

Beyond extensive reasoning tasks, Kimi-VL-Thinking-2506 demonstrates stronger visual perception capabilities (Table 5). Compared to the previous non-thinking model (Kimi-VL-A3B-Instruct), Kimi-VL-A3B-Thinking-2506 achieves competitive or superior results on general multimodal understanding benchmarks: 84.4% on MMBench-EN-v1.1, 70.4% on MMStar, 70.0% on RealWorldQA, and 78.4% on MMVet, underscoring its broader competence in vision-language tasks. In terms of token efficiency, the 2506 version only requires in average 180 tokens per answer when solving MMBench, 1/3 compared to the previous thinking model while improving 8.4% accuracy.

Kimi-VL-A3B-Thinking-2506 also extends its reasoning ability to video and long-context domains. It establishes new state-of-the-art results among open-source models on VideoMMMU (65.2%, 4% better than GPT-4o), a challenging video reasoning benchmark; it also maintains general understanding performance with 71.9% on Video-MME, matching the long video understanding ability of Kimi-VL-A3B-Instruct. It also scores 42.1% (first open-source model matching GPT-4o) on MMLongBench-Doc (Table 5), representing a 10% improvement over the previous thinking model and 7% over the previous instruct model, demonstrating its robust ability on broader long-form visual inputs.

As mentioned in the method part, the continual training on MoonViT (3.2 million max input pixels) of Kimi-VL-A3B-Thinking-2506 leads to substantial improvements on high-resolution perception and OS grounding benchmarks, achieving 83.2% on V* Benchmark (without external tools), 52.8% on ScreenSpot-Pro, and 52.5% on OSWorld-G (full set with refusal samples), showing huge gains over the previous thinking variants. We hope that this high-resolution multimodal reasoning model brings about interesting new capabilities in the real world.
