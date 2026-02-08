# References

Only references that are cited substantively in the section notes are included here.

- **Alberti et al. (2019)** — Alberti, C., Lee, K., and Collins, M. A bert baseline for the natural questions. *arXiv preprint arXiv:1901.08634*, 2019. Cited in 03_experiments.md; open domain QA systems achieving 30-50% on Natural Questions.

- **Alcorn et al. (2018)** — Cited in 01_introduction.md; erratic behavior of image classifiers on diverse inputs.

- **Al-Rfou et al. (2018)** — Cited in 02_approach.md; byte-level LMs not competitive with word-level LMs on One Billion Word Benchmark.

- **Amodei et al. (2016)** — Cited in 01_introduction.md; example of supervised learning with large datasets and high-capacity models.

- **Artetxe et al. (2017)** — Artetxe, M., Labaka, G., Agirre, E., and Cho, K. Unsupervised neural machine translation. *arXiv preprint arXiv:1710.11041*, 2017. Cited in 03_experiments.md (Figure 1 caption and Translation section); WMT-14 Fr-En unsupervised MT baseline.

- **Artetxe et al. (2019)** — Artetxe, M., Labaka, G., and Agirre, E. An effective approach to unsupervised machine translation. *arXiv preprint arXiv:1902.01313*, 2019. Cited in 03_experiments.md; current best unsupervised MT approach achieving 33.5 BLEU.

- **Ba et al. (2016)** — Ba, J. L., Kiros, J. R., and Hinton, G. E. Layer normalization. *arXiv preprint arXiv:1607.06450*, 2016. Cited in 02_approach.md; layer normalization technique used in the model.

- **Bajgar et al. (2016)** — Bajgar, O., Kadlec, R., and Kleindienst, J. Embracing data abundance: Booktest dataset for reading comprehension. *arXiv preprint arXiv:1610.00956*, 2016. Cited in 03_experiments.md and 05_related-work.md; source of CBT SOTA results and human performance estimates; improved CBT results using larger Project Gutenberg dataset.

- **Barz & Denzler (2019)** — Barz, B. and Denzler, J. Do we train on test data? Purging CIFAR of near-duplicates. *arXiv preprint arXiv:1902.00423*, 2019. Cited in 04_generalization-vs-memorization.md; CIFAR-10 has 3.3% train-test overlap.

- **Bengio et al. (2003)** — Cited in 02_approach.md; foundational reference for factorizing joint probabilities as product of conditional probabilities.

- **Bowman et al. (2018)** — Cited in 01_introduction.md; one of the two most ambitious multitask learning efforts (17 dataset-objective pairs).

- **Caruana (1997)** — Cited in 01_introduction.md; multitask learning as a framework for improving general performance.

- **Chelba et al. (2013)** — Cited in 03_experiments.md; One Billion Word Benchmark, where GPT-2 is still significantly worse than prior work.

- **Collobert et al. (2011)** — Cited in 01_introduction.md; word vectors as inputs to task-specific architectures (early transfer learning).

- **Conneau et al. (2017a)** — Conneau, A., Kiela, D., Schwenk, H., Barrault, L., and Bordes, A. Supervised learning of universal sentence representations from natural language inference data. *arXiv preprint arXiv:1705.02364*, 2017a. Cited in 05_related-work.md; transfer performance of representations learned by NLI models.

- **Conneau et al. (2017b)** — Conneau, A., Lample, G., Ranzato, M., Denoyer, L., and Jegou, H. Word translation without parallel data. *arXiv preprint arXiv:1710.04087*, 2017b. Cited in 03_experiments.md; unsupervised word translation with bilingual lexicon, GPT-2 En-Fr BLEU slightly worse.

- **Dai & Le (2015)** — Dai, A. M. and Le, Q. V. Semi-supervised sequence learning. In *Advances in neural information processing systems*, pp. 3079-3087, 2015. Cited in 01_introduction.md and 05_related-work.md; transferring contextual representations of recurrent networks, RNN-based fine-tuning approaches.

- **Dai et al. (2019)** — Cited in 03_experiments.md (Table 3 caption); source of other SOTA results in Table 3.

- **Davies (2018)** — Davies, M. The 14 billion word iWeb corpus. https://corpus.byu.edu/iWeb/, 2018. Cited in 05_related-work.md; alternative approach to constructing large web text corpora.

- **Dehghani et al. (2018)** — Cited in 03_experiments.md; prior LM accuracy of 19% on LAMBADA.

