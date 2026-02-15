# APPENDIX B: COMPLETE PROOF [p. 15–16]

This section provides a complete proof to show PINE can eliminate position bias [p. 15].

To simplify the notation and without loss of generality (w.l.o.g), the authors still use examples in Section 3.1 [p. 16].

**Theorem 1.** Given an input, if H_PINE is applied to every layer, attention head, and token to replace the conventional attention computation, then the model outputs are inter-document position-invariant representations [p. 16].

First, the embedding layer is not a function of input documents positions [p. 16]. Suppose that the ith layer's input hidden states are not a function of input documents positions, then within each layer [p. 16]:

- The attention hidden states are not a function of input documents positions (Lemma) [p. 16].
- The Layernorm, FFN outputs are not a function of input documents positions [p. 16].
- Therefore, the output hidden states of ith transformer layer, i.e., the input hidden states of i + 1th transformer layer, are not a function of input documents positions [p. 16].

Using mathematical induction, the authors know the final outputs are not a function of input documents positions [p. 16].

**Proof ends.** [p. 16]

Notes on the proof [p. 16]:

- PINE needs to be applied on each layer, attention heads, and tokens to satisfy the above proof [p. 16].

- The extra big O computation cost is purely come from the position re-assignment step: O(klogk) for sorting k documents [p. 16]. Since the model needs to repeat this step for every token, the extra computation cost is O(nklogk), where n is the number of tokens [p. 16].

- Although position re-assignment brings an extra computational cost, it is a must to complete the proof [p. 16]. Removing this step will make PINE unable to "eliminate" position bias [p. 16]. Similarly, a bidirectional attention mask is also a must to complete the proof [p. 16].

- PINE is not limited to specific position encoding algorithms [p. 16].
