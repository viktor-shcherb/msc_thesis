# References

This file contains only the bibliography entries that are cited in the section notes.

---

**[1]** Joshua Ainslie, James Lee-Thorp, Michiel de Jong, Yury Zemlyanskiy, Federico Lebron, and Sumit Sanghai. "GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints". In: *arXiv preprint arXiv:2305.13245* (2023).
- Cited in 07_mamba-2-architecture.md as grouped-query attention (GQA), motivating grouped-input SSM head patterns.

**[2]** Yaroslav Aksenov, Nikita Balagansky, Sofia Maria Lo Cicero Vaina, Boris Shaposhnikov, Alexey Gorbatovski, and Daniil Gavrilov. "Linear Transformers with Learnable Kernel Functions are Better In-Context Models". In: *arXiv preprint arXiv:2402.10644* (2024).
- Cited in 09b_architecture-ablations.md as ReBased method for linear attention approximations (Table 7); cited in 16_appendix-d-experimental-details.md (D.4) as ReBased ablation baseline.

**[3]** Ekin Akyurek, Bailin Wang, Yoon Kim, and Jacob Andreas. "In-Context Language Learning: Architectures and Algorithms". In: *The International Conference on Machine Learning (ICML)*. 2024.
- Cited in 10_related-work-discussion.md as concurrent work studying tradeoffs of SSM vs. attention representations on in-context learning tasks.

**[4]** Ameen Ali, Itamar Zimerman, and Lior Wolf. *The Hidden Attention of Mamba Models*. 2024. arXiv: 2403.01590.
- Cited in 10_related-work-discussion.md regarding whether interpretability techniques can be transferred to SSMs.

**[5]** Simran Arora, Sabri Eyuboglu, Aman Timalsina, Isys Johnson, Michael Poli, James Zou, Atri Rudra, and Christopher Re. "Zoology: Measuring and Improving Recall in Efficient Language Models". In: *The International Conference on Learning Representations (ICLR)*. 2024.
- Cited in 09_empirical-validation.md as the source of the MQAR task formulation; cited in 10_related-work-discussion.md as variant of linear attention.

**[6]** Simran Arora, Sabri Eyuboglu, Michael Zhang, Aman Timalsina, Silas Alberti, Dylan Zinsley, James Zou, Atri Rudra, and Christopher Re. "Simple Linear Attention Language Models Balance the Recall-Throughput Tradeoff". In: *The International Conference on Machine Learning (ICML)*. 2024.
- Cited in 01_introduction.md as MQAR task; cited in 09_empirical-validation.md as the Based architecture baseline for MQAR; cited in 09b_architecture-ablations.md (Table 7); cited in 10_related-work-discussion.md; cited in 16_appendix-d-experimental-details.md (D.1, D.4) as Based MQAR task source and ablation baseline.

**[7]** Dzmitry Bahdanau, Kyunghyun Cho, and Yoshua Bengio. "Neural Machine Translation by Jointly Learning to Align and Translate". In: *The International Conference on Learning Representations (ICLR)*. 2015.
- Cited in 10_related-work-discussion.md as standard attention reference.

**[9]** Maximilian Beck, Korbinian Poppel, Markus Spanring, Andreas Auer, Oleksandra Prudnikova, Michael Kopp, Gunter Klambauer, Johannes Brandstetter, and Sepp Hochreiter. "xLSTM: Extended Long Short-Term Memory". In: *arXiv preprint arXiv:2405.04517* (2024).
- Cited in 10_related-work-discussion.md as xLSTM, adopting state expansion and other gating techniques.

**[10]** Stella Biderman, Hailey Schoelkopf, Quentin Gregory Anthony, Herbie Bradley, Kyle O'Brien, et al. "Pythia: A Suite for Analyzing Large Language Models across Training and Scaling". In: *The International Conference on Machine Learning (ICML)*. PMLR. 2023, pp. 2397-2430.
- Cited in 09_empirical-validation.md as Pythia baseline for downstream evaluations (Table 1).

**[14]** Aleksandar Botev, Soham De, Samuel L Smith, Anushan Fernando, George-Cristian Muraru, Ruba Haroun, Leonard Berrada, et al. "RecurrentGemma: Moving Past Transformers for Efficient Open Language Models". In: *arXiv preprint arXiv:2404.07839* (2024).
- Cited in 10_related-work-discussion.md as RecurrentGemma, showing RNN with input-dependent gating competitive with Transformers.

**[16]** James Bradbury, Stephen Merity, Caiming Xiong, and Richard Socher. "Quasi-recurrent Neural Networks". In: *arXiv preprint arXiv:1611.01576* (2016).
- Cited in 10_related-work-discussion.md as QRNN, a modern RNN variant related to selective SSMs.

**[17]** William Brandon, Aniruddha Nrusimha, Kevin Qian, Zachary Ankner, Tian Jin, Zhiye Song, and Jonathan Ragan-Kelley. "Striped attention: Faster ring attention for causal transformers". In: *arXiv preprint arXiv:2311.09431* (2023).
- Cited in 08_systems-optimization.md regarding load-balancing for sequence parallelism in attention.

**[18]** Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, et al. "Language Models are Few-shot Learners". In: *Advances in Neural Information Processing Systems (NeurIPS)* 33 (2020), pp. 1877-1901.
- Cited in 01_introduction.md as GPT; cited in 09_empirical-validation.md as training recipe reference; cited in 08_systems-optimization.md for tensor parallelism context; cited in 16_appendix-d-experimental-details.md (D.2) as GPT3 model sizes and training recipe baseline.

