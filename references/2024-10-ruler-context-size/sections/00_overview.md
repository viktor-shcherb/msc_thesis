# Overview

**Title:** RULER: What's the Real Context Size of Your Long-Context Language Models?

**Authors:** Cheng-Ping Hsieh*, Simeng Sun*, Samuel Kriman, Shantanu Acharya, Dima Rekesh, Fei Jia, Yang Zhang, Boris Ginsburg
(*Authors contributed equally.)

**Affiliation:** NVIDIA
**Contact:** {chsieh, simengs}@nvidia.com

**Venue:** Published as a conference paper at COLM 2024

**Date:** arXiv v3: 6 Aug 2024 (arXiv:2404.06654v3)

**Code:** https://github.com/hsiehjackson/RULER

## Abstract

> "The needle-in-a-haystack (NIAH) test, which examines the ability to retrieve a piece of information (the "needle") from long distractor texts (the "haystack"), has been widely adopted to evaluate long-context language models (LMs). However, this simple retrieval-based test is indicative of only a superficial form of long-context understanding. To provide a more comprehensive evaluation of long-context LMs, we create a new synthetic benchmark RULER with flexible configurations for customized sequence length and task complexity. RULER expands upon the vanilla NIAH test to encompass variations with diverse types and quantities of needles. Moreover, RULER introduces new task categories multi-hop tracing and aggregation to test behaviors beyond searching from context. We evaluate 17 long-context LMs with 13 representative tasks in RULER. Despite achieving nearly perfect accuracy in the vanilla NIAH test, almost all models exhibit large performance drops as the context length increases. While these models all claim context sizes of 32K tokens or greater, only half of them can maintain satisfactory performance at the length of 32K. Our analysis of Yi-34B, which supports context length of 200K, reveals large room for improvement as we increase input length and task complexity. We open source RULER to spur comprehensive evaluation of long-context LMs." [p. 1]

## Section Headings

1. Introduction [p. 1-2]
2. Related Work [p. 3]
3. The RULER Benchmark [p. 3-6]
   - 3.1 Retrieval: Needle-in-a-haystack (NIAH) [p. 3-5]
   - 3.2 Multi-hop Tracing: Variable Tracking (VT) [p. 5]
   - 3.3 Aggregation: Common Words (CWE) and Frequent Words Extraction (FWE) [p. 5]
   - 3.4 Question Answering (QA) [p. 5-6]
4. Experiments & Results [p. 6-7]
5. Task Error Analysis [p. 7-9]
6. Model Analysis [p. 9-10]
7. Conclusion [p. 10]
8. Limitations [p. 10]
References [p. 11-16]
Appendix A: Models [p. 17]
Appendix B: Task Configurations [p. 18]
Appendix C: Task Correlation Analysis [p. 19]
Appendix D: Prompt Templates [p. 20-23]
Appendix E: Passkey Retrieval and Vanilla NIAH Results [p. 24]
Appendix F: Additional Results [p. 25-27]
