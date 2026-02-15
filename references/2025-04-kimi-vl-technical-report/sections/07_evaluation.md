# 4 Evaluation [p. 10]

We begin by presenting our comprehensive model and conducting a comparative analysis with leading state-of-the-art (SoTA) solutions. Following this introduction, we proceed to assess various sub-capabilities of the model through detailed performance evaluations. This part examines how effectively the model handles different tasks and scenarios, providing insights into its strengths and limitations across diverse functional domains.

## 4.1 Comparison to the State-of-the-Art Models [p. 10-11]

**Table 3** (p. 11): "Performance of Kimi-VL against proprietary and open-source efficient VLMs; performance of GPT-4o is also listed in grey for reference. Top and second-best results are in boldface and underline respectively. Some results of competing models are unavailable due to limitation of model ability on specific tasks or model context length."

| Benchmark (Metric) | GPT-4o | GPT-4o-mini | Qwen2.5-VL-7B | Llama3.2-11B-Inst. | Gemma3-12B-IT | DeepSeek-VL2 | Kimi-VL-A3B |
|-------------------|--------|-------------|---------------|---------------------|-----------------|--------------|-------------|
| Architecture | - | - | Dense | Dense | Dense | MoE | MoE |
| # Act. Params (LLM+VT) | - | - | 7.6B+0.7B | 8B+2.6B | 12B+0.4B | 4.1B+0.4B | 2.8B+0.4B |
| # Total Params | - | - | 8B | 11B | 12B | 28B | 16B |
| **College-level** MMMU_val (Pass@1) | 69.1 | **60.0** | 58.6 | 48 | 59.6 | 51.1 | 57.0 |
| VideoMMMU (Pass@1) | 61.2 | - | 47.4 | 41.8 | **57.2** | 44.4 | 52.6 |
| MMVU_val (Pass@1) | 67.4 | **61.6** | 50.1 | 44.4 | 57.0 | 52.1 | 52.2 |
| **General** MMBench-EN-v1.1 (Acc) | **83.1** | 77.1 | 82.6 | 65.8 | 74.6 | 79.6 | **83.1** |
| MMStar (Acc) | 64.7 | 54.8 | **63.9** | 49.8 | 56.1 | 55.5 | 61.3 |
| MMVet (Pass@1) | 69.1 | 66.9 | 67.1 | 57.6 | 64.9 | 60.0 | **66.7** |
| RealWorldQA (Acc) | 75.4 | 67.1 | **68.5** | 63.3 | 59.1 | 68.4 | 68.1 |
| AI2D (Acc) | 84.6 | 77.8 | 83.9 | 77.3 | 78.1 | 81.4 | **84.9** |
| **Multi-image** BLINK (Acc) | 68.0 | 53.6 | 56.4 | 39.8 | 50.3 | - | **57.3** |
| **Math** MathVista (Pass@1) | 63.8 | 52.5 | 68.2 | 47.7 | 56.1 | 62.8 | **68.7** |
| MathVision (Pass@1) | 30.4 | - | 25.1 | 13.6 | **32.1** | 17.3 | 21.4 |
| **OCR** InfoVQA (Acc) | 80.7 | 57.9 | 82.6 | 34.6 | 43.8 | 78.1 | **83.2** |
| OCRBench (Acc) | 815 | 785 | 864 | 753 | 702 | 811 | **867** |
| **OS Agent** ScreenSpot-V2 (Acc) | 18.1 | - | 86.8 | - | - | - | **92.8** |
| ScreenSpot-Pro (Acc) | 0.8 | - | 29.0 | - | - | - | **34.5** |
| OSWorld (Pass@1) | 5.03 | - | 2.8 | - | - | - | **8.22** |
| WindowsAgentArena (Pass@1) | 9.4 | 2.7 | 3.4 | - | - | - | **10.4** |
| **Long Document** MMLongBench-Doc (Acc) | 42.8 | 29.0 | 29.6 | 13.8 | 21.3 | - | **35.1** |
| **Long Video** Video-MME (w/o sub / w/ sub) | 71.9/77.2 | 64.8/68.9 | 65.1/71.6 | 46.0/49.5 | 58.2/62.1 | - | **67.8/72.6** |
| MLVU_MCQ (Acc) | 64.6 | 48.1 | 70.2 | 44.4 | 52.3 | - | **74.2** |
| LongVideoBench_all | 66.7 | 58.2 | 56.0 | 45.5 | 51.5 | - | **64.5** |
| **Video Perception** EgoSchema_full | 72.2 | - | 65.0 | 54.3 | 56.9 | 38.5 | **78.5** |
| VSI-Bench | 34.0 | - | 34.2 | 20.6 | 32.4 | 21.7 | **37.4** |
| TOMATO | 37.7 | 28.8 | 27.6 | 21.5 | 28.6 | 27.2 | **31.7** |

