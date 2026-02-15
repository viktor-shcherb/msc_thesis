# Appendix C: Attention sink in open-sourced LMs [p. 17-21]

## C.1 How positional embedding relates to attention sink [p. 17-18]

In Section 3.3, we have shown that Mistral-7B, LLaMA2-7B Base, and LLaMA3-8B Base, which adopt rotary as PE, have no attention sink for repeated token sequences. While GPT2, which adopts learnable PE, has the attention sink in such situations. To further understand this, we explore how positional embedding plays a role through a theoretical perspective.

### Activations

[p. 17]

Suppose the repeated sequence is $\mathbf{X} = \{x_1, x_2, \ldots, x_T\}$ and each $x_i = x$. For LMs with NoPE/relative PE/ALiBi/Rotary, we have the initial hidden states $h_i^0 = x\mathbf{W}_E$, which are the same among all the token positions since $\mathbf{P} = \mathbf{0}$. Then for the first transformer block $l = 1$, we know that $k_i^{1,h} = \text{LN}(h_i^0)\mathbf{W}_K^{1,h} = \text{LN}(x\mathbf{W}_E)\mathbf{W}_K^{1,h}$, $q_i^{1,h} = \text{LN}(h_i^0)\mathbf{W}_Q^{1,h} = \text{LN}(x\mathbf{W}_E)\mathbf{W}_Q^{1,h}$, and $v_i^{1,h} = \text{LN}(h_i^0)\mathbf{W}_V^{1,h} = \text{LN}(x\mathbf{W}_E)\mathbf{W}_V^{1,h}$. Then all tokens have the same $k_i^{1,h}$, $q_i^{1,h}$, and $v_i^{1,h}$. Then the attention output is

$$
\bar{v}_i^{1,h} = \sum_{i=1}^{t} A_{i,i}^{1,h} v_i^{1,h} = v_i^{1,h} \quad (10)
$$

Then $o_i^1 = \text{Concat}_{h=1}^{H}(\bar{v}_i^{1,h})\mathbf{W}_O^1$, we have the hidden states after the first block:

$$
h_i^1 = \text{FFN}(\text{LN}(o_i^1 + h_i^0)) + o_i^1 + h_i^0 \quad (11)
$$

$$
= \text{FFN}(\text{LN}(\text{Concat}_{h=1}^{H}(v_i^{1,h})\mathbf{W}_O^1 + h_i^0)) + \text{Concat}_{h=1}^{H}(v_i^{1,h})\mathbf{W}_O^1 + h_i^0 \quad (12)
$$

$$
= \text{FFN}(\text{LN}(\text{Concat}_{h=1}^{H}(\text{LN}(h_i^0)\mathbf{W}_V^{1,h})\mathbf{W}_O^1 + h_i^0)) \quad (13)
$$

$$
+ \text{Concat}_{h=1}^{H}(\text{LN}(h_i^0)\mathbf{W}_V^{1,h})\mathbf{W}_O^1 + h_i^0. \quad (14)
$$

Since $h_1^0 = h_2^0 = \cdots = h_T^0$, we have $h_1^1 = h_2^1 = \cdots = h_T^1$ based on the above equation. Using this induction, we could prove that

$$
h_l^l = \text{FFN}(\text{LN}(\text{Concat}_{h=1}^{H}(\text{LN}(h_l^{l-1})\mathbf{W}_V^{l,h})\mathbf{W}_O^l + h_l^{l-1})) \quad (15)
$$

$$
+ \text{Concat}_{h=1}^{H}(\text{LN}(h_l^{l-1})\mathbf{W}_V^{l,h})\mathbf{W}_O^l + h_l^{l-1}, \quad \forall \ 1 \leq l \leq L. \quad (16)
$$

$$
h_1^l = h_2^l = \cdots = h_T^l, \quad \forall \ 0 \leq l \leq L. \quad (17)
$$

Typically, the hidden states of the first token $h_1^l$ in specific blocks have massive activations. Due to the above equality, all the repeated tokens have massive activations. Furthermore, we could derive the closed form or upper bounds for attention scores under the repeated token sequence.

**Proposition 1.** For LMs with NoPE, the attention scores for t repeated tokens are $t^{-1}$ uniformly, i.e., there is no attention sink.

