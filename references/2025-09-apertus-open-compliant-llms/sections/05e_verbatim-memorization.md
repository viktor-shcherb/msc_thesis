# 5.4 Verbatim Memorization [p. 46]

[p. 46] Verbatim similarity in the long-context pretrained base models, Apertus-8B-64k^46 and Apertus-70B-64k,^47 is evaluated on the Gutenberg sequences injected into the pretraining corpus, as detailed in Section 3.2.4. The evaluation uses Rouge-L, which measures the longest common subsequence relative to reference length (Lin, 2004), and the normalized length of the longest common contiguous substring (LCCS) (Freeman et al., 2024). The Type-Token Ratio (TTR) -- a measure of lexical diversity calculated as the ratio of unique to total tokens (Kettunen, 2014) -- is also employed in a dual capacity: as a filtering criterion on ground-truth suffixes to exclude structured, low-entropy content during evaluation, and as a diagnostic of text degeneration in model outputs during inference.

^46: huggingface.co/swiss-ai/Apertus-8B-2509
^47: huggingface.co/swiss-ai/Apertus-70B-2509

## 5.4.1 Apertus Memorization Patterns [p. 46]

[p. 46] Both Apertus-8B and Apertus-70B remain at baseline memorization (Rouge-L approximately 0.18, comparable to unrelated Gutenberg texts, Figure 8). Importantly, neither model exhibits memorization across any tested exposure frequency (<=128) or prefix length (<=5,000).

**Figure 8** (p. 46): **"Apertus Maintains Robustness Against Verbatim Memorization."** The heatmaps show average Rouge-L scores for suffixes of 500 tokens for Apertus-8B and Apertus-70B. The y-axis represents exposure frequencies during training (1--128), with unexposed Gutenberg bucket 0 serving as a baseline. The prefix length varied from 50 to 5,000 tokens at a fixed offset of 0. The results demonstrate successful mitigation of verbatim memorization in the Apertus model, as the Rouge-L scores for both model scales remain at baseline levels regardless of exposure frequency or prefix length.

- Left heatmap: "Apertus 8B (Greedy)" -- Rouge-L scores range from approximately 0.166 to 0.178 across all exposure frequencies (0, 1, 2, 4, 8, 16, 32, 64, 128) and prefix lengths (50, 100, 250, 500, 1000, 2000, 3000, 4000, 5000). Values are uniformly low with no visible increase pattern. Individual cell values visible: row 0 shows 0.166, 0.171, 0.172, 0.179, 0.180, 0.180, 0.184, 0.181, 0.182; similar patterns across all rows.
- Right heatmap: "Apertus 70B (Greedy)" -- Rouge-L scores range similarly, approximately 0.169 to 0.197. Values slightly higher overall than 8B but still uniformly at baseline. Row 0 shows 0.169, 0.174, 0.177, 0.178, 0.183, 0.188, 0.186, 0.186, 0.186. Higher exposure frequency rows (64, 128) show marginally higher values (up to 0.197) but no systematic memorization pattern.

## Robustness Across Decoding Strategies [p. 46]

[p. 46] Prior work established a connection between memorization and repetition-induced text degeneration (Xu et al., 2025), a phenomenon also observed for Apertus under greedy decoding (Table 25). TTR values remain low (0.22--0.31), increasing with exposure frequency but still well below the ground truth (~0.539). Qualitative inspection suggests this stems from thematic loops, particularly for rarely or unseen texts, which can produce artificially low Rouge-L scores (~0.18) reflecting poor generation quality rather than genuine mitigation. To rule this out, nucleus sampling (temperature=1.0, top-p=0.9) is also evaluated. Under this setting, Apertus maintains a high TTR (~0.500) close to the ground truth, while Rouge-L and LCCS remain at baseline. These results confirm that Apertus's mitigation is robust across decoding strategies and not an artifact of greedy decoding.

---
[p. 47 continued]

**Table 25: Impact of Decoding Strategy on Memorization and Text Degeneration for Apertus 70B.** Metrics are averaged across Gutenberg V1 and V2 at a fixed offset of 0, computed on 500-token suffixes conditioned on 500-token prefixes. The table compares greedy and nucleus sampling across exposure frequencies. Under greedy decoding, significant degeneration occurs, yet TTR still increases moderately from ~0.225 for unseen sequences to 0.313 at the highest exposure (a gain of 44 unique tokens). In contrast, nucleus sampling maintains high lexical diversity (TTR approximately 0.500). Crucially, verbatim recall metrics (Rouge-L, LCCS) remain at baseline for both strategies, confirming that the applied mitigation is robust and not an artifact of text degeneration. The arrows (up, down) show the desired direction for each metric.

| Exposure Frequency | Rouge-L (down) greedy | Rouge-L (down) nucleus | LCCS (down) greedy | LCCS (down) nucleus | TTR (up) greedy | TTR (up) nucleus | TTR (up) ground truth |
|---|---|---|---|---|---|---|---|
| 0 | 0.178 | 0.175 | 0.010 | 0.010 | 0.229 | 0.500 | 0.538 |
| 1 | 0.184 | 0.178 | 0.011 | 0.010 | 0.220 | 0.496 | 0.535 |
| 2 | 0.183 | 0.179 | 0.010 | 0.009 | 0.219 | 0.497 | 0.539 |
| 4 | 0.182 | 0.175 | 0.010 | 0.010 | 0.221 | 0.499 | 0.538 |
| 8 | 0.183 | 0.175 | 0.010 | 0.009 | 0.230 | 0.500 | 0.538 |
| 16 | 0.184 | 0.177 | 0.010 | 0.010 | 0.235 | 0.499 | 0.537 |
| 32 | 0.185 | 0.180 | 0.011 | 0.010 | 0.246 | 0.499 | 0.536 |
| 64 | 0.184 | 0.179 | 0.011 | 0.010 | 0.270 | 0.503 | 0.539 |
| 128 | 0.188 | 0.180 | 0.013 | 0.012 | 0.313 | 0.504 | 0.540 |

