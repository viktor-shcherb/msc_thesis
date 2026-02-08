# 5. Related Works [p. 8-9]

In addition to methods based on position interpolation, this section discusses related works of other approaches. [p. 8]

## Retrieval-based approaches [p. 8]

Retrieval-based approaches use an external memory module to memorize long past context and retrieval modules for related documents fetching at inference (Tworkowski et al., 2023; Wang et al., 2023; Borgeaud et al., 2022). These designs typically need explicit modifications on the LLM architectures. LongRoPE, in contrast, is more lightweight, with minor positional embedding modifications. It can also handle more long context tasks beyond retrieval, such as long document summarization and few-shot learning. [p. 8]

## Attention-based context window extensions [p. 8]

Beyond positional embedding interpolation, some research achieves input context extension using the original LLM context window length by manipulating attention mechanisms (Han et al., 2023; Xiao et al., 2023; Ratner et al., 2022). The key idea is to mitigate the attention explosion issue caused by new positions using novel attention masks. These efforts and positional interpolation methods are complementary. [p. 8]

## Fine-tuning based approaches [p. 8-9]

Fine-tuning based approaches focus on how to effectively fine-tune pre-trained LLMs with modified position embeddings for longer context. Works like Code LLaMA (Roziere et al., 2023), LLaMA2 Long (Xiong et al., 2023) and ScaledRoPE (Liu et al., 2023) choose a very large base value for RoPE and fine-tune on the target length. LongRoPE offers flexibility for various target lengths and can achieve beyond 2M length. More recently, as fine-tuning for long context lengths (i.e., over 128k) demands substantial GPU resources, LongLoRA (Chen et al., 2023b) and PoSE (Zhu et al., 2023) are proposed to mitigate this overhead. LongRoPE's method is orthogonal to these efficient fine-tuning works. [p. 9]
