# 4 Probing Individual Attention Heads [p. 4-6]

The authors investigate individual attention heads to probe what aspects of language they have learned. They evaluate attention heads on labeled datasets for tasks like dependency parsing. An overview of results is shown in Figure 5. [p. 4]

## 4.1 Method [p. 4]

BERT uses byte-pair tokenization (Sennrich et al., 2016), which means some words (~8% in their data) are split up into multiple tokens. The authors therefore convert token-token attention maps to word-word attention maps: [p. 4]

- For attention *to* a split-up word: sum up the attention weights over its tokens. [p. 4]
- For attention *from* a split-up word: take the mean of the attention weights over its tokens. [p. 4]

These transformations preserve the property that the attention from each word sums to 1. For a given attention head and word, they take whichever other word receives the most attention weight as that model's prediction. [SEP] and [CLS] are ignored, although in practice this does not significantly change the accuracies for most heads. [p. 4]

## 4.2 Dependency Syntax [p. 4-6]

**Setup.** Attention maps are extracted from BERT on the Wall Street Journal portion of the Penn Treebank (Marcus et al., 1993) annotated with Stanford Dependencies. Both "directions" of prediction are evaluated for each attention head: the head word attending to the dependent and the dependent attending to the head word. Some dependency relations are simpler to predict than others: for example a noun's determiner is often the immediately preceding word. Therefore as a point of comparison, predictions from a simple fixed-offset baseline are shown. For example, a fixed offset of -2 means the word two positions to the left of the dependent is always considered to be the head. [p. 4-5]

**Results.** [p. 5-6]

No single attention head does well at syntax "overall"; the best head gets 34.5 UAS, which is not much better than the right-branching baseline, which gets 26.3 UAS. This finding is similar to the one reported by Raganato and Tiedemann (2018), who also evaluate individual attention heads for syntax. [p. 5]

However, certain attention heads specialize to specific dependency relations, sometimes achieving high accuracy and substantially outperforming the fixed-offset baseline. For all relations in Table 1 except `pobj`, the dependent attends to the head word rather than the other way around, likely because each dependent has exactly one head but heads have multiple dependents. [p. 6]

Heads can disagree with standard annotation conventions while still performing syntactic behavior. For example, head 7-6 marks 's as the dependent for the `poss` relation, while gold-standard labels mark the complement of an 's as the dependent (the accuracy in Table 1 counts 's as correct). [p. 6]

### Table 1

**Table 1** (p. 6): "The best performing attentions heads of BERT on WSJ dependency parsing by dependency type. Numbers after baseline accuracies show the best offset found (e.g., (1) means the word to the right is predicted as the head). We show the 10 most common relations as well as 5 other ones attention heads do well on. Bold highlights particularly effective heads."

| Relation | Head | Accuracy | Baseline |
|----------|------|----------|----------|
| All      | 7-6  | 34.5     | 26.3 (1) |
| prep     | 7-4  | 66.7     | 61.8 (-1) |
| pobj     | 9-6  | **76.3** | 34.6 (-2) |
| det      | 8-11 | **94.3** | 51.7 (1) |
| nn       | 4-10 | 70.4     | 70.2 (1) |
| nsubj    | 8-2  | 58.5     | 45.5 (1) |
| amod     | 4-10 | 75.6     | 68.3 (1) |
| dobj     | 8-10 | **86.8** | 40.0 (-2) |
| advmod   | 7-6  | 48.8     | 40.2 (1) |
| aux      | 4-10 | 81.1     | 71.5 (1) |
| poss     | 7-6  | **80.5** | 47.7 (1) |
| auxpass  | 4-10 | **82.5** | 40.5 (1) |
| ccomp    | 8-1  | **48.8** | 12.4 (-2) |
| mark     | 8-2  | **50.7** | 14.5 (2) |
| prt      | 6-7  | **99.1** | 91.4 (-1) |

**Figure 5** (p. 5): "BERT attention heads that correspond to linguistic phenomena. In the example attention maps, the darkness of a line indicates the strength of the attention weight. All attention to/from red words is colored red; these colors are there to highlight certain parts of the attention heads' behaviors. For Head 9-6, we don't show attention to [SEP] for clarity. Despite not being explicitly trained on these tasks, BERT's attention heads perform remarkably well, illustrating how syntax-sensitive behavior can emerge from self-supervised training alone."

Six attention head examples are shown:
- **Head 8-10:** Direct objects attend to their verbs. 86.8% accuracy at the `dobj` relation.
- **Head 8-11:** Noun modifiers (e.g., determiners) attend to their noun. 94.3% accuracy at the `det` relation.
- **Head 7-6:** Possessive pronouns and apostrophes attend to the head of the corresponding NP. 80.5% accuracy at the `poss` relation.
- **Head 4-10:** Passive auxiliary verbs attend to the verb they modify. 82.5% accuracy at the `auxpass` relation.
- **Head 9-6:** Prepositions attend to their objects. 76.3% accuracy at the `pobj` relation.
- **Head 5-4:** Coreferent mentions attend to their antecedents. 65.1% accuracy at linking the head word of a coreferent mention to the head of one of that mention's antecedents.

The authors note the similarity between machine-learned attention weights and human-defined syntactic relations is striking, but these are relations for which attention heads do particularly well. For many relations, BERT only slightly improves over the simple baseline, so individual attention heads do not capture dependency structure as a whole. [p. 6]

## 4.3 Coreference Resolution [p. 6]

**Setup.** The authors evaluate attention heads on coreference resolution using the CoNLL-2012 dataset (Pradhan et al., 2012). They compute antecedent selection accuracy: what percent of the time the head word of a coreferent mention most attends to the head of one of that mention's antecedents. Documents are truncated to 128 tokens to keep memory usage manageable. [p. 6]

Three baselines are compared:
- Picking the nearest other mention. [p. 6]
- Picking the nearest other mention with the same head word as the current mention. [p. 6]
- A simple rule-based system inspired by Lee et al. (2011). It proceeds through 4 sieves: (1) full string match, (2) head word match, (3) number/gender/person match, (4) all other mentions. The nearest mention satisfying the earliest sieve is returned. [p. 6]

The performance of a recent neural coreference system from Wiseman et al. (2015) is also shown. [p. 6]

**Results.** Results are shown in Table 2. One of BERT's attention heads achieves decent coreference resolution performance, improving by over 10 accuracy points on the string-matching baseline and performing close to the rule-based system. It is particularly good with nominal mentions, perhaps because it is capable of fuzzy matching between synonyms as seen in the bottom right of Figure 5. [p. 6-7]

### Table 2

**Table 2** (p. 7): "Accuracies (%) for systems at selecting a correct antecedent given a coreferent mention in the CoNLL-2012 data. One of BERT's attention heads performs fairly well at coreference."

| Model        | All  | Pronoun | Proper | Nominal |
|--------------|------|---------|--------|---------|
| Nearest      | 27   | 29      | 29     | 19      |
| Head match   | 52   | 47      | 67     | 40      |
| Rule-based   | 69   | 70      | 77     | 60      |
| Neural coref | 83*  | –       | –      | –       |
| Head 5-4     | **65** | 64    | 73     | 58      |

*Only roughly comparable because on non-truncated documents and with different mention detection.