Table 3 presents a comprehensive evaluation of Kimi-VL against state-of-the-art vision-language models across multiple benchmarks. Although having a more parameter-efficient architecture (2.8B+0.4B activated parameters) compared to larger models such as GPT-4o, Llama-3.2-11B-Inst, and Qwen2.5-VL-7B (actually 8.3B) on 12B-1T, Kimi-VL demonstrates competitive or superior performance in several key areas. Our model employs a Mixture-of-Experts (MoE) architecture similar to DeepSeek-VL2, but outperforms it on most benchmarks with significantly fewer parameters (activated: 2.8B vs 4.5B; total: 16B vs 28B); it also outperforms Qwen2.5-VL-7B (actually 8.3B) on 19 out of 24 benchmarks, though the latter

---
[p. 11 continued]

has 2.59× more activated parameters. The following sections analyze performance across specific domains, which reveals Kimi-VL's strengths in OCR, math, agent, long-form content understanding, multi-image and video perception.

### 4.1.1 College-level Academic Problems [p. 11]

Our Kimi-VL model demonstrates competitive performance on college-level academic benchmarks. On MMMU validation set, it achieves a score of 57.0%, which outperforms DeepSeek-VL2 (51.1%) and is comparable to Qwen2.5-VL-7B (58.6%) and even Gemma-3-12B-IT (59.6%), despite having significantly fewer activated parameters. On video college-level problems, it significantly outperforms Qwen2.5-VL-7B and DeepSeek-VL2, only behind >10B Gemma-3-12B-IT, demonstrating reasonable university-level understanding capabilities compared to larger models. These results indicate that Kimi-VL effectively balances parameter efficiency with academic reasoning abilities.

**Figure 7** (p. 12): "Kimi-VL exhibits strong visual reasoning capabilities by grounding visual content in spatial, contextual, and cultural knowledge. It accurately identifies matching urban locations based on structural and layout features, interprets scenes from video games like Cyberpunk 2077 using stylistic cues, and recognizes real-world landmarks such as the Rogers Centre in Toronto."

Description: Three-panel visual reasoning example
- Key elements: Three instruction-response pairs showing urban location matching, landmark identification (Rogers Centre, Toronto), and video game scene recognition (Cyberpunk 2077)
- Notable patterns: First panel shows dense urban aerial view question with detailed reasoning about building types, streets, and urban density. Second panel shows CN Tower with detailed identification. Third panel shows Cyberpunk 2077 game scene with stylistic analysis
- Supports claim: Demonstrates visual reasoning capabilities grounded in spatial, contextual, and cultural knowledge

### 4.1.2 General Visual Ability [p. 12]

Kimi-VL exhibits strong general visual understanding capabilities across multiple benchmarks. On MMBench-EN-v1.1, it achieves 83.1% accuracy, outperforming all efficient VLMs in comparison, and performing on par with GPT-4o. For AI2D, our model achieves 84.9% and surpasses all compared models including GPT-4o (84.6%). On MMVet, Kimi-VL scores 66.7% and ties closely with Qwen2.5-VL-7B (67.1%) and GPT-4o-mini (66.9%). For RealWorldQA, it achieves 68.1%, outperforming Gemma3-12B (59.1%) and approaching Qwen2.5-VL-7B (68.5%). These results demonstrate that our model maintains robust general visual understanding capabilities despite its compact architecture.

