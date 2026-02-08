# References

Only references cited in the section notes are included.

- **Adi et al., 2017:** Yossi Adi, Einat Kermany, Yonatan Belinkov, Ofer Lavi, and Yoav Goldberg. 2017. Fine-grained analysis of sentence embeddings using auxiliary prediction tasks. In *ICLR*.
  - Cited in 01_introduction.md and 07_related-work.md as an example of probing classifiers applied to internal vector representations.

- **Bahdanau et al., 2015:** Dzmitry Bahdanau, Kyunghyun Cho, and Yoshua Bengio. 2015. Neural machine translation by jointly learning to align and translate. In *ICLR*.
  - Cited in 01_introduction.md as the foundational work on attention mechanisms.

- **Belinkov et al., 2017:** Yonatan Belinkov, Nadir Durrani, Fahim Dalvi, Hassan Sajjad, and James R. Glass. 2017. What do neural machine translation models learn about morphology? In *ACL*.
  - Cited in 01_introduction.md as an example of probing classifiers applied to internal vector representations.

- **Blevins et al., 2018:** Terra Blevins, Omer Levy, and Luke S. Zettlemoyer. 2018. Deep rnns encode soft hierarchical syntax. In *ACL*.
  - Cited in 07_related-work.md as prior work demonstrating models capturing aspects of syntax without explicit training.

- **Burns et al., 2018:** Kaylee Burns, Aida Nematzadeh, Alison Gopnik, and Thomas L. Griffiths. 2018. Exploiting attention to reveal shortcomings in memory models. In *BlackboxNLP@EMNLP*.
  - Cited in 07_related-work.md as work analyzing attention of memory networks on a question answering dataset.

- **Chen et al., 2018:** Kehai Chen, Rui Wang, Masao Utiyama, Eiichiro Sumita, and Tiejun Zhao. 2018. Syntax-directed attention for neural machine translation. In *AAAI*.
  - Cited in 01_introduction.md as prior work proposing to incorporate syntactic information to improve attention.

- **Conneau et al., 2018:** Alexis Conneau, German Kruszewski, Guillaume Lample, Loic Barrault, and Marco Baroni. 2018. What you can cram into a single $&!#* vector: Probing sentence embeddings for linguistic properties. In *ACL*.
  - Cited in 05_probing-attention-head-combinations.md as showing that randomly initialized BERT with pre-trained embeddings is a surprisingly strong baseline for probing tasks.

- **Dai and Le, 2015:** Andrew M Dai and Quoc V Le. 2015. Semi-supervised sequence learning. In *NIPS*.
  - Cited in 01_introduction.md as an example of pre-trained language models achieving high accuracy on supervised tasks.

- **Devlin et al., 2019:** Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2019. BERT: Pre-training of deep bidirectional transformers for language understanding. In *NAACL-HLT*.
  - Cited in 01_introduction.md and 02_background.md as the model analyzed in this paper.

- **Eriguchi et al., 2016:** Akiko Eriguchi, Kazuma Hashimoto, and Yoshimasa Tsuruoka. 2016. Tree-to-sequence attentional neural machine translation. In *ACL*.
  - Cited in 01_introduction.md as prior work proposing to incorporate syntactic information to improve attention.

- **Giulianelli et al., 2018:** Mario Giulianelli, Jack Harding, Florian Mohnert, Dieuwke Hupkes, and Willem H. Zuidema. 2018. Under the hood: Using diagnostic classifiers to investigate and improve how language models track agreement information. In *BlackboxNLP@EMNLP*.
  - Cited in 07_related-work.md as work using probing classifiers to investigate internal vector representations.

- **Goldberg, 2019:** Yoav Goldberg. 2019. Assessing BERT's syntactic abilities. *arXiv preprint arXiv:1901.05287*.
  - Cited in 05_probing-attention-head-combinations.md as work drawing similar conclusions about BERT learning syntax from examining predictions on agreement tasks.

- **Gulordava et al., 2018:** Kristina Gulordava, Piotr Bojanowski, Edouard Grave, Tal Linzen, and Marco Baroni. 2018. Colorless green recurrent networks dream hierarchically. In *NAACL-HLT*.
  - Cited in 07_related-work.md as work examining model outputs on carefully chosen input sentences.

- **Hewitt and Manning, 2019:** John Hewitt and Christopher D. Manning. 2019. Finding syntax with structural probes. In *NAACL-HLT*.
  - Cited in 05_probing-attention-head-combinations.md and 07_related-work.md as work building structural probes on top of BERT's vector representations for syntax.

