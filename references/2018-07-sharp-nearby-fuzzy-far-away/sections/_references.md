# References

Only references that are actually cited in the section notes are included below.

---

**Adi et al. (2017)**
Yossi Adi, Einat Kermany, Yonatan Belinkov, Ofer Lavi, and Yoav Goldberg. 2017. Fine-grained analysis of sentence embeddings using auxiliary prediction tasks. *International Conference on Learning Representations (ICLR)*.
Cited in: 01_introduction.md (LSTMs can remember sentence lengths, word identity, word order), 05_nearby-vs-long-range.md (word order awareness within a sentence), 06_to-cache-or-not.md (awareness of which words appear in context degrades with sequence length).

**Bahdanau et al. (2015)**
Dzmitry Bahdanau, Kyunghyun Cho, and Yoshua Bengio. 2015. Neural machine translation by jointly learning to align and translate. *International Conference on Learning Representations (ICLR)*.
Cited in: 06_to-cache-or-not.md (as an example of successful copy/attention mechanism).

**Boyd-Graber and Blei (2009)**
Jordan Boyd-Graber and David Blei. 2009. Syntactic topic models. In *Advances in neural information processing systems (NIPS)*, pages 185--192.
Cited in: 04_how-much-context.md (function words rely on less context than content words).

**Chelba et al. (2017)**
Ciprian Chelba, Mohammad Norouzi, and Samy Bengio. 2017. N-gram language modeling using recurrent neural network estimation. *arXiv preprint arXiv:1703.10724*.
Cited in: 07_discussion.md (showed 13 tokens of context yields ~8% perplexity increase on PTB, compared to 25% in this paper's setup).

**Dauphin et al. (2017)**
Yann N Dauphin, Angela Fan, Michael Auli, and David Grangier. 2017. Language modeling with gated convolutional networks. *International Conference on Machine Learning (ICML)*.
Cited in: 01_introduction.md (as a neural language model that outperforms n-gram models).

**Gal and Ghahramani (2016)**
Yarin Gal and Zoubin Ghahramani. 2016. A theoretically grounded application of dropout in recurrent neural networks. In *Advances in Neural Information Processing Systems (NIPS)*, pages 1019--1027.
Cited in: 09_appendix-a-hyperparameters.md (dropout on recurrent connections, embedding weights, and input/output connections).

**Ghosh et al. (2016)**
Shalini Ghosh, Oriol Vinyals, Brian Strope, Scott Roy, Tom Dean, and Larry Heck. 2016. Contextual lstm (clstm) models for large scale nlp tasks. *Workshop on Large-scale Deep Learning for Data Mining, KDD*.
Cited in: 07_discussion.md (memory models feeding explicit context representations to the LSTM).

**Grave et al. (2017a)**
Edouard Grave, Moustapha M Cisse, and Armand Joulin. 2017a. Unbounded cache model for online language modeling with open vocabulary. In *Advances in Neural Information Processing Systems (NIPS)*, pages 6044--6054.
Cited in: 01_introduction.md (as a neural language model), 06_to-cache-or-not.md (as an example of successful caching mechanism).

**Grave et al. (2017b)**
Edouard Grave, Armand Joulin, and Nicolas Usunier. 2017b. Improving Neural Language Models with a Continuous Cache. *International Conference on Learning Representations (ICLR)*.
Cited in: 01_introduction.md (the neural caching model), 06_to-cache-or-not.md (description of the cache model, replication of their setup).

**Graves (2013)**
Alex Graves. 2013. Generating sequences with recurrent neural networks. *arXiv preprint arXiv:1308.0850*.
Cited in: 01_introduction.md (as a neural language model).

**Hill et al. (2016)**
Felix Hill, Antoine Bordes, Sumit Chopra, and Jason Weston. 2016. The goldilocks principle: Reading children's books with explicit memory representations. *International Conference on Learning Representations (ICLR)*.
Cited in: 04_how-much-context.md (prior findings on context use consistent with this paper), 06_to-cache-or-not.md (as an example of successful caching mechanism).

**Hochreiter and Schmidhuber (1997)**
Sepp Hochreiter and Jurgen Schmidhuber. 1997. Long short-term memory. *Neural computation* 9(8):1735--1780.
Cited in: 04_how-much-context.md (LSTMs designed to capture long-range dependencies).

**Inan et al. (2017)**
Hakan Inan, Khashayar Khosravi, and Richard Socher. 2017. Tying word vectors and word classifiers: A loss framework for language modeling. *International Conference on Learning Representations (ICLR)*.
Cited in: 09_appendix-a-hyperparameters.md (weight tying between word embedding and softmax layers).

**Jozefowicz et al. (2016)**
Rafal Jozefowicz, Oriol Vinyals, Mike Schuster, Noam Shazeer, and Yonghui Wu. 2016. Exploring the limits of language modeling. *arXiv preprint arXiv:1602.02410*.
Cited in: 01_introduction.md (as a neural language model that outperforms n-gram models).

**Lau et al. (2017)**
Jey Han Lau, Timothy Baldwin, and Trevor Cohn. 2017. Topically Driven Neural Language Model. *Association for Computational Linguistics (ACL)*.
Cited in: 07_discussion.md (memory models feeding explicit context representations to the LSTM).

**Li et al. (2016)**
Jiwei Li, Xinlei Chen, Eduard Hovy, and Dan Jurafsky. 2016. Visualizing and understanding neural models in nlp. *North American Association of Computational Linguistics (NAACL)*.
Cited in: 01_introduction.md (LSTMs model negation and intensification).

**Linzen et al. (2016)**
Tal Linzen, Emmanuel Dupoux, and Yoav Goldberg. 2016. Assessing the ability of lstms to learn syntax-sensitive dependencies. *Transactions of the Association for Computational Linguistics (TACL)*.
Cited in: 01_introduction.md (LSTMs capture subject-verb agreement).

**Manning et al. (2014)**
Christopher Manning, Mihai Surdeanu, John Bauer, Jenny Finkel, Steven Bethard, and David McClosky. 2014. The stanford corenlp natural language processing toolkit. In *Proceedings of 52nd annual meeting of the association for computational linguistics: system demonstrations*, pages 55--60.
Cited in: 04_how-much-context.md (POS tags obtained using Stanford CoreNLP).

**Marcus et al. (1993)**
Mitchell P Marcus, Mary Ann Marcinkiewicz, and Beatrice Santorini. 1993. Building a large annotated corpus of english: The penn treebank. *Computational linguistics* 19(2):313--330.
Cited in: 03_approach.md (Penn Treebank dataset).

**Melis et al. (2018)**
Gabor Melis, Chris Dyer, and Phil Blunsom. 2018. On the State of the Art of Evaluation in Neural Language Models. *International Conference on Learning Representations (ICLR)*.
Cited in: 01_introduction.md (as a neural language model), 04_how-much-context.md (NLM performance sensitive to hyperparameters).

**Merity et al. (2017)**
Stephen Merity, Caiming Xiong, James Bradbury, and Richard Socher. 2017. Pointer Sentinel Mixture Models. *International Conference on Learning Representations (ICLR)*.
Cited in: 03_approach.md (WikiText-2 dataset), 06_to-cache-or-not.md (as an example of successful copy mechanism).

**Merity et al. (2018)**
Stephen Merity, Nitish Shirish Keskar, and Richard Socher. 2018. Regularizing and Optimizing LSTM Language Models. *International Conference on Learning Representations (ICLR)*.
Cited in: 01_introduction.md (standard LSTM language model used), 03_approach.md (model trained using Averaging SGD optimizer, code base), 09_appendix-a-hyperparameters.md (averaging SGD optimizer, default hyperparameter settings).

**Mikolov et al. (2010)**
Tomas Mikolov, Martin Karafiat, Lukas Burget, Jan Cernocky, and Sanjeev Khudanpur. 2010. Recurrent neural network based language model. In *Eleventh Annual Conference of the International Speech Communication Association*.
Cited in: 03_approach.md (Penn Treebank dataset preprocessing).

**Press and Wolf (2017)**
Ofir Press and Lior Wolf. 2017. Using the output embedding to improve language models. *European Chapter of the Association for Computational Linguistics*. http://aclweb.org/anthology/E17-2025.
Cited in: 09_appendix-a-hyperparameters.md (weight tying between word embedding and softmax layers).

**Wan et al. (2013)**
Li Wan, Matthew Zeiler, Sixin Zhang, Yann Le Cun, and Rob Fergus. 2013. Regularization of neural networks using dropconnect. In *International Conference on Machine Learning (ICML)*, pages 1058--1066.
Cited in: 09_appendix-a-hyperparameters.md (dropout on recurrent connections, embedding weights, and input/output connections).

**Wang and Cho (2016)**
Tian Wang and Kyunghyun Cho. 2016. Larger-Context Language Modelling with Recurrent Neural Network. *Association for Computational Linguistics (ACL)*.
Cited in: 04_how-much-context.md (prior findings on context use consistent with this paper).

**Yang et al. (2018)**
Zhilin Yang, Zihang Dai, Ruslan Salakhutdinov, and William W Cohen. 2018. Breaking the softmax bottleneck: a high-rank rnn language model. *International Conference on Learning Representations (ICLR)*.
Cited in: 01_introduction.md (as a neural language model that outperforms n-gram models).