**[19]** Krzysztof Choromanski, Valerii Likhosherstov, David Dohan, Xingyou Song, Andreea Gane, Tamas Sarlos, Peter Hawkins, Jared Davis, Afroz Mohiuddin, Lukasz Kaiser, et al. "Rethinking Attention with Performers". In: *The International Conference on Learning Representations (ICLR)*. 2021.
- Cited in 04_structured-masked-attention.md as Performer (Positive Random Features / FAVOR+); cited in 09b_architecture-ablations.md (Table 6); cited in 10_related-work-discussion.md.

**[20]** Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, et al. "PaLM: Scaling Language Modeling with Pathways". In: *Journal of Machine Learning Research* 24.240 (2023), pp. 1-113.
- Cited in 07_mamba-2-architecture.md for head dimension conventions; cited in 08_systems-optimization.md for TP context; cited in 16_appendix-d-experimental-details.md (D.2) as inspiration for "improved recipe" training changes.

**[21]** Junyoung Chung, Caglar Gulcehre, KyungHyun Cho, and Yoshua Bengio. "Empirical Evaluation of Gated Recurrent Neural Networks on Sequence Modeling". In: *arXiv preprint arXiv:1412.3555* (2014).
- Cited in 10_related-work-discussion.md as GRU, a classical RNN related to gating in selective SSMs.

**[23]** Tri Dao. "FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning". In: *The International Conference on Learning Representations (ICLR)*. 2024.
- Cited in 01_introduction.md as FlashAttention-2; cited in 09_empirical-validation.md as speed benchmark baseline (Figure 10).

**[24]** Tri Dao, Beidi Chen, Nimit S Sohoni, Arjun Desai, Michael Poli, Jessica Grogan, Alexander Liu, Aniruddh Rao, Atri Rudra, and Christopher Re. "Monarch: Expressive structured matrices for efficient and accurate training". In: *International Conference on Machine Learning*. PMLR. 2022, pp. 4690-4721.
- Cited in 10_related-work-discussion.md as M2 (monarch matrix) structured matrix mixer.

**[25]** Tri Dao, Daniel Y Fu, Khaled K Saab, Armin W Thomas, Atri Rudra, and Christopher Re. "Hungry Hungry Hippos: Towards Language Modeling with State Space Models". In: *The International Conference on Learning Representations (ICLR)*. 2023.
- Cited in 09_empirical-validation.md as H3 baseline; cited in 10_related-work-discussion.md as a variant of structured SSM.

**[26]** Tri Dao, Albert Gu, Matthew Eichhorn, Atri Rudra, and Christopher Re. "Learning Fast Algorithms for Linear Transforms Using Butterfly Factorizations". In: *The International Conference on Machine Learning (ICML)*. 2019.
- Cited in 02c_structured-matrices.md, 10_related-work-discussion.md as butterfly matrix examples; cited in 14_appendix-b-efficient-algorithms-scalar-ssm-scan.md as 1-SS matrices being a special case of butterfly matrices.

**[27]** Tri Dao, Nimit Sohoni, Albert Gu, Matthew Eichhorn, Amit Blonder, Megan Leszczynski, Atri Rudra, and Christopher Re. "Kaleidoscope: An Efficient, Learnable Representation for All Structured Linear Maps". In: *The International Conference on Learning Representations (ICLR)*. 2020.
- Cited in 10_related-work-discussion.md as part of the M2 / monarch matrix line of work; cited in 14_appendix-b-efficient-algorithms-scalar-ssm-scan.md as 1-SS matrices being a special case of butterfly matrices.

**[28]** Timothee Darcet, Maxime Oquab, Julien Mairal, and Piotr Bojanowski. "Vision Transformers Need Registers". In: *The International Conference on Learning Representations (ICLR)*. 2024.
- Cited in 02d_overview-ssd.md and 10_related-work-discussion.md regarding "attention sink" phenomenon.

**[29]** Soham De, Samuel L Smith, Anushan Fernando, Aleksandar Botev, George Cristian-Muraru, et al. "Griffin: Mixing Gated Linear Recurrences with Local Attention for Efficient Language Models". In: *arXiv preprint arXiv:2402.19427* (2024).
- Cited in 09_empirical-validation.md as concurrent hybrid work; cited in 10_related-work-discussion.md as Griffin.

**[30]** Christopher De Sa, Albert Gu, Rohan Puttagunta, Christopher Re, and Atri Rudra. "A Two-Pronged Progress in Structured Dense Matrix Vector Multiplication". In: *Proceedings of the Twenty-Ninth Annual ACM-SIAM Symposium on Discrete Algorithms*. SIAM. 2018, pp. 1060-1079.
- Cited in 10_related-work-discussion.md as exotic structured matrix example.

**[31]** Hantian Ding, Zijian Wang, Giovanni Paolini, et al. "Fewer truncations improve language modeling". In: *arXiv preprint arXiv:2404.10830* (2024).
- Cited in 08_systems-optimization.md regarding variable-length sequence packing.

**[33]** Dan Fu, Simran Arora, Jessica Grogan, Isys Johnson, Evan Sabri Eyuboglu, Armin Thomas, Benjamin Spector, Michael Poli, Atri Rudra, and Christopher Re. "Monarch mixer: A simple sub-quadratic gemm-based architecture". In: *Advances in Neural Information Processing Systems* 36 (2024).
- Cited in 02c_structured-matrices.md and 10_related-work-discussion.md as butterfly/monarch matrix mixer.

