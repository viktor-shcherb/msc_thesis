# Appendix D: Details on the COUNTERFACT Dataset [p. 24-25]

[p. 24-25] Construction pipeline:

1. Start from ParaRel tuples `(s, r, o_c)` and relation templates.
2. Build requested rewrite `{s, r, o_c, o*, p*}` where `o*` sampled from same relation's object pool.
3. Sample paraphrase prompts `P^P` for generalization tests.
4. Build neighborhood prompts `P^N` using Wikidata entities sharing relation `r` with subject to stress-test bleedover.
5. Sample generation prompts `P^G` and reference texts `RT` for implicit-consistency evaluation.

[p. 24] Reported motivation for neighborhood design: nearby entities are more susceptible to linear-edit bleedover than random entities.

[p. 24-25] Final record structure includes rewrite request, paraphrases, neighborhood prompts, generation prompts, and references.
