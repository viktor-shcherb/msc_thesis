# 6 Counting [p. 9–10]

We finally highlight another representational problem that arises specifically in counting problems. Our analysis points to a fundamental difficulty that emerges from the normalisation of the softmax. In particular, the normalisation of the softmax makes it hard for a model to take into account the **length** of a sequence. This is exacerbated by the fact that positional encodings are often normalised and thus relative, meaning that they also do not hold absolute positional information. Intuitively, counting is a problem that requires some notion of 'unboundedness' of the representations, whilst the normalisations used inside a Transformer work against this.

We start by showing that without causal masking and positional embeddings, a Transformer is immediately unable to count the number of tokens in a sequence, highlighting a pathological issue which stems directly from the softmax normalisation. We note that similar issues have been already pointed out [22]. We show the result in Proposition 6.1 and report the full statement in the Appendix (Proposition B.9).

## Proposition 6.1

A Transformer without positional encodings and a causal attention mechanism is immediately unable to count.

While causal mechanisms and positional encodings help to break such representational issues, they break the permutation invariance of the Transformer, meaning that the representations will be heavily miss-aligned with the task, something which has been shown to hinder performance [9]. As permutations grow factorially with sequence length, this makes it practically very challenging for a decoder-only Transformer to learn such a property simply from the data. This explains the extreme incapacity of counting highlighted in Section 3. Further, as a corollary of Theorem 4.2, we have that even if a model would be able to generalise perfectly, the problem of representational collapse points to an impossibility result in counting regardless. The result is summarised in Corollary 6.2, with the full statement in the Appendix (Corollary B.10).

## Corollary 6.2 (Informal)

Counting in certain situations becomes impossible due to representational collapse and finite floating point precision.

Corollary 6.2 shows how our main result on representational collapse points to practical issues when it comes to certain styles of prompts. When paired with low floating point arithmetic precision, representation collapse becomes problematic.
