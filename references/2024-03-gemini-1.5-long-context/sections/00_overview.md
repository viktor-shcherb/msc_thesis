# Overview

**Title:** Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context

**Authors:** Gemini Team, Google

**Affiliations:** Google DeepMind

**Venue:** arXiv preprint (arXiv:2403.05530v5)

**Date:** 16 Dec 2024

**Correspondence:** gemini-1_5-report@google.com

## Abstract

> "In this report, we introduce the Gemini 1.5 family of models, representing the next generation of highly compute-efficient multimodal models capable of recalling and reasoning over fine-grained information from millions of tokens of context, including multiple long documents and hours of video and audio. The family includes two new models: (1) an updated Gemini 1.5 Pro, which exceeds the February version on the great majority of capabilities and benchmarks; (2) Gemini 1.5 Flash, a more lightweight variant designed for efficiency with minimal regression in quality. Gemini 1.5 models achieve near-perfect recall on long-context retrieval tasks across modalities, improve the state-of-the-art in long-document QA, long-video QA and long-context ASR, and match or surpass Gemini 1.0 Ultra's state-of-the-art performance across a broad set of benchmarks. Studying the limits of Gemini 1.5's long-context ability, we find continued improvement in next-token prediction and near-perfect retrieval (>99%) up to at least 10M tokens, a generational leap over existing models such as Claude 3.0 (200k) and GPT-4 Turbo (128k). Finally, we highlight real-world use cases, such as Gemini 1.5 collaborating with professionals on completing their tasks achieving 26 to 75% time savings across 10 different job categories, as well as surprising new capabilities of large language models at the frontier; when given a grammar manual for Kalamang, a language with fewer than 200 speakers worldwide, the model learns to translate English to Kalamang at a similar level to a person who learned from the same content." [p. 1]

## Section Headings

1. Introduction
2. An Improved Gemini 1.5 Pro
3. Model Architecture
   - 3.1. Gemini 1.5 Pro
   - 3.2. Gemini 1.5 Flash
   - 3.3. Serving efficiency and latency
4. Training Infrastructure and Dataset
5. Evaluation Results
   - 5.1. Qualitative Examples of Multimodal Long-Context Capabilities
   - 5.2. Long-context Evaluations
     - 5.2.1. Diagnostic Long-Context Evaluations
       - 5.2.1.1 Perplexity over Long Sequences
       - 5.2.1.2 Text Haystack
       - 5.2.1.3 Video Haystack
       - 5.2.1.4 Audio Haystack
       - 5.2.1.5 Improved Diagnostics
     - 5.2.2. Realistic Long-Context Evaluations
       - 5.2.2.1 In-context language learning -- learning to translate a new language from one book
       - 5.2.2.2 In-context language learning -- learning to transcribe speech in a new language in context
       - 5.2.2.3 Scaling In-Context learning for low-resource machine translation
       - 5.2.2.4 Long-document QA
       - 5.2.2.5 Long-context Audio
       - 5.2.2.6 Long-context Video QA
       - 5.2.2.7 In-Context Planning
       - 5.2.2.8 Unstructured Multimodal Data Analytics Task
6. Core Capability Evaluations
   - 6.1. Core Text Evals
     - 6.1.1. Math and Science
     - 6.1.2. General Reasoning
     - 6.1.3. Code
     - 6.1.4. Multilinguality
     - 6.1.5. Function Calling
     - 6.1.6. Instruction Following
     - 6.1.7. Real-world and long-tail expert GenAI tasks
   - 6.2. Core Vision Multimodal Evaluations
     - 6.2.1. Multimodal Reasoning
     - 6.2.2. Charts and Document Understanding
     - 6.2.3. Natural Image Understanding
     - 6.2.4. Video Understanding
   - 6.3. Core Audio Multimodal Evaluations