*Proof.* We have that

$$
A_{i,i}^{l,h} = \frac{e^{\langle q_i^{l,h}, k_i^{l,h} \rangle}}{\sum_{j=1}^{t} e^{\langle q_i^{l,h}, k_j^{l,h} \rangle}} = \frac{e^{q^{l,h} k^{l,h\top}}}{\sum_{j=1}^{t} e^{q^{l,h} k^{l,h\top}}} = \frac{e^{q^{l,h} k^{l,h\top}}}{t e^{q^{l,h} k^{l,h\top}}} = \frac{1}{t}. \quad (18)
$$

Therefore, the attention scores follow a uniform distribution over all previous tokens. □

**Proposition 2.** For LMs with relative PE, there is no attention sink for t repeated tokens.

*Proof.* For LMs with relative PE, the dot product between each query and key is

$$
\langle q_i^{l,h}, k_i^{l,h} \rangle = q_i^{l,h} k_i^{l,h\top} + g_{\text{rel}}(t - i) = q^{l,h} k^{l,h\top} + g_{\text{rel}}(t - i), \quad (19)
$$

then we have the attention scores

$$
A_{i,i}^{l,h} = \frac{e^{\langle q_i^{l,h}, k_i^{l,h} \rangle}}{\sum_{j=1}^{t} e^{\langle q_i^{l,h}, k_j^{l,h} \rangle}} = \frac{e^{q^{l,h} k^{l,h\top} + g_{\text{rel}}(t-i)}}{\sum_{j=1}^{t} e^{q^{l,h} k^{l,h\top} + g_{\text{rel}}(t-i)}} = \frac{e^{g_{\text{rel}}(t-i)}}{\sum_{j=1}^{t} e^{g_{\text{rel}}(t-i)}}. \quad (20)
$$

[p. 18]

Considering $g_{\text{rel}}(t - i)$ is a monotonic non-increasing function of $t - i$ and $g_{\text{rel}}(t - i) = B - 1$ when $t - i > D$, then $A_{t,1}^{l,h} = A_{t,1}^{l,h} = \cdots = A_{t,t-D}^{l,h}$ are the largest values. Therefore, there is no attention sink on the first token. □

**Proposition 3.** For LMs with ALiBi, there is no attention sink for t repeated tokens.

*Proof.* For LMs with ALiBi, similar to relative PE, the dot product between each query and key is

$$
\langle q_i^{l,h}, k_i^{l,h} \rangle = q_i^{l,h} k_i^{l,h\top} + g_{\text{alibi}}^h(t - i) = q^{l,h} k^{l,h\top} + g_{\text{alibi}}^h(t - i), \quad (21)
$$

then we have the attention scores

$$
A_{i,i}^{l,h} = \frac{e^{\langle q_i^{l,h}, k_i^{l,h} \rangle}}{\sum_{j=1}^{t} e^{\langle q_i^{l,h}, k_j^{l,h} \rangle}} = \frac{e^{q^{l,h} k^{l,h\top} + g_{\text{alibi}}^h(t-i)}}{\sum_{j=1}^{t} e^{q^{l,h} k^{l,h\top} + g_{\text{alibi}}^h(t-i)}} = \frac{e^{g_{\text{alibi}}^h(t-i)}}{\sum_{j=1}^{t} e^{g_{\text{alibi}}^h(t-i)}}. \quad (22)
$$

Here $g_{\text{alibi}}^h(t - i)$ is monotonic decreasing function of $t - i$, so there is no attention sink on the first token. □

**Proposition 4.** For LMs with Rotary, there is no attention sink for t repeated tokens when t is large if $||q^{l,h}|| \cdot ||k^{l,h}|| \leq \xi$ for a constant $\xi$.

*Proof.* For LMs with Rotary, the dot product between each query and key is

$$
\langle q_i^{l,h}, k_i^{l,h} \rangle = q_i^{l,h} \mathbf{R}_{\Theta,i-j} k_i^{l,h\top} \quad (23)
$$

$$
= q^{l,h} \mathbf{R}_{\Theta,i-j} k^{l,h\top} \quad (24)
$$

