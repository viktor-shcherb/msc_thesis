# 1. Introduction [p. 1-2]

[p. 1] Prompting large language models performs well across many domains (Brown et al., 2020; Chowdhery et al., 2022, *inter alia*). However, most evaluation benchmarks provide only information relevant to the problem solution, unlike real-world situations where problems come with contextually related information that may or may not be relevant. [p. 1]

Studies in psychology have shown that irrelevant information may significantly decrease problem-solving accuracy in children and adults (Hoyer et al., 1979; Pasolunghi et al., 1999; Marzocchi et al., 2002, *inter alia*). [p. 1]

This work studies the *distractibility* of large language models for various prompting techniques: how is large language model prompting affected by irrelevant context, and what strategies can improve performance. [p. 1]

To measure distractibility, the authors construct the GSM-IC dataset, a grade-school math problem dataset derived from GSM8K (Cobbe et al., 2021) and introduce two different metrics. In contrast to prior work that creates benchmark variations by substituting sentences of the base problems with variations (Patel et al., 2021; Kumar et al., 2021, *inter alia*), GSM-IC keeps the base problem description and adds one irrelevant sentence that does not affect the solution of the problem (Table 1). [p. 1]

**Table 1** (p. 1): An example problem from GSM-IC. An irrelevant sentence (*italic and underlined*) that does not affect the standard answer is added immediately before the question.

| | Text |
|---|---|
| **Original Problem** | Jessica is six years older than Claire. In two years, Claire will be 20 years old. How old is Jessica now? |
| **Modified Problem** | Jessica is six years older than Claire. In two years, Claire will be 20 years old. *Twenty years ago, the age of Claire's father is 3 times of Jessica's age.* How old is Jessica now? |
| **Standard Answer** | 24 |

[p. 1] The authors use Codex (`code-davinci-002`) and GPT-3.5 (`text-davinci-003`) in the GPT3 model family to evaluate state-of-the-art prompting techniques on GSM-IC, including chain-of-thought prompting (CoT; Wei et al., 2022), zero-shot chain-of-thought prompting (0-CoT; Kojima et al., 2022), least-to-most prompting (LtM; Zhou et al., 2022), and prompting with programs (PROGRAM; Chowdhery et al., 2022). [p. 1-2]

[p. 2] Performance on GSM-IC greatly decreases compared to the original GSM8K (without irrelevant context). The authors then investigate several approaches to mitigate this weakness, including self-consistency (Wang et al., 2022c) and adding irrelevant information to the exemplars in the prompt. They also investigate the usage of task-specific instructions (Wei et al., 2021; Sanh et al., 2021; Ouyang et al., 2022; Suzgun et al., 2022; Chung et al., 2022), where they prepend an instruction sentence *"feel free to ignore irrelevant information in the problem description"* to the exemplars. [p. 2]

## Key Findings (summarized in introduction)

1. All investigated prompting techniques are sensitive to irrelevant information. Among the original problems that can be solved by baseline prompts with greedy decoding, no more than 18% of them can be consistently solved for all types of irrelevant information, showing that the large language model is easily distracted and produces inconsistent predictions when adding a small amount of irrelevant information to the problem description. [p. 2]

2. Self-consistency improves the performance of all prompting techniques on GSM-IC. The recall rate of the correct answer for GSM-IC is as high as 99.7% with 20 samples per problem, i.e., at least one of the 20 solutions result in the correct final answer, meaning that using multiple samples allows the model to almost always retrieve the correct answer. [p. 2]

3. Adding irrelevant information to the exemplars shown in the prompt consistently boosts the performance, and the same holds for adding an instruction to ignore irrelevant context. This suggests that language models are -- to some extent -- able to learn to ignore irrelevant information by following examples or instructions. [p. 2]

4. The authors identify different factors of the irrelevant information that affect the model's sensitivity to irrelevant context. Their breakdown analysis shows that varying the numbers in the irrelevant information does not notably change the model performance, while the degree of lexical overlap with the original problem description matters. [p. 2]

[p. 2] The authors state as contribution that filtering out irrelevant information is essential for handling real-world tasks. Their evaluation indicates that despite the strong performance on challenging reasoning problems, state-of-the-art language models still have fundamental weaknesses in context understanding and identifying the relevant information from the input. They suggest that future work should also consider model sensitivity to irrelevant context, in addition to solving more challenging problems. [p. 2]
