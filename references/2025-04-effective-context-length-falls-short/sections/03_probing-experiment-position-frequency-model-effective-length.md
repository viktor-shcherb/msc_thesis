# 3 A Probing Experiment on Position Frequency and Model Effective Length [p. 4–5]

[p. 4]

In this section, we empirically investigate the impact of the left-skewed position frequency distribution on the effective context length of LLMs. Since the training data distributions for most open-source LLMs are opaque and cannot be directly analyzed by external researchers, this study represents the first exploration of the impact of position frequency during the pretraining stage.

## Evaluation [p. 4]

To measure the effective context length, we adopt the popular Needle-in-a-Haystack task (gkamradt, 2023). We use the 4-needle test, the same as described in the Llama 3.1 report (Llama Team, 2024), which involves inserting four needles (6-digit numbers (Hsieh et al., 2024; Mohtashami & Jaggi, 2023)) into the context at four random positions. The model is required to retrieve at least two of them. The input examples used in this experiment can be found in Table 3 of the Appendix. The examples are given in 128-token steps until the model fails to correctly retrieve at least two of the four inserted needles. We perform 500 tests at each length.

## Experimental Setup [p. 4]

We pretrain two 1.3B-parameter models (referred to as TinyLlama-1.3B) from scratch on the natural data distribution of the SlimPajama dataset to observe changes in the model's effective length. The total training tokens are 1T and we evaluate the model's effective context length for every 10B tokens during training. Both models begin to exhibit needle-retrieval ability after about 50B tokens of training. To measure the critical position frequency is difficult to control directly, we perform controlled experiments by adjusting two factors: (1) consumed tokens, and (2) the training context window size. The first factor is straightforward. For the second factor, we illustrate the position frequency distribution after training with 1T tokens using different training lengths (2K and 4K) in Figure 3. The configuration of our pretraining codebase and models is detailed in Section A.2.

**Figure 2** (p. 4): "Analyzing effective context length of LLMs pretrained on SlimPajama with respect to training length, token consumption, and position frequency. In Figure 2b, we use the model effective length as the X-axis, and the Y-axis indicates the number of times the model was exposed to that specific position during training."

Description: Two line charts
- Key elements: (a) Shows effective length vs. consumed tokens with two lines for SlimPajama-1.3B-2k and SlimPajama-1.3B-4k. X-axis ranges from 0 to 1000B consumed tokens, Y-axis shows effective length. (b) Shows effective length vs. position frequency. X-axis shows effective length from 256 to 2048, Y-axis shows position frequency (log scale).
- Notable patterns: (a) Both models show increasing effective length with more consumed tokens, with 4K training length achieving higher effective length. (b) Shows strong correlation between position frequency during training and effective length achieved.
- Supports claim: Models can achieve similar effective context lengths when exposed to similar frequencies of position indices, even if their maximum training lengths differ.

## Findings [p. 5]

Following previous work (Kaplan et al., 2020), we demonstrate how the models' effective length grows with increasing training tokens for two different training lengths (*Finding (1)*), while our further analysis reveals that the underlying factor (*Findings (2) and (3)*).

**(1) Larger training context window consumes fewer tokens to achieve the same effective context length:** In Figure 2a, a notable observation is that doubling the training length no longer sequences results in a greater effective context length when the same number of tokens is consumed. Specifically, the model trained with a sequence length of 4K tokens achieves an effective context length of 1.4K after consuming 400B tokens. In contrast, the model trained with a 2K training length needs around 1T tokens to attain the same effective context length.

**(2) Models can achieve similar effective context lengths if they have been exposed to similar frequencies of position indices, even if their maximum training lengths differ:** By directly plotting the effective context length against the frequency of position indices used to model that length (Figure 2b), we observe that the growth trends of effective lengths for different models align when the position frequency distribution is similar. The X-axis represents the frequency of indices at that length. For instance, when the effective length reaches 1,280 tokens, both models exhibit a position frequency f(1280) of 100B. This indicates that models can attain comparable effective context lengths when they have been trained on similar frequencies of position indices, regardless of differences in their maximum training lengths.

**Figure 3** (p. 5): "Position frequency distribution for models trained with different training lengths after consuming 1T tokens. With the same number of tokens, training length has little effect on small relative positions. For example, the relative position 0 appears 4K times in both a single sequence and in two 2K sequences with the same total token count of 4K in each case."

Description: Bar chart showing position frequency distribution
- Key elements: X-axis shows position indices from 0 to beyond 3×10³, Y-axis shows position frequency. Two sets of bars for Training Length 4K (blue) and Training Length 2K (orange).
- Notable patterns: For small position indices (i ≤ 1024), both training lengths show nearly identical frequencies. As position index i continues to increase, the frequency gap between models trained with 4K and 2K context lengths becomes increasingly larger. Both models consume roughly the same number of tokens (around 300B) when reaching an effective length of 1024.
- Supports claim: The growth trend of the model's effective length aligns with the position frequency distribution.

**(3) The growth trend of the model's effective length aligns with the position frequency distribution:** In Figure 3, we observe that models with different training lengths have close position frequencies for i ≤ 1024. As i continues to increase, the frequency gap between models trained with 4K and 2K context lengths becomes increasingly larger. The growth rates of their effective lengths also align with this trend (Figure 2). Both models consume roughly the same number of tokens (around 300B) when reaching an effective length of 1024. However, as the effective length increases further, the growth rate of the model pretrained with a 2K context window becomes significantly slower.

## Limitations in Gathering Distant Inputs [p. 5]

We visualize the performance of infrequent positions with the Needle-in-a-Haystack (4-needle) test (gkamradt, 2023). The distance between the query and the needles increases as the depth becomes smaller and the testing context length becomes longer. The results indicate that when the needle depth is high, both TinyLlama.1.3B and the latest Llama3.1 8B model fail to retrieve the needle effectively. In Figure 4, when we place the query at the end of the document, we find that needles close to the query can be recovered from the *beginning* of the document. Concretely, in Llama3.1, performance significantly degrades when position indices exceed 90K. TinyLlama struggles to gather information when the distance exceeds 1,536 tokens. We also evaluate 13 models from the open-source community, as shown in Table 4, and find that most failure cases occur within the first ⅔ of the document. This may indicate that the last ⅓ positions of current LLMs all fall in the tail of the position frequency distribution.