- **Devlin et al. (2018)** — Devlin, J., Chang, M.-W., Lee, K., and Toutanova, K. BERT: Pre-training of deep bidirectional transformers for language understanding. *arXiv preprint arXiv:1810.04805*, 2018. Cited in 01_introduction.md (transferring self-attention blocks), 02_approach.md (largest BERT model equivalent to 345M GPT-2), 03_experiments.md (supervised SOTA on CoQA), 06_discussion.md (uni-directional representation inefficiencies).

- **Dinan et al. (2018)** — Dinan, E., Roller, S., Shuster, K., Fan, A., Auli, M., and Weston, J. Wizard of Wikipedia: Knowledge-powered conversational agents. *arXiv preprint arXiv:1811.01241*, 2018. Cited in 05_related-work.md; LM pre-training helpful for dialog-based QA systems.

- **Fan et al. (2018)** — Fan, A., Lewis, M., and Dauphin, Y. Hierarchical neural story generation. In *Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics*, 2018. Cited in 03_experiments.md; Top-k random sampling used for summarization generation.

- **Finn et al. (2017)** — Finn, C., Abbeel, P., and Levine, S. Model-agnostic meta-learning for fast adaptation of deep networks. *arXiv preprint arXiv:1703.03400*, 2017. Cited in 02_approach.md; MAML inner/outer loop optimization framework for task conditioning.

- **Gehrmann et al. (2018)** — Gehrmann, S., Deng, Y., and Rush, A. M. Bottom-up abstractive summarization. *arXiv preprint arXiv:1808.10792*, 2018. Cited in 03_experiments.md (Table 4 caption); Bottom-Up Sum SOTA model for summarization.

- **Gillick et al. (2015)** — Gillick, D., Brunk, C., Vinyals, O., and Subramanya, A. Multilingual language processing from bytes. *arXiv preprint arXiv:1512.00103*, 2015. Cited in 02_approach.md; processing Unicode strings as UTF-8 bytes.

- **Gong et al. (2018)** — Gong, C., He, D., Tan, X., Qin, T., Wang, L., and Liu, T.-Y. Frage: frequency-agnostic word representation. In *Advances in Neural Information Processing Systems*, pp. 1341-1352, 2018. Cited in 03_experiments.md (Table 3 caption); source of PTB and WikiText-2 SOTA results.

- **Grave et al. (2016)** — Grave, E., Joulin, A., and Usunier, N. Improving neural language models with a continuous cache. *arXiv preprint arXiv:1612.04426*, 2016. Cited in 03_experiments.md; LAMBADA perplexity SOTA of 99.8.

- **He et al. (2016)** — He, K., Zhang, X., Ren, S., and Sun, J. Identity mappings in deep residual networks. In *European conference on computer vision*, pp. 630-645. Springer, 2016. Cited in 02_approach.md; pre-activation residual network, similar to modified layer normalization placement.

- **Hestness et al. (2017)** — Hestness, J., Narang, S., Ardalani, N., Diamos, G., Jun, H., Kianinejad, H., Patwary, M., Ali, M., Yang, Y., and Zhou, Y. Deep learning scaling is predictable, empirically. *arXiv preprint arXiv:1712.00409*, 2017. Cited in 05_related-work.md; thorough analysis of performance as a function of model capacity and dataset size.

- **Hill et al. (2015)** — Hill, F., Bordes, A., Chopra, S., and Weston, J. The Goldilocks principle: Reading children's books with explicit memory representations. *arXiv preprint arXiv:1511.02301*, 2015. Cited in 03_experiments.md; Children's Book Test dataset.

- **Hill et al. (2016)** — Hill, F., Cho, K., and Korhonen, A. Learning distributed representations of sentences from unlabelled data. *arXiv preprint arXiv:1602.03483*, 2016. Cited in 05_related-work.md; research on learning representations.

- **Hoang et al. (2018)** — Hoang, L., Wiseman, S., and Rush, A. M. Entity tracking improves cloze-style reading comprehension. *arXiv preprint arXiv:1810.02891*, 2018. Cited in 03_experiments.md; LAMBADA accuracy SOTA using restricted prediction setting.

- **Howard & Ruder (2018)** — Howard, J. and Ruder, S. Universal language model fine-tuning for text classification. In *Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, volume 1, pp. 328-339, 2018. Cited in 05_related-work.md; improved RNN-based fine-tuning approaches of Dai & Le (2015).

- **Jelinek & Mercer (1980)** — Jelinek, F. and Mercer, R. L. Interpolated estimation of markov source parameters from sparse data. In *Proceedings of the Workshop on Pattern Recognition in Practice, Amsterdam, The Netherlands: North-Holland, May.*, 1980. Cited in 02_approach.md; foundational reference for factorizing joint probabilities over symbols.

