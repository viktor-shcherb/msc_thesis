# Related Works [p. 10]

## Long-context language models

Frontier models such as GPT-4 (OpenAI, 2023), Gemini (Team et al., 2024b), and Claude claim to have an extended context window beyond 100K tokens [p. 10]. In the open-source community, there are also efforts to train models with longer input lengths (Dubey et al., 2024; Fu et al., 2024; AI et al., 2024; Guo et al., 2024), explore position extrapolation techniques (Peng et al., 2024; Chen et al., 2023; Ding et al., 2024), and experiment with efficient architectures (Beltagy et al., 2020; Bertsch et al., 2023; Gu & Dao, 2024; Dao & Gu, 2024; Yen et al., 2024; Lieber et al., 2024, inter alia) [p. 10].

## Synthetic tasks

Synthetic tasks are often used to evaluate LCLMs since they can be procedurally generated, enabling arbitrarily long input lengths and controlled "needle" placement (Tay et al., 2021; Liu et al., 2023) [p. 10]. In particular, Needle-in-a-Haystack (NIAH; Kamradt, 2024) inserts a "needle" at specific depths of a long essay (i.e., the haystack) and asks the model to recall the fact [p. 10]. Recent works have expanded upon it and designed new procedural benchmarks for LCLMs (Hsieh et al., 2024; Li et al., 2024b; Levy et al., 2024; Arora et al., 2023; Laban et al., 2024; Goldman et al., 2024, inter alia) [p. 10]. However, they do not study how results on synthetic tasks transfer to real applications [p. 10]. In contrast, they evaluate both synthetic and downstream tasks and investigate how they correlate with each other [p. 10].

## Long-context benchmarks

As discussed in the main paper, existing benchmarks either are limit to relatively short context lengths (Shaham et al., 2023; Li et al., 2024a; An et al., 2024; Bai et al., 2024; Dong et al., 2024; Kwan et al., 2024) or lack rigorous evaluation methods (Zhang et al., 2024b; Yuan et al., 2024) [p. 10]. Many works instead rely on specific domains, such as question answering (Wang et al., 2024b; Karpinska et al., 2024; Wang et al., 2024a;c), in-context learning (Li et al., 2024c; Bertsch et al., 2024; Yuan et al., 2024; Agarwal et al., 2024), summarization (Chang et al., 2024; Kim et al., 2024; Shen et al., 2022), or RAG (Lee et al., 2024) [p. 10]. In this work, they construct a comprehensive benchmark that tests across diverse downstream tasks at long input lengths and also present a unified comparison and analysis across 59 LCLMs [p. 10].
