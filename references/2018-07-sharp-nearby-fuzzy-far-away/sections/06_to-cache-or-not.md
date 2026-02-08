# 6 To cache or not to cache? [p. 6]

As shown in Section 5.1, LSTM language models use a high-level, rough semantic representation for long-range context, suggesting that they might not be using information from any specific words located far away. Adi et al. (2017) have also shown that while LSTMs are aware of which words appear in their context, this awareness degrades with increasing length of the sequence. However, the success of copy mechanisms such as attention and caching (Bahdanau et al., 2015; Hill et al., 2016; Merity et al., 2017; Grave et al., 2017a,b) suggests that information in the distant context is very useful. [p. 6]

Given this fact, can LSTMs copy any words from context without relying on external copy mechanisms? Do they copy words from nearby and long-range context equally? How does the caching model help? [p. 6]

The authors investigate these questions by studying how LSTMs copy words from different regions of context. They look at two regions: nearby (within 50 most recent tokens) and long-range (beyond 50 tokens), and study three categories of target words: [p. 6]

- $C_{\text{near}}$: words that can be copied from nearby context
- $C_{\text{far}}$: words that can *only* be copied from long-range context
- $C_{\text{none}}$: words that cannot be copied at all given a limited context

## 6.1 Can LSTMs copy words without caches? [p. 6]

Even without a cache, LSTMs often regenerate words that have already appeared in prior context. The authors investigate how much the model relies on the previous occurrences of the upcoming target word, by analyzing the change in loss after dropping and replacing this target word in the context. [p. 6]

**LSTMs can regenerate words seen in nearby context.** To demonstrate the usefulness of target word occurrences in context, they experiment with dropping all the distant context versus dropping only occurrences of the target word from the context. They compare removing all tokens after the 50 most recent tokens (Equation 1 with $n = 50$), versus removing only the target word, in context of size $n = 300$: [p. 7]

$$\delta_{\text{drop}}(w_{t-1}, \ldots, w_{t-n}) = f_{\text{word}}(w_t, (w_{t-1}, \ldots, w_{t-n})), \quad (4)$$

where $f_{\text{word}}(w, \text{span})$ drops words equal to $w$ in a given span. They compare applying both perturbations to a baseline model with unperturbed context restricted to $n = 300$. They also include the target words that never appear in the context ($C_{\text{none}}$) as a control set for this experiment. [p. 7]

The results show that LSTMs rely on the rough semantic representation of the faraway context to generate $C_{\text{far}}$, but directly copy $C_{\text{near}}$ from the nearby context. [p. 7]

**Figure 4a** (p. 7): "Dropping tokens" -- Effects of perturbing the target word in the context compared to dropping long-range context altogether, on PTB. Error bars represent 95% confidence intervals. Words that can only be copied from long-range context are more sensitive to dropping all the distant words than to dropping the target. For words that can be copied from nearby context, dropping only the target has a much larger effect on loss compared to dropping the long-range context.

- X-axis: First occurrence of target in context (nearby, long-range, none (control set))
- Y-axis: Increase in Loss, range 0.00-0.12
- Two bar groups: Drop 250 most distant tokens (red), Drop only target (dark red)
- For "nearby" ($C_{\text{near}}$): dropping target (~0.08) > dropping distant tokens (~0.03)
- For "long-range" ($C_{\text{far}}$): dropping distant tokens (~0.10) > dropping target (~0.02)
- For "none" ($C_{\text{none}}$): both perturbations have small effects (~0.03-0.04)

In Figure 4a, the long-range context bars show that for words that can only be copied from long-range context ($C_{\text{far}}$), removing all distant context is far more disruptive than removing only occurrences of the target word (12% and 2% increase in perplexity, respectively). This suggests the model relies more on the rough semantic representation of faraway context to predict these $C_{\text{far}}$ tokens, rather than directly copying them from the distant context. [p. 7]

On the other hand, for words that can be copied from nearby context ($C_{\text{near}}$), removing all long-range context has a smaller effect (about 3.5% increase in perplexity) as seen in Figure 4a, compared to removing the target word which increases perplexity by almost 9%. This suggests that these $C_{\text{near}}$ tokens are more often copied from nearby context, than inferred from information found in the rough semantic representation of long-range context. [p. 7]

**Replacing target words with other tokens.** To test whether dropping the target tokens altogether hurts the model too much by adversely affecting grammaticality, they replace target words in the context with other words from the vocabulary. This perturbation is similar to Equation 4, except instead of dropping the token, they replace it with a different one. They experiment with replacing the target with `<unk>`, and also replacing it with a word that has the same part-of-speech tag and a similar frequency in the dataset. [p. 7]

