# 7 Related Work [p. 9–10]

## Analysis of NMT representations [p. 9]

One popular approach to the analysis of NMT representations is to evaluate how informative they are for various linguistic tasks. Different levels of linguistic analysis have been considered including morphology (Belinkov et al., 2017a; Dalvi et al., 2017; Bisazza and Tump, 2018), syntax (Shi et al., 2016) and semantics (Hill et al., 2017; Belinkov et al., 2017b; Raganato and Tiedemann, 2018). [p. 9]

Bisazza and Tump (2018) showed that the target language determines which information gets encoded. This agrees with the results in Section 5.2.2 of this paper, where the authors observed that attention heads are more likely to track syntactic relations requiring more complex agreement in the target language (in this case the subject-verb relation). [p. 9]

## Sensitivity to grammatical errors [p. 9]

An alternative method to study the ability of language models and machine translation models to capture hierarchical information is to test their sensitivity to specific grammatical errors (Linzen et al., 2016; Gulordava et al., 2018; Tran et al., 2018; Sennrich, 2017; Tang et al., 2018). While this line of work has shown that NMT models, including the Transformer, do learn some syntactic structures, the current work provides further insight into the role of multi-head attention. [p. 9]

## Attention weight analysis [p. 9–10]

There are several works analyzing attention weights of different NMT models (Ghader and Monz, 2017; Voita et al., 2018; Tang et al., 2018; Raganato and Tiedemann, 2018). Raganato and Tiedemann (2018) use the self-attention weights of the Transformer's encoder to induce a tree structure for each sentence and compute the unlabeled attachment score of these trees. However, they do not evaluate specific syntactic relations (i.e. labeled attachment scores) or consider how different heads specialize to specific dependency relations. [p. 9–10]

## Individual neuron analysis [p. 10]

Recently Bau et al. (2019) proposed a method for identifying important individual neurons in NMT models. They show that similar important neurons emerge in different models. Rather than verifying the importance of individual neurons, the current work identifies the importance of entire attention heads using layer-wise relevance propagation and verifies findings by observing which heads are retained when pruning the model. [p. 10]