- **Jain and Wallace, 2019:** Sarthak Jain and Byron C. Wallace. 2019. Attention is not explanation. *arXiv preprint arXiv:1902.10186*.
  - Cited in 07_related-work.md as arguing that attention often does not "explain" model predictions and that attention weights frequently do not correlate with feature importance.

- **Khandelwal et al., 2018:** Urvashi Khandelwal, He He, Peng Qi, and Daniel Jurafsky. 2018. Sharp nearby, fuzzy far away: How neural language models use context. In *ACL*.
  - Cited in 07_related-work.md as work examining model outputs on carefully chosen input sentences.

- **Kruskal, 1964:** Joseph B Kruskal. 1964. Multidimensional scaling by optimizing goodness of fit to a nonmetric hypothesis. *Psychometrika*, 29(1):1-27.
  - Cited in 06_clustering-attention-heads.md as the source of the multidimensional scaling method used to embed attention heads.

- **Lee et al., 2011:** Heeyoung Lee, Yves Peirsman, Angel Chang, Nathanael Chambers, Mihai Surdeanu, and Dan Jurafsky. 2011. Stanford's multi-pass sieve coreference resolution system at the conll-2011 shared task. In *CoNLL*.
  - Cited in 04_probing-individual-heads.md as inspiration for the rule-based coreference baseline.

- **Linzen et al., 2016:** Tal Linzen, Emmanuel Dupoux, and Yoav Goldberg. 2016. Assessing the ability of lstms to learn syntax-sensitive dependencies. *TACL*.
  - Cited in 01_introduction.md and 07_related-work.md as an example of examining model outputs on carefully chosen input sentences.

- **Liu et al., 2019:** Nelson F. Liu, Matt Gardner, Yonatan Belinkov, M. Peters, and Noah A. Smith. 2019. Linguistic knowledge and transferability of contextual representations. In *NAACL-HLT*.
  - Cited in 05_probing-attention-head-combinations.md and 07_related-work.md as work demonstrating models capturing aspects of syntax/coreference and drawing similar conclusions about BERT learning syntax.

- **Marcus et al., 1993:** Mitchell P Marcus, Mary Ann Marcinkiewicz, and Beatrice Santorini. 1993. Building a large annotated corpus of english: The Penn treebank. *Computational linguistics*, 19(2):313-330.
  - Cited in 04_probing-individual-heads.md as the source of the WSJ dependency parsing evaluation data.

- **Marecek and Rosa, 2018:** David Marecek and Rudolf Rosa. 2018. Extracting syntactic trees from transformer encoder self-attentions. In *BlackboxNLP@EMNLP*.
  - Cited in 07_related-work.md as proposing heuristic ways of converting attention scores to syntactic trees without quantitative evaluation.

- **Marvin and Linzen, 2018:** Rebecca Marvin and Tal Linzen. 2018. Targeted syntactic evaluation of language models. In *EMNLP*.
  - Cited in 07_related-work.md as work examining model outputs on carefully chosen input sentences.

- **Michel et al., 2019:** Paul Michel, Omer Levy, and Graham Neubig. 2019. Are sixteen heads really better than one? *arXiv preprint arXiv:1905.10650*.
  - Cited in 07_related-work.md as showing that many of BERT's attention heads can be pruned.

- **Pennington et al., 2014:** Jeffrey Pennington, Richard Socher, and Christopher Manning. 2014. Glove: Global vectors for word representation. In *EMNLP*.
  - Cited in 05_probing-attention-head-combinations.md as the source of GloVe embeddings used in the attention-and-words probing classifier.

- **Peters et al., 2018:** Matthew E Peters, Mark Neumann, Mohit Iyyer, Matt Gardner, Christopher Clark, Kenton Lee, and Luke Zettlemoyer. 2018. Deep contextualized word representations. In *NAACL-HLT*.
  - Cited in 01_introduction.md as an example of pre-trained language models achieving high accuracy on supervised tasks.

- **Pradhan et al., 2012:** Sameer Pradhan, Alessandro Moschitti, Nianwen Xue, Olga Uryupina, and Yuchen Zhang. 2012. Conll-2012 shared task: Modeling multilingual unrestricted coreference in ontonotes. In *Joint Conference on EMNLP and CoNLL-Shared Task*.
  - Cited in 04_probing-individual-heads.md as the source of the CoNLL-2012 coreference resolution evaluation data.

- **Radford et al., 2018:** Alec Radford, Karthik Narasimhan, Tim Salimans, and Ilya Sutskever. 2018. Improving language understanding by generative pre-training. *https://blog.openai.com/language-unsupervised*.
  - Cited in 01_introduction.md as an example of pre-trained language models achieving high accuracy on supervised tasks.

