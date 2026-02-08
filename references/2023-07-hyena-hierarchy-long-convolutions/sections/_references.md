# References

This file contains only the references cited in the section notes.

---

**Basri et al., 2020**
R. Basri, M. Galun, A. Geifman, D. Jacobs, Y. Kasten, and S. Kritchman. Frequency bias in neural networks for input of non-uniform density. In *International Conference on Machine Learning*, pages 685--694. PMLR, 2020.
Cited in 03_hyena-definition-and-properties.md regarding low-frequency bias of neural networks motivating sine activations in Hyena filters.

**Black et al., 2021**
S. Black, L. Gao, P. Wang, C. Leahy, and S. Biderman. GPT-Neo: Large Scale Autoregressive Language Modeling with Mesh-Tensorflow, Mar. 2021. URL https://doi.org/10.5281/zenodo.5297715.
Cited in 04_experiments.md as the reference GPTNeo baseline in downstream evaluation (Tables 4.5, 4.6), and in 10_appendix-d-samples-visualizations.md for attention matrix comparison with Hyena.

**Brown et al., 2020**
T. Brown, B. Mann, N. Ryder, M. Subbiah, J. D. Kaplan, P. Dhariwal, A. Neelakantan, P. Shyam, G. Sastry, A. Askell, et al. Language models are few-shot learners. *Advances in Neural Information Processing Systems*, 33:1877--1901, 2020.
Cited in 04_experiments.md as standard GPT baseline (FlashAttention experiments, Figure 4.2).

**Chen, 1984**
C.-T. Chen. *Linear system theory and design*. Saunders college publishing, 1984.
Cited in 02_preliminaries-and-related-work.md regarding state-space models.

**Child et al., 2019**
R. Child, S. Gray, A. Radford, and I. Sutskever. Generating long sequences with sparse transformers. *arXiv preprint arXiv:1904.10509*, 2019.
Cited in 01_introduction.md as one of the sparse approximation approaches to reducing attention cost.

**Cramer, 2021**
P. Cramer. Alphafold2 and the future of structural biology. *Nature structural & molecular biology*, 28(9):704--705, 2021.
Cited in 01_introduction.md as an example of Transformer breakthroughs in biology.

**Dao et al., 2019**
T. Dao, A. Gu, M. Eichhorn, A. Rudra, and C. Re. Learning fast algorithms for linear transforms using butterfly factorizations. In *International Conference on Machine Learning*, pages 1517--1527. PMLR, 2019.
Cited in 03_hyena-definition-and-properties.md regarding butterfly decompositions for fast matrix-vector multiplications.

**Dao et al., 2022a**
T. Dao, B. Chen, N. S. Sohoni, A. Desai, M. Poli, J. Grogan, A. Liu, A. Rao, A. Rudra, and C. Re. Monarch: Expressive structured matrices for efficient and accurate training. In *International Conference on Machine Learning*, pages 4690--4721. PMLR, 2022a.
Cited in 03_hyena-definition-and-properties.md regarding butterfly decompositions.

**Dao et al., 2022b**
T. Dao, D. Y. Fu, S. Ermon, A. Rudra, and C. Re. Flashattention: Fast and memory-efficient exact attention with io-awareness. *arXiv preprint arXiv:2205.14135*, 2022b.
Cited in 01_introduction.md and 04_experiments.md as the FlashAttention baseline for speed benchmarking.

**Dao et al., 2022c**
T. Dao, D. Y. Fu, K. K. Saab, A. W. Thomas, A. Rudra, and C. Re. Hungry hungry hippos: Towards language modeling with state space models. *arXiv preprint arXiv:2212.14052*, 2022c.
Cited extensively throughout: in 01_introduction.md as H3 method requiring hybridization, in 03_hyena-definition-and-properties.md as the mechanism Hyena generalizes, in 04_experiments.md for associative recall benchmarks and WikiText103 perplexity results, for FFTConv CUDA kernel, in 07_appendix-a-experimental-details.md regarding hybrid architectures and WikiText103 baselines, and in 08_appendix-b-theoretical-results.md regarding the H3 mechanism in surrogate attention analysis.

**Dosovitskiy et al., 2020**
A. Dosovitskiy, L. Beyer, A. Kolesnikov, D. Weissenborn, X. Zhai, T. Unterthiner, M. Dehghani, M. Minderer, G. Heigold, S. Gelly, et al. An image is worth 16x16 words: Transformers for image recognition at scale. *arXiv preprint arXiv:2010.11929*, 2020.
Cited in 01_introduction.md as an example of Transformer breakthroughs in vision, and in 04_experiments.md as the ViT architecture used in image classification experiments.

