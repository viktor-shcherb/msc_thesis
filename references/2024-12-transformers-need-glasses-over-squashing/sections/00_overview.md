# Overview

## Paper Metadata

**Title:** Transformers need glasses! Information over-squashing in language tasks

**Authors:** Federico Barbero*, Andrea Banino, Steven Kapturowski, Dharshan Kumaran, João G.M. Araújo, Alex Vitvitskyi, Razvan Pascanu, Petar Veličković

**Affiliations:**
- Federico Barbero*: University of Oxford, federico.barbero@cs.ox.ac.uk
- Andrea Banino: Google DeepMind, abanino@google.com
- Steven Kapturowski: Google DeepMind, skapturowski@google.com
- Dharshan Kumaran: Google DeepMind, dkumaran@google.com
- João G.M. Araújo: Google DeepMind, joaogiu@google.com
- Alex Vitvitskyi: Google DeepMind, avlife@google.com
- Razvan Pascanu: Google DeepMind, razp@google.com
- Petar Veličković: Google DeepMind, petarv@google.com

*Work performed while at Google DeepMind.

**Venue:** 38th Conference on Neural Information Processing Systems (NeurIPS 2024)

**Date:** October 24, 2024 (arXiv:2406.04267v2)

## Abstract

> We study how information propagates in decoder-only Transformers, which are the architectural backbone of most existing frontier large language models (LLMs). We carry out a theoretical signal propagation analysis—specifically, we analyse the representations of the last token in the final layer of the Transformer: this is the representation that will be used for next-token prediction. Our analysis reveals a representational collapse phenomenon: we prove that certain distinct sequences of inputs to the Transformer yield arbitrarily close representations in the final token. This effect is exacerbated by the low-precision floating-point formats frequently used in modern LLMs. As a result, the model is provably unable to respond to these sequences in different ways—leading to errors in, e.g., tasks involving counting or copying. Further, we show that decoder-only Transformer language models can lose sensitivity to specific tokens in the input, which relates to the well-known phenomenon of over-squashing in graph neural networks. We provide empirical evidence supporting our claims on contemporary LLMs. Our theory also points to simple solutions towards ameliorating these issues.

## Section Headings

1. Abstract
2. 1 Introduction
   - 1.1 Contributions
3. 2 Background
   - 2.1 Related Work
4. 3 Motivating Examples
   - 3.1 Copying
   - 3.2 Counting
5. 4 Representational Collapse
6. 5 Over-squashing in Language Tasks
7. 6 Counting
8. 7 Conclusion and Future Work
9. 8 Acknowledgements
10. References
11. Appendix A: Broader Impact
12. Appendix B: Proofs
    - B.1 Representational Collapse
    - B.2 Over-squashing
    - B.3 Counting
13. Appendix C: Experiments
    - C.1 Experimental Details
    - C.2 Counting with Gemma
    - C.3 Synthetic Experiments on Representational Collapse
    - C.4 Effect of Positional Encodings
    - C.5 Ablation on Prompt Structure
    - C.6 Local sliding window attention
