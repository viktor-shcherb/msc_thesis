# 1 Introduction [p. 2]

With the rapid advancement of artificial intelligence, human expectations for AI assistants have transcended traditional language-only interactions, increasingly aligning with the inherently multimodal nature of our world. To better understand and interact with these expectations, new generations of natively multimodal models, such as GPT-4o (OpenAI et al. 2024) and Google Gemini (Gemini Team et al. 2024), have emerged with the capability to seamlessly perceive and interpret visual inputs. Very recently, advanced multimodal models, pioneered by OpenAI o1 series (OpenAI 2024) and Kimi k1.5 (K. Team et al. 2025), have further pushed these boundaries by incorporating deeper and longer reasoning on multimodal inputs, thereby tackling more complex problems in the multimodal domain.

Nevertheless, development in large VLMs in the open-source community has significantly lagged behind their language-only counterparts, particularly in aspects of scalability, computational efficiency, and advanced reasoning capabilities. While language-only model DeepSeek R1 (DeepSeek-AI, D. Guo, et al. 2025) has already leveraged the efficient and more scalable mixture-of-experts (MoE) architecture and facilitated sophisticated long chain-of-thought (CoT) reasoning, most recent open-source VLMs, e.g. Qwen2.5-VL (Bai et al. 2025) and Gemma-3 (Gemma Team et al. 2025), continue to rely on dense architectures and do not support long-CoT reasoning. Early explorations into MoE-based vision-language models, such as DeepSeek-VL2 (Zhiyu Wu et al. 2024) and Aria (D. Li et al. 2024), exhibit limitations in other crucial dimensions. Architecturally, both models still adopt relatively traditional vision encoders, hindering their adaptability to diverse visual inputs. From a capability perspective, DeepSeek-VL2 supports only a limited context length (4K), while Aria falls short in fine-grained visual tasks. Additionally, neither of them supports long-video abilities. Consequently, there remains a pressing need for an open-source VLM that effectively integrates structural innovation, stable capabilities, and enhanced reasoning through long-thinking.

In light of this, we present **Kimi-VL**, a vision-language model from the open-source community. Structurally, Kimi-VL consists of our Moonlight (J. Liu et al. 2025a) MoE language model with only **2.8B activated (16B total) parameters**, paired with a 400M native-resolution MoonViT vision encoder. In terms of capability, as illustrated in Figure 2, Kimi-VL can robustly handle diverse tasks (fine-grained perception, math, college-level problems, OCR, agent, etc.) across a broad spectrum of input forms (single-image, multi-image, video, long-document, etc.). Specifically, it features the following exciting abilities:

**1) Kimi-VL is smart**: it has comparable text ability against efficient pure-text LLMs; without long thinking, Kimi-VL is already competitive in multimodal reasoning and multi-turn agent benchmarks, e.g., MMMU, MathVista, OSWorld.

**2) Kimi-VL processes long**: it effectively tackles long-context understanding on various multimodal inputs within its 128K context window, far ahead of similar-scale competitors on long video benchmarks and MMLongBench-Doc.

**3) Kimi-VL perceives clear**: it shows all-round competitive ability over existing efficient dense and MoE VLMs in various vision-language scenarios: visual perception, visual world knowledge, OCR, high-resolution OS screenshot, etc.

Furthermore, with long-CoT activation and reinforcement learning (RL), we introduce the long-thinking version of Kimi-VL, **Kimi-VL-Thinking**, which further substantially improves performance on more complex multimodal reasoning scenarios. Despite its small scale, Kimi-VL-Thinking offers compelling performance on hard reasoning benchmarks (e.g., MMMU, MathVision, MathVista), outperforming many state-of-the-art VLMs with even larger sizes. We further release and improved version of the thinking model, **Kimi-VL-Thinking-2506**. The improved version has even better performance on these reasoning benchmarks while retaining or improving on common visual perception and understanding scenarios, e.g. high-resolution perception (V*), OS grounding, video and long document understanding.

**Figure 2** (p. 2): "Highlights of Kimi-VL performance for a wide range of benchmarks like, general benchmarks (MMMU, MMBench), OCR (InfoVQA), multi-image (BLINK), long video (LongVideoBench, Video-MME), long document (MMLongBench-Doc), and agent (ScreenSpot-Pro and OSWorld). Detailed results are presented in Table 3."

Description: Multi-panel bar chart
- Key elements: 8 benchmark categories shown as separate bar charts. Each shows performance comparison between Kimi-VL-A3B (blue bars), Qwen2.5-VL-7B (gray), DeepSeek-VL2 (gray), GPT-4o/GPT-4o-mini (tan/beige), Llama-3.2-11B-Inst (tan), Gemma-3-12B-IT (tan)
- Notable patterns:
  - MMMU (val): Kimi-VL 57.0, comparable to Qwen2.5-VL-7B 57.1
  - MMBench-EN-v1.1: Kimi-VL 80.1
  - InfoVQA: Kimi-VL 69.6 (highest shown)
  - BLINK: Kimi-VL 57.3
  - LongVideoBench: Kimi-VL 64.5 (highest shown)
  - Video-MME (w/o sub): Kimi-VL 67.6
  - MMLongBench-Doc: Kimi-VL 35.1
  - ScreenSpot-Pro: Kimi-VL 34.5
  - OSWorld (Pass@1): Kimi-VL 8.2
- Supports claim: Demonstrates Kimi-VL's competitive or superior performance across diverse benchmark categories compared to larger models
