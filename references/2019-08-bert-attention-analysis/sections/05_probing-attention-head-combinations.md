# 5 Probing Attention Head Combinations [p. 6-8]

Since individual attention heads specialize to particular aspects of syntax, the model's overall "knowledge" about syntax is distributed across multiple attention heads. The authors now measure this overall ability by proposing a novel family of attention-based probing classifiers and applying them to dependency parsing. For these classifiers, the BERT attention outputs are treated as fixed, i.e., the authors do not back-propagate into BERT and only train a small number of parameters. [p. 6-7]

The probing classifiers are basically graph-based dependency parsers. Given an input word, the classifier produces a probability distribution over other words in the sentence indicating how likely each other word is to be the syntactic head of the current one. [p. 7]

## Attention-Only Probe [p. 7]

The first probe learns a simple linear combination of attention weights:

$$p(i|j) \propto \exp\left(\sum_{k=1}^{n} w_k \alpha_{ij}^k + u_k \alpha_{ji}^k\right)$$

where p(i|j) is the probability of word i being word j's syntactic head, alpha_{ij}^k is the attention weight from word i to word j produced by head k, and n is the number of attention heads. Both directions of attention are included: candidate head to dependent as well as dependent to candidate head. The weight vectors w and u are trained using standard supervised learning on the train set. [p. 7]

## Attention-and-Words Probe [p. 7]

Given the finding that heads specialize to particular syntactic relations, probing classifiers should benefit from having information about the input words. The authors build a model that sets the weights of the attention heads based on the GloVe (Pennington et al., 2014) embeddings for the input words. Intuitively, if the dependent and candidate head are "the" and "cat," the probing classifier should learn to assign most of the weight to head 8-11, which achieves excellent performance at the determiner relation. [p. 7]

The attention-and-words probing classifier assigns the probability of word i being word j's head as:

$$p(i|j) \propto \exp\left(\sum_{k=1}^{n} W_{k,:}(v_i \oplus v_j) \alpha_{ij}^k + U_{k,:}(v_i \oplus v_j) \alpha_{ji}^k\right)$$

Where v denotes GloVe embeddings and the circled-plus symbol denotes concatenation. The GloVe embeddings are held fixed in training, so only the two weight matrices W and U are learned. The dot product W_{k,:}(v_i + v_j) produces a word-sensitive weight for the particular attention head. [p. 7]

## Results [p. 7-8]

**Setup.** Methods are evaluated on the Penn Treebank dev set annotated with Stanford dependencies. [p. 7]

Three baselines are compared: [p. 7-8]
- A right-branching baseline that always predicts the head is to the dependent's right.
- A simple one-hidden-layer network that takes as input the GloVe embeddings for the dependent and candidate head as well as distance features between the two words.^5
- The attention-and-words probe, but with attention maps from a BERT network with pre-trained word/positional embeddings but randomly initialized other weights. This kind of baseline is surprisingly strong at other probing tasks (Conneau et al., 2018).

^5 Indicator features for short distances as well as continuous distance features, with distance ahead/behind treated separately to capture word order.

### Table 3

**Table 3** (p. 8): "Results of attention-based probing classifiers on dependency parsing. A simple model taking BERT attention maps and GloVe embeddings as input performs quite well. *Not directly comparable to our numbers; see text."

| Model                    | UAS     |
|--------------------------|---------|
| Structural probe         | 80 UUAS* |
| Right-branching          | 26      |
| Distances + GloVe        | 58      |
| Random Init Attn + GloVe | 30      |
| Attn                     | 61      |
| Attn + GloVe             | 77      |

The Attn + GloVe probing classifier substantially outperforms the baselines and achieves a decent UAS of 77, suggesting BERT's attention maps have a fairly thorough representation of English syntax. [p. 8]

As a rough comparison, the authors also report results from the structural probe from Hewitt and Manning (2019), which builds a probing classifier on top of BERT's vector representations rather than attention. The scores are not directly comparable because the structural probe only uses a single layer of BERT, produces undirected rather than directed parse trees, and is trained to produce the syntactic distance between words rather than directly predicting the tree structure. Nevertheless, the similarity in score to the Attn + GloVe probing classifier suggests there is not much more syntactic information in BERT's vector representations compared to its attention maps. [p. 8]

Overall, the results from probing both individual and combinations of attention heads suggest that BERT learns some aspects of syntax purely as a by-product of self-supervised training. Other work has drawn a similar conclusion from examining BERT's predictions on agreement tasks (Goldberg, 2019) or internal vector representations (Hewitt and Manning, 2019; Liu et al., 2019). Traditionally, syntax-aware models have been developed through architecture design (e.g., recursive neural networks) or from direct supervision from human-curated treebanks. The authors' findings are part of a growing body of work indicating that indirect supervision from rich pre-training tasks like language modeling can also produce models sensitive to language's hierarchical structure. [p. 8]
