# 3 Construction Process of LongBench Pro [p. 3-6]

## 3.1 Document Collection [p. 3]

[p. 3] Source documents are curated from public internet domains (news, medicine, science, literature, law, education) and formats (reports, tables, code, dialogue, lists, JSON).

[p. 3] Collection balancing dimensions:
- Single-document and multi-document settings.
- English and Chinese.
- Six target length buckets: 8K, 16K, 32K, 64K, 128K, 256K tokens.

[p. 3] Length assignment rule uses Qwen tokenizer and +/-20% tolerance around target length. Human compliance review filters privacy-sensitive, copyrighted, or non-compliant content.

## 3.2 Human-Model Collaborative Sample Generation [p. 4-5]

[p. 4] For each long document, five frontier models draft 3 candidate samples each, including:
- question
- reference answer
- design rationale
- solution process

[p. 4] Drafting models:
- Gemini-2.5-Pro (Comanici et al., 2025)
- GPT-5 (OpenAI, 2025)
- Claude-4-Sonnet (Anthropic, 2025)
- DeepSeek-V3.2 (Liu et al., 2025)
- Qwen3-235B-A22B-Thinking-2507 (Yang et al., 2025)

[p. 4-5] Human annotators then evaluate:
1. Task/context alignment from rationale.
2. Answer correctness from solution process.
3. Challenge level using model responses (challenging if at least one model fails).
4. Best sample selection or rejection.

[p. 5] Accepted samples are reviewed by long-context experts; rejected samples are revised.

## 3.3 Question Standardization [p. 5]

[p. 5] Two prompt formats are standardized for each question:
- Non-thinking prompt.
- Thinking prompt requiring step-by-step reasoning before answer.

[p. 5] Both require structured line-by-line outputs with `[Answer]` marker for automatic extraction/scoring.

## 3.4 Answer Review [p. 5]

[p. 5] The review protocol combines:
- human precision on answer-component correctness
- model-assisted recall for potentially missing components

Two independent annotators verify each sample; disagreements escalate to long-context experts.

## 3.5 Difficulty Classification [p. 5-6]

[p. 5-6] Difficulty is model-calibrated via three tiers with five representative models each (high/mid/low).

[p. 6] Definition rules:
- **Extreme**: at most one high-tier model solves it (for summarization, score > 0.65 counts as correct).
- **Hard**: after excluding Extreme, at most one mid-tier model solves it.
- **Moderate**: after excluding Hard, at most one low-tier model solves it.
- **Easy**: remainder.

[p. 6] The paper positions this as a scalable, model-aligned alternative to subjective human-only difficulty labeling.

**Figure 3** (p. 5): "The construction process of LongBench Pro includes document collection, human-model collaborative sample generation, question standardization, answer review, and difficulty classification."
- Description: pipeline diagram from document intake through quality control and labeling.
- Key elements: staged workflow and iterative expert validation.
- Supports claim: quality and scalability are achieved through explicit human-model division of labor.
