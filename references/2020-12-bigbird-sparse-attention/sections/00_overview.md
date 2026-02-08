# Big Bird: Transformers for Longer Sequences

**Authors:** Manzil Zaheer, Guru Guruganesh, Avinava Dubey, Joshua Ainslie, Chris Alberti, Santiago Ontanon, Philip Pham, Anirudh Ravula, Qifan Wang, Li Yang, Amr Ahmed

**Affiliation:** Google Research

**Contact:** {manzilz, gurug, avinavadubey}@google.com

**Venue:** 34th Conference on Neural Information Processing Systems (NeurIPS 2020), Vancouver, Canada.

**Date:** 2020 (arXiv v2: 8 Jan 2021)

## Abstract

> "Transformers-based models, such as BERT, have been one of the most successful deep learning models for NLP. Unfortunately, one of their core limitations is the quadratic dependency (mainly in terms of memory) on the sequence length due to their full attention mechanism. To remedy this, we propose, BIGBIRD, a sparse attention mechanism that reduces this quadratic dependency to linear. We show that BIGBIRD is a universal approximator of sequence functions and is Turing complete, thereby preserving these properties of the quadratic, full attention model. Along the way, our theoretical analysis reveals some of the benefits of having O(1) global tokens (such as CLS), that attend to the entire sequence as part of the sparse attention mechanism. The proposed sparse attention can handle sequences of length up to 8x of what was previously possible using similar hardware. As a consequence of the capability to handle longer context, BIGBIRD drastically improves performance on various NLP tasks such as question answering and summarization. We also propose novel applications to genomics data." [p. 1]

## Section headings (discovered so far)

1. Introduction (p. 1-2)
   - 1.1 Related Work (p. 2-3)
2. BIGBIRD Architecture (p. 3-4)
3. Theoretical Results about Sparse Attention Mechanism (p. 4-6)
   - 3.1 Notation (p. 5)
   - 3.2 Universal Approximators (p. 5)
   - 3.3 Turing Completeness (p. 6)
   - 3.4 Limitations (p. 6)
4. Experiments: Natural Language Processing (p. 6-9)
   - 4.1 Encoder-Decoder Tasks (p. 8-9)
5. Experiments: Genomics (p. 9-10)
6. Conclusion (p. 10)
A. Universal Approximators (p. 17-21)
   - A.1 Notation (p. 17)
   - A.2 Proof (p. 17-20)
     - A.2.1 Approximate F_{CD} by piece-wise constant functions (p. 17-18)
     - A.2.2 Contextual Mappings and Sparse Attention Mechanisms (p. 18-20)
     - A.2.3 Approximating modified Transformers by Transformers (p. 21)
B. Turing Completeness (p. 22-27)
   - B.1 Notation (p. 22)
   - B.2 Details of the Simulation (p. 22-27)
     - B.2.1 Layer 1: Simulate Transition Function (p. 24-25)
     - B.2.2 Layer 2: Finding Head Node (p. 25)
     - B.2.3 Layer 3: Distinguishing Node Type (p. 25-26)
     - B.2.4 Layer 4: Finding next symbol on tape (p. 26-27)
     - B.2.5 Final transformation (p. 27)
C. Limitations (p. 28-29)
D. Implementation details (p. 30-32)
E. NLP experiments details (p. 33-38)
   - E.1 MLM Pretraining (p. 33)
   - E.2 Question Answering (p. 33-35)
   - E.3 Relationship to Contemporary Work (p. 35)
   - E.4 Classification (p. 35-37)
   - E.5 Summarization (p. 37-38)
F. Genomics experiments details (p. 39-42)
   - F.1 Pretraining (p. 39-40)
   - F.2 Promoter Region Prediction (p. 40-41)
   - F.3 Chromatin-Profile Prediction (p. 41-42)
