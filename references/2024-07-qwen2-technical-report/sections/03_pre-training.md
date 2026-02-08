# Pre-training [p. 5-6]

[p. 5] In the pre-training of Qwen2, efforts were focused on refining the dataset and investigating methods to handle extended context lengths effectively.

## Pre-training Data [p. 5-6]

[p. 5] The pre-training of the Qwen2 models involves the development of a new, large-scale, high-quality multilingual dataset, representing an improvement over the corpora used in previous Qwen and Qwen1.5 models (Bai et al., 2023a; Qwen Team, 2024a), enhancing the scale, quality, and diversity of the pre-training data in several key areas:

**Quality Enhancement** [p. 5]: The filtering algorithm has been refined with additional heuristic and model-based methods, including the use of the Qwen models to filter out low-quality data. Moreover, these models are utilized to synthesize high-quality pre-training data.

**Data Expansion** [p. 6]: Compared to Qwen1.5 (Qwen Team, 2024a), a significantly larger volume of high-quality code, mathematics, and multilingual data has been collected, enhancing the model's capabilities in respective areas. The new dataset supports **approximately 30 languages**, such as English, Chinese, Spanish, French, German, Arabic, Russian, Korean, Japanese, Thai, and Vietnamese.

**Distribution Improvement** [p. 6]: Experiments on scaled-down models are conducted to optimize the mixing of data from various sources and domains, to ensure the model learns the distribution akin to human-like learning.

[p. 6] Based on these enhancements, the pre-training data was expanded from **3 trillion tokens in Qwen1.5** (Qwen Team, 2024a) to **7 trillion tokens**. An attempt to further relax the quality threshold resulted in a 12 trillion token dataset. However, the model trained on this dataset did not show a significant performance improvement over the 7 trillion token model. It is suspected that increasing the volume of data does not necessarily benefit model pre-training. Considering training costs, the authors opted to use the higher-quality 7 trillion token dataset for training larger models, leaving further exploration for future model iterations.

All Qwen2 dense models, excluding Qwen2-0.5B, were pre-trained on this large-scale dataset of over 7 trillion tokens. **Qwen2-0.5B was pre-trained using the 12 trillion token dataset.** The MoE model received an additional **4.5 trillion tokens** of pre-training, in line with the principle of upcycling. Similar to previous Qwen models, high-quality multi-task instruction data is integrated into the Qwen2 pre-training process to enhance in-context learning and instruction-following abilities.

## Long-context Training [p. 6]

[p. 6] To enhance the long-context capability of Qwen2, the context length was augmented from **4,096 tokens to 32,768 tokens** during the concluding phase of pre-training. This expansion was complemented by the introduction of a significantly increased volume of high-quality, lengthy data. In conjunction with these enhancements, the base frequency of RoPE was modified from **10,000 to 1,000,000** to optimize performance in long-context scenarios (Xiong et al., 2023).

To fully leverage the model's length extrapolation potential, the YARN mechanism (Peng et al., 2023) and the Dual Chunk Attention mechanism (An et al., 2024) were adopted. These strategies enable the model to process sequences of up to **131,072 tokens** while maintaining high performance, as evidenced by minimal perplexity degradation in preliminary experiments.
