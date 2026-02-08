# 3 Keys Capture Input Patterns [p. 3-4]

[p. 3] The authors posit that the key vectors K in feed-forward layers act as pattern detectors over the input sequence, where each individual key vector k_i corresponds to a specific pattern over the input prefix x_1, ..., x_j. To test this claim, they analyze the keys of a trained language model's feed-forward layers by retrieving the training examples (prefixes of a sentence) most associated with a given key, and then asking humans to identify patterns within the retrieved examples.

For almost every key k_i in the sample, a small set of well-defined patterns, recognizable by humans, covers most of the examples associated with the key.

## 3.1 Experiment

[p. 3] **Model:** The language model of Baevski and Auli (2019), a 16-layer transformer language model trained on WikiText-103 (Merity et al., 2017). This model defines d = 1024 and d_m = 4096, and has a total of d_m * 16 = 65,536 potential keys to analyze. The authors randomly sample 10 keys per layer (160 in total).

**Retrieving trigger examples:** Given a key k_i^l that corresponds to the i-th hidden dimension of the l-th feed-forward layer, the memory coefficient ReLU(x_j^l . k_i^l) is computed for every prefix x_1, ..., x_j of every sentence from the WikiText-103's training set. For example, for the hypothetical sentence "I love dogs", three coefficients are computed, for the prefixes "I", "I love", and "I love dogs". Then, the *top-t trigger examples* are retrieved, that is, the t prefixes whose representation at layer l yielded the highest inner product with k_i^l.

Footnote 3 [p. 3]: Training examples are segmented into sentences to simplify the annotation task and later analyses.

**Pattern analysis:** Human experts (NLP graduate students) annotate the top-25 prefixes retrieved for each key, and are asked to (a) identify repetitive patterns that occur in at least 3 prefixes (which would strongly indicate a connection to the key, as this would unlikely happen if sentences were drawn at random), (b) describe each recognized pattern, and (c) classify each recognized pattern as "shallow" (e.g. recurring n-gram) or "semantic" (recurring topic). Each key and its corresponding top-25 prefixes were annotated by one expert. To assure that every pattern is grounded in at least 3 prefixes, the experts are instructed to specify, for each of the top-25 prefixes, which pattern(s) it contains. A prefix may be associated with multiple (shallow or semantic) patterns.

**Table 1** (p. 3): Examples of human-identified patterns that trigger different memory keys.

| Key | Pattern | Example trigger prefixes |
|---|---|---|
| k_{149}^1 | Ends with "substitutes" (shallow) | *At the meeting, Elton said that "for artistic reasons there could be no substitutes* / *In German service, they were used as substitutes* / *Two weeks later, he came off the substitutes* |
| k_{2546}^6 | Military, ends with "base"/"bases" (shallow + semantic) | *On 1 April the SRSG authorised the SADF to leave their bases* / *Aircraft from all four carriers attacked the Australian base* / *Bombers flying missions to Rabaul and other Japanese bases* |
| k_{2997}^{10} | a "part of" relation (semantic) | *In June 2012 she was named as one of the team that competed* / *He was also a part of the Indian delegation* / *Toy Story is also among the top ten in the BFI list of the 50 films you should* |
| k_{2989}^{13} | Ends with a time range (semantic) | *Worldwide, most tornadoes occur in the late afternoon, between 3 pm and 7* / *Weekend tolls are in effect from 7:00 pm Friday until* / *The building is open to the public seven days a week, from 11:00 am to* |
| k_{1935}^{16} | TV shows (semantic) | *Time shifting viewing added 57 percent to the episode's* / *The first season set that the episode was included in was as part of the* / *From the original NBC daytime version, archived* |

A fully-annotated example of the top-25 prefixes from a single memory key is shown in Appendix A.

## 3.2 Results

[p. 3-4] **Memories are associated with human-recognizable patterns.** Experts were able to identify at least one pattern for every key, with an average of 3.6 identified patterns per key. Furthermore, the vast majority of retrieved prefixes (65%-80%) were associated with at least one identified pattern (Figure 2). Thus, the top examples triggering each key share clear patterns that humans can recognize.

**Figure 2** (p. 3): "Breakdown of the labels experts assigned to trigger examples in each layer. Some examples were not associated with any pattern ('not-covered')."

The figure is a stacked bar chart with layers 1-16 on the x-axis and "% trigger examples" (0-100) on the y-axis. Bars are colored in four categories: shallow (blue/teal, with hatching), shallow + semantic (orange, with hatching), semantic (green), and not-covered (gray). Lower layers (1-9) are dominated by shallow patterns. Upper layers (10-16) show increasing proportions of semantic patterns. The "not-covered" proportion is roughly 20-35% across layers.

[p. 4] **Shallow layers detect shallow patterns.** Comparing the amount of prefixes associated with shallow patterns and semantic patterns (Figure 2), the lower layers (layers 1-9) are dominated by shallow patterns, often with prefixes that share the last word (e.g. k_{149}^1 in Table 1). In contrast, the upper layers (layers 10-16) are characterized by more semantic patterns, with prefixes from similar contexts but without clear surface-form similarities (e.g. k_{1935}^{16} in Table 1). This observation corroborates recent findings that lower (upper) layers in deep contextualized models encode shallow (semantic) features of the inputs (Peters et al., 2018; Jawahar et al., 2019; Liu et al., 2019).

**Mutation experiment:** [p. 4] To further test this hypothesis, 1600 random keys (100 keys per layer) are sampled and local modifications applied to the top-50 trigger examples of every key. Specifically, either the *first*, *last*, or a *random* token is removed from the input, and the effect on the memory coefficient is measured. Figure 3 shows that the model considers the end of an example as more salient than the beginning for predicting the next token. In upper layers, removing the last token has less impact, supporting the conclusion that upper-layer keys are less correlated with shallow patterns.

**Figure 3** (p. 4): "Relative change in memory coefficient caused by removing the first, the last, or a random token from the input."

The figure shows a line chart with layers 1-16 on the x-axis and "change in memory coefficient (%)" on the y-axis (range approximately -70 to -10). Three lines are plotted:
- **first** (blue squares): relatively flat around -10 to -15% across all layers
- **random** (green triangles): relatively flat around -15 to -20% across all layers
- **last** (orange circles): starts at approximately -65 to -70% in layer 1, and gradually increases (less negative) to approximately -20% by layer 16

This shows that removing the last token causes a dramatic drop in memory coefficient in lower layers but the effect diminishes in upper layers, where keys are more semantic.
