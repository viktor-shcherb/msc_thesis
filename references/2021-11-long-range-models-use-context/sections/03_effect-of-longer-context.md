# 3 The effect of longer context [p. 4-6]

[p. 4] This section evaluates RT and LT checkpoints on the PG-19 validation set with varied prefix length. The authors discover that although these models are theoretically able to encode long sequences, increasing the prefix length beyond 2K tokens does not bring discernible improvements in aggregate. However, they do identify small subsets of tokens that benefit from long-range context. Additionally, they find that these models take advantage of long-range context to different degrees on different types of books (e.g., continuous fictional narratives vs. discontinuous magazine articles). [p. 4]

## Validation perplexity does not improve when the prefix length grows beyond 2K tokens [p. 4-5]

[p. 4] As shown in Figure 1, RT perplexity plateaus when evaluated with prefixes longer than 2K.^9 In contrast, relative to RT, the perplexity curve for the more primitive LT starts flattening earlier at around 1K tokens (note that its effective context size is only 5K). The authors conclude that while RT's clustering heads take better advantage of global context than LT, the long-range context beyond 2K tokens is not helping overall. Surprisingly, the perplexity gap between RT and LT is relatively consistent regardless of the prefix length, which indicates that much of RT's gains do not come from its increased ability to leverage long-range context but rather from better modeling of *local context*. [p. 4-5]

**Footnote 9:** As a point of comparison, the perplexity of the much smaller LSTM language models evaluated by Khandelwal et al. (2018) plateaus after 200 words. Additionally, Press et al. (2020) discover that the perplexity flattens after 1K for a smaller standard Transformer LM. [p. 4]

**Figure 1** (p. 4): "The perplexity of all target tokens plateaus after 2K prefix tokens for both Routing Transformer (**RT**) and Local Transformer (**LT**), showing the negligible overall impact of the long-range context."
- X-axis: prefix length (tokens), ranging from ~1000 to 8000.
- Y-axis: perplexity, ranging from ~35 to ~40.
- RT curve (blue): starts at ~40 at prefix length ~1000, drops to ~35.2 by ~2000, then plateaus.
- LT curve (green): starts at ~40 at prefix length ~1000, drops to ~38 by ~2000, then plateaus.
- Both curves show negligible improvement beyond 2K prefix tokens.

## Infrequent tokens can benefit from increased prefix length [p. 4-5]

[p. 4-5] While the overall perplexity does not improve with increasing prefix length, different behavior is observed when filtering the target tokens by frequency, as shown in Figure 2. *Frequent* tokens are defined as the top 10% more frequently-occurring tokens in the subword vocabulary of PG-19 while the rest of tokens are classified as *infrequent*.^10 While adding long-range context does not improve either model's predictions of frequent tokens, the RT's perplexity of infrequent tokens decreases from ~1200 with a prefix length of 2K to 1180 with prefix length of 5K. However, infrequent token perplexity increases back to 1200 as the input is further extended, suggesting that the additional context perhaps confounds the model. Meanwhile, the LT is significantly worse than RT on infrequent token prediction, and its perplexity increases as the prefix length is increased.^11 [p. 5]

**Footnote 10:** Around 20K tokens in the target token set are classified as infrequent, which amounts to 9% of all target tokens. [p. 5]

**Footnote 11:** This is likely an artifact due to the elimination of routing attention heads from the RT checkpoint, since the LT trained from scratch does not exhibit this behavior. More details are included in Appendix F. [p. 5]

**Figure 2** (p. 5): "RT perplexity of infrequent tokens continues to decrease until prefix is 5K."
- Two panels: "Frequent tokens" (left) and "Infrequent tokens" (right).
- Left panel (Frequent tokens): X-axis: prefix length (2500-7500); Y-axis: perplexity (~25-28). RT (blue) flat at ~25.5; LT (green) flat at ~27.
- Right panel (Infrequent tokens): X-axis: prefix length (2500-7500); Y-axis: perplexity (~1200-2400). RT (blue) decreases from ~1200 to ~1180 at 5K, then increases back. LT (green) starts around ~2000 and increases with prefix length.

## Tokens inside a subword cluster benefit from longer contexts [p. 5-6]

[p. 5-6] One issue with the frequency-based analysis is that frequency categorization was computed at a subword level and may not exactly correspond to word frequency, especially for infrequent words (e.g., entities) that are split into multiple subwords. A follow-up experiment isolates all words that are split into multiple subwords, examining perplexity of these tokens as a function of their position in the subword cluster. For example, the word "Trocadero" is separated into three subword tokens "Tro", "cade", and "ro". The authors specifically distinguish between the *first* subword in the cluster ("Tro") from the *rest* of the subwords ("cade" and "ro") in the plots shown in Figure 3. The perplexities are computed over 4.1K *first* and 5.1K *rest* subword tokens. [p. 5-6]

The *first* subword category exhibits the same curve shape as those for infrequent tokens for both models, although the magnitude of the perplexities is far higher. The rest of the subwords are far easier for both models to predict, but the RT perplexity curve shows some positive impact from the long-range context until a prefix size of 5K tokens. [p. 6]

**Figure 3** (p. 5): "RT perplexity of tokens inside subword clusters continues to decrease until a prefix length of 5K."
- Two panels: "First subword token" (left) and "Rest of subword tokens" (right).
- Left panel: X-axis: prefix length (2500-7500); Y-axis: perplexity (~7000-22000). RT (blue) decreases from ~20000 to ~8000 by 5K, then levels off. LT (green) starts ~9000 and increases.
- Right panel: X-axis: prefix length (2500-7500); Y-axis: perplexity (~3.5-5.5). RT (blue) decreases from ~4.5 to ~4.0 by 5K. LT (green) relatively flat around ~4.5-5.0.

