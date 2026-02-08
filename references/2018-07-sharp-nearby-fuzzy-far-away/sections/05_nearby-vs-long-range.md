# 5 Nearby vs. long-range context [p. 4-6]

An effective context size of 200 tokens allows for representing linguistic information at many levels of abstraction, such as words, sentences, topics, etc. This section investigates the importance of contextual information such as word order and word identity. Unlike prior work that studies LSTM embeddings at the sentence level, the authors look at both nearby and faraway context, and analyze how the language model treats contextual information presented in different regions of the context. [p. 4]

## 5.1 Does word order matter? [p. 4-5]

Adi et al. (2017) have shown that LSTMs are aware of word order within a sentence. The authors investigate whether LSTM language models are sensitive to word order within a larger context window. To determine the range in which word order affects model performance, they permute substrings in the context to observe their effect on dev loss compared to the unperturbed baseline. [p. 4]

The context perturbation is defined as:

$$\delta_{\text{permute}}(w_{t-1}, \ldots, w_{t-n}) = (w_{t-1}, .., \rho(w_{t-s_1-1}, .., w_{t-s_2}), .., w_{t-n}) \quad (2)$$

where $\rho \in \{\text{shuffle, reverse}\}$ and $(s_1, s_2]$ denotes the range of the substring to be permuted, referred to as the *permutable span*. [p. 4]

They distinguish *local word order* (within 20-token permutable spans, about the length of an average sentence) from *global word order* (which extends beyond local spans to include all the farthest tokens in the history). Permutable spans are selected within a context of $n = 300$ tokens, greater than the effective context size. [p. 5]

**Local word order only matters for the most recent 20 tokens.** They locate the region of context beyond which local word order has no relevance, by permuting word order locally at various points within the context. They set $s_2 = s_1 + 20$. [p. 5]

**Figure 2a** (p. 5): Shows that local word order matters very much within the most recent 20 tokens, and far less beyond that.

- X-axis: Distance of perturbation from target (number of tokens), values: 1, 5, 10, 15, 20, 30, 50, 100, 200
- Y-axis: Increase in Loss, range 0.0-3.0
- Four curves: Shuffle 20 token windows PTB, Reverse 20 token windows PTB, Shuffle 20 token windows Wiki, Reverse 20 token windows Wiki
- Sharp drop from distance 1 to 20; near zero beyond 20 tokens

**Global order of words only matters for the most recent 50 tokens.** They locate the point beyond which the general location of words within the context is irrelevant, by permuting global word order. They set $s_2 = n$. [p. 5]

**Figure 2b** (p. 5): After 50 tokens, shuffling or reversing the remaining words in the context has no effect on the model performance.

- X-axis: Distance of perturbation from target (number of tokens), same scale as 2a
- Y-axis: Increase in Loss, range 0.0-3.0
- Three curves (Wiki only): Shuffle entire context, Reverse entire context, Replace context with random sequence
- Shuffle and Reverse curves drop to near zero by distance 50
- Replace curve remains higher than shuffle/reverse at all distances, showing the gap between permutation and replacement

To determine whether insensitivity to word order is due to the language model simply not being sensitive to any changes in the long-range context, they further replace words in the permutable span with a randomly sampled sequence of the same length from the training set. The gap between the permutation and replacement curves in Figure 2b illustrates that the identity of words in the far away context is still relevant, and only the order of the words is not. [p. 5]

**Discussion.** Word order matters only within the most recent sentence, beyond which the order of sentences matters for 2-3 sentences (determined by experiments on global word order). After 50 tokens, word order has almost no effect, but the identity of those words is still relevant, suggesting a high-level, rough semantic representation for these faraway words. They define 50 tokens as the boundary between nearby and long-range context for the rest of the study. [p. 5]

## 5.2 Types of words and the region of context [p. 5-6]

Open-class or *content words* such as nouns, verbs, adjectives and adverbs contribute more to the semantic context of natural language than *function words* such as determiners and prepositions. Given the observation that the language model represents long-range context as a rough semantic representation, the question is how important function words are in the long-range context. Function words are defined as all words that are not nouns, verbs, adjectives or adverbs. [p. 5-6]

**Content words matter more than function words.** To study the effect of content and function words on model perplexity, they drop them from different regions of the context and compare the resulting change in loss. The perturbation: [p. 6]

$$\delta_{\text{drop}}(w_{t-1}, \ldots, w_{t-n}) = (w_{t-1}, .., w_{t-s_1}, f_{\text{pos}}(y, (w_{t-s_1-1}, .., w_{t-n}))) \quad (3)$$

where $f_{\text{pos}}(y, \text{span})$ is a function that drops all words with POS tag $y$ in a given span. $s_1$ denotes the starting offset of the perturbed subsequence. For these experiments, $s_1 \in \{5, 20, 100\}$. [p. 6]

On average, there are slightly more content words than function words in any given text. As shown in Section 4, dropping more words results in higher loss. To eliminate the effect of dropping different fractions of words, for each experiment where they drop a specific word type, they add a control experiment where the same number of tokens are sampled randomly from the context and dropped. [p. 6]

**Figure 3** (p. 6): Effect of dropping content and function words from 300 tokens of context relative to an unperturbed baseline, on PTB. Error bars represent 95% confidence intervals.

- X-axis: Distance of perturbation from target (number of tokens), values: 5, 20, 100
- Y-axis: Increase in Loss, range 0.0-0.5
- Four bars at each distance: Drop all content words (52.6%), Drop all function words (47.4%), Random drop 52.6% tokens of 300, Random drop 47.4% tokens of 300
- At distance 5: content word drop causes ~0.48 increase, much larger than ~0.28 for function words
- At distance 20: content word drop still higher than function words, but gap narrows
- At distance 100: only content words remain relevant

Dropping content words as close as 5 tokens from the target word increases model perplexity by about 65%, whereas dropping the same proportion of tokens at random results in a much smaller 17% increase. Dropping all function words is not very different from dropping the same proportion of words at random, but still increases loss by about 15%. [p. 6]

This suggests that within the most recent sentence, content words are extremely important but function words are also relevant since they help maintain grammaticality and syntactic structure. Beyond a sentence, only content words have a sizeable influence on model performance. [p. 6]