$$
= ||q^{l,h}|| \, ||k^{l,h} \mathbf{R}_{\Theta,i-1}|| \cos\left(\frac{q^{l,h} \mathbf{R}_{\Theta,i-1} k^{l,h\top}}{||q^{l,h}|| \, ||k^{l,h} \mathbf{R}_{\Theta,i-1}||}\right) \quad (25)
$$

$$
= ||q^{l,h}|| \, ||k^{l,h}|| \cos(\beta_{i-1}), \quad (26)
$$

where $\beta_{i-1}$ is the angle between the rotated query and the rotated key. Then the attention scores are

$$
A_{i,i}^{l,h} = \frac{e^{\langle q_i^{l,h}, k_i^{l,h} \rangle}}{\sum_{j=1}^{t} e^{\langle q_i^{l,h}, k_j^{l,h} \rangle}} = \frac{e^{q^{l,h} \mathbf{R}_{\Theta,i-i} k^{l,h\top}}}{\sum_{j=1}^{t} e^{q^{l,h} \mathbf{R}_{\Theta,i-j} k^{l,h\top}}} = \frac{e^{||q^{l,h}|| \, ||k^{l,h}|| \cos(\beta_{i-j})}}{\sum_{j=1}^{t} e^{||q^{l,h}|| \, ||k^{l,h}|| \cos(\beta_{i-j})}}. \quad (27)
$$

Suppose the norm of multiplication for query and key $||q^{l,h}|| \, ||k^{l,h}|| = \xi$. Considering $-1 \leq \cos(\beta_{i-j}) \leq 1$, then we have

$$
A_{i,i}^{l,h} = \frac{e^{\xi \cos(\beta_{i-1})}}{\sum_{j=1}^{t} e^{\xi \cos(\beta_{i-j})}} = \frac{1}{1 + \sum_{j \neq i} e^{\xi(\cos(\beta_{i-j}) - 1)}} \leq \frac{e^{2\xi}}{e^{2\xi} + (t-1)}. \quad (28)
$$

Then the attention scores for each token are upper-bounded and decrease to 0 as $t$ grows. □

For LMs with absolute PE/learnable PE, the initial hidden states $h_i^0 = x\mathbf{W}_E + p_t$. Although the word embeddings are the same for repeated tokens, $p_t$ for different token positions $t$ is different. Therefore, GPT2 models have no the above equality. From Table 1(Left), GPT2-XL still allocates significant attention to the first token even with repeated tokens, which motivates us to explore whether attention sink is related to these learned positional embedding vectors $\mathbf{p}_{1:T}$ after LM pre-training.

Therefore, we conduct two experiments on GPT2-XL. Firstly, we replace the first positional embedding vector $\mathbf{p}_1$ with other vectors $\mathbf{p}_{t \neq 1}$. In Table 7, we find that the amplitude of attention sink on the first token is significantly reduced. Then we also consider swapping the first positional embedding vector $\mathbf{p}_1$ with another position $\mathbf{p}_{t \neq 1}$. Consequently, the $t$-th token becomes the new sink token. Therefore, attention sink in GPT2-XL is strongly attached to the first positional embedding vector $\mathbf{p}_1$.

**Table 7:** In GPT2-XL, replacing or swapping the first positional embedding vector $\mathbf{p}_1$ with another position $\mathbf{p}_{t \neq 1}$ significantly impact the amplitude and position of attention sink.

| Replaced position $t$ | no | 5 | 10 | 15 | 20 | 25 | 25 |
|---|---|---|---|---|---|---|---|
| Sink₁↑(%) | 62.28 | 0.20 | 2.36 | 7.73 | 10.63 | 10.97 | 10.21 |
| Sinkₜ↓(%) | - | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| Swapped position $t$ | no | 5 | 10 | 15 | 20 | 25 | 25 |
| Sink₁↑(%) | 62.28 | 1.44 | 3.73 | 6.78 | 8.95 | 9.42 | 9.73 |
| Sinkₜ↑(%) | - | 57.63 | 54.48 | 52.81 | 51.70 | 51.13 | 50.22 |

## C.2 Attention sink under different data domains [p. 19]

