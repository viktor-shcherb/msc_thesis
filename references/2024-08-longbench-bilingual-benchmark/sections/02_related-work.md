# 2 Related Work [p. 2-3]

## Long Context Modeling Techniques

[p. 2] Two key challenges in long text modeling: the high runtime overhead on longer context, and the catastrophic forgetting phenomenon when processing long sequences.

Approaches discussed:

**Efficient and unforgetful Transformers** (Tay et al., 2022):
- Sparse and efficient computation: Child et al. (2019), Kitaev et al. (2020), Beltagy et al. (2020), Zaheer et al. (2020), Wang et al. (2020), Fedus et al. (2022), Ding et al. (2023)
- Recurrent and memory modules: Dai et al. (2019), Rae et al. (2020), Wu et al. (2022), Martins et al. (2022), Bulatov et al. (2022), Orvieto et al. (2023), Liang et al. (2023), Zhou et al. (2023)

**Length extrapolation of Transformers** (Press et al., 2022; Sun et al., 2022; Chen et al., 2023): adopted in training of long context LLMs such as ChatGLM2-32k (Zeng et al., 2023) and LongChat-32k (Li et al., 2023).

## Evaluation for Long Context Understanding

[p. 2-3] Many previous works on long text modeling rely on perplexity for evaluation (Beltagy et al., 2020; Roy et al., 2021; Press et al., 2022). However, as suggested in Sun et al. (2021), the perplexity metric may not necessarily reflect the model's performance on sequence-level tasks in real applications.

Some works assess long text modeling through artificial tasks such as retrieval (Tay et al., 2021; Chen et al., 2023; Li et al., 2023), which may also fall short in mirroring real-world scenarios.

Concurrently, **ZeroSCROLLS** (Shaham et al., 2022, 2023) and **L-Eval** (An et al., 2023) are proposed as evaluation benchmarks for long text modeling. However, they encompass a restricted range of task types, limiting the diversity of long text modeling patterns.

[p. 3] **AgentBench** (Liu et al., 2023c) mentions the challenge of LLM-as-Agent's handling long interaction trajectories but fails to incorporate it as a dedicated evaluation dimension.

In contrast, LongBench includes six major task categories, with each category featuring sequences of varying lengths, languages, and domains. The authors believe it provides a more holistic evaluation of long text modeling ability across a spectrum of lengths, distributions, and long dependency patterns.