- **Raganato and Tiedemann, 2018:** Alessandro Raganato and Jorg Tiedemann. 2018. An analysis of encoder representations in transformer-based machine translation. In *BlackboxNLP@EMNLP*.
  - Cited in 04_probing-individual-heads.md and 07_related-work.md as prior work that evaluates individual attention heads for syntax (overall UAS only).

- **Sennrich et al., 2016:** Rico Sennrich, Barry Haddow, and Alexandra Birch. 2016. Neural machine translation of rare words with subword units. In *ACL*.
  - Cited in 04_probing-individual-heads.md as the source of byte-pair tokenization used by BERT.

- **Shi et al., 2016:** Xing Shi, Inkit Padhi, and Kevin Knight. 2016. Does string-based neural mt learn source syntax? In *EMNLP*.
  - Cited in 07_related-work.md as prior work demonstrating models capturing aspects of syntax without explicit training.

- **Strubell et al., 2018:** Emma Strubell, Patrick Verga, Daniel Andor, David I Weiss, and Andrew McCallum. 2018. Linguistically-informed self-attention for semantic role labeling. In *EMNLP*.
  - Cited in 01_introduction.md as prior work proposing to incorporate syntactic information to improve attention.

- **Sundararajan et al., 2017:** Mukund Sundararajan, Ankur Taly, and Qiqi Yan. 2017. Axiomatic attribution for deep networks. In *ICML*.
  - Cited in 03_surface-level-patterns.md as the source of gradient-based feature importance measures used to analyze [SEP] attention.

- **Tenney et al., 2018:** Ian Tenney, Patrick Xia, Berlin Chen, Alex Wang, Adam Poliak, R Thomas McCoy, Najoung Kim, Benjamin Van Durme, Samuel R Bowman, Dipanjan Das, et al. 2018. What do you learn from context? Probing for sentence structure in contextualized word representations. In *ICLR*.
  - Cited in 07_related-work.md as demonstrating models capturing aspects of coreference without explicit training.

- **Tenney et al., 2019:** Ian Tenney, Dipanjan Das, and Ellie Pavlick. 2019. Bert rediscovers the classical nlp pipeline. *arXiv preprint arXiv:1905.05950*.
  - Cited in 07_related-work.md as demonstrating models capturing aspects of coreference without explicit training.

- **Tu et al., 2018:** Zhaopeng Tu, Baosong Yang, Michael R. Lyu, and Tong Zhang. 2018. Multi-head attention with disagreement regularization. In *EMNLP*.
  - Cited in 06_clustering-attention-heads.md as showing that encouraging attention heads to have different behaviors can improve Transformer performance at machine translation.

- **Vaswani et al., 2017:** Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and Illia Polosukhin. 2017. Attention is all you need. In *NIPS*.
  - Cited in 01_introduction.md and 02_background.md as the Transformer architecture that BERT is based on.

- **Vig, 2019:** Jesse Vig. 2019. Visualizing attention in transformer-based language models. *arXiv preprint arXiv:1904.02679*.
  - Cited in 07_related-work.md as building a visualization tool for BERT's attention without performing quantitative analysis.

- **Voita et al., 2018:** Elena Voita, Pavel Serdyukov, Rico Sennrich, and Ivan Titov. 2018. Context-aware neural machine translation learns anaphora resolution. In *ACL*.
  - Cited in 07_related-work.md as showing that attention of a context-aware neural machine translation system captures anaphora.

- **Voita et al., 2019:** Elena Voita, David Talbot, Fedor Moiseev, Rico Sennrich, and Ivan Titov. 2019. Analyzing multi-head self-attention: Specialized heads do the heavy lifting, the rest can be pruned. *arXiv preprint arXiv:1905.09418*.
  - Cited in 07_related-work.md as concurrent work identifying syntactic, positional, and rare-word-sensitive attention heads in machine translation models and showing many heads can be pruned.

- **Wiseman et al., 2015:** Sam Joshua Wiseman, Alexander Matthew Rush, Stuart Merrill Shieber, and Jason Weston. 2015. Learning anaphoricity and antecedent ranking features for coreference resolution. In *ACL*.
  - Cited in 04_probing-individual-heads.md as a neural coreference baseline system.

- **Zhang and Bowman, 2018:** Kelly W. Zhang and Samuel R. Bowman. 2018. Language modeling teaches you more syntax than translation does: Lessons learned through auxiliary task analysis. In *BlackboxNLP@EMNLP*.
  - Cited in 07_related-work.md as work using probing classifiers to investigate internal vector representations.
