# Appendix I: LLMs fine-tuning results [p. 22]

Results for GPT-3.5 and Mistral-7B fine-tuning are shown on the Fig. 9. [p. 22]

**Figure 9** (p. 23): "LLM fine-tuning makes full context effective. a) After fine-tuning both GPT-3.5 and Mistral-7B significantly improved their scores along context lengths achieving 90% + accuracy on QA1 task. b) GPT-3.5 fine-tuned for QA1 task shows improved performance on QA2-QA5 tasks. c) Full fine-tuning of smaller Mistral-7B on QA1 results in degraded scores for other tasks (QA2-QA5). No distractor text for b) and c)."

Description: Three line charts showing fine-tuning results
- Key elements:
  - (a) Left chart: "QA1: Single supporting fact" showing accuracy (%) vs context size in tokens (100 to 10000). Four lines: GPT-3.5, GPT-3.5-finetuned, Mistral-7B, Mistral-7B-finetuned
  - (b) Top right chart: GPT-3.5 and GPT-3.5 fine-tuned performance across tasks QA1-QA5, showing accuracy (%) from 0-100%
  - (c) Bottom right chart: Mistral-7B and Mistral-7B-finetuned performance across tasks QA1-QA5, showing accuracy (%) from 0-100%
- Notable patterns:
  - (a) Both fine-tuned models (solid lines) maintain 90%+ accuracy across all context lengths (100-10000 tokens), while non-fine-tuned models (dashed lines) show dramatic performance degradation beyond 1000 tokens
  - (b) GPT-3.5 fine-tuned shows improvement on all QA1-QA5 tasks compared to base model
  - (c) Mistral-7B fine-tuned shows improvement on QA1 but degraded performance on QA2-QA5 compared to base model
- Supports claim: Fine-tuning makes full context effective for the trained task, but transfer to other tasks varies by model - GPT-3.5 generalizes better across tasks while Mistral-7B shows task-specific overfitting.
