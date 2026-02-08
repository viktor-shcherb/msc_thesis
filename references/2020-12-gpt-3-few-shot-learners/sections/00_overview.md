# Overview

**Title:** Language Models are Few-Shot Learners

**Authors:** Tom B. Brown*, Benjamin Mann*, Nick Ryder*, Melanie Subbiah*, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, Dario Amodei (* Equal contribution)

**Affiliation:** OpenAI (Jared Kaplan also affiliated with Johns Hopkins University)

**Venue:** arXiv:2005.14165 [cs.CL]

**Date:** 22 Jul 2020 (v4)

## Abstract

> "Recent work has demonstrated substantial gains on many NLP tasks and benchmarks by pre-training on a large corpus of text followed by fine-tuning on a specific task. While typically task-agnostic in architecture, this method still requires task-specific fine-tuning datasets of thousands or tens of thousands of examples. By contrast, humans can generally perform a new language task from only a few examples or from simple instructions -- something which current NLP systems still largely struggle to do. Here we show that scaling up language models greatly improves task-agnostic, few-shot performance, sometimes even reaching competitiveness with prior state-of-the-art fine-tuning approaches. Specifically, we train GPT-3, an autoregressive language model with 175 billion parameters, 10x more than any previous non-sparse language model, and test its performance in the few-shot setting. For all tasks, GPT-3 is applied without any gradient updates or fine-tuning, with tasks and few-shot demonstrations specified purely via text interaction with the model. GPT-3 achieves strong performance on many NLP datasets, including translation, question-answering, and cloze tasks, as well as several tasks that require on-the-fly reasoning or domain adaptation, such as unscrambling words, using a novel word in a sentence, or performing 3-digit arithmetic. At the same time, we also identify some datasets where GPT-3's few-shot learning still struggles, as well as some datasets where GPT-3 faces methodological issues related to training on large web corpora. Finally, we find that GPT-3 can generate samples of news articles which human evaluators have difficulty distinguishing from articles written by humans. We discuss broader societal impacts of this finding and of GPT-3 in general." [p. 1]

## Paper structure

1. Introduction (p. 3)
2. Approach (p. 6)
   - 2.1 Model and Architectures (p. 8)
   - 2.2 Training Dataset (p. 8)
   - 2.3 Training Process (p. 9)
   - 2.4 Evaluation (p. 10)
3. Results (p. 10)
   - 3.1 Language Modeling, Cloze, and Completion Tasks (p. 11)
     - 3.1.1 Language Modeling (p. 11)
     - 3.1.2 LAMBADA (p. 11)
     - 3.1.3 HellaSwag (p. 13)
     - 3.1.4 StoryCloze (p. 13)
   - 3.2 Closed Book Question Answering (p. 13)
   - 3.3 Translation (p. 14)
   - 3.4 Winograd-Style Tasks (p. 16)
   - 3.5 Common Sense Reasoning (p. 17)
   - 3.6 Reading Comprehension (p. 18)
   - 3.7 SuperGLUE (p. 18)
   - 3.8 NLI (p. 20)
   - 3.9 Synthetic and Qualitative Tasks (p. 21)
     - 3.9.1 Arithmetic (p. 21)
     - 3.9.2 Word Scrambling and Manipulation Tasks (p. 23)
     - 3.9.3 SAT Analogies (p. 24)
     - 3.9.4 News Article Generation (p. 25)
     - 3.9.5 Learning and Using Novel Words (p. 26)
     - 3.9.6 Correcting English Grammar (p. 29)
4. Measuring and Preventing Memorization Of Benchmarks (p. 29)
5. Limitations (p. 33)
6. Broader Impacts (p. 34)
   - 6.1 Misuse of Language Models (p. 35)
     - 6.1.1 Potential Misuse Applications (p. 35)
     - 6.1.2 Threat Actor Analysis (p. 35)
     - 6.1.3 External Incentive Structures (p. 35)
   - 6.2 Fairness, Bias, and Representation (p. 36)
     - 6.2.1 Gender (p. 36)
     - 6.2.2 Race (p. 37)
     - 6.2.3 Religion (p. 38)
     - 6.2.4 Future Bias and Fairness Challenges (p. 39)
   - 6.3 Energy Usage (p. 39)
7. Related Work (p. 39)
8. Conclusion (p. 40)
Acknowledgements (p. 41)
Contributions (p. 42)
A. Details of Common Crawl Filtering (p. 43)
B. Details of Model Training (p. 43)
C. Details of Test Set Contamination Studies (p. 43)
D. Total Compute Used to Train Language Models (p. 46)
E. Human Quality Assessment of Synthetic News Articles (p. 46)
F. Additional Samples from GPT-3 (p. 48)
G. Details of Task Phrasing and Specifications (p. 50)
H. Results on All Tasks for All Model Sizes (p. 63)
References (p. 68)
