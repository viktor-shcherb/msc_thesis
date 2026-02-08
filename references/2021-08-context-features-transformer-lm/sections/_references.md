# References

Only references actually cited in the section notes are included.

---

**Barzilay and Lapata (2008)**
Regina Barzilay and Mirella Lapata. 2008. Modeling local coherence: An entity-based approach. *Computational Linguistics*, 34(1):1-34.
- Cited in 04_related-work.md as prior work on discourse representations in feature-based models whose finding that nouns carry information is consistent with this paper's results.

**Beltagy et al. (2020)**
Iz Beltagy, Matthew E. Peters, and Arman Cohan. 2020. Longformer: The long-document transformer. *arXiv:2004.05150*.
- Cited in 01_introduction.md as evidence that transformer LMs benefit from conditioning on up to a thousand previous tokens.

**Bengio et al. (2003)**
Yoshua Bengio, Rejean Ducharme, Pascal Vincent, and Christian Janvin. 2003. A neural probabilistic language model. *The Journal of Machine Learning Research*, 3:1137-1155.
- Cited in 04_related-work.md as an early feature-based model that could in principle use unlimited-length contexts.

**Brown (2011)**
Ralf D Brown. 2011. The CMU-EBMT machine translation system. *Machine Translation*, 25(2):179.
- Cited in 01_introduction.md as an example showing count-based LMs in production systems typically used 10-20 tokens of context.

**Brown et al. (1992)**
Peter F Brown, Stephen A Della Pietra, Vincent J Della Pietra, Jennifer C Lai, and Robert L Mercer. 1992. An estimate of an upper bound for the entropy of english. *Computational Linguistics*, 18(1):31-40.
- Cited in 02_approach.md and 03_experiments.md as past work on evaluating language models where evaluation bottoms out in conditional entropy.

**Caccia et al. (2020)**
Massimo Caccia, Lucas Caccia, William Fedus, Hugo Larochelle, Joelle Pineau, and Laurent Charlin. 2020. Language GANs falling short. In *International Conference on Learning Representations*.
- Cited in 03_experiments.md as work showing that diversity of outputs is important for evaluating LM quality.

**Caglayan et al. (2020)**
Ozan Caglayan, Pranava Madhyastha, and Lucia Specia. 2020. Curious case of language generation evaluation metrics: A cautionary tale. In *Proceedings of the 28th International Conference on Computational Linguistics*, pages 2322-2328.
- Cited in 03_experiments.md as work showing generation depends on choice of decoding procedure.

**Child et al. (2019)**
Rewon Child, Scott Gray, Alec Radford, and Ilya Sutskever. 2019. Generating long sequences with sparse transformers. *URL https://openai.com/blog/sparse-transformers*.
- Cited in 01_introduction.md as work on making longer contexts computationally feasible.

**Clark et al. (2019)**
Kevin Clark, Urvashi Khandelwal, Omer Levy, and Christopher D. Manning. 2019. What does BERT look at? an analysis of BERT's attention. In *Proceedings of the 2019 ACL Workshop BlackboxNLP*, pages 276-286.
- Cited in 04_related-work.md as work investigating behavior of individual transformer attention heads.

**Dai et al. (2019)**
Zihang Dai, Zhilin Yang, Yiming Yang, Jaime Carbonell, Quoc Le, and Ruslan Salakhutdinov. 2019. Transformer-XL: Attentive language models beyond a fixed-length context. In *Proceedings of the 57th Annual Meeting of the ACL*, pages 2978-2988.
- Cited in 01_introduction.md as work on making longer contexts computationally feasible.

**Elman (1990)**
Jeffrey L Elman. 1990. Finding structure in time. *Cognitive Science*, 14(2):179-211.
- Cited in 04_related-work.md as an early recurrent neural network language model.

**Goodman (2001)**
Joshua T Goodman. 2001. A bit of progress in language modeling. *Computer Speech & Language*, 15(4):403-434.
- Cited in 04_related-work.md as a subsequent model using skip-grams and caches.

**Hahn (2020)**
Michael Hahn. 2020. Theoretical limitations of self-attention in neural sequence models. *Transactions of the Association for Computational Linguistics*, 8:156-171.
- Cited in 02_approach.md as evidence of theoretical limits to transformers' ability to use long contexts.

**Hashimoto et al. (2019)**
Tatsunori Hashimoto, Hugh Zhang, and Percy Liang. 2019. Unifying human and statistical evaluation for natural language generation. In *Proceedings of the 2019 Conference of the North American Chapter of the ACL*, pages 1689-1701.
- Cited in 03_experiments.md as work showing diversity metrics are important for evaluating LM quality.