**Elhage et al., 2021**
N. Elhage, N. Nanda, C. Olsson, T. Henighan, N. Joseph, B. Mann, A. Askell, Y. Bai, A. Chen, T. Conerly, et al. A mathematical framework for transformer circuits. *Transformer Circuits Thread*, 2021.
Cited in 01_introduction.md and 04_experiments.md regarding mechanistic interpretability of Transformers motivating Hyena design, in 07_appendix-a-experimental-details.md as inspiration for synthetic benchmarks, and in 09_appendix-c-discussion-additional-results.md regarding circuits-based analysis for single layer recall.

**Fukushima and Miyake, 1982**
K. Fukushima and S. Miyake. Neocognitron: A self-organizing neural network model for a mechanism of visual pattern recognition. In *Competition and cooperation in neural nets*, pages 267--285. Springer, 1982.
Cited in 02_preliminaries-and-related-work.md as early CNN work.

**Garg et al., 2022**
S. Garg, D. Tsipras, P. Liang, and G. Valiant. What can transformers learn in-context? a case study of simple function classes. *arXiv preprint arXiv:2208.01066*, 2022.
Cited in 01_introduction.md regarding the emergence of in-context learning in Transformers, and in 07_appendix-a-experimental-details.md as ICL research inspiring synthetic benchmarks.

**Gu et al., 2020**
A. Gu, T. Dao, S. Ermon, A. Rudra, and C. Re. Hippo: Recurrent memory with optimal polynomial projections. *Advances in Neural Information Processing Systems*, 33:1474--1487, 2020.
Cited in 02_preliminaries-and-related-work.md and 03_hyena-definition-and-properties.md regarding SSMs and long convolution models.

**Gu et al., 2021**
A. Gu, K. Goel, and C. Re. Efficiently modeling long sequences with structured state spaces. *arXiv preprint arXiv:2111.00396*, 2021.
Cited in 02_preliminaries-and-related-work.md, 03_hyena-definition-and-properties.md, 04_experiments.md, and 07_appendix-a-experimental-details.md as S4, the standard SSM-based long convolution parametrization.

**He et al., 2016**
K. He, X. Zhang, S. Ren, and J. Sun. Deep residual learning for image recognition. In *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition*, pages 770--778, 2016.
Cited in 02_preliminaries-and-related-work.md as a classical CNN reference.

**Hoffmann et al., 2022**
J. Hoffmann, S. Borgeaud, A. Mensch, E. Buchatskaya, T. Cai, E. Rutherford, D. d. l. Casas, L. A. Hendricks, J. Welbl, A. Clark, et al. Training compute-optimal large language models. *arXiv preprint arXiv:2203.15556*, 2022.
Cited in 01_introduction.md regarding scaling properties of Transformers, and in 07_appendix-a-experimental-details.md for the FLOP computation strategy.

**Kitaev et al., 2020**
N. Kitaev, L. Kaiser, and A. Levskaya. Reformer: The efficient transformer. *arXiv preprint arXiv:2001.04451*, 2020.
Cited in 01_introduction.md as one of the sparse/low-rank approximation approaches.

**LeCun et al., 1998**
Y. LeCun, L. Bottou, Y. Bengio, and P. Haffner. Gradient-based learning applied to document recognition. *Proceedings of the IEEE*, 86(11):2278--2324, 1998.
Cited in 02_preliminaries-and-related-work.md as a classical CNN reference.

**Li et al., 2015**
Y. Li, H. Yang, E. R. Martin, K. L. Ho, and L. Ying. Butterfly factorization. *Multiscale Modeling & Simulation*, 13(2):714--732, 2015.
Cited in 03_hyena-definition-and-properties.md regarding butterfly decompositions for fast matrix-vector multiplications.

**Li et al., 2020**
Z. Li, N. Kovachki, K. Azizzadenesheli, B. Liu, K. Bhattacharya, A. Stuart, and A. Anandkumar. Fourier neural operator for parametric partial differential equations. *arXiv preprint arXiv:2010.08895*, 2020.
Cited in 02_preliminaries-and-related-work.md, 04_experiments.md, and 07_appendix-a-experimental-details.md as the FNO frequency-domain parametrization compared in experiments.

**Li et al., 2022**
Y. Li, T. Cai, Y. Zhang, D. Chen, and D. Dey. What makes convolutional models great on long sequence modeling? *arXiv preprint arXiv:2210.09298*, 2022.
Cited in 03_hyena-definition-and-properties.md regarding SGConv and observations about exponential decay filters.