- **Jia & Liang (2017)** — Jia, R. and Liang, P. Adversarial examples for evaluating reading comprehension systems. *arXiv preprint arXiv:1707.07328*, 2017. Cited in 01_introduction.md; erratic behavior of reading comprehension systems.

- **Jozefowicz et al. (2016)** — Jozefowicz, R., Vinyals, O., Schuster, M., Shazeer, N., and Wu, Y. Exploring the limits of language modeling. *arXiv preprint arXiv:1602.02410*, 2016. Cited in 02_approach.md and 05_related-work.md; prior work training LMs on news articles; scaled RNN-based LMs on 1BW Benchmark.

- **Kaiser et al. (2017)** — Kaiser, L., Gomez, A. N., Shazeer, N., Vaswani, A., Parmar, N., Jones, L., and Uszkoreit, J. One model to learn them all. *arXiv preprint arXiv:1706.05137*, 2017. Cited in 02_approach.md; task-specific encoders and decoders for task conditioning.

- **Karpathy et al. (2015)** — Karpathy, A., Johnson, J., and Fei-Fei, L. Visualizing and understanding recurrent neural networks. *arXiv preprint arXiv:1506.02078*, 2015. Cited in 05_related-work.md; RNN cells performing line-width tracking and quote/comment detection.

- **Kiros et al. (2015)** — Kiros, R., Zhu, Y., Salakhutdinov, R. R., Zemel, R., Urtasun, R., Torralba, A., and Fidler, S. Skip-thought vectors. In *Advances in neural information processing systems*, pp. 3294-3302, 2015. Cited in 02_approach.md and 05_related-work.md; prior work training LMs on fiction books; influential early work on deep representation learning for text.

- **Kirkpatrick et al. (2017)** — Kirkpatrick, J., Pascanu, R., Rabinowitz, N., Veness, J., Desjardins, G., Rusu, A. A., Milan, K., Quan, J., Ramalho, T., Grabska-Barwinska, A., et al. Overcoming catastrophic forgetting in neural networks. *Proceedings of the national academy of sciences*, pp. 201611835, 2017. Cited in 01_introduction.md; systems are sensitive to task specification changes.

- **Krizhevsky et al. (2012)** — Krizhevsky, A., Sutskever, I., and Hinton, G. E. Imagenet classification with deep convolutional neural networks. In *Advances in neural information processing systems*, pp. 1097-1105, 2012. Cited in 01_introduction.md; example of supervised learning with large datasets.

- **Kwiatkowski et al. (2019)** — Kwiatkowski, T., Palomaki, J., Rhinehart, O., Collins, M., Parikh, A., Alberti, C., Epstein, D., Polosukhin, I., Kelcey, D., Devlin, J., et al. Natural questions: a benchmark for question answering research. 2019. Cited in 03_experiments.md (Figure 1 caption and Question Answering section); Natural Questions dataset for factoid QA evaluation.

- **Lake et al. (2017)** — Lake, B. M., Ullman, T. D., Tenenbaum, J. B., and Gershman, S. J. Building machines that learn and think like people. *Behavioral and Brain Sciences*, 40, 2017. Cited in 01_introduction.md; erratic behavior of captioning models.

- **Lample et al. (2017)** — Lample, G., Conneau, A., Denoyer, L., and Ranzato, M. Unsupervised machine translation using monolingual corpora only. *arXiv preprint arXiv:1711.00043*, 2017. Cited in 03_experiments.md; unsupervised MT baseline outperformed by GPT-2 on Fr-En.

- **Levesque et al. (2012)** — Levesque, H., Davis, E., and Morgenstern, L. The Winograd schema challenge. In *Thirteenth International Conference on the Principles of Knowledge Representation and Reasoning*, 2012. Cited in 03_experiments.md; Winograd Schema Challenge dataset.

- **Levy & Goldberg (2014)** — Levy, O. and Goldberg, Y. Neural word embedding as implicit matrix factorization. In *Advances in neural information processing systems*, pp. 2177-2185, 2014. Cited in 05_related-work.md; understanding word representations.

- **Liu et al. (2018)** — Liu, P. J., Saleh, M., Pot, E., Goodrich, B., Sepassi, R., Kaiser, L., and Shazeer, N. Generating Wikipedia by summarizing long sequences. *arXiv preprint arXiv:1801.10198*, 2018. Cited in 05_related-work.md; model trained to generate Wikipedia articles also learned to translate names between languages.

