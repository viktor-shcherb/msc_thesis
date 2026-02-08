# 5. Conclusion, Limitation, and Future Work [p. 21]

[p. 21] DeepSeek-V2 is introduced as a large MoE language model that supports 128K context length. In addition to strong performance, it is characterized by economical training and efficient inference, benefiting from its innovative architecture including MLA and DeepSeekMoE. In practice, compared with DeepSeek 67B, DeepSeek-V2 achieves significantly stronger performance, and meanwhile saves 42.5% of training costs, reduces the KV cache by 93.3%, and boosts the maximum generation throughput to 5.76 times. Evaluation results further demonstrate that with only 21B activated parameters, DeepSeek-V2 achieves top-tier performance among open-source models and becomes the strongest open-source MoE model.

## Limitations

[p. 21] DeepSeek-V2 and its chat versions share the acknowledged limitations commonly found in other LLMs, including:
- The lack of ongoing knowledge updates after pre-training
- The possibility of generating non-factual information such as unverified advice
- A chance to produce hallucinations
- Since the data primarily consists of Chinese and English content, the model may exhibit limited proficiency in other languages. In scenarios beyond Chinese and English, it should be used with caution.

## Future Work

[p. 21] DeepSeek will continuously invest in open-source large models with longtermism, aiming to progressively approach the goal of artificial general intelligence. Specific directions:

- **Scaling up MoE models:** Ongoing exploration is dedicated to devising methods that enable further scaling up MoE models while maintaining economical training and inference costs. The goal of their next step is to achieve performance on par with GPT-4 in their upcoming release.
- **Alignment:** The alignment team continuously strives to enhance the models, aiming to develop a model that is not only helpful but also honest and safe for worldwide users. The ultimate objective is to align the values of the model with human values, while minimizing the need for human supervision. By prioritizing ethical considerations and responsible development, they are dedicated to creating a positive and beneficial impact on society.
- **Multi-modality:** Currently, DeepSeek-V2 is designed to support the text modality exclusively. In their forward-looking agenda, they intend to enable the model to support multiple modalities, enhancing its versatility and utility in a wider range of scenarios.
