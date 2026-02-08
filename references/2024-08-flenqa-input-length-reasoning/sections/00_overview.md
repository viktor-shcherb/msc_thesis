# Overview

**Title:** Same Task, More Tokens: the Impact of Input Length on the Reasoning Performance of Large Language Models

**Authors:** Mosh Levy*1, Alon Jacoby*1, Yoav Goldberg1,2
- *These authors contributed equally to this work.
- 1: Bar-Ilan University
- 2: Allen Institute for AI
- Contact: {moshe0110, alonj4}@gmail.com

**Venue:** arXiv:2402.14848v2 [cs.CL]

**Date:** 10 Jul 2024

**Abstract:**
> "This paper explores the impact of extending input lengths on the capabilities of Large Language Models (LLMs). Despite LLMs advancements in recent times, their performance consistency across different input lengths is not well understood. We investigate this aspect by introducing a novel QA reasoning framework, specifically designed to assess the impact of input length. We isolate the effect of input length using multiple versions of the same sample, each being extended with padding of different lengths, types and locations. Our findings show a notable degradation in LLMs' reasoning performance at much shorter input lengths than their technical maximum. We show that the degradation trend appears in every version of our dataset, although at different intensities. Additionally, our study reveals that the traditional metric of next word prediction correlates negatively with performance of LLMs' on our reasoning dataset. We analyse our results and identify failure modes that can serve as useful guides for future research, potentially informing strategies to address the limitations observed in LLMs." [p. 1]

## Section Headings

1. Introduction
2. Desired Data Properties
3. FLenQA
   - 3.1 Base instances
   - 3.2 The tasks
   - 3.3 Length Variations
     - 3.3.1 Background Texts
     - 3.3.2 Location of key paragraphs in the text
   - 3.4 Base instances are answerable
4. Main Experiments
   - 4.1 Impact of Length and Location
   - 4.2 Kind of irrelevant material
5. Correlation with Next Word Prediction
6. Does Chain of Thought Help?
7. Length-induced Failure Modes
8. Related Work
9. Discussion
   - Limitations
   - Acknowledgements
A. Datasets (Appendix)
   - A.1 Ruletaker
   - A.2 MonoRel
   - A.3 People in Rooms (PIR)
B. Full Evaluation Setup (Appendix)
   - B.1 Prompts
   - B.2 Parameters
   - B.3 Locating the answer in models' replies
   - B.4 Evaluating the coverage of key facts in CoT
C. Full Results (Appendix)
