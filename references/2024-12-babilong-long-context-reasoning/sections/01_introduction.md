# Introduction [p. 1-2]

## Context and motivation

Today, large language models (LLMs) and neural architectures are continually evolving and achieving remarkable improvements, particularly in their ability to handle longer contexts (OpenAI, 2023b; Reid et al., 2024; Anthropic, 2024). The ability of these models to process and generate text based on rich contextual information is crucial for several reasons. For example, longer contexts provide more information for the model to condition its outputs, leading to more accurate, contextually relevant, and up-to-date responses. Furthermore, long-context capabilities can enhance in-context learning by providing more in-context examples, instructions to follow, or example trajectories in context of reinforcement learning (Chevalier et al., 2023; Agarwal et al., 2024; Lee et al., 2023). [p. 1]

## Limitations of existing benchmarks

Despite these advances in models capabilities, the benchmarks used to evaluate them have not kept pace. For example, current benchmarks such as Longbench (Bai et al., 2023) and L-Eval (An et al., 2023) scale only up to 40,000 tokens, while models are capable of hundreds of thousands and millions of tokens (Rodkin et al., 2024; Reid et al., 2024; Bulatov et al., 2024; Anthropic, 2024; Liu et al., 2024a; Gu & Dao, 2023; OpenAI, 2023a). [p. 1]

Creating natural and comprehensive long-context benchmarks that are human labeled is very challenging. As a consequence, synthetic benchmarks focusing on variations of "needle-in-a-haystack" [p. 1]

tasks have become increasingly common (Zhang et al., 2024b; Liu et al., 2024a; Song et al., 2024b; Hsieh et al., 2024). One widely used needle-in-a-haystack task involves finding specific "needles with magic numbers" in a haystack of Paul Grahm's essays¹. However, the widespread use of this approach has highlighted its limitations - it is overly simplistic, and novel long context models often achieve perfect performance, as recently demonstrated by fully green numbers (Reid et al., 2024; Cohere, 2024; Liu et al., 2024a; Wang et al., 2024c). This shows that while it serves well as a basic verification tool, it is not a rigorous benchmark that can effectively challenge and differentiate advanced long-context models. Another major drawback of the original default setup² is that model predictions are evaluated and scored by an LLM (GPT-3.5-turbo) on a scale of 1 to 10, with the same single needle used for each position and document length. While averaging over multiple different needles can provide more robust results. [p. 2]

¹https://github.com/gkamradt/LLMTest_NeedleInAHaystack

## Introducing BABILong

To bridge this gap, we introduce the BABILong benchmark, designed to test language models' ability to reason across facts distributed in extremely long documents. BABILong includes a diverse set of 20 reasoning tasks, including fact chaining, simple induction, deduction, counting, and handling lists/sets, that were designed as prerequisites for any system that aims to be capable of conversing with a human (Weston et al., 2016). As a source of long natural documents we use books from PG19 corpora (Rae et al., 2020). In this way, BABILong enables the creation of tasks of almost arbitrary length, in order to adapt them to the evaluation of new, more powerful models in an extensible and controllable way. We provide sets of predefined lengths with splits up to 10 million tokens, and we evaluate models on samples with up to 50 million tokens. [p. 2]

## Key findings

We find that popular LLMs effectively use only 10-20% of the context, with performance declining sharply as length and task complexity increase. Retrieval-Augmented Generation methods achieve a modest 60% accuracy in answering single-fact questions, regardless of context length. Among other methods, Mamba and Recurrent Memory Transformers (RMT and ARMT) show the highest performance, with ARMT capable of processing lengths up to 50 million tokens. [p. 2]

## Main contributions

The main contributions of our work are as follows: [p. 2]

1. We introduce BABILong, a novel scalable generative multi-task benchmark for evaluating the performance of NLP models in processing arbitrarily long documents with distributed facts. [p. 2]

2. We evaluate over 30 recent long-input language models with various sizes, architectures, and context extension methods on BABILong. [p. 2]

**Figure 1** (p. 2): "a) Generation of BABILong dataset. Facts relevant for the question are hidden inside a larger background texts from PG19. b) Recurrent transformers answer questions about facts from very long texts when retrieval augmented generation fails. Common RAG method fails to answer questions because order of facts matters. GPT-4 effectively uses only about 10% of the full 128K window. Gemini 1.5 Pro shows strong performance up to 64K tokens. Small LMs, ARMT & RMT with GPT-2 (137M) and Mamba (130M) fine-tuned for the task are able to solve it, with recurrent memory transformers scoring well up to record 50 000 000 tokens. Here we show the best results obtained by models."

Description: Composite figure with two panels: a) shows a schematic diagram of BABILong dataset generation with sample bAbI task facts (F1: Mary went to the bathroom, F2: John moved to the hallway, F3: Mary travelled to the office, Q: Where is Mary?) being scattered throughout chunks of background text from PG19. b) shows a line graph plotting accuracy (%) vs context size (tokens, log scale from 1E+4 to 1E+7) for different models on QA1: Single supporting fact task. Notable patterns: GPT-4 maintains ~100% accuracy up to ~11.1M tokens then drops to ~80% at 50M; ARMT(137M) and RMT(137M) show strong performance across all lengths; Mamba (130M) performs well up to 64K then declines; Gemini 1.5 Pro 002 and Llama3-CharQA-1.5-8B-RAG show declining performance with increased context.

Supports claim: Popular LLMs effectively use only 10-20% of context [p. 2], and recurrent memory transformers can process up to 50 million tokens [p. 2].
