# C Full Results [p. 13-15]

[p. 13-15] This appendix provides the full breakdown of results across all tasks, padding types, key paragraph positions, and models.

**Figure 13** (p. 13): **"Full results for the Ruletaker dataset."**
- Layout: 4 rows x 2 columns of subplots. Rows correspond to key paragraph positions: First, Middle, Last, Random. Columns correspond to padding type: Resampling padding (left) and Books Corpus padding (right).
- X-axis: Input Length (# tokens), range 0-3000.
- Y-axis: Accuracy, range 0.4-1.0.
- Lines for GPT3.5 (blue), GPT4 (green), Gemini Pro (yellow), Mistral Medium (purple), Mixtral 8x7B (pink/magenta). Dashed lines = CoT, solid lines = Normal prompting.
- General trends: All models show accuracy decline as input length increases in most conditions. GPT4 with CoT maintains the highest accuracy across nearly all conditions. The decline is steeper with Books Corpus padding than with Resampling padding for most models. "First" position generally shows the least degradation, while "Random" position shows the most. Mixtral 8x7B and GPT3.5 show the steepest declines overall.

**Figure 14** (p. 14): **"Full results for the MonoRel dataset."**
- Layout: 4 rows x 2 columns of subplots. Rows: First, Middle, Last, Random positions. Columns: Resampling padding (left), Books Corpus padding (right).
- X-axis: Input Length (# tokens), range 0-3000.
- Y-axis: Accuracy, range 0.4-1.0.
- Lines for GPT3.5, GPT4, Gemini Pro, Mistral Medium, Mixtral 8x7B. Dashed = CoT, solid = Normal.
- General trends: GPT4 maintains near-perfect accuracy in most conditions (both CoT and Normal). Other models degrade with length. With Books Corpus padding, declines are more pronounced. GPT3.5 and Gemini Pro show notable drops especially in the Random position. Mistral Medium maintains relatively stable performance on MonoRel compared to other tasks.

**Figure 15** (p. 14): **"Full results for the People In Rooms (PIR) dataset."**
- Layout: 4 rows x 2 columns of subplots. Rows: First, Middle, Last, Random positions. Columns: Resampling padding (left), Books Corpus padding (right).
- X-axis: Input Length (# tokens), range 0-3000.
- Y-axis: Accuracy, range 0.4-1.0.
- Lines for GPT3.5, GPT4, Gemini Pro, Mistral Medium, Mixtral 8x7B. Dashed = CoT, solid = Normal.
- General trends: PIR shows the most varied results across models and conditions. GPT4 (CoT) stays highest. Gemini Pro shows steep declines especially in the Middle and Random positions. Mixtral 8x7B drops sharply across all conditions. Resampling padding generally produces less degradation than Books Corpus padding. The "Last" position tends to yield better performance than other positions for most models.

**Figure 16** (p. 15): **"Differences in accuracy between different positions of key paragraphs in input."** Averaged over both types of irrelevant padding: similar (resampling from the data) and dissimilar (Books corpus) padding.
- Layout: 5 vertically stacked subplots, one per model: GPT3.5, GPT4, Gemini Pro, Mixtral 8x7B, Mistral Medium.
- X-axis: Input length (# tokens), range approximately 250-3000.
- Y-axis: Accuracy.
- Lines for First (green), Middle (black), Last (yellow/orange), Random (purple).
- GPT3.5: Y-axis range ~0.55-0.75. All positions decline. "Last" tends to be slightly higher.
- GPT4: Y-axis range ~0.8-1.0. Relatively flat, "Last" highest, minimal position effect.
- Gemini Pro: Y-axis range ~0.55-0.8. Clear separation between positions. "Last" highest, "Random" lowest.
- Mixtral 8x7B: Y-axis range ~0.55-0.85. Steep decline across all positions. Positions converge at longer lengths.
- Mistral Medium: Y-axis range ~0.6-0.85. Moderate decline. "Last" position maintains slight advantage.

**Figure 17** (p. 15): **"Biases in answer generation and non-answers."** Frequency of responses with True, False, or neither, per model.
- Layout: 5 vertically stacked subplots, one per model: GPT3.5, GPT4, Gemini Pro, Mixtral 8x7B, Mistral Medium.
- X-axis: Input length (# tokens), values: 250, 500, 1000, 2000, 3000.
- Y-axis: Frequency, range 0-400.
- Stacked/grouped bars: True (green), Other/Refused (black), False (orange/yellow). Dashed line at ~300-400 indicates Samples Per Label.
- GPT3.5: True and False roughly balanced at short lengths; at longer lengths, False slightly increases relative to True, minimal Other/Refused.
- GPT4: True and False remain relatively balanced across all lengths. Very few Other/Refused answers.
- Gemini Pro: Most pronounced bias. False answers increase substantially with length (reaching ~400 at 3000 tokens), True answers shrink, and Other/Refused answers appear and grow notably.
- Mixtral 8x7B: Moderate increase in False bias at longer lengths. Some Other/Refused answers appear.
- Mistral Medium: False bias increases with length. Other/Refused answers grow more substantially than in GPT models.