## Routing Transformers are able to copy tokens that occur in the long-range context [p. 5-6]

[p. 5-6] Target subword tokens that can be copied from somewhere in the prefix form another interesting group to analyze.^12 While this is commonplace for frequent words (e.g., determiners, pronouns), it also occurs for entities and rare words (e.g., character names in a novel); sometimes, a word can occur several thousand tokens after its last occurrence. The authors focus on the latter category of tokens, specifically using a prefix length of 2K tokens as a cutoff to distinguish local and long-range context. Perplexities are computed over 22K tokens which occur last time more than 2K tokens away, and 36K tokens that never appear in the prefix. [p. 5-6]

In particular, Figure 4 shows the perplexity of tokens that cannot be found in the previous 2K tokens, but occur somewhere in the long-range context (2K to 8K tokens away). While the LT curve for such tokens plateaus after 2K tokens, indicating that LT cannot take advantage of repeated words in the distant context, the RT curve steadily decreases until 8K tokens. The right plot, which shows the subset of target tokens which do not occur anywhere in the short or long-term context, decreases until about 5K tokens and then plateaus. Overall, these results show that long-range context is helpful for tokens that appear even several thousands tokens away. [p. 6]

**Footnote 12:** There is some overlap between the token categories analyzed so far. The authors verify in the Appendix C Table 2 that the overlap between these categories is not significant enough to confound the results. [p. 5]

**Figure 4** (p. 5): "RT perplexity of target tokens whose last appearance is more than 2K tokens away in the prefix keeps decreasing."
- Two panels: "Occurs >2K tokens away" (left) and "Not in prefix" (right).
- Left panel: X-axis: prefix length (2500-7500); Y-axis: perplexity (~170-200). RT (blue) steadily decreases from ~200 to ~170 across the range. LT (green) relatively flat around ~190.
- Right panel: X-axis: prefix length (2500-7500); Y-axis: perplexity (~800-1000). RT (blue) decreases from ~1000 to ~800 by ~5K, then plateaus. LT (green) increases from ~900 upward.

## Following patterns in the long-range context [p. 6]

[p. 6] Besides the token categories examined above, some qualitative examples are examined that are too infrequent to analyze at scale. Interestingly, some simple patterns (slightly more complex than copying) that the RT model picks up on are observed. Specifically, it learns to increment chapter numbers even if the previous chapter title appears more than 2K tokens away: for example, when predicting "Chapter V" in the validation book *Keith of the Border*, modifying the previous chapter title "Chapter IV", which occurs 2300 tokens away, to "Chapter V" causes the loss of the predicted token "V" to increase by over 10. [p. 6]

## The impact of book type on the benefits of long-range context [p. 6]

[p. 6] PG-19 contains a diverse array of topics, genres, and formats, not all of which equally benefit from long-range context modeling. While continuous narratives (e.g., novels) build up many high-level discourse structures over a long sequence of tokens, discontinuous text like magazines, textbooks, or short story collections may require primarily local modeling. To better understand the effect of the type of book on long-range LM perplexity, every book in PG-19's validation set is annotated as either *fiction* or *non-fiction* and *continuous*^13 or *discontinuous*.^14 Out of 49 books annotated, 30 are non-fiction,^15 31 are discontinuous, and 25 books are both non-fiction and discontinuous. [p. 6]

**Footnote 13:** Books with related but distinct sections (such as textbooks) are considered discontinuous in the annotation. [p. 6]

**Footnote 14:** The authors also annotate whether the work has been written by the same author or various authors, which is presented in the Appendix. [p. 6]

**Footnote 15:** Some magazines contain short stories or poems interspersed with news articles and essays; these are counted as non-fiction in the analysis. [p. 6]

The RT model takes better advantage of long-range context for fictional and continuous books, as the perplexity for these books plateaus at around 5K tokens. Figure 6 shows fictional and continuous books exploit better the long-range context while predicting tokens within subword clusters. Overall, the improvement stems largely from continuous and fictional books; more details are included in Appendix B. [p. 6]

**Figure 5** (p. 6): "RT takes better advantage of context beyond 2K tokens for fictional and continuous books than non-fictional and discontinuous books, respectively."
- Two panels: "fic. & non-fic." (left) and "cont. & discont." (right).
- Left panel: X-axis: prefix length (2500-7500); Y-axis: perplexity (~34-38). Fiction (red) decreases from ~37 to ~34 as prefix grows. Non-fiction (blue) relatively flat around ~36-37.
- Right panel: X-axis: prefix length (2500-7500); Y-axis: perplexity (~35-37). Continuous (red) decreases from ~37 to ~35. Discontinuous (blue) relatively flat around ~36-37.

**Figure 6** (p. 6): "The majority of improvements on tokens inside subword clusters (i.e., excluding the first token in subword clusters) from prefixes longer than 2K tokens comes from fictional and continuous books."
- Two panels: "Rest of subword tokens" for fic. & non-fic. (left) and cont. & discont. (right).
- Left panel: X-axis: prefix length (2500-7500); Y-axis: perplexity (~1.0-1.2). Fiction (red) decreases. Non-fiction (blue) relatively flat.
- Right panel: X-axis: prefix length (2500-7500); Y-axis: perplexity (~1.0-1.2). Continuous (red) decreases. Discontinuous (blue) relatively flat.
