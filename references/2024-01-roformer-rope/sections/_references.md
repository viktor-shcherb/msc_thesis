# References

Only references cited in the section notes are included below.

## Gehring et al. [2017]
Jonas Gehring, Michael Auli, David Grangier, Denis Yarats, and Yann N Dauphin. Convolutional sequence to sequence learning. In *International Conference on Machine Learning*, pages 1243-1252. PMLR, 2017.
- Cited in 01_introduction.md as an example of CNN-based models and trainable absolute position encoding.

## Islam et al. [2020]
Md. Amirul Islam, Sen Jia, and Neil D. B. Bruce. How much position information do convolutional neural networks encode? *ArXiv*, abs/2001.08248, 2020.
- Cited in 01_introduction.md showing that padding in CNNs can implicitly learn position information.

## Vaswani et al. [2017]
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, L ukasz Kaiser, and Illia Polosukhin. Attention is all you need. In *Advances in Neural Information Processing Systems*, volume 30. Curran Associates, Inc., 2017.
- Cited throughout: 01_introduction.md, 02_background-and-related-work.md, 03_proposed-approach.md, 04_experiments.md as the original Transformer paper, baseline for machine translation, and source of sinusoidal position encoding.

## Devlin et al. [2019]
J. Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. Bert: Pre-training of deep bidirectional transformers for language understanding. In *NAACL-HLT*, 2019.
- Cited in 01_introduction.md, 02_background-and-related-work.md, 04_experiments.md as the BERT baseline model with trainable absolute position encoding.

## Radford et al. [2019]
A. Radford, Jeffrey Wu, R. Child, David Luan, Dario Amodei, and Ilya Sutskever. Language models are unsupervised multitask learners. 2019.
- Cited in 01_introduction.md and 02_background-and-related-work.md as an example of trainable absolute position encoding.

## Yun et al. [2020]
Chulhee Yun, Srinadh Bhojanapalli, Ankit Singh Rawat, Sashank Reddi, and Sanjiv Kumar. Are transformers universal approximators of sequence-to-sequence functions? In *International Conference on Learning Representations*, 2020.
- Cited in 01_introduction.md showing that self-attention architecture is position-agnostic.

## Lan et al. [2020]
Zhenzhong Lan, Mingda Chen, Sebastian Goodman, Kevin Gimpel, Piyush Sharma, and Radu Soricut. Albert: A lite bert for self-supervised learning of language representations. In *International Conference on Learning Representations*, 2020.
- Cited in 01_introduction.md and 02_background-and-related-work.md as an example of trainable absolute position encoding.

## Clark et al. [2020]
Kevin Clark, Minh-Thang Luong, Quoc V. Le, and Christopher D. Manning. ELECTRA: Pre-training text encoders as discriminators rather than generators. In *ICLR*, 2020.
- Cited in 01_introduction.md and 02_background-and-related-work.md as an example of trainable absolute position encoding.

## Radford and Narasimhan [2018]
A. Radford and Karthik Narasimhan. Improving language understanding by generative pre-training. 2018.
- Cited in 01_introduction.md, 02_background-and-related-work.md as an example of trainable absolute position encoding and as a comparison of relative position embedding variants.

## Parikh et al. [2016]
Ankur P. Parikh, Oscar Tackstrom, Dipanjan Das, and Jakob Uszkoreit. A decomposable attention model for natural language inference. In *EMNLP*, 2016.
- Cited in 01_introduction.md as an early relative position encoding approach.

## Shaw et al. [2018]
Peter Shaw, Jakob Uszkoreit, and Ashish Vaswani. Self-attention with relative position representations. In *NAACL-HLT*, 2018.
- Cited in 01_introduction.md and 02_background-and-related-work.md as the approach that introduced trainable relative position embeddings with clipped relative distance.

## Huang et al. [2018]
Cheng-Zhi Anna Huang, Ashish Vaswani, Jakob Uszkoreit, Noam Shazeer, I. Simon, C. Hawthorne, Andrew M. Dai, M. Hoffman, M. Dinculescu, and D. Eck. Music transformer. *arXiv: Learning*, 2018.
- Cited in 01_introduction.md as a relative position encoding approach.

## Dai et al. [2019]
Zihang Dai, Z. Yang, Yiming Yang, J. Carbonell, Quoc V. Le, and R. Salakhutdinov. Transformer-xl: Attentive language models beyond a fixed-length context. In *ACL*, 2019.
- Cited in 01_introduction.md and 02_background-and-related-work.md for decomposing the attention score into four terms and replacing absolute positions with relative sinusoid-encoded counterparts.

## Yang et al. [2019]
Z. Yang, Zihang Dai, Yiming Yang, J. Carbonell, R. Salakhutdinov, and Quoc V. Le. Xlnet: Generalized autoregressive pretraining for language understanding. In *NeurIPS*, 2019.
- Cited in 01_introduction.md as a relative position encoding approach.

