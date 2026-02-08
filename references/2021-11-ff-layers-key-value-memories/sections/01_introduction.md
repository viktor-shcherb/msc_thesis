# 1 Introduction [p. 1-2]

## Motivation

[p. 1] Transformer-based language models (Vaswani et al., 2017) are at the core of state-of-the-art natural language processing (Devlin et al., 2019; Brown et al., 2020), largely due to the success of self-attention. While much literature has been devoted to analyzing the function of self-attention layers (Voita et al., 2019; Clark et al., 2019; Vig and Belinkov, 2019), they account for only a third of a typical transformer's parameters (4d^2 per layer, where d is the model's hidden dimension). Most of the parameter budget is spent on position-wise feed-forward layers (8d^2 per layer), yet their role remains under-explored.

The central research question: What, if so, is the function of feed-forward layers in a transformer language model?

## Key Claims

[p. 1-2] The paper shows that feed-forward layers emulate neural memories (Sukhbaatar et al., 2015), where:

- The first parameter matrix in the layer corresponds to *keys*
- The second parameter matrix corresponds to *values*
- The keys (first parameter matrix) interact with the input to produce coefficients, which are then used to compute a weighted sum of the values (second parameter matrix) as the output

While the theoretical similarity between feed-forward layers and key-value memories has previously been suggested by Sukhbaatar et al. (2019), this paper takes the observation one step further and analyzes the "memories" that the feed-forward layers store.

## Findings

[p. 1-2]

1. **Keys correlate with human-interpretable textual patterns:** Each key correlates with a specific set of human-interpretable input patterns, such as n-grams or semantic topics. For example, k_2 in Figure 1 is triggered by inputs that describe a period of time and end with "a".

2. **Values induce distributions over the output vocabulary:** Each value can induce a distribution over the output vocabulary, and this distribution correlates with the next-token distribution of the corresponding keys in the upper layers. For example, the corresponding value v_2 represents a distribution that puts most of its probability mass on the word "while".

3. **Lower layers capture shallow patterns, upper layers capture semantic ones.**

4. **Final output is a composition of memories:** Each layer combines hundreds of active memories, creating a distribution that is qualitatively different from each of its component memories' values. The residual connection between layers acts as a refinement mechanism, gently tuning the prediction at each layer while retaining most of the residual's information.

5. **Output distribution is gradually constructed in a bottom-up fashion.**

**Figure 1** (p. 1): "An illustration of how a feed-forward layer emulates a key-value memory. Input vectors (here, x_5) are multiplied by keys to produce memory coefficients (e.g., the memory coefficient for v_1 is 0.2), which then weigh distributions over the output vocabulary, stored in the values. The feed-forward layer's output is thus the weighted sum of its values."

The figure shows the architecture with input tokens "Stay with you for a" at the bottom, passing through Transformer layers and a self-attention layer, producing representations x_1 through x_5. The FF layer processes x_5: keys k_1 through k_{d_m} produce memory coefficients (e.g. 0.2 for v_1, 1.5 for v_2, ..., 0 for v_{d_m}), which weight the value vectors v_1 through v_{d_m}. The value v_2 is shown containing text snippets like "it will take a", "every once in a", "and for a", and the output distribution highlights "while".

Footnote 1 [p. 2]: The code for reproducing experiments is available at https://github.com/mega002/ff-layers/.
