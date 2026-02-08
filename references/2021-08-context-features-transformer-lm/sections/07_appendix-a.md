# A Comparison of Experimental Paradigms [p. 11]

[p. 11] In Figure 5 the authors show the contrast between the experimental paradigm of Sections 3.1-3.2 and that of Section 3.3. Especially for the experiments involving parts of speech, there is a significant difference in both the quantitative and qualitative results across the two paradigms.

**Figure 5** (p. 11): "Comparison of model performance in the train+eval and eval-only settings. The units represent the percentage of the gap between the full information and no information models/contexts. That way, if a point falls on the dotted y = x line, then that ablation has the same relative effect in each paradigm. If a point falls above the dotted line, then that ablation leads to better relative performance in the train+eval paradigm, and if a point falls below the dotted line, then that ablation leads to better relative performance in the eval-only paradigm."

Figure 5 has two sub-figures:

**(a) Mid-range condition (first 256 tokens after ablation):**
- Scatter plot with x-axis "normalized accuracy (train+eval)" and y-axis "normalized accuracy (eval ablation)".
- Axes range from roughly -40 to 140 on both dimensions.
- A dotted y = x line runs diagonally.
- "full information" is near the origin (0, 0).
- Structural ablations (shuf. within trigrams, shuf. trigrams within sent., sent. shuf.) cluster in the 20-40 range on x-axis and 20-40 on y-axis, near the diagonal.
- POS-based ablations (N, N&VB, N&VB&ADJ, cont. words) cluster around x = 50-70 and y = 40-60, sitting below the diagonal -- indicating relatively better performance in the train+eval paradigm.
- "shuffle all" and "common" fall around x = 60-70 and y = 60-70.
- "replace w/ old" and "rare" are around x = 70-80 and y = 75-80.
- "no information" is near (100, 100).
- "func. words" is the most extreme outlier at roughly (120, 69), well above the diagonal -- indicating much worse performance under the eval-only paradigm relative to the train+eval paradigm.

**(b) Long-range condition (tokens 256-512 after ablation):**
- Same axes and layout as (a).
- Points are more tightly clustered near the diagonal.
- "full information" near (0, 0).
- POS-based ablations (N&VB, N, N&VB&ADJ, cont. words) are in the negative x range (around -20 to -30), below the diagonal at y around 40-60.
- Structural ablations cluster more tightly around x = 30-60, y = 60-80.
- "func. words" is again the biggest outlier at approximately (120, 100-110).
- "no information" is near (100, 100).
- "common" and "rare" cluster around x = 70-90, y = 80-90.
