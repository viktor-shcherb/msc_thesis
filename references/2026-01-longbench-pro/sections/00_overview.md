# Overview

**Title:** LongBench Pro: A More Realistic and Comprehensive Bilingual Long-Context Evaluation Benchmark

**Authors:** Ziyang Chen^1,2, Xing Wu^1, Junlong Jia^3, Chaochen Gao^1,2, Qi Fu^4, Debing Zhang^4, Songlin Hu^1,2

**Affiliations:**
1. Institute of Information Engineering, Chinese Academy of Sciences
2. School of Cyber Security, University of Chinese Academy of Sciences
3. School of Artificial Intelligence, Beihang University
4. Xiaohongshu Inc.

**Correspondence:** Xing Wu, Songlin Hu (`wuxing@iie.ac.cn`, `husonglin@iie.ac.cn`)

**Venue:** arXiv:2601.02872v1 [cs.CL]

**Date:** 6 Jan 2026

**Abstract:**
> "The rapid expansion of context length in large language models (LLMs) has outpaced existing evaluation benchmarks. Current long-context benchmarks often trade off scalability and realism: synthetic tasks underrepresent real-world complexity, while fully manual annotation is costly to scale to extreme lengths and diverse scenarios. We present LongBench Pro, a more realistic and comprehensive bilingual benchmark of 1,500 naturally occurring long-context samples in English and Chinese spanning 11 primary tasks and 25 secondary tasks, with input lengths from 8k to 256k tokens. LongBench Pro supports fine-grained analysis with task-specific metrics and a multi-dimensional taxonomy of context requirement (full vs. partial dependency), length (six levels), and difficulty (four levels calibrated by model performance). To balance quality with scalability, we propose a Human-Model Collaborative Construction pipeline: frontier LLMs draft challenging questions and reference answers, along with design rationales and solution processes, to reduce the cost of expert verification. Experts then rigorously validate correctness and refine problematic cases. Evaluating 46 widely used long-context LLMs on LongBench Pro yields three findings: (1) long-context optimization contributes more to long-context comprehension than parameter scaling; (2) effective context length is typically shorter than the claimed context length, with pronounced cross-lingual misalignment; and (3) the “thinking” paradigm helps primarily models trained with native reasoning, while mixed-thinking designs offer a promising Pareto trade-off. In summary, LongBench Pro provides a robust testbed for advancing long-context understanding." [p. 1]

## Section Headings

1. Introduction [p. 2]
2. Task Framework of LongBench Pro [p. 3]
3. Construction Process of LongBench Pro [p. 3-6]
   - 3.1 Document Collection [p. 3]
   - 3.2 Human-Model Collaborative Sample Generation [p. 4-5]
   - 3.3 Question Standardization [p. 5]
   - 3.4 Answer Review [p. 5]
   - 3.5 Difficulty Classification [p. 5-6]
4. Data Statistics and Validation of LongBench Pro [p. 6]
5. Evaluation [p. 6-13]
   - 5.1 Evaluation Settings [p. 6-7]
   - 5.2 General Performance [p. 7-10]
   - 5.3 Upper-Bound Performance [p. 10]
   - 5.4 Comparison Across Length Dimension [p. 10-11]
   - 5.5 Comparison Across Task Dimension [p. 10-11]
   - 5.6 Comparison Across Context Requirement Dimension [p. 12]
   - 5.7 Comparison Across Construction Strategies [p. 12-13]
6. Related Works [p. 13]
7. Conclusion and Future Work [p. 13]
References [p. 13-15]
Appendix A. Task Definitions [p. 16-20]
Appendix B. Annotation Guidelines [p. 21-26]
Appendix C. Annotator Statistics and Compensation [p. 26-27]
Appendix D. Inference Parameter Settings [p. 26, 28]
Appendix E. Truncation Length Setting [p. 26]
