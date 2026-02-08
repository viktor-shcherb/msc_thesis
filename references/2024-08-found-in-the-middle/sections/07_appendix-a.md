# A Multi-doc QA datasets [p. 13]

[p. 13] The authors use NaturalQuestions (Kwiatkowski et al., 2019) (released in Apache-2.0 license) and SynthWiki (Peysakhovich and Lerer, 2023) to conduct the experiments. Both datasets contain question-answer pairs, a gold document containing the answer, and $K - 1$ distractor documents, where $K = 10$ and 20.

## NaturalQuestions

The NaturalQuestions dataset is the subset with 2655 queries selected by Liu et al. (2023) where the annotated long answer is a paragraph. The $k - 1$ distractor passages are Wikipedia chunks retrieved by Contriever (Izacard et al., 2022a) that are most relevant to the query but do not contain any of the annotated answers in NaturalQuestions. The distractor documents are presented in the context in order of decreasing relevance.

## SynthWiki

The SynthWiki dataset (Peysakhovich and Lerer, 2023) is a synthetic multi-doc QA dataset with 990 entries. All the documents in SynthWiki are GPT-4 generated Wikipedia paragraphs for fictional people, thus it can minimize the knowledge contamination issue from pre-training and ensure the LLMs can only use information from the provided context. The distractor documents are randomly sampled and randomly ordered in SynthWiki.

## Ethical considerations

NaturalQuestions is collected from public English Wikipedia articles and SynthWiki is collected by GPT-4 automatic generation of English fake Wikipedia articles. These two datasets should not contain any information that names or uniquely identifies individual people or offensive content. The authors ensure that the use of these two datasets was consistent with their intended purpose for academic research and in accordance with their specified licensing agreements.
