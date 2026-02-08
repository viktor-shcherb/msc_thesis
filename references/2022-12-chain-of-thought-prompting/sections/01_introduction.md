# 1 Introduction [p. 1--2]

[p. 1] The NLP landscape has been revolutionized by language models (Peters et al., 2018; Devlin et al., 2019; Brown et al., 2020, *inter alia*). Scaling up model size confers benefits such as improved performance and sample efficiency (Kaplan et al., 2020; Brown et al., 2020, *inter alia*). However, scaling model size alone has not proved sufficient for achieving high performance on challenging tasks such as arithmetic, commonsense, and symbolic reasoning (Rae et al., 2021).

This work explores how the reasoning ability of large language models can be unlocked by a simple method motivated by two ideas:

1. Techniques for arithmetic reasoning can benefit from generating natural language rationales that lead to the final answer. Prior work has given models the ability to generate natural language intermediate steps by training from scratch (Ling et al., 2017) or finetuning a pretrained model (Cobbe et al., 2021), in addition to neuro-symbolic methods that use formal languages instead of natural language (Roy and Roth, 2015; Chiang and Chen, 2019; Amini et al., 2019; Chen et al., 2019).

2. Large language models offer the exciting prospect of in-context few-shot learning via *prompting*. Instead of finetuning a separate language model checkpoint for each new task, one can simply "prompt" the model with a few input-output exemplars demonstrating the task. This has been successful for a range of simple question-answering tasks (Brown et al., 2020).

[p. 2] Both ideas have key limitations. For rationale-augmented training and finetuning methods, it is costly to create a large set of high quality rationales, which is much more complicated than simple input-output pairs used in normal machine learning. For the traditional few-shot prompting method used in Brown et al. (2020), it works poorly on tasks that require reasoning abilities, and often does not improve substantially with increasing language model scale (Rae et al., 2021).

The paper combines the strengths of these two ideas in a way that avoids their limitations. Specifically, the authors explore the ability of language models to perform few-shot prompting for reasoning tasks, given a prompt that consists of triples: (input, *chain of thought*, output). A *chain of thought* is a series of intermediate natural language reasoning steps that lead to the final output, and the authors refer to this approach as *chain-of-thought prompting*. An example prompt is shown in Figure 1.

Empirical evaluations on arithmetic, commonsense, and symbolic reasoning benchmarks show that chain-of-thought prompting outperforms standard prompting, sometimes to a striking degree. Figure 2 illustrates one such result -- on the GSM8K benchmark of math word problems (Cobbe et al., 2021), chain-of-thought prompting with PaLM 540B outperforms standard prompting by a large margin and achieves new state-of-the-art performance. A prompting-only approach is important because it does not require a large training dataset and because a single model checkpoint can perform many tasks without loss of generality.

## Figure 1 [p. 1]

**Figure 1** (p. 1): "Chain-of-thought prompting enables large language models to tackle complex arithmetic, commonsense, and symbolic reasoning tasks. Chain-of-thought reasoning processes are highlighted."

The figure contrasts standard prompting (left) with chain-of-thought prompting (right) on a math word problem. In standard prompting, the model input contains question-answer exemplars and the model outputs an incorrect answer ("The answer is 27."). In chain-of-thought prompting, the exemplar answers include highlighted intermediate reasoning steps (e.g., "Roger started with 5 balls. 2 cans of 3 tennis balls each is 6 tennis balls. 5 + 6 = 11."), and the model output also produces a chain of thought leading to the correct answer ("The answer is 9.").

## Figure 2 [p. 2]

**Figure 2** (p. 2): "PaLM 540B uses chain-of-thought prompting to achieve new state-of-the-art performance on the GSM8K benchmark of math word problems. Finetuned GPT-3 and prior best are from Cobbe et al. (2021)."

Bar chart showing solve rate (%) on GSM8K Math Word Problems for four conditions:
- Finetuned GPT-3 175B: ~33%
- Prior best: ~55%
- PaLM 540B standard prompting: ~18%
- PaLM 540B chain-of-thought prompting: ~57%

The figure supports the claim that chain-of-thought prompting with PaLM 540B surpasses finetuned GPT-3 with a verifier and achieves new state-of-the-art on GSM8K.
