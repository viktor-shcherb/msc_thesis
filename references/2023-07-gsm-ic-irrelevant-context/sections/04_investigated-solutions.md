# 4. Investigated Solutions [p. 4-5]

This section reviews the investigated prompting techniques (Section 4.1), presents the formats of the prompts (Section 4.2), and introduces instructed prompting (Section 4.3). [p. 4]

## 4.1 Base Techniques

[p. 4] **Chain-of-thought prompting (CoT; Wei et al., 2022)** is a prompting technique that guides the language models to solve a problem in a step-by-step manner. By presenting exemplars that solve the corresponding problems with intermediate reasoning steps in the prompts, CoT significantly improves the reasoning performance over direct answer prediction without such intermediate reasoning steps. [p. 4]

**Zero-shot chain-of-thought prompting (0-CoT; Kojima et al., 2022)** is a variation of CoT where the prompt does not contain any exemplar. Instead, the model is prompted directly with the problem of interest followed by the instruction *"Let's think step by step:"*. [p. 4]

**Least-to-most prompting (LtM; Zhou et al., 2022)** teaches language models to (1) break down a problem into subproblems, and (2) solve those subproblems sequentially using CoT. The final answer is that to the last subproblem. [p. 4]

**Program prompts (PROGRAM; Chowdhery et al., 2022)** represent the arithmetic reasoning process as a program. Following prior work on solving GSM8K problems with code (Chowdhery et al., 2022; Gao et al., 2022; Chen et al., 2022), a Python program is included as the problem solution in the prompt, and the generated Python code is executed using an external Python interpreter to obtain the final answer. [p. 4]

**Self-consistency (SC; Wang et al., 2022c; Shi et al., 2022a)** may further boost the reasoning performance by marginalizing over intermediate reasoning steps that share the same final result. In practice, SC can be implemented by (1) sampling several solutions from the large language model and (2) taking the majority vote. SC is orthogonal to the above techniques and can be combined with any of them. [p. 4]

## 4.2 Prompt Design

[p. 4-5] For few-shot prompting techniques (i.e., CoT, LtM, and PROGRAM), the input prompt includes exemplar problems and their solutions before the problem of interest. Following Zhou et al. (2022) on exemplar creation, only one simple exemplar is used for the main experiments. This exemplar is either based on the [Original Problem] or the [Problem with Irrelevant Context], which allows investigating the effect of irrelevant information in the prompt exemplar. For 0-CoT, following Kojima et al. (2022), the problem of interest is presented directly followed by *"A: Let's think step by step:"*. [p. 4-5]

**Figure 2** (p. 5): "Prompt formats for the investigated techniques on the right, which are constructed from building blocks on the left (best viewed in color). The [Problem with Irrelevant Context] is obtained by adding an irrelevant sentence (*italic and underlined*) to the original problem description and it can be used as an alternative to the [Original Problem] in the prompts on the right. In these prompts, identifiers highlighted and wrapped by brackets (e.g., [Problem of Interest]) are replaced by the contents of the corresponding building blocks. The prompts for all settings can be found in Appendix C."

The figure shows building blocks on the left:
- **[Original Problem]:** "Q: Elsa has 5 apples. Anna has 2 more apples than Elsa. How many apples do they have together?"
- **[Problem with Irrelevant Context]:** "Q: Elsa has 5 apples. Anna has 2 more apples than Elsa. *Liz has 4 peaches.* How many apples do they have together?"
- **[CoT Solution]:** "A: Anna has 2 more apples than Elsa, so Anna has 2 + 5 = 7 apples. Elsa and Anna have 5 + 7 = 12 apples together. The answer is 12."
- **[LtM Solution]:** "A: Let's break down this problem: 1. How many apples does Anna have? 2. How many apples do Elsa and Anna have together? 1. Anna has 2 more apples than Elsa. So Anna has 2 + 5 = 7 apples. 2. Elsa and Anna have 5 + 7 = 12 apples together."
- **[PROGRAM Solution]:** "A: Let's solve the problem by a Python program: Elsa_apples = 5 / Anna_apples = 2 + Elsa_apples / Elsa_Anna_apples = Elsa_apples + Anna_apples / print(Elsa_Anna_apples)"

Prompt formats on the right:
- **CoT Prompt:** [Original Problem] / [CoT Solution] / Q: [Problem of Interest] / A:
- **0-CoT Prompt (No Exemplar Problem):** Q: [Problem of Interest] / A: Let's think step by step:
- **LtM Prompt:** [Original Problem] / [LtM Solution] / Q: [Problem of Interest] / A: Let's break down this problem:
- **PROGRAM Prompt:** [Original Problem] / [PROGRAM Solution] / Q: [Problem of Interest] / A: Let's solve the problem by a Python program:
- **Instructed CoT Prompt:** "Solve grade school math problems. Feel free to ignore irrelevant information given in the questions." / [Original Problem] / [CoT Solution] / Q: [Problem of Interest] / A:

## 4.3 Instructed Prompting

[p. 5] In addition to presenting irrelevant information in the exemplars, the authors also investigate whether natural language instructions help language models ignore irrelevant context and become less distracted. Extending the line of work (Suzgun et al., 2022; Sanh et al., 2021; Ouyang et al., 2022) that includes a general task description before exemplars, they add the sentence *"Solve grade school math problems. Feel free to ignore irrelevant information given in the questions."* before the exemplars in the prompt (Figure 2), which explicitly *instructs* the language model to ignore irrelevant information in the problem description. [p. 5]