In multi-image reasoning tasks, Kimi-VL shows promising capabilities with a score of 57.3% on the BLINK benchmark. This performance surpasses Qwen2.5-VL-7B (56.4%), GPT-4o-mini (53.6%), Gemma3-12B-IT (50.3%), and Llama3.2-11B-Inst. (39.8%). The ability to reason across multiple images requires understanding spatial and temporal relationships between visual elements, which our model handles effectively with fewer parameters than most competitors.

### 4.1.3 Mathematical Reasoning [p. 12-13]

With its relatively small scale, Kimi-VL also demonstrates strong mathematical reasoning capabilities, particularly on the MathVista benchmark where it achieves 68.7%, outperforming all compared models including GPT-4o (63.8%) and Qwen2.5-VL-7B (68.2%). It indicates our model's exceptional ability to understand and solve mathematical problems

**Figure 8** (p. 13): "Kimi-VL demonstrates its capability to perform symbolic reasoning and geometric inference by solving a circle geometry problem step by step. The model analyzes given conditions, applies geometric theorems such as the inscribed angle theorem and properties of triangle angles, and accurately derives the target angle."

Description: Instruction-response pair showing geometric problem solving
- Key elements: Top shows circle geometry diagram with Chinese instruction about finding angles. Bottom shows detailed step-by-step solution in Chinese with mathematical reasoning
- Notable patterns: Structured solution approach: 1) analyzing inscribed angles, 2) applying angular relationships, 3) calculating target angle, yielding final answers of 28°
- Supports claim: Demonstrates symbolic reasoning and geometric inference capabilities through systematic problem-solving

presented in visual contexts. On the more challenging MathVision benchmark, due to limited activated parameters, Kimi-VL outperforms DeepSeek-VL2 (17.3%), but falls behind Qwen2.5-VL-7B and Gemma-12B-IT. Nevertheless, through RL and test-time scaling, Kimi-VL-Thinking has significantly improved and already on par with 30B-level VLMs (see Table 4). These results highlight our model's effectiveness in combining visual perception with mathematical problem-solving, an essential capability for real-world applications.

### 4.1.4 Document Understanding and OCR [p. 13]

Kimi-VL excels in document understanding and OCR tasks across all benchmarks in this category. On InfoVQA, it achieves 83.2% accuracy, outperforming GPT-4o-mini (57.9%) and DeepSeek-VL2 (78.1%). For OCRBench, our model scores 86.7%, surpassing all other models including GPT-4o-mini (78.5%) and DeepSeek-VL2 (81.1%). These results demonstrate that our model has exceptional text recognition and document understanding capabilities, making it especially suitable for applications involving document processing and information extraction.

**Figure 9** (p. 14): "Diverse OCR visualization. Kimi-VL demonstrates strong OCR capabilities across varied content types, including structured financial tables, complex mathematical formulas, and handwritten Chinese text. The model accurately parses tabular data into markdown, converts formulas to LaTeX, and transcribes handwritten paragraphs with contextual understanding, showcasing its versatility in multimodal text extraction and interpretation."

Description: Three-panel OCR example
- Key elements: Left panel shows financial table with instruction and response parsing it to markdown. Middle panel shows complex mathematical formulas with LaTeX conversion. Right panel shows handwritten Chinese text with transcription
- Notable patterns: Structured data extraction from tables, formula recognition and LaTeX conversion, handwritten text recognition with contextual understanding
- Supports claim: Demonstrates versatile OCR capabilities across structured tables, mathematical notation, and handwritten text

### 4.1.5 Agent Grounding and Multi-turn Agent Interaction [p. 13]

