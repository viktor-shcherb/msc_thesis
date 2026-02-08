# References

Only references cited in the section notes are included below.

## [1]
Martin Arjovsky, Amar Shah, and Yoshua Bengio. Unitary evolution recurrent neural networks. In *The International Conference on Machine Learning (ICML)*, pages 1120-1128, 2016.
- Cited in 01_introduction.md (orthogonal RNNs to combat vanishing gradients) and 04_experiments.md (LRD tests for RNNs on pixel-level image classification).

## [2]
Alexei Baevski and Michael Auli. Adaptive input representations for neural language modeling. *arXiv preprint arXiv:1809.10853*, 2018.
- Cited in 04_experiments.md as the strong Transformer baseline for WikiText-103 language modeling that S4's implementation is based on, and in 10a_appendix-d3-general-sequence-modeling.md (S4 uses the same Transformer backbone; Adaptive Embedding with standard cutoffs; evaluation and generation speed baselines).

## [3]
Shaojie Bai, J Zico Kolter, and Vladlen Koltun. An empirical evaluation of generic convolutional and recurrent networks for sequence modeling. *arXiv preprint arXiv:1803.01271*, 2018.
- Cited in 01_introduction.md (dilated convolutions to increase context size) and 10a_appendix-d3-general-sequence-modeling.md (TCN baseline in Table 12).

## [4]
Shaojie Bai, J Zico Kolter, and Vladlen Koltun. Trellis networks for sequence modeling. In *The International Conference on Learning Representations (ICLR)*, 2019.
- Cited in 10a_appendix-d3-general-sequence-modeling.md (TrellisNet baseline in WikiText-103 and Table 12).

## [5]
Shiyu Chang, Yang Zhang, Wei Han, Mo Yu, Xiaoxiao Guo, Wei Tan, Xiaodong Cui, Michael Witbrock, Mark Hasegawa-Johnson, and Thomas S Huang. Dilated recurrent neural networks. In *Advances in Neural Information Processing Systems (NeurIPS)*, 2017.
- Cited in 10a_appendix-d3-general-sequence-modeling.md (Dilated GRU and Dilated RNN baselines in Table 12).

## [6]
Rewon Child, Scott Gray, Alec Radford, and Ilya Sutskever. Generating long sequences with sparse transformers. *arXiv preprint arXiv:1904.10509*, 2019.
- Cited in 10a_appendix-d3-general-sequence-modeling.md (Sparse Transformer could not be run due to CUDA implementation issues).

