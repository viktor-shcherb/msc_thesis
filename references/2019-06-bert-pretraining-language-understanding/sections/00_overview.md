# Overview

**Title:** BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding

**Authors:** Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova

**Affiliation:** Google AI Language

**Venue:** NAACL 2019 (arXiv:1810.04805v2, 24 May 2019)

**Abstract:**
> "We introduce a new language representation model called BERT, which stands for Bidirectional Encoder Representations from Transformers. Unlike recent language representation models (Peters et al., 2018a; Radford et al., 2018), BERT is designed to pre-train deep bidirectional representations from unlabeled text by jointly conditioning on both left and right context in all layers. As a result, the pre-trained BERT model can be fine-tuned with just one additional output layer to create state-of-the-art models for a wide range of tasks, such as question answering and language inference, without substantial task-specific architecture modifications."

> "BERT is conceptually simple and empirically powerful. It obtains new state-of-the-art results on eleven natural language processing tasks, including pushing the GLUE score to 80.5% (7.7% point absolute improvement), MultiNLI accuracy to 86.7% (4.6% absolute improvement), SQuAD v1.1 question answering Test F1 to 93.2 (1.5 point absolute improvement) and SQuAD v2.0 Test F1 to 83.1 (5.1 point absolute improvement)."

## Section headings (observed so far)

1. Introduction
2. Related Work
   - 2.1 Unsupervised Feature-based Approaches
   - 2.2 Unsupervised Fine-tuning Approaches
   - 2.3 Transfer Learning from Supervised Data
3. BERT
   - 3.1 Pre-training BERT
   - 3.2 Fine-tuning BERT
4. Experiments
   - 4.1 GLUE
   - 4.2 SQuAD v1.1
   - 4.3 SQuAD v2.0
   - 4.4 SWAG
5. Ablation Studies
   - 5.1 Effect of Pre-training Tasks
   - 5.2 Effect of Model Size
   - 5.3 Feature-based Approach with BERT
6. Conclusion
7. Appendix A: Additional Details for BERT
   - A.1 Illustration of the Pre-training Tasks
   - A.2 Pre-training Procedure
   - A.3 Fine-tuning Procedure
   - A.4 Comparison of BERT, ELMo, and OpenAI GPT
   - A.5 Illustrations of Fine-tuning on Different Tasks
8. Appendix B: Detailed Experimental Setup
   - B.1 Detailed Descriptions for the GLUE Benchmark Experiments
9. Appendix C: Additional Ablation Studies
   - C.1 Effect of Number of Training Steps
   - C.2 Ablation for Different Masking Procedures