**Massaroli et al., 2020**
S. Massaroli, M. Poli, J. Park, A. Yamashita, and H. Asama. Dissecting neural odes. *Advances in Neural Information Processing Systems*, 33:3952--3963, 2020.
Cited in 01_introduction.md regarding the concept of data-controlled operators.

**Mehta et al., 2022**
H. Mehta, A. Gupta, A. Cutkosky, and B. Neyshabur. Long range language modeling via gated state spaces. *arXiv preprint arXiv:2206.13947*, 2022.
Cited in 01_introduction.md and 03_hyena-definition-and-properties.md as the GSS method (Hyena$_1$ special case), and in 04_experiments.md as a baseline in associative recall.

**Mildenhall et al., 2021**
B. Mildenhall, P. P. Srinivasan, M. Tancik, J. T. Barron, R. Ramamoorthi, and R. Ng. Nerf: Representing scenes as neural radiance fields for view synthesis. *Communications of the ACM*, 65(1):99--106, 2021.
Cited in 03_hyena-definition-and-properties.md regarding neural implicit representation literature.

**Nguyen et al., 2022**
E. Nguyen, K. Goel, A. Gu, G. W. Downs, P. Shah, T. Dao, S. A. Baccus, and C. Re. S4nd: Modeling images and videos as multidimensional signals using state spaces. *arXiv preprint arXiv:2210.06583*, 2022.
Cited in 04_experiments.md and 07_appendix-a-experimental-details.md as the S4ND baseline for image classification experiments.

**Olsson et al., 2022**
C. Olsson, N. Elhage, N. Nanda, N. Joseph, N. DasSarma, T. Henighan, B. Mann, A. Askell, Y. Bai, A. Chen, et al. In-context learning and induction heads. *arXiv preprint arXiv:2209.11895*, 2022.
Cited in 01_introduction.md and 04_experiments.md regarding mechanistic interpretability and in-context learning.

**Oppenheim et al., 1997**
A. V. Oppenheim, A. S. Willsky, S. H. Nawab, and J.-J. Ding. *Signals and systems*, volume 2. Prentice hall Upper Saddle River, NJ, 1997.
Cited in 02_preliminaries-and-related-work.md regarding the convolution theorem of DFT.

**Paperno et al., 2016**
D. Paperno, G. Kruszewski, A. Lazaridou, Q. N. Pham, R. Bernardi, S. Pezzelle, M. Baroni, G. Boleda, and R. Fernandez. The lambada dataset: Word prediction requiring a broad discourse context. *arXiv preprint arXiv:1606.06031*, 2016.
Cited in 04_experiments.md and 07_appendix-a-experimental-details.md regarding the LAMBADA task evaluation.

**Peng, 2021**
B. Peng. RWKV-LM, 8 2021. URL https://github.com/BlinkDL/RWKV-LM.
Cited in 04_experiments.md as the RWKV baseline in downstream evaluation (Tables 4.2, 4.5, 4.6), and in 10_appendix-d-samples-visualizations.md as the comparison model (RWKV-v4, 169M) in D.4 downstream examples.

**Power et al., 2022**
A. Power, Y. Burda, H. Edwards, I. Babuschkin, and V. Misra. Grokking: Generalization beyond overfitting on small algorithmic tasks. *arXiv preprint arXiv:2201.02177*, 2022.
Cited in 01_introduction.md and 04_experiments.md regarding mechanistic interpretability benchmarks.

**Radford et al., 2022**
A. Radford, J. W. Kim, T. Xu, G. Brockman, C. McLeavey, and I. Sutskever. Robust speech recognition via large-scale weak supervision. *arXiv preprint arXiv:2212.04356*, 2022.
Cited in 01_introduction.md as an example of Transformer breakthroughs in audio.

**Rae et al., 2019**
J. W. Rae, A. Potapenko, S. M. Jayakumar, C. Hillier, and T. P. Lillicrap. Compressive transformers for long-range sequence modelling. *arXiv preprint*, 2019. URL https://arxiv.org/abs/1911.05507.
Cited in 04_experiments.md and 07_appendix-a-experimental-details.md regarding PG-19 long-range benchmark results.

**Romero et al., 2021a**
D. W. Romero, R.-J. Bruintjes, J. M. Tomczak, E. J. Bekkers, M. Hoogendoorn, and J. C. van Gemert. Flexconv: Continuous kernel convolutions with differentiable kernel sizes. *arXiv preprint arXiv:2110.08059*, 2021a.
Cited in 02_preliminaries-and-related-work.md and 03_hyena-definition-and-properties.md regarding implicit filter parametrization via FFNs.

