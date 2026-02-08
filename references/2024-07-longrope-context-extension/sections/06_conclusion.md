# 6. Conclusion [p. 9]

LongRoPE is presented as a method that remarkably extends the context length of LLMs to an unprecedented 2048k, while maintaining their capabilities within original shorter context window. Two forms of non-uniformities in RoPE positional embedding are exploited using an efficient evolutionary search. This offers twofold benefits: it provides good initialization for fine-tuning and enables an 8x context window extension without fine-tuning. Building on this, a progressive extension strategy is proposed using 256k-length fine-tuned LLMs to reach a 2048k context window size without extra fine-tuning. Extensive experiments validate the effectiveness of LongRoPE. The authors envision that the LongRoPE-2048k models will enable many new long context applications and inspire further research. [p. 9]

# Broader Impacts [p. 9]

> "This paper presents work whose goal is to advance the field of Machine Learning. There are many potential societal consequences of our work, none of which we feel must be specifically highlighted here." [p. 9]