**Henaff et al. (2016)**
Mikael Henaff, Jason Weston, Arthur Szlam, Antoine Bordes, and Yann LeCun. 2016. Tracking the world state with recurrent entity networks. In *ICLR*.
- Cited in 04_related-work.md as prior work with specialized neural architectures consistent with the finding that nouns carry most usable information.

**Honnibal et al. (2020)**
Matthew Honnibal, Ines Montani, Sofie Van Landeghem, and Adriane Boyd. 2020. spaCy: Industrial-strength Natural Language Processing in Python.
- Cited in 03_experiments.md as the spaCy model used for part-of-speech tagging.

**Jain and Wallace (2019)**
Sarthak Jain and Byron C. Wallace. 2019. Attention is not explanation. In *NAACL-HLT*.
- Cited in 04_related-work.md for the claim that patterns of attention do not necessarily correlate with model predictions.

**Khandelwal et al. (2018)**
Urvashi Khandelwal, He He, Peng Qi, and Dan Jurafsky. 2018. Sharp nearby, fuzzy far away: How neural language models use context. In *Proceedings of the 56th Annual Meeting of the ACL (Volume 1: Long Papers)*, pages 284-294.
- Cited in 01_introduction.md as showing RNN LMs have effective context of 200 tokens; in 01_introduction.md and 03_experiments.md as the closely related prior study measuring context sensitivity at evaluation time; in 04_related-work.md for RNN context influence.

**Kitaev et al. (2020)**
Nikita Kitaev, Lukasz Kaiser, and Anselm Levskaya. 2020. Reformer: The efficient transformer. In *International Conference on Learning Representations*.
- Cited in 01_introduction.md as work on making longer contexts computationally feasible.

**Kneser and Ney (1995)**
Reinhard Kneser and Hermann Ney. 1995. Improved backing-off for m-gram language modeling. In *1995 International Conference on Acoustics, Speech, and Signal Processing*, volume 1, pages 181-184. IEEE.
- Cited in 01_introduction.md and 04_related-work.md as a foundational count-based language model.

**Li et al. (2016)**
Jiwei Li, Will Monroe, and Dan Jurafsky. 2016. Understanding neural networks through representation erasure. *arXiv preprint arXiv:1612.08220*.
- Cited in 04_related-work.md as describing an alternative procedure for ablating contexts.

**Merity et al. (2016)**
Stephen Merity, Caiming Xiong, James Bradbury, and Richard Socher. 2016. Pointer sentinel mixture models. *CoRR*, abs/1609.07843.
- Cited in 03_experiments.md as the source of the WikiText-103 dataset.

**Mikolov et al. (2010)**
Tomas Mikolov, Martin Karafiat, Lukas Burget, Jan Cernocky, and Sanjeev Khudanpur. 2010. Recurrent neural network based language model. In *Eleventh Annual Conference of the International Speech Communication Association*.
- Cited in 01_introduction.md and 04_related-work.md as an early recurrent neural network language model.

**Mollica et al. (2020)**
F. Mollica, Matthew Siegelman, Evgeniia Diachek, S. Piantadosi, Zachary Mineroff, Richard Futrell, Hope H. Kean, Peng Qian, and E. Fedorenko. 2020. Composition is the core driver of the language-selective network. *Neurobiology of Language*, 1:104-134.
- Cited in 03_experiments.md as prior work exploring more complex shuffling procedures in neuroscience contexts.

**Perez et al. (2021)**
Ethan Perez, Douwe Kiela, and Kyunghyun Cho. 2021. Rissanen data analysis: Examining dataset characteristics via description length. *arXiv preprint arXiv:2103.03872*.
- Cited in 04_related-work.md as work on introducing usable information for question answering and sentence understanding tasks.

**Pham et al. (2020)**
Thang M Pham, Trung Bui, Long Mai, and Anh Nguyen. 2020. Out of order: How important is the sequential order of words in a sentence in natural language understanding tasks? *arXiv preprint arXiv:2012.15180*.
- Cited in 03_experiments.md for exploring within-sentence shuffling in entailment models; in 04_related-work.md for finding that shuffling has limited effect on NLI accuracy.

**Pimentel et al. (2020)**
Tiago Pimentel, Josef Valvoda, Rowan Hall Maudslay, Ran Zmigrod, Adina Williams, and Ryan Cotterell. 2020. Information-theoretic probing for linguistic structure. In *Proceedings of the 58th Annual Meeting of the ACL*, pages 4609-4622.
- Cited in 04_related-work.md as information-theoretic work on probing that shares similar motivations.

