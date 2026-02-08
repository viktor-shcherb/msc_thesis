# Overview

**Title:** Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization

**Authors:**
- Cheng-Yu Hsieh^{1*} (University of Washington; Google Cloud AI Research correspondence: cydhsieh@cs.washington.edu, chenyulee@google.com)
- Yung-Sung Chuang^2 (MIT)
- Chun-Liang Li^3 (Google Cloud AI Research)
- Zifeng Wang^3 (Google Cloud AI Research)
- Long T. Le^3 (Google Cloud AI Research)
- Abhishek Kumar^{\dagger} (Google DeepMind)
- James Glass^2 (MIT)
- Alexander Ratner^1 (University of Washington)
- Chen-Yu Lee^3 (Google Cloud AI Research)
- Ranjay Krishna^{1\ddagger} (University of Washington)
- Tomas Pfister^{3\ddagger} (Google Cloud AI Research)

\* Work done while the author was a student researcher at Google Cloud AI Research.
\dagger Work done while the author was at Google DeepMind.
\ddagger The authors contributed equally to this work.

**Affiliations:** ^1University of Washington, ^2MIT, ^3Google Cloud AI Research

**Venue:** arXiv:2406.16008v2 [cs.CL]

**Date:** 3 Jul 2024

## Abstract

> "Large language models (LLMs), even when specifically trained to process long input contexts, struggle to capture relevant information located in the middle of their input. This phenomenon has been known as the *lost-in-the-middle* problem. In this work, we make three contributions. First, we set out to understand the factors that cause this phenomenon. In doing so, we establish a connection between lost-in-the-middle to LLMs' intrinsic attention bias: LLMs exhibit an *U-shaped attention bias* where the tokens at the beginning and at the end of its input receive higher attention, regardless of their relevance. Second, we mitigate this positional bias through a calibration mechanism, *found-in-the-middle*, that allows the model to attend to contexts faithfully according to their relevance, even though when they are in the middle. Third, we show *found-in-the-middle* not only achieves better performance in locating relevant information within a long context, but also eventually leads to improved retrieval-augmented generation (RAG) performance across various tasks, outperforming existing methods by up to 15 percentage points. These findings open up future directions in understanding LLM attention bias and its potential consequences." [p. 1]

## Section Headings

1. Introduction [p. 1-2]
2. Positional attention bias overpowers mid-sequence context [p. 2-4]
   - 2.1 U-shaped attention bias [p. 3-4]
   - 2.2 Does attention favor relevant context? [p. 4]
3. Found-in-the-middle: modeling and isolating positional attention bias [p. 4-6]
   - 3.1 Two main factors in model attention [p. 5]
   - 3.2 Disentangling positional attention bias [p. 5-6]
4. Improving long-context utilization with found-in-the-middle [p. 6-8]
   - 4.1 Attention calibration [p. 6]
   - 4.2 Calibrated v.s. uncalibrated attention [p. 6-7]
   - 4.3 Attention calibration in practice [p. 7-8]
5. Related work [p. 8-9]
6. Discussion [p. 9]
   - Limitations [p. 9]
   - Ethical Statement [p. 9]
References [p. 10-12]
Appendix A: Multi-doc QA datasets [p. 13]
Appendix B: Implementation details [p. 13]
Appendix C: Additional experiment results [p. 13-14]
Appendix D: Compute and inference details [p. 13]
