# Data Collection [p. 58-60]

[p. 58] The authors measure several properties of the model's overall behavior and of each constituent attention head. With the exception of the attention head ablations (which are the most computationally-intensive, and so were run only on the small models), they measure these properties on all snapshots of all models across training (that is, 200 snapshots each for the twelve small models, and 14 or 15 snapshots each for the six full-scale models). By measuring them on each snapshot, they can see how each property evolves over the course of training, rather than simply measuring the final model. [p. 58]

The properties collected are: [p. 58]

1. **Per-token losses** with **unaltered models**
2. **Per-token losses** with **ablations** of individual attention heads
3. **Empirical head measurements** with **head activation evaluators**: using heuristics to score attention heads based on their observed activations, as another way of estimating "copying", "prefix matching" and "previous token" attention.
4. **Mathematical head measurements** with the **trace of QK eigenvalues** for the previous-token QK-circuit term: measuring how much the WQWK weight matrix reads in a subspace affected by heads that attend to the previous token.

## (1) Per-token losses (unaltered models) [p. 58]

[p. 58] The most straightforward property measured is per-token losses from each model snapshot. The model snapshot is run on a set of 10,000 randomly-selected examples from the dataset, each of which is 512 tokens in length, and individual token losses are saved for every token. The set is held the same between all snapshots and between all models in all three families. [p. 58]

When analyzing the per-token loss data, it is summarized in two different ways: [p. 58]

- **Random token per example.** For each example, the loss for just one random token out of the 512 tokens is extracted and the rest discarded, giving a length-10,000 vector for each model snapshot. (The random index used for each example is consistent between each model.) [p. 58]

- **Context index average.** The per-token losses are averaged by context index (i.e. by position), giving a length-512 vector for each model snapshot. The *i*context-th entry in the vector is an average over the 10,000 tokens drawn from position *i*context in each example. [p. 58]

## (2) Per-token losses (attention head ablations) [p. 58-59]

[p. 58] One way to study individual attention heads is to measure the difference between the complete model's overall behavior and the overall behavior of a model that is exactly the same except for missing that head. This is done by successively ablating (i.e. zeroing-out) each attention head's contribution to the residual stream. The approach of removing a head's contribution can be thought of as loosely similar to a genetic "knockout" experiment in biology, where observing the effect of removing a specific gene can provide information about the gene's function. [p. 58]

Ablations can be done in two different ways: a "full" ablation, and a "pattern-preserving" ablation. (The model analysis table shows only pattern-preserving ablations; the other method is explained for comparison.) The full ablation would remove *all* of a head's contributions to model behavior, whereas the pattern-preserving ablation removes the ablated head's contribution to all later heads' *output* vectors, but preserves the ablated head's contribution to all later heads' attention *patterns*.^29 [p. 59]

### Full ablation [p. 59]

- *Method:* Run the model, replacing the ablated attention head's result vector with a zero vector. [p. 59]
- *Outcome:* All downstream computations are impacted (including all Q, K, and V calculations, and attention patterns). [p. 59]

### Pattern-preserving ablation (shown in Model Analysis Table) [p. 59]

- *Method:* [p. 59]
  - Step 1: Run the model for the first time, saving all attention patterns and discarding the output logits.
  - Step 2: Run model a second time. Replace the ablated attention head's result vector with a zero vector, and force all attention patterns to be the version recorded in the first run.
- *Outcome:* Only downstream V calculations are affected by the ablation, not Q and K calculations. The contribution a head makes to later layers' attention patterns is preserved.^30 [p. 59]

[p. 59] This is by far the most computationally-intensive measurement performed, although fortunately it consists of many small single-GPU jobs and so could often be run in "spare" capacity. [p. 59]

As a quick note of comparison, the previous work in Transformer Circuits also contained ablation experiments. Although there are similarities (most notably the decision to freeze patterns), the specific ablations described here are ***individual attention head*** ablations where only one attention head is modified at a time, whereas the ablations described in the prior work are ***nth-order term*** ablations in which all attention heads are manipulated at once and the process is repeated iteratively *n* times. [p. 59]

## (3) Head activation evaluators [p. 60]

[p. 60] Three heuristic measurements of attention heads are constructed, to score how strongly a head exhibits specific properties of interest. These are empirical measurements, based on observed activations on example data. [p. 60]

Heads are evaluated on the following properties: [p. 60]

- **Copying.** Does the head's direct effect on the residual stream increase the logits of the same token as the one being attended to? [p. 60]
- **Prefix matching.** On repeated sequences of random tokens, does the head attend to earlier tokens that are followed by a token that matches the present token? [p. 60]
- **Previous token attention.** Does the head attend to the token that immediately precedes the present token? [p. 60]

