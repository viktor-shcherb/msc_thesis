# B Additional Figures [p. 12-14]

This section contains all figures complementary to those presented in the main text. Some figures, such as Figures 1b, 1d etc. present results for only one of the two datasets, and the complementary results for the other dataset are presented here. The analysis and conclusions remain unchanged. All results are averaged from three models trained with different random seeds. Error bars on curves represent the standard deviation and those on bar charts represent 95% confidence intervals. [p. 12]

## Figure 8 [p. 12]

**Figure 8** (p. 12): "Complementary to Figure 2b. Perturb global order, i.e. all tokens in the context before a given point, in PTB. Effects of shuffling and reversing the order of words in 300 tokens of context, relative to an unperturbed baseline. Changing the global order of words within the context does not affect loss beyond 50 tokens."

- X-axis: Distance of perturbation from target (number of tokens), values: 1, 5, 10, 15, 20, 30, 50, 100, 200
- Y-axis: Increase in Loss, range 0.0-3.0
- Three curves: Shuffle entire context, Reverse entire context, Replace context with rand sequence
- All three curves show sharp decrease from distance 1 to ~50 tokens
- Shuffle and Reverse curves reach near zero by 50 tokens
- Replace curve remains higher at all distances (showing that word identity still matters even when order does not)
- Supports the same conclusion as Figure 2b but on PTB instead of Wiki

## Figure 9 [p. 12]

**Figure 9** (p. 12): "Complementary to Figure 3. Effect of dropping content and function words from 300 tokens of context relative to an unperturbed baseline, on Wiki. Dropping both content and function words 5 tokens away from the target results in a nontrivial increase in loss, whereas beyond 20 tokens, content words are far more relevant."

- X-axis: Distance of perturbation from target (number of tokens), values: 5, 20, 100
- Y-axis: Increase in Loss, range 0.0-0.6
- Four bars at each distance: Drop all content words (54.4%), Drop all function words (45.6%), Random drop 54.4% tokens of 300, Random drop 45.6% tokens of 300
- At distance 5: content word drop causes ~0.55 increase; function word drop causes ~0.35 increase; both random controls are lower
- At distance 20: content word drop still higher (~0.20) than function words (~0.10)
- At distance 100: only content words remain relevant (~0.08); function words near zero
- Supports the same conclusion as Figure 3 but on Wiki instead of PTB

## Figure 10 [p. 13]

**Figure 10** (p. 13): "Complementary to Figures 1b and 1d, respectively. Effects of varying the number of tokens provided in the context, as compared to the same model provided with infinite context. Increase in loss represents an absolute increase in NLL over the entire corpus, due to restricted context. **(a)** Changing model hyperparameters does not change the context usage trend, but does change model performance. We report perplexities to highlight the consistent trend. **(b)** Content words need more context than function words."

### Figure 10a: Changing model hyperparameters for Wiki [p. 13]

- X-axis: Context Size (number of tokens), log scale from 10 to 1000
- Y-axis: Perplexity, range roughly 65-120
- Multiple curves: Default Model Wiki, LSTM Hidden 575 (vs. 1150), 2 layers (vs. 3), Word Emb 200 (vs. 400), No LSTM layer dropout (vs. 0.2), No recurrent dropout (vs. 0.5), BPTT 100 (vs. 70), BPTT 10 (vs. 70)
- All curves converge around 200-500 tokens regardless of hyperparameter setting
- Complementary to Figure 1b which showed this for PTB

### Figure 10b: Different parts-of-speech for PTB [p. 13]

- X-axis: Context Size (number of tokens), log scale from 5 to 1000
- Y-axis: Increase in Loss, range 0.0-0.8
- Five curves: NN (nouns), JJ (adjectives), VB (verbs), IN (prepositions), DT (determiners) -- all for PTB
- NN curve is highest and slowest to decay
- DT curve drops to near zero fastest
- Complementary to Figure 1d which showed this for Wiki

## Figure 11 [p. 13]

**Figure 11** (p. 13): "Complementary to Figure 4. Effects of perturbing the target word in the context compared to dropping long-range context altogether, on Wiki."

### Figure 11a: Dropping tokens [p. 13]

- X-axis: First occurrence of target in context (nearby, long-range, none (control set))
- Y-axis: Increase in Loss, range 0.00-0.20
- Two bar groups: Drop 250 most distant tokens, Drop only target
- For "nearby": Drop only target (~0.13) > Drop 250 most distant tokens (~0.05)
- For "long-range": Drop 250 most distant tokens (~0.22) > Drop only target (~0.04)
- For "none" (control set): Drop 250 most distant tokens (~0.11) > Drop only target (~0.10)

> **(a)** "Words that can only be copied from long-range context are more sensitive to dropping all the distant words than to dropping the target. For words that can be copied from nearby context, dropping only the target has a much larger effect on loss compared to dropping the long-range context." [p. 13]

### Figure 11b: Perturbing occurrences of target word in context [p. 13]

- X-axis: First occurrence of target in context (nearby, long-range)
- Y-axis: Increase in Loss, range 0.000-0.200
- Three bar groups: Drop only target, Replace target with <unk>, Replace with similar
- For "nearby": Replace with similar (~0.175) > Replace with <unk> (~0.150) > Drop only target (~0.13)
- For "long-range": all three perturbations have similar effects (~0.03-0.04)

> **(b)** "Replacing the target word with other tokens from vocabulary hurts more than dropping it from the context, for words that can be copied from nearby context, but has no effect on words that can only be copied from far away." [p. 13]

## Figure 12 [p. 14]

**Figure 12** (p. 14): "Failure of neural cache on Wiki. Lightly shaded regions show flat distribution."

Shows an example passage from Wiki where the neural cache fails. The passage describes a scene involving guerrillas and a crash site. The target word is "hours" (shown in bold). Lightly shaded regions indicate the cache distribution is flat/uncertain, meaning the cache cannot confidently point to any particular word to copy. This is the Wiki complement to Figure 6 (which showed the same failure mode on PTB). [p. 14]

## Figure 13 [p. 14]

**Figure 13** (p. 14): "Success of neural cache on Wiki. Brightly shaded region shows peaky distribution."

Shows an example passage from Wiki about a tropical storm near La Fortuna, Mexico. The target word is "Fortuna" (shown in bold). The brightly shaded region around the earlier occurrence of "Fortuna" shows a peaky cache distribution, indicating the cache is confidently pointing to the word it wants to copy. This is the Wiki complement to Figure 5 (which showed the same success mode on PTB). [p. 14]
