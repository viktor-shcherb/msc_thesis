# References

Only references actually cited in the section notes are included.

## [1]
Alok Aggarwal and S Vitter, Jeffrey. The input/output complexity of sorting and related problems. *Communications of the ACM*, 31(9):1116–1127, 1988.
- Cited in 01_introduction.md as the foundational IO-aware algorithms reference; in 07_appendix-a-related-work.md for IO complexity literature connection.

## [3]
Iz Beltagy, Matthew E Peters, and Arman Cohan. Longformer: The long-document transformer. *arXiv preprint arXiv:2004.05150*, 2020.
- Cited in 01_introduction.md as a combination sparse/low-rank approximation method; in 03c_block-sparse-flashattention.md for sparsity ratio $N^{-1} \log N$; in 04_experiments.md for positional embedding repetition technique (Beltagy et al. [3]); in 07_appendix-a-related-work.md as a combined sparse/low-rank approach; in 11_appendix-e-full-experimental-results.md as a baseline (Longformer) in E.6 full benchmarking.

## [4]
L Susan Blackford, Antoine Petitet, Roldan Pozo, Karin Remington, R Clint Whaley, James Demmel, Jack Dongarra, Iain Duff, Sven Hammarling, Greg Henry, et al. An updated set of basic linear algebra subprograms (blas). *ACM Transactions on Mathematical Software*, 28(2):135–151, 2002.
- Cited in 01_introduction.md as an example of IO-aware algorithms in numerical linear algebra.

## [5]
Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. Language models are few-shot learners. *Advances in neural information processing systems*, 33:1877–1901, 2020.
- Cited in 01_introduction.md noting that Transformers have grown larger.

## [6]
Ilias Chalkidis, Ion Androutsopoulos, and Nikolaos Aletras. Neural legal judgment prediction in English. In *Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics*, pages 4317–4323, Florence, Italy, 2019.
- Cited in 04_experiments.md as the ECtHR dataset source for long document classification.

## [7]
Ilias Chalkidis, Manos Fergadiotis, Dimitrios Tsarapatsanis, Nikolaos Aletras, Ion Androutsopoulos, and Prodromos Malakasiotis. Paragraph-level rationale extraction through regularization: A case study on european court of human rights cases. In *NAACL*, 2021.
- Cited in 04_experiments.md alongside [6] for the ECtHR dataset.

## [8]
Benjamin Charlier, Jean Feydy, Joan Alexis Glaunes, Francois-David Collin, and Ghislain Durif. Kernel operations on the gpu, with autodiff, without memory overflows. *Journal of Machine Learning Research*, 22(74):1-6, 2021.
- Cited in 10_appendix-d-extension-details.md as the KeOps library, a successful example of reducing memory reads/writes to speed up kernel operations.

## [9]
Beidi Chen, Tri Dao, Eric Winsor, Zhao Song, Atri Rudra, and Christopher Re. Scatterbrain: Unifying sparse and low-rank attention. In *Advances in Neural Information Processing Systems (NeurIPS)*, 2021.
- Cited in 01_introduction.md as a combination sparse/low-rank approximation method; in 07_appendix-a-related-work.md as a combined sparse/low-rank approach (Scatterbrain).

## [10]
Tianqi Chen, Bing Xu, Chiyuan Zhang, and Carlos Guestrin. Training deep nets with sublinear memory cost. *arXiv preprint arXiv:1604.06174*, 2016.
- Cited in 03a_tiling-and-recomputation.md as a form of selective gradient checkpointing.

## [11]
Rewon Child, Scott Gray, Alec Radford, and Ilya Sutskever. Generating long sequences with sparse transformers. *arXiv preprint arXiv:1904.10509*, 2019.
- Cited in 03c_block-sparse-flashattention.md for sparsity ratio $s = N^{-1/2}$; in 11_appendix-e-full-experimental-results.md as a baseline (Block-Sparse Attention from OpenAI) in E.6 full benchmarking.

## [12]
Krzysztof Marcin Choromanski, Valerii Likhosherstov, David Dohan, Xingyou Song, Andreea Gane, Tamas Sarlos, Peter Hawkins, Jared Quincy Davis, Afroz Mohiuddin, Lukasz Kaiser, et al. Rethinking attention with performers. In *ICLR*, 2020.
- Cited in 01_introduction.md as a low-rank approximation method; in 04_experiments.md as a baseline in LRA (Table 3) and Path-X/Path-256 (Table 6); in 07_appendix-a-related-work.md as a low-rank approximation (Performer).