In agent-based tasks, Kimi-VL demonstrates remarkable performance. On single-step grounding, our model shows strong accuracy, with 92.0% on ScreenSpot-V2 and 34.5% on the more difficult ScreenSpot-Pro (on 4K screens), proving its strong agent grounding abilities. More importantly, it also shows strong multi-step turn agent interaction abilities: For OSWorld, Kimi-VL reaches 8.22%, outperforming GPT-4o (5.03%) and other capable open-source models; On WindowsAgentArena, our model achieves 10.4%, also surpassing GPT-4o (9.4%) and others. These results highlight Kimi-VL's exceptional ability to understand and interact with operating system interfaces, suggesting strong potential for applications in automated UI navigation and task execution.

**Figure 10** (p. 15): "Kimi-VL is capable of following multi-step reasoning processes to complete complex GUI tasks. In this example, it successfully enables the 'Do Not Track' feature in the Chrome browser to enhance online privacy. The agent interprets each screen, identifies relevant UI elements, and performs the appropriate actions sequentially with clear thoughts, actions, and API calls."

Description: Multi-step GUI task completion visualization
- Key elements: 12-step sequence showing Chrome browser privacy settings navigation. Each step includes screenshot, thought process, action, and toolcall details
- Notable patterns: Sequential reasoning through complex UI navigation: opening settings, finding privacy options, locating "Do Not Track", enabling the feature, and verification. Includes detailed reasoning at each step with specific UI element identification
- Supports claim: Demonstrates multi-turn agent interaction capabilities through systematic GUI task completion

### 4.1.6 Long Document and Long Video Understanding [p. 14]

Kimi-VL demonstrates competitive performance in long-form content understanding. On MMLongBench-Doc, a challenging benchmark with question-answering over long documents, it achieves 35.1%, outperforming GPT-4o-mini (29.0%) and Qwen2.5-VL-7B (29.6%), only behind GPT-4o (42.8%). For long video understanding, on Video-MME, our model outperforms all efficient VLMs with particularly strong subtitle settings where these models have to find answers from video frames instead of hacking from input subtitles; on w/ subtitle setting, it also reaches extraordinary 72.6% accuracy. On the MCQ subset, it achieves an impressive 74.2% score, achieving state-of-the-art and surpassing both GPT-4o (64.6%) and Qwen2.5-VL-7B (70.2%). For LongVideoBench, it scores 64.5%, outperforming all compared models except GPT-4o (66.7%). These results demonstrate Kimi-VL 's strong capability to understand long-form PDFs and videos.

**Figure 11** (p. 16): "Video scene splitting. Kimi-VL processes a long-form video by segmenting it into coherent scenes and providing detailed start/end timestamps along with fine-grained natural language descriptions for each scene."

Description: Two-panel video scene splitting visualization
- Key elements: Left panel shows grid of video frames from different scenes. Right panel shows detailed response with timestamps and descriptions
- Notable patterns: The response provides start and end timestamps for multiple scenes with detailed natural language descriptions of visual content, actions, and context for each scene segment
- Supports claim: Demonstrates long video understanding through temporal segmentation and detailed scene-level description

### 4.1.7 Egocentric and Fine-grained Video Perception [p. 14]

Kimi-VL also shows strong performance in more nuanced video perception tasks. On EgoSchema full set (hidden test set), it achieves 78.5%, significantly outperforming GPT-4o (72.2%), Qwen2.5-VL-7B (65.0%). For VSI-Bench, a very tough benchmark that requires identifying multiple visual details and correspondences of multiple objects in a video, our model scores 37.4%, surpassing GPT-4o (34.0%) and Qwen2.5-VL-7B (34.2%). In TOMATO that examines fine-grained temporal perception of VLMs, Kimi-VL reaches 31.7%, outperforming Qwen2.5-VL-7B (27.6%) and GPT-4o-Mini (28.8%). These results demonstrate our model's strong capability to understand dynamic visual content, track objects over time, and interpret complex actions in video sequences, making it well-suited for applications requiring temporal visual understanding.
