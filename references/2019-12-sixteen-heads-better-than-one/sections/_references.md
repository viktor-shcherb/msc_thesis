# References

Only references cited in the section notes are included here.

---

**Ahmed et al., 2017**
Karim Ahmed, Nitish Shirish Keskar, and Richard Socher. Weighted transformer network for machine translation. *arXiv preprint arXiv:1711.02132*, 2017.
- Cited in 01_introduction.md as an extension to MHA methodology.

**Bahdanau et al., 2015**
Dzmitry Bahdanau, Kyunghyun Cho, and Yoshua Bengio. Neural machine translation by jointly learning to align and translate. In *Proceedings of the International Conference on Learning Representations (ICLR)*, 2015.
- Cited in 01_introduction.md and 07_related-work.md as the standard attention mechanism that the Transformer extends.

**Cho et al., 2014**
Kyunghyun Cho, Bart van Merrienboer, Caglar Gulcehre, Dzmitry Bahdanau, Fethi Bougares, Holger Schwenk, and Yoshua Bengio. Learning phrase representations using rnn encoder-decoder for statistical machine translation. In *Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, pages 1724-1734, 2014.
- Cited in 01_introduction.md and 07_related-work.md as the standard attention mechanism that the Transformer extends.

**Devlin et al., 2018**
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. Bert: Pre-training of deep bidirectional transformers for language understanding. In *Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL-HLT)*, 2018.
- Cited in 01_introduction.md for question answering; in 01_introduction.md and 03_are-all-attention-heads-important.md as the BERT model used in experiments; in 07_related-work.md as an adopter of MHA for transfer learning.

**Hassibi and Stork, 1993**
Babak Hassibi and David G. Stork. Second order derivatives for network pruning: Optimal brain surgeon. In *Proceedings of the 5th Annual Conference on Neural Information Processing Systems (NIPS)*, pages 164-171, 1993.
- Cited in 04_iterative-pruning.md and 07_related-work.md as prior work on pruning neural networks.

**Koehn, 2004**
Philipp Koehn. Statistical significance tests for machine translation evaluation. In *Proceedings of the 2004 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, pages 388-395, 2004.
- Cited in 03_are-all-attention-heads-important.md for paired bootstrap resampling significance test.

**Koehn et al., 2007**
Philipp Koehn, Hieu Hoang, Alexandra Birch, Chris Callison-Burch, Marcello Federico, Nicola Bertoldi, Brooke Cowan, Wade Shen, Christine Moran, Richard Zens, Chris Dyer, Ondrej Bojar, Alexandra Constantin, and Evan Herbst. Moses: Open source toolkit for statistical machine translation. In *Proceedings of the 45th Annual Meeting of the Association for Computational Linguistics (ACL)*, pages 177-180, 2007.
- Cited in 03_are-all-attention-heads-important.md for tokenized BLEU scoring.

**LeCun et al., 1990**
Yann LeCun, John S. Denker, and Sara A. Solla. Optimal brain damage. In *Proceedings of the 2nd Annual Conference on Neural Information Processing Systems (NIPS)*, pages 598-605, 1990.
- Cited in 04_iterative-pruning.md and 07_related-work.md as prior work on pruning neural networks.

**Luong et al., 2015**
Thang Luong, Hieu Pham, and Christopher D. Manning. Effective approaches to attention-based neural machine translation. In *Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, pages 1412-1421, 2015.
- Cited in 02_background.md as the scaled bilinear attention variant used in MHA; in 07_related-work.md as the formulation most contemporaneous implementations are based on.

**Michel and Neubig, 2018**
Paul Michel and Graham Neubig. MTNT: A testbed for machine translation of noisy text. In *Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, pages 543-553, 2018.
- Cited in 03_are-all-attention-heads-important.md as the out-of-domain test set (MTNT) for WMT.

**Molchanov et al., 2017**
Pavlo Molchanov, Stephen Tyree, Tero Karras, Timo Aila, and Jan Kautz. Pruning convolutional neural networks for resource efficient inference. In *Proceedings of the International Conference on Learning Representations (ICLR)*, 2017.
- Cited in 04_iterative-pruning.md as prior work on pruning; the head importance score $I_h$ is equivalent to their Taylor expansion method. Their recommendation to normalize importance scores by layer is followed. Also cited in 07_related-work.md as structured pruning approach.

**Neubig et al., 2019**
Graham Neubig, Zi-Yi Dou, Junjie Hu, Paul Michel, Danish Pruthi, and Xinyi Wang. compare-mt: A tool for holistic comparison of language generation systems. In *Meeting of the North American Chapter of the Association for Computational Linguistics (NAACL) Demo Track*, Minneapolis, USA, June 2019.
- Cited in 03_are-all-attention-heads-important.md for the `compare-mt` statistical significance tool.