## [13]
Xiang Dai, Ilias Chalkidis, Sune Darkner, and Desmond Elliott. Revisiting transformer-based models for long document classification. *arXiv preprint arXiv:2204.06683*, 2022.
- Cited in 01_introduction.md for 6.4 points of lift from modeling longer sequences on long-document classification; in 11_appendix-e-full-experimental-results.md for long document classification hyperparameters.

## [16]
Tri Dao, Nimit Sohoni, Albert Gu, Matthew Eichhorn, Amit Blonder, Megan Leszczynski, Atri Rudra, and Christopher Re. Kaleidoscope: An efficient, learnable representation for all structured linear maps. In *ICLR*, 2020.
- Cited in 03c_block-sparse-flashattention.md noting butterfly sparsity pattern can approximate arbitrary sparsity; in 07_appendix-a-related-work.md for butterfly matrices expressing structured matrices with optimal runtime/parameters.

## [17]
Tri Dao, Beidi Chen, Kaizhao Liang, Jiaming Yang, Zhao Song, Atri Rudra, and Christopher Re. Pixelated butterfly: Simple and efficient sparse training for neural network models. In *ICLR*, 2022.
- Cited in 03c_block-sparse-flashattention.md for the fixed butterfly sparsity pattern used in downstream experiments; also for sparsity ratio $N^{-1} \log N$; in 07_appendix-a-related-work.md for extensions of butterfly matrices to be more hardware-friendly; in 10_appendix-d-extension-details.md for sparse MLP layers.

## [19]
Giannis Daras, Nikita Kitaev, Augustus Odena, and Alexandros G Dimakis. Smyrf-efficient attention using asymmetric clustering. *Advances in Neural Information Processing Systems*, 33:6476–6489, 2020.
- Cited in 04_experiments.md as a baseline in LRA (Table 3) and Path-X/Path-256 (Table 6); in 07_appendix-a-related-work.md as a hashing-based sparse approximation (Smyrf); in 11_appendix-e-full-experimental-results.md as a baseline in E.6 full benchmarking.

## [22]
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. BERT: Pre-training of deep bidirectional transformers for language understanding. 2019.
- Cited in 04_experiments.md for the BERT-large model used in training speed experiments; in 07_appendix-a-related-work.md as a widely-used Transformer in NLP.

## [26]
Jean Feydy, Joan Glaunes, Benjamin Charlier, and Michael Bronstein. Fast geometric learning with symbolic matrices. *Advances in Neural Information Processing Systems*, 33, 2020.
- Cited in 10_appendix-d-extension-details.md as the KeOps library, a successful example of reducing memory reads/writes to speed up kernel operations.

## [27]
Jorg Flum and Martin Grohe. *Parameterized Complexity Theory*. Springer, 2006.
- Cited in 03b_io-complexity-analysis.md for parameterized complexity lower bounds as future work.

## [32]
Aaron Gokaslan, Vanya Cohen, Pavlick Ellie, and Stefanie Tellex. Openwebtext corpus, 2019.
- Cited in 04_experiments.md as the dataset for GPT-2 training experiments.

## [33]
Jim Gray, Surajit Chaudhuri, Adam Bosworth, Andrew Layman, Don Reichart, Murali Venkatrao, Frank Pellow, and Hamid Pirahesh. Data cube: A relational aggregation operator generalizing group-by, cross-tab, and sub-totals. *Data mining and knowledge discovery*, 1(1):29–53, 1997.
- Cited in 03a_tiling-and-recomputation.md as the source of the term "algebraic aggregation".

## [34]
Andreas Griewank and Andrea Walther. *Evaluating derivatives: principles and techniques of algorithmic differentiation*. SIAM, 2008.
- Cited in 03a_tiling-and-recomputation.md for selective gradient checkpointing.

## [37]
Albert Gu, Karan Goel, and Christopher Re. Efficiently modeling long sequences with structured state spaces. In *ICLR*, 2022.
- Cited in 04_experiments.md for alternative architectures that can model long context (Path-X discussion); in 07_appendix-a-related-work.md as an S4 extension using state-space models.

