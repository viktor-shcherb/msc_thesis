# 7 Conclusion [p. 10]

[p. 10] The authors propose a memory efficient approach to reduce the memory requirements of Transformers, the backbone of state-of-the-art AI models. The approach allows the context length to scale linearly with the number of devices while maintaining performance, eliminating the memory bottleneck imposed by individual devices. Through extensive experiments on language modeling and reinforcement learning, they demonstrate its effectiveness, enabling training sequences that are up to device count times longer than those of prior memory-efficient Transformers, exceeding a context length of 100 million without making approximations to attention.

In terms of future prospects, the possibility of near-infinite context introduces opportunities such as:
- Large video-audio-language models
- Learning from extended feedback and trial-and-errors
- Understanding and generating codebase
- Adapting AI models to understand scientific data such as gene sequences
- Developing strong reasoning from link gathering data
