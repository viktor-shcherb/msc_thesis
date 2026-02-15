# Overview

**Title:** Kimi-VL Technical Report

**Authors:** Kimi Team

**Affiliations:** Not specified in pages 1-6

**Venue:** arXiv preprint arXiv:2504.07491v3 [cs.CV]

**Date:** 23 Jun 2025

## Abstract

> "We present Kimi-VL, an efficient open-source Mixture-of-Experts (MoE) vision-language model (VLM) that offers advanced multimodal reasoning, long-context understanding, and strong agent capabilities—all while activating only 2.8B parameters in its language decoder (Kimi-VL-A3B). Kimi-VL demonstrates strong performance across challenging domains: as a general-purpose VLM, Kimi-VL excels in multi-turn agent tasks (e.g., OSWorld), matching flagship models. Furthermore, it exhibits remarkable capabilities across diverse challenging vision language tasks, including college-level image and video comprehension, OCR, mathematical reasoning, multi-image understanding. In comparative evaluations, it effectively competes with cutting-edge efficient VLMs such as GPT-4o-mini, Qwen2.5-VL-7B, and Gemma-3-12B-IT, while surpassing GPT-4o in several key domains. Kimi-VL also advances in processing long contexts and perceiving clearly. With a 128K extended context window, Kimi-VL can process diverse long inputs, achieving impressive scores of 64.5 on LongVideoBench and 35.1 on MMLongBench-Doc. Its native-resolution vision encoder, MoonViT, further allows it to see and understand ultra-high-resolution visual inputs, achieving 83.2 on InfoVQA and 34.5 on ScreenSpot-Pro, while maintaining lower computational cost for common tasks.
>
> Building upon Kimi-VL, we introduce an advanced long-thinking variant: Kimi-VL-Thinking-2506. Developed through long chain-of-thought (CoT) supervised fine-tuning (SFT) and reinforcement learning (RL), the latest model exhibits strong long-horizon reasoning capabilities (64.0 on MMMU, 46.3 on MMMU-Pro, 56.9 on MathVision, 80.1 on MathVista, 65.2 on VideoMMMU) while obtaining robust general abilities (84.4 on MMBench, 83.2 on V* and 52.8 on ScreenSpot-Pro). With only around 3B activated parameters, it sets a new standard for efficient yet capable multimodal thinking models. Code and models are publicly accessible at https://github.com/MoonshotAI/Kimi-VL." [p. 1]

## Section Headings

1. Introduction [p. 2]
2. Approach [p. 3]
   - 2.1 Model Architecture [p. 3]
   - 2.2 Muon Optimizer [p. 4]
   - 2.3 Pre-Training Stages [p. 4]
   - 2.4 Post-Training Stages [p. 6]
   - 2.5 Infrastructure [p. 7]
3. Data Construction [p. 8]
   - 3.1 Pre-Training Data [p. 8]
   - 3.2 Instruction Data [p. 10]
   - 3.3 Reasoning Data [p. 10]
4. Evaluation [p. 10]
   - 4.1 Comparison to the State-of-the-Art Models [p. 10]
   - 4.1.1 College-level Academic Problems [p. 11]
   - 4.1.2 General Visual Ability [p. 12]
   - 4.1.3 Mathematical Reasoning [p. 12]
   - 4.1.4 Document Understanding and OCR [p. 13]
   - 4.1.5 Agent Grounding and Multi-turn Agent Interaction [p. 13]
   - 4.1.6 Long Document and Long Video Understanding [p. 14]
   - 4.1.7 Egocentric and Fine-grained Video Perception [p. 14]
   - 4.2 Kimi-VL-A3B-Thinking: A Reasoning Extension of Kimi-VL [p. 16]
   - 4.3 Kimi-VL-A3B-Thinking-2506: From Reasoning Extension to Integrated Thinking Model [p. 18]
5. Conclusion, Limitation, and Future Work [p. 19]
References [p. 19-21]

## Figures

**Figure 1** (p. 1): "Comparison between Kimi-VL-Thinking-2506 and frontier open-source VLMs, including short-thinking VLMs (e.g. Gemma-3 series, Qwen2.5-VL series) and long-thinking VLMs (QVQ-72B/Max-Preview), on MathVision benchmark. Our model achieves strong multimodal reasoning with just 2.8B LLM activated parameters."

Description: Scatter plot
- Key elements: X-axis shows "Activated Parameters (B)" from approximately 0 to 40B, Y-axis shows "MathVision Result" from approximately 20 to 65
- Notable patterns: Kimi-VL-A3B-Thinking-2506 (blue star, top left) achieves ~64 score with ~3B parameters. Kimi-VL-A3B-Thinking (blue star) at ~31 score. Various baseline models plotted including Gemma-3-12B-IT, Qwen-2.5-VL-7B, DeepSeek-VL2, GPT-4o models, Llama-3.2-11B-Inst. Long-thinking models (QVQ-72B/Max-Preview) shown with dotted trend line.
- Supports claim: Demonstrates Kimi-VL-Thinking-2506's efficiency - achieving competitive or superior performance with significantly fewer activated parameters than other models

**Figure 5** (p. 6): "The post-training stages of Kimi-VL and Kimi-VL-Thinking, including two stages of joint SFT in 32K and 128K context, and further long-CoT SFT and RL stages to activate and enhance long thinking abilities."

Description: Flow diagram
- Key elements: Three blue boxes in sequence showing progressive training stages
- Notable patterns: Progressive enhancement from base SFT to long-CoT to RL
- Supports claim: Shows the post-training pipeline for developing thinking capabilities

