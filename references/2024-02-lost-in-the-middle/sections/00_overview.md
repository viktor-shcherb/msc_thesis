# Overview

**Title:** Lost in the Middle: How Language Models Use Long Contexts

**Authors:**
- Nelson F. Liu (Stanford University)
- Kevin Lin (University of California, Berkeley)
- John Hewitt (Stanford University)
- Ashwin Paranjape (Samaya AI)
- Michele Bevilacqua (Samaya AI)
- Fabio Petroni (Samaya AI)
- Percy Liang (Stanford University)

*Work partially completed as an intern at Samaya AI.

**Venue:** arXiv:2307.03172v3 [cs.CL]
**Date:** 20 Nov 2023

## Abstract

> "While recent language models have the ability to take long contexts as input, relatively little is known about how well they *use* longer context. We analyze the performance of language models on two tasks that require identifying relevant information in their input contexts: multi-document question answering and key-value retrieval. We find that performance can degrade significantly when changing the position of relevant information in long input contexts, indicating that current language models do not robustly make use of information in long input contexts. In particular, we observe that performance is often highest when relevant information occurs at the beginning or end of the input context, and significantly degrades when models must access relevant information in the middle of long contexts, even for explicitly long-context models. Our analysis provides a better understanding of how language models use their input context and provides new evaluation protocols for future long-context language models." [p. 1]

## Section Headings

1. Introduction
2. Multi-Document Question Answering
   - 2.1 Experimental Setup
   - 2.2 Models
   - 2.3 Results and Discussion
3. How Well Can Language Models Retrieve From Input Contexts?
   - 3.1 Experimental Setup
   - 3.2 Results and Discussion
4. Why Are Language Models Not Robust to Changes in the Position of Relevant Information?
   - 4.1 Effect of Model Architecture
   - 4.2 Effect of Query-Aware Contextualization
   - 4.3 Effect of Instruction Fine-Tuning
5. Is More Context Is Always Better? A Case Study With Open-Domain QA
6. Related Work
   - 6.1 Long-Context Language Models
   - 6.2 How Do Language Models Use Context?
   - 6.3 The Serial-Position Effect
7. Conclusion
Acknowledgments
References
A. Ambiguity in Multi-Document QA Distractor Documents
B. Random Distractors in Multi-Document QA
C. Randomizing Distractor Order in Multi-Document QA
D. GPT-4 Performance
E. Llama-2 Performance
F. Token Counts
G. Full Multi-Document Question Answering Results
   - G.1 10 Total Retrieved Documents
   - G.2 20 Total Retrieved Documents
   - G.3 30 Total Retrieved Documents