## [40]
John Hennessy and David Patterson. Memory hierarchy design. *Computer Architecture: A Quantitative Approach*, pages 390–525, 2003.
- Cited in 01_introduction.md as an example of IO-aware algorithms; in 07_appendix-a-related-work.md for textbook computer architecture treatments.

## [43]
Andrei Ivanov, Nikoli Dryden, Tal Ben-Nun, Shigang Li, and Torsten Hoefler. Data movement is all you need: A case study on optimizing transformers. *Proceedings of Machine Learning and Systems*, 3:711–732, 2021.
- Cited in 01_introduction.md noting most operations in Transformers are bottlenecked by memory accesses.

## [44]
Zhe Jia and Peter Van Sandt. Dissecting the Ampere GPU architecture via microbenchmarking. GPU Technology Conference, 2021.
- Cited in 02_background.md for A100 GPU SRAM bandwidth estimates.

## [45]
Zhe Jia, Marco Maggioni, Benjamin Staiger, and Daniele P Scarpazza. Dissecting the nvidia Volta GPU architecture via microbenchmarking. *arXiv preprint arXiv:1804.06826*, 2018.
- Cited in 01_introduction.md and 02_background.md for GPU HBM/SRAM specifications.

## [46]
Zhe Jia, Blake Tillman, Marco Maggioni, and Daniele Paolo Scarpazza. Dissecting the graphcore IPU architecture via microbenchmarking. *arXiv preprint arXiv:1912.03413*, 2019.
- Cited in 02_background.md noting performance on other hardware accelerators is similar.

## [47]
Alistair EW Johnson, Tom J Pollard, Lu Shen, Li-wei H Lehman, Mengling Feng, Mohammad Ghassemi, Benjamin Moody, Peter Szolovits, Leo Anthony Celi, and Roger G Mark. Mimic-iii, a freely accessible critical care database. *Scientific data*, 3(1):1–9, 2016.
- Cited in 04_experiments.md as the MIMIC-III dataset source for long document classification.

## [48]
Norman P Jouppi, Cliff Young, Nishant Patil, David Patterson, Gaurav Agrawal, Raminder Bajwa, Sarah Bates, Suresh Bhatia, Nan Boden, Al Borchers, et al. In-datacenter performance analysis of a tensor processing unit. In *ISCA*, pages 1–12, 2017.
- Cited in 02_background.md noting performance on other hardware accelerators is similar.

## [50]
Angelos Katharopoulos, Apoorv Vyas, Nikolaos Pappas, and Francois Fleuret. Transformers are RNNs: Fast autoregressive transformers with linear attention. In *ICML*, pages 5156–5165. PMLR, 2020.
- Cited in 01_introduction.md as a low-rank approximation method; in 04_experiments.md as a baseline in LRA (Table 3) and Path-X/Path-256 (Table 6); in 07_appendix-a-related-work.md as a linear attention approach.

## [51]
Nikita Kitaev, Lukasz Kaiser, and Anselm Levskaya. Reformer: The efficient transformer. In *ICML*, 2020.
- Cited in 01_introduction.md as a sparse-approximation method; in 03a_tiling-and-recomputation.md for softmax decomposition with scaling; in 04_experiments.md as a baseline in LRA (Table 3) and Path-X/Path-256 (Table 6); in 07_appendix-a-related-work.md as a hashing-based sparse approximation; in 08_appendix-b-algorithm-details.md for showing attention does not need quadratic extra memory; in 11_appendix-e-full-experimental-results.md as a baseline in E.6 full benchmarking.

## [53]
Mingzhen Li, Yi Liu, Xiaoyan Liu, Qingxiao Sun, Xin You, Hailong Yang, Zhongzhi Luan, Lin Gan, Guangwen Yang, and Depei Qian. The deep learning compiler: A comprehensive survey. *IEEE Transactions on Parallel and Distributed Systems*, 32(3):708–727, 2020.
- Cited in 02_background.md for automatic fusion of elementwise operations by compilers.

## [56]
Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke Zettlemoyer, and Veselin Stoyanov. Roberta: A robustly optimized bert pretraining approach. *arXiv preprint arXiv:1907.11692*, 2019.
- Cited in 04_experiments.md as the pretrained RoBERTa model used for long document classification.

