# F Local Transformer checkpoint results [p. 15-16]

[p. 15] In the main text, both the RT checkpoint and an LT model derived from the same RT checkpoint by replacing the clustering heads with local attention heads are analyzed. After the submission deadline and before the camera ready deadline, the author of the Routing Transformer released a new LT checkpoint, which has 24 layers in total.^18 To make sure the behavior of the former LT is the same with an LT trained from scratch, all analysis was conducted again on this new checkpoint. Overall, the new LT checkpoint performs slightly better on token-level tasks but is inferior to the previous LT checkpoint on suffix identification, a sequence-level task. Since the trends are the same, no conclusion needs to be changed. [p. 15]

**Footnote 18:** Both the RT model and the *former* LT model have 22 layers. [p. 15]

## The Effect of Longer Context [p. 15]

[p. 15] In Figure 18 are the perplexities in aggregate over all target tokens of both the RT and the new LT checkpoints. The target tokens are the same ones used in the main text. The new LT has better perplexity than the one presented in the main text (36.5 vs. 40 as the prefix length extends to 8K). [p. 15]

## Perturbation of long-range context [p. 15]

[p. 15] Similar to the former LT (Figure 20), the newly released LT checkpoint (Figure 19) is not sensitive at all to the perturbation further than local 2K tokens. Both models are impacted by local random replacement more than shuffling, however, the new LT checkpoint has overall better perplexity than the RT-derived LT. [p. 15]

## Sequence-level tasks [p. 15-16]

[p. 15-16] Figure 22 shows the performance of both RT and the released LT checkpoint on sequence-level tasks. Compared to the results in the main text, the new LT checkpoint performs better at sequence-copying task, however, the trend remains the same -- the order of tokens beyond 2K tokens is not properly encoded. On the other hand, the new LT checkpoint is slightly worse in suffix identification while the former RT-derived LT has almost identical performance as the RT. This implies even though the clustering heads are removed from the previous LT, useful information is preserved by the local attention heads. [p. 15-16]

Overall, the released LT checkpoint has better token-level performance but performs worse on suffix identification. Each plot shares the same trend with its corresponding one in the main text, thus no conclusion needs to be modified. [p. 16]

**Figure 22** (p. 15): **Left:** "Both models assign low perplexity if a duplicate sequence appears within previous 512 tokens." **Right:** "Adding context beyond 2K tokens does not improve performance of suffix identification. Moreover, the recently released LT performs worse than the one derived from the RT checkpoint."
- Two panels: "Sequence copying" (left) and "Suffix identification" (right).
- Left panel: X-axis: distance of duplicate from target (0-8000); Y-axis: perplexity (~15-35). Two lines: RT (blue) and LT (green). Both models achieve low perplexity (~15) when duplicate is within ~512 tokens. Perplexity rises sharply to ~30-35 when duplicate is >2K tokens away, then remains flat.
- Right panel: X-axis: prefix length (0-8000); Y-axis: accuracy (~0.30-0.45). Two lines: RT (blue) and LT (green). RT achieves ~0.40 accuracy. LT is slightly worse at ~0.35 accuracy. Both plateau after ~2K prefix length.
