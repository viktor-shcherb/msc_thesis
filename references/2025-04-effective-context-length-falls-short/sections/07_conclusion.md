# 6 Conclusion [p. 11]

[p. 11]

This work uncovers the limitations of current open-source large language models in effectively utilizing their extended training context windows. We show that using positions at the tail of the left-skewed position frequency distributions strongly impedes models' long-range dependency modeling ability. We introduce STRING, a novel approach that shifts well-trained positions to replace ineffective ones during inference, thereby enhancing the ability to capture contextual information without requiring additional training. Our experiments demonstrate that STRING significantly boosts the performance of strong baselines like Llama 3.1 70B and Qwen2 72B on prominent long-context benchmarks, setting new state-of-the-art results for open-source LLMs.
