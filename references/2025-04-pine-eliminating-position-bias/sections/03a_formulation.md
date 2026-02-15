# 3.1 Formulation [p. 3]

The authors take retrieval-augmented QA as an example, where current LMs' performance may greatly suffer from position bias (Liu et al., 2024) [p. 3].

## Task Setup

The task requires the model to answer a question based on a set of given retrieved documents, where one of them contains the correct answer [p. 3]. The system prompt SYS is: `"Write a high-quality one-sentence answer for the given question using only the provided search results (some of which might be irrelevant)."` [p. 3].

Given a question Q, and three retrieved documents: D₁, D₂, and D₃, the authors can formulate several different inputs. For example, `[SYS|Q|D₂|D₃|D₁]` and `[SYS|Q|D₃|D₁]` [p. 3].

The authors expect models to have the same output for these inputs because D₂, D₃, D₁ are **position-agnostic documents**: their relative order is not supposed to affect the final result [p. 3]. However, the current LMs answer differently when presented with these different inputs and tend to answer correctly when the document contains the answer at the beginning or at the end of all documents (Liu et al., 2024) [p. 3].

## Problem Statement

The systematic differences of model outputs caused by relative positions of documents reflect the **position bias** of the model [p. 3]. Therefore, current LMs cannot conduct **inter-document position-invariant** inference, and the goal is to make the inference invariant w.r.t. relative document orders [p. 3].

In the rest of this section, the authors will use this running example. However, they emphasize that "documents" have different meanings in different tasks: responses in LM-as-a-judge, properties in molecule generation, and conditions in math reasoning [p. 3-4]. Therefore, readers should be aware that the method is not just designed for a single task. In the rest of the paper, the authors merge SYS and Q into SYS for simplicity [p. 4].
