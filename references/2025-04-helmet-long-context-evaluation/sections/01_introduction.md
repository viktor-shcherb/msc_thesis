# Introduction [p. 1-2]

## Long-Context LCLMs and Evaluation Challenges

Long-context language models (LCLMs) unlock a myriad of applications, from summarizing long documents to learning new tasks on the fly with thousands of examples [p. 1]. Many recent benchmarks have sought to evaluate language models' long-context abilities (Zhang et al., 2024b; An et al., 2024; Shaham et al., 2023; Bai et al., 2024, inter alia) [p. 1].

However, recent developments in long-context evaluation (Chen et al., 2023; Xiong et al., 2023; Peng et al., 2024; Fu et al., 2024) still rely either on perplexity or on synthetic needle-in-a-haystack tasks (NIAH; Kamradt, 2024; Hsieh et al., 2024) [p. 1]. Frontier LCLMs (Dubey et al., 2024; Team et al., 2024c; OpenAI, 2023; Team et al., 2024a) also mostly report NIAH, sometimes with arbitrary subsets of other datasets, as shown in Table 1 [p. 1-2].

**Table 1** (p. 1): Most LCLMs evaluate on synthetic (Syn.) tasks. checkmark: base models. x: x-BENCH.

| Model | Syn. PPL | NIAH | ZeroSCROLLS | RAG | ICL |
|-------|----------|------|-------------|-----|-----|
| Gemini-1.5 | checkmark | x | x | x | x |
| GPT-4o | checkmark | x | x | x | x |
| Llama-3.1 | checkmark | x | x | x | x |
| Jamba-1.5 | x | x | x | x | x |
| Xiong et al. | x | x | x | checkmark | x |
| Chen et al. | checkmark | checkmark | x | x | x |
| Peng et al. | checkmark | x | x | x | x |
| Fu et al. | checkmark | checkmark | checkmark | x | x |

[Note: Table shows that most frontier LCLMs primarily evaluate on synthetic tasks like perplexity (Syn. PPL) and NIAH, with limited coverage of other benchmarks like ZeroSCROLLS, RAG, and ICL]

## Motivation Question

Why don't model developers agree on these evaluations? [p. 2] The authors take a closer look and find that existing benchmarks suffer from many critical design flaws, including:

### Insufficient coverage of downstream tasks

Existing benchmarks either focus on synthetic tasks (Hsieh et al., 2024) or include only a single question answering (Zhang et al., 2024b) [p. 2]. Other works study particular aspects of LCLMs, such as summarization (Chang et al., 2024), in-context learning (Li et al., 2024c), and retrieval-augmented generation (RAG; Lee et al., 2024), but they do not provide a holistic evaluation of LCLMs [p. 2].

### Inadequate lengths

Most natural language datasets in existing benchmarks (Shaham et al., 2023; An et al., 2024; Table 4) are too short to effectively test frontier long-context abilities (usually ≥128K) [p. 2].

### Unreliable metrics

For commonly used long-document QA and summarization tasks, most existing benchmarks still rely on metrics like ROUGE (Lin, 2004), which are often noisy and unreliable (Goyal et al., 2023; Deutsch et al., 2022; Chang et al., 2024) [p. 2].

### Incompatibility with base models

Many LCLM developers evaluate base models without instruction tuning, but most existing benchmarks require models to be instruction-tuned—hence developers can only rely on synthetic tasks or perplexity [p. 2].

## Benchmark Reliability Concerns

Consequently, existing benchmarks are either not applicable to long-context works (inadequate lengths or incompatibility) or provide highly noisy signals (insufficient coverage or unreliable metrics) [p. 2]. The authors summarize the shortcomings of existing benchmarks in Table 2 [p. 2].

For the three benchmarks that support a 128K+ context length (NIAH, RULER, and x-BENCH), the authors use them to evaluate six frontier models and report the numbers in Figure 1 [p. 2]. They observe that NIAH does not reflect differences across models; RULER and x-BENCH show unexpected trends—on RULER, Gemini Flash outperforms Gemini Pro; on x-BENCH, the 70B Llama model underperforms compared to the 8B one [p. 2]. This raises concerns about the reliability of the evaluations and how they can differentiate long-context models, which likely contributes to the lack of use of these benchmarks in model development [p. 2].

**Figure 1** (p. 2): Long-context benchmark results of frontier LCLMs (Llama-3.1 8B/70B, GPT-4o-mini, GPT-4o-08-06, and Gemini-1.5 Flash/Pro)

Description: Bar chart comparing four benchmarks (NIAH, RULER, x-BENCH, HELMET) across different models at varying context lengths (8K, 70B mini, 4G Flash, Pro).
- NIAH shows performance near 80-100% for all models, appearing saturated
- RULER shows 60-90% performance with unexpected trends (Flash outperforming Pro)
- x-BENCH shows 40-60% performance with inconsistent model rankings (70B underperforming 8B)
- HELMET (theirs) shows 30-60% performance with more consistent rankings across models
- Supports claim: NIAH is saturated for almost all models; RULER and x-BENCH show unexpected trends for Llama-3.1 (Dubey et al., 2024). In contrast, HELMET demonstrates more consistent rankings of these frontier models.

## Introducing HELMET

To address these challenges, the authors present HELMET (How to Evaluate Long-context Models Effectively and Thoroughly) [p. 2]. They curate seven application-centric long-context tasks across seven categories [p. 2]. Beyond widely adopted categories like synthetic recall, long-document question answering (QA), and summarization, they also add many-shot in-context learning (ICL), retrieval-augmented generation (RAG), passage re-ranking, and generation with citations (Gao et al., 2023) [p. 2].

### Addressing Existing Benchmark Shortcomings

The authors further address the shortcomings of existing benchmarks [p. 2]:

1. They ensure all datasets support input lengths of 128K tokens and are easily extendable to longer contexts (§2.1) [p. 2]
2. They introduce reference-based model evaluation for QA and summarization and show that it significantly improves over n-gram overlap metrics (§2.2) [p. 2]
3. They refine the prompts and in-context demonstrations used for all tasks, reducing evaluation noise caused by different output formats and allowing base models to be evaluated robustly across most categories (§2.3) [p. 2]

Together, HELMET enables a holistic evaluation of long-context capabilities and provides more reliable signals for model development [p. 2-3]. Figure 1 demonstrates that HELMET can clearly differentiate models with varying capabilities and reflect comparisons consistent with human perception [p. 3]. More detailed discussion on HELMET's improvements over previous benchmarks and direct comparisons can be found in §A [p. 3].

## Main Findings

To understand the progress of LCLMs and how different long-context capabilities correlate with one another, the authors evaluate a comprehensive list of 59 LCLMs of various architectures, scales, and training approaches [p. 3]. Their analysis reveals that:

1. Synthetic tasks poorly indicate downstream performance (§3.1) [p. 3]
2. Different categories in HELMET exhibit distinct trends (§3.2) [p. 3]
3. Open-source models significantly lag behind closed ones on tasks that require reasoning over long contexts or following complex instructions—the gap further widens as context length increases (§3.3) [p. 3]

Finally, they find that the RAG category strikes a good balance between ease of use, stronger correlation with downstream tasks, and compatibility with base models [p. 3]. Ultimately, it is imperative to evaluate LCLMs across a diverse spectrum of categories [p. 3]. The authors hope their work and insights provide a more effective way to evaluate LCLMs for future model development and benchmarking [p. 3].
