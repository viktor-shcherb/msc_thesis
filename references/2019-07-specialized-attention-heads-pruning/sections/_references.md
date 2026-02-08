# References

This file contains only those bibliography entries cited in the section notes.

---

**Vaswani et al. (2017)**
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin. "Attention Is All You Need." NeurIPS 2017, Los Angeles.
Cited in 01_introduction.md (Transformer as dominant paradigm, multi-head attention efficiency), 02_transformer-architecture.md (architecture description), 10_appendix-b.md (model parameter setup and optimizer).

**Bojar et al. (2018)**
Ondrej Bojar et al. WMT 2018 shared task on machine translation.
Cited in 01_introduction.md (Transformer achieving state-of-the-art results in shared translation tasks).

**Niehues et al. (2018)**
Jan Niehues et al. IWSLT 2018 shared task.
Cited in 01_introduction.md (Transformer achieving state-of-the-art results in shared translation tasks).

**Raganato and Tiedemann (2018)**
Alessandro Raganato and Jorg Tiedemann. "An Analysis of Encoder Representations in Transformer-Based Machine Translation." In *Proceedings of the 2018 EMNLP Workshop BlackboxNLP: Analyzing and Interpreting Neural Networks for NLP*, pages 287-297, Brussels, Belgium. ACL.
Cited in 01_introduction.md (prior attempts to investigate information learned by the encoder), 07_related-work.md (analysis of NMT representations for semantics; self-attention weights used to induce tree structures).

**Voita et al. (2018)**
Elena Voita, Pavel Serdyukov, Rico Sennrich, Ivan Titov. "Context-Aware Neural Machine Translation Learns Anaphora Resolution." In *Proceedings of the 56th Annual Meeting of the ACL (Volume 1: Long Papers)*, pages 1264-1274, Melbourne, Australia. ACL.
Cited in 01_introduction.md and 04_identifying-important-heads.md (prior analysis using average/maximum attention weights), 07_related-work.md (attention weight analysis of NMT models).

**Tang et al. (2018)**
Gongbo Tang, Mathias Muller, Annette Rios, Rico Sennrich. "Why Self-Attention? A Targeted Evaluation of Neural Machine Translation Architectures." In *Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing*, pages 4263-4272. ACL.
Cited in 01_introduction.md and 04_identifying-important-heads.md (prior analysis using maximum attention weights), 07_related-work.md (sensitivity to grammatical errors; attention weight analysis).

**Ding et al. (2017)**
Yanzhuo Ding, Yang Liu, Huanbo Luan, Maosong Sun. "Visualizing and Understanding Neural Machine Translation." In *Proceedings of the 55th Annual Meeting of the ACL (Volume 1: Long Papers)*, pages 1150-1159, Vancouver, Canada. ACL.
Cited in 01_introduction.md (layer-wise relevance propagation method), 04_identifying-important-heads.md (LRP method description), 09_appendix-a.md (formal rules for LRP followed from this work).

**Louizos et al. (2018)**
Christos Louizos, Max Welling, Diederik P. Kingma. "Learning Sparse Neural Networks through L0 Regularization." ICLR 2018.
Cited in 01_introduction.md (pruning method basis), 06_pruning-attention-heads.md (method for pruning heads, Hard Concrete distributions).

**Lison et al. (2018)**
Pierre Lison, Jorg Tiedemann, Milen Kouylekov. "OpenSubtitles2018: Statistical Rescoring of Sentence Alignments in Large, Noisy Parallel Corpora." LREC 2018.
Cited in 03_data-and-setting.md (OpenSubtitles2018 corpus for domain evaluation).

**Manning et al. (2014)**
Christopher D. Manning, Mihai Surdeanu, John Bauer, Jenny Finkel, Steven J. Bethard, David McClosky. "The Stanford CoreNLP Natural Language Processing Toolkit." ACL 2014 System Demonstrations.
Cited in 05b_syntactic-heads.md (dependency structure generation for syntactic head evaluation).

