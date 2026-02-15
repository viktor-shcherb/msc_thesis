# APPENDIX E: IMPLEMENTATION DETAILS [p. 23–24]

## E.1 Experiment Setting [p. 23]

For reproducibility, the generation temperature is set to 0 [p. 23]. The authors use PyTorch (Ansel et al., 2024; Paszke et al., 2019), Transformers (Wolf et al., 2020), and vLLM (Kwon et al., 2023) for experiments [p. 23]. All experiments are launched with a single node of 8x A100 80G with SXM connection [p. 23]. 70B and 110B models are launched with 3x and 4x A100, and other model sizes can be launched with 1x A100 [p. 23].

## E.2 Molecule Generation and Math Reasoning Task Details [p. 23]

### Molecule Generation

In this task, the input contains several properties that are interchangeable, and LMs are asked to generate molecules that satisfy these properties [p. 23]. The authors train such an LM with QM9 (Ramakrishnan et al., 2014) dataset [p. 23]. The QM9 dataset collects over 130k 3D molecules with 3D structures (Li et al., 2024) calculated by density functional theory (DFT) [p. 23]. Each molecule in QM9 has less than 9 heavy atoms, and its chemical elements all belong to H, C, N, O, F [p. 23]. The authors take six quantum property values as the conditional input to LMs and train LMs to generate molecules with the conditioned quantum property values [p. 23]. They split the training dataset of QM9 to two subsets where each subset has 50k samples, and train LMs and an EGNN-based quantum property prediction models (Satorras et al., 2021) on these two subsets, respectively [p. 23].

The six quantum properties are: polarizability (alpha), HOMO energy (epsilon_HOMO), LUMO energy (epsilon_LUMO), HOMO-LUMO gap (Delta_epsilon), dipole moment (mu), and heat capacity at 298.15K (C_v) [p. 23]. The LM is a 8-layer Llama model with 8 attention heads and 768 hidden dimensions [p. 23].

To evaluate the performance, the authors sample 10000 sets of 6-property conditions, randomize the property order in each condition, and generate molecules conditioned on these property values by the trained LM, and compute the mean absolute difference (MAE) between the given property values and the property values of the generated molecules [p. 23]. Note that they use the trained EGNN-based property prediction models to calculate the property values of the generated molecules [p. 23].

### Math Reasoning

The authors use R-GSM (Chen et al., 2024a), a subset of GSM8K [p. 23]. This small dataset (which contains 220 problems) is designed to test LMs' performance with interchangeable premise orders [p. 23]. Problems in the dataset contain several conditions that do not have a progressive relationship [p. 23]. Therefore, their positions are interchangeable [p. 23]. The authors further clean this dataset to remove problems where conditions do not read smoothly after changing positions (e.g., use pronouns in the first condition but introduce names in the second condition), yielding a small set containing 95 problems [p. 23]. They test Qwen-1.5 models on this dataset [p. 23].

## E.3 Prompts [p. 23–24]

### LM-as-a-judge prompt

The authors use the prompts provided by RewardBench (Lambert et al., 2024a) official repo for the LM-as-a-judge task [p. 23]:

**System prompt:** "Please act as an impartial judge and evaluate the quality of the responses provided by two AI assistants to the user question displayed below. You should choose the assistant that follows the user's instructions and answers the user's question better. Your evaluation should consider factors such as the helpfulness, relevance, accuracy, depth, creativity, and level of detail of their responses. Begin your evaluation by comparing the two responses and provide a short explanation. Avoid any position biases and ensure that the order in which the responses were presented does not influence your decision. Do not allow the length of the responses to influence your evaluation. Do not favor certain names of the assistants. Be as objective as possible. After providing your explanation, output your final verdict by strictly following this format: '[[A]]' if assistant A is better, '[[B]]' if assistant B is better." [p. 23–24]

**User prompt:** [User Question] ... [The Start of Assistant A's Answer] ... [The End of Assistant A's Answer] [The Start of Assistant B's Answer] ... [The End of Assistant B's Answer] [p. 24]

### Retrieval-augmented QA prompt

The authors use the prompts of official repo (Liu et al., 2024) for the retrieval-augmented QA experiments [p. 24]:

**User Prompt:** "Write a high-quality one-sentence answer for the given question using only the provided search results (some of which might be irrelevant). Document (Title: ......): ...... ... Document (Title: ......): ...... Question: ......" [p. 24]

### Other tasks

Molecule generation does not need prompts [p. 24]. The authors use prompts in OpenAI/simple-evals to evaluate R-GSM dataset [p. 24].