**Figure 4b** (p. 7): "Perturbing occurrences of target word in context" -- Error bars represent 95% confidence intervals. Replacing the target word with other tokens from vocabulary hurts more than dropping it from the context, for words that can be copied from nearby context, but has no effect on words that can only be copied from far away.

- X-axis: First occurrence of target in context (nearby, long-range)
- Y-axis: Increase in Loss, range 0.00-0.14
- Three bar groups: Drop only target (red), Replace with `<unk>` (lighter red), Replace target with similar token (lightest red)
- For "nearby" ($C_{\text{near}}$): Replace with similar token (~0.12-0.13) > Replace with `<unk>` (~0.10) > Drop only target (~0.08)
- For "long-range" ($C_{\text{far}}$): all three perturbations have similar small effects (~0.02)

Replacing the target with other words results in up to a 14% increase in perplexity for $C_{\text{near}}$, which suggests that the replacement token seems to confuse the model far more than when the token is simply dropped. However, the words that rely on the long-range context, $C_{\text{far}}$, are largely unaffected by these changes, which confirms the conclusion from dropping the target tokens: $C_{\text{far}}$ words are predicted from the rough representation of faraway context instead of specific occurrences of certain words. [p. 8]

## 6.2 How does the cache help? [p. 8-9]

If LSTMs can already regenerate words from nearby context, how are copy mechanisms helping the model? The authors answer this by analyzing how the neural cache model (Grave et al., 2017b) helps with improving model performance. The cache records the hidden state $h_t$ at each timestep $t$, and computes a cache distribution over the words in the history as follows: [p. 8]

$$P_{\text{cache}}(w_t | w_{t-1}, \ldots, w_1; h_t, \ldots, h_1) \propto \sum_{i=1}^{t-1} \mathbb{1}[w_i = w_t] \exp(\theta h_i^T h_t), \quad (5)$$

where $\theta$ controls the flatness of the distribution. This cache distribution is then interpolated with the model's output distribution over the vocabulary. Consequently, certain words from the history are upweighted, encouraging the model to copy them. [p. 8]

**Caches help words that can be copied from long-range context the most.** To study the effectiveness of the cache for the three classes of words ($C_{\text{near}}, C_{\text{far}}, C_{\text{none}}$), they evaluate an LSTM language model with and without a cache, and measure the difference in perplexity for these words. In both settings, the model is provided all prior context (not just 300 tokens) in order to replicate the Grave et al. (2017b) setup. The amount of history recorded, known as the cache size, is a hyperparameter set to 500 past timesteps for PTB and 3,875 for Wiki, both values very similar to the average document lengths in the respective datasets. [p. 8]

**Figure 7** (p. 8): "Model performance relative to using a cache." Error bars represent 95% confidence intervals. Words that can only be copied from the distant context benefit the most from using a cache.

- Two panels: Dataset = PTB, Cache size = 500 words (left); Dataset = Wiki, Cache size = 3,875 words (right)
- X-axis: First occurrence of target in context (nearby, long-range, none)
- Y-axis: Increase in Loss, range roughly -0.1 to 0.4
- For PTB: $C_{\text{near}}$ ~0.22 increase; $C_{\text{far}}$ ~0.28 increase; $C_{\text{none}}$ negative (cache hurts)
- For Wiki: $C_{\text{near}}$ ~0.32 increase; $C_{\text{far}}$ ~0.53 increase; $C_{\text{none}}$ negative (cache hurts)

The cache helps words that can only be copied from long-range context ($C_{\text{far}}$) more than words that can be copied from nearby ($C_{\text{near}}$). Without caching, $C_{\text{near}}$ words see a 22% increase in perplexity for PTB, and a 32% increase for Wiki, whereas $C_{\text{far}}$ see a 28% increase in perplexity for PTB, and a 53% increase for Wiki. The cache is complementary to the standard model, since it especially helps regenerate words from the long-range context where the latter falls short. [p. 8-9]

However, the cache also hurts about 36% of the words in PTB and 20% in Wiki, which are words that cannot be copied from context ($C_{\text{none}}$), as illustrated by bars for "none" in Figure 7. [p. 9]

**Figure 5** (p. 8): "Success of neural cache on PTB." Brightly shaded region shows peaky distribution. Shows an example where the cache distribution is concentrated on a single word that it wants to copy. [p. 8]

**Figure 6** (p. 8): "Failure of neural cache on PTB." Lightly shaded regions show flat distribution. When the target is not present in the history, the cache distribution is more flat, illustrating the model's confusion. This suggests that the neural cache model might benefit from having the option to ignore the cache when it cannot make a confident choice. [p. 9]
