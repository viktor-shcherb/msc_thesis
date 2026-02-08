# 3 Arithmetic Reasoning [p. 3--6]

[p. 3] The authors begin by considering math word problems of the form in Figure 1, which measure the arithmetic reasoning ability of language models. Though simple for humans, arithmetic reasoning is a task where language models often struggle (Hendrycks et al., 2021; Patel et al., 2021, *inter alia*). Strikingly, chain-of-thought prompting when used with the 540B parameter language model performs comparably with task-specific finetuned models on several tasks, even achieving new state of the art on the challenging GSM8K benchmark (Cobbe et al., 2021).

## 3.1 Experimental Setup [p. 3--4]

[p. 3] Chain-of-thought prompting is explored for various language models on multiple benchmarks.

**Benchmarks.** Five math word problem benchmarks are considered:
1. **GSM8K** -- benchmark of math word problems (Cobbe et al., 2021)
2. **SVAMP** -- dataset of math word problems with varying structures (Patel et al., 2021)
3. **ASDiv** -- dataset of diverse math word problems (Miao et al., 2020)
4. **AQuA** -- dataset of algebraic word problems (Koncel-Kedziorski et al., 2016)
5. **MAWPS** -- benchmark (Koncel-Kedziorski et al., 2016)

Example problems are given in Appendix Table 12.

**Standard prompting.** For the baseline, standard few-shot prompting is used, as popularized by Brown et al. (2020), in which a language model is given in-context exemplars of input-output pairs before outputting a prediction for a test-time example. Exemplars are formatted as questions and answers. The model gives the answer directly, as shown in Figure 1 (left).

**Chain-of-thought prompting.** The proposed approach augments each exemplar in few-shot prompting with a chain of thought for an associated answer, as illustrated in Figure 1 (right). As most of the datasets only have an evaluation split, the authors manually composed a set of eight few-shot exemplars with chains of thought for prompting -- Figure 1 (right) shows one chain of thought exemplar, and the full set of exemplars is given in Appendix Table 20. (These particular exemplars did not undergo prompt engineering; robustness is studied in Section 3.4 and Appendix A.2.)

[p. 4] For math word problems, the same single set of eight chain of thought exemplars was used for all benchmarks except AQuA, which is multiple choice instead of free response. For AQuA, four exemplars and solutions from the training set were used, as given in Appendix Table 21.

**Language models.** Five large language models are evaluated:

1. **GPT-3** (Brown et al., 2020): text-ada-001, text-babbage-001, text-curie-001, and text-davinci-002, which presumably correspond to InstructGPT models of 350M, 1.3B, 6.7B, and 175B parameters (Ouyang et al., 2022).
2. **LaMDA** (Thoppilan et al., 2022): models of 422M, 2B, 8B, 68B, and 137B parameters.
3. **PaLM**: models of 8B, 62B, and 540B parameters.
4. **UL2 20B** (Tay et al., 2022).
5. **Codex** (Chen et al., 2021, code-davinci-002 in the OpenAI API).

Sampling is done from the models via greedy decoding (though follow-up work shows chain-of-thought prompting can be improved by taking the majority final answer over many sampled generations (Wang et al., 2022a)). For LaMDA, averaged results over five random seeds are reported, where each seed had a different randomly shuffled order of exemplars. As LaMDA experiments did not show large variance among different seeds, results for a single exemplar order are reported for all other models to save compute.

## Figure 3 [p. 4]

**Figure 3** (p. 4): "Examples of (input, chain of thought, output) triples for arithmetic, commonsense, and symbolic reasoning benchmarks. Chains of thought are highlighted. Full prompts in Appendix G."

The figure shows nine example tasks arranged in a 3x3 grid. Each cell shows a question and an answer with the chain-of-thought portion highlighted:

- **Row 1:** Math Word Problems (free response), Math Word Problems (multiple choice), CSQA (commonsense)
- **Row 2:** StrategyQA, Date Understanding, Sports Understanding
- **Row 3:** SayCan (Instructing a robot), Last Letter Concatenation, Coin Flip (state tracking)

For example, the Math Word Problems (free response) cell shows: "Q: Roger has 5 tennis balls..." with highlighted chain of thought: "Roger started with 5 balls. 2 cans of 3 tennis balls each is 6 tennis balls. 5 + 6 = 11. The answer is 11."

## 3.2 Results [p. 4--5]

[p. 4--5] The strongest results of chain-of-thought prompting are summarized in Figure 4, with all experimental outputs for each model collection, model size, and benchmark shown in Table 2 in the Appendix.

Three key takeaways:

