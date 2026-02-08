# What Context Features Can Transformer Language Models Use?

**Authors:** Joe O'Connor, Jacob Andreas
**Affiliations:** Massachusetts Institute of Technology
**Contact:** {joeoc, jda}@mit.edu
**Venue:** arXiv:2106.08367v1 [cs.CL]
**Date:** 15 Jun 2021
**Code:** https://github.com/lingo-mit/context-ablations

## Abstract

> "Transformer-based language models benefit from conditioning on contexts of hundreds to thousands of previous tokens. What aspects of these contexts contribute to accurate model prediction? We describe a series of experiments that measure *usable information* by selectively ablating lexical and structural information in transformer language models trained on English Wikipedia. In both mid- and long-range contexts, we find that several extremely destructive context manipulations---including shuffling word order within sentences and deleting all words other than nouns---remove less than 15% of the usable information. Our results suggest that long contexts, but not their detailed syntactic and propositional content, are important for the low perplexity of current transformer language models." [p. 1]

## Section headings

1. Introduction
2. Approach
3. Experiments
   - 3.1 Does order matter?
   - 3.2 Do all words matter?
   - 3.3 Evaluating on augmented data
   - 3.4 Making better language models?
4. Related Work
5. Discussion
- Acknowledgments
- Impact Statement
- References
- Appendix A: Comparison of Experimental Paradigms
- Appendix B: Longer Context Window
- Appendix C: Sample Generations
