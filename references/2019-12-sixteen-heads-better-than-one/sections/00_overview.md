# Overview

**Title:** Are Sixteen Heads Really Better than One?

**Authors:**
- Paul Michel, Language Technologies Institute, Carnegie Mellon University, Pittsburgh, PA (pmichel1@cs.cmu.edu)
- Omer Levy, Facebook Artificial Intelligence Research, Seattle, WA (omerlevy@fb.com)
- Graham Neubig, Language Technologies Institute, Carnegie Mellon University, Pittsburgh, PA (gneubig@cs.cmu.edu)

**Venue:** 33rd Conference on Neural Information Processing Systems (NeurIPS 2019), Vancouver, Canada.

**Date:** 2019 (arXiv: 1905.10650v3, 4 Nov 2019)

**Code:** https://github.com/pmichel31415/are-16-heads-really-better-than-1

**Abstract:**

> "Attention is a powerful and ubiquitous mechanism for allowing neural models to focus on particular salient pieces of information by taking their weighted average when making predictions. In particular, multi-headed attention is a driving force behind many recent state-of-the-art natural language processing (NLP) models such as Transformer-based MT models and BERT. These models apply multiple attention mechanisms in parallel, with each attention "head" potentially focusing on different parts of the input, which makes it possible to express sophisticated functions beyond the simple weighted average. In this paper we make the surprising observation that even if models have been trained using multiple heads, in practice, a large percentage of attention heads can be removed at test time without significantly impacting performance. In fact, some layers can even be reduced to a single head. We further examine greedy algorithms for pruning down models, and the potential speed, memory efficiency, and accuracy improvements obtainable therefrom. Finally, we analyze the results with respect to which parts of the model are more reliant on having multiple heads, and provide precursory evidence that training dynamics play a role in the gains provided by multi-head attention." [p. 1]

## Section headings

1. Introduction
2. Background: Attention, Multi-headed Attention, and Masking
   - 2.1 Single-headed Attention
   - 2.2 Multi-headed Attention
   - 2.3 Masking Attention Heads
3. Are All Attention Heads Important?
   - 3.1 Experimental Setup
   - 3.2 Ablating One Head
   - 3.3 Ablating All Heads but One
   - 3.4 Are Important Heads the Same Across Datasets?
4. Iterative Pruning of Attention Heads
   - 4.1 Head Importance Score for Pruning
   - 4.2 Effect of Pruning on BLEU/Accuracy
   - 4.3 Effect of Pruning on Efficiency
5. When Are More Heads Important? The Case of Machine Translation
6. Dynamics of Head Importance during Training
7. Related Work
8. Conclusion
A. Ablating All Heads but One: Additional Experiment
B. Additional Pruning Experiments