## [7]
Narsimha Chilkuri and Chris Eliasmith. Parallelizing legendre memory unit training. *The International Conference on Machine Learning (ICML)*, 2021.
- Cited in 07_appendix-a-discussion.md (showed that Voelker et al.'s SSM could be sped up at train time with a convolutional view) and 10a_appendix-d3-general-sequence-modeling.md (LMUFFT baseline in Table 12).

## [8]
Krzysztof Choromanski, Valerii Likhosherstov, David Dohan, Xingyou Song, Andreea Gane, Tamas Sarlos, Peter Hawkins, Jared Davis, Afroz Mohiuddin, Lukasz Kaiser, et al. Rethinking attention with performers. In *The International Conference on Learning Representations (ICLR)*, 2020.
- Cited in 01_introduction.md (efficient Transformer variant), 04_experiments.md (efficiency benchmark baseline, LRA baseline), and 10_appendix-d-experiment-details.md (Speech Commands Performer baseline sweep details).

## [9]
Yann N Dauphin, Angela Fan, Michael Auli, and David Grangier. Language modeling with gated convolutional networks. In *International conference on machine learning*, pages 933-941. PMLR, 2017.
- Cited in 10a_appendix-d3-general-sequence-modeling.md (CNN with GLU activations baseline for WikiText-103).

## [10]
Edward De Brouwer, Jaak Simm, Adam Arany, and Yves Moreau. Gru-ode-bayes: Continuous modeling of sporadically-observed time series. In *Advances in Neural Information Processing Systems (NeurIPS)*, 2019.
- Cited in 04_experiments.md (dedicated line of work on irregularly sampled data / sampling resolution change).

## [11]
Chris Donahue, Julian McAuley, and Miller Puckette. Adversarial audio synthesis. In *ICLR*, 2019.
- Cited in 04_experiments.md (WaveGAN discriminator used as a baseline CNN for raw speech classification; worse than S4 with 90x more parameters) and 10_appendix-d-experiment-details.md (WaveGAN-D baseline details and specialization compared to S4).

## [12]
Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, et al. An image is worth 16x16 words: Transformers for image recognition at scale. *arXiv preprint arXiv:2010.11929*, 2020.
- Cited in 01_introduction.md (Vision Transformers as example of reduced specialization) and 04_experiments.md (Vision Transformers for pixel-level image classification with less 2-D information).

## [13]
N Benjamin Erichson, Omri Azencot, Alejandro Queiruga, Liam Hodgkinson, and Michael W Mahoney. Lipschitz recurrent neural networks. In *International Conference on Learning Representations*, 2021.
- Cited in 01_introduction.md (Lipschitz RNNs to combat vanishing gradients), 10_appendix-d-experiment-details.md (Speech Commands LipschitzRNN baseline sweep details), and 10a_appendix-d3-general-sequence-modeling.md (LipschitzRNN baseline in Table 12).

## [14]
Karan Goel, Albert Gu, Chris Donahue, and Christopher Re. It's raw! audio generation with state-space models. *arXiv preprint arXiv:2202.09729*, 2022.
- Cited in 03b_architecture-details.md (follow-up work that found S4 can sometimes suffer from numerical instabilities; introduced the P P^* parameterization fix).

## [15]
Gene H Golub and Charles F Van Loan. *Matrix computations*, volume 3. JHU press, 2013.
- Cited in 09c_appendix-c3-convolutional-view.md (Woodbury matrix identity, Proposition 4).

## [16]
Albert Gu, Tri Dao, Stefano Ermon, Atri Rudra, and Christopher Re. Hippo: Recurrent memory with optimal polynomial projections. In *Advances in Neural Information Processing Systems (NeurIPS)*, 2020.
- Cited in 01_introduction.md, 02_background-state-spaces.md (HiPPO theory of continuous-time memorization), 03_method-structured-state-spaces.md (Theorem 1 on NPLR representation of HiPPO matrices), 07_appendix-a-discussion.md (extended the SSM to a general continuous-time function approximation framework), 09a_appendix-c1-nplr-representations.md (generalized Laguerre polynomial case of HiPPO), and 10a_appendix-d3-general-sequence-modeling.md (HiPPO-RNN baseline in Table 12).

## [17]
Albert Gu, Caglar Gulcehre, Tom Le Paine, Matt Hoffman, and Razvan Pascanu. Improving the gating mechanism of recurrent neural networks. In *The International Conference on Machine Learning (ICML)*, 2020.
- Cited in 10a_appendix-d3-general-sequence-modeling.md (LSTM and UR-GRU baselines in Table 12).

## [18]
Albert Gu, Isys Johnson, Karan Goel, Khaled Saab, Tri Dao, Atri Rudra, and Christopher Re. Combining recurrent, convolutional, and continuous-time models with the structured learnable linear state space layer. In *Advances in Neural Information Processing Systems (NeurIPS)*, 2021.
- Cited in 01_introduction.md (LSSL -- proof of concept that deep SSMs can address LRDs), 03_method-structured-state-spaces.md (proposed a different unimplemented algorithm), 07_appendix-a-discussion.md (most recent prior work using full SSM explicitly as a deep model), 08_appendix-b-numerical-instability.md (Theorem 2 from this work shown to be numerically unstable), 10_appendix-d-experiment-details.md (LSSL state size N set to H as done in this work; Speech Commands baseline numbers), and 10b_appendix-d3.5-d4-d5.md (SC dataset used in prior work).

## [19]
Albert Gu, Ankit Gupta, Karan Goel, and Christopher Re. On the parameterization and initialization of diagonal state space models. *arXiv preprint arXiv:2206.11893*, 2022.
- Cited in 10b_appendix-d3.5-d4-d5.md (D.5 Reproduction: updated LRA results from this follow-up; hyperparameter changes documented in Appendix B; Table 11 for Speech Commands baselines).

## [20]
Albert Gu, Isys Johnson, Aman Timalsina, Atri Rudra, and Christopher Re. How to train your hippo: State space models with generalized basis projections. *arXiv preprint arXiv:2206.12037*, 2022.
- Cited in 10b_appendix-d3.5-d4-d5.md (D.5 Reproduction: updated LRA results from this follow-up; S4-LegS refers to the same model).

## [21]
Sepp Hochreiter and Jurgen Schmidhuber. Long short-term memory. *Neural computation*, 9(8):1735-1780, 1997.
- Cited in 10a_appendix-d3-general-sequence-modeling.md (LSTM baseline in Table 12).

## [22]
Angelos Katharopoulos, Apoorv Vyas, Nikolaos Pappas, and Francois Fleuret. Transformers are rnns: Fast autoregressive transformers with linear attention. In *International Conference on Machine Learning*, pages 5156-5165. PMLR, 2020.
- Cited in 01_introduction.md (Linear Transformer, efficient Transformer variant), 04_experiments.md (efficiency benchmark baseline), and 10a_appendix-d3-general-sequence-modeling.md (Transformer and Linear Transformer generation speed baselines reported from this work; CIFAR-10 memory limit set to match their results).

## [23]
Patrick Kidger, James Morrill, James Foster, and Terry Lyons. Neural controlled differential equations for irregular time series. *arXiv preprint arXiv:2005.08926*, 2020.
- Cited in 10b_appendix-d3.5-d4-d5.md (D.5 Reproduction: part of line of work using 10-class SC subset).

## [24]
Mario Lezcano-Casado and David Martinez-Rubio. Cheap orthogonal constraints in neural networks: A simple parametrization of the orthogonal and unitary group. In *The International Conference on Machine Learning (ICML)*, 2019.
- Cited in 10_appendix-d-experiment-details.md (ExpRNN baseline sweep details for Speech Commands) and 10a_appendix-d3-general-sequence-modeling.md (expRNN baseline in Table 12).

## [25]
Shuai Li, Wanqing Li, Chris Cook, Ce Zhu, and Yanbo Gao. Independently recurrent neural network (IndRNN): Building a longer and deeper RNN. In *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition*, pages 5457-5466, 2018.
- Cited in 10a_appendix-d3-general-sequence-modeling.md (IndRNN baseline in Table 12).

## [26]
Vasileios Lioutas and Yuhong Guo. Time-aware large kernel convolutions. In *International Conference on Machine Learning*, pages 6172-6183. PMLR, 2020.
- Cited in 10a_appendix-d3-general-sequence-modeling.md (TaLK Convolutions baseline for WikiText-103; example user of the Transformer baseline from [2]).

## [27]
Stephen Merity, Nitish Shirish Keskar, James Bradbury, and Richard Socher. Scalable language modeling: Wikitext-103 on a single gpu in 12 hours. *SysML*, 2018.
- Cited in 10a_appendix-d3-general-sequence-modeling.md (AWD-QRNN baseline for WikiText-103).

## [28]
Aaron van den Oord, Sander Dieleman, Heiga Zen, Karen Simonyan, Oriol Vinyals, Alex Graves, Nal Kalchbrenner, Andrew Senior, and Koray Kavukcuoglu. Wavenet: A generative model for raw audio. *arXiv preprint arXiv:1609.03499*, 2016.
- Cited in 01_introduction.md (dilated convolutions to increase context size).

## [29]
Victor Pan. *Structured matrices and polynomials: unified superfast algorithms*. Springer Science & Business Media, 2001.
- Cited in 03_method-structured-state-spaces.md (Vandermonde product complexity, fast algorithms for Cauchy matrices based on FMM) and 09c_appendix-c3-convolutional-view.md (fast numerical algorithms for Cauchy matrices based on FMM).

## [30]
Victor Pan. Fast approximate computations with cauchy matrices and polynomials. *Mathematics of Computation*, 86(308):2799-2826, 2017.
- Cited in 03_method-structured-state-spaces.md (stable near-linear algorithms for Cauchy matrices) and 09c_appendix-c3-convolutional-view.md (fast numerical algorithms for Cauchy matrices).

## [31]
Victor Y Pan. Transformations of matrix structures work again. *Linear Algebra and Its Applications*, 465:107-138, 2015.
- Cited in 03_method-structured-state-spaces.md (stable near-linear algorithms for Cauchy matrices) and 09c_appendix-c3-convolutional-view.md (fast numerical algorithms for Cauchy matrices).

## [33]
Jack Rae, Chris Dyer, Peter Dayan, and Timothy Lillicrap. Fast parametric learning with activation memorization. *The International Conference on Machine Learning (ICML)*, 2018.
- Cited in 10a_appendix-d3-general-sequence-modeling.md (LSTM + Cache + Hebbian + MbPA, the best performing pure RNN for WikiText-103).

## [34]
Prajit Ramachandran, Tom Le Paine, Pooya Khorrami, Mohammad Babaeizadeh, Shiyu Chang, Yang Zhang, Mark A Hasegawa-Johnson, Roy H Campbell, and Thomas S Huang. Fast generation for convolutional autoregressive models. *arXiv preprint arXiv:1704.06001*, 2017.
- Cited in 10a_appendix-d3-general-sequence-modeling.md (fast cached PixelCNN++ version used for generation speed benchmarking).

## [32]
Razvan Pascanu, Tomas Mikolov, and Yoshua Bengio. On the difficulty of training recurrent neural networks. In *International conference on machine learning*, pages 1310-1318, 2013.
- Cited in 02_background-state-spaces.md (vanishing/exploding gradients problem).

## [35]
David W Romero, Anna Kuzina, Erik J Bekkers, Jakub M Tomczak, and Mark Hoogendoorn. Ckconv: Continuous kernel convolution for sequential data. *arXiv preprint arXiv:2102.02611*, 2021.
- Cited in 04_experiments.md (raw speech classification baseline following their protocol; also cited for sampling resolution change work), 10a_appendix-d3-general-sequence-modeling.md (CKConv baseline in Table 12), and 10b_appendix-d3.5-d4-d5.md (D.5: part of line of work using 10-class SC subset).

## [36]
David W Romero, Robert-Jan Bruintjes, Jakub M Tomczak, Erik J Bekkers, Mark Hoogendoorn, and Jan C van Gemert. Flexconv: Continuous kernel convolutions with differentiable kernel sizes. In *The International Conference on Learning Representations (ICLR)*, 2022.
- Cited in 10b_appendix-d3.5-d4-d5.md (D.5: part of line of work using 10-class SC subset).

## [37]
Yulia Rubanova, Tian Qi Chen, and David K Duvenaud. Latent ordinary differential equations for irregularly-sampled time series. In *Advances in Neural Information Processing Systems*, pages 5321-5331, 2019.
- Cited in 04_experiments.md (dedicated line of work on irregularly sampled data / sampling resolution change).

## [38]
T Konstantin Rusch and Siddhartha Mishra. Unicornn: A recurrent model for learning very long time dependencies. *The International Conference on Machine Learning (ICML)*, 2021.
- Cited in 10a_appendix-d3-general-sequence-modeling.md (UNIcoRNN baseline in Table 12).

## [39]
Tim Salimans, Andrej Karpathy, Xi Chen, and Diederik P Kingma. Pixelcnn++: Improving the pixelcnn with discretized logistic mixture likelihood and other modifications. *arXiv preprint arXiv:1701.05517*, 2017.
- Cited in 10a_appendix-d3-general-sequence-modeling.md (UNet-style backbone and mixture of logistics loss for CIFAR density estimation).

## [40]
Yi Tay, Mostafa Dehghani, Samira Abnar, Yikang Shen, Dara Bahri, Philip Pham, Jinfeng Rao, Liu Yang, Sebastian Ruder, and Donald Metzler. Long range arena: A benchmark for efficient transformers. In *International Conference on Learning Representations*, 2021.
- Cited in 01_introduction.md (LRA benchmark highlighting poor LRD performance), 04_experiments.md (LRA benchmark protocol and baselines; efficiency benchmark protocol), and 10_appendix-d-experiment-details.md (Transformer benchmark protocol; extended LRA results table with all 11 methods).

## [41]
Ilya Tolstikhin, Neil Houlsby, Alexander Kolesnikov, Lucas Beyer, Xiaohua Zhai, Thomas Unterthiner, Jessica Yung, Daniel Keysers, Jakob Uszkoreit, Mario Lucic, et al. Mlp-mixer: An all-mlp architecture for vision. *arXiv preprint arXiv:2105.01601*, 2021.
- Cited in 04_experiments.md (patch-based model without 2-D inductive bias, referenced alongside Vision Transformers).

## [42]
Trieu H Trinh, Andrew M Dai, Minh-Thang Luong, and Quoc V Le. Learning longer-term dependencies in RNNs with auxiliary losses. In *The International Conference on Machine Learning (ICML)*, 2018.
- Cited in 10a_appendix-d3-general-sequence-modeling.md (Transformer and r-LSTM baselines in Table 12).

## [43]
Arnold Tustin. A method of analysing the behaviour of linear systems in terms of time series. *Journal of the Institution of Electrical Engineers-Part IIA: Automatic Regulators and Servo Mechanisms*, 94(1):130-142, 1947.
- Cited in 02_background-state-spaces.md (bilinear discretization method used to convert continuous-time SSM to discrete-time).

## [44]
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and Illia Polosukhin. Attention is all you need. In *Advances in Neural Information Processing Systems (NeurIPS)*, 2017.
- Cited in 10_appendix-d-experiment-details.md (Speech Commands Transformer baseline sweep details) and 10a_appendix-d3-general-sequence-modeling.md (Transformer baseline in Table 12).

## [45]
Aaron Voelker, Ivana Kajic, and Chris Eliasmith. Legendre memory units: Continuous-time representation in recurrent neural networks. In *Advances in Neural Information Processing Systems*, pages 15544-15553, 2019.
- Cited in 01_introduction.md (structured state matrices for LRDs), 07_appendix-a-discussion.md (derived a non-trainable SSM motivated from approximating a neuromorphic spiking model), and 10a_appendix-d3-general-sequence-modeling.md (LMU baseline in Table 12).

## [46]
Aaron Russell Voelker. *Dynamical systems in spiking neuromorphic hardware*. PhD thesis, University of Waterloo, 2019.
- Cited in 07_appendix-a-discussion.md (derived a non-trainable SSM motivated from approximating a neuromorphic spiking model).

## [47]
Pete Warden. Speech commands: A dataset for limited-vocabulary speech recognition. *ArXiv*, abs/1804.03209, 2018.
- Cited in 04_experiments.md (Speech Commands dataset used for SC10 speech classification benchmark) and 10b_appendix-d3.5-d4-d5.md (D.5: originally a 35-class dataset of spoken English words).

## [48]
Max A Woodbury. Inverting modified matrices. *Memorandum report*, 42:106, 1950.
- Cited in 09c_appendix-c3-convolutional-view.md (Woodbury matrix identity, Proposition 4).

## [49]
Felix Wu, Angela Fan, Alexei Baevski, Yann N Dauphin, and Michael Auli. Pay less attention with lightweight and dynamic convolutions. In *The International Conference on Learning Representations (ICLR)*, 2019.
- Cited in 10a_appendix-d3-general-sequence-modeling.md (Dynamic Convolutions baseline for WikiText-103).

## [50]
Haoyi Zhou, Shanghang Zhang, Jieqi Peng, Shuai Zhang, Jianxin Li, Hui Xiong, and Wancai Zhang. Informer: Beyond efficient transformer for long sequence time-series forecasting. In *The Thirty-Fifth AAAI Conference on Artificial Intelligence, AAAI 2021, Virtual Conference*, volume 35, pages 11106-11115. AAAI Press, 2021.
- Cited in 04_experiments.md (specialized Transformer architecture for time-series forecasting; S4 outperforms Informer on 40/50 settings) and 10b_appendix-d3.5-d4-d5.md (D.3.5: Figure 5 comparing S4 vs. Informer architecture; Tables 13 and 14 with full forecasting results on all 50 settings).
