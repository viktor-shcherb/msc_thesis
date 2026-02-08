# 8.5 Speech Generation Results [p. 67–69]

[p. 67] For speech generation, the focus is on evaluating the quality of token-wise input streaming models with the Llama 3 embeddings for the text normalization and prosody modeling tasks. The evaluation focuses on comparisons with models that do not take the Llama 3 embeddings as an additional input. [p. 68]

## Text Normalization

[p. 68] **Text normalization.** To measure the effect of Llama 3 embeddings, experiments are conducted with changing the amount of right context the model uses. The model is trained using a right context of 3 TN tokens (demarcated by unicode category). This model is compared to models that do not use the Llama 3 embeddings, using a 3-token right context or a full bi-directional context. As expected, Table 34 shows using the full right context improves performance for the model without Llama 3 embeddings. However, the model that incorporates the Llama 3 embeddings outperforms all other models, hence enabling token-rate input/output streaming without relying on long context in the input. [p. 68]

**Table 34** Sample-wise text normalization (TN) accuracy. We compare models with or without Llama 3 8B embeddings, and using different right-context values. [p. 68]

| Model | Context | Accuracy |
|---|---|---|
| Without Llama 3 8B | 3 | 73.6% |
| Without Llama 3 8B | ∞ | 88.0% |
| With Llama 3 8B | 3 | **90.7%** |

## Prosody Modeling

[p. 68] **Prosody modeling.** To evaluate the performance of the prosody model (PM) with Llama 3 8B, two sets of human evaluation are conducted comparing models with and without Llama 3 embeddings. Raters listened to samples from different models and indicated their preferences. To generate the final speech waveform, an in-house transformer based acoustic model (Wu et al., 2021) that predicts spectral features and a WaveRNN neural vocoder (Kalchbrenner et al., 2018) are used to generate the final speech waveform. [p. 68]

First, a direct comparison is made to a streaming baseline model without Llama 3 embeddings. In the second test, the Llama 3 8B PM is compared to a non-streaming baseline model without Llama 3 embeddings. As shown in Table 35, the Llama 3 8B PM is preferred 60% of the time compared to the streaming baseline, and 63.6% of the time compared to the non-streaming baseline, indicating a significant improvement in perceived quality. [p. 69]

The key advantage of the Llama 3 8B PM is its token-wise streaming capability (Section 8.2.2), which maintains low latency during inference. This reduces the model's lookahead requirements, enabling more responsive and real-time speech synthesis compared to non-streaming baselines. Overall, the Llama 3 8B prosody model consistently outperforms the baseline models, demonstrating its effectiveness in enhancing the naturalness and expressiveness of synthesized speech. [p. 69]

**Table 35** Prosody Modeling (PM) evaluation. *Left:* Rater preferences of PM for Llama 3 8B vs. streaming phone-only baseline. *Right:* Rater preferences of PM for Llama 3 8B vs. non-streaming phone-only baseline. [p. 69]

| Model | Preference | | Model | Preference |
|---|---|---|---|---|
| PM for Llama 3 8B | **60.0%** | | PM for Llama 3 8B | **63.6%** |
| Streaming phone-only baseline | 40.0% | | Non-streaming phone-only baseline | 36.4% |
