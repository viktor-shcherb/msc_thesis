# HuggingFace text-generation-inference Issue #512 [https://github.com/huggingface/text-generation-inference/issues/512]

**Type:** github-repo
**Fetched:** 2026-02-08
**Priority:** supplementary

## Issue Metadata

- **Opened by:** Florian Zimmermeister (@flozi00)
- **Date opened:** June 30, 2023
- **Status:** Closed / Completed

## Issue Summary

GitHub issue requesting implementation of NTK-Aware Scaled RoPE in HuggingFace's text-generation-inference (TGI) framework to extend LLaMA model context windows to 8k+ tokens.

## Request

Florian Zimmermeister requested adding NTK-aware RoPE scaling support, noting the simplicity of the change:

> "As it's only 3 lines of code to change it would be pretty easy to change."

## Resources Shared

The issue linked to:
- The original Reddit discussion by bloc97
- A Google Colab notebook demonstrating the technique with implementation examples

## Implementation Progress

- **Draft PR #529** opened in early July 2023 by Ian Butler (@iantbutler01) for initial testing
- Contributor Ian Butler expanded the implementation beyond LLaMA to support "any model using rotary embeddings," including Falcon 40B
- Dynamic NTK-aware scaling variants were also implemented
- **Final PR #741** merged the complete implementation into TGI

## Validation

The original poster shared performance comparison showing:

> "The purple one is trained with the 3 line fix given in the colab"

This confirmed practical validation of the approach in the TGI production framework.

## Resolution

- Issue marked as **CLOSED / COMPLETED** via PR #741
- By July 13, 2023, RoPE scaling was merged into the HuggingFace Transformers repository (PR #24653), providing a reference implementation
- The implementation supports multiple scaling types: linear (PI), NTK-aware, and dynamic NTK

## Significance

This issue documents the rapid adoption path of NTK-aware RoPE from a Reddit post to production-grade infrastructure. The timeline from Reddit post (late June 2023) to merged HuggingFace PR (July 2023) was approximately 2-3 weeks, demonstrating the community-driven velocity of this contribution.