**[34]** Daniel Y Fu, Elliot L Epstein, Eric Nguyen, Armin W Thomas, Michael Zhang, Tri Dao, Atri Rudra, and Christopher Re. "Simple Hardware-efficient Long Convolutions for Sequence Modeling". In: *The International Conference on Machine Learning (ICML)* (2023).
- Cited in 10_related-work-discussion.md as a variant dropping the recurrence in favor of convolutional representation.

**[35]** Leo Gao, Stella Biderman, Sid Black, Laurence Golding, Travis Hoppe, et al. "The Pile: An 800GB Dataset of Diverse Text for Language Modeling". In: *arXiv preprint arXiv:2101.00027* (2020).
- Cited in 09_empirical-validation.md as the Pile dataset used for training.

**[37]** Paolo Glorioso, Quentin Anthony, Yury Tokpanov, James Whittington, Jonathan Pilault, Adam Ibrahim, and Beren Millidge. "Zamba: A Compact 7B SSM Hybrid Model". In: *arXiv preprint arXiv:2405.16712* (2024).
- Cited in 09_empirical-validation.md as concurrent hybrid architecture work.

**[38]** Riccardo Grazzi, Julien Siems, Simon Schrodi, Thomas Brox, and Frank Hutter. "Is Mamba Capable of In-Context Learning?" In: *arXiv preprint arXiv:2402.03170* (2024).
- Cited in 10_related-work-discussion.md as concurrent work on SSM in-context learning.

**[39]** Albert Gu. "Modeling Sequences with Structured State Spaces". PhD thesis. Stanford University, 2023.
- Cited in 02a_structured-state-space-models.md as general reference for SSMs; cited in 10_related-work-discussion.md as S4 lineage.

**[40]** Albert Gu and Tri Dao. "Mamba: Linear-Time Sequence Modeling with Selective State Spaces". In: *arXiv preprint arXiv:2312.00752* (2023).
- Cited extensively: 01_introduction.md, 02a_structured-state-space-models.md, 02d_overview-ssd.md, 03d_computing-ssms-structured-matrix-algorithms.md, 06_hardware-efficient-algorithm.md, 07_mamba-2-architecture.md, 09_empirical-validation.md, 10_related-work-discussion.md, 14_appendix-b-efficient-algorithms-scalar-ssm-scan.md, 16_appendix-d-experimental-details.md (D.3) as the original Mamba paper (S6 model).

**[41]** Albert Gu, Tri Dao, Stefano Ermon, Atri Rudra, and Christopher Re. "HIPPO: Recurrent Memory with Optimal Polynomial Projections". In: *Advances in Neural Information Processing Systems (NeurIPS)*. 2020.
- Cited in 10_related-work-discussion.md as early continuous-time online memorization work.

**[42]** Albert Gu, Karan Goel, and Christopher Re. "Efficiently Modeling Long Sequences with Structured State Spaces". In: *The International Conference on Learning Representations (ICLR)*. 2022.
- Cited in 01_introduction.md as S4; cited in 02a_structured-state-space-models.md as original DPLR structure; cited in 10_related-work-discussion.md; cited in 15_appendix-c-theory-details.md (C.1) as Woodbury inversion identity in SSM literature.

**[43]** Albert Gu, Ankit Gupta, Karan Goel, and Christopher Re. "On the Parameterization and Initialization of Diagonal State Space Models". In: *Advances in Neural Information Processing Systems (NeurIPS)*. 2022.
- Cited in 02a_structured-state-space-models.md as diagonal structure (S4D); cited in 03d_computing-ssms-structured-matrix-algorithms.md; cited in 10_related-work-discussion.md.

**[44]** Albert Gu, Isys Johnson, Karan Goel, Khaled Saab, Tri Dao, Atri Rudra, and Christopher Re. "Combining Recurrent, Convolutional, and Continuous-time Models with the Linear State Space Layer". In: *Advances in Neural Information Processing Systems (NeurIPS)*. 2021.
- Cited in 02a_structured-state-space-models.md and 10_related-work-discussion.md as early SSM work.

**[45]** Albert Gu, Isys Johnson, Aman Timalsina, Atri Rudra, and Christopher Re. "How to Train Your HIPPO: State Space Models with Generalized Basis Projections". In: *The International Conference on Learning Representations (ICLR)*. 2023.
- Cited in 10_related-work-discussion.md as a variant of structured SSM.

**[46]** Ankit Gupta, Albert Gu, and Jonathan Berant. "Diagonal State Spaces are as Effective as Structured State Spaces". In: *Advances in Neural Information Processing Systems* 35 (2022), pp. 22982-22994.
- Cited in 02a_structured-state-space-models.md as diagonal structure; cited in 03d_computing-ssms-structured-matrix-algorithms.md; cited in 10_related-work-discussion.md.

**[47]** Dan Hendrycks and Kevin Gimpel. "Gaussian Error Linear Units (GELUs)". In: *arXiv preprint arXiv:1606.08415* (2016).
- Cited in 07_mamba-2-architecture.md as part of SiLU/Swish activation history.

**[49]** Sepp Hochreiter and Jurgen Schmidhuber. "Long Short-Term Memory". In: *Neural Computation* 9.8 (1997), pp. 1735-1780.
- Cited in 10_related-work-discussion.md as LSTM, a classical RNN related to selective SSMs.

