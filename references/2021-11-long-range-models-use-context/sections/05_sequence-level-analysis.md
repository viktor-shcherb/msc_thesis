# 5 Sequence-level analysis [p. 8–9]

[p. 8] All previous experiments focused on *token-level perplexity*, which is the standard way in which LMs are evaluated. However, the prefixes in these evaluations consist solely of ground-truth text, mirroring the "teacher-forcing" setup that LMs are trained with. When these models are deployed practically to generate text, they have to rely on their previous predictions instead of ground-truth text, and several prior works have noted different behavior in this setting (Wang and Sennrich, 2020; Holtzman et al., 2020; Welleck et al., 2020). This section shifts from token-level tasks to analyzing RT and LT performance on *sequence-level* tasks. In particular, it examines how well the models can memorize an exact sequence in the distant context, as opposed to a single token as done previously. It also examines the models' ability to identify which of six 128-token suffixes follows a given prefix, which examines their behavior outside the standard teacher-forced setting. [p. 8]

## Sequence-level copying [p. 8–9]

[p. 8–9] As a sequence-level analogue to the token-copying analysis in the previous section, the authors examine both RT's and LT's ability to memorize a sequence that occurs in the distant context. To test this ability, they copy the target sequence and paste it into different positions of the prefix. The left plot in Figure 13 shows that both models give a very low perplexity to the target sequence if its duplicate appears within the previous 512 tokens. However, > "both models lose their ability to take advantage of the copied sequence if it occurs more than 2K tokens away" [p. 8]. This confirms the previous discovery that sequence order is in general not encoded in the long-range context. [p. 8–9]

## Suffix identification [p. 9]

[p. 9] To move beyond token-level experiments, the authors adopt a similar setting as the multiple choice task in SWAG (Zellers et al., 2018). Specifically, a prefix is paired with the ground-truth next 128 tokens (or *suffix*) as well as five randomly sampled sequences of length 128 that come from the same book and do not occur in the prefix or gold suffix. The prefix is constrained to end at a full stop and each candidate suffix to start from a new sentence so that the difference in perplexity is not due to ungrammaticality. An example is shown in Table 1. 7K examples are constructed, and the accuracy of both models at correctly choosing the correct suffix is computed. The model makes a correct prediction when the gold suffix has lower perplexity than all other suffixes. As shown in the right plot of Figure 13, increasing prefix length beyond 2K does not improve suffix identification accuracy. Surprisingly, the LT and RT model have almost identical (and poor) performance on this task.^17 While RT is a significantly better LM in terms of token-level perplexity, it does not appear to be superior in terms of using long-range context to improve sequence prediction. Overall, both models often predict obviously wrong negative suffixes: the full version of Table 1 together with RT's perplexity score for each suffix is included in Appendix E. [p. 9]

**Footnote 17:** While evaluating on the newly released LT checkpoint, the performance of LT is slightly worse, but the trend is similar. Adding context beyond 2K tokens does not keep improving the suffix identification accuracy. The authors direct the reader to Appendix F for more details. [p. 9]

> "Combined with our previous token-level analysis, we conclude that the distant context helps a subset of tokens in superficial ways; however, distant context is currently not helpful for sequence-level prediction tasks." [p. 9]

**Figure 13** (p. 8): **Left:** "Both models assign low perplexity if a duplicate sequence appears within previous 512 tokens." **Right:** "Both models have almost identical performance on our suffix identification task. Adding context beyond 2K tokens does not improve performance of either sequence-level prediction task."
- Two panels: "Sequence copying" (left) and "Suffix identification" (right).
- Left panel: X-axis: distance of duplicate from target (0-8000); Y-axis: perplexity (~10-40). RT (blue) and LT (green). Both models achieve very low perplexity (~10-15) when duplicate is within ~512 tokens. Perplexity rises sharply to ~35-40 when duplicate is >2K tokens away, then remains flat.
- Right panel: X-axis: prefix length (0-8000); Y-axis: accuracy (~0.30-0.45). RT (blue) and LT (green). Both lines are nearly identical, rising from ~0.30 to ~0.40 by ~2K prefix length, then plateauing. No improvement beyond 2K.

**Table 1** (p. 8): "An example of suffix identification task, the full version of this example is included in Appendix E."

| Role | Text |
|------|------|
| Prefix | ... If the doctor's prophecy is correct... (~700 tokens) ... "How far is it to his place?""Oh, a mile at least.We can have a cab.""A mile? |
| Gold suffix: | Then we shall see if there is any truth in what that swab of a doctor said ... |
| Negative 1: | If I can see Mr.Elberry to-day we may let you have a cheque ... |
| Negative 2: | It was not until he had signed and sent it off that the full significance of all... |
| Negative 3: | He hurried in, fearing that she might have taken some turn for the worse... |
| Negative 4: | look!!!"Her voice had fallen suddenly to a quivering whisper and she was... |
| Negative 5: | Again the Admiral burst out cheering."There remains, therefore... |
