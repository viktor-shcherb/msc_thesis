# B Effect of longer context [p. 11-13]

[p. 11] In Section 3 the authors discussed that books that are fictional and continuous benefit more from the long-range context. They also annotated the validation set by the authorship (i.e., whether a book is written by single author or various authors). Out of 49 books, 11 are written by various authors, 10 of which are non-fictions. Due to this overlap, only the results of fic/non-fic are shown in the main text. [p. 11]

In this section, all targets are further broken down into the three types of tokens examined in Section 3, and the results displayed by book types. Perplexity of infrequent tokens (Figure 15), tokens inside subword clusters (Figure 16), and tokens whose last occurrence is more than 2K tokens away (Figure 17). In general, for the small set of tokens whose perplexity keeps decreasing as more context is added, the major source of improvements are from the continuous and fictional books. [p. 11]

**Table 2** (p. 11): "Ratio of overlapped target tokens among different categorizations. **infreq** are infrequent tokens, **in-subword** are tokens within a subword cluster (i.e., excluding the first word in a subword cluster), **distant** are tokens only appear in the distant context (more than 2K away). Row 1 column 3 the number 0.08 indicates around 8% of the infrequent tokens are those that can only be found in the distant context."

|           | infreq | in-subword | distant |
|-----------|--------|------------|---------|
| infreq    | 1.     | 0.09       | 0.08    |
| in-subword| 0.36   | 1.         | 0.1     |
| distant   | 0.07   | 0.02       | 1.      |

**Figure 15** (p. 12): "Perplexity of infrequent target tokens, broken down by genre (**left**), continuity (**middle**), and authorship (**right**). Perplexity of infrequent tokens in fictional, continuous and single-authored books decreases as the context length increases to around 5K. On the other hand, the rest types of books rely on more local context while predicting the infrequent tokens."
- Three panels: "genre" (left), "continuity" (middle), "author" (right).
- Left panel (genre): X-axis: prefix length (2000-8000); Y-axis: perplexity (~1000-3000). Two lines: nonfics (blue) and fics (green). Nonfics relatively flat around ~1000. Fics start at ~2500-3000 and decrease to ~1000-1500 by prefix length ~5K.
- Middle panel (continuity): X-axis: prefix length (2000-8000); Y-axis: perplexity (~1000-3000). Two lines: discontinuous (blue) and continuous (green). Discontinuous relatively flat around ~1000-1500. Continuous starts at ~2500-3000 and decreases to ~1000-1500 by prefix length ~5K.
- Right panel (author): X-axis: prefix length (2000-8000); Y-axis: perplexity (~1200-1600). Two lines: various_author (blue) and same_author (green). Various_author relatively flat or slightly increasing around ~1400-1500. Same_author starts at ~1500 and decreases to ~1200-1300 by prefix length ~5K.

**Figure 16** (p. 13): "Perplexity of target tokens inside subword clusters (i.e., excluding the first subword in each cluster), broken down by genre (**left**), continuity (**middle**), and authorship (**right**). Perplexity of these tokens in fictional and continuous books improves as the length increases up to around 4K, whereas nonfictional and discontinuous books are not taking any advantage of long-range context at all."
- Three panels: "genre" (left), "continuity" (middle), "author" (right).
- Left panel (genre): X-axis: prefix length (2000-8000); Y-axis: perplexity (~3.50-4.75). Two lines: nonfics (blue) and fics (green). Nonfics relatively flat around ~3.50-3.75. Fics start at ~4.50-4.75 and decrease to ~3.50-3.75 by prefix length ~4K.
- Middle panel (continuity): X-axis: prefix length (2000-8000); Y-axis: perplexity (~3.50-4.75). Two lines: discontinuous (blue) and continuous (green). Discontinuous relatively flat around ~3.50-3.75. Continuous starts at ~4.50-4.75 and decreases to ~3.50-3.75 by prefix length ~4K.
- Right panel (author): X-axis: prefix length (2000-8000); Y-axis: perplexity (~3.50-4.75). Two lines: various_author (blue) and same_author (green). Various_author starts at ~4.25 and decreases slightly. Same_author starts at ~4.50 and decreases to ~3.75 by prefix length ~4K.

**Figure 17** (p. 13): "Perplexity of target tokens that can only be found in the distant context, when evaluated with the Routing Transformer on subset of PG-19 validation set, broken down by genre (**left**), continuity (**middle**), and authorship (**right**). Fictional, continuous, and single-authored books continue to have improved perplexity for this type of tokens as the prefix length increases up to 8K. The single-authored books also contain discontinuous books which require less modeling of long-range context. The decreasing curve indicates the model might have acquired author specific token statistics from incorporating longer context."
- Three panels: "genre" (left), "continuity" (middle), "authorship" (right).
- Left panel (genre): X-axis: prefix length (2000-8000); Y-axis: perplexity (~165-180). Two lines: nonfics (blue) and fics (green). Nonfics relatively flat around ~165-167. Fics start at ~180 and decrease steadily to ~165.
- Middle panel (continuity): X-axis: prefix length (2000-8000); Y-axis: perplexity (~170-185). Two lines: discontinuous (blue) and continuous (green). Discontinuous starts at ~175 and decreases slightly. Continuous starts at ~180-185 and decreases to ~170.
- Right panel (authorship): X-axis: prefix length (2000-8000); Y-axis: perplexity (~165-190). Two lines: various_author (blue) and same_author (green). Various_author relatively flat around ~175-180. Same_author starts at ~185-190 and decreases to ~165.