## [58]
Peter Mattson, Christine Cheng, Gregory Diamos, Cody Coleman, Paulius Micikevicius, David Patterson, Hanlin Tang, Gu-Yeon Wei, Peter Bailis, Victor Bittorf, et al. Mlperf training benchmark. *Proceedings of Machine Learning and Systems*, 2:336–349, 2020.
- Cited in 01_introduction.md and 04_experiments.md as the MLPerf 1.1 training speed record baseline for BERT; in 11_appendix-e-full-experimental-results.md noting Apex FMHA used in MLPerf submissions.

## [60]
Maxim Milakov and Natalia Gimelshein. Online normalizer calculation for softmax. *arXiv preprint arXiv:1805.02867*, 2018.
- Cited in 03a_tiling-and-recomputation.md for softmax decomposition with scaling; in 08_appendix-b-algorithm-details.md for the softmax normalization constant technique.

## [61]
NVIDIA. Nvidia Tesla V100 GPU architecture, 2017.
- Cited in 01_introduction.md and 02_background.md noting compute has outpaced memory speed.

## [62]
NVIDIA. Nvidia A100 tensor core GPU architecture, 2020.
- Cited in 01_introduction.md and 02_background.md noting compute has outpaced memory speed.

## [63]
NVIDIA. Nvidia H100 tensor core GPU architecture, 2022.
- Cited in 01_introduction.md and 02_background.md noting compute has outpaced memory speed.

## [65]
Adam Paszke, Sam Gross, Francisco Massa, Adam Lerer, James Bradbury, Gregory Chanan, Trevor Killeen, Zeming Lin, Natalia Gimelshein, Luca Antiga, et al. Pytorch: An imperative style, high-performance deep learning library. *Advances in neural information processing systems*, 32, 2019.
- Cited in 02_background.md for automatic fusion of elementwise operations by compilers.

## [66]
Markus N Rabe and Charles Staats. Self-attention does not need $O(n^2)$ memory. *arXiv preprint arXiv:2112.05682*, 2021.
- Cited in 03a_tiling-and-recomputation.md for softmax decomposition and gradient checkpointing to reduce memory; in 08_appendix-b-algorithm-details.md for showing attention does not need quadratic extra memory, for backward pass gradient checkpointing suggestion, and for detailed comparison in B.5 (three major differences: memory footprint vs. memory accesses, block summarization approach, backward pass computation).

## [67]
Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, Ilya Sutskever, et al. Language models are unsupervised multitask learners. *OpenAI blog*, 1(8):9, 2019.
- Cited in 01_introduction.md for GPT-2 speedup; in 04_experiments.md for GPT-2 training experiments; in 11_appendix-e-full-experimental-results.md for GPT-2 implementation details.

## [70]
Jonathan Ragan-Kelley, Connelly Barnes, Andrew Adams, Sylvain Paris, Fredo Durand, and Saman Amarasinghe. Halide: a language and compiler for optimizing parallelism, locality, and recomputation in image processing pipelines. *Acm Sigplan Notices*, 48(6):519–530, 2013.
- Cited in 01_introduction.md as an example of IO-aware algorithms in image processing; in 05_limitations-and-future-directions.md as inspiration for a high-level language compiling to IO-aware CUDA.

## [71]
Raghu Ramakrishnan, Johannes Gehrke, and Johannes Gehrke. *Database management systems*, volume 3. McGraw-Hill New York, 2003.
- Cited in 01_introduction.md as an example of IO-aware algorithms in database joins.

## [72]
Benjamin Recht and Christopher Re. Parallel stochastic gradient algorithms for large-scale matrix completion. *Mathematical Programming Computation*, 5(2):201–226, 2013.
- Cited in 05_limitations-and-future-directions.md for parallelizable attention across multiple GPUs.

## [74]
Aurko Roy, Mohammad Saffar, Ashish Vaswani, and David Grangier. Efficient content-based sparse attention with routing transformers. *Transactions of the Association for Computational Linguistics*, 9:53–68, 2021.
- Cited in 01_introduction.md as a sparse-approximation method.