**[50]** Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, et al. "An Empirical Analysis of Compute-Optimal Large Language Model Training". In: *Advances in Neural Information Processing Systems (NeurIPS)* 35 (2022), pp. 30016-30030.
- Cited in 09_empirical-validation.md as Chinchilla scaling protocol; cited in 16_appendix-d-experimental-details.md (D.2) as Chinchilla scaling laws for token-to-model-size ratio.

**[51]** Samy Jelassi, David Brandfonbrener, Sham M Kakade, and Eran Malach. "Repeat After Me: Transformers Are Better Than State Space Models at Copying". In: *The International Conference on Machine Learning (ICML)*. 2024.
- Cited in 09_empirical-validation.md and 10_related-work-discussion.md regarding phonebook look-up tasks challenging for recurrent models.

**[52]** Angelos Katharopoulos, Apoorv Vyas, Nikolaos Pappas, and Francois Fleuret. "Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention". In: *International Conference on Machine Learning*. PMLR. 2020, pp. 5156-5165.
- Cited in 01_introduction.md as the Linear Attention framework; cited in 02b_attention.md; cited in 04_structured-masked-attention.md; cited in 10_related-work-discussion.md; cited in 15_appendix-c-theory-details.md (C.2) as standard linear attention with causal and autoregressive properties.

**[53]** Tobias Katsch. "GateLoop: Fully Data-Controlled Linear Recurrence for Sequence Modeling". In: *arXiv preprint arXiv:2311.01927* (2023).
- Cited in 02b_attention.md; cited in 04_structured-masked-attention.md; cited in 10_related-work-discussion.md as GateLoop, concurrently proposing input-dependent decay factors.

**[54]** Shiva Kaul. "Linear Dynamical Systems as a Core Computational Primitive". In: *Advances in Neural Information Processing Systems* 33 (2020), pp. 16808-16820.
- Cited in 02a_structured-state-space-models.md regarding universal approximation of SSMs.

**[55]** Vijay Anand Korthikanti, Jared Casper, Sangkug Lym, Lawrence McAfee, Michael Andersch, Mohammad Shoeybi, and Bryan Catanzaro. "Reducing activation recomputation in large transformer models". In: *Proceedings of Machine Learning and Systems* 5 (2023).
- Cited in 08_systems-optimization.md as the original sequence parallelism technique for residual/normalization.

**[56]** James Lee-Thorp, Joshua Ainslie, Ilya Eckstein, and Santiago Ontanon. "FNet: Mixing tokens with fourier transforms". In: *arXiv preprint arXiv:2105.03824* (2021).
- Cited in 10_related-work-discussion.md as FNet (Fourier Transform matrix mixer).

**[57]** Tao Lei. "When Attention Meets Fast Recurrence: Training Language Models with Reduced Compute". In: *Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing*. 2021, pp. 7633-7648.
- Cited in 10_related-work-discussion.md as SRU.

**[58]** Tao Lei, Yu Zhang, Sida I Wang, Hui Dai, and Yoav Artzi. "Simple Recurrent Units for Highly Parallelizable Recurrence". In: *arXiv preprint arXiv:1709.02755* (2017).
- Cited in 10_related-work-discussion.md as SRU.

**[59]** Yuhong Li, Tianle Cai, Yi Zhang, Deming Chen, and Debadeepta Dey. "What Makes Convolutional Models Great on Long Sequence Modeling?" In: *The International Conference on Learning Representations (ICLR)*. 2023.
- Cited in 10_related-work-discussion.md as work dropping recurrence in favor of convolutional representation.

**[60]** Opher Lieber, Barak Lenz, Hofit Bata, Gal Cohen, Jhonatan Osin, et al. "Jamba: A Hybrid Transformer-Mamba Language Model". In: *arXiv preprint arXiv:2403.19887* (2024).
- Cited in 09_empirical-validation.md and 09b_architecture-ablations.md as Jamba hybrid work; cited in 10_related-work-discussion.md.

**[61]** Hao Liu, Wilson Yan, Matei Zaharia, and Pieter Abbeel. "World Model on Million-Length Video And Language With RingAttention". In: *arXiv preprint arXiv:2402.08268* (2024).
- Cited in 08_systems-optimization.md as Ring attention for sequence parallelism.

**[62]** Hao Liu, Matei Zaharia, and Pieter Abbeel. "Ring attention with blockwise transformers for near-infinite context". In: *arXiv preprint arXiv:2310.01889* (2023).
- Cited in 08_systems-optimization.md as Ring attention.

**[63]** Chris Lu, Yannick Schroecker, Albert Gu, Emilio Parisotto, Jakob Foerster, Satinder Singh, and Feryal Behbahani. "Structured State Space Models for In-Context Reinforcement Learning". In: *Advances in Neural Information Processing Systems (NeurIPS)*. 2023.
- Cited in 10_related-work-discussion.md as MIMO SSM in non-language domain.

**[64]** Xuezhe Ma, Chunting Zhou, Xiang Kong, Junxian He, Liangke Gui, Graham Neubig, Jonathan May, and Luke Zettlemoyer. "Mega: Moving Average Equipped Gated Attention". In: *The International Conference on Learning Representations (ICLR)*. 2023.
- Cited in 10_related-work-discussion.md as variant of structured SSM.

**[67]** Catherine Olsson, Nelson Elhage, Neel Nanda, et al. "In-context Learning and Induction Heads". In: *Transformer Circuits Thread* (2022).
- Cited in 09_empirical-validation.md as induction heads task related to associative recall.