**Romero et al., 2021b**
D. W. Romero, A. Kuzina, E. J. Bekkers, J. M. Tomczak, and M. Hoogendoorn. Ckconv: Continuous kernel convolution for sequential data. *arXiv preprint arXiv:2102.02611*, 2021b.
Cited in 02_preliminaries-and-related-work.md, 03_hyena-definition-and-properties.md, 04_experiments.md, and 07_appendix-a-experimental-details.md as CKConv, an implicit parametrization using FFNs compared in experiments.

**Ronneberger et al., 2015**
O. Ronneberger, P. Fischer, and T. Brox. U-net: Convolutional networks for biomedical image segmentation. In *International Conference on Medical Image Computing and Computer-Assisted Intervention*, pages 234--241. Springer, 2015.
Cited in 02_preliminaries-and-related-work.md as a classical CNN reference.

**Roy et al., 2021**
A. Roy, M. Saffar, A. Vaswani, and D. Grangier. Efficient content-based sparse attention with routing transformers. *Transactions of the Association for Computational Linguistics*, 9:53--68, 2021.
Cited in 01_introduction.md as one of the sparse approximation approaches to reducing attention cost.

**Schlag et al., 2021**
I. Schlag, K. Irie, and J. Schmidhuber. Linear transformers are secretly fast weight programmers. In *International Conference on Machine Learning*, pages 9355--9366. PMLR, 2021.
Cited in 01_introduction.md as one of the linearized approaches to reducing attention cost.

**Selesnick and Burrus, 2017**
I. W. Selesnick and C. S. Burrus. Fast convolution and filtering. In *The Digital Signal Processing Handbook*, pages 8--1. CRC Press, 2017.
Cited in 01_introduction.md and 02_preliminaries-and-related-work.md regarding fast convolution algorithms and circular convolution.

**Sitzmann et al., 2020**
V. Sitzmann, J. N. Martel, A. W. Bergman, D. B. Lindell, and G. Wetzstein. Implicit neural representations with periodic activation functions. *arXiv preprint arXiv:2006.09661*, 2020.
Cited in 03_hyena-definition-and-properties.md regarding neural implicit representation literature.

**Tu et al., 2022**
Z. Tu, H. Talebi, H. Zhang, F. Yang, P. Milanfar, A. Bovik, and Y. Li. Maxvit: Multi-axis vision transformer. *arXiv preprint arXiv:2204.01697*, 2022.
Cited in 01_introduction.md as one of the approaches to reducing attention cost.

**Vaswani et al., 2017**
A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, L. Kaiser, and I. Polosukhin. Attention is all you need. In *Advances in Neural Information Processing Systems*, pages 5998--6008, 2017.
Cited in 01_introduction.md and 02_preliminaries-and-related-work.md as the original Transformer/attention paper.

**Wang et al., 2019**
A. Wang, Y. Pruksachatkun, N. Nangia, A. Singh, J. Michael, F. Hill, O. Levy, and S. Bowman. Superglue: A stickier benchmark for general-purpose language understanding systems. *Advances in Neural Information Processing Systems*, 32, 2019.
Cited in 04_experiments.md and 07_appendix-a-experimental-details.md as the SuperGLUE benchmark used in downstream evaluation.

**Wang et al., 2020**
S. Wang, B. Z. Li, M. Khabsa, H. Fang, and H. Ma. Linformer: Self-attention with linear complexity. *arXiv preprint arXiv:2006.04768*, 2020.
Cited in 01_introduction.md as one of the low-rank approximation approaches.

**Zhai et al., 2021**
S. Zhai, W. Talbott, N. Srivastava, C. Huang, H. Goh, R. Zhang, and J. Susskind. An attention free transformer. *arXiv preprint arXiv:2105.14103*, 2021.
Cited in 01_introduction.md and 02_preliminaries-and-related-work.md as the AFT method, and in 04_experiments.md as AFT-conv baseline.

**Zhang et al., 2022**
Y. Zhang, A. Backurs, S. Bubeck, R. Eldan, S. Gunasekar, and T. Wagner. Unveiling transformers with lego: a synthetic reasoning task. *arXiv preprint arXiv:2206.04301*, 2022.
Cited in 01_introduction.md and 04_experiments.md regarding mechanistic interpretability benchmarks.

