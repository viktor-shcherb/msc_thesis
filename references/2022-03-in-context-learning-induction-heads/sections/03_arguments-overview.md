# Arguments that induction heads are the mechanism for the majority of in-context learning [p. 8-9]

[p. 8] The main part of the paper makes the case that induction heads may *provide the primary mechanism* for the majority of in-context learning for transformer models in general. As stated in the introduction, this is a very broad hypothesis and much of the evidence is indirect, but the authors believe that all the lines of evidence together make a relatively strong, though not conclusive, case. [p. 8]

## Evidence strength summary [p. 8]

Before going through the arguments, the authors delineate where the evidence is more conclusive vs. less conclusive:

- For small, attention-only models, the authors believe they have strong evidence that attention heads are the mechanism for the majority of in-context learning, as they have evidence supported by ablations and mechanistic reverse engineering.
- Conversely, for all models, they can make a strong case that induction heads play *some role* in in-context learning, as they can demonstrate examples and show suggestive correlations.
- However, the larger the models get, the harder it is to establish that induction heads account for the actual *majority* of in-context learning. For large models with MLPs, they must rely on mainly correlational evidence, which could be confounded.
- Alternate hypotheses are explored throughout, including at the end of Argument 1 and again briefly in Argument 6. [p. 8]

### Summary of evidence for sub-claims (strongest argument for each) [p. 9]

|                      | Small Attention-Only   | Small with MLPs                          | Large Models              |
|----------------------|------------------------|------------------------------------------|---------------------------|
| Contributes Some     | Strong, Causal         | Strong, Causal                           | Medium, Correlational & Mechanistic |
| Contributes Majority | Strong, Causal         | Medium, Causal                           | Medium, Correlational     |

## List of arguments [p. 9]

The list of arguments, one per section (repeated from the introduction):

- **Argument 1** (*Macroscopic co-occurrence*): Transformer language models undergo a "phase change" early in training, during which induction heads form and simultaneously in-context learning improves dramatically.

- **Argument 2** (*Macroscopic co-perturbation*): When the transformer architecture is changed in a way that shifts whether induction heads can form (and when), the dramatic improvement in in-context learning shifts in a precisely matching way.

- **Argument 3** (*Direct ablation*): When induction heads are directly "knocked out" at test-time in small models, the amount of in-context learning greatly decreases.

- **Argument 4** (*Specific examples of induction head generality*): Although induction heads are defined very narrowly in terms of copying literal sequences, the same heads are empirically observed to also implement more sophisticated types of in-context learning, including highly abstract behaviors, making it plausible they explain a large fraction of in-context learning.

- **Argument 5** (*Mechanistic plausibility of induction head generality*): For small models, induction heads can be explained mechanistically, and it can be shown they contribute to in-context learning. Furthermore, the actual mechanism of operation suggests natural ways in which it could be repurposed to perform more general in-context learning.

- **Argument 6** (*Continuity from small to large models*): In the previous 5 arguments, the case for induction heads explaining in-context learning is stronger for small models than for large ones. However, many behaviors and data related to both induction heads and in-context learning are smoothly continuous from small to large models, suggesting the simplest explanation is that mechanisms are the same. [p. 9]

For each argument, the paper has a similar table showing the strength of evidence provided by that claim as it applies to large/small models and some/most of context learning. The summary table above is the sum of the evidence from all six lines of reasoning. [p. 9]