## [75]
Amit Sabne. XLA: Compiling machine learning for peak performance. 2020.
- Cited in 02_background.md for automatic fusion of elementwise operations by compilers.

## [77]
Mohammad Shoeybi, Mostofa Patwary, Raul Puri, Patrick LeGresley, Jared Casper, and Bryan Catanzaro. Megatron-LM: Training multi-billion parameter language models using model parallelism. *arXiv preprint arXiv:1909.08053*, 2019.
- Cited in 01_introduction.md, 02_background.md, and 04_experiments.md as the Megatron-LM baseline for GPT-2 training and for fusing masking with softmax; in 10_appendix-d-extension-details.md for multi-GPU attention splitting.

## [80]
Yi Tay, Mostafa Dehghani, Samira Abnar, Yikang Shen, Dara Bahri, Philip Pham, Jinfeng Rao, Liu Yang, Sebastian Ruder, and Donald Metzler. Long range arena: A benchmark for efficient transformers. In *ICLR*, 2020.
- Cited in 01_introduction.md for difficulty of longer context; in 04_experiments.md as the LRA benchmark source, as a baseline (Local Attention), and for Path-X prior work; in 11_appendix-e-full-experimental-results.md for LRA hyperparameters and Path-X/Path-256 fine-tuning procedure.

## [82]
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Lukasz Kaiser, and Illia Polosukhin. Attention is all you need. *Advances in neural information processing systems*, 30, 2017.
- Cited in 01_introduction.md as the original Transformer architecture.

## [83]
Hongyu Wang, Shuming Ma, Li Dong, Shaohan Huang, Dongdong Zhang, and Furu Wei. Deepnet: Scaling transformers to 1,000 layers. *arXiv preprint arXiv:2203.00555*, 2022.
- Cited in 01_introduction.md noting Transformers have grown deeper.

## [84]
Sinong Wang, Belinda Z Li, Madian Khabsa, Han Fang, and Hao Ma. Linformer: Self-attention with linear complexity. *arXiv preprint arXiv:2006.04768*, 2020.
- Cited in 01_introduction.md as a low-rank approximation method; in 04_experiments.md as a baseline in LRA (Table 3) and Path-X/Path-256 (Table 6); in 11_appendix-e-full-experimental-results.md as a baseline in E.6 full benchmarking.

## [85]
Samuel Williams, Andrew Waterman, and David Patterson. Roofline: an insightful visual performance model for multicore architectures. *Communications of the ACM*, 52(4):65–76, 2009.
- Cited in 01_introduction.md as an example of IO-aware algorithms; in 02_background.md for the concept of arithmetic intensity; in 07_appendix-a-related-work.md for the Roofline model of arithmetic intensity.

## [87]
Thomas Wolf, Lysandre Debut, Victor Sanh, Julien Chaumond, Clement Delangue, Anthony Moi, Pierric Cistac, Tim Rault, Remi Louf, Morgan Funtowicz, Joe Davison, Sam Shleifer, Patrick von Platen, Clara Ma, Yacine Jernite, Julien Plu, Canwen Xu, Teven Le Scao, Sylvain Gugger, Mariama Drame, Quentin Lhoest, and Alexander M. Rush. Transformers: State-of-the-art natural language processing. In *Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing: System Demonstrations*, pages 38–45, 2020.
- Cited in 01_introduction.md and 04_experiments.md as the HuggingFace baseline for GPT-2 training.

## [88]
David P Woodruff. Optimal space lower bounds for all frequency moments. In *SODA*, volume 4, pages 167–175. Citeseer, 2004.
- Cited in 03b_io-complexity-analysis.md for streaming algorithms lower bound technique.

## [90]
Yunyang Xiong, Zhanpeng Zeng, Rudrasis Chakraborty, Mingxing Tan, Glenn Fung, Yin Li, and Vikas Singh. Nystromformer: A nystom-based algorithm for approximating self-attention. In *AAAI Conference on Artificial Intelligence*, volume 35, page 14138, 2021.
- Cited in 04_experiments.md for the LRA experimental setting and tuning procedure sensitivity; in 11_appendix-e-full-experimental-results.md for LRA hyperparameter reproduction source.

