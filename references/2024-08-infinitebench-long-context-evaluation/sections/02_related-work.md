# 2 Related Work [p. 2–3]

## Extending Context Length

[p. 2] Transformers, typically trained on text sequences under 8K tokens due to self-attention's quadratic complexity, face challenges in longer downstream tasks. Two main strategies have emerged: (1) the development of positional encodings capable of handling longer text sequences (Sun et al., 2022; Press et al., 2021), and (2) the refinement of inference stage techniques to extend current LLMs post-training. The primary approach involves modifying rotary positional encoding (Su et al., 2023) and implementing post-training adjustments to better manage the increased relative positional distances in longer sequences (Zhu et al., 2023; Peng et al., 2023b; Chen et al., 2023a).

## 100K+ LLMs

[p. 3] Recently, many LLMs have shown the ability to handle over 100K tokens. Popular proprietary 100K+ LLMs include GPT-4, Claude 2 (Anthropic, 2023), and Kimi-Chat (AI, 2023). On the other hand, there are much fewer open-source 100K+ models. Some notable models include YaRN (Peng et al., 2023b) and Yi-200K (01.AI, 2023a,b). The paper benchmarks GPT-4, Claude 2, Kimi-Chat, and YaRN-Mistral-7B-128K on InfiniteBench, which are some of the latest and strongest LLMs that claim to handle over 100K tokens.

## Inference Infrastructure

[p. 3] Numerous studies aim to accelerate self-attention computation. Research primarily concentrates on refining attention mechanisms through improved IO management (Dao et al., 2022; Dao, 2023), memory optimization (Kwon et al., 2023; Shazeer, 2019; Ainslie et al., 2023), and enhanced parallelization in decoding (Dao et al., 2023; Hong et al., 2023). Approaches like Sliding Window Attention (Beltagy et al., 2020), LM-Infinite (Han et al., 2023), and StreamingLLM (Xiao et al., 2023) introduce attention variants for handling infinitely long sequences without overwhelming computation or memory overhead. However, these techniques often face challenges in maintaining historical information.

## Long Context Benchmarks

[p. 3] Several benchmarks exist for evaluating long-context AI models, notably featuring context lengths of around 10K tokens. L-Eval (An et al., 2023) and LongBench (Bai et al., 2023) are prominent examples, aggregating pre-existing tasks (Kociskỳ et al., 2017; Dasigi et al., 2021; Yang et al., 2018; Huang et al., 2021; Joshi et al., 2017) into comprehensive benchmarks. LongBench encompasses four categories -- QA, summarization, synthetic retrieval, and code -- spanning 21 tasks, with four being novel. Conversely, L-Eval incorporates 18 tasks across QA, summarization, math, retrieval, and multiple-choice (MC) domains, introducing three new tasks. Another notable benchmark, LooGLE (Li et al., 2023), differentiates between short and long dependency examples, focusing on summary and QA tasks; its summary corpus contrasts with InfiniteBench, utilizing academic papers over novels. The Long-Range Arena (LRA) (Tay et al., 2020) further diversifies with six tasks in text, image, and math, designed for scalability. In comparison, InfiniteBench stands out for its substantially longer contexts and a broader range of task domains. Table 1 offers a detailed comparison of these long-context benchmarks.

## Table 1

**Table 1** (p. 2): "Comparison to existing long-context benchmarks and InfiniteBench. 'En' and 'Zh' refer to English and Chinese tasks. 'Code', 'Math', 'Novel', 'Dialogue' indicate whether the domain includes tasks from those domains, and 'Synthetic' indicates whether there are auto-generated tasks."

| Benchmark              | Avg Len  | En | Zh | Code | Math | Novel | Dialogue | Synthetic |
|------------------------|----------|----|----|------|------|-------|----------|-----------|
| LRA (Tay et al., 2020) | ~10K     | Yes | No | No  | Yes  | No   | No       | Yes       |
| LongBench (Bai et al., 2023) | ~10K | Yes | Yes | Yes | No  | Yes  | Yes      | Yes       |
| L-Eval (An et al., 2023) | 4K-60K | Yes | No | Yes | Yes | No   | No       | Yes       |
| LooGLE (Li et al., 2023) | ~20K   | Yes | No | No  | No  | No   | Yes      | No        |
| InfiniteBench (ours)   | ~200K    | Yes | Yes | Yes | Yes | Yes  | Yes      | Yes       |