1. **Chain-of-thought prompting is an emergent ability of model scale** (Wei et al., 2022b). Chain-of-thought prompting does not positively impact performance for small models, and only yields performance gains when used with models of ~100B parameters. The authors qualitatively found that models of smaller scale produced fluent but illogical chains of thought, leading to lower performance than standard prompting.

2. [p. 5] **Chain-of-thought prompting has larger performance gains for more-complicated problems.** For instance, for GSM8K (the dataset with the lowest baseline performance), performance more than doubled for the largest GPT and PaLM models. On the other hand, for SingleOp, the easiest subset of MAWPS which only requires a single step to solve, performance improvements were either negative or very small (see Appendix Table 3).

3. **Chain-of-thought prompting via GPT-3 175B and PaLM 540B compares favorably to prior state of the art**, which typically finetunes a task-specific model on a labeled training dataset. Figure 4 shows how PaLM 540B uses chain-of-thought prompting to achieve new state of the art on GSM8K, SVAMP, and MAWPS (though note that standard prompting already passed the prior best for SVAMP). On the other two datasets, AQuA and ASDiv, PaLM with chain-of-thought prompting reaches within 2% of the state of the art (Appendix Table 2).

**Error analysis for GSM8K.** The authors manually examined model-generated chains of thought by LaMDA 137B for GSM8K. Of 50 random examples where the model returned the correct final answer, all of the generated chains of thought were also logically and mathematically correct except two that coincidentally arrived at the correct answer (see Appendix D.1, and Table 8 for examples of correct model-generated chains of thought). Of 50 random samples where the model gave the wrong answer, 46% of the chains of thought were almost correct, barring minor mistakes (calculator error, symbol mapping error, or one reasoning step missing), and the other 54% had major errors in semantic understanding or coherence (see Appendix D.2).

To provide a small insight into why scaling improves chain-of-thought reasoning ability, the authors performed a similar analysis of errors made by PaLM 62B and whether those errors were fixed by scaling to PaLM 540B. The summary is that scaling PaLM to 540B fixes a large portion of one-step missing and semantic understanding errors in the 62B model (see Appendix A.1).

## Figure 4 [p. 5]

**Figure 4** (p. 5): "Chain-of-thought prompting enables large language models to solve challenging math problems. Notably, chain-of-thought reasoning is an emergent ability of increasing model scale. Prior best numbers are from Cobbe et al. (2021) for GSM8K, Jie et al. (2022) for SVAMP, and Lan et al. (2021) for MAWPS."