**Arora et al., 2022**
S. Arora, A. Narayan, M. F. Chen, L. J. Orr, N. Guha, K. Bhatia, I. Chami, F. Sala, and C. Re. Ask me anything: A simple strategy for prompting language models. *arXiv preprint arXiv:2210.02441*, 2022.
Cited in 07_appendix-a-experimental-details.md as the parsing pipeline used for SuperGLUE evaluation.

**Cubuk et al., 2020**
E. D. Cubuk, B. Zoph, J. Shlens, and Q. V. Le. Randaugment: Practical automated data augmentation with a reduced search space. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops*, pages 702--703, 2020.
Cited in 07_appendix-a-experimental-details.md as a data augmentation method used in ImageNet training.

**Gao et al., 2020**
L. Gao, S. Biderman, S. Black, L. Golding, T. Hoppe, C. Foster, J. Phang, H. He, A. Thite, N. Nabeshima, et al. The pile: An 800gb dataset of diverse text for language modeling. *arXiv preprint arXiv:2101.00027*, 2020.
Cited in 07_appendix-a-experimental-details.md as The Pile dataset used for language modeling experiments.

**Hendrycks et al., 2019**
D. Hendrycks, N. Mu, E. D. Cubuk, B. Zoph, J. Gilmer, and B. Lakshminarayanan. Augmix: A simple data processing method to improve robustness and uncertainty. *arXiv preprint arXiv:1912.02781*, 2019.
Cited in 07_appendix-a-experimental-details.md as a data augmentation method used in ImageNet training.

**Liang et al., 2022**
P. Liang, R. Bommasani, T. Lee, D. Tsipras, D. Soylu, M. Yasunaga, Y. Zhang, D. Narayanan, Y. Wu, A. Kumar, et al. Holistic evaluation of language models. *arXiv preprint arXiv:2211.09110*, 2022.
Cited in 07_appendix-a-experimental-details.md as language model benchmarking research inspiring synthetic benchmarks.

**Yuan et al., 2021**
L. Yuan, Y. Chen, T. Wang, W. Yu, Y. Shi, Z.-H. Jiang, F. E. Tay, J. Feng, and S. Yan. Tokens-to-token vit: Training vision transformers from scratch on imagenet. In *Proceedings of the IEEE/CVF International Conference on Computer Vision*, pages 558--567, 2021.
Cited in 07_appendix-a-experimental-details.md as the T2T-ViT training procedure used for ImageNet experiments.

**Zhang et al., 2017**
H. Zhang, M. Cisse, Y. N. Dauphin, and D. Lopez-Paz. mixup: Beyond empirical risk minimization. *arXiv preprint arXiv:1710.09412*, 2017.
Cited in 07_appendix-a-experimental-details.md as a data augmentation method used in ImageNet training.

**Huang et al., 2016**
G. Huang, Y. Sun, Z. Liu, D. Sedra, and K. Q. Weinberger. Deep networks with stochastic depth. In *European conference on computer vision*, pages 646--661. Springer, 2016.
Cited in 07_appendix-a-experimental-details.md (Table A.5) as a training technique used for ImageNet ViT/Hyena-ViT experiments.

**Polyak and Juditsky, 1992**
B. T. Polyak and A. B. Juditsky. Acceleration of stochastic approximation by averaging. *SIAM journal on control and optimization*, 30(4):838--855, 1992.
Cited in 07_appendix-a-experimental-details.md (Table A.5) as the EMA method (set to None in ViT/Hyena-ViT training).

**Szegedy et al., 2016**
C. Szegedy, V. Vanhoucke, S. Ioffe, J. Shlens, and Z. Wojna. Rethinking the inception architecture for computer vision. In *Proceedings of the IEEE conference on computer vision and pattern recognition*, pages 2818--2826, 2016.
Cited in 07_appendix-a-experimental-details.md (Table A.5) as the label smoothing technique used in ImageNet training.

**Yun et al., 2019**
S. Yun, D. Han, S. J. Oh, S. Chun, J. Choe, and Y. Yoo. Cutmix: Regularization strategy to train strong classifiers with localizable features. In *Proceedings of the IEEE/CVF international conference on computer vision*, pages 6023--6032, 2019.
Cited in 07_appendix-a-experimental-details.md (Table A.5) as a data augmentation method used in ImageNet training.

**Zhong et al., 2020**
Z. Zhong, L. Zheng, G. Kang, S. Li, and Y. Yang. Random erasing data augmentation. In *Proceedings of the AAAI conference on artificial intelligence*, volume 34, pages 13001--13008, 2020.
Cited in 07_appendix-a-experimental-details.md (Table A.5) as a data augmentation method used in ImageNet training.
