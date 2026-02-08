# 4 The perturbation of long-range context [p. 6]

[p. 6] The experiments in the previous section show that incorporating long-range context (further than 2K tokens away from the target) yields only marginal improvements to the overall perplexities of RT and LT. However, the long-range context does have a notable positive impact on a subset of tokens and book types. The authors ask: Do these improvements persist in the presence of severe perturbations to the distant context? If so, this would indicate that the models are not encoding any complex discourse structure in the context but rather relying on surface information (e.g., token presence) to make better predictions. A perturbation analysis is performed to quantitatively measure the robustness of the state-of-the-art RT model.^16 [p. 6]

**Footnote 16:** Figure 20 in the Appendix shows that the Local Transformer never uses context beyond 3K. Due to this limitation, only results on RT are presented in this section. [p. 6]

**Figure 8** (p. 6): "Generic illustration of the x-axis in all the perturbation analysis."
- Diagram showing the max sequence length (8K) divided into three segments from left to right: "perturbed prefix" (highlighted in red), "unperturbed prefix", and "Target". The x-axis represents the perturbation length.

Formally, given a prefix sequence $P = (w_0, w_1, \ldots, w_n)$ with which the model wants to predict target sequence $(w_{n+1}, w_{n+2}, \ldots, w_{n+k})$. A perturbation $\rho$ is applied to the first $m$ tokens of the prefix $(w_{0:m})$ to obtain the perturbed prefix:

$$\tilde{P} = (\rho(w_0, \ldots, w_m), w_{m+1}, \ldots, w_n).$$

Three perturbation operations are defined for $\rho$ and results are reported averaged over five runs for each of them: [p. 6]

- **Sequence shuffling**: Tokens within the perturbed window $w_{0:m}$ are shuffled across the entire window (i.e., sentence boundaries are not respected).

- **Random sequence replacement**: $w_{0:m}$ is replaced with a random sequence from another validation book that is $m$ tokens long.

- **Specific token drop**: Specific tokens within $w_{0:m}$ (e.g., those that occur in the target) are dropped and replaced with the padding token.

**Figure 7** (p. 6): "Perturbing up to 6K prefix tokens does not notably affect RT's overall perplexity. The corresponding plot for LT is included in Appendix D."
- X-axis: perturbation length (0-8000); Y-axis: perplexity (~35-42).
- Three lines: RT-shuffle (blue), RT-random (green), RT-8K (red dashed baseline).
- Inset zooms into perturbation length 0-5000, showing perplexity range ~35.25-35.50.
- All three lines remain near ~35.2-35.5 for perturbation lengths up to ~6K, then rise sharply. RT-shuffle rises to ~42 at 8K. RT-random rises to ~40 at 8K.
- Supports the claim that perturbing up to 6K prefix tokens does not notably affect RT's overall perplexity.

**Figure 9** (p. 6): "While perturbing up to 6K prefix tokens has little impact on frequent tokens, it increases the perplexity of infrequent tokens."
- Two panels: "Frequent tokens" (left) and "Infrequent tokens" (right).
- Left panel: X-axis: perturbation length (0-8000); Y-axis: perplexity (~25-29). RT-shuffle (blue), RT-random (green), RT-8K (red dashed). All lines flat at ~25 until ~6K, then rise slightly.
- Right panel: X-axis: perturbation length (0-8000); Y-axis: perplexity (~1200-2250). Inset zooms into 0-5000 showing ~1200-1225. RT-shuffle and RT-random increase sharply after ~5K perturbation length, with RT-shuffle reaching ~2250 and RT-random ~1750.

**Figure 10** (p. 6): "Both shuffling and random replacement increase the perplexity of tokens inside subword clusters, with the former having more negative impact."
- Two panels: "First subword token" (left) and "Rest of subword tokens" (right).
- Left panel: X-axis: perturbation length (0-8000); Y-axis: perplexity (~8000-16000). RT-shuffle (blue) rises from ~8000 to ~16000. RT-random (green) rises from ~8000 to ~10000. RT-8K (red dashed) flat at ~8000.
- Right panel: X-axis: perturbation length (0-8000); Y-axis: perplexity (~3.6-4.2). RT-shuffle rises from ~3.6 to ~4.2. RT-random rises from ~3.6 to ~3.9. RT-8K flat at ~3.6.