The figure contains three rows of line plots (GSM8K, SVAMP, MAWPS) and three columns (LaMDA, GPT, PaLM). Each plot shows solve rate (%) on the y-axis and model scale (# parameters in billions) on the x-axis. Two lines per plot: standard prompting (solid with filled circles) and chain-of-thought prompting (solid with open circles). A dashed horizontal line marks prior supervised best.

- **GSM8K:** For all three model families, chain-of-thought prompting shows little or no improvement at small scales but large gains at the largest scale. PaLM 540B with chain-of-thought prompting reaches ~57%, exceeding the prior supervised best (~55%).
- **SVAMP:** Similar pattern; PaLM 540B with chain-of-thought prompting achieves the highest performance (~80%), well above prior supervised best (~57%).
- **MAWPS:** Chain-of-thought prompting at the largest scale reaches very high accuracy (~90%+ for PaLM 540B), above prior supervised best.

Model scales shown: LaMDA (0.4, 8, 137 billion), GPT (0.4, 7, 175 billion), PaLM (8, 62, 540 billion).

## 3.3 Ablation Study [p. 5--6]

[p. 5--6] The observed benefits of chain-of-thought prompting raise the natural question of whether the same performance improvements can be conferred via other types of prompting. Figure 5 shows an ablation study with three variations of chain of thought:

**Equation only.** One reason why chain-of-thought prompting might help is that it produces the mathematical equation to be evaluated, so a variation is tested where the model is prompted to output only a mathematical equation before giving the answer. Figure 5 shows that equation only prompting does not help much for GSM8K, which implies that the semantics of the questions in GSM8K are too challenging to directly translate into an equation without the natural language reasoning steps in chain of thought. For datasets of one-step or two-step problems, however, equation only prompting does improve performance, since the equation can be easily derived from the question (see Appendix Table 6).

[p. 6] **Variable compute only.** Another intuition is that chain of thought allows the model to spend more computation (i.e., intermediate tokens) on harder problems. To isolate the effect of variable computation from chain-of-thought reasoning, a configuration is tested where the model is prompted to output only a sequence of dots (...) equal to the number of characters in the equation needed to solve the problem. This variant performs about the same as the baseline, which suggests that variable computation by itself is not the reason for the success of chain-of-thought prompting, and that there appears to be utility from expressing intermediate steps via natural language.

**Chain of thought after answer.** Another potential benefit of chain-of-thought prompting could simply be that such prompts allow the model to better access relevant knowledge acquired during pretraining. An alternative configuration is tested where the chain of thought prompt is only given after the answer, isolating whether the model actually depends on the produced chain of thought to give the final answer. This variant performs about the same as the baseline, which suggests that the sequential reasoning embodied in the chain of thought is useful for reasons beyond just activating knowledge.

## Figure 5 [p. 6]

**Figure 5** (p. 6): "Ablation study for different variations of prompting using LaMDA 137B and PaLM 540B. Results for other datasets are given in Appendix Table 6 and Table 7."

Bar chart showing GSM8K solve rate (%) for LaMDA and PaLM across five conditions:
- Standard prompting
- Equation only
- Variable compute only
- Reasoning after answer
- Chain-of-thought prompting

For both LaMDA and PaLM, chain-of-thought prompting substantially outperforms all other variants. Standard prompting, equation only, variable compute only, and reasoning after answer all perform similarly (low single-digit to ~18% range), while chain-of-thought prompting achieves much higher solve rates (~14% for LaMDA 137B and ~57% for PaLM 540B, approximately).

## 3.4 Robustness of Chain of Thought [p. 6]

[p. 6] Sensitivity to exemplars is a key consideration of prompting approaches -- for instance, varying the permutation of few-shot exemplars can cause the accuracy of GPT-3 on SST-2 to range from near chance (54.3%) to near state of the art (93.4%) (Zhao et al., 2021).

The authors evaluate robustness to chains of thought written by different annotators. In addition to the results above which used chains of thought written by Annotator A, two other co-authors of the paper (Annotators B and C) independently wrote chains of thought for the same few-shot exemplars (shown in Appendix H). Annotator A also wrote another chain of thought that was more concise than the original, following the style of solutions given in Cobbe et al. (2021).

Figure 6 shows these results for LaMDA 137B on GSM8K and MAWPS (ablation results for other datasets are given in Appendix Table 6 / Table 7). Although there is variance among different chain of thought annotations, as would be expected when using exemplar-based prompting (Le Scao and Rush, 2021; Reynolds and McDonell, 2021; Zhao et al., 2021), all sets of chain of thought prompts outperform the standard baseline by a large margin. This result implies that successful use of chain of thought does not depend on a particular linguistic style.

To confirm that successful chain-of-thought prompting works for other sets of exemplars, the authors also run experiments with three sets of eight exemplars randomly sampled from the GSM8K training set, an independent source.

> Footnote 1: "For instance, whereas original chain of thought uses several short sentences ('There were originally 9 computers. For each of 4 days, 5 more computers were added. So 5 * 4 = 20 computers were added. 9 + 20 is 29.'), the concise chain of thought would read '5 * 4 = 20 new computers were added. So there are 9 + 20 = 29 new computers in the server room now'." [p. 6]

## Figure 6 [p. 6]

**Figure 6** (p. 6): "Chain-of-thought prompting has variance for different prompt examples (as expected) but outperforms standard prompting for various annotators as well as for different exemplars."

Bar chart with two groups (GSM8K on left, MAWPS on right), each showing solve rate (%) for multiple conditions:
- Standard prompting
- Chain-of-thought prompting (Annotator A, original)
- Different annotator (B)
- Different annotator (C)
- Intentionally concise style
- Exemplars from GSM8K (alpha)
- Exemplars from GSM8K (beta)
- Exemplars from GSM8K (gamma)

For GSM8K, solve rates range roughly from ~5% (standard prompting) to ~10--17% across the various chain-of-thought conditions. For MAWPS, solve rates range from roughly ~20% (standard prompting) to ~40--60% across chain-of-thought conditions. All chain-of-thought variants outperform standard prompting on both benchmarks.

---
[p. 7 continued]

These GSM8K training set exemplars (examples in this dataset already included reasoning steps like a chain of thought) performed comparably with the manually written exemplars and also substantially outperformed standard prompting. Footnote 2 notes: samples were limited to ≤ 60 tokens to fit into the input context window, and examples were limited to ≤ 2 steps to solve for a fair comparison with the eight manually composed exemplars.

In addition to robustness to annotators, independently-written chains of thought, different exemplars, and various language models, chain-of-thought prompting for arithmetic reasoning is also robust to different exemplar orders and varying numbers of exemplars (see Appendix A.2).
