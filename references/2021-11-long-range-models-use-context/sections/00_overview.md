# Do Long-Range Language Models Actually Use Long-Range Context?

**Authors:** Simeng Sun^1, Kalpesh Krishna^1, Andrew Mattarella-Micke^2, Mohit Iyyer^1
**Affiliations:** University of Massachusetts Amherst^1, Intuit AI^2
**Contact:** {simengsun,kalpesh,miyyer}@cs.umass.edu, andrew_mattarella-micke@intuit.com
**Venue:** arXiv:2109.09115v1 [cs.CL]
**Date:** 19 Sep 2021

## Abstract

> "Language models are generally trained on short, truncated input sequences, which limits their ability to use discourse-level information present in long-range context to improve their predictions. Recent efforts to improve the efficiency of self-attention have led to a proliferation of long-range Transformer language models, which can process much longer sequences than models of the past. However, the ways in which such models take advantage of the long-range context remain unclear. In this paper, we perform a fine-grained analysis of two long-range Transformer language models (including the Routing Transformer, which achieves state-of-the-art perplexity on the PG-19 long-sequence LM benchmark dataset) that accept input sequences of up to 8K tokens. Our results reveal that providing long-range context (i.e., beyond the previous 2K tokens) to these models only improves their predictions on a small set of tokens (e.g., those that can be copied from the distant context) and does not help at all for sentence-level prediction tasks. Finally, we discover that PG-19 contains a variety of different document types and domains, and that long-range context helps most for literary novels (as opposed to textbooks or magazines)." [p. 1]

## Section headings

1. Introduction
2. Background & Setup
   - 2.1 Long-range Language Modeling
   - 2.2 Experimental setup
3. The effect of longer context
4. The perturbation of long-range context
5. Sequence-level analysis
6. Related work
7. Conclusion
- Ethical concerns
- Acknowledgements
- Appendix A: Routing Transformer and end-sequence degradation
- Appendix B: Effect of longer context
- Appendix C: Token overlaps
- Appendix D: Perturbation
- Appendix E: Suffix Identification
- Appendix F: Local Transformer checkpoint results