**[68]** Antonio Orvieto, Samuel L Smith, Albert Gu, Anushan Fernando, Caglar Gulcehre, Razvan Pascanu, and Soham De. "Resurrecting Recurrent Neural Networks for Long Sequences". In: *The International Conference on Machine Learning (ICML)*. 2023.
- Cited in 02a_structured-state-space-models.md for universal approximation; cited in 10_related-work-discussion.md as MIMO SSM.

**[70]** Jongho Park, Jaeseung Park, Zheyang Xiong, Nayoung Lee, Jaewoong Cho, Samet Oymak, Kangwook Lee, and Dimitris Papailiopoulos. "Can Mamba Learn How to Learn? A Comparative Study on In-Context Learning Tasks". In: *The International Conference on Machine Learning (ICML)*. 2024.
- Cited in 10_related-work-discussion.md as concurrent work on SSM in-context learning.

**[71]** Bo Peng, Eric Alcaide, Quentin Anthony, Alon Albalak, et al. "RWKV: Reinventing RNNs for the Transformer Era". In: *arXiv preprint arXiv:2305.13048* (2023).
- Cited in 09_empirical-validation.md as RWKV-4 baseline; cited in 10_related-work-discussion.md as RWKV(-4).

**[72]** Bo Peng, Daniel Goldstein, Quentin Anthony, Alon Albalak, Eric Alcaide, Stella Biderman, et al. "Eagle and Finch: RWKV with matrix-valued states and dynamic recurrence". In: *arXiv preprint arXiv:2404.05892* (2024).
- Cited in 10_related-work-discussion.md as RWKV-5/6 (Eagle and Finch) adopting selectivity and state expansion.

**[73]** Hao Peng, Nikolaos Pappas, Dani Yogatama, Roy Schwartz, Noah A Smith, and Lingpeng Kong. "Random Feature Attention". In: *The International Conference on Learning Representations (ICLR)*. 2021.
- Cited in 04_structured-masked-attention.md as Random Feature Attention (RFA); cited in 09b_architecture-ablations.md (Table 6); cited in 10_related-work-discussion.md.

**[74]** Clement Pernet. "Computing with Quasiseparable Matrices". In: *Proceedings of the ACM on International Symposium on Symbolic and Algebraic Computation*. 2016, pp. 389-396.
- Cited in 03b_semiseparable-matrices.md regarding quasiseparable matrix definitions.

**[75]** Clement Pernet, Hippolyte Signargout, and Gilles Villard. "Exact computations with quasiseparable matrices". In: *arXiv preprint arXiv:2302.04515* (2023).
- Cited in 03b_semiseparable-matrices.md and 03d_computing-ssms-structured-matrix-algorithms.md regarding tight parameterization bounds.

**[76]** Clement Pernet and Arne Storjohann. "Time and space efficient generators for quasiseparable matrices". In: *Journal of Symbolic Computation* 85 (2018), pp. 224-246.
- Cited in 03b_semiseparable-matrices.md regarding SSS and other representations of semiseparable matrices.

**[77]** Michael Poli, Stefano Massaroli, Eric Nguyen, Daniel Y Fu, Tri Dao, Stephen Baccus, Yoshua Bengio, Stefano Ermon, and Christopher Re. "Hyena Hierarchy: Towards Larger Convolutional Language Models". In: *The International Conference on Machine Learning (ICML)*. 2023.
- Cited in 09_empirical-validation.md as Hyena baseline; cited in 10_related-work-discussion.md as work using Toeplitz matrices and convolutional representations.

**[78]** Hadi Pouransari, Chun-Liang Li, Jen-Hao Rick Chang, Pavan Kumar Anasosalu Vasu, Cem Koc, Vaishaal Shankar, and Oncel Tuzel. "Dataset Decomposition: Faster LLM Training with Variable Sequence Length Curriculum". In: *arXiv preprint arXiv:2405.13226* (2024).
- Cited in 08_systems-optimization.md regarding packing multiple sequences for variable-length training.

**[79]** Ofir Press, Noah Smith, and Mike Lewis. "Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation". In: *International Conference on Learning Representations*. 2022.
- Cited in 04_structured-masked-attention.md as ALiBi positional encoding; cited in 10_related-work-discussion.md.

**[80]** Zhen Qin, Xiaodong Han, Weixuan Sun, Bowen He, Dong Li, Dongxu Li, Yuchao Dai, Lingpeng Kong, and Yiran Zhong. "Toeplitz Neural Network for Sequence Modeling". In: *The International Conference on Learning Representations (ICLR)*. 2023.
- Cited in 10_related-work-discussion.md as Toeplitz matrix work and convolutional representation.

**[81]** Zhen Qin, Xiaodong Han, Weixuan Sun, Dongxu Li, Lingpeng Kong, Nick Barnes, and Yiran Zhong. "The devil in linear transformer". In: *arXiv preprint arXiv:2210.10340* (2022).
- Cited in 10_related-work-discussion.md as a variant of linear attention.

**[82]** Zhen Qin, Dong Li, Weigao Sun, Weixuan Sun, Xuyang Shen, Xiaodong Han, Yunshen Wei, et al. "TransNormerLLM: A Faster and Better Large Language Model with Improved TransNormer". In: *arXiv preprint arXiv:2307.14995* (2023).
- Cited in 07_mamba-2-architecture.md regarding extra normalization; cited in 10_related-work-discussion.md as TransNormerLLM.

