# Overview

**Title:** The Impact of Positional Encoding on Length Generalization in Transformers

**Authors:** Amirhossein Kazemnejad^1, Inkit Padhi^2, Karthikeyan Natesan Ramamurthy^2, Payel Das^2, Siva Reddy^{1,3,4}

**Affiliations:**
- ^1 Mila, McGill University
- ^2 IBM Research
- ^3 Facebook CIFAR AI Chair
- ^4 ServiceNow Research

**Contact:** {amirhossein.kazemnejad, siva.reddy}@mila.quebec; inkpad@ibm.com; {knatesa, daspa}@us.ibm.com

**Venue:** 37th Conference on Neural Information Processing Systems (NeurIPS 2023)

**Date:** 6 Nov 2023 (arXiv v2: 2305.19466v2)

## Abstract

> "Length generalization, the ability to generalize from small training context sizes to larger ones, is a critical challenge in the development of Transformer-based language models. Positional encoding (PE) has been identified as a major factor influencing length generalization, but the exact impact of different PE schemes on extrapolation in downstream tasks remains unclear. In this paper, we conduct a systematic empirical study comparing the length generalization performance of decoder-only Transformers with five different position encoding approaches including Absolute Position Embedding (APE), T5's Relative PE, ALiBi, and Rotary, in addition to Transformers without positional encoding (NoPE). Our evaluation encompasses a battery of reasoning and mathematical tasks. Our findings reveal that the most commonly used positional encoding methods, such as ALiBi, Rotary, and APE, are not well suited for length generalization in downstream tasks. More importantly, NoPE outperforms other explicit positional encoding methods while requiring no additional computation. We theoretically demonstrate that NoPE can represent both absolute and relative PEs, but when trained with SGD, it mostly resembles T5's Relative PE attention patterns. Finally, we find that scratchpad is not always helpful to solve length generalization and its format highly impacts the model's performance. Overall, our work suggests that explicit position encodings are not essential for decoder-only Transformers to generalize well to longer sequences." [p. 1]

## Section Headings

1. Introduction
2. Background: Positional Encoding in Transformers
3. Model Evaluation
4. What Is The Effect of Positional Encoding?
5. How Does NoPE Represent Positions?
   - 5.1 NoPE can theoretically represent both absolute and relative PEs
   - 5.2 NoPE learns to use relative PE in practice
6. Does Scratchpad Render The Choice of Positional Encoding Irrelevant?
   - 6.1 Which part of the sequence is attended to?
7. Discussion
   - Scaling up to 1B models
   - Perplexity vs. downstream Performance
8. Related Work
   - Length Generalization Failure In Transformers
   - Positional Encoding
9. Conclusion
   - Limitations
- Acknowledgements
- Appendix A: Number of Instances Decreases Rapidly as Sequence Length Grows
- Appendix B: Background
  - B.1 Preliminaries
  - B.2 Positional Encoding
- Appendix C: Proofs
  - C.1 Absolute Positional Encoding in NoPE
  - C.2 Relative Positional Encoding in NoPE
- Appendix D: Experimental Details
  - D.1 Tasks
  - D.2 Hyperparameters
  - D.3 Compute
  - D.4 Reproducibility
- Appendix E: Full Results
  - E.1 Detailed Model Accuracy
  - E.2 Detailed Head Distance
  - E.3 Detailed Model Accuracy On Various Scratchpad Formats
- Appendix F: Pretraining at 1.3B Scale
  - F.1 Model Architecture
  - F.2 Dataset Selection
  - F.3 Generalization Evaluation
