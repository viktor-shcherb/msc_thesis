# Overview

## Paper Metadata

**Title:** Round and Round We Go! What makes Rotary Positional Encodings useful?

**Authors:**
- Federico Barbero (University of Oxford)*
- Alex Vitvitskyi (Google DeepMind)
- Christos Perivolaropoulos (Google DeepMind)
- Razvan Pascanu (Google DeepMind)
- Petar Veličković (Google DeepMind)

*Work performed while the author was at Google DeepMind.

**Venue:** Published as a conference paper at ICLR 2025

**Date:** arXiv:2410.06205v3 [cs.CL] 13 May 2025

## Abstract

> "Positional Encodings (PEs) are a critical component of Transformer-based Large Language Models (LLMs), providing the attention mechanism with important sequence-position information. One of the most popular types of encoding used today in LLMs are Rotary Positional Encodings (RoPE), that rotate the queries and keys based on their relative distance. A common belief is that RoPE is useful because it helps to decay token dependencies as relative distance increases. In this work, we argue that this is unlikely to be the core reason. We study the internals of a trained Gemma 7B model to understand how RoPE is being used at a mechanical level. We find that Gemma learns to use RoPE to construct robust 'positional' attention patterns, by exploiting the highest frequencies. We also find that, in general, Gemma greatly prefers to use the lowest frequencies of RoPE, which we suspect are used to carry semantic information. We mathematically prove interesting properties of RoPE and conduct experiments to verify our findings, proposing a modification of RoPE that fixes some highlighted issues and improves performance. We believe this work represents an important step in better understanding PEs in LLMs, which we believe holds crucial value for scaling LLMs to large sizes and context lengths."

## Section Headings

1. Introduction
2. Background
   - 2.1 Rotary Positional Encodings (RoPE)
   - 2.2 Related Works
3. Does RoPE decay activations with distance?
4. How are different frequencies used?
5. High frequencies: Positional attention
