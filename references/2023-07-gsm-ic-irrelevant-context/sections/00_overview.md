# Overview

**Title:** Large Language Models Can Be Easily Distracted by Irrelevant Context

**Authors:**
- Freda Shi (Google DeepMind; Toyota Technological Institute at Chicago) — equal contribution
- Xinyun Chen (Google DeepMind) — equal contribution
- Kanishka Misra (Google DeepMind; Purdue University)
- Nathan Scales (Google DeepMind)
- David Dohan (Google DeepMind)
- Ed Chi (Google DeepMind)
- Nathanael Schärli (Google DeepMind)
- Denny Zhou (Google DeepMind)

**Venue:** Proceedings of the 40th International Conference on Machine Learning (ICML), Honolulu, Hawaii, USA. PMLR 202, 2023.

**Date:** 2023 (arXiv v3: 6 Jun 2023)

**Abstract:**
> "Large language models have achieved impressive performance on various natural language processing tasks. However, so far they have been evaluated primarily on benchmarks where all information in the input context is relevant for solving the task. In this work, we investigate the distractibility of large language models, i.e., how the model problem-solving accuracy can be influenced by irrelevant context. In particular, we introduce Grade-School Math with Irrelevant Context (GSM-IC), an arithmetic reasoning dataset with irrelevant information in the problem description. We use this benchmark to measure the distractibility of cutting-edge prompting techniques for large language models, and find that the model performance is dramatically decreased when irrelevant information is included. We also identify several approaches for mitigating this deficiency, such as decoding with self-consistency and adding to the prompt an instruction that tells the language model to ignore the irrelevant information." [p. 1]

**Dataset:** Available at https://github.com/google-research-datasets/GSM-IC

## Section Headings

1. Introduction
2. Related Work
3. The GSM-IC Dataset
   - 3.1 Dataset Creation
   - 3.2 Evaluation Metrics
4. Investigated Solutions
   - 4.1 Base Techniques
   - 4.2 Prompt Design
   - 4.3 Instructed Prompting
5. Experiments
   - 5.1 Main Results on GSM-IC
   - 5.2 Break-Down Analysis
     - 5.2.1 Factors of the Irrelevant Context
     - 5.2.2 Break-Down Accuracies w.r.t. # Steps
   - 5.3 Instructed Prompting Improves Robustness to Irrelevant Context
   - 5.4 Complicated Prompts May Hurt the Robustness to Irrelevant Context
   - 5.5 Extension to DROP
6. Conclusion and Discussion
7. Acknowledgement
A. GSM-IC Details
B. Sample Predictions on GSM-IC
C. Full Prompts in Experiments