## [92]
Manzil Zaheer, Guru Guruganesh, Kumar Avinava Dubey, Joshua Ainslie, Chris Alberti, Santiago Ontanon, Philip Pham, Anirudh Ravula, Qifan Wang, Li Yang, et al. Big bird: Transformers for longer sequences. *Advances in Neural Information Processing Systems*, 33, 2020.
- Cited in 01_introduction.md as a combination sparse/low-rank approximation method; in 03c_block-sparse-flashattention.md for sparsity ratio $N^{-1} \log N$; in 07_appendix-a-related-work.md as a combined sparse/low-rank approach (BigBird); in 11_appendix-e-full-experimental-results.md as a baseline (BigBird Attention) in E.6 full benchmarking.

## [2]
Irwan Bello. LambdaNetworks: Modeling long-range interactions without attention. *arXiv preprint arXiv:2102.08602*, 2021.
- Cited in 07_appendix-a-related-work.md as an attempt at replacing attention in image classification and language modeling.

## [14]
Zihang Dai, Zhilin Yang, Yiming Yang, Jaime G Carbonell, Quoc Le, and Ruslan Salakhutdinov. Transformer-XL: Attentive language models beyond a fixed-length context. In *Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics*, pages 2978–2988, 2019.
- Cited in 07_appendix-a-related-work.md for attending over states from previous sequences to lengthen context.

## [15]
Tri Dao, Albert Gu, Matthew Eichhorn, Atri Rudra, and Christopher Re. Learning fast algorithms for linear transforms using butterfly factorizations. In *ICML*, 2019.
- Cited in 07_appendix-a-related-work.md for butterfly matrices used to express structured matrices.

## [18]
Tri Dao, Beidi Chen, Nimit Sohoni, Arjun Desai, Michael Poli, Jessica Grogan, Alexander Liu, Aniruddh Rao, Atri Rudra, and Christopher Re. Monarch: Expressive structured matrices for efficient and accurate training. In *ICML*, 2022.
- Cited in 07_appendix-a-related-work.md as an extension of butterfly matrices aimed at hardware-friendliness.

## [20]
Christopher De Sa, Albert Gu, Rohan Puttagunta, Christopher Re, and Atri Rudra. A two-pronged progress in structured dense matrix vector multiplication. In *Proceedings of the Twenty-Ninth Annual ACM-SIAM Symposium on Discrete Algorithms*, pages 1060–1079. SIAM, 2018.
- Cited in 07_appendix-a-related-work.md for butterfly matrices expressing structured matrices with almost optimal runtime and parameters.

## [21]
Peter J Denning. The working set model for program behavior. *Communications of the ACM*, 11(5):323–333, 1968.
- Cited in 07_appendix-a-related-work.md for the working set model of memory hierarchies.

## [23]
Xin Dong, Shangyu Chen, and Sinno Jialin Pan. Learning to prune deep neural networks via layer-wise optimal brain surgeon. *arXiv preprint arXiv:1705.07565*, 2017.
- Cited in 07_appendix-a-related-work.md for sparse model compression via weight matrix sparsification (pruning).

## [24]
Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, et al. An image is worth 16x16 words: Transformers for image recognition at scale. In *ICLR*, 2020.
- Cited in 07_appendix-a-related-work.md as a widely-used Transformer in computer vision.

## [25]
Y Eidelman and I Gohberg. On a new class of structured matrices. *Integral Equations and Operator Theory*, 34(3):293–324, 1999.
- Cited in 07_appendix-a-related-work.md as a class of structured matrices (quasi-separable).

## [28]
Jonathan Frankle and Michael Carbin. The lottery ticket hypothesis: Finding sparse, trainable neural networks. In *ICLR*, 2018.
- Cited in 07_appendix-a-related-work.md for the lottery tickets hypothesis in sparse training.

## [29]
Jonathan Frankle, Gintare Karolina Dziugaite, Daniel M Roy, and Michael Carbin. Stabilizing the lottery ticket hypothesis. *arXiv preprint arXiv:1903.01611*, 2019.
- Cited in 07_appendix-a-related-work.md for the lottery tickets hypothesis in sparse training.

## [30]
Jonathan Frankle, Gintare Karolina Dziugaite, Daniel Roy, and Michael Carbin. Linear mode connectivity and the lottery ticket hypothesis. In *ICML*, pages 3259–3269. PMLR, 2020.
- Cited in 07_appendix-a-related-work.md for the lottery tickets hypothesis in sparse training.

