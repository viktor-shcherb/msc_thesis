# 1. Introduction [p. 1-2]

[p. 1] LLMs, despite remarkable success on various tasks (OpenAI et al., 2023; Touvron et al., 2023), often suffer from limited context window size, e.g., LLaMA2's 4096 token limit (Touvron et al., 2023). Beyond the context window, LLM's performance declines due to the additional positions the model has not been trained on. This poses challenges in important scenarios like in-context learning with numerous examples (Huang et al., 2023) and LLM agents (Park et al., 2023; Madaan et al., 2023).

Recent works show that a pre-trained LLM context window can be extended to around 128k by fine-tuning on longer texts (Chen et al., 2023b;a; Peng et al., 2023; Zhang et al., 2024; Liu et al., 2023). Three major obstacles to further extend the context window:

1. **Untrained new position indices** introduce many catastrophic values, leading to out-of-distribution issues and making fine-tuning difficult to converge (Chen et al., 2023a). Particularly challenging when an extension from 4k to >1000k introduces more than 90% new positions.
2. **Fine-tuning requires texts of corresponding lengths.** Long texts in current datasets, especially those exceeding 1000k, are limited. Training on extra-long texts is computationally expensive, requiring prohibitively extensive training hours and GPU resources.
3. **Attention becomes dispersed** when extending to extremely long context windows, as it's spread thinly across numerous token positions, degrading performance on the original short context (Chen et al., 2023a).

One approach to mitigate the first challenge is to interpolate RoPE positional embedding (Su et al., 2021; Chen et al., 2023a), which downscales new position indices to the pre-trained range, as shown in Fig. 2. Position Interpolation (PI) (Chen et al., 2023a) linearly interpolates RoPE's rotary angles by the extension ratio. NTK (LocalLLaMA, 2023b;a) advocates unequal interpolation and extrapolation across RoPE dimensions. YaRN (Peng et al., 2023) categorizes RoPE dimensions into three frequency-based groups and applies extrapolation, NTK, and linear interpolations, respectively. However, positional embedding exhibits *complex non-uniform information entropy* in the Transformer architecture. Such subtle non-uniformity is not effectively leveraged by existing approaches, leading to information loss and hence limiting the context window size.

[p. 2] Section 2 reveals two key findings empirically: **(1)** Effective positional interpolation should consider two forms of non-uniformities: varying RoPE dimensions and token positions. Lower RoPE dimensions and initial starting token positions benefit from less interpolation, but the optimal solutions depend on the target extended length. **(2)** By considering these non-uniformities into positional interpolation, one can effectively retain information in the original RoPE, particularly key dimensions and token positions. This minimizes the loss caused by positional interpolation, and thus provides better initialization for fine-tuning. Moreover, it allows an 8x extension in non-fine-tuning scenarios.

Motivated by the findings, the authors introduce **LongRoPE**, an effective method that extends the LLM context window beyond 2 *million* tokens. LongRoPE is based on three key innovations:

1. **Non-uniform positional interpolation search.** LongRoPE fully exploits multidimensional non-uniformities in positional interpolation. It identifies effective rescale factors for RoPE's rotation angles for each RoPE dimension, based on token positions. An evolutionary search algorithm with two optimization techniques boosts search efficiency. Fig. 2 shows an example of the searched rescaled RoPE.

2. **Progressive extension strategy.** LongRoPE leverages an efficient, progressive extension strategy to achieve a 2048k context window without the need for direct fine-tuning on texts with extremely long lengths, which are scarce and hardly available. The strategy begins by searching for a 256k length on the pre-trained LLM and fine-tuning it under this length. Then, as non-uniform positional interpolation allows for an 8x extension in non-fine-tuning settings, a second search for new RoPE rescale factors on the fine-tuned extended LLM is conducted. This ultimately achieves the 2048k context window for LLaMA2 and Mistral (Jiang et al., 2023).

3. **Short context window recovery.** To mitigate performance degradation on the original (shorter) context window, LongRoPE continues to adjust the RoPE rescale factors on the extended LLM. Similar to scaling up from 256k to 2048k, they scale down to 4k and 8k context windows on the 256k fine-tuned LLM using the search algorithm to encourage less positional interpolation. During inference, if the sequence length is less than 8k, they update RoPE with the searched rescale factors.

Extensive experiments across different LLMs and various long-context tasks demonstrate the effectiveness of the method. LongRoPE is highly effective in maintaining low perplexity from 4k to 2048k evaluation length, achieving over 90% passkey retrieval accuracy, and delivering comparable accuracy on standard benchmarks designed within the 4096 context window. LongRoPE can be applied to any LLMs based on RoPE embedding.

**Figure 1** (p. 1): "Books3 perplexity comparison between LongRoPE and state-of-the-art long-context LLMs using other extension methods."

The figure is a line plot with Context Window Size on the x-axis (8k to 2048k, log scale) and Perplexity on the y-axis (0 to 100). Lines shown:
- LongLoRA-7B-100k: perplexity spikes sharply around 100k
- Code LLaMA-7B-100k: perplexity spikes sharply around 100k
- YaRN-LLaMA2-7B-64k: perplexity spikes around 64k
- YaRN-LLaMA2-7B-128k: perplexity spikes around 128k
- **LongRoPE-LLaMA2-7B-2048k**: maintains low perplexity (~5-7) all the way to 2048k
- Mistral-7B (8k): baseline, low perplexity at 8k
- YaRN-Mistral-7B-64k: spikes after 64k
- YaRN-Mistral-7B-128k: spikes after 128k
- **LongRoPE-Mistral-7B-2048k**: maintains low perplexity through 2048k

The figure demonstrates that LongRoPE models are the only ones that maintain stable low perplexity at context windows beyond 128k, up to 2048k.