**[83]** Zhen Qin, Weixuan Sun, Hui Deng, Dongxu Li, Yunshen Wei, Baohong Lv, Junjie Yan, Lingpeng Kong, and Yiran Zhong. "CosFormer: Rethinking Softmax in Attention". In: *The International Conference on Learning Representations (ICLR)*. 2022.
- Cited in 04_structured-masked-attention.md as cosFormer; cited in 09b_architecture-ablations.md (Table 6).

**[84]** Zhen Qin, Songlin Yang, Weixuan Sun, Xuyang Shen, Dong Li, Weigao Sun, and Yiran Zhong. "HGRN2: Gated Linear RNNs with State Expansion". In: *arXiv preprint arXiv:2404.07904* (2024).
- Cited in 10_related-work-discussion.md as HGRN2, incorporating state expansion.

**[85]** Zhen Qin, Songlin Yang, and Yiran Zhong. "Hierarchically Gated Recurrent Neural Network for Sequence Modeling". In: *Advances in Neural Information Processing Systems* 36 (2023).
- Cited in 10_related-work-discussion.md as HGRN.

**[86]** Ali Rahimi and Benjamin Recht. "Random Features for Large-Scale Kernel Machines". In: *Advances in Neural Information Processing Systems (NeurIPS)* 20 (2007).
- Cited in 04_structured-masked-attention.md as the random Fourier feature approximation underlying RFA.

**[87]** Prajit Ramachandran, Barret Zoph, and Quoc V Le. "Swish: A Self-gated Activation Function". In: *arXiv preprint arXiv:1710.05941* 7.1 (2017), p. 5.
- Cited in 07_mamba-2-architecture.md as part of Swish/SiLU activation history.

**[89]** Imanol Schlag, Kazuki Irie, and Jurgen Schmidhuber. "Linear Transformers are Secretly Fast Weight Programmers". In: *The International Conference on Machine Learning (ICML)*. PMLR. 2021, pp. 9355-9366.
- Cited in 10_related-work-discussion.md as a variant of linear attention.

**[90]** Noam Shazeer. "Fast Transformer Decoding: One Write-head is All You Need". In: *arXiv preprint arXiv:1911.02150* (2019).
- Cited in 07_mamba-2-architecture.md as the original multi-query attention (MQA).

**[91]** Sam Shleifer, Jason Weston, and Myle Ott. "NormFormer: Improved Transformer Pretraining with Extra Normalization". In: *arXiv preprint arXiv:2110.09456* (2021).
- Cited in 07_mamba-2-architecture.md as NormFormer, motivating the extra normalization in Mamba-2.

**[92]** Mohammad Shoeybi, Mostofa Patwary, Raul Puri, Patrick LeGresley, Jared Casper, and Bryan Catanzaro. "Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism". In: *arXiv preprint arXiv:1909.08053* (2019).
- Cited in 01_introduction.md and 07_mamba-2-architecture.md as Megatron for tensor parallelism; cited in 08_systems-optimization.md.

**[93]** Jimmy TH Smith, Andrew Warrington, and Scott W Linderman. "Simplified State Space Layers for Sequence Modeling". In: *The International Conference on Learning Representations (ICLR)*. 2023.
- Cited in 02a_structured-state-space-models.md as diagonal structure; cited in 10_related-work-discussion.md; cited in 14_appendix-b-efficient-algorithms-scalar-ssm-scan.md as S5 defining the associative scan operator for SSMs.

**[94]** Jianlin Su, Yu Lu, Shengfeng Pan, Ahmed Murtadha, Bo Wen, and Yunfeng Liu. "Roformer: Enhanced Transformer with Rotary Position Embedding". In: *arXiv preprint arXiv:2104.09864* (2021).
- Cited in 10_related-work-discussion.md as RoPE positional embedding.

**[95]** Yutao Sun, Li Dong, Shaohan Huang, Shuming Ma, Yuqing Xia, Jilong Xue, Jianyong Wang, and Furu Wei. "Retentive network: A successor to transformer for large language models". In: *arXiv preprint arXiv:2307.08621* (2023).
- Cited in 02b_attention.md; cited in 04_structured-masked-attention.md as RetNet decay mask; cited in 09_empirical-validation.md as baseline; cited in 10_related-work-discussion.md; cited in 14_appendix-b-efficient-algorithms-scalar-ssm-scan.md (Remark 9) as related "chunkwise" algorithms.

**[96]** Yi Tay, Mostafa Dehghani, Dara Bahri, and Donald Metzler. "Efficient Transformers: A Survey". In: *ACM Computing Surveys* 55.6 (2022), pp. 1-28.
- Cited in 01_introduction.md and 02b_attention.md as survey of attention approximation methods.

**[97]** Chameleon Team. "Chameleon: Mixed-Modal Early-Fusion Foundation Models". In: *arXiv preprint arXiv:2405.09818* (2024).
- Cited in 09b_architecture-ablations.md as independently proposing "QK-Norm" for softmax attention.

**[98]** Anna Thomas, Albert Gu, Tri Dao, Atri Rudra, and Christopher Re. "Learning Compressed Transforms with Low Displacement Rank". In: *Advances in Neural Information Processing Systems (NeurIPS)*. 2018, pp. 9052-9060.
- Cited in 02c_structured-matrices.md and 10_related-work-discussion.md as exotic structured matrix work.

