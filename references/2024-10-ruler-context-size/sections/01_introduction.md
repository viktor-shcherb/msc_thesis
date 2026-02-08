# Introduction [p. 1-2]

## Motivation

[p. 1] Recent advancements in AI system engineering (Dao et al., 2022; Jacobs et al., 2023; Fu et al., 2024) and language model designs (Chen et al., 2023; Xiong et al., 2023) have enabled efficient scaling up of context length for language models (Liu et al., 2024a; Young et al., 2024). Previous works (AI21, 2024; X.AI, 2024; Reid et al., 2024; Anthropic, 2024) commonly adopt synthetic tasks, such as passkey retrieval (Mohtashami & Jaggi, 2023) and needle-in-a-haystack (Kamradt, 2023) to evaluate long-context LMs. However, these evaluations are used inconsistently across works and reveal merely the retrieval capability, failing to gauge other forms of long-context understanding.

## RULER Proposal

[p. 1] The authors propose RULER, a new benchmark to evaluate long-context modeling capabilities for language models. RULER contains four task categories to test behaviors (Ribeiro et al., 2020) beyond simple retrieval from context:

1. **Retrieval:** extends the needle-in-a-haystack (Kamradt, 2023; NIAH) test to evaluate retrieval capability with diverse types and quantities of needles.
2. **Multi-hop Tracing:** proposes *variable tracking*, a minimal proxy task for coreference chain resolution to check the behavior of tracing entities with multi-hop connections.
3. **Aggregation:** proposes *common/frequent words extraction*, proxy tasks for summarization to test the ability to aggregate relevant information that spans long-range context.
4. **Question Answering:** adds distracting information to the input of existing short-context QA datasets to evaluate question answering capability at various context sizes.

## Comparison to Existing Benchmarks

[p. 2] Compared to existing realistic benchmarks (Table 1), RULER consists solely of synthetic tasks, which offer the flexibility to control sequence length and task complexity. The synthetic input in RULER reduces reliance on parametric knowledge, which interferes with the utilization of long-context input in realistic tasks (Shaham et al., 2023; Bai et al., 2023).

**Table 1** (p. 2): Comparison between existing long-context benchmarks and RULER. "Realistic" type refers to human-annotated while "synthetic" type refers to auto-generated.

| Benchmark & Task            | Avg Len | Type      | Diverse Tasks | Min. Parametric Knowledge | Controllable Context |
|-----------------------------|---------|-----------|:---:|:---:|:---:|
| ZeroSCROLLS                 | ~10k    | realistic | Y   | X   | X   |
| L-Eval                      | ~8k     | realistic | Y   | X   | X   |
| BAMBOO                      | ~16k    | realistic | Y   | Y   | X   |
| LongBench                   | ~8k     | hybrid    | Y   | X   | X   |
| LooGLE                      | ~20k    | hybrid    | Y   | Y   | X   |
| InfiniteBench               | ~200k   | hybrid    | Y   | Y   | X   |
| Needle-in-a-haystack (NIAH) | any     | synthetic | X   | Y   | Y   |
| Passkey / Line / KV Retrieval | any   | synthetic | X   | Y   | Y   |
| RULER (Ours)                | any     | synthetic | Y   | Y   | Y   |

(Y = yes/checkmark, X = no/cross)

RULER includes diverse task domains beyond retrieval, reduces reliance on parametric knowledge with synthetic input, and offers flexibility to control the contexts for different sequence lengths and task complexities. In RULER, contexts can be adjusted by changing the volume or placement of relevant and distracted information.

## Key Findings

[p. 2] Using RULER, the authors benchmark Gemini-1.5 (Reid et al., 2024), GPT-4 (OpenAI: Josh Achiam et al., 2023), and 15 open-source models with context length ranging from 4k to 128K. Key findings:

- Despite achieving nearly perfect performance on the vanilla NIAH test, almost all models exhibit large degradation on more complex tasks in RULER as sequence length increases.
- While all models claim context size of 32k tokens or greater, results indicate that only half of them can effectively handle sequence length of 32K by exceeding a qualitative threshold.
- Almost all models fall below the threshold before reaching the claimed context lengths.
- The top two models -- Gemini-1.5 and GPT-4 -- consistently outperform other models regardless of the chosen weighting scheme.
- Two weighted average scores are used to aggregate performance from 4k to 128k, where the weights simulate the length distribution of real-world use cases.

## Yi-34B Analysis

[p. 2] The authors further analyze Yi-34B, which claims context length of 200K and achieves reasonably good performance on RULER among open-source models. Results demonstrate large degradation in Yi's performance as input length and task complexity increase. At large context sizes, Yi-34B often returns incomplete answers and fails to precisely locate the relevant information. Two behaviors emerge with scaling of context size across multiple models: (1) increased reliance on parametric knowledge and (2) increased tendency to copy from context for non-retrieval tasks.

## Ablation Findings

[p. 2] Additional ablations demonstrate that:
- Training on longer sequences does not always lead to better performance on RULER.
- Larger model sizes positively correlate with better long-context capabilities.
- Non-Transformer architectures, such as RWKV and Mamba, still lag behind Transformer by large margins on RULER.

## Contributions

[p. 2] The authors list three contributions:
1. A new benchmark RULER for evaluating long-context language models via synthetic tasks with flexible configurations.
2. New task categories, specifically multi-hop tracing and aggregation, to test behaviors other than retrieval from long context.
3. Evaluation of 17 long-context LMs using RULER with analysis across models and task complexities.

The authors open source RULER at https://github.com/hsiehjackson/RULER.