---
[p. 7–8 continued]

## Sequence-level perturbations further than 2K tokens from the target have minimal impact on perplexity [p. 7]

[p. 7] Applying sequence-level shuffling and random replacement to the distant context, both operations have minimal impact on the perplexity of all tokens (Figure 7) as well as frequent/infrequent tokens (Figure 9) provided at least 2K tokens are left unperturbed. However, these perturbations do have increasing impact as the perturbations come closer to the target, especially for infrequent tokens. Zooming in on the long-range context, random replacement consistently results in higher perplexity than shuffling, but also shuffling distant context actually achieves slightly *lower* perplexity than when the model is given completely unperturbed prefixes. Overall, these results demonstrate that RT is insensitive to the word order of the long-range context. [p. 7]

## Tokens inside subword clusters and tokens repeated in the distant context depend on word order [p. 7]

[p. 7] Similar to the analysis in Section 3, the experiments above may hide impacts on small subsets of tokens, which motivates a more fine-grained analysis. Tokens inside subword clusters (Figure 10) and those that can only be copied from long-range context (Figure 11) are sensitive to both the order and the content of the remote context. While random replacement is more harmful than shuffling for tokens that can be copied in the distant context (172 shuffled vs 174 random replacement perplexity when perturbing 6K tokens), shuffling is more detrimental for tokens inside subword clusters (3.8 vs 3.7 perplexity when perturbing 6K tokens). [p. 7]

**Figure 11** (p. 7): "Both perturbation operations increase the perplexity of target tokens whose last appearance in the prefix is more than 2K tokens away."
- Single panel: "Occurs >2K tokens away"
- X-axis: perturbation length (0-8000); Y-axis: perplexity (~170-220).
- RT-shuffle (blue) rises from ~170 to ~220 as perturbation length increases. RT-random (green) rises from ~170 to ~210. RT-8K (red dashed) flat at ~170.
- Inset zooms into perturbation length 0-5000 showing perplexity range ~170-175.

## Routing Transformer encodes token identity in the long-range context [p. 7–8]

[p. 7–8] Moving to more targeted perturbations, given the observation that RT perplexity decreases on copied tokens as sequence length increases (Section 3), the question is how much that perplexity decrease depends on word order and surrounding content. The authors drop tokens in the distant context whose next appearance is in the target sequence. As a control experiment, they drop the same number of random tokens for each perturbation length. [p. 7]

[p. 8] As shown in the right plot of Figure 12, dropping the previous long-range occurrences of target tokens increases the perplexity of those target tokens, which shows that RT indeed memorizes token identity in the long-range context to some extent. The left plot shows that dropping long-range duplicate tokens does not affect tokens that also occur within the local context (i.e., the prior 2K tokens). The flat curve before 6K indicates the model relies only on the most recent occurrences for prediction. [p. 8]

**Figure 12** (p. 7): "Perplexity of target tokens whose last occurrence in the prefix is within previous 2K tokens (**left**) or more than 2K tokens away (**right**), when dropping either these target tokens or random tokens in the perturbed range. The curve on the right indicates RT memorizes token identity in the distant prefix to some extent."
- Two panels: "Occurs <2K tokens" (left) and "Occurs >2K tokens away" (right).
- Left panel: X-axis: perturbation length (2000-8000); Y-axis: perplexity (~14.1-14.4). Two lines: drop-target (blue) and drop-random (green). Both lines relatively flat around ~14.1-14.3, with drop-target slightly higher.
- Right panel: X-axis: perturbation length (2000-8000); Y-axis: perplexity (~167-172). Drop-target (blue) rises from ~168 to ~172 as perturbation length increases. Drop-random (green) relatively flat around ~168-169. Shows RT memorizes token identity in distant prefix.