## Raffel et al. [2020]
Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, W. Li, and Peter J. Liu. Exploring the limits of transfer learning with a unified text-to-text transformer. *J. Mach. Learn. Res.*, 21:140:1-140:67, 2020.
- Cited in 01_introduction.md and 02_background-and-related-work.md for reformulating the attention score with a trainable bias term.

## Ke et al. [2020]
Guolin Ke, Di He, and T. Liu. Rethinking positional encoding in language pre-training. *ArXiv*, abs/2006.15595, 2020.
- Cited in 01_introduction.md and 02_background-and-related-work.md for investigating correlations between absolute positions and words and proposing separate projection matrices.

## He et al. [2020]
Pengcheng He, Xiaodong Liu, Jianfeng Gao, and Weizhu Chen. Deberta: Decoding-enhanced bert with disentangled attention. *ArXiv*, abs/2006.03654, 2020.
- Cited in 01_introduction.md and 02_background-and-related-work.md for arguing that relative positions can only be fully modeled using the middle two terms and replacing absolute with relative position embeddings.

## Huang et al. [2020]
Zhiheng Huang, Davis Liang, Peng Xu, and Bing Xiang. Improve transformer models with better relative position embeddings. In *Findings of the Association for Computational Linguistics: EMNLP 2020*, pages 3327-3335, Online, November 2020. Association for Computational Linguistics.
- Cited in 01_introduction.md and 02_background-and-related-work.md as a relative position encoding approach following the settings of encoding only in attention weights.

## Liu et al. [2020]
Xuanqing Liu, Hsiang-Fu Yu, Inderjit S. Dhillon, and Cho-Jui Hsieh. Learning to encode position for transformer with continuous dynamical model. In *Proceedings of the 37th International Conference on Machine Learning, ICML 2020*, volume 119 of *Proceedings of Machine Learning Research*, pages 6327-6335. PMLR, 2020.
- Cited in 01_introduction.md for modeling position encoding dependency from the perspective of Neural ODE.

## Chen et al. [2018a]
Tian Qi Chen, Yulia Rubanova, Jesse Bettencourt, and David Duvenaud. Neural ordinary differential equations. In *Advances in Neural Information Processing Systems 31: NeurIPS 2018*, pages 6572-6583, 2018a.
- Cited in 01_introduction.md for modeling position in complex space.

## Wang et al. [2020]
Benyou Wang, Donghao Zhao, Christina Lioma, Qiuchi Li, Peng Zhang, and Jakob Grue Simonsen. Encoding word order in complex embeddings. In *International Conference on Learning Representations*, 2020.
- Cited in 01_introduction.md for modeling position in complex space.

## Katharopoulos et al. [2020]
Angelos Katharopoulos, Apoorv Vyas, Nikolaos Pappas, and Francois Fleuret. Transformers are rnns: Fast autoregressive transformers with linear attention. In *International Conference on Machine Learning*, pages 5156-5165. PMLR, 2020.
- Cited in 03_proposed-approach.md for linear attention reformulation using feature maps and the elu+1 kernel.

## Shen et al. [2021]
Zhuoran Shen, Mingyuan Zhang, Haiyu Zhao, Shuai Yi, and Hongsheng Li. Efficient attention: Attention with linear complexities. In *Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision*, pages 3531-3539, 2021.
- Cited in 03_proposed-approach.md for using softmax to normalize queries and keys separately.

## Singh et al. [2018]
Amapreet Singh, Julian Michael, Felix Hill, Omer Levy, and Samuel Bowman. Glue: A multi-task benchmark and analysis platform for natural language understanding. 04 2018.
- Cited in 04_experiments.md as the GLUE benchmark for downstream evaluation.

## Choromanski et al. [2020]
Krzysztof Choromanski, Valerii Likhosherstov, David Dohan, Xingyou Song, A. Gane, Tamas Sarlos, Peter Hawkins, J. Davis, Afroz Mohiuddin, Lukasz Kaiser, David Belanger, Lucy J. Colwell, and Adrian Weller. Rethinking attention with performers. *ArXiv*, abs/2009.14794, 2020.
- Cited in 04_experiments.md as the Performer model with linear attention used in Section 4.4 experiments.

## Bojar et al. [2014]
Ondrej Bojar, Christian Buck, Christian Federmann, Barry Haddow, Philipp Koehn, Johannes Leveling, Christof Monz, Pavel Pecina, Matt Post, Herve Saint-Amand, Radu Soricut, Lucia Specia, and Ales Tamchyna. Findings of the 2014 workshop on statistical machine translation. pages 12-58, 06 2014.
- Cited in 04_experiments.md as the WMT 2014 English-German dataset for machine translation.

## Sennrich et al. [2015]
Rico Sennrich, Barry Haddow, and Alexandra Birch. Neural machine translation of rare words with subword units. 08 2015.
- Cited in 04_experiments.md for byte pair encoding (BPE) used in the translation vocabulary.

## Ott et al. [2019]
Myle Ott, Sergey Edunov, Alexei Baevski, Angela Fan, Sam Gross, Nathan Ng, David Grangier, and Michael Auli. fairseq: A fast, extensible toolkit for sequence modeling. pages 48-53, 01 2019.
- Cited in 04_experiments.md as the fairseq toolkit used for machine translation experiments.