**Ott et al., 2018**
Myle Ott, Sergey Edunov, David Grangier, and Michael Auli. Scaling neural machine translation. In *Proceedings of the 3rd Conference on Machine Translation (WMT)*, pages 1-9, 2018.
- Cited in 01_introduction.md for machine translation performance; in 03_are-all-attention-heads-important.md as the pretrained WMT model used in experiments.

**Radford et al., 2018**
Alec Radford, Karthik Narasimhan, Time Salimans, and Ilya Sutskever. Improving language understanding with unsupervised learning. Technical report, Technical report, OpenAI, 2018.
- Cited in 01_introduction.md for text classification; in 07_related-work.md as an adopter of MHA for transfer learning.

**Raganato and Tiedemann, 2018**
Alessandro Raganato and Jorg Tiedemann. An analysis of encoder representations in transformer-based machine translation. In *Proceedings of the Workshop on BlackboxNLP: Analyzing and Interpreting Neural Networks for NLP*, pages 287-297, 2018.
- Cited in 01_introduction.md for showing that some heads are predictive of dependency structures.

**Shen et al., 2018**
Tao Shen, Tianyi Zhou, Guodong Long, Jing Jiang, Shirui Pan, and Chengqi Zhang. Disan: Directional self-attention network for rnn/cnn-free language understanding. In *Proceedings of the 32nd Meeting of the Association for Advancement of Artificial Intelligence (AAAI)*, 2018.
- Cited in 01_introduction.md as an extension to MHA methodology.

**Strubell et al., 2018**
Emma Strubell, Patrick Verga, Daniel Andor, David Weiss, and Andrew McCallum. Linguistically-informed self-attention for semantic role labeling. In *Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, pages 5027-5038, 2018.
- Cited in 01_introduction.md and 07_related-work.md for semantic role labeling.

**Tang et al., 2018**
Gongbo Tang, Mathias Muller, Annette Rios, and Rico Sennrich. Why self-attention? a targeted evaluation of neural machine translation architectures. In *Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, pages 4263-4272, 2018.
- Cited in 01_introduction.md for showing MHA can help with subject-verb agreement.

**Vaswani et al., 2017**
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Lukasz Kaiser, and Illia Polosukhin. Attention is all you need. In *Proceedings of the 30th Annual Conference on Neural Information Processing Systems (NIPS)*, pages 5998-6008, 2017.
- Cited in 01_introduction.md as the Transformer architecture; in 02_background.md for the concatenation formulation of MHA and non-linear feed-forward networks; in 03_are-all-attention-heads-important.md as the "large" transformer architecture used for WMT experiments; in 07_related-work.md as the introduction of multi-headed attention.

**Williams et al., 2018**
Adina Williams, Nikita Nangia, and Samuel Bowman. A broad-coverage challenge corpus for sentence understanding through inference. In *Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL-HLT)*, pages 1112-1122, 2018.
- Cited in 03_are-all-attention-heads-important.md as the MultiNLI dataset used for BERT evaluation.

**Anwar et al., 2017**
Sajid Anwar, Kyuyeon Hwang, and Wonyong Sung. Structured pruning of deep convolutional neural networks. *J. Emerg. Technol. Comput. Syst.*, pages 32:1-32:18, 2017.
- Cited in 07_related-work.md as a structured pruning approach.

**Binder et al., 2016**
Alexander Binder, Gregoire Montavon, Sebastian Lapuschkin, Klaus-Robert Muller, and Wojciech Samek. Layer-wise relevance propagation for neural networks with local renormalization layers. In *International Conference on Artificial Neural Networks*, pages 63-71, 2016.
- Cited in 07_related-work.md as the LRP method used by Voita et al. (2019) for determining important heads.

**Cettolo et al., 2015**
Mauro Cettolo, Jan Niehues, Sebastian Stuker, Luisa Bentivogli, and Marcello Federico. Report on the 11th iwslt evaluation campaign, iwslt 2014. In *Proceedings of the 2014 International Workshop on Spoken Language Translation (IWSLT)*, 2015.
- Cited in 06_dynamics-of-head-importance.md as the source of the IWSLT 2014 dataset used for training dynamics experiments; in 10_appendix-b.md as the dataset source for the IWSLT additional pruning experiment.

**Cheng et al., 2016**
Jianpeng Cheng, Li Dong, and Mirella Lapata. Long short-term memory-networks for machine reading. In *Proceedings of the 2016 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, pages 551-561, 2016.
- Cited in 07_related-work.md for achieving state-of-the-art in reading comprehension with attention.

