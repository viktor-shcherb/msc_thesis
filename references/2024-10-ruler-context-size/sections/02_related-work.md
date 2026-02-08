# Related Work [p. 3]

## Long-context Language Models

[p. 3] Numerous long-context language models have been introduced owing to progress in engineering, architectural, and algorithmic designs.

**Attention efficiency:** Flash attention (Dao et al., 2022; Dao, 2023) and Ring attention (Liu et al., 2023) significantly reduce the memory footprint required for processing long context. Various sparse attention mechanisms (Child et al., 2019; Jaszczur et al., 2021) such as shifted sparse attention (Chen et al., 2024), dilated attention (Ding et al., 2023), and attention sinks (Han et al., 2023; Xiao et al., 2024b) were employed to enable efficient context scaling.

**Position embeddings:** Novel position embedding methods were proposed to improve length extrapolation in Transformers (Vaswani et al., 2017), including ALiBi (Press et al., 2022), xPOS (Sun et al., 2023b), and RoPE (Su et al., 2023) variants (Chen et al., 2023; Xiong et al., 2023; Peng et al., 2024; Liu et al., 2024b; Ding et al., 2024; Zhu et al., 2024).

**Context size reduction:** Another line of research focuses on reducing context size. This can be achieved by caching previous context using recurrence mechanism (Zhang et al., 2024a; Bulatov et al., 2023; Martins et al., 2022; Wu et al., 2022), retrieving relevant information from context (Xu et al., 2024a; Mohtashami & Jaggi, 2023; Wang et al., 2024; Tworkowski et al., 2024; Xiao et al., 2024a), or preserving the salient information via compression (Jiang et al., 2023).

**Novel architectures:** Novel architectures (Gu et al., 2022; Fu et al., 2023a; Poli et al., 2023; Fu et al., 2023b; Sun et al., 2023a; Beck et al., 2024; Sun et al., 2024) such as Mamba (Gu & Dao, 2023) and RWKV (Peng et al., 2023) have also been proposed to efficiently handle long-context input.

## Long-context Benchmarks and Tasks

[p. 3] The authors' work is closely related to other works on benchmarking long-context language models:

- **ZeroSCROLLS** (Shaham et al., 2023) covers ten realistic natural language tasks, such as long-document QA and (query-based) summarization.
- **L-Eval** (An et al., 2024) also uses realistic data, which was filtered manually to ensure quality.
- **LongBench** (Bai et al., 2023) contains tasks in a bilingual setting.
- **InfiniteBench** (Zhang et al., 2024b) includes tasks with length greater than 100K tokens.
- **LTM** (Castillo et al., 2024) targets the evaluation of long-term conversations.

To isolate the effect of parametric knowledge, previous works (Dong et al., 2023; Li et al., 2023b) also propose to use documents posted online later than a certain cutoff date, or leverage extremely low-resource materials (Tanzer et al., 2024).

Compared to realistic benchmarks, synthetic tasks are more flexible to control the setup (e.g., sequence length and task complexity) and less affected by parametric knowledge. Recent works have primarily focused on retrieval-based synthetic tasks (Kamradt, 2023; Mohtashami & Jaggi, 2023; Li et al., 2023a; Liu et al., 2024d; Lee et al., 2024), with a few investigating other aspects, including fact reasoning (Kuratov et al., 2024; Karpinska et al., 2024), long-range discourse modeling (Sun et al., 2022), question answering (Levy et al., 2024; Yuan et al., 2024), many-shot in-context learning (Agarwal et al., 2024; Bertsch et al., 2024; Xu et al., 2024b), and code understanding (Liu et al., 2024c).