## [31]
Karan Goel, Albert Gu, Chris Donahue, and Christopher Re. It's raw! audio generation with state-space models. In *ICML*, 2022.
- Cited in 07_appendix-a-related-work.md as an S4 extension for state-space models.

## [35]
Albert Gu, Tri Dao, Stefano Ermon, Atri Rudra, and Christopher Re. Hippo: Recurrent memory with optimal polynomial projections. In *NeurIPS*, 2020.
- Cited in 07_appendix-a-related-work.md for projecting history on a polynomial basis for long context modeling.

## [36]
Albert Gu, Isys Johnson, Karan Goel, Khaled Saab, Tri Dao, Atri Rudra, and Christopher Re. Combining recurrent, convolutional, and continuous-time models with linear state space layers. *Advances in Neural Information Processing Systems*, 34, 2021.
- Cited in 07_appendix-a-related-work.md as an S4 extension using state-space models.

## [38]
Song Han, Jeff Pool, John Tran, and William J Dally. Learning both weights and connections for efficient neural networks. *arXiv preprint arXiv:1506.02626*, 2015.
- Cited in 07_appendix-a-related-work.md for sparse model compression via weight matrix sparsification (pruning).

## [39]
Song Han, Huizi Mao, and William J Dally. Deep compression: Compressing deep neural networks with pruning, trained quantization and huffman coding. In *ICLR*, 2016.
- Cited in 07_appendix-a-related-work.md for sparse model compression via weight matrix sparsification (pruning).

## [41]
Sara Hooker. The hardware lottery. *arXiv preprint arXiv:2009.06489*, 2020.
- Cited in 07_appendix-a-related-work.md for the phenomenon where structured matrices fail to achieve wall-clock speedup due to optimized dense implementations.

## [42]
Weizhe Hua, Zihang Dai, Hanxiao Liu, and Quoc V Le. Transformer quality in linear time. *arXiv preprint arXiv:2202.10447*, 2022.
- Cited in 07_appendix-a-related-work.md as an attempt at replacing attention (FLASH) in language modeling.

## [49]
Thomas Kailath, Sun-Yuan Kung, and Martin Morf. Displacement ranks of matrices and linear equations. *Journal of Mathematical Analysis and Applications*, 68(2):395–407, 1979.
- Cited in 07_appendix-a-related-work.md as a class of structured matrices (low-displacement rank).

## [52]
Zhenzhong Lan, Mingda Chen, Sebastian Goodman, Kevin Gimpel, Piyush Sharma, and Radu Soricut. Albert: A lite BEDRT for self-supervised learning of language representations. In *ICLR*, 2020.
- Cited in 07_appendix-a-related-work.md for compressing along the sequence dimension to attend to multiple tokens at once.

## [54]
Valerii Likhosherstov, Krzysztof Choromanski, Jared Davis, Xingyou Song, and Adrian Weller. Sub-linear memory: How to make performers slim. *arXiv preprint arXiv:2012.11346*, 2020.
- Cited in 07_appendix-a-related-work.md as a low-rank approximation (Performer variant).

## [55]
Ji Lin, Yongming Rao, Jiwen Lu, and Jie Zhou. Runtime neural pruning. In *NeurIPS*, volume 30, 2017.
- Cited in 07_appendix-a-related-work.md for sparse model compression via weight matrix sparsification (pruning).

## [57]
Xuezhe Ma, Xiang Kong, Sinong Wang, Chunting Zhou, Jonathan May, Hao Ma, and Luke Zettlemoyer. Luna: Linear unified nested attention. *Advances in Neural Information Processing Systems*, 34, 2021.
- Cited in 07_appendix-a-related-work.md for compressing along the sequence dimension to attend to multiple tokens at once.

## [59]
Frank McSherry, Michael Isard, and Derek G Murray. Scalability! but at what {COST}? In *15th Workshop on Hot Topics in Operating Systems (HotOS XV)*, 2015.
- Cited in 07_appendix-a-related-work.md for analyses of scalability in the context of memory hierarchies.

## [64]
D Stott Parker. Random butterfly transformations with applications in computational linear algebra. 1995.
- Cited in 07_appendix-a-related-work.md for butterfly matrices used to express structured matrices.