**Maddison et al. (2017)**
Chris J. Maddison, Andriy Mnih, Yee Whye Teh. "The Concrete Distribution: A Continuous Relaxation of Discrete Random Variables." ICLR 2017.
Cited in 06_pruning-attention-heads.md (Concrete/Gumbel softmax distribution for Hard Concrete).

**Jang et al. (2017)**
Eric Jang, Shixiang Gu, Ben Poole. "Categorical Reparameterization with Gumbel-Softmax." ICLR 2017.
Cited in 06_pruning-attention-heads.md (Gumbel softmax distribution for Hard Concrete).

**Kingma and Welling (2014)**
Diederik P. Kingma, Max Welling. "Auto-Encoding Variational Bayes." ICLR 2014.
Cited in 06_pruning-attention-heads.md (reparameterization trick for optimizing the objective).

**Rezende et al. (2014)**
Danilo Jimenez Rezende, Shakir Mohamed, Daan Wierstra. "Stochastic Backpropagation and Approximate Inference in Deep Generative Models." ICML 2014.
Cited in 06_pruning-attention-heads.md (reparameterization trick for optimizing the objective).

**Kaiser and Bengio (2018)**
Lukasz Kaiser, Samy Bengio. "Discrete Autoencoders for Sequence Models." *arXiv preprint arXiv:1801.09797*, 2018.
Cited in 06_pruning-attention-heads.md (prior use of noise and rectification for discretization).

**Zhu and Gupta (2017)**
Michael Zhu, Suyog Gupta. "To Prune, or Not to Prune: Exploring the Efficacy of Pruning for Model Compression." *arXiv preprint arXiv:1710.01878*, 2017.
Cited in 06_pruning-attention-heads.md (sparse architectures from pruning cannot be trained from scratch to same performance).

**Gale et al. (2019)**
Trevor Gale, Erich Elsen, Sara Hooker. "The State of Sparsity in Deep Neural Networks." *arXiv preprint*, 2019.
Cited in 06_pruning-attention-heads.md (sparse architectures from pruning cannot be trained from scratch to same performance).

**Belinkov et al. (2017a)**
Yonatan Belinkov, Nadir Durrani, Fahim Dalvi, Hassan Sajjad, James Glass. "What Do Neural Machine Translation Models Learn about Morphology?" In *Proceedings of the 55th Annual Meeting of the ACL (Volume 1: Long Papers)*, pages 861-872. ACL.
Cited in 07_related-work.md (analysis of NMT representations for morphology).

**Dalvi et al. (2017)**
Fahim Dalvi, Nadir Durrani, Hassan Sajjad, Yonatan Belinkov, Stephan Vogel. "Understanding and Improving Morphological Learning in the Neural Machine Translation Decoder." In *Proceedings of the Eighth International Joint Conference on Natural Language Processing (Volume 1: Long Papers)*, pages 142-151. Asian Federation of Natural Language Processing.
Cited in 07_related-work.md (analysis of NMT representations for morphology).

**Bisazza and Tump (2018)**
Arianna Bisazza, Clara Tump. "The Lazy Encoder: A Fine-Grained Analysis of the Role of Morphology in Neural Machine Translation." In *Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing*, pages 2871-2876, Brussels, Belgium. ACL.
Cited in 07_related-work.md (target language determines which information gets encoded; agrees with Section 5.2.2 results on subject-verb relation).

**Shi et al. (2016)**
Xing Shi, Inkit Padhi, Kevin Knight. "Does String-Based Neural MT Learn Source Syntax?" In *Proceedings of the 2016 Conference on Empirical Methods in Natural Language Processing*, pages 1526-1534. ACL.
Cited in 07_related-work.md (analysis of NMT representations for syntax).

**Hill et al. (2017)**
Felix Hill, Kyunghyun Cho, Sebastien Jean, Y Bengio. "The Representational Geometry of Word Meanings Acquired by Neural Machine Translation Models." *Machine Translation*, 31, 2017.
Cited in 07_related-work.md (analysis of NMT representations for semantics).

