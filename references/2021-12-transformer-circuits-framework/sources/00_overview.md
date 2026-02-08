# A Mathematical Framework for Transformer Circuits

**Author(s):** Nelson Elhage, Neel Nanda, Catherine Olsson, Tom Henighan, Nicholas Joseph, Ben Mann, Amanda Askell, Yuntao Bai, Anna Chen, Tom Conerly, Nova DasSarma, Dawn Drain, Deep Ganguli, Zac Hatfield-Dodds, Danny Hernandez, Andy Jones, Jackson Kernion, Liane Lovitt, Kamal Ndousse, Dario Amodei, Tom Brown, Jack Clark, Jared Kaplan, Sam McCandlish, Chris Olah
**Type:** Blog post (long-form research article)
**Date:** December 2021
**Primary URL:** https://transformer-circuits.pub/2021/framework/index.html

## Summary

This article presents a mathematical framework for reverse-engineering transformer models by analyzing their weight matrices directly. By studying simplified attention-only transformers (zero-layer, one-layer, and two-layer), the authors decompose transformer computations into interpretable circuits built from QK (query-key) and OV (output-value) matrix products. The framework reveals that zero-layer transformers implement bigram statistics, one-layer transformers implement skip-trigrams, and two-layer transformers can compose attention heads to form "induction heads" -- a general in-context learning algorithm. This work is foundational to the field of mechanistic interpretability.

## Source structure

1. **Main article** (`01_main-article.md`) -- The full Transformer Circuits Thread article at transformer-circuits.pub, covering the mathematical framework, residual stream conceptualization, attention head decomposition into QK/OV circuits, composition types (Q-composition, K-composition, V-composition), virtual attention heads, analysis of zero/one/two-layer transformers, induction heads, skip-trigrams, eigenvalue analysis, and ablation studies.
2. **Anthropic research announcement** (`02_anthropic-announcement.md`) -- The research page at anthropic.com providing summary and contextual framing within Anthropic's broader interpretability research agenda.