## [68]
Jack Rae and Ali Razavi. Do transformers need deep long-range memory? In *Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics*, 2020.
- Cited in 11_appendix-e-full-experimental-results.md as a baseline (Local Attention) in E.6 full benchmarking results.

## [69]
Jack W Rae, Anna Potapenko, Siddhant M Jayakumar, and Timothy P Lillicrap. Compressive transformers for long-range sequence modelling. In *ICLR*, 2020.
- Cited in 07_appendix-a-related-work.md for attending over states from previous sequences (Compressive Transformer).

## [73]
Hongyu Ren, Hanjun Dai, Zihang Dai, Mengjiao Yang, Jure Leskovec, Dale Schuurmans, and Bo Dai. Combiner: Full attention transformer with sparse computation cost. *Advances in Neural Information Processing Systems*, 34, 2021.
- Cited in 07_appendix-a-related-work.md as a combined sparse/low-rank approach.

## [76]
Victor Sanh, Thomas Wolf, and Alexander M Rush. Movement pruning: Adaptive sparsity by fine-tuning. *arXiv preprint arXiv:2005.07683*, 2020.
- Cited in 07_appendix-a-related-work.md for sparse model compression via weight matrix sparsification (pruning).

## [78]
Vikas Sindhwani, Tara Sainath, and Sanjiv Kumar. Structured transforms for small-footprint deep learning. In *NeurIPS*, pages 3088–3096, 2015.
- Cited in 07_appendix-a-related-work.md as a class of structured matrices (Toeplitz-like).

## [79]
Sainbayar Sukhbaatar, Edouard Grave, Piotr Bojanowski, and Armand Joulin. Adaptive attention span in transformers. In *Proceedings of the Annual Meeting of the Association for Computational Linguistics*, 2019.
- Cited in 07_appendix-a-related-work.md for compressing along the sequence dimension to attend to multiple tokens at once.

## [81]
Yi Tay, Mostafa Dehghani, Dara Bahri, and Donald Metzler. Efficient transformers: A survey. *arXiv preprint arXiv:2009.06732*, 2020.
- Cited in 07_appendix-a-related-work.md as the recommended survey on efficient Transformer methods.

## [86]
Michael E Wolf and Monica S Lam. A data locality optimizing algorithm. In *Proceedings of the ACM SIGPLAN 1991 conference on Programming language design and implementation*, pages 30–44, 1991.
- Cited in 07_appendix-a-related-work.md for data locality in the context of memory hierarchies.

## [89]
Felix Wu, Angela Fan, Alexei Baevski, Yann N Dauphin, and Michael Auli. Pay less attention with lightweight and dynamic convolutions. In *ICLR*, 2019.
- Cited in 07_appendix-a-related-work.md for compressing along the sequence dimension to attend to multiple tokens at once.

## [91]
Li Yuan, Yunpeng Chen, Tao Wang, Weihao Yu, Yujun Shi, Zi-Hang Jiang, Francis EH Tay, Jiashi Feng, and Shuicheng Yan. Tokens-to-token vit: Training vision transformers from scratch on imagenet. In *Proceedings of the IEEE/CVF International Conference on Computer Vision*, pages 558–567, 2021.
- Cited in 07_appendix-a-related-work.md as a widely-used Transformer in computer vision.

## [93]
Shuangfei Zhai, Walter Talbott, Nitish Srivastava, Chen Huang, Hanlin Goh, Ruixiang Zhang, and Josh Susskind. An attention free transformer. *arXiv preprint arXiv:2105.14103*, 2021.
- Cited in 07_appendix-a-related-work.md as an attempt at replacing attention (AFT) in image classification and language modeling.

## [94]
Chen Zhu, Wei Ping, Chaowei Xiao, Mohammad Shoeybi, Tom Goldstein, Anima Anandkumar, and Bryan Catanzaro. Long-short transformer: Efficient transformers for language and vision. *Advances in Neural Information Processing Systems*, 34, 2021.
- Cited in 07_appendix-a-related-work.md as a combined sparse/low-rank approach (Long-short transformer); in 11_appendix-e-full-experimental-results.md as a baseline (LSFormer) in E.6 full benchmarking.