- **McCann et al. (2017)** — McCann, B., Bradbury, J., Xiong, C., and Socher, R. Learned in translation: Contextualized word vectors. In *Advances in Neural Information Processing Systems*, pp. 6294-6305, 2017. Cited in 05_related-work.md; representations derived from machine translation models.

- **McCann et al. (2018)** — McCann, B., Keskar, N. S., Xiong, C., and Socher, R. The natural language decathlon: Multitask learning as question answering. *arXiv preprint arXiv:1806.08730*, 2018. Cited in 01_introduction.md (decaNLP benchmark, ambitious multitask effort) and 02_approach.md (MQAN model, language as flexible task specification).

- **Merity et al. (2016)** — Merity, S., Xiong, C., Bradbury, J., and Socher, R. Pointer sentinel mixture models. *arXiv preprint arXiv:1609.07843*, 2016. Cited in 02_approach.md; prior work training LMs on Wikipedia.

- **Mikolov et al. (2013)** — Mikolov, T., Sutskever, I., Chen, K., Corrado, G. S., and Dean, J. Distributed representations of words and phrases and their compositionality. In *Advances in neural information processing systems*, pp. 3111-3119, 2013. Cited in 01_introduction.md; word vectors as inputs to task-specific architectures.

- **Nallapati et al. (2016)** — Nallapati, R., Zhou, B., Gulcehre, C., Xiang, B., et al. Abstractive text summarization using sequence-to-sequence rnns and beyond. *arXiv preprint arXiv:1602.06023*, 2016. Cited in 03_experiments.md; CNN and Daily Mail summarization dataset.

- **Paperno et al. (2016)** — Paperno, D., Kruszewski, G., Lazaridou, A., Pham, Q. N., Bernardi, R., Pezzelle, S., Baroni, M., Boleda, G., and Fernandez, R. The LAMBADA dataset: Word prediction requiring a broad discourse context. *arXiv preprint arXiv:1606.06031*, 2016. Cited in 03_experiments.md; LAMBADA dataset for testing long-range dependencies.

- **Pennington et al. (2014)** — Pennington, J., Socher, R., and Manning, C. GloVe: Global vectors for word representation. In *Proceedings of the 2014 conference on empirical methods in natural language processing (EMNLP)*, pp. 1532-1543, 2014. Cited in 05_related-work.md; scaled word vector representation learning to all of Common Crawl.

- **Peters & Lecocq (2013)** — Peters, M. E. and Lecocq, D. Content extraction using diverse feature sets. In *Proceedings of the 22nd International Conference on World Wide Web*, pp. 89-90. ACM, 2013. Cited in 02_approach.md; Dragnet content extractor used for WebText.

- **Peters et al. (2018)** — Peters, M. E., Neumann, M., Iyyer, M., Gardner, M., Clark, C., Lee, K., and Zettlemoyer, L. Deep contextualized word representations. *arXiv preprint arXiv:1802.05365*, 2018. Cited in 01_introduction.md; transferring contextual representations (ELMo).

- **Radford et al. (2017)** — Radford, A., Jozefowicz, R., and Sutskever, I. Learning to generate reviews and discovering sentiment. *arXiv preprint arXiv:1704.01444*, 2017. Cited in 01_introduction.md; language models for sentiment analysis without supervised training.

- **Radford et al. (2018)** — Radford, A., Narasimhan, K., Salimans, T., and Sutskever, I. Improving language understanding by generative pre-training. 2018. Cited in 01_introduction.md (transferring self-attention blocks, GPT) and 02_approach.md (GPT model architecture that GPT-2 follows).

- **Ramachandran et al. (2016)** — Ramachandran, P., Liu, P. J., and Le, Q. V. Unsupervised pre-training for sequence to sequence learning. *arXiv preprint arXiv:1611.02683*, 2016. Cited in 05_related-work.md; seq2seq models benefit from pre-trained LM initialization.

- **Recht et al. (2018)** — Recht, B., Roelofs, R., Schmidt, L., and Shankar, V. Do cifar-10 classifiers generalize to cifar-10? *arXiv preprint arXiv:1806.00451*, 2018. Cited in 01_introduction.md; systems are brittle to data distribution changes.

- **Reddy et al. (2018)** — Reddy, S., Chen, D., and Manning, C. D. CoQA: A conversational question answering challenge. *arXiv preprint arXiv:1808.07042*, 2018. Cited in 03_experiments.md; CoQA dataset for reading comprehension.

- **Schwartz et al. (2017)** — Schwartz, R., Sap, M., Konstas, I., Zilles, L., Choi, Y., and Smith, N. A. Story cloze task: Uw nlp system. In *Proceedings of the 2nd Workshop on Linking Models of Lexical, Sentential and Discourse-level Semantics*, pp. 52-55, 2017. Cited in 01_introduction.md; language models for commonsense reasoning without supervised training.