There are 17 available data domains in the Pile dataset (Gao et al., 2020), including Pile-CC, PubMed Central, ArXiv, Github, FreeLaw, Stack Exchange, USPTO Backgrounds, Pubmed Abstracts, Gutenberg (PG-19), Wikipedia (en), DM Mathematics, Ubuntu IRC, EuroParl, HackerNews, PhilPapers, NIH ExPorter, and Enron Emails. We sample 100 data from each domain and then evaluate the attention sink metric for GPT2-XL/Mistral-7B/LLaMA2-7B Base/LLaMA3-8B Base. As shown in Figure 9, the evaluated attention sink metrics Sink₁↑ are similar across different domains when $\epsilon = 0.2$ and $\epsilon = 0.3$. Small fluctuations appear when $\epsilon = 0.4$.

**Figure 9** (p. 19): Input domains have negligible effects on attention sink metric Sink₁↑ for (left) $\epsilon = 0.2$ and (middle) $\epsilon = 0.3$. There are small fluctuations for (right) $\epsilon = 0.4$.

Description: Three scatter plots showing Sink₁↑(%) vs Domain ID (1-17) for different values of $\epsilon$ (0.2, 0.3, 0.4). Each plot shows four model types: GPT2-XL (blue circles), LLaMA2-7B Base (red diamonds), Mistral-7B (orange diamonds), and LLaMA3-8B Base (purple squares).
- Key elements: x-axis shows Domain ID from 1 to 17, y-axis shows Sink₁↑(%) ranging from 60-100%
- Notable patterns: For $\epsilon = 0.2$ and $\epsilon = 0.3$, GPT2-XL shows consistent high values around 90-100%, while other models show lower, more stable values around 70-80%. For $\epsilon = 0.4$, there's more variation across domains but still consistent patterns per model.
- Supports claim: Input domains have negligible effects on attention sink metric.

## C.3 Attention sink under different pre-trained LMs [p. 19-21]

### Relation to LM performance [p. 19]

We leverage the platform (Gao et al., 2024) to evaluate the performance of open-sourced LMs, including LLaMA3/OPT/Pythia/GPT2 families, on downstream LM task, e.g., HellaSwag (Zellers et al., 2019). The results are visualized parallel with our attention sink metric in Figure 10, including both accuracy (Acc) and accuracy under normalization (Acc_Norm). We find that within the same LM family with the increase of model scale, both attention sink amplitude and downstream LM performance are increasing. However, across different LM families, stronger attention sink does not always mean stronger performance. For instance, the OPT family has stronger attention sink than Pythia under the comparable model scale. However, the downstream LM performance is comparable.

**Figure 10** (p. 20): Attention sink and downstream performance for various pre-trained LMs.

Description: Three line plots showing the relationship between model parameters (x-axis: 10M to 10B) and three metrics (y-axis): Sink₁↑(%), Acc(%), and Acc_Norm(%).
- Key elements: Models shown include GPT2, Pythia, LLaMA2, LLaMA3, and OPT families with parameter counts ranging from 10M to 10B
- Notable patterns: Within each family, both attention sink and performance increase with model scale. GPT2 shows highest Sink₁↑ values (80-100%). LLaMA2 and LLaMA3 show lower sink values but comparable or better downstream performance.
- Supports claim: Within the same LM family, attention sink and performance both increase with scale. Across families, stronger attention sink does not always correlate with better performance.

### ℓ₂-norm [p. 19-20]

We first show that large $\ell_2$-norm of hidden states $h_1^l$ and small $\ell_2$-norm of keys $k_1^{l,h}$ and values $v_1^{l,h}$ (especially for values) universally exist in open-sourced LMs, including LLaMA2-7B Base (Figure 11), GPT2-Large (Figure 12), Mistral-7B (Figure 13), and Pythia-1B (Figure 14). It is noted that for the final transformer block $l = L$, we take the hidden states before LN. We note that different LMs may have different starting blocks where massive activations appear.

**Figure 11** (p. 20): $\ell_2$-norm of hidden states/keys/values of the first token/other tokens in LLaMA2-7B Base.

