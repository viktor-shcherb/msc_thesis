# GPT-4 Technical Report

**Authors:** OpenAI

**Affiliations:** OpenAI

**Venue:** arXiv (cs.CL), 2303.08774v6

**Date:** 4 Mar 2024 (arXiv v6)

**Correspondence:** gpt4-report@openai.com

> "We report the development of GPT-4, a large-scale, multimodal model which can accept image and text inputs and produce text outputs. While less capable than humans in many real-world scenarios, GPT-4 exhibits human-level performance on various professional and academic benchmarks, including passing a simulated bar exam with a score around the top 10% of test takers. GPT-4 is a Transformer-based model pre-trained to predict the next token in a document. The post-training alignment process results in improved performance on measures of factuality and adherence to desired behavior. A core component of this project was developing infrastructure and optimization methods that behave predictably across a wide range of scales. This allowed us to accurately predict some aspects of GPT-4's performance based on models trained with no more than 1/1,000th the compute of GPT-4." [p. 1]

## Section headings (observed so far)

1. Introduction
2. Scope and Limitations of this Technical Report
3. Predictable Scaling
   - 3.1 Loss Prediction
   - 3.2 Scaling of Capabilities on HumanEval
4. Capabilities
   - 4.1 Visual Inputs
5. Limitations
6. Risks & mitigations
7. Conclusion
8. Authorship, Credit Attribution, and Acknowledgements
References
Appendix
   - A. Exam Benchmark Methodology
     - A.1 Sourcing
     - A.2 Prompting: multiple-choice
     - A.3 Prompting: free-response
     - A.4 Images
     - A.5 Scoring
     - A.6 Codeforces rating
     - A.7 Model snapshot details
     - A.8 Example few-shot prompts
   - B. Impact of RLHF on capability
   - C. Contamination on professional and academic exams
   - D. Contamination on academic benchmarks
   - E. GSM-8K in GPT-4 training
   - F. Multilingual MMLU
   - G. Examples of GPT-4 Visual Input
   - H. System Card
     - H.1 Introduction
       - H.1.1 Overview of findings and mitigations
     - H.2 GPT-4 Observed Safety Challenges
       - H.2.1 Evaluation Approach
         - H.2.1.1 Qualitative Evaluations
         - H.2.1.2 Quantitative Evaluations
       - H.2.2 Hallucinations
       - H.2.3 Harmful Content
       - H.2.4 Harms of representation, allocation, and quality of service
       - H.2.5 Disinformation and Influence Operations
       - H.2.6 Proliferation of Conventional and Unconventional Weapons
       - H.2.7 Privacy
       - H.2.8 Cybersecurity
       - H.2.9 Potential for Risky Emergent Behaviors
       - H.2.10 Interactions with other systems
       - H.2.11 Economic Impacts
       - H.2.12 Acceleration
       - H.2.13 Overreliance
     - H.3 Deployment Preparation
       - H.3.1 Model Mitigations
     - H.4 System Safety
       - H.4.1 Usage Policies and Monitoring
       - H.4.2 Content Classifier Development
     - H.5 Conclusion and Next Steps
     - H.6 Acknowledgements
     - References (System Card bibliography)
     - A. Full RBRM Instructions for Classifying Refusal Styles (System Card Appendix)
     - B. Full RBRM Instructions for Classifying Regulated Advice (System Card Appendix)
     - C. Full RBRM Instructions for Classifying Sexual Content (System Card Appendix)
     - D. Harmful Content Table Full Examples (System Card Appendix)
     - E. Harms of Representation Table Examples (System Card Appendix)
     - F. Disinformation and Influence Operations Table Examples (System Card Appendix)
     - Full Chemical Compound Similarity and Purchase Tool Use Example (System Card Appendix)
