# Overview

**Title:** Llama 2: Open Foundation and Fine-Tuned Chat Models

**Authors:** Hugo Touvron*, Louis Martin^dagger, Kevin Stone^dagger, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, Dan Bikel, Lukas Blecher, Cristian Canton Ferrer, Moya Chen, Guillem Cucurull, David Esiobu, Jude Fernandes, Jeremy Fu, Wenyin Fu, Brian Fuller, Cynthia Gao, Vedanuj Goswami, Naman Goyal, Anthony Hartshorn, Saghar Hosseini, Rui Hou, Hakan Inan, Marcin Kardas, Viktor Kerkez, Madian Khabsa, Isabel Kloumann, Artem Korenev, Punit Singh Koura, Marie-Anne Lachaux, Thibaut Lavril, Jenya Lee, Diana Liskovich, Yinghai Lu, Yuning Mao, Xavier Martinet, Todor Mihaylov, Pushkar Mishra, Igor Molybog, Yixin Nie, Andrew Poulton, Jeremy Reizenstein, Rashi Rungta, Kalyan Saladi, Alan Schelten, Ruan Silva, Eric Michael Smith, Ranjan Subramanian, Xiaoqing Ellen Tan, Binh Tang, Ross Taylor, Adina Williams, Jian Xiang Kuan, Puxin Xu, Zheng Yan, Iliyan Zarov, Yuchen Zhang, Angela Fan, Melanie Kambadur, Sharan Narang, Aurelien Rodriguez, Robert Stojnic, Sergey Edunov, Thomas Scialom*

(* Equal contribution, corresponding authors: {tscialom, htouvron}@meta.com; ^dagger = second author)

**Affiliation:** GenAI, Meta

**Venue:** arXiv:2307.09288v2 [cs.CL]

**Date:** 19 Jul 2023

## Abstract

> "In this work, we develop and release Llama 2, a collection of pretrained and fine-tuned large language models (LLMs) ranging in scale from 7 billion to 70 billion parameters. Our fine-tuned LLMs, called Llama 2-Chat, are optimized for dialogue use cases. Our models outperform open-source chat models on most benchmarks we tested, and based on our human evaluations for helpfulness and safety, may be a suitable substitute for closed-source models. We provide a detailed description of our approach to fine-tuning and safety improvements of Llama 2-Chat in order to enable the community to build on our work and contribute to the responsible development of LLMs." [p. 1]

## Section Headings

1. Introduction (p. 3)
2. Pretraining (p. 5)
   - 2.1 Pretraining Data (p. 5)
   - 2.2 Training Details (p. 5)
     - 2.2.1 Training Hardware & Carbon Footprint (p. 6)
   - 2.3 Llama 2 Pretrained Model Evaluation (p. 7)
3. Fine-tuning (p. 8)
   - 3.1 Supervised Fine-Tuning (SFT) (p. 9)
   - 3.2 Reinforcement Learning with Human Feedback (RLHF) (p. 9)
     - 3.2.1 Human Preference Data Collection (p. 10)
     - 3.2.2 Reward Modeling (p. 10)
     - 3.2.3 Iterative Fine-Tuning (p. 13)
   - 3.3 System Message for Multi-Turn Consistency (p. 16)
   - 3.4 RLHF Results (p. 17)
     - 3.4.1 Model-Based Evaluation (p. 17)
     - 3.4.2 Human Evaluation (p. 18)
4. Safety (p. 20)
   - 4.1 Safety in Pretraining (p. 20)
   - 4.2 Safety Fine-Tuning (p. 23)
     - 4.2.1 Safety Categories and Annotation Guidelines (p. 23)
     - 4.2.2 Safety Supervised Fine-Tuning (p. 24)
     - 4.2.3 Safety RLHF (p. 24)
     - 4.2.4 Context Distillation for Safety (p. 27)
   - 4.3 Red Teaming (p. 28)
   - 4.4 Safety Evaluation of Llama 2-Chat (p. 29)
5. Discussion (p. 32)
   - 5.1 Learnings and Observations (p. 32)
   - 5.2 Limitations and Ethical Considerations (p. 34)
   - 5.3 Responsible Release Strategy (p. 35)
6. Related Work (p. 35)
7. Conclusion (p. 36)
References (p. 37–45)
A. Appendix (p. 46)
   - A.1 Contributions (p. 46)
     - A.1.1 Acknowledgments (p. 46)
   - A.2 Additional Details for Pretraining (p. 47)
     - A.2.1 Architecture Changes Compared to Llama 1 (p. 47)
     - A.2.2 Additional Details for Pretrained Models Evaluation (p. 48)
   - A.3 Additional Details for Fine-tuning (p. 51)
     - A.3.1 Detailed Statistics of Meta Human Preference Data (p. 51)
     - A.3.2 Curriculum Strategy for Meta Human Preference Data (p. 51)
     - A.3.3 Ablation on Ranking Loss with Preference Rating-based Margin for Reward Modeling (p. 51)
     - A.3.4 Ablation on Ranking Loss with Safety Auxiliary Loss for Reward Modeling (p. 52)
     - A.3.5 Additional Results for GAtt (p. 54)
     - A.3.6 How Far Can Model-Based Evaluation Go? (p. 54)
     - A.3.7 Human Evaluation (p. 56)
   - A.4 Additional Details for Safety (p. 58)
     - A.4.1 Tension between Safety and Helpfulness in Reward Modeling (p. 58)
     - A.4.2 Qualitative Results on Safety Data Scaling (p. 58)
     - A.4.3 English Pronouns (p. 58)
     - A.4.4 Context Distillation Preprompts (p. 60)
     - A.4.5 Safety Errors: False Refusals and Vague Responses (p. 60)
     - A.4.6 Examples of Safety Evaluation (p. 66)
     - A.4.7 Description of Automatic Safety Benchmarks (p. 69)
     - A.4.8 Automatic Safety Benchmark Evaluation Results (p. 69)
   - A.5 Data Annotation (p. 72)
     - A.5.1 SFT Annotation Instructions (p. 72)
     - A.5.2 Negative User Experience Categories (p. 74)
     - A.5.3 Quality Assurance Process (p. 74)
     - A.5.4 Annotator Selection (p. 74)
   - A.6 Dataset Contamination (p. 75)
   - A.7 Model Card (p. 77)