Description: Three line plots showing $\ell_2$-norm values across transformer blocks (0-32 on x-axis).
- Left panel: Hidden states $h_1^l$ (blue) shows large values around 1000, while $h_{l \neq 1}^l$ (orange) shows much lower values around 200
- Middle panel: Keys $k_1^l$ (blue) around 4-6, $k_{l \neq 1}^l$ (orange) shows values around 12-18
- Right panel: Values $v_1^l$ (blue) starts low and increases to ~6, $v_{l \neq 1}^l$ (orange) shows steady increase to ~18
- Key elements: x-axis shows transformer block index, y-axis shows $\ell_2$-norm values
- Notable patterns: Large $\ell_2$-norm for hidden states of first token, smaller norm for keys/values of first token compared to other tokens
- Supports claim: Large $\ell_2$-norm of $h_1^l$ and small $\ell_2$-norm of $k_1^{l,h}$ and $v_1^{l,h}$ universally exist

**Figure 12** (p. 20): $\ell_2$-norm of hidden states/keys/values of the first token/other tokens in GPT2-Large.

Description: Three line plots showing $\ell_2$-norm values across transformer blocks (0-36 on x-axis).
- Left panel: $h_1^l$ shows a distinctive hump pattern peaking around 2400 at blocks 8-24, $h_{l \neq 1}^l$ stays low around 700
- Middle panel: $k_1^l$ peaks around 18 then drops, $k_{l \neq 1}^l$ shows values 12-18
- Right panel: $v_1^l$ starts very low (~2) and increases to ~8, $v_{l \neq 1}^l$ shows steady increase to ~6
- Notable patterns: GPT2-Large shows more dramatic variation in hidden state norms with a pronounced peak in middle layers
- Supports claim: Similar pattern of large $h_1^l$ norm and distinct first token behavior

**Figure 13** (p. 20): $\ell_2$-norm of hidden states/keys/values of the first token/other tokens in Mistral-7B.

Description: Three line plots showing $\ell_2$-norm values across transformer blocks (0-32 on x-axis).
- Left panel: $h_1^l$ shows consistent values around 280, $h_{l \neq 1}^l$ shows lower values around 70
- Middle panel: $k_1^l$ shows consistent values around 12-18, $k_{l \neq 1}^l$ around 12-18
- Right panel: $v_1^l$ starts low and increases to ~10, $v_{l \neq 1}^l$ shows similar pattern
- Notable patterns: Mistral-7B shows more stable patterns compared to GPT2-Large
- Supports claim: Pattern holds across different architectures

**Figure 14** (p. 20): $\ell_2$-norm of hidden states/keys/values of the first token/other tokens in Pythia-1B.

Description: Three line plots showing $\ell_2$-norm values across transformer blocks (0-16 on x-axis).
- Left panel: $h_1^l$ shows hump pattern peaking around 1800 at blocks 4-8, $h_{l \neq 1}^l$ around 400
- Middle panel: $k_1^l$ shows decreasing pattern from ~24 to ~6, $k_{l \neq 1}^l$ relatively stable around 18-24
- Right panel: $v_1^l$ shows highly variable pattern decreasing from ~12 to ~3, $v_{l \neq 1}^l$ starts around 6-9 and decreases
- Notable patterns: Pythia shows different patterns, especially in the decreasing trends for keys/values
- Supports claim: While patterns vary, the distinction between first token and other tokens is still evident

[p. 21]

**Figure 15** (p. 21): Cosine similarity and $\ell_2$-norm product between keys and queries in LLaMA3-8B Base.

Description: Eight heatmap panels arranged in 2 rows and 4 columns, showing attention patterns for different sequence lengths ($l = 5, 10, 19, 31$) and heads ($h = 1$).
- Top row: Heatmaps showing cosine similarity $\cos(q_i^{l,h}, k_j^{l,h})$ with blue diagonal patterns and yellow/green off-diagonal regions marked as "Sink" or "No Sink"
- Bottom row: Heatmaps showing $||q_i^{l,h}|| \cdot ||k_j^{l,h}||$ with purple/blue diagonal patterns and yellow off-diagonal regions
- Key elements: x-axis and y-axis represent token positions, color scales show cosine similarity (-0.4 to 0.4) and norm products (0 to 260)
- Notable patterns: Diagonal patterns in cosine similarity, distinct "Sink" regions in some configurations, varying intensity of norm products
- Supports claim: QK angles contribute to attention sink through more visualizations

**Figure 16** (p. 21): Cosine similarity and $\ell_2$-norm product between keys and queries in LLaMA2-7B Base.

