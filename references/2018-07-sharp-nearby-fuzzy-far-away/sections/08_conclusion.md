# 8 Conclusion [p. 10]

The authors have empirically shown that a standard LSTM language model can effectively use about 200 tokens of context on two benchmark datasets, regardless of hyperparameter settings such as model size. [p. 10]

The model is sensitive to word order in the nearby context, but less so in the long-range context. [p. 10]

The model is able to regenerate words from nearby context, but heavily relies on caches to copy words from far away. [p. 10]

These findings not only help better understand these models but also suggest ways for improving them, as discussed in Section 7. [p. 10]

While observations in this paper are reported at the token level, deeper understanding of sentence-level interactions warrants further investigation, which is left to future work. [p. 10]

## Acknowledgments [p. 10]

The authors thank Arun Chaganty, Kevin Clark, Reid Pryzant, Yuhao Zhang and anonymous reviewers for their comments and suggestions. Support acknowledged from the DARPA Communicating with Computers (CwC) program under ARO prime contract no. W911NF15-1-0462 and the NSF via grant IIS-1514268. [p. 10]
