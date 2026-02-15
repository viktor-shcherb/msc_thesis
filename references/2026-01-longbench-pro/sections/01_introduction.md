# 1 Introduction [p. 2]

[p. 2] Long-context LLM capability is framed as increasingly critical for codebase analysis, legal document understanding, and long-form synthesis. The authors argue that model context windows have expanded rapidly (citing Gemini-2.5, GPT-5, Claude-4), but benchmark realism and coverage have not kept pace.

[p. 2] They position prior work in two groups:
- Synthetic benchmarks (Hsieh et al., 2024; Yen et al., 2024): scalable and controllable, but less representative of real semantic complexity.
- Manual realistic benchmarks (Qiu et al., 2024; Bai et al., 2025): realistic, but costly to scale to 128K-256K and broad task sets.

[p. 2] LongBench Pro is introduced as a bilingual (EN/ZH), fully natural benchmark with:
- 1,500 samples
- 11 primary tasks and 25 secondary tasks
- Length buckets from 8K to 256K
- Three analysis dimensions: context requirement, length, difficulty

[p. 2] The claimed contribution is to combine realism and scalability via a human-model collaborative pipeline in which frontier models draft candidate QA artifacts and experts verify/correct them.

[p. 2] The three headline findings previewed in the introduction are:
1. Long-context optimization can be more valuable than parameter scaling.
2. Effective context length is often lower than claimed context length.
3. Thinking helps mainly for models with native reasoning training; mixed-thinking design is a strong practical compromise.

[p. 2] The explicit contribution bullets are:
- Release of LongBench Pro with 1,500 bilingual samples and multi-dimensional tags.
- Validation of the collaborative construction strategy as a cost-quality improvement over human-only annotation.
- A broad empirical evaluation across 46 long-context models.

**Figure 1** (p. 1): "Performance of advanced long-context LLMs on LongBench Pro"
- Description: leaderboard-style bar chart comparing advanced models on benchmark performance.
- Key elements: model labels and aggregate performance scores.
- Supports claim: there is substantial room for improvement even among frontier long-context systems.
