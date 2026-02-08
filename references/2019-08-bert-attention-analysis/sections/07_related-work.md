# 7 Related Work [p. 9-10]

There has been substantial recent work performing analysis to better understand what neural networks learn, especially from language model pre-training. [p. 9]

## Examining model outputs

One line of research examines the *outputs* of language models on carefully chosen input sentences (Linzen et al., 2016; Khandelwal et al., 2018; Gulordava et al., 2018; Marvin and Linzen, 2018). For example, the model's performance at subject-verb agreement (generating the correct number of a verb far away from its subject) provides a measure of the model's syntactic ability, although it does not reveal *how* that ability is captured by the network. [p. 9]

## Examining internal vector representations

Another line of work investigates the internal *vector representations* of the model (Adi et al., 2017; Giulianelli et al., 2018; Zhang and Bowman, 2018), often using probing classifiers. Probing classifiers are simple neural networks that take the vector representations of a pre-trained model as input and are trained to do a supervised task (e.g., part-of-speech tagging). If a probing classifier achieves high accuracy, it suggests the input representations reflect the corresponding aspect of language (e.g., low-level syntax). Like the current work, some of these studies have also demonstrated models capturing aspects of syntax (Shi et al., 2016; Blevins et al., 2018) or coreference (Tenney et al., 2018, 2019; Liu et al., 2019) without explicitly being trained for the tasks. [p. 9]

## Analyzing attention

With regards to analyzing attention, Vig (2019) builds a visualization tool for BERT's attention and reports observations about the attention behavior, but does not perform quantitative analysis. Burns et al. (2018) analyze the attention of memory networks to understand model performance on a question answering dataset. [p. 9]

There has also been some initial work in correlating attention with syntax: [p. 9]
- Raganato and Tiedemann (2018) evaluate the attention heads of a machine translation model on dependency parsing, but only report overall UAS scores instead of investigating heads for specific syntactic relations or using probing classifiers. [p. 9]
- Marecek and Rosa (2018) propose heuristic ways of converting attention scores to syntactic trees, but do not quantitatively evaluate their approach. [p. 9]

For coreference, Voita et al. (2018) show that the attention of a context-aware neural machine translation system captures anaphora, similar to the current paper's finding for BERT. [p. 9-10]

## Concurrent work

Concurrently with the current paper, Voita et al. (2019) identify syntactic, positional, and rare-word-sensitive attention heads in machine translation models. They also demonstrate that many attention heads can be pruned away without substantially hurting model performance. Interestingly, the important attention heads that remain after pruning tend to be ones with identified behaviors. Michel et al. (2019) similarly show that many of BERT's attention heads can be pruned. Although the current paper only found interpretable behaviors in a subset of BERT's attention heads, these recent works suggest that there might not be much to explain for some attention heads because they have little effect on model performance. [p. 10]

## Attention as explanation

Jain and Wallace (2019) argue that attention often does not "explain" model predictions. They show that attention weights frequently do not correlate with other measures of feature importance. Furthermore, attention weights can often be substantially changed without altering model predictions. However, the authors' motivation for looking at attention is different: rather than explaining model predictions, they are seeking to understand information learned by the models. For example, if a particular attention head learns a syntactic relation, they consider that an important finding from an analysis perspective even if that head is not always used when making predictions for some downstream task. [p. 10]