**[99]** Ilya O Tolstikhin, Neil Houlsby, Alexander Kolesnikov, Lucas Beyer, Xiaohua Zhai, Thomas Unterthiner, Jessica Yung, et al. "MLP-Mixer: An All-MLP Architecture for Vision". In: *Advances in Neural Information Processing Systems* 34 (2021), pp. 24261-24272.
- Cited in 10_related-work-discussion.md as MLP-Mixer (unstructured matrix mixer).

**[100]** Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, et al. "Llama: Open and Efficient Foundation Language Models". In: *arXiv preprint arXiv:2302.13971* (2023).
- Cited in 01_introduction.md as Llama; cited in 07_mamba-2-architecture.md for head dimension conventions; cited in 08_systems-optimization.md for TP context; cited in 16_appendix-d-experimental-details.md (D.2) as inspiration for "improved recipe" training changes.

**[101]** Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, et al. "Llama 2: Open foundation and fine-tuned chat models". In: *arXiv preprint arXiv:2307.09288* (2023).
- Cited in 08_systems-optimization.md for TP context.

**[102]** Raf Vandebril, M Van Barel, Gene Golub, and Nicola Mastronardi. "A bibliography on semiseparable matrices". In: *Calcolo* 42 (2005), pp. 249-270.
- Cited in 03b_semiseparable-matrices.md as survey of semiseparable matrix literature; cited in 15_appendix-c-theory-details.md (C.1) as motivation for the semiseparable family via inverses of banded matrices.

**[103]** Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and Illia Polosukhin. "Attention Is All You Need". In: *Advances in Neural Information Processing Systems (NeurIPS)*. 2017.
- Cited in 10_related-work-discussion.md as standard attention reference and sinusoidal positional embeddings.

**[104]** Shida Wang and Beichen Xue. "State-space Models with Layer-wise Nonlinearity are Universal Approximators with Exponentially Decaying Memory". In: *arXiv preprint arXiv:2309.13414* (2023).
- Cited in 02a_structured-state-space-models.md regarding universal approximation of SSMs.

**[105]** Sinong Wang, Belinda Z Li, Madian Khabsa, Han Fang, and Hao Ma. "Linformer: Self-attention with Linear Complexity". In: *arXiv preprint arXiv:2006.04768* (2020).
- Cited in 04_structured-masked-attention.md as Linformer low-rank attention approximation.

**[106]** Guangxuan Xiao, Yuandong Tian, Beidi Chen, Song Han, and Mike Lewis. "Efficient Streaming Language Models with Attention Sinks". In: *The International Conference on Learning Representations (ICLR)*. 2024.
- Cited in 02d_overview-ssd.md and 10_related-work-discussion.md regarding "attention sink" phenomenon.

**[107]** Yunyang Xiong, Zhanpeng Zeng, Rudrasis Chakraborty, Mingxing Tan, Glenn Fung, Yin Li, and Vikas Singh. "Nystromformer: A Nystrom-Based Algorithm for Approximating Self-Attention". In: *Proceedings of the AAAI Conference on Artificial Intelligence*. Vol. 35. 2021.
- Cited in 04_structured-masked-attention.md as Nystromformer kernel approximation.

**[108]** Songlin Yang, Bailin Wang, Yikang Shen, Rameswar Panda, and Yoon Kim. "Gated Linear Attention Transformers with Hardware-Efficient Training". In: *The International Conference on Machine Learning (ICML)*. 2024.
- Cited in 10_related-work-discussion.md as Gated Linear Attention (GLA); cited in 14_appendix-b-efficient-algorithms-scalar-ssm-scan.md (Remark 9) as related "chunkwise" algorithms.

**[110]** Jinle Zeng, Min Li, Zhihua Wu, Jiaqi Liu, Yuang Liu, Dianhai Yu, and Yanjun Ma. "Boosting distributed training performance of the unpadded bert model". In: *arXiv preprint arXiv:2208.08124* (2022).
- Cited in 08_systems-optimization.md regarding variable-length sequence techniques.

**[111]** Shuangfei Zhai, Walter Talbott, Nitish Srivastava, Chen Huang, Hanlin Goh, Ruixiang Zhang, and Josh Susskind. "An Attention Free Transformer". In: *arXiv preprint arXiv:2105.14103* (2021).
- Cited in 10_related-work-discussion.md as the attention-free Transformer underlying RWKV.

**[112]** Yujia Zhai, Chengquan Jiang, Leyuan Wang, Xiaoying Jia, Shang Zhang, Zizhong Chen, Xin Liu, and Yibo Zhu. "Bytetransformer: A high-performance transformer boosted for variable-length inputs". In: *2023 IEEE International Parallel and Distributed Processing Symposium (IPDPS)*. IEEE. 2023, pp. 344-355.
- Cited in 08_systems-optimization.md regarding variable-length sequence techniques.

**[113]** Michael Zhang, Kush Bhatia, Hermann Kumbong, and Christopher Re. "The Hedgehog & the Porcupine: Expressive Linear Attentions with Softmax Mimicry". In: *The International Conference on Learning Representations (ICLR)*. 2024.
- Cited in 10_related-work-discussion.md as a variant of linear attention.

**[114]** Lin Zheng, Chong Wang, and Lingpeng Kong. "Linear complexity randomized self-attention mechanism". In: *International Conference on Machine Learning*. PMLR. 2022, pp. 27011-27041.
- Cited in 04_structured-masked-attention.md as Linear Randomized Attention; cited in 10_related-work-discussion.md.

