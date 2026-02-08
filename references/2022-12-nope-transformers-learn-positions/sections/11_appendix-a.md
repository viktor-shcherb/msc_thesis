# A NoPos Performance Across Different Segments of the Input [p. 8]

[p. 8] To shed more light on the findings shown in Section 4, the authors explore whether there are parts of the sequence that the NoPos model better predicts compared to other positional methods (e.g., is the NoPos model better at the beginning or the end of the sequence). They compute the model's perplexity in different parts of the sequences. Specifically, they split each input sequence into eight consecutive segments and compute the perplexity for each segment separately.

They evaluate the NoPos and Learned 1.3B parameter models trained on the Pile, with input sequence length of 1024, and use the standard validation set.

Figure 4 shows the results of this experiment. The NoPos model performs similarly or slightly worse than the baseline model on all input parts.

**Figure 4** (p. 8): "NoPos model shows similar performances on each part of the sequence, comparing to the baseline *Learned* absolute position encoding."

Line plot with X-axis: Sequence Split (1:64, 65:128, 129:192, 193:256, 257:320, 321:384, 385:448, 449:512), Y-axis: Loss (~4.2 to ~4.9). Two lines are shown: NoPos (blue circle) and Sinusoidal (orange plus) per the figure legend (note: the caption text refers to the baseline as "Learned" but the legend labels the second line "Sinusoidal"). Both lines start high (~4.85–4.9) at the 1:64 segment, drop sharply to ~4.55 at 65:128, then gradually decrease across subsequent segments, reaching ~4.25–4.3 at 449:512. NoPos is consistently slightly above or overlapping with the Sinusoidal line. The overall trend shows both models perform better (lower loss) on later parts of the sequence, and the gap between NoPos and the baseline is small and approximately constant across all segments.