**Figure 6** (p. 8): "Manuscript reasoning visualization. Kimi-VL-Thinking demonstrates the ability to perform historical and scientific inference by analyzing handwritten manuscripts step by step. In this example, our model identifies the author as Albert Einstein based on handwriting style, content analysis, and language cues. It reasons that the manuscripts relate to gravitational field equations, consistent with Einstein's contributions to general relativity."

Description: Two-panel visualization
- Key elements: Left panel shows handwritten manuscript with instruction prompt; Right panel shows detailed multi-step reasoning response
- Notable patterns: Structured analysis including handwriting style, content analysis, contextual analysis leading to conclusion
- Supports claim: Demonstrates complex historical and scientific inference capabilities through systematic visual analysis

**Figure 7** (p. 12): "Kimi-VL exhibits strong visual reasoning capabilities by grounding visual content in spatial, contextual, and cultural knowledge. It accurately identifies matching urban locations based on structural and layout features, interprets scenes from video games like Cyberpunk 2077 using stylistic cues, and recognizes real-world landmarks such as the Rogers Centre in Toronto."

Description: Three-panel visual reasoning example
- Key elements: Three instruction-response pairs showing urban location matching, landmark identification, and video game scene recognition
- Notable patterns: Detailed reasoning about building types, streets, urban density; CN Tower identification; Cyberpunk 2077 game scene analysis
- Supports claim: Demonstrates visual reasoning grounded in spatial, contextual, and cultural knowledge

**Figure 8** (p. 13): "Kimi-VL demonstrates its capability to perform symbolic reasoning and geometric inference by solving a circle geometry problem step by step. The model analyzes given conditions, applies geometric theorems such as the inscribed angle theorem and properties of triangle angles, and accurately derives the target angle."

Description: Instruction-response pair showing geometric problem solving
- Key elements: Circle geometry diagram with Chinese instruction; detailed step-by-step solution in Chinese
- Notable patterns: Structured mathematical reasoning with angle calculations yielding final answer of 28°
- Supports claim: Demonstrates symbolic reasoning and geometric inference capabilities

**Figure 9** (p. 14): "Diverse OCR visualization. Kimi-VL demonstrates strong OCR capabilities across varied content types, including structured financial tables, complex mathematical formulas, and handwritten Chinese text. The model accurately parses tabular data into markdown, converts formulas to LaTeX, and transcribes handwritten paragraphs with contextual understanding, showcasing its versatility in multimodal text extraction and interpretation."

Description: Three-panel OCR example
- Key elements: Financial table with markdown parsing; mathematical formulas with LaTeX conversion; handwritten Chinese text transcription
- Notable patterns: Structured data extraction, formula recognition, handwritten text recognition with contextual understanding
- Supports claim: Demonstrates versatile OCR capabilities across multiple content types

**Figure 10** (p. 15): "Kimi-VL is capable of following multi-step reasoning processes to complete complex GUI tasks. In this example, it successfully enables the 'Do Not Track' feature in the Chrome browser to enhance online privacy. The agent interprets each screen, identifies relevant UI elements, and performs the appropriate actions sequentially with clear thoughts, actions, and API calls."

Description: Multi-step GUI task completion visualization
- Key elements: 12-step sequence showing Chrome browser privacy settings navigation with screenshots
- Notable patterns: Sequential reasoning through UI navigation with thought process, action, and toolcall details at each step
- Supports claim: Demonstrates multi-turn agent interaction capabilities through systematic GUI task completion

**Figure 11** (p. 16): "Video scene splitting. Kimi-VL processes a long-form video by segmenting it into coherent scenes and providing detailed start/end timestamps along with fine-grained natural language descriptions for each scene."

Description: Two-panel video scene splitting visualization
- Key elements: Grid of video frames from different scenes; detailed response with timestamps and descriptions
- Notable patterns: Start/end timestamps for multiple scenes with detailed natural language descriptions of visual content, actions, and context
- Supports claim: Demonstrates long video understanding through temporal segmentation and scene-level description

**Figure 12** (p. 17): "Catching and understanding key details from an hour-long video course. Kimi-VL demonstrates its ability to comprehend and interpret instructional video content by analyzing lecture sequences and extracting conceptual progression over time. In this case, the model identifies a deepening of the traditional saying 'Teach a man to fish, and you feed him for a lifetime' into a more nuanced idea: 'Teach him the taste of fish and make him hungry.'"

Description: Two-panel video understanding example
- Key elements: Top panel shows "Instruction" with old Chinese saying and video frames from presentation; Bottom panel shows "Response" with detailed interpretation
- Notable patterns: Nine video frames showing presenter at different timestamps (00:00 to 35:55); Response explains requirement to teach taste of fish and make hungry, implying importance of inspiring learners
- Supports claim: Demonstrates ability to comprehend instructional video content over long duration and extract conceptual progression

**Figure 13** (p. 18): "Test-time accuracy when scaling the max thinking token length of our Kimi-VL-Thinking model."

Description: Three scatter plots showing test-time scaling
- Key elements: Three separate plots for MathVision, MathVista, and MMMU; X-axis shows "Max Thinking Length (k tokens)" from 1 to 16; Y-axis shows "Best 1-T Test Accuracy (%)"
- Notable patterns: MathVision shows steady increase from 18.7% (1k) → 22.6% (2k) → 29.0% (4k) → 34.0% (8k) → 36.8% (16k); MathVista shows increase from 66.7% (1k) → 69.0% (2k) → 70.9% (4k) → 70.6% (8k) → 71.3% (16k) with early saturation; MMMU shows increase from 49.2% (1k) → 52.4% (2k) → 56.2% (4k) → 60.1% (8k) → 61.7% (16k)
- Supports claim: Demonstrates test-time scaling properties where longer thinking token lengths generally improve accuracy, though benefits vary by benchmark