## Papineni et al. [2002]
Kishore Papineni, Salim Roukos, Todd Ward, and Wei Jing Zhu. Bleu: a method for automatic evaluation of machine translation. 10 2002.
- Cited in 04_experiments.md as the BLEU metric used for evaluating machine translation.

## Zhu et al. [2015]
Yukun Zhu, Ryan Kiros, Richard Zemel, Ruslan Salakhutdinov, Raquel Urtasun, Antonio Torralba, and Sanja Fidler. Aligning books and movies: Towards story-like visual explanations by watching movies and reading books. In *arXiv preprint arXiv:1506.06724*, 2015.
- Cited in 04_experiments.md as the BookCorpus used for pre-training.

## Foundation [2021]
Wikimedia Foundation. Wikimedia downloads, https://dumps.wikimedia.org. 2021.
- Cited in 04_experiments.md as the Wikipedia Corpus used for pre-training.

## Loshchilov and Hutter [2017]
Ilya Loshchilov and Frank Hutter. Decoupled Weight Decay Regularization. *arXiv e-prints*, art. arXiv:1711.05101, November 2017.
- Cited in 04_experiments.md as the AdamW optimizer used for pre-training.

## Dolan and Brockett [2005]
William B. Dolan and Chris Brockett. Automatically constructing a corpus of sentential paraphrases. In *Proceedings of the Third International Workshop on Paraphrasing (IWP2005)*, 2005.
- Cited in 04_experiments.md as the MRPC dataset from GLUE.

## Socher et al. [2013]
Richard Socher, A. Perelygin, J.Y. Wu, J. Chuang, C.D. Manning, A.Y. Ng, and C. Potts. Recursive deep models for semantic compositionality over a sentiment treebank. *EMNLP*, 1631:1631-1642, 01 2013.
- Cited in 04_experiments.md as the SST-2 dataset from GLUE.

## Rajpurkar et al. [2016]
Pranav Rajpurkar, Jian Zhang, Konstantin Lopyrev, and Percy Liang. Squad: 100,000+ questions for machine comprehension of text. pages 2383-2392, 01 2016.
- Cited in 04_experiments.md as the QNLI dataset from GLUE.

## Al-Natsheh et al. [2017]
Hussein Al-Natsheh. Udl at semeval-2017 task 1: Semantic textual similarity estimation of english sentence pairs using regression model over pairwise features. 08 2017.
- Cited in 04_experiments.md as the STS-B dataset from GLUE.

## Chen et al. [2018b]
Z. Chen, H. Zhang, L. Zhang, X.and Zhao. Quora question pairs., 2018b. https://www.kaggle.com/c/quora-question-pairs
- Cited in 04_experiments.md as the QQP dataset from GLUE.

## Williams et al. [2018]
Adina Williams, Nikita Nangia, and Samuel Bowman. A broad-coverage challenge corpus for sentence understanding through inference. pages 1112-1122, 01 2018.
- Cited in 04_experiments.md as the MNLI dataset from GLUE.

## Wolf et al. [2020]
Thomas Wolf, Lysandre Debut, Victor Sanh, Julien Chaumond, Clement Delangue, Anthony Moi, Pierric Cistac, Tim Rault, Remi Louf, Morgan Funtowicz, and Alexander M. Rush. Transformers: State-of-the-art natural language processing. In *Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing: System Demonstrations*, pages 38-45, Online, October 2020. Association for Computational Linguistics.
- Cited in 04_experiments.md as the Huggingface Transformers library used for fine-tuning.

## Mahoney [2006]
Matt Mahoney. Large text compression benchmark. http://www.mattmahoney.net/dc/text.html. 2006.
- Cited in 04_experiments.md as the Enwik8 dataset used for Performer experiments.

## Su [2020]
Jianlin Su. Wobert: Word-based chinese bert model - zhuiyiai. Technical report, 2020. https://github.com/ZhuiyiTechnology/WoBERT
- Cited in 04_experiments.md as the WoBERT model used as the base for Chinese data experiments.

## Wei et al. [2019]
Victor Junqiu Wei, Xiaozhe Ren, Xiaoguang Li, Wenyong Huang, Yi Liao, Yasheng Wang, Jiashu Lin, Xin Jiang, Xiao Chen, and Qun Liu. Nezha: Neural contextualized representation for chinese language understanding. 08 2019.
- Cited in 04_experiments.md as the NEZHA model with relative position embedding in the Chinese data comparison.

## Xiao et al. [2019]
Chaojun Xiao, Haoxi Zhong, Zhipeng Guo, Cunchao Tu, Zhiyuan Liu, Maosong Sun, Tianyang Zhang, Xianpei Han, Zhen hu, Heng Wang, and Jianfeng Xu. Cail2019-scm: A dataset of similar case matching in legal domain. 11 2019.
- Cited in 04_experiments.md as the CAIL2019-SCM dataset for Chinese long text evaluation.
