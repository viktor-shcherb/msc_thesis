# Overview

**Title:** The Llama 3 Herd of Models
**Authors:** Llama Team, AI @ Meta
**Affiliations:** Meta
**Date:** July 23, 2024
**Venue:** arXiv:2407.21783v3
**Website:** https://llama.meta.com/

## Abstract

> "Modern artificial intelligence (AI) systems are powered by foundation models. This paper presents a new set of foundation models, called Llama 3. It is a herd of language models that natively support multilinguality, coding, reasoning, and tool usage. Our largest model is a dense Transformer with 405B parameters and a context window of up to 128K tokens. This paper presents an extensive empirical evaluation of Llama 3. We find that Llama 3 delivers comparable quality to leading language models such as GPT-4 on a plethora of tasks. We publicly release Llama 3, including pre-trained and post-trained versions of the 405B parameter language model and our Llama Guard 3 model for input and output safety. The paper also presents the results of experiments in which we integrate image, video, and speech capabilities into Llama 3 via a compositional approach. We observe this approach performs competitively with the state-of-the-art on image, video, and speech recognition tasks. The resulting models are not yet being broadly released as they are still under development." [p. 1]

## Section Headings

1. Introduction
2. General Overview
3. Pre-Training
   - 3.1 Pre-Training Data
     - 3.1.1 Web Data Curation
     - 3.1.2 Determining the Data Mix
     - 3.1.3 Annealing Data
   - 3.2 Model Architecture
     - 3.2.1 Scaling Laws
   - 3.3 Infrastructure, Scaling, and Efficiency
     - 3.3.1 Training Infrastructure
     - 3.3.2 Parallelism for Model Scaling
     - 3.3.3 Collective Communication
     - 3.3.4 Reliability and Operational Challenges
   - 3.4 Training Recipe
     - 3.4.1 Initial Pre-Training
     - 3.4.2 Long Context Pre-Training
     - 3.4.3 Annealing
4. Post-Training
   - 4.1 Modeling
     - 4.1.1 Chat Dialog Format
     - 4.1.2 Reward Modeling
     - 4.1.3 Supervised Finetuning
     - 4.1.4 Direct Preference Optimization
     - 4.1.5 Model Averaging
     - 4.1.6 Iterative Rounds
   - 4.2 Post-training Data
     - 4.2.1 Preference Data
     - 4.2.2 SFT Data
     - 4.2.3 Data Processing and Quality Control
   - 4.3 Capabilities
     - 4.3.1 Code
     - 4.3.2 Multilinguality
     - 4.3.3 Math and Reasoning
     - 4.3.4 Long Context
     - 4.3.5 Tool Use
     - 4.3.6 Factuality
     - 4.3.7 Steerability
5. Results
   - 5.1 Pre-trained Language Model
     - 5.1.1 Standard Benchmarks
     - 5.1.2 Model Robustness
     - 5.1.3 Adversarial Benchmarks
     - 5.1.4 Contamination Analysis
   - 5.2 Post-trained Language Model
     - 5.2.1 General Knowledge and Instruction-Following Benchmarks
     - 5.2.2 Proficiency Exams
     - 5.2.3 Coding Benchmarks
     - 5.2.4 Multilingual Benchmarks
     - 5.2.5 Math and Reasoning Benchmarks
     - 5.2.6 Long Context Benchmarks
     - 5.2.7 Tool Use Performance
   - 5.3 Human Evaluations
   - 5.4 Safety
     - 5.4.1 Benchmark Construction
     - 5.4.2 Safety Pre-training
     - 5.4.3 Safety Finetuning
     - 5.4.4 Safety Results
     - 5.4.5 Cybersecurity and Chemical/Biological Weapons Safety
     - 5.4.6 Red Teaming
     - 5.4.7 System Level Safety
     - 5.4.8 Limitations
6. Inference
   - 6.1 Pipeline Parallelism
   - 6.2 FP8 Quantization
7. Vision Experiments
   - 7.1 Data
     - 7.1.1 Image Data
     - 7.1.2 Video Data
   - 7.2 Model Architecture
   - 7.3 Model Scaling
   - 7.4 Pre-training
   - 7.5 Post-Training
     - 7.5.1 Supervised Finetuning Data
     - 7.5.2 Supervised Finetuning Recipe
     - 7.5.3 Preference Data
     - 7.5.4 Reward Modeling
     - 7.5.5 Direct Preference Optimization
     - 7.5.6 Rejection Sampling
     - 7.5.7 Quality Tuning
   - 7.6 Image Recognition Results
   - 7.7 Video Recognition Results
8. Speech Experiments
   - 8.1 Data
     - 8.1.1 Speech Understanding
     - 8.1.2 Speech Generation
   - 8.2 Model Architecture
     - 8.2.1 Speech Understanding
     - 8.2.2 Speech Generation
   - 8.3 Training Recipe
     - 8.3.1 Speech Understanding
     - 8.3.2 Speech Generation
   - 8.4 Speech Understanding Results
   - 8.5 Speech Generation Results
9. Related Work
   - 9.1 Language
   - 9.2 Multimodality
10. Conclusion
11. Contributors and Acknowledgements
