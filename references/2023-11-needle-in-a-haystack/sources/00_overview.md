# Needle In A Haystack -- Pressure Testing LLMs

**Author(s):** Greg Kamradt
**Type:** Community contribution (X/Twitter threads + GitHub repository)
**Date:** November 2023
**Primary URL:** https://github.com/gkamradt/LLMTest_NeedleInAHaystack

## Summary

The Needle In A Haystack (NIAH) test is a systematic evaluation methodology for testing long-context retrieval ability of large language models. A specific factual statement (the "needle") is placed at varying positions within a long document composed of unrelated text (the "haystack"), and the model is asked to retrieve it. By iterating over different context lengths and document depths, the test produces a 2D heatmap of retrieval accuracy that reveals where in the context window a model fails to attend. The methodology was first applied to GPT-4-128K (November 8, 2023) and Claude 2.1-200K (November 21, 2023), revealing significant retrieval degradation patterns that became a widely cited benchmark for long-context evaluation.

## Source structure

1. **GitHub Repository** (primary) — Full methodology, code, parameters, evaluation rubric, multi-needle extension, and visualization notebook
2. **X Thread — GPT-4-128K Results** (primary) — Original findings on GPT-4-128K recall performance, the first public NIAH results
3. **X Thread — Claude 2.1-200K Results** (primary) — Follow-up findings on Claude 2.1 with 200K token context
4. **YouTube Video — Overview** (supplementary) — Walkthrough of methodology and results interpretation
5. **X Thread — Visualization Code** (supplementary) — Design decisions behind the NIAH heatmap visualization format
