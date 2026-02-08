# Introduction [p. 1-2]

[p. 1] LLMs, typically based on large transformers trained on vast corpora, have shown exceptional abilities in memorization, comprehension, and reasoning (OpenAI, 2023; Touvron et al., 2023; Zheng et al., 2023). A critical factor affecting LLM performance is the context window -- the number of tokens an LLM can process simultaneously. Since the debut of ChatGPT with a 2,000-token window in November 2022, significant efforts have been made including more efficient attention mechanisms (Dao et al., 2022a; Zaheer et al., 2020; Ding et al., 2023), scalable position embeddings (Su et al., 2021; Sun et al., 2022), and quantization techniques (Frantar et al., 2022; Dettmers et al., 2022).

[p. 2] As of December 2023, several LLMs claim context windows up to hundreds of thousands of tokens, including proprietary models like GPT-4 Turbo (128,000 tokens), Claude-2.1 (200,000 tokens), and Moonshot AI (200,000 Chinese characters), and open-source models such as ChatGLM-32k (Zeng et al., 2022) and LongChat-32k (Li* et al., 2023). Nevertheless, the effectiveness of these long-context LLMs in managing long texts remains an area ripe for exploration and assessment.

Alongside the evolution of LLMs, a wide range of benchmarks have emerged for capability assessment (Hendrycks et al., 2020; Suzgun et al., 2022; Cobbe et al., 2021; Huang et al., 2023). Most utilize short questions or instructions, making them unsuitable for evaluating long-context capabilities. While a few benchmarks focus on specific long-context abilities like summarization, QA, and continue writing (Huang et al., 2021; Liu et al., 2023b; Dasigi et al., 2021), comprehensive long-document evaluations have been limited. Recent benchmarks such as SCROLLS (Shaham et al., 2022), L-Eval (An et al., 2023) and LongBench (Bai et al., 2023) have started to address this gap by including a suite of long-document tasks.

Three significant limitations persist in existing benchmarks:
1. The ultra-long setting (32,000 tokens or longer) is scarcely represented, limiting insights into LLM performance in extreme context lengths.
2. The integration of test samples of varying lengths within these benchmarks complicates the evaluation of LLMs across different length ranges.
3. The focus on traditional tasks such as QA and summarization often does not necessitate comprehensive content understanding by the LLMs, as many questions in these tasks do not require full-text comprehension.

The authors introduce **Ada-LEval**, a benchmark to assess the long-context capabilities with length-adaptable questions. Ada-LEval comprises two challenging tasks: **TSort** (arranging text segments in correct order) and **BestAnswer** (choosing the best answer among multiple candidates).

Both tasks feature three advantages:
1. **Controllable Test Cases**: The length of each test case can be finely tuned -- by adjusting the number and length of text segments in TSort and altering the number of distractor options in BestAnswer.
2. **Necessity for Full-Text Comprehension**: Successful completion of both tasks mandates complete reading and understanding of the provided text.
3. **Precise Accuracy Measurement**: The design allows for unambiguous accuracy calculation. TSort has a definitive "correct" order, whereas in BestAnswer, the annotated responses by the questioner serve as definitive answers.

Key experimental findings reported:
- A noteworthy decline in performance of existing LLMs as text length increases, particularly in ultra-long scenarios.
- The ablation study uncovers several shortcomings in current LLMs, including limited instruction following over extended texts and pronounced input order bias.
- Exploration of various scalable position embedding techniques aimed at enlarging the context window of LLMs. Models equipped with those techniques show improved performance over standard models, and performance is comparable to their counterparts trained on longer contexts.