**Radford et al. (2019)**
Alec Radford, Jeff Wu, Rewon Child, David Luan, Dario Amodei, and Ilya Sutskever. 2019. Language models are unsupervised multitask learners.
- Cited in 03_experiments.md as the source of the GPT-2 model architecture used in all experiments.

**Rae et al. (2019)**
Jack W Rae, Anna Potapenko, Siddhant M. Jayakumar, and Timothy P. Lillicrap. 2019. Compressive transformers for long-range sequence modelling.
- Cited in 01_introduction.md as work on longer contexts; in 04_related-work.md as consistent with the finding that long-range contexts can be informatively summarized in fixed-sized vectors.

**Sankar et al. (2019)**
Chinnadhurai Sankar, Sandeep Subramanian, Christopher Pal, Sarath Chandar, and Yoshua Bengio. 2019. Do neural dialog systems use the conversation history effectively? an empirical study. *arXiv preprint arXiv:1906.01603*.
- Cited in 04_related-work.md for reporting similar context-sensitivity effects in neural dialogue models.

**Shannon (1948)**
Claude E Shannon. 1948. A mathematical theory of communication. *The Bell System Technical Journal*, 27(3):379-423.
- Cited in 02_approach.md as the originator of Shannon mutual information, which V-information generalizes.

**Vaswani et al. (2017)**
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Lukasz Kaiser, and Illia Polosukhin. 2017. Attention is all you need. In *Advances in Neural Information Processing Systems 30*, pages 5998-6008.
- Cited in 01_introduction.md and 02_approach.md as the foundational transformer architecture.

**Voita and Titov (2020)**
Elena Voita and Ivan Titov. 2020. Information-theoretic probing with minimum description length. In *Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, pages 183-196.
- Cited in 04_related-work.md as information-theoretic work on probing that shares similar motivations.

**Voita et al. (2019)**
Elena Voita, David Talbot, Fedor Moiseev, Rico Sennrich, and Ivan Titov. 2019. Analyzing multi-head self-attention: Specialized heads do the heavy lifting, the rest can be pruned. In *Proceedings of the 57th Annual Meeting of the ACL*, pages 5797-5808.
- Cited in 04_related-work.md as work investigating behavior of individual transformer attention heads.

**Wang et al. (2019)**
Alex Wang, Yada Pruksachatkun, Nikita Nangia, Amanpreet Singh, Julian Michael, Felix Hill, Omer Levy, and Samuel R Bowman. 2019. SuperGLUE: A stickier benchmark for general-purpose language understanding systems. *arXiv preprint arXiv:1905.00537*.
- Cited in 02_approach.md as evidence of practical limits to transformers' ability to use long contexts.

**Wang et al. (2020)**
Sinong Wang, Belinda Li, Madian Khabsa, Han Fang, and Hao Ma. 2020. Linformer: Self-attention with linear complexity. *arXiv preprint arXiv:2006.04768*.
- Cited in 01_introduction.md as work on making longer contexts computationally feasible.

**Wolf et al. (2020)**
Thomas Wolf, Lysandre Debut, Victor Sanh, Julien Chaumond, Clement Delangue, Anthony Moi, Pierric Cistac, Tim Rault, Remi Louf, Morgan Funtowicz, Joe Davison, Sam Shleifer, Patrick von Platen, Clara Ma, Yacine Jernite, Julien Plu, Canwen Xu, Teven Le Scao, Sylvain Gugger, Mariama Drame, Quentin Lhoest, and Alexander M. Rush. 2020. Transformers: State-of-the-art natural language processing. In *Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing: System Demonstrations*, pages 38-45.
- Cited in 01_introduction.md for training infrastructure improvements; in 03_experiments.md as the implementation of GPT-2 used.

**Xu et al. (2020)**
Yilun Xu, Shengjia Zhao, Jiaming Song, Russell Stewart, and Stefano Ermon. 2020. A theory of usable information under computational constraints. In *International Conference on Learning Representations*.
- Cited in 01_introduction.md and 02_approach.md as the source of the V-information framework; in 03_experiments.md for the non-negativity property of V-information.

**Zhang et al. (2016)**
Chiyuan Zhang, Samy Bengio, Moritz Hardt, Benjamin Recht, and Oriol Vinyals. 2016. Understanding deep learning requires rethinking generalization. *arXiv preprint arXiv:1611.03530*.
- Cited in 02_approach.md for the risk of overfitting in finite-corpus LM evaluation.
