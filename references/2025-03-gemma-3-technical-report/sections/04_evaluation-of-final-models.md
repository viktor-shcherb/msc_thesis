# Evaluation of final models [p. 4–5]

In this section, the authors evaluate the IT models over a series of automated benchmarks and human evaluations across a variety of domains, as well as static benchmarks such as MMLU.

## 4.1. LMSYS Chatbot Arena [p. 4–5]

In this section, the authors report the performance of their IT 27B model on LMSys Chatbot Arena (Chiang et al., 2024) in blind side-by-side evaluations by human raters against other state-of-the-art models. The authors report Elo scores in Table 5. Gemma 3 27B IT (1338) is among the top 10 best models, with a score above other non-thinking open models, such as DeepSeek-V3 (1318), LLaMA 3 405B (1257), and Qwen2.5-70B (1257), which are much larger models. Finally, the Elo of Gemma 3 is significantly higher than Gemma 2, at 1220. Note that Elo scores do not take into account visual abilities, which none of the aforementioned models have.

**Table 5** | Evaluation of Gemma 3 27B IT model in the Chatbot Arena (Chiang et al., 2024). All the models are evaluated against each other through blind side-by-side evaluations by human raters. Each model is attributed a score, based on the Elo rating system. *Gemma-3-27B-IT numbers are preliminary results received on March 8, 2025.*

| Rank | Model                            | Elo  | 95% CI    | Open | Type  | #params/#activated |
|------|----------------------------------|------|-----------|------|-------|--------------------|
| 1    | Grok-3-Preview-02-24             | 1412 | +8/-10    | -    | -     | -                  |
| 1    | GPT4.5-Preview                   | 1411 | +11/-11   | -    | -     | -                  |
| 3    | Gemini-2.0-Flash-Thinking-Exp-01-21 | 1384 | +6/-5     | -    | -     | -                  |
| 3    | Gemini-2.0-Pro-Exp-02-05         | 1380 | +5/-6     | -    | -     | -                  |
| 3    | ChatGPT-4o-latest (2025-01-29)   | 1377 | +5/-4     | -    | -     | -                  |
| 6    | DeepSeek-R1                      | 1363 | +8/-6     | yes  | MoE   | 671B/37B           |
| 6    | Gemini-2.0-Flash-001             | 1357 | +6/-5     | -    | -     | -                  |
| 8    | o1-2024-12-17                    | 1352 | +4/-6     | -    | -     | -                  |
| 9    | **Gemma-3-27B-IT**               | **1338** | **+8/-9** | **yes** | **Dense** | **27B**        |
| 9    | Qwen2.5-Max                      | 1336 | +7/-5     | -    | -     | -                  |
| 9    | o1-preview                       | 1335 | +4/-3     | -    | -     | -                  |
| 9    | o3-mini-high                     | 1329 | +8/-6     | -    | -     | -                  |
| 13   | DeepSeek-V3                      | 1318 | +8/-6     | yes  | MoE   | 671B/37B           |
| 14   | GLM-4-Plus-0111                  | 1311 | +8/-8     | -    | -     | -                  |
| 14   | Qwen-Plus-0125                   | 1310 | +7/-5     | -    | -     | -                  |
| 14   | Claude 3.7 Sonnet                | 1309 | +9/-11    | -    | -     | -                  |
| 14   | Gemini-2.0-Flash-Lite            | 1308 | +5/-5     | -    | -     | -                  |
| 18   | Step-2-16k-Exp                   | 1305 | +7/-6     | -    | -     | -                  |
| 18   | o3-mini                          | 1304 | +5/-4     | -    | -     | -                  |
| 18   | o1-mini                          | 1304 | +4/-3     | -    | -     | -                  |
| 18   | Gemini-1.5-Pro-002               | 1302 | +3/-3     | -    | -     | -                  |
| ...  |                                  |      |           |      |       |                    |
| 28   | Meta-Llama-3.1-405B-Instruct-bf16| 1269 | +4/-3     | yes  | Dense | 405B               |
| ...  |                                  |      |           |      |       |                    |
| 38   | Llama-3.3-70B-Instruct           | 1257 | +5/-3     | yes  | Dense | 70B                |
| ...  |                                  |      |           |      |       |                    |
| 39   | Qwen2.5-72B-Instruct             | 1257 | +3/-3     | yes  | Dense | 72B                |
| ...  |                                  |      |           |      |       |                    |
| 59   | Gemma-2-27B-it                   | 1220 | +3/-2     | yes  | Dense | 27B                |

## 4.2. Standard benchmarks [p. 5]

In Table 6, the authors show the performance of their final models across a variety of benchmarks compared to their previous model iteration, and Gemini 1.5. The authors do not compare directly with external models that often report their own evaluation settings, since running them in their setting does not guarantee a fair comparison. The authors encourage the reader to follow third-party static leaderboards for a fairer comparison across models. The authors include additional evaluations of their models on other benchmarks in the appendix.

**Figure 1** (p. 2): "Example of visual interaction with Gemma 3 27B IT model."

Description: Screenshot showing a receipt with handwritten text and a chat interface with Gemma 3 27B IT model
- Key elements: A photograph of a receipt titled "Jungfraubahnen" showing itemized costs in CHF, paired with a chat conversation where the user asks "I only had the sliced meat, how much do I need to pay? Include a 18% tip"
- Notable patterns: The model provides a detailed breakdown: identifies the sliced meat cost (CHF 36.50), calculates the 18% tip (CHF 6.57), and provides the total (CHF 43.07)
- Supports claim: Demonstrates the multimodal vision capabilities of Gemma 3 to read text from images and perform mathematical reasoning
