# Overview

**Title:** Gemma 3 Technical Report

**Authors:** Gemma Team, Google DeepMind

**Affiliations:** Google DeepMind

**Venue/Date:** arXiv:2503.19786 [cs.CL], 2025-03-12

**Abstract:**
> "We introduce Gemma 3, a multimodal addition to the Gemma family of lightweight open models, ranging in scale from 1 to 27 billion parameters. This version introduces vision understanding abilities, a wider coverage of languages and longer context – at least 128K tokens. We also change the architecture of the model to reduce the KV-cache memory that tends to explode with long context. This is achieved by increasing the ratio of local to global attention layers, and keeping the span on local attention short. The Gemma 3 models are trained with distillation and achieve superior performance to Gemma 2 for both pre-trained and instruction finetuned versions. In particular, our novel post-training recipe significantly improves the math, chat, instruction-following and multilingual abilities, making Gemma3-4B-IT competitive with Gemma-2-27B-IT and Gemma3-27B-IT comparable to Gemini-1.5-Pro across benchmarks. We release all our models to the community."

**Section headings:**
1. Introduction
2. Model Architecture
   - 2.1. Vision modality
   - 2.2. Pre-training
   - 2.3. Quantization Aware Training
   - 2.4. Compute Infrastructure
3. Instruction-Tuning
4. Evaluation of final models
   - 4.1. LMSYS Chatbot Arena
   - 4.2. Standard benchmarks
5. Ablations
   - 5.1. Pre-training ability probing
   - 5.2. Local:Global attention layers
   - 5.3. Enabling long context
   - 5.4. Small versus large teacher
   - 5.5. Vision encoder
6. Memorization and Privacy
7. Responsibility, Safety, Security
   - 7.1. Governance & Assessment
   - 7.2. Safety policies and train-time mitigations
   - 7.3. Assurance Evaluations
   - 7.4. Our approach to responsible open models
8. Discussion and Conclusion
Appendix (Tables 9-21, detailed benchmark results)

**Contact:** gemma-3-report@google.com