Description: Eight heatmap panels similar to Figure 15, showing attention patterns for different sequence lengths and heads in LLaMA2-7B.
- Top row: Cosine similarity heatmaps with similar blue diagonal and yellow/green patterns
- Bottom row: Norm product heatmaps with purple/blue patterns
- Key elements: Similar structure to Figure 15 with different value ranges
- Notable patterns: Similar diagonal structure but with different sink/no-sink distributions compared to LLaMA3
- Supports claim: Pattern comparison across different model architectures

### QK angles [p. 21]

Then we further demonstrate that QK angles contribute to attention sink through more visualizations, including LLaMA3-8B Base (Figure 15), LLaMA2-7B Base (Figure 16), Mistral-7B (Figure 17), and GPT2-Large (Figure 18).

### Block-wise and head-wise property [p. 21]

In the main paper, we mainly discuss the ratio of heads that have attention sink using the definition of attention sink metric Sink₁↑. Here we visualize the locations of these attention sink heads in open-sourced LMs, including LLaMA2 family (Figure 19), LLaMA3/LLaMA3.1 family (Figure 20), Pythia family (Figure 21), Pythia family (Figure 23), and OPT family (Figure 24). We visualize the distributions of importance scores for the first token $\alpha_1^{l,h}$ across different transformer blocks $1 \leq l \leq L$ and different heads $1 \leq h \leq H$ before computing the attention sink metric. We find that (1) different pre-trained LMs have various attention sink distributions but they tend to have less obvious attention sink in earlier transformer blocks; (2) instruction tuning does not significantly modify such attention sink distributions when comparing base versions and instruct versions.

---
[p. 21–25 continued]

**Figure 17** (p. 22): Cosine similarity and $\ell_2$-norm product between keys and queries in Mistral-7B.

Description: Eight heatmap panels arranged in 2 rows and 4 columns, showing attention patterns for different sequence lengths ($l = 5, 10, 19, 31$) and heads ($h = 1$).
- Top row: Heatmaps showing cosine similarity $\cos(q_i^{l,h}, k_j^{l,h})$ with blue diagonal patterns and yellow/green off-diagonal regions marked as "Sink" or "No Sink"
- Bottom row: Heatmaps showing $||q_i^{l,h}|| \cdot ||k_j^{l,h}||$ with purple/blue diagonal patterns and yellow off-diagonal regions
- Key elements: x-axis and y-axis represent token positions, color scales show cosine similarity (-0.2 to 0.6) and norm products (0 to 200)
- Notable patterns: Similar diagonal structure to LLaMA models with varying sink/no-sink patterns
- Supports claim: QK angles contribute to attention sink in Mistral-7B

**Figure 18** (p. 22): Cosine similarity and $\ell_2$-norm product between keys and queries in GPT2-Large.

Description: Eight heatmap panels showing attention patterns for different sequence lengths ($l = 5, 10, 19, 31$) and heads ($h = 1$).
- Top row: Heatmaps showing cosine similarity with blue/cyan diagonal patterns and yellow/green off-diagonal regions
- Bottom row: Heatmaps showing norm products with cyan/green patterns and yellow off-diagonal regions
- Key elements: Similar structure to previous figures with cosine similarity range (-0.75 to 0.0) and norm products (0 to 150)
- Notable patterns: GPT2-Large shows different color patterns with more cyan/green tones, indicating different magnitude ranges
- Supports claim: QK angles contribute to attention sink across different architectures including GPT2-Large

**Figure 19** (p. 22): Distribution of importance scores for the first token across different blocks and heads in the LLaMA2 family.

Description: Four heatmap panels showing importance score distributions for LLaMA2-7B Base, LLaMA2-7B Chat, LLaMA2-13B Base, and LLaMA2-13B Chat.
- Key elements: x-axis shows Head (0-32), y-axis shows Block (0-32), color scale shows importance scores (0.2 to 0.8)
- Notable patterns: Heatmaps show green-yellow coloring with some blue-green regions, indicating varying importance scores across blocks and heads. Similar patterns between Base and Chat versions for same model size.
- Supports claim: Instruction tuning does not significantly modify attention sink distributions when comparing base and instruct versions

**Figure 20** (p. 22): Distribution of importance scores for the first token across blocks and heads in the LLaMA3/LLaMA3.1 family.

