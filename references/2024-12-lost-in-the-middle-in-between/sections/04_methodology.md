# 4 Methodology [p. 4]

For each question in the datasets (and their context-reduced variants), we create multiple prompts by positioning evidence documents at various locations within a total of 20 documents, following the approach outlined by Liu et al. (2024). Given the high number of potential combinations of evidence positions (${20 \choose n}$ = 190, 1140, 4845 possible orderings per prompt in our 2-, 3-, and 4-hop settings, where $n$ represents the number of document positions and $k$ the number of evidence documents), we select a subset of combinations to manage the computational cost of generating long-context prompts.

Specifically, we choose 5 combinations where the gold documents are placed adjacent to one another, as well as 4 combinations with distractor documents interspersed between the gold documents for 2- and 4-hop questions, and 3 combinations for 3-hop questions. The distractor documents are retained in their original order, based on their relevance determined through the retrieval process.

The prompts are processed by the models with a temperature setting of 0, and the generation is limited to a maximum of 256 tokens.
