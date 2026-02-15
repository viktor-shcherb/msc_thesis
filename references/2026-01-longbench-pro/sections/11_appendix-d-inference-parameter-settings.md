# Appendix D. Inference Parameter Settings [p. 26, 28]

[p. 26, 28] Appendix D lists per-model inference parameters: model type, input/output context limits, truncation length, non-thinking output length, thinking output length, and temperatures.

## Table 5 (representative rows, exact values) [p. 28]

| Model | Type | Input/Output Context | Truncation | Output Length (Non-Thk / Thk) | Temperature (Non-Thk / Thk) |
|---|---|---|---|---|---|
| Gemini-2.5-Pro | Thinking | 1M / 64k | 1M | - / 32k | - / 1.0 |
| Gemini-2.5-Flash | Mixed | 1M / 64k | 1M | 1k / 32k | 1.0 / 1.0 |
| GPT-5 | Thinking | 272k / 128k | 272k | - / 32k | - / 1.0 |
| Claude-4-Sonnet | Mixed | 1M / 64k | 1M | 1k / 32k | 1.0 / 1.0 |
| DeepSeek-V3.2* | Mixed | 160k | 120k | 1k / 32k | 1.0 / 1.0 |
| Qwen3-235B-A22B-Thinking-2507 | Thinking | 256k | 224k | - / 32k | - / 0.6 |
| Qwen3-235B-A22B-Instruct-2507 | Instruct | 256k | 224k | 1k / 32k | 0.7 / 0.7 |
| GLM-4.6* | Mixed | 198k | 120k | 1k / 32k | 1.0 / 1.0 |
| MiniMax-M2* | Thinking | 192k | 120k | - / 32k | - / 1.0 |
| MiniMax-Text-01 | Instruct | 4M | 1M | 1k / 32k | 1.0 / 1.0 |
| Llama-3.1-405B-Instruct | Instruct | 128k | 120k | 1k / 8k | 0.6 / 0.6 |

`*` marker note from table: these models may support longer contexts, but truncation is set to 120k and thinking output to 32k for stable/equitable evaluation.

[p. 28] The table is intended to make cross-model evaluation settings auditable and reproducible.
