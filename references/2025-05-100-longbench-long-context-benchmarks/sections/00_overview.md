# Overview

## Paper Metadata

**Title:** 🏀-LongBench: Are de facto Long-Context Benchmarks Literally Evaluating Long-Context Ability?

**Authors:** Wang Yang¹, Hongye Jin², Shaochen Zhong³, Song Jiang⁴, Qifan Wang¹, Vipin Chaudhary¹, Xiaotian Han¹

**Affiliations:**
- ¹Case Western Reserve University
- ²Texas A&M University
- ³Rice University
- ⁴Meta

**Contact:** {wxy320,vipin,xhan9}@case.edu, jhy@410@tamu.edu, hz88@rice.edu, {songjiang,wqfer}@meta.com

**Venue:** arXiv preprint

**Date:** 2025-05 (arXiv:2505.19293v1 [cs.CL] 25 May 2025)

**Code:** https://github.com/useryan/100-LongBench.git

## Abstract

> "Long-context capability is considered one of the most important abilities of LLMs, as a truly long context-capable LLM shall enable its users to effortlessly process many originally exhausting tasks — e.g., digesting a long-form document to find answers v.s., directly asking an LLM about it. However, existing real-task-based long-context evaluation benchmarks have two major shortcomings: Firstly, benchmarks like LongBench often do not provide proper metrics to separate long-context performance from the model's baseline ability, so when conducting a cross-model comparison, such conflation makes the user unable to understand how exactly one model or method excels at the long-context task in relation to its baseline ability. Secondly, such benchmarks are often formed in a way where each data sample has a fixed sequence length, which not only makes them solely evaluate models with a certain range of context windows, and also they are a proxy to know at what length the model/method-of-interests would fail. To address these issues, we introduce a length-controllable long-context benchmark and a novel metric that disentangles baseline knowledge from long-context capabilities. Experiments demonstrate the superiority of our approach in effectively evaluating LLMs. The code is available at https://github.com/useryan/100-LongBench.git."

## Section Structure

Based on pages 1-6:

1. **Introduction** (p. 1-2)
2. **Motivation: why do we need to refine long-context benchmarks?** (p. 2-3)
3. **How to truly evaluate Language Models' long-context capability?** (p. 3-6)
   - 3.1 Construct a new long-context benchmark (p. 3-4)
   - 3.2 LongScore: a new long-context metric (p. 4-5)
   - 3.3 Compare to other benchmarks (p. 5-6)
4. **Experimental Analysis** (p. 6+)
   - 4.1 Verification of the reliability of the proposed benchmark (p. 6)
   - 4.2 Verification of the effectiveness of the proposed metric (p. 6)

Additional sections (not yet visible): likely Discussion, Related Work, Conclusion, Appendices
