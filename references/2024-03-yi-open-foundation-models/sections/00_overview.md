# Overview

**Title:** Yi: Open Foundation Models by 01.AI

**Authors:** 01.AI (see Appendix A for full author list and contributions)

**Affiliations:** 01.AI

**Venue:** arXiv preprint, arXiv:2403.04652v3

**Date:** 21 Jan 2025 (v3)

**Code:** https://github.com/01-ai/Yi
**Model:** https://huggingface.co/01-ai

## Abstract

> "We introduce the Yi model family, a series of language and multimodal models that demonstrate strong multi-dimensional capabilities. The Yi model family is based on 6B and 34B pretrained language models, then we extend them to chat models, 200K long context models, depth-upscaled models, and vision-language models. Our base models achieve strong performance on a wide range of benchmarks like MMLU, and our finetuned chat models deliver strong human preference rate on major evaluation platforms like AlpacaEval and Chatbot Arena. Building upon our scalable super-computing infrastructure and the classical transformer architecture, we attribute the performance of Yi models primarily to its data quality resulting from our data-engineering efforts. For pretraining, we construct 3.1 trillion tokens of English and Chinese corpora using a cascaded data deduplication and quality filtering pipeline. For finetuning, we polish a small scale (less than 10K) instruction dataset over multiple iterations such that every single instance has been verified directly by our machine learning engineers. For vision-language, we combine the chat language model with a vision transformer encoder and train the model to align visual representations to the semantic space of the language model. We further extend the context length to 200K through lightweight continual pretraining and demonstrate strong needle-in-a-haystack retrieval performance. We show that extending the depth of the pretrained checkpoint through continual pretraining further improves performance. We believe that given our current results, continuing to scale up model parameters using thoroughly optimized data will lead to even stronger frontier models." [p. 1]

## Section Headings

1. Introduction (p. 3)
2. Pretraining (p. 4)
   - 2.1 Data Processing (p. 4)
   - 2.2 Tokenization (p. 5)
   - 2.3 Model Architecture (p. 6)
3. Finetuning (p. 6)
   - 3.1 Data Preprocessing (p. 6)
   - 3.2 Training Method (p. 7)
4. Infrastructure (p. 7)
5. Safety (p. 9)
6. Evaluations (p. 9)
   - 6.1 Base Model Performance (p. 9)
     - 6.1.1 Main Results (p. 9)
     - 6.1.2 Discussions (p. 10)
     - 6.1.3 In-Context Learning Study (p. 11)
   - 6.2 Chat Model Performance (p. 12)
     - 6.2.1 Automatic Evaluations (p. 12)
     - 6.2.2 Human Evaluations (p. 12)
7. Capability Extension (p. 14)
   - 7.1 Long Context Modeling (p. 14)
   - 7.2 Vision-Language (p. 15)
   - 7.3 Depth Upscaling (p. 16)
8. Final Discussions (p. 18)
A. Author List and Contributions (p. 19)
References (p. 20–26)