## Goldfish Loss Alters Memorization Dynamics [p. 47]

[p. 47] Prior work has shown the positional fragility of LLM memorization: initial tokens in the context window trigger the strongest recall, while memorization decays as prefixes shift further away (Xu et al., 2025). The authors' findings suggest that Goldfish Loss breaks this dependency, since selective token masking prevents the formation of continuous long-range anchors on initial tokens that typically anchor verbatim memorization. For the top 5% of most-memorized sequences (after filtering as in Section 5.4.2), recall does not follow the sharp offset-dependent decay predicted by positional fragility in Xu et al. (2025). Instead, it fluctuates within a narrow range (Figure 9), and the specific sequences vary with offset, likely because deterministic masking exposes different "unprotected" windows at different positions.

## Potential Primacy Effect [p. 47]

[p. 47] Figure 9 also suggests a potential primacy effect: Gutenberg sequences introduced during the first 0--9T tokens of pretraining appear more strongly memorized than those introduced in 9--12T. This pattern, however, may be confounded by differences in textual complexity between the v1 and v2 Gutenberg probe sets and therefore warrants further investigation.

**Figure 9** (p. 48): **"Temporal and Altered Positional Memorization Dynamics."** Three heatmaps comparing memorization for Gutenberg-V1 sequences (injected into the first 9T tokens of pretraining) versus Gutenberg-V2 sequences (injected between the 9-12T token marks) for the top 5% most-memorized sequences, evaluated using 500-token prefixes to generate 500-token suffixes. The x-axis represents the offset -- the number of tokens skipped from the start of a sequence before prefix extraction -- varied from 0 to 2048. The y-axis represents exposure frequency (repetitions). Left panel: "Gutenberg V1 (0-9T) - Top 5% Per Cell" -- shows Rouge-L scores across offsets and repetitions. Middle panel: "Gutenberg V2 (9-12T) - Top 5% Per Cell" -- similar layout. Rightmost panel: "Gutenberg V2 - V1 / Exp 0% Per Cell" -- difference plot showing that V2 - V1 is predominantly blue, indicating that sequences from the earlier training stage (V1) were more strongly memorized (a primacy effect). The difference can be substantial; a Rouge-L difference of 0.1, as seen in some cells, corresponds to 50 additional tokens being memorized in the 500-token suffix. Both the V1 and V2 plots show that for the top memorized sequences, recall fluctuates across offsets rather than exhibiting the sharp decay characteristic of positional fragility.

## 5.4.2 Failure Case Studies [p. 47–48]

[p. 47] Despite its success, Goldfish Loss has a key limitation: its deterministic hashing is fragile to near-duplicates. This property becomes critical when training data contains multiple, slightly varied versions of the same text. The analysis shows that the most frequently memorized sequences are overwhelmingly canonical works, including Keats's poems, Shakespeare's plays, the US Constitution, and the Bible, which appear both in the Gutenberg sequences and repeatedly in the 15T pretraining corpus, accounting for all 22 sequences with a ROUGE-L score >= 0.7 among the 10,672 Gutenberg probes.

Goldfish Loss hashes a fixed-size preceding context (H = 50 tokens) to decide which tokens to mask, but even small divergences alter the hash. Two main sources are identified:

(i) **Formatting divergence**, since the Gutenberg sequences follow a fixed layout of ~21.5 tokens per line, whereas web versions often differ in line-breaking, introducing varying numbers of `\n` tokens.

---
[p. 48 continued]

(ii) **Tokenizer inconsistency**, where leading whitespace or subword segmentation produces different token IDs (Bostrom & Durrett, 2020; Chai et al., 2024). A single-token shift is enough for Gutenberg and web variants of the same passage to be masked inconsistently, so tokens masked in the Gutenberg version are revealed in the web version, allowing the model to memorize the entire sequence.

The authors also find "false positives" as shown in Figure 10: high verbatim recall of structured, low-diversity content (e.g., tables, recipe lists, contents pages). Here, high ROUGE-L reflects template learning rather than true verbatim memorization, typically on true suffixes with TTR <= 0.4 for a 500-token suffix. Such cases carry lower copyright and privacy risks than memorization of literary passages.

**Figure 10** (p. 48): **"Memorization patterns across TTR distributions for 500-token suffixes."** Three panels:
- (a) "TTR Distribution" -- Distribution of ground truth TTR values for Stage 1 (500 sequences per bucket) and Stage 2 (167 sequences per bucket). The vertical line at TTR=0.4 marks the threshold below which sequences are predominantly structured, repetitive content. An inset table shows filtering statistics.
- (b) "TTR vs Memorization" -- Scatter plot showing negative correlation between TTR and ROUGE-L scores (r = -0.540 for Stage 1, r = -0.451 for Stage 2), demonstrating that low-diversity sequences exhibit higher verbatim recall.
- (c) "Mean Memorization" -- Bar chart showing mean memorization levels across TTR ranges for Stage 1 and Stage 2, confirming that sequences with TTR <= 0.4 show elevated ROUGE-L scores, often representing template learning rather than true verbatim memorization of unique content.