Description: Four heatmap panels showing distributions for LLaMA3-8B Base, LLaMA3-8B Instruct, LLaMA3.1-8B Base, and LLaMA3.1-8B Instruct.
- Key elements: x-axis shows Head, y-axis shows Block, color scale shows importance scores (0.2 to 0.8)
- Notable patterns: Green-yellow-blue mosaic patterns with varying intensity across blocks and heads. Consistent patterns between base and instruct versions.
- Supports claim: Similar attention sink distributions across LLaMA3 variants regardless of instruction tuning

**Figure 21** (p. 23): Distribution of importance scores for the first token across blocks and heads in the Mistral family.

Description: Two heatmap panels showing distributions for Mistral-7B and Mistral-7B Instruct.
- Key elements: x-axis shows Head, y-axis shows Block, color scale shows importance scores (0.2 to 0.8)
- Notable patterns: Green-yellow coloring with high consistency between base and instruct versions
- Supports claim: Instruction tuning has minimal impact on attention sink distribution in Mistral models

**Figure 22** (p. 23): Distribution of importance scores for the first token across blocks and heads in the GPT2 family.

Description: Four heatmap panels showing distributions for GPT2, GPT2-Medium, GPT2-Large, and GPT2-XL.
- Key elements: x-axis shows Head, y-axis shows Block, color scale shows importance scores (0.2 to 0.8)
- Notable patterns: Green-blue coloring with some darker blue regions in earlier blocks. Patterns become more pronounced with larger model sizes (GPT2-XL shows more distinct blue regions in earlier layers).
- Supports claim: Different pre-trained LMs have various attention sink distributions but tend to have less obvious attention sink in earlier transformer blocks

**Figure 23** (p. 23): Distribution of importance scores for the first token across blocks and heads in the Pythia family.

Description: Ten heatmap panels showing distributions for Pythia-14M, Pythia-31M, Pythia-70M, Pythia-160M, Pythia-410M, Pythia-1B, Pythia-1.4B, Pythia-2.8B, Pythia-6.9B, and Pythia-12B.
- Key elements: x-axis shows Head, y-axis shows Block, color scale shows importance scores (0.1 to 1.0 for smaller models, 0.2 to 0.8 for larger models)
- Notable patterns: Smaller models (6M-160M) show more varied patterns with purple-yellow coloring. Larger models (410M-12B) show more consistent green-yellow patterns with blue regions in earlier blocks.
- Supports claim: Attention sink distributions vary with model scale, with larger models showing more consistent patterns

**Figure 24** (p. 24): Distribution of importance scores for the first token across blocks and heads in the OPT family.

Description: Six heatmap panels showing distributions for OPT-125M, OPT-350M, OPT-1.3B, OPT-2.7B, OPT-6.7B, and OPT-13B.
- Key elements: x-axis shows Head, y-axis shows Block, color scale shows importance scores (0.2 to 0.6)
- Notable patterns: Green-blue coloring across all sizes with blue regions concentrated in earlier blocks. Consistent pattern across different model scales.
- Supports claim: OPT family shows less obvious attention sink in earlier transformer blocks

### Jamba [p. 24]

Besides the auto-regressive Transformers, we also consider Jamba (Lieber et al., 2024; Team et al., 2024), a new foundation language model. Both Jamba-v0.1 (Lieber et al., 2024) and Jamba-1.5 Mini (Team et al., 2024) have 4 Jamba blocks, which includes 3 Mamba layers (Gu & Dao, 2023), 4 Mamba MoE layers (Shazeer et al., 2017; Fedus et al., 2022), and 1 Transformer layer. This adds to 32 layers (including 4 Transformer layers), with a total of 52B parameters, and 12B active parameters in total. Firstly, we evaluate the attention sink metric and find that Sink₁↑ = 88.48% for Jamba-v0.1 and Sink₁↑ = 87.88% for Jamba-1.5 Mini, which indicates a strong attention sink on the first token. Then we visualize attention scores for several heads, as shown in Figure 25 and Figure 26. We also visualize the distribution of importance scores for the first token across blocks and heads in Jamba models in Figure 27. We observe that most heads have obvious attention sink, except for several heads in the 3rd Transformer layer.

**Figure 25** (p. 24): Attention sink in Jamba-v0.1.