**Dai et al., 2019**
Zihang Dai, Zhilin Yang, Yiming Yang, William W Cohen, Jaime Carbonell, Quoc V Le, and Ruslan Salakhutdinov. Transformer-xl: Attentive language models beyond a fixed-length context. *arXiv preprint arXiv:1901.02860*, 2019.
- Cited in 07_related-work.md as an adopter of MHA for language modeling.

**Han et al., 2015**
Song Han, Jeff Pool, John Tran, and William Dally. Learning both weights and connections for efficient neural network. In *Proceedings of the 29th Annual Conference on Neural Information Processing Systems (NIPS)*, pages 1135-1143, 2015.
- Cited in 07_related-work.md as a fine-grained "weight-by-weight" pruning approach.

**Kim and Rush, 2016**
Yoon Kim and Alexander M. Rush. Sequence-level knowledge distillation. In *Proceedings of the 2016 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, pages 1317-1327, 2016.
- Cited in 07_related-work.md for popularizing fine-grained pruning approaches (mostly on NMT).

**Li et al., 2016**
Hao Li, Asim Kadav, Igor Durdanovic, Hanan Samet, and Hans Peter Graf. Pruning filters for efficient convnets. *arXiv preprint arXiv:1608.08710*, 2016.
- Cited in 07_related-work.md as a structured pruning approach.

**Murray and Chiang, 2015**
Kenton Murray and David Chiang. Auto-sizing neural networks: With applications to n-gram language models. In *Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, pages 908-916, 2015.
- Cited in 07_related-work.md as the first to investigate structured pruning for auto-sizing feed-forward language models in NLP.

**Parikh et al., 2016**
Ankur Parikh, Oscar Tackstrom, Dipanjan Das, and Jakob Uszkoreit. A decomposable attention model for natural language inference. In *Proceedings of the 2016 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, pages 2249-2255, 2016.
- Cited in 07_related-work.md for achieving state-of-the-art in natural language inference with attention.

**Paulus et al., 2017**
Romain Paulus, Caiming Xiong, and Richard Socher. A deep reinforced model for abstractive summarization. In *Proceedings of the International Conference on Learning Representations (ICLR)*, 2017.
- Cited in 07_related-work.md for abstractive summarization with attention.

**Radford et al., 2019**
Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, and Ilya Sutskever. Language models are unsupervised multitask learners. *OpenAI Blog*, 1:8, 2019.
- Cited in 07_related-work.md as an adopter of MHA for language modeling.

**See et al., 2016**
Abigail See, Minh-Thang Luong, and Christopher D. Manning. Compression of neural machine translation models via pruning. In *Proceedings of the Computational Natural Language Learning (CoNLL)*, pages 291-301, 2016.
- Cited in 07_related-work.md for popularizing fine-grained pruning approaches (mostly on NMT).

**Shwartz-Ziv and Tishby, 2017**
Ravid Shwartz-Ziv and Naftali Tishby. Opening the black box of deep neural networks via information. *arXiv preprint arXiv:1703.00810*, 2017.
- Cited in 06_dynamics-of-head-importance.md for the analysis of two training phases (empirical risk minimization and compression) that is reminiscent of the two regimes observed in head importance dynamics.

**Voita et al., 2019**
Elena Voita, David Talbot, Fedor Moiseev, Rico Sennrich, and Titov Ivan. Analyzing multi-head self-attention: Specialized heads do the heavy lifting, the rest can be pruned. In *Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics (ACL)*, page to appear, 2019.
- Cited in 07_related-work.md as concurrent work making a similar observation on multi-head attention, using LRP and gradient descent on mask variables for pruning.

**Dolan and Brockett, 2005**
William B. Dolan and Chris Brockett. Automatically constructing a corpus of sentential paraphrases. In *Proceedings of the Third International Workshop on Paraphrasing (IWP2005)*, 2005.
- Cited in 10_appendix-b.md as the source of the MRPC dataset used in additional pruning experiments.

**Socher et al., 2013**
Richard Socher, Alex Perelygin, Jean Wu, Jason Chuang, Christopher D. Manning, Andrew Ng, and Christopher Potts. Recursive deep models for semantic compositionality over a sentiment treebank. In *Proceedings of the 2013 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, pages 1631-1642, 2013.
- Cited in 10_appendix-b.md as the source of the SST-2 dataset used in additional pruning experiments.

**Warstadt et al., 2018**
Alex Warstadt, Amanpreet Singh, and Samuel R. Bowman. Neural network acceptability judgments. *arXiv preprint arXiv:1805.12471*, 2018.
- Cited in 10_appendix-b.md as the source of the CoLA dataset used in additional pruning experiments.