- **See et al. (2017)** — See, A., Liu, P. J., and Manning, C. D. Get to the point: Summarization with pointer-generator networks. *arXiv preprint arXiv:1704.04368*, 2017. Cited in 03_experiments.md (Figure 1 caption); CNN and Daily Mail summarization reference.

- **Sennrich et al. (2015)** — Sennrich, R., Haddow, B., and Birch, A. Neural machine translation of rare words with subword units. *arXiv preprint arXiv:1508.07909*, 2015. Cited in 02_approach.md; Byte Pair Encoding method.

- **Subramanian et al. (2018)** — Subramanian, S., Trischler, A., Bengio, Y., and Pal, C. J. Learning general purpose distributed sentence representations via large scale multi-task learning. *arXiv preprint arXiv:1804.00079*, 2018. Cited in 05_related-work.md; explored large-scale multitask training.

- **Sutskever et al. (2014)** — Sutskever, I., Vinyals, O., and Le, Q. V. Sequence to sequence learning with neural networks. In *Advances in neural information processing systems*, pp. 3104-3112, 2014. Cited in 01_introduction.md; example of supervised learning with large datasets.

- **Sutskever et al. (2015)** — Sutskever, I., Jozefowicz, R., Gregor, K., Rezende, D., Lillicrap, T., and Vinyals, O. Towards principled unsupervised learning. *arXiv preprint arXiv:1511.06440*, 2015. Cited in 02_approach.md; concerns with density estimation as a principled training objective.

- **Trichelair et al. (2018)** — Trichelair, P., Emami, A., Cheung, J. C. K., Trischler, A., Suleman, K., and Diaz, F. On the evaluation of common-sense reasoning in natural language understanding. *arXiv preprint arXiv:1811.01778*, 2018. Cited in 03_experiments.md; recommended reading to contextualize Winograd Schema results.

- **Trinh & Le (2018)** — Trinh, T. H. and Le, Q. V. A simple method for commonsense reasoning. *arXiv preprint arXiv:1806.02847*, 2018. Cited in 02_approach.md (Common Crawl quality issues, commonsense reasoning) and 03_experiments.md (progress on Winograd Schema using LMs).

- **Vaswani et al. (2017)** — Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L., and Polosukhin, I. Attention is all you need. In *Advances in Neural Information Processing Systems*, pp. 5998-6008, 2017. Cited in 02_approach.md; Transformer self-attention architecture.

- **Vinyals & Le (2015)** — Vinyals, O. and Le, Q. A Neural Conversational Model. 2015. Cited in 03_experiments.md; prior qualitative results on factoid question answering in neural systems.

- **Vinyals et al. (2015)** — Vinyals, O., Fortunato, M., and Jaitly, N. Pointer networks. In *Advances in Neural Information Processing Systems*, 2015. Cited in 06_discussion.md; extractive pointer network outputs currently SOTA on many QA and reading comprehension datasets.

- **Wang et al. (2018)** — Wang, A., Singh, A., Michael, J., Hill, F., Levy, O., and Bowman, S. R. GLUE: A multi-task benchmark and analysis platform for natural language understanding. *arXiv preprint arXiv:1804.07461*, 2018. Cited in 01_introduction.md; GLUE benchmark for multitask evaluation.

- **Weston (2016)** — Weston, J. E. Dialog-based language learning. In *Neural Information Processing Systems*, pp. 829-837, 2016. Cited in 02_approach.md; argued for need to develop systems capable of learning from natural language directly, demonstrated learning QA from dialog.

- **Wieting & Kiela (2019)** — Wieting, J. and Kiela, D. No training required: Exploring random encoders for sentence classification. 2019. Cited in 05_related-work.md; critically evaluating representations of pre-training methods.

- **Wolf et al. (2019)** — Wolf, T., Sanh, V., Chaumond, J., and Delangue, C. TransferTransfo: A transfer learning approach for neural network based conversational agents. *arXiv preprint arXiv:1901.08149*, 2019. Cited in 05_related-work.md; LM pre-training helpful for chit-chat dialog generation.

- **Yogatama et al. (2019)** — Yogatama, D., d'Autume, C. d. M., Connor, J., Kocisky, T., Chrzanowski, M., Kong, L., Lazaridou, A., Ling, W., Yu, L., Dyer, C., et al. Learning and evaluating general linguistic intelligence. *arXiv preprint arXiv:1901.11373*, 2019. Cited in 01_introduction.md; recent multitask work reporting modest improvements.