**[8]** George A Baker, George A Baker Jr, Peter Graves-Morris, and Susan S Baker. *Pade Approximants: Encyclopedia of Mathematics and It's Applications, Vol. 59*. Cambridge University Press, 1996.
- Cited in 14_appendix-b-efficient-algorithms-scalar-ssm-scan.md (B.3.5) as the associative scan algorithm achieving both $O(\log T)$ depth and $O(T)$ work.

**[11]** Yonatan Bisk, Rowan Zellers, Jianfeng Gao, Yejin Choi, et al. "PIQA: Reasoning about Physical Commonsense in Natural Language". In: *Proceedings of the AAAI Conference on Artificial Intelligence*. Vol. 34. 2020.
- Cited in 16_appendix-d-experimental-details.md (D.3) as downstream evaluation benchmark.

**[12]** Sid Black, Stella Biderman, Eric Hallahan, Quentin Anthony, Leo Gao, Laurence Golding, Horace He, Connor Leahy, Kyle McDonell, Jason Phang, et al. "Gpt-NeoX-20B: An Open-source Autoregressive Language Model". In: *arXiv preprint arXiv:2204.06745* (2022).
- Cited in 16_appendix-d-experimental-details.md (D.3) as GPT-NeoX tokenizer used for downstream evaluation.

**[13]** Guy E. Blelloch. "Prefix Sums and Their Applications". In: *Synthesis of Parallel Algorithms*. Morgan Kaufmann. 1990.
- Cited in 14_appendix-b-efficient-algorithms-scalar-ssm-scan.md as the divide-and-conquer algorithm for parallelizing associative scans.

**[15]** George EP Box, Gwilym M Jenkins, Gregory C Reinsel, and Greta M Ljung. *Time Series Analysis: Forecasting and Control*. John Wiley & Sons, 2015.
- Cited in 15_appendix-c-theory-details.md (C.2) as the classical ARIMA process definition used for autoregressive transformations.

**[22]** Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar Khot, Ashish Sabharwal, Carissa Schoenick, and Oyvind Tafjord. "Think you have Solved Question Answering? Try ARC, the AI2 Reasoning Challenge". In: *arXiv preprint arXiv:1803.05457* (2018).
- Cited in 16_appendix-d-experimental-details.md (D.3) as ARC-challenge downstream evaluation benchmark.

**[32]** Yuli Eidelman and Israel Gohberg. "On a new class of structured matrices". In: *Integral Equations and Operator Theory* 34.3 (1999), pp. 293-324.
- Cited in 03b_semiseparable-matrices.md regarding quasiseparable matrix definitions.

**[36]** Leo Gao, Jonathan Tow, Stella Biderman, Sid Black, Anthony DiPofi, Charles Foster, Laurence Golding, Jeffrey Hsu, Kyle McDonell, Niklas Muennighoff, Jason Phang, Laria Reynolds, Eric Tang, Anish Thite, Ben Wang, Kevin Wang, and Andy Zou. *A Framework for Few-shot Language Model Evaluation*. Version v0.0.1. Sept. 2021. DOI: 10.5281/zenodo.5371628.
- Cited in 16_appendix-d-experimental-details.md (D.3) as the LM evaluation harness from EleutherAI.

**[48]** W. Daniel Hillis and Guy L. Steele Jr. "Data parallel algorithms". In: *Communications of the ACM* 29.12 (1986), pp. 1170-1183.
- Cited in 14_appendix-b-efficient-algorithms-scalar-ssm-scan.md (Remark 8) as the "work-inefficient but more parallelizable" prefix sum algorithm.

**[65]** Eric Martin and Chris Cundy. "Parallelizing Linear Recurrent Neural Nets Over Sequence Length". In: *The International Conference on Learning Representations (ICLR)*. 2018.
- Cited in 14_appendix-b-efficient-algorithms-scalar-ssm-scan.md regarding turning recurrences into associative scans.

**[66]** Todor Mihaylov, Peter Clark, Tushar Khot, and Ashish Sabharwal. "Can a Suit of Armor Conduct Electricity? A New Dataset for Open Book Question Answering". In: *arXiv preprint arXiv:1809.02789* (2018).
- Cited in 16_appendix-d-experimental-details.md (D.3) as OpenBookQA downstream evaluation benchmark.

**[69]** Denis Paperno, German Kruszewski, Angeliki Lazaridou, Ngoc-Quan Pham, Raffaella Bernardi, Sandro Pezzelle, Marco Baroni, Gemma Boleda, and Raquel Fernandez. "The LAMBADA Dataset: Word Prediction Requiring a Broad Discourse Context". In: *Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics*. 2016, pp. 1525-1534.
- Cited in 16_appendix-d-experimental-details.md (D.3) as LAMBADA downstream evaluation benchmark.

**[88]** Keisuke Sakaguchi, Ronan Le Bras, Chandra Bhagavatula, and Yejin Choi. "Winogrande: An Adversarial Winograd Schema Challenge at Scale". In: *Communications of the ACM* 64.9 (2021), pp. 99-106.
- Cited in 16_appendix-d-experimental-details.md (D.3) as WinoGrande downstream evaluation benchmark.

**[109]** Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali Farhadi, and Yejin Choi. "HellaSwag: Can a Machine Really Finish Your Sentence?" In: *Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics*. 2019.
- Cited in 16_appendix-d-experimental-details.md (D.3) as HellaSwag downstream evaluation benchmark.

