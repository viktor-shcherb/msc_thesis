# Overview

**Title:** Lost in the Middle, and In-Between: Enhancing Language Models' Ability to Reason Over Long Contexts in Multi-Hop QA

**Authors:** George Arthur Baker, Ankush Raut, Sagi Shaier, Lawrence E Hunter, Katharina von der Wense

**Affiliations:**
- George Arthur Baker: University of Colorado Boulder
- Ankush Raut: University of Colorado Boulder
- Sagi Shaier: University of Colorado Boulder
- Lawrence E Hunter: University of Colorado Boulder
- Katharina von der Wense: University of Colorado Boulder, University of Chicago Department of Pediatrics, Johannes Gutenberg University Mainz

**Contact:** {george.baker, sagi.shaier, katharina.kann}@colorado.edu

**Venue:** arXiv:2412.10079 [cs.CL]

**Date:** 13 Dec 2024

**Code and Data:** https://github.com/Spongeorge/long-context-multihop

## Abstract

> "Previous work finds that recent long-context language models tend to make equal use of information in the middle of their inputs, preferring pieces of information located at the tail ends or located at undue bias in situations where we would like models to be equally capable of using relevant parts of the input. Thus far, the problem has mainly only been considered in settings with single pieces of critical information, leaving it an open question how much the problem arises when multiple necessary pieces of information are spread over the context. Here, we demonstrate the effects of the "lost in the middle" problem in the multi-hop answering setting — in which multiple reasoning "hops" over disconnected documents are required — and show the performance degrades not only with respect to the distance of information from the edges of the context, but also between pieces of information. Additionally, we experiment with means of alleviating the problem by reducing extraneous document contents through knowledge graph triple extraction and summarization, and prompting models to reason more thoroughly using chain-of-thought prompting. We make our code and data available at: https://github.com/Spongeorge/long-context-multihop"

## Section Headings

From pages 1-13 (complete):
- 1 Introduction
- 2 Related Work
  - 2.1 The "Lost in the Middle" Problem
  - 2.2 Mitigation Strategies for "Lost in the Middle"
  - 2.3 Multi-Hop Question Answering
  - 2.4 Impact of Input Length on Reasoning
- 3 Experiments
  - 3.1 Datasets
    - 3.1.1 Models
    - 3.1.2 Metrics
    - 3.1.3 Context Reduction Methods
- 4 Methodology
- 5 Results
- 6 Analysis
- 7 Future Work
- 8 Conclusion
- Limitations
- References
- Appendix A: Full Results