**Belinkov et al. (2017b)**
Yonatan Belinkov, Lluis Marquez, Hassan Sajjad, Nadir Durrani, Fahim Dalvi, James Glass. "Evaluating Layers of Representation in Neural Machine Translation on Part-of-Speech and Semantic Tagging Tasks." In *Proceedings of the Eighth International Joint Conference on Natural Language Processing (Volume 1: Long Papers)*, pages 1-10. Asian Federation of Natural Language Processing.
Cited in 07_related-work.md (analysis of NMT representations for semantics).

**Linzen et al. (2016)**
Tal Linzen, Emmanuel Dupoux, Yoav Goldberg. "Assessing the Ability of LSTMs to Learn Syntax-Sensitive Dependencies." *Transactions of the Association for Computational Linguistics*, 4:521-535, 2016.
Cited in 07_related-work.md (sensitivity to grammatical errors in language models).

**Gulordava et al. (2018)**
Kristina Gulordava, Piotr Bojanowski, Edouard Grave, Tal Linzen, Marco Baroni. "Colorless Green Recurrent Networks Dream Hierarchically." In *Proceedings of the 2018 Conference of the North American Chapter of the ACL: Human Language Technologies, Volume 1 (Long Papers)*, pages 1195-1205. ACL.
Cited in 07_related-work.md (sensitivity to grammatical errors).

**Tran et al. (2018)**
Ke Tran, Arianna Bisazza, Christof Monz. "The Importance of Being Recurrent for Modeling Hierarchical Structure." In *Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing*, pages 4731-4736. ACL.
Cited in 07_related-work.md (sensitivity to grammatical errors).

**Sennrich (2017)**
Rico Sennrich. "How Grammatical is Character-level Neural Machine Translation? Assessing MT Quality with Contrastive Translation Pairs." In *Proceedings of the 15th Conference of the European Chapter of the ACL: Volume 2, Short Papers*, pages 376-382, Valencia, Spain.
Cited in 07_related-work.md (sensitivity to grammatical errors).

**Ghader and Monz (2017)**
Hamidreza Ghader, Christof Monz. "What Does Attention in Neural Machine Translation Pay Attention To?" In *Proceedings of the Eighth International Joint Conference on Natural Language Processing (Volume 1: Long Papers)*, pages 30-39. Asian Federation of Natural Language Processing.
Cited in 07_related-work.md (attention weight analysis of NMT models).

**Bau et al. (2019)**
Anthony Bau, Yonatan Belinkov, Hassan Sajjad, Nadir Durrani, Fahim Dalvi, James Glass. "Identifying and Controlling Important Neurons in Neural Machine Translation." In *International Conference on Learning Representations*, New Orleans, 2019.
Cited in 07_related-work.md (method for identifying important individual neurons in NMT models).

**Bach et al. (2015)**
Sebastian Bach, Alexander Binder, Gregoire Montavon, Frederick Klauschen, Klaus-Robert Muller, Wojciech Samek. "On Pixel-Wise Explanations for Non-Linear Classifier Decisions by Layer-Wise Relevance Propagation." *PLoS ONE*, 10(7):e0130140, 2015.
Cited in 09_appendix-a.md (original LRP method designed for image classifiers).

**Sennrich et al. (2016)**
Rico Sennrich, Barry Haddow, Alexandra Birch. "Neural Machine Translation of Rare Words with Subword Units." In *Proceedings of the 54th Annual Meeting of the ACL (Volume 1: Long Papers)*, pages 1715-1725, Berlin, Germany. ACL.
Cited in 10_appendix-b.md (byte-pair encoding for data preprocessing).

**Popel and Bojar (2018)**
Martin Popel, Ondrej Bojar. "Training Tips for the Transformer Model." pages 43-70, 2018.
Cited in 10_appendix-b.md (Transformer performance depends heavily on batch size).

**Kingma and Ba (2015)**
Diederik Kingma, Jimmy Ba. "Adam: A Method for Stochastic Optimization." In *Proceedings of the International Conference on Learning Representations (ICLR 2015)*.
Cited in 10_appendix-b.md (Adam optimizer used for training).