(Note that "copying" is a property that depends on a head's OV circuit, whereas "prefix matching" and "previous token attention" are properties that depend on a head's QK circuit.) [p. 60]

[p. 60] The authors are interested in these properties in particular -- copying, prefix matching, and previous token attention -- because they are relevant to induction heads' function of predicting repeated sequences of random tokens. Specifically, (1) a head with both a "copying" OV circuit and a "prefix matching" QK circuit is thereby an induction head by their definition, because it attends to previous instances of the present token and increases the logit of the token that followed; and (2) a "previous token" head can be used as an algorithmic component of a future induction head in a later layer (as explained in more detail in Argument 5). [p. 60]

In more detail, each head evaluator is implemented as follows, and each score is averaged over 10 examples. [p. 60]

- **Copying:** Generate a sequence of 25 random tokens, excluding the most common and the least common tokens. Compute this head's contribution to the residual stream, then convert that using the unembeddings (i.e. along the "direct path") to impacts on each logit. Logits are transformed by subtracting the mean of the logits and passing through a ReLU, allowing the evaluator to focus on where logits are raised. Compute the ratio of the amount it raises the logits of the token being attended to, to that of all tokens in this sample. This value ranges from 0 (only raises other tokens) to 0.5 (only raises the present token), so it is scaled into the range of -1 to 1. [p. 60]

- **Prefix matching:** Generate a sequence of 25 random tokens, excluding the most common and the least common tokens. Repeat this sequence 4 times and prepend a "start of sequence" token.^31 Compute the attention pattern. The prefix matching score is the average of all attention pattern entries attending from a given token back to the tokens that preceded the same token in earlier repeats. [p. 60]

- **Previous token:** Draw an example from the training distribution. Compute the attention pattern. The previous token score is the average of the entries of all the attention pattern entries attending from token *i* to token *i*-1. [p. 60]

[p. 60] In the Appendix the authors validate the connection between these empirical measurements and the mathematical properties of attention head weight matrices explored in Transformer Circuits, and show a joint distribution of scores for copying and prefix matching, for heads in the small and large models. [p. 60]

## (4) Trace of QK eigenvalues (for previous-token QK-circuit term) [p. 60-61]

[p. 60] In addition to the heuristic measurements described above, another measure of **prefix matching** is constructed that draws on concepts from A Mathematical Framework for Transformer Circuits. In short, the measure captures how overall large and positive the eigenvalues are of the *W* matrix found in the term of the QK circuit that corresponds specifically to "pure K-composition" with heads that attend to the previous token. Positive eigenvalues of *W* indicate "same-matching": preferring that this component of the query and key vectors be the same. A "same-matching" *W* matrix associated with a "previous token" term in the QK circuit is a simple way to implement basic prefix matching behavior. [p. 60-61]

[p. 61] The "QK circuit" is a term coined in the previous work to refer specifically to the entire transformation $C_{QK}^h$ which is applied to the one-hot token vectors *t* to compute the attention pattern $A^h$ for a specific head: $A^h = \text{softmax}^* (t^T \cdot C_{QK}^h t)$. The full computation of $C_{QK}^h$ for a given head can be decomposed into many terms, each corresponding to one of the many paths through the model that needs to be computed in order to map tokens to their attention scores for that head. The section Path Expansion of Attention Scores QK Circuit in the earlier work shows all the terms of a full expansion for a two-layer model; models with more layers have QK circuits with even more terms. [p. 61]

[p. 61] For this measure, the scope of the calculation is narrowed to the simplest possible term of the QK circuit that could contribute to the "prefix-matching" behavior of an induction head: namely, only pure K-composition terms (in which the query-side term is just the direct path from the embeddings), and furthermore only the subset of those that correspond specifically to K-composing with an earlier head that consistently attends to the immediately previous token. [p. 61]

In order to compute this measure for a given head, the following steps are taken: [p. 61]

1. For all attention heads in earlier layers, measure how "previous-token-like" the head is, as the average of the attention pattern along the previous-token off-diagonal, over an example text. [p. 61]

2. Compute the *W* matrix found in each individual $Id \otimes A^{h_e} \otimes W_E^T W_{QK}^{h_l} W_{OV}^{h_e} W_E$ term, for each head in earlier layers. [p. 61]

3. Create a combined *W* matrix by weighting the matrices in step 2 by the measurement in step 1 of how "previous-token-like" each previous head is. [p. 61]

4. Measure the trace (i.e. the sum of the eigenvalues) of this combined weighted *W* matrix. [p. 61]

Because this measure relies on K-composition with heads in previous layers, it is only defined for models more than one layer deep, and only for attention heads in the second layer and beyond. [p. 61]

The authors show in the Appendix that this measure correlates well with the heuristic prefix matching evaluator on the small models. [p. 61]