7. Advancing Mathematical Reasoning
8. Flash-8B: Pushing the Frontier for More Efficient Models
9. Safety, Security, and Responsibility
   - 9.1. Our Process
   - 9.2. Policies and Desiderata
     - 9.2.1. Identifying risks (potential impact assessments)
     - 9.2.2. Safety policies
     - 9.2.3. Desiderata, aka "helpfulness"
   - 9.3. Training for Safety, Security, and Responsibility
     - 9.3.1. Pre-Training
     - 9.3.2. Supervised Fine-Tuning
     - 9.3.3. Reinforcement Learning from Human Feedback
   - 9.4. Results on Training/Development Evaluations
     - 9.4.1. Policy Violations
     - 9.4.2. Helpfulness
     - 9.4.3. Security and Privacy
     - 9.4.4. Representational Harms
   - 9.5. Assurance Evaluations
     - 9.5.1. Baseline Assurance
     - 9.5.2. Dangerous Capability Evaluations
   - 9.6. External Safety Testing
     - 9.6.1. Societal risks
     - 9.6.2. Radiological and Nuclear risks
     - 9.6.3. Cyber risks
   - 9.7. Product Deployment
10. Discussion
11. Contributions and Acknowledgments
12. Appendix
   - 12.1. Model Card
   - 12.2. Further haystack results
   - 12.3. Automatic question-generation pipeline for Long-document QA
   - 12.4. Multilingual performance breakdown
   - 12.5. Long context video
     - 12.5.1. Video Haystack
     - 12.5.2. 1H-Video QA Hard Examples
   - 12.6. Generic long context math prompting
     - 12.6.1. Hendrycks' MATH Dataset: Performance Analysis and Potential for Improvement
     - 12.6.2. Intermediate Algebra (Levels 4 and 5): A Persistent Challenge
     - 12.6.3. Leveraging Python and SymPy for Enhanced Performance
     - 12.6.4. Generic long prompt as an alternative to sophisticated prompts and fine-tuning
     - 12.6.5. Python Evaluation Process
     - 12.6.6. Downloading and preparing all SymPy and SciPy examples
     - 12.6.7. An expert-written Python Minerva prompt
     - 12.6.8. Example instructions added to Python prompts
     - 12.6.9. Example problem and a Gemini 1.5 Pro solution
   - 12.7. Unstructured Multimodal Data Analytics
   - 12.8. Planning
   - 12.9. Productivity Impact of LLMs Across Jobs
   - 12.10. Expertise QA
     - 12.10.1. Results
     - 12.10.2. Instructions to in-house experts (example with 5 models)
   - 12.11. STEM QA with Context: Data and Human Evaluation
   - 12.12. QA for Web Search Topics
     - 12.12.1. Examples of TREC Search Topic Description
   - 12.13. Prompts and answer extraction strategies
     - 12.13.1. BBH
     - 12.13.2. DROP
     - 12.13.3. Hellaswag
     - 12.13.4. MMLU
     - 12.13.5. AMC
     - 12.13.6. MATH
     - 12.13.7. GSM8K
     - 12.13.8. GPQA
     - 12.13.9. PhysicsFinals
     - 12.13.10. HumanEval and Natural2Code
   - 12.14. Vision tasks
     - 12.14.1. V* benchmark
     - 12.14.2. AI2D
     - 12.14.3. MMMU
     - 12.14.4. MathVista
     - 12.14.5. ChartQA
     - 12.14.6. ChemicalDiagramQA
     - 12.14.7. DocVQA
     - 12.14.8. DUDE
     - 12.14.9. TAT-DQA
     - 12.14.10. InfographicVQA
     - 12.14.11. TextVQA
     - 12.14.12. VQAv2
   - 12.15. Blink
   - 12.16. RealworldQA
     - 12.16.1. ActivityNet-QA
     - 12.16.2. EgoSchema
     - 12.16.3. VATEX
     - 12.16.4. YouCook2
     - 12.16.5. OpenEQA
     - 12.16.6. Text Needle-in-a-Haystack
     - 12.16.7. Video Needle-in-a-Haystack
     - 12.16.8. Audio Needle-in-a-Haystack
     - 12.16.9. Multi-round Co-reference Resolution (MRCR)
     - 12.16.10. Long-document QA
     - 12.16.11. 1H-VideoQA
     - 12.16.12. Long-context Audio
     - 12.16.13. MTOB
     - 12.16.14. ASROB
     - 12.16.15. Multilinguality
     - 12.16.16. Dolomites
   - 12.17. More MTOB results
     - 12.17.1. Qualitative Examples
   - 12.18. More BetterChartQA Details and Results
