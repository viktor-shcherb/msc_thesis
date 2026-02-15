# 3.4 Key Information Retrieval [p. 6]

## Evaluation Protocol [p. 6]

The Needle-In-A-Haystack (Kamradt, 2023) test is widely used to evaluate the ability to extract critical information embedded in a large context [p. 6]. The authors follow the multi-needle evaluation protocol of LWM (Liu et al., 2024a) and Gemini 1.5 (Reid et al., 2024) [p. 6]. The needles are inserted into varying depths within contexts of different lengths [p. 6]. Each needle consists of a concise sentence that assigns a unique magic number to a specific city [p. 6]. The goal is to retrieve the magic numbers corresponding to the query cities [p. 6]. They position the answer needle at five different depths within the context: 0%, 25%, 50%, 75%, and 100%, while placing other distracting needles at varying positions [p. 6]. Each combination of depth and length is evaluated using 50 samples [p. 6]. The average accuracy is reported [p. 6]. Let N denote the total number of number-city pairs and R the number of query cities [p. 6].

## Retrieve from 4K Context Length [p. 6]

As shown in Table 2, the authors insert N = 1, 2, 4, 6 needles into 4K-length contexts and retrieve R = 1, 2, 2, 2 needles [p. 6]. They evaluate 3B-size models trained with 4K input length (Appendix B) [p. 6]. They find that both models obtain good accuracy for N = 1 and N = 2 [p. 6]. As N and R increase, DIFF Transformer maintains a consistent accuracy, while the performance of Transformer drops significantly [p. 6]. In particular, at N = 6, R = 2, the accuracy gap between the two models reaches 30% [p. 6]. The results indicate the superior ability of DIFF Transformer to retrieve key information in distracting contexts [p. 6].

| Model | N = 1<br>R = 1 | N = 2<br>R = 2 | N = 4<br>R = 2 | N = 6<br>R = 2 |
|-------|----------------|----------------|----------------|----------------|
| Transformer | 1.00 | 0.85 | 0.62 | 0.35 |
| DIFF | 1.00 | 0.92 | 0.84 | 0.85 |

Table 2: Multi-needle retrieval accuracy in 4K length, averaged across varying answer needle positions [p. 6]. N represents the number of needles, and R denotes the number of query cities [p. 6].

## Retrieve from 64K Context Length [p. 6]

As shown in Figure 5, the evaluated context length ranges from 8K to 64K for the N = 8, R = 1 setting [p. 6]. They evaluate the 3B-size models with length extension (Section 3.3) [p. 6]. They report the accuracy across varying answer needle depths (y-axis) and context lengths (x-axis) [p. 6]. The bottom row is the average accuracy for all depths [p. 6]. DIFF Transformer maintains stable performance across different context lengths [p. 6]. In contrast, Transformer's average accuracy gradually declines as the context length increases to the maximal length, i.e., 64K [p. 6]. Besides, DIFF Transformer outperforms Transformer particularly when key information is positioned within the first half of the context (i.e., 0%, 25%, and 50% depth) [p. 6]. In particular, when needles are placed at the 25% depth in a 64K context, DIFF Transformer shows 76% accuracy improvement over Transformer [p. 6].

**Figure 5** (p. 6): "Multi-needle retrieval results in 64k length."

Description: Two heatmaps comparing Transformer and Diff Transformer performance
- **(a) Transformer:**
  - Rows: Depth (%) from 0 to Avg, values: 0, 25, 50, 75, 100, Avg
  - Columns: Context Length from 4K to 64K (4K, 8K, 16K, 32K, 48K, 56K, 64K)
  - Color scale: Score from -0.0 (dark red) to 1.0 (teal)
  - Values show declining performance, especially at 25% depth and longer contexts
  - Notable poor cells: 0.16 at 25%/24K, 0.12 at 25%/32K, 0.12 at 25%/64K
  - Average row shows decline: 0.95, 0.84, 0.78, 0.64, 0.50, 0.75, 0.78, 0.52
- **(b) DIFF Transformer:**
  - Same structure as (a)
  - Generally higher scores (more teal coloring) across all positions
  - More consistent performance across depths and context lengths
  - 25%/64K cell shows 0.88 (vs 0.12 in Transformer)
  - Average row maintains high scores: 1.00, 0.94, 0.87, 0.83, 0.83, 0.92, 0.84, 0.85
- Supports claim: DIFF Transformer maintains stable performance across context lengths while Transformer declines, with 76% improvement at 25% depth in 64K context [p. 6]

## Attention Score Analysis [p. 6–7]

Table 3 presents the attention scores allocated to the answer span and the noise context for the key information retrieval task [p. 6]. The scores indicate the model's ability to preserve useful information against attention noise [p. 6]. The authors compare the normalized attention scores when key information is inserted at different positions (i.e., depths) within the context [p. 6]. Compared with Transformer, DIFF Transformer allocates higher attention scores to the answer span and has lower attention noise [p. 6].

| Model | Attention to Answer ↑ |  |  |  |  | Attention Noise ↓ |  |  |  |  |
|-------|------|------|------|------|------|------|------|------|------|------|
|       | 0%   | 25%  | 50%  | 75%  | 100% | 0%   | 25%  | 50%  | 75%  | 100% |
| Transformer | 0.03 | 0.03 | 0.03 | 0.07 | 0.09 | 0.51 | 0.54 | 0.52 | 0.49 | 0.49 |
| DIFF | 0.27 | 0.30 | 0.31 | 0.32 | 0.40 | 0.01 | 0.02 | 0.02 | 0.02 | 0.01 |

Table 3: Attention scores allocated to answer spans and noise context in the key information retrieval task [p. 7]. The target answer is inserted in varying positions (i.e., depth) of context [p. 7]. DIFF Transformer allocates more attention scores to useful information and effectively cancels out attention noise [p. 7].