Description: Four triangular heatmap panels showing attention scores for different layers and heads ($l = 1, h = 3$; $l = 2, h = 12$; $l = 3, h = 31$; $l = 4, h = 23$).
- Key elements: Each panel shows a triangular attention matrix with "Sink" marker on the left, color scale from 0.2 to 1.0 in purple-blue tones
- Notable patterns: All four panels show strong diagonal patterns indicating attention sink behavior, with purple coloring at the diagonal and blue in the upper triangle
- Supports claim: Jamba-v0.1 exhibits strong attention sink with Sink₁↑ = 88.48%

**Figure 26** (p. 24): Attention sink in Jamba-1.5 Mini.

Description: Four triangular heatmap panels showing attention scores for different layers and heads ($l = 1, h = 3$; $l = 2, h = 12$; $l = 3, h = 31$; $l = 4, h = 23$).
- Key elements: Similar structure to Figure 25 with triangular attention matrices, color scale from 0.2 to 1.0 in purple-blue tones
- Notable patterns: Consistent diagonal patterns across all panels, similar to Jamba-v0.1
- Supports claim: Jamba-1.5 Mini exhibits strong attention sink with Sink₁↑ = 87.88%

**Figure 27** (p. 25): Distribution of importance scores for the first token across blocks and heads in the Jamba models.

Description: Two horizontal bar-like heatmap panels for Jamba-v0.1 and Jamba-1.5 Mini.
- Key elements: x-axis shows Head, y-axis shows Block (compressed vertical scale), color scale from 0.2 to 0.9 with yellow-green-blue coloring
- Notable patterns: Horizontal bands showing importance scores across heads for each block. Most areas show yellow-green coloring (high importance scores) with some blue-green regions indicating lower scores in certain heads, particularly in the 3rd Transformer layer.
- Supports claim: Most heads have obvious attention sink except for several heads in the 3rd Transformer layer

## C.4 Huggingface links for open-sourced LMs [p. 25]

Table 8: Huggingface links for open-sourced LMs we used in this paper.

| Model | Huggingface link |
|---|---|
| LLaMA2-7B Base | meta-llama/Llama-2-7b-hf |
| LLaMA2-7B Chat | meta-llama/Llama-2-7b-chat-hf |
| LLaMA2-13B Base | meta-llama/Llama-2-13b-hf |
| LLaMA2-13B Chat | meta-llama/Llama-2-13b-chat-hf |
| LLaMA3-8B Base | meta-llama/Meta-Llama-3-8B |
| LLaMA3-8B Instruct | meta-llama/Meta-Llama-3-8B-Instruct |
| LLaMA3.1-8B Base | meta-llama/Meta-Llama-3.1-8B |
| LLaMA3.1-8B Instruct | meta-llama/Meta-Llama-3.1-8B-Instruct |
| GPT2 | openai-community/gpt2 |
| GPT2-Medium | openai-community/gpt2-medium |
| GPT2-Large | openai-community/gpt2-large |
| GPT2-XL | openai-community/gpt2-xl |
| Mistral-7B | mistralai/Mistral-7B-v0.1 |
| Mistral-7B Instruct | mistralai/Mistral-7B-Instruct-v0.1 |
| Pythia-14M | EleutherAI/pythia-14m |
| Pythia-31M | EleutherAI/pythia-31m |
| Pythia-70M | EleutherAI/pythia-70m |
| Pythia-160M | EleutherAI/pythia-160m |
| Pythia-410M | EleutherAI/pythia-410m |
| Pythia-1B | EleutherAI/pythia-1b |
| Pythia-1.4B | EleutherAI/pythia-1.4b |
| Pythia-2.8B | EleutherAI/pythia-2.8b |
| Pythia-6.9B | EleutherAI/pythia-6.9b |
| Pythia-12B | EleutherAI/pythia-12b |
| OPT-125M | facebook/opt-125m |
| OPT-350M | facebook/opt-350m |
| OPT-1.3B | facebook/opt-1.3b |
| OPT-2.7B | facebook/opt-2.7b |
| OPT-6.7B | facebook/opt-6.7b |
| OPT-13B | facebook/opt-13b |
| Jamba-v0.1 | ai21labs/Jamba-v0.1 |
| Jamba-1.5 Mini | ai21labs/AI21-Jamba-1.5-Mini |
