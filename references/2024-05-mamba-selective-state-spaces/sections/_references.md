# References

Only references cited in the section notes are listed below, with the paper's own citation format.

---

**Arjovsky, Shah, and Bengio 2016**
Martin Arjovsky, Amar Shah, and Yoshua Bengio. "Unitary Evolution Recurrent Neural Networks". In: *The International Conference on Machine Learning (ICML)*. 2016, pp. 1120–1128.
— Cited in 03a_motivation-selection-as-compression.md as the origin of the Copying task; in 09_appendix-b-related-work.md for orthogonal RNNs.

**Avsec et al. 2021**
Ziga Avsec, Vikram Agarwal, Daniel Visentin, Joseph R Ledsam, Agnieszka Grabska-Barwinska, Kyle R Taylor, Yannis Assael, John Jumper, Pushmeet Kohli, and David R Kelley. "Effective Gene Expression Prediction from Sequence by Integrating Long-range Interactions". In: *Nature Methods* 18.10 (2021), pp. 1196–1203.
— Cited in 04a_dna-modeling.md for DNA requiring long-range dependencies.

**Bahdanau, Cho, and Bengio 2015**
Dzmitry Bahdanau, Kyunghyun Cho, and Yoshua Bengio. "Neural Machine Translation by Jointly Learning to Align and Translate". In: *The International Conference on Learning Representations (ICLR)*. 2015.
— Cited in 01_introduction.md and 03c_efficient-implementation.md as the origin of the attention mechanism; in 08_appendix-a-selection-mechanism.md for selection vs. attention.

**J. L. Ba, Kiros, and Hinton 2016**
Jimmy Lei Ba, Jamie Ryan Kiros, and Geoffrey E Hinton. "Layer Normalization". In: *arXiv preprint arXiv:1607.06450* (2016).
— Cited in 03d_simplified-ssm-architecture.md for the optional LayerNorm; in 08_appendix-a-selection-mechanism.md as "J. Ba et al. 2016" for connections to fast weights.

**Balduzzi and Ghifary 2016**
Renato Balduzzi and Muhammad Ghifary. "Strongly-Typed Recurrent Neural Networks". In: *The International Conference on Machine Learning (ICML)*. 2016.
— Cited in 09_appendix-b-related-work.md as an older gated RNN without time-wise nonlinearities.

**Biderman et al. 2023**
Stella Biderman, Hailey Schoelkopf, Quentin Gregory Anthony, Herbie Bradley, Kyle O'Brien, Eric Hallahan, Mohammad Aflah Khan, Shivanshu Purohit, USVSN Sai Prashanth, Edward Raff, et al. "Pythia: A Suite for Analyzing Large Language Models across Training and Scaling". In: *The International Conference on Machine Learning (ICML)*. PMLR. 2023, pp. 2397–2430.
— Cited in 04_empirical-evaluation.md as the primary baseline (Pythia) trained on the same data.

**Blelloch 1990**
Guy E Blelloch. "Prefix Sums and Their Applications". In: (1990).
— Cited in 03c_efficient-implementation.md for the work-efficient parallel scan algorithm.

**Bradbury et al. 2016**
James Bradbury, Stephen Merity, Caiming Xiong, and Richard Socher. "Quasi-recurrent Neural Networks". In: *arXiv preprint arXiv:1611.01576* (2016).
— Cited in 02_state-space-models.md as a closely related method (QRNN); in 09_appendix-b-related-work.md for gated RNNs without time-wise nonlinearities.

**Brown et al. 2020**
Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. "Language Models are Few-shot Learners". In: *Advances in Neural Information Processing Systems (NeurIPS)* 33 (2020), pp. 1877–1901.
— Cited in 01_introduction.md, 04_empirical-evaluation.md, and 12_appendix-e-experimental-details.md for the GPT-3 training recipe and scaling law model sizes.

**Choromanski et al. 2021**
Krzysztof Choromanski, Valerii Likhosherstov, David Dohan, Xingyou Song, Andreea Gane, Tamas Sarlos, Peter Hawkins, Jared Davis, Afroz Mohiuddin, Lukasz Kaiser, David Belanger, Lucy Colwell, and Adrian Weller. "Rethinking Attention with Performers". In: *The International Conference on Learning Representations (ICLR)*. 2021.
— Cited in 09_appendix-b-related-work.md for the Performer approximation to exponential kernel attention.

**Chowdhery et al. 2023**
Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung, Charles Sutton, Sebastian Gehrmann, et al. "PaLM: Scaling Language Modeling with Pathways". In: *Journal of Machine Learning Research* 24.240 (2023), pp. 1–113.
— Cited in 03d_simplified-ssm-architecture.md and 12_appendix-e-experimental-details.md for the SwiGLU variant and improved training recipe.

**J. Chung et al. 2014**
Junyoung Chung, Caglar Gulcehre, KyungHyun Cho, and Yoshua Bengio. "Empirical Evaluation of Gated Recurrent Neural Networks on Sequence Modeling". In: *arXiv preprint arXiv:1412.3555* (2014).
— Cited in 08_appendix-a-selection-mechanism.md for the GRU gating mechanism.

**Dao 2024**
Tri Dao. "FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning". In: *The International Conference on Learning Representations (ICLR)*. 2024.
— Cited in 04c_speed-memory-benchmarks.md as the best attention implementation (FlashAttention-2).

**Dao, Fu, Ermon, et al. 2022**
Tri Dao, Daniel Y Fu, Stefano Ermon, Atri Rudra, and Christopher Re. "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness". In: *Advances in Neural Information Processing Systems (NeurIPS)*. 2022.
— Cited in 03c_efficient-implementation.md and 11_appendix-d-hardware-aware-algorithm.md for memory bandwidth being the bottleneck.

**Dao, Fu, Saab, et al. 2023**
Tri Dao, Daniel Y Fu, Khaled K Saab, Armin W Thomas, Atri Rudra, and Christopher Re. "Hungry Hungry Hippos: Towards Language Modeling with State Space Models". In: *The International Conference on Learning Representations (ICLR)*. 2023.
— Cited in 01_introduction.md, 02_state-space-models.md, 03d_simplified-ssm-architecture.md, 04_empirical-evaluation.md, 09_appendix-b-related-work.md, 11_appendix-d-hardware-aware-algorithm.md, and 12_appendix-e-experimental-details.md as the H3 architecture.

**Dauphin et al. 2017**
Yann N Dauphin, Angela Fan, Michael Auli, and David Grangier. "Language Modeling with Gated Convolutional Networks". In: *The International Conference on Machine Learning (ICML)*. PMLR. 2017, pp. 933–941.
— Cited in 03d_simplified-ssm-architecture.md for the SwiGLU variant; in 08_appendix-a-selection-mechanism.md for GLU as an activation function.

**DeepSound 2017**
DeepSound. *SampleRNN*. https://github.com/deepsound-project/samplernn-pytorch. 2017.
— Cited in 04b_audio-modeling.md as the YouTubeMix dataset source.

**Donahue, McAuley, and Puckette 2019**
Chris Donahue, Julian McAuley, and Miller Puckette. "Adversarial Audio Synthesis". In: *The International Conference on Learning Representations (ICLR)*. 2019.
— Cited in 04b_audio-modeling.md as the SC09 dataset and WaveGAN baseline.

**Dosovitskiy et al. 2020**
Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, et al. "An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale". In: *The International Conference on Learning Representations (ICLR)*. 2020.
— Cited in 01_introduction.md for the breadth of FM domains (vision).

**Elhage et al. 2021**
Nelson Elhage, Neel Nanda, Catherine Olsson, Tom Henighan, Nicholas Joseph, Ben Mann, Amanda Askell, Yuntao Bai, Anna Chen, Tom Conerly, Nova DasSarma, Dawn Drain, Deep Ganguli, Zac Hatfield-Dodds, Danny Hernandez, Andy Jones, Jackson Kernion, Liane Lovitt, Kamal Ndousse, Dario Amodei, Tom Brown, Jack Clark, Jared Kaplan, Sam McCandlish, and Chris Olah. "A Mathematical Framework for Transformer Circuits". In: *Transformer Circuits Thread* (2021). https://transformer-circuits.pub/2021/framework/index.html.
— Cited in 04_empirical-evaluation.md for the mechanistic interpretability lens on induction heads.

**Friston, Harrison, and Penny 2003**
Karl J Friston, Lee Harrison, and Will Penny. "Dynamic Causal Modelling". In: *Neuroimage* 19.4 (2003), pp. 1273–1302.
— Cited in 02_state-space-models.md for the general state space model concept (computational neuroscience).

**Fu et al. 2023**
Daniel Y Fu, Elliot L Epstein, Eric Nguyen, Armin W Thomas, Michael Zhang, Tri Dao, Atri Rudra, and Christopher Re. "Simple Hardware-Efficient Long Convolutions for Sequence Modeling". In: *The International Conference on Machine Learning (ICML)*. 2023.
— Cited in 09_appendix-b-related-work.md as LongConv, focusing on the convolutional representation of S4.

**Funahashi and Nakamura 1993**
Ken-ichi Funahashi and Yuichi Nakamura. "Approximation of Dynamical Systems by Continuous Time Recurrent Neural Networks". In: *Neural Networks* 6.6 (1993), pp. 801–806.
— Cited in 03e_properties-of-selection-mechanisms.md and 08_appendix-a-selection-mechanism.md for the connection between RNN gating and discretization.

**L. Gao, Biderman, et al. 2020**
Leo Gao, Stella Biderman, Sid Black, Laurence Golding, Travis Hoppe, Charles Foster, Jason Phang, Horace He, Anish Thite, Noa Nabeshima, Shivanshu Presser, and Connor Leahy. "The Pile: An 800GB Dataset of Diverse Text for Language Modeling". In: *arXiv preprint arXiv:2101.00027* (2020).
— Cited in 04_empirical-evaluation.md as the Pile dataset.

**Goel et al. 2022**
Karan Goel, Albert Gu, Chris Donahue, and Christopher Re. "It's Raw! Audio Generation with State-Space Models". In: *The International Conference on Machine Learning (ICML)*. 2022.
— Cited in 01_introduction.md and 04b_audio-modeling.md as SaShiMi architecture for audio.

**Gu, Dao, et al. 2020**
Albert Gu, Tri Dao, Stefano Ermon, Atri Rudra, and Christopher Re. "HIPPO: Recurrent Memory with Optimal Polynomial Projections". In: *Advances in Neural Information Processing Systems (NeurIPS)*. 2020.
— Cited in 01_introduction.md, 02_state-space-models.md, 03c_efficient-implementation.md, 03f_additional-model-details.md, 08_appendix-a-selection-mechanism.md, and 09_appendix-b-related-work.md for the HIPPO theory and early time-varying SSMs.

**Gu, Goel, and Re 2022**
Albert Gu, Karan Goel, and Christopher Re. "Efficiently Modeling Long Sequences with Structured State Spaces". In: *The International Conference on Learning Representations (ICLR)*. 2022.
— Cited throughout (01_introduction.md, 02_state-space-models.md, 03c_efficient-implementation.md, 03f_additional-model-details.md, 04d_model-ablations.md, 09_appendix-b-related-work.md, 11_appendix-d-hardware-aware-algorithm.md) as the S4 model.

**Gu, Gulcehre, et al. 2020**
Albert Gu, Caglar Gulcehre, Tom Le Paine, Matt Hoffman, and Razvan Pascanu. "Improving the Gating Mechanism of Recurrent Neural Networks". In: *The International Conference on Machine Learning (ICML)*. 2020.
— Cited in 02_state-space-models.md for connections between discretization and RNN gating.

**Gu, Gupta, et al. 2022**
Albert Gu, Ankit Gupta, Karan Goel, and Christopher Re. "On the Parameterization and Initialization of Diagonal State Space Models". In: *Advances in Neural Information Processing Systems (NeurIPS)*. 2022.
— Cited in 01_introduction.md, 02_state-space-models.md, 03f_additional-model-details.md, 04d_model-ablations.md, and 09_appendix-b-related-work.md for diagonal SSM parameterization (S4D-Lin, S4D-Real).

**Gu, Johnson, Goel, et al. 2021**
Albert Gu, Isys Johnson, Karan Goel, Khaled Saab, Tri Dao, Atri Rudra, and Christopher Re. "Combining Recurrent, Convolutional, and Continuous-time Models with the Linear State Space Layer". In: *Advances in Neural Information Processing Systems (NeurIPS)*. 2021.
— Cited in 01_introduction.md, 03c_efficient-implementation.md, 03e_properties-of-selection-mechanisms.md, and 09_appendix-b-related-work.md for the LSSL model.

**Gu, Johnson, Timalsina, et al. 2023**
Albert Gu, Isys Johnson, Aman Timalsina, Atri Rudra, and Christopher Re. "How to Train Your HIPPO: State Space Models with Generalized Basis Projections". In: *The International Conference on Learning Representations (ICLR)*. 2023.
— Cited in 02_state-space-models.md, 03f_additional-model-details.md, and 09_appendix-b-related-work.md for initialization and normalization.

**Gupta, Gu, and Berant 2022**
Ankit Gupta, Albert Gu, and Jonathan Berant. "Diagonal State Spaces are as Effective as Structured State Spaces". In: *Advances in Neural Information Processing Systems* 35 (2022), pp. 22982–22994.
— Cited in 01_introduction.md, 02_state-space-models.md, and 09_appendix-b-related-work.md for diagonal SSMs (DSS).

**Gupta, Mehta, and Berant 2022**
Ankit Gupta, Harsh Mehta, and Jonathan Berant. Direct analysis of recurrent dynamics in structured state spaces (2022). Full bibliographic entry is in earlier bibliography pages.
— Cited in 09_appendix-b-related-work.md for direct analysis of recurrent dynamics in SSMs.

**Ha, Dai, and Quoc V. Le 2017**
David Ha, Andrew Dai, and Quoc V. Le. "HyperNetworks". In: *The International Conference on Learning Representations (ICLR)*. 2017.
— Cited in 08_appendix-a-selection-mechanism.md for the original hypernetworks idea (a large RNN whose recurrent parameters are generated by a smaller RNN).

**Hafner et al. 2020**
Danijar Hafner, Timothy Lillicrap, Jimmy Ba, and Mohammad Norouzi. "Dream to Control: Learning Behaviors by Latent Imagination". In: *The International Conference on Learning Representations (ICLR)*. 2020.
— Cited in 02_state-space-models.md for MDP/RL usage of state space models.

**Hasani et al. 2023**
Ramin Hasani, Mathias Lechner, Tsun-Hsuan Wang, Makram Chahine, Alexander Amini, and Daniela Rus. "Liquid Structural State-Space Models". In: *The International Conference on Learning Representations (ICLR)*. 2023.
— Cited in 02_state-space-models.md and 09_appendix-b-related-work.md as Liquid S4, an input-dependent state transition SSM variant.

**Henaff, Szlam, and LeCun 2016**
Mikael Henaff, Arthur Szlam, and Yann LeCun. "Recurrent Orthogonal Networks and Long-Memory Tasks". In: *The International Conference on Machine Learning (ICML)*. 2016.
— Cited in 09_appendix-b-related-work.md for orthogonal RNNs.

**Hendrycks and Gimpel 2016**
Dan Hendrycks and Kevin Gimpel. "Gaussian Error Linear Units (GELUs)". In: *arXiv preprint arXiv:1606.08415* (2016).
— Cited in 03d_simplified-ssm-architecture.md for the SiLU / Swish activation function.

**Hochreiter 1991**
Sepp Hochreiter. "Untersuchungen zu dynamischen neuronalen Netzen". Diploma thesis. Technische Universitat Munchen. 1991.
— Cited in 09_appendix-b-related-work.md for the vanishing gradients problem.

**Hochreiter and Schmidhuber 1997**
Sepp Hochreiter and Jurgen Schmidhuber. "Long Short-Term Memory". In: *Neural Computation* 9.8 (1997), pp. 1735–1780.
— Cited in 08_appendix-a-selection-mechanism.md for the LSTM gating mechanism.

**Hochreiter, Bengio, et al. 2001**
Sepp Hochreiter, Yoshua Bengio, Simone Frasconi, and Jurgen Schmidhuber. "Gradient Flow in Recurrent Nets: The Difficulty of Learning Long-Term Dependencies". In: *A Field Guide to Dynamical Recurrent Networks*. IEEE Press. 2001.
— Cited in 09_appendix-b-related-work.md for the vanishing gradients problem.

**Hoffmann et al. 2022**
Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, et al. "An Empirical Analysis of Compute-Optimal Large Language Model Training". In: *Advances in Neural Information Processing Systems* 35 (2022), pp. 30016–30030.
— Cited in 04_empirical-evaluation.md and 12_appendix-e-experimental-details.md for the Chinchilla scaling protocol.

**Hua et al. 2022**
Weizhe Hua, Zihang Dai, Hanxiao Liu, and Quoc Le. "Transformer Quality in Linear Time". In: *The International Conference on Machine Learning (ICML)*. PMLR. 2022, pp. 9099–9117.
— Cited in 03d_simplified-ssm-architecture.md for the gated attention unit (GAU) inspiration; in 08_appendix-a-selection-mechanism.md and 09_appendix-b-related-work.md for elementwise multiplicative gating and the GAU architecture.

**Ismail Fawaz et al. 2019**
Hassan Ismail Fawaz, Germain Forestier, Jonathan Weber, Lhassane Idoumghar, and Pierre-Alain Muller. "Deep Learning for Time Series Classification: A Review". In: *Data Mining and Knowledge Discovery* 33.4 (2019), pp. 917–963.
— Cited in 01_introduction.md for the breadth of FM domains (time series).

**Ivanov et al. 2021**
Andrei Ivanov, Nikoli Dryden, Tal Ben-Nun, Shigang Li, and Torsten Hoefler. "Data Movement is All You Need: A Case Study on Optimizing Transformers". In: *Proceedings of Machine Learning and Systems* 3 (2021), pp. 711–732.
— Cited in 03c_efficient-implementation.md and 11_appendix-d-hardware-aware-algorithm.md for memory bandwidth being the bottleneck.

**Jing et al. 2019**
Li Jing, Caglar Gulcehre, John Peurifoy, Yichen Shen, Max Tegmark, Marin Soljacic, and Yoshua Bengio. "Gated Orthogonal Recurrent Units: On Learning to Forget". In: *Neural Computation* 31.4 (2019), pp. 765–783.
— Cited in 04_empirical-evaluation.md for the Denoising task (equivalent to Selective Copying); in 09_appendix-b-related-work.md for orthogonal RNNs struggling on the Selective Copying task.

**Kalman 1960**
Rudolph Emil Kalman. "A New Approach to Linear Filtering and Prediction Problems". In: (1960).
— Cited in 01_introduction.md and 02_state-space-models.md for classical state space models.

**Katharopoulos et al. 2020**
Angelos Katharopoulos, Apoorv Vyas, Nikolaos Pappas, and Francois Fleuret. "Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention". In: *International Conference on Machine Learning*. PMLR. 2020, pp. 5156–5165.
— Cited in 02_state-space-models.md for linear attention as a degenerate linear SSM; in 09_appendix-b-related-work.md for the Linear Attention framework.

**Kaul 2020**
Ankit Kaul. "Linear Dynamical Systems as a Core Computational Primitive". In: *Advances in Neural Information Processing Systems (NeurIPS)*. 2020.
— Cited in 09_appendix-b-related-work.md for direct analysis of recurrent dynamics in SSMs.

**Z. Kong et al. 2021**
Zhifeng Kong, Wei Ping, Jiaji Huang, Kexin Zhao, and Bryan Catanzaro. "DiffWave: A Versatile Diffusion Model for Audio Synthesis". In: *International Conference on Learning Representations*. 2021.
— Cited in 04b_audio-modeling.md as a DiffWave baseline.

**Kosma, Nikolentzos, and Vazirgiannis 2023**
Vasileios Kosma, Giannis Nikolentzos, and Michalis Vazirgiannis. Input-dependent convolutions work (2023).
— Cited in 08_appendix-a-selection-mechanism.md as an example of input-dependent convolutions beyond selective SSMs.

**Krizhevsky, Sutskever, and Hinton 2012**
Alex Krizhevsky, Ilya Sutskever, and Geoffrey E Hinton. "ImageNet Classification with Deep Convolutional Neural Networks". In: *Advances in Neural Information Processing Systems (NeurIPS)* 25 (2012).
— Cited in 03c_efficient-implementation.md for convolutions as hardware-friendly primitives.

**Lei 2021**
Tao Lei. "When Attention Meets Fast Recurrence: Training Language Models with Reduced Compute". In: *Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP)*. 2021.
— Cited in 09_appendix-b-related-work.md for the SRU (simple recurrent unit) as a gated RNN variant.

**Lei et al. 2017**
Tao Lei, Yu Zhang, Sida I Wang, Hui Dai, and Yoav Artzi. "Simple Recurrent Units for Highly Parallelizable Recurrence". In: *arXiv preprint arXiv:1709.02755* (2017).
— Cited in 02_state-space-models.md as a closely related method (SRU); in 09_appendix-b-related-work.md for gated RNNs without time-wise nonlinearities.

**Lezcano-Casado and Martinez-Rubio 2019**
Mario Lezcano-Casado and David Martinez-Rubio. "Cheap Orthogonal Constraints in Neural Networks: A Simple Parametrization of the Orthogonal and Unitary Group". In: *The International Conference on Machine Learning (ICML)*. 2019.
— Cited in 09_appendix-b-related-work.md for orthogonal RNNs.

**Y. Li et al. 2023**
Yuhong Li, Tianle Cai, Yi Zhang, Deming Chen, and Debadeepta Dey. "What Makes Convolutional Models Great on Long Sequence Modeling?" In: *The International Conference on Learning Representations (ICLR)*. 2023.
— Cited in 01_introduction.md, 02_state-space-models.md, and 09_appendix-b-related-work.md as SGConv, focusing on the convolutional representation of S4.

**Lioutas and Guo 2020**
Vasileios Lioutas and Yuhong Guo. "Time-aware Large Kernel Convolutions". In: *The International Conference on Machine Learning (ICML)*. 2020.
— Cited in 08_appendix-a-selection-mechanism.md as an example of input-dependent convolutions.

**Lu et al. 2023**
Chris Lu, Yannick Schroecker, Albert Gu, Emilio Parisotto, Jakob Foerster, Satinder Singh, and Feryal Behbahani. "Structured State Space Models for In-Context Reinforcement Learning". In: *Advances in Neural Information Processing Systems (NeurIPS)*. 2023.
— Cited in 03e_properties-of-selection-mechanisms.md for episode boundaries in RL; in 09_appendix-b-related-work.md for applying S5 to meta-RL with a hard-coded selection mechanism.

**Lutati, Zimerman, and Wolf 2023**
Shahar Lutati, Itamar Zimerman, and Lior Wolf. Input-dependent convolutions work (2023).
— Cited in 08_appendix-a-selection-mechanism.md as an example of input-dependent convolutions beyond selective SSMs.

**Ma et al. 2023**
Xuezhe Ma, Chunting Zhou, Xiang Kong, Junxian He, Liangke Gui, Graham Neubig, Jonathan May, and Luke Zettlemoyer. "Mega: Moving Average Equipped Gated Attention". In: *The International Conference on Learning Representations (ICLR)*. 2023.
— Cited in 01_introduction.md, 02_state-space-models.md, 03f_additional-model-details.md, 08_appendix-a-selection-mechanism.md, and 09_appendix-b-related-work.md as an SSM variant (EMA simplification of S4).

**Martin and Cundy 2018**
Eric Martin and Chris Cundy. "Parallelizing Linear Recurrent Neural Nets Over Sequence Length". In: *The International Conference on Learning Representations (ICLR)*. 2018.
— Cited in 03c_efficient-implementation.md for the parallel scan algorithm; in 09_appendix-b-related-work.md for parallelizing older RNNs.

**Mehri et al. 2017**
Soroush Mehri, Kundan Kumar, Ishaan Gulrajani, Rithesh Kumar, Shubham Jain, Jose Sotelo, Aaron Courville, and Yoshua Bengio. "SampleRNN: An Unconditional End-to-End Neural Audio Generation Model". In: *The International Conference on Learning Representations (ICLR)*. 2017.
— Cited in 04b_audio-modeling.md as a SampleRNN baseline.

**Mehta et al. 2023**
Harsh Mehta, Ankit Gupta, Ashok Cutkosky, and Behnam Neyshabur. "Long Range Language Modeling via Gated State Spaces". In: *The International Conference on Learning Representations (ICLR)*. 2023.
— Cited in 04d_model-ablations.md for findings on random initializations; in 08_appendix-a-selection-mechanism.md for elementwise multiplicative gating; in 09_appendix-b-related-work.md as GSS, the first gated neural network architecture incorporating SSMs.

**Mhammedi et al. 2017**
Zakaria Mhammedi, Andrew Hellicar, Ashfaqur Rahman, and James Bailey. "Efficient Orthogonal Parametrisation of Recurrent Neural Networks using Householder Reflections". In: *International Conference on Machine Learning*. PMLR. 2017, pp. 2401–2409.
— Cited in 09_appendix-b-related-work.md for orthogonal RNNs.

**Nguyen, Goel, et al. 2022**
Eric Nguyen, Karan Goel, Albert Gu, Gordon Downs, Preey Shah, Tri Dao, Stephen Baccus, and Christopher Re. "S4ND: Modeling Images and Videos as Multidimensional Signals with State Space Models". In: *Advances in Neural Information Processing Systems (NeurIPS)*. 2022.
— Cited in 01_introduction.md and 02_state-space-models.md for SSMs on vision and resolution invariance.

**Nguyen, Poli, et al. 2023**
Eric Nguyen, Michael Poli, Marjan Faizi, Armin Thomas, Callum Birch-Sykes, Michael Wornow, Aman Patel, Clayton Rabideau, Stefano Massaroli, and Yoshua Bengio, et al. "HyenaDNA: Long-range Genomic Sequence Modeling at Single Nucleotide Resolution". In: *Advances in Neural Information Processing Systems (NeurIPS)*. 2023.
— Cited in 04a_dna-modeling.md as the primary DNA baseline (HyenaDNA); in 09_appendix-b-related-work.md for long context claims up to 1M.

**Olsson et al. 2022**
Catherine Olsson, Nelson Elhage, Neel Nanda, Nicholas Joseph, Nova DasSarma, Tom Henighan, Ben Mann, Amanda Askell, Yuntao Bai, Anna Chen, Tom Conerly, Dawn Drain, Deep Ganguli, Zac Hatfield-Dodds, Danny Hernandez, Scott Johnston, Andy Jones, Jackson Kernion, Liane Lovitt, Kamal Ndousse, Dario Amodei, Tom Brown, Jack Clark, Jared Kaplan, Sam McCandlish, and Chris Olah. "In-context Learning and Induction Heads". In: *Transformer Circuits Thread* (2022). https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html.
— Cited in 03a_motivation-selection-as-compression.md and 04_empirical-evaluation.md for the induction heads mechanism.

**Oord et al. 2016**
Aaron van den Oord, Sander Dieleman, Heiga Zen, Karen Simonyan, Oriol Vinyals, Alex Graves, Nal Kalchbrenner, Andrew Senior, and Koray Kavukcuoglu. "WaveNet: A Generative Model for Raw Audio". In: *arXiv preprint arXiv:1609.03499* (2016).
— Cited in 01_introduction.md and 04b_audio-modeling.md for the WaveNet baseline.

**Orvieto et al. 2023**
Antonio Orvieto, Samuel L Smith, Albert Gu, Anushan Fernando, Caglar Gulcehre, Razvan Pascanu, and Soham De. "Resurrecting Recurrent Neural Networks for Long Sequences". In: *The International Conference on Machine Learning (ICML)*. 2023.
— Cited in 01_introduction.md, 02_state-space-models.md, and 09_appendix-b-related-work.md as an SSM variant and for direct analysis of recurrent dynamics.

**Pascanu, Mikolov, and Bengio 2013**
Razvan Pascanu, Tomas Mikolov, and Yoshua Bengio. "On the Difficulty of Training Recurrent Neural Networks". In: *International Conference on Machine Learning*. 2013, pp. 1310–1318.
— Cited in 09_appendix-b-related-work.md for the vanishing gradients problem.

**B. Peng et al. 2023**
Bo Peng, Eric Alcaide, Quentin Anthony, Alon Albalak, Samuel Arcadinho, Huanqi Cao, Xin Cheng, Michael Chung, Matteo Grella, Kranthi Kiran GV, et al. "RWKV: Reinventing RNNs for the Transformer Era". In: *arXiv preprint arXiv:2305.13048* (2023).
— Cited in 02_state-space-models.md, 04_empirical-evaluation.md, 05_discussion.md, 09_appendix-b-related-work.md, and 12_appendix-e-experimental-details.md for the RWKV model.

**H. Peng et al. 2021**
Hao Peng, Nikolaos Pappas, Dani Yogatama, Roy Schwartz, Noah A Smith, and Lingpeng Kong. "Random Feature Attention". In: *The International Conference on Learning Representations (ICLR)*. 2021.
— Cited in 09_appendix-b-related-work.md for Random Feature Attention (RFA), using random Fourier features to approximate softmax attention.

**Poli et al. 2023**
Michael Poli, Stefano Massaroli, Eric Nguyen, Daniel Y Fu, Tri Dao, Stephen Baccus, Yoshua Bengio, Stefano Ermon, and Christopher Re. "Hyena Hierarchy: Towards Larger Convolutional Language Models". In: *The International Conference on Machine Learning (ICML)*. 2023.
— Cited in 01_introduction.md, 02_state-space-models.md, 04_empirical-evaluation.md, 08_appendix-a-selection-mechanism.md, and 09_appendix-b-related-work.md for the Hyena architecture and long context claims.

**Qin, Han, W. Sun, B. He, et al. 2023**
Zhen Qin, Xiaodong Han, Weixuan Sun, Bowen He, Dong Li, Dongxu Li, Yuchao Dai, Lingpeng Kong, and Yiran Zhong. "Toeplitz Neural Network for Sequence Modeling". In: *The International Conference on Learning Representations (ICLR)*. 2023.
— Cited in 09_appendix-b-related-work.md for Toeplitz Neural Network, focusing on the convolutional representation of S4.

**Rahimi and Recht 2007**
Ali Rahimi and Benjamin Recht. "Random Features for Large-Scale Kernel Machines". In: *Advances in Neural Information Processing Systems (NeurIPS)* 20 (2007).
— Cited in 09_appendix-b-related-work.md for the random Fourier feature approximation of Gaussian kernels used in RFA.

**Ramachandran, Zoph, and Quoc V Le 2017**
Prajit Ramachandran, Barret Zoph, and Quoc V Le. "Swish: A Self-gated Activation Function". In: *arXiv preprint arXiv:1710.05941* 7.1 (2017), p. 5.
— Cited in 03d_simplified-ssm-architecture.md for the SiLU / Swish activation function.

**Romero et al. 2021**
David W Romero, Anna Kuzina, Erik J Bekkers, Jakub M Tomczak, and Mark Hoogendoorn. "CKConv: Continuous Kernel Convolution For Sequential Data". In: *arXiv preprint arXiv:2102.02611* (2021).
— Cited in 02_state-space-models.md, 03a_motivation-selection-as-compression.md, and 04_empirical-evaluation.md for MLP-parameterized global convolutions solving the vanilla Copying task.

**Saon, Gupta, and Cui 2023**
George Saon, Ankit Gupta, and Xiaodong Cui. "Diagonal State Space Augmented Transformers for Speech Recognition". In: *ICASSP 2023-2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*. IEEE. 2023, pp. 1–5.
— Cited in 01_introduction.md for SSMs on continuous signal data (speech); in 12_appendix-e-experimental-details.md for combining LTI SSMs with Attention.

**Schlag, Irie, and Schmidhuber 2021**
Imanol Schlag, Kazuki Irie, and Jurgen Schmidhuber. "Linear Transformers are Secretly Fast Weight Programmers". In: *The International Conference on Machine Learning (ICML)*. PMLR. 2021, pp. 9355–9366.
— Cited in 08_appendix-a-selection-mechanism.md for connecting classical RNNs with the mechanism of linear attention via fast weights.

**Schmidhuber 1992**
Jurgen Schmidhuber. "Learning to control fast-weight memories: An alternative to dynamic recurrent networks". In: *Neural Computation* 4.1 (1992), pp. 131–139.
— Cited in 08_appendix-a-selection-mechanism.md for fast weights and hypernetwork variants.

**Shazeer 2020**
Noam Shazeer. "GLU Variants Improve Transformer". In: *arXiv preprint arXiv:2002.05202* (2020).
— Cited in 03d_simplified-ssm-architecture.md, 12_appendix-e-experimental-details.md for the SwiGLU variant; in 08_appendix-a-selection-mechanism.md for GLU as an activation function.

**F. Shi et al. 2023**
Freda Shi, Xinyun Chen, Kanishka Misra, Nathan Scales, David Dohan, Ed H Chi, Nathanael Scharli, and Denny Zhou. "Large Language Models can be Easily Distracted by Irrelevant Context". In: *The International Conference on Machine Learning (ICML)*. PMLR. 2023, pp. 31210–31227.
— Cited in 03e_properties-of-selection-mechanisms.md for the observation that many sequence models do not improve with longer context.

**J. Shi, K. A. Wang, and Fox 2023**
Jiaxin Shi, Ke Alexander Wang, and Emily Fox. "Sequence Modeling with Multiresolution Convolutional Memory". In: *The International Conference on Machine Learning (ICML)*. PMLR. 2023, pp. 31312–31327.
— Cited in 09_appendix-b-related-work.md as MultiresConv, focusing on the convolutional representation of S4.

**Smith, Warrington, and Linderman 2023**
Jimmy T.H. Smith, Andrew Warrington, and Scott Linderman. "Simplified State Space Layers for Sequence Modeling". In: *The International Conference on Learning Representations (ICLR)*. 2023.
— Cited in 01_introduction.md, 02_state-space-models.md, 03c_efficient-implementation.md, and 09_appendix-b-related-work.md as S5 model and parallel scan.

**Y. Sun et al. 2023**
Yutao Sun, Li Dong, Shaohan Huang, Shuming Ma, Yuqing Xia, Jilong Xue, Jianyong Wang, and Furu Wei. "Retentive network: A successor to transformer for large language models". In: *arXiv preprint arXiv:2307.08621* (2023).
— Cited in 02_state-space-models.md, 03d_simplified-ssm-architecture.md, 05_discussion.md, 09_appendix-b-related-work.md, and 12_appendix-e-experimental-details.md for the RetNet architecture.

**Sutskever, Vinyals, and Quoc V Le 2014**
Ilya Sutskever, Oriol Vinyals, and Quoc V Le. "Sequence to Sequence Learning with Neural Networks". In: *Advances in Neural Information Processing Systems (NeurIPS)* 27 (2014).
— Cited in 01_introduction.md for the breadth of FM domains.

**Tallec and Ollivier 2018**
Corentin Tallec and Yann Ollivier. "Can Recurrent Neural Networks Warp Time?" In: *The International Conference on Learning Representations (ICLR)*. 2018.
— Cited in 02_state-space-models.md, 03e_properties-of-selection-mechanisms.md, and 08_appendix-a-selection-mechanism.md for connections between discretization and RNN gating.

**Tay, Dehghani, Abnar, et al. 2021**
Yi Tay, Mostafa Dehghani, Samira Abnar, et al. "Long Range Arena: A Benchmark for Efficient Transformers". In: *International Conference on Learning Representations (ICLR)*. 2021.
— Cited in 01_introduction.md for the Long Range Arena benchmark.

**Tay, Dehghani, Bahri, et al. 2022**
Yi Tay, Mostafa Dehghani, Dara Bahri, and Donald Metzler. "Efficient Transformers: A Survey". In: *ACM Computing Surveys* 55.6 (2022), pp. 1–28.
— Cited in 01_introduction.md and 09_appendix-b-related-work.md for the survey of efficient attention variants.

**Touvron et al. 2023**
Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothee Lacroix, Baptiste Roziere, Naman Goyal, Eric Hambro, Faisal Azhar, et al. "Llama: Open and Efficient Foundation Language Models". In: *arXiv preprint arXiv:2302.13971* (2023).
— Cited in 01_introduction.md, 03d_simplified-ssm-architecture.md, 04_empirical-evaluation.md, 05_discussion.md, and 12_appendix-e-experimental-details.md for the LLaMA recipe and training baselines.

**Vaswani et al. 2017**
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and Illia Polosukhin. "Attention Is All You Need". In: *Advances in Neural Information Processing Systems (NeurIPS)*. 2017.
— Cited in 01_introduction.md, 03c_efficient-implementation.md, and 08_appendix-a-selection-mechanism.md for the Transformer architecture.

**Vorontsov et al. 2017**
Eugene Vorontsov, Chiheb Trabelsi, Samuel Kadoury, and Chris Pal. "On Orthogonality and Learning Recurrent Networks with Long Term Dependencies". In: *International Conference on Machine Learning*. PMLR. 2017, pp. 3570–3578.
— Cited in 09_appendix-b-related-work.md for orthogonal RNNs.

**J. Wang et al. 2023**
Jue Wang, Wentao Zhu, Pichao Wang, Xiang Yu, Linda Liu, Mohamed Omar, and Raffay Hamid. "Selective Structured State-Spaces for Long-form Video Understanding". In: *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*. 2023, pp. 6387–6397.
— Cited in 09_appendix-b-related-work.md as Selective S4, which uses S4 to generate a binary mask (an architectural modification rather than a true selection mechanism).

**Warden 2018**
Pete Warden. "Speech Commands: A Dataset for Limited-Vocabulary Speech Recognition". In: *ArXiv* abs/1804.03209 (2018).
— Cited in 04b_audio-modeling.md for the SC09 dataset.

**Williams, Waterman, and Patterson 2009**
Samuel Williams, Andrew Waterman, and David Patterson. "Roofline: An Insightful Visual Performance Model for Multicore Architectures". In: *Communications of the ACM* 52.4 (2009), pp. 65–76.
— Cited in 03c_efficient-implementation.md and 11_appendix-d-hardware-aware-algorithm.md for memory bandwidth being the bottleneck on modern hardware.

**Yang et al. 2019**
Brandon Yang, Gabriel Bender, Quoc V Le, and Jiquan Ngiam. "CondConv: Conditionally Parameterized Convolutions for Efficient Inference". In: *Advances in Neural Information Processing Systems (NeurIPS)* 32 (2019).
— Cited in 08_appendix-a-selection-mechanism.md as an example of input-dependent convolutions.

**S. Zhai et al. 2021**
Shuangfei Zhai, Walter Talbott, Nitish Srivastava, Chen Huang, Hanlin Goh, Ruixiang Zhang, and Josh Susskind. "An Attention Free Transformer". In: *arXiv preprint arXiv:2105.14103* (2021).
— Cited in 02_state-space-models.md and 09_appendix-b-related-work.md for the attention-free Transformer (AFT) underlying RWKV.

**Zhang et al. 2023**
Michael Zhang, Khaled K Saab, Michael Poli, Tri Dao, Karan Goel, and Christopher Re. "Effectively Modeling Time Series with Simple Discrete State Spaces". In: *The International Conference on Learning Representations (ICLR)*. 2023.
— Cited in 02_state-space-models.md for alternate SSM flavors that bypass discretization and parameterize discrete parameters directly.

**Black et al. 2022**
Sid Black, Stella Biderman, Eric Hallahan, Quentin Anthony, Leo Gao, Laurence Golding, Horace He, Connor Leahy, Kyle McDonell, Jason Phang, Michael Pieler, USVSN Sai Prashanth, Shivanshu Purohit, Laria Reynolds, Jonathan Tow, Ben Wang, and Samuel Weinbach. "GPT-NeoX-20B: An Open-Source Autoregressive Language Model". In: *Proceedings of the ACL Workshop on Challenges & Perspectives in Creating Large Language Models*. 2022.
— Cited in 12_appendix-e-experimental-details.md for the GPT-NeoX tokenizer used in downstream evaluation pretraining.

**Bulatov, Kuratov, and Burtsev 2023**
Aydar Bulatov, Yuri Kuratov, and Mikhail Burtsev. "Scaling Transformer to 1M tokens and beyond with RMT". In: *arXiv preprint* (2023).
— Cited in 09_appendix-b-related-work.md as the Recurrent Memory Transformer, a lightweight wrapper around a Transformer backbone that generalized to 1M sequences on synthetic memorization tasks.

**Child et al. 2019**
Rewon Child, Scott Gray, Alec Radford, and Ilya Sutskever. "Generating Long Sequences with Sparse Transformers". In: *arXiv preprint arXiv:1904.10509* (2019).
— Cited in 09_appendix-b-related-work.md for Sparse Transformer, showing proof-of-concept on audio waveforms of length $2^{20}$.

**Ding et al. 2023**
Jiayu Ding, Shuming Ma, Li Dong, Xingxing Zhang, Shaohan Huang, Wenhui Wang, and Furu Wei. "LongNet: Scaling Transformers to 1,000,000,000 Tokens". In: *arXiv preprint* (2023).
— Cited in 09_appendix-b-related-work.md as LongNet, which claimed to scale to 1B length but only evaluated on length < 100K for actual tasks.

**Fathi et al. 2023**
Fathi et al. (2023). Full bibliographic details not available in this window.
— Cited in 12_appendix-e-experimental-details.md for combining LTI SSMs with Attention leading to substantial improvements.

**Fathullah et al. 2023**
Fathullah et al. (2023). Full bibliographic details not available in this window.
— Cited in 12_appendix-e-experimental-details.md for combining LTI SSMs with Attention leading to substantial improvements.

**L. Gao, Tow, et al. 2021**
Leo Gao, Jonathan Tow, Stella Biderman, Sid Black, Anthony DiPofi, Charles Foster, Laurence Golding, Jeffrey Hsu, Kyle McDonell, Niklas Muennighoff, Jason Phang, Laria Reynolds, Eric Tang, Anish Thite, Ben Wang, Kevin Wang, and Andy Zou. "A Framework for Few-shot Language Model Evaluation". In: Zenodo (2021). https://doi.org/10.5281/zenodo.5371628.
— Cited in 12_appendix-e-experimental-details.md for the LM evaluation harness from EleutherAI used for downstream evaluation.

**Paperno et al. 2016**
Denis Paperno, German Kruszewski, Angeliki Lazaridou, Ngoc Quan Pham, Raffaella Bernardi, Sandro Pezzelle, Marco Baroni, Gemma Boleda, and Raquel Fernandez. "The LAMBADA Dataset: Word Prediction Requiring a Broad Discourse Context". In: *Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (ACL)*. 2016.
— Cited in 12_appendix-e-experimental-details.md as a downstream evaluation task measuring common sense reasoning.

**Qin, Han, W. Sun, D. Li, et al. 2022**
Zhen Qin, Xiaodong Han, Weixuan Sun, Dongxu Li, Lingpeng Kong, Nick Barnes, and Yiran Zhong. "The Devil in Linear Transformer". In: *Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)*. 2022.
— Cited in 09_appendix-b-related-work.md as TransNormer, showing the LA denominator term can be unstable and proposing LayerNorm replacement.

**Qin, W. Sun, et al. 2022**
Zhen Qin, Weixuan Sun, Hui Deng, Dongxu Li, Yunshen Wei, Baohong Lv, Junjie Yan, Lingpeng Kong, and Yiran Zhong. "cosFormer: Rethinking Softmax in Attention". In: *The International Conference on Learning Representations (ICLR)*. 2022.
— Cited in 09_appendix-b-related-work.md as cosFormer, augmenting RFA with a cosine reweighting mechanism incorporating positional information.

**Su et al. 2021**
Jianlin Su, Yu Lu, Shengfeng Pan, Ahmed Murtadha, Bo Wen, and Yunfeng Liu. "RoFormer: Enhanced Transformer with Rotary Position Embedding". In: *arXiv preprint arXiv:2104.09864* (2021).
— Cited in 12_appendix-e-experimental-details.md for rotary positional encodings (RoPE) used in Transformer++.

**Zellers et al. 2019**
Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali Farhadi, and Yejin Choi. "HellaSwag: Can a Machine Really Finish Your Sentence?" In: *Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics (ACL)*. 2019.
— Cited in 12_appendix-e-experimental-details.md as a downstream evaluation task measuring common sense reasoning.

**Zheng, C. Wang, and L. Kong 2022**
Zhanpeng Zheng, Chenrui Wang, and Lingpeng Kong. "Linear Complexity Randomized Self-attention Mechanism". In: *International Conference on Machine Learning*. PMLR. 2022.
— Cited in 09_appendix-b-related-work.md for Linear Randomized Attention, generalizing RFA from the perspective of importance sampling.

**Zuo et al. 2022**
Simiao Zuo, Xiaodong Liu, Jian Jiao, Denis Charles, Eren Manavoglu, Tuo Zhao, and Jianfeng Gao. "Efficient Long Sequence Modeling via State Space Augmented Transformer". In: *arXiv preprint* (2022).
— Cited in 12_appendix-e-experimental-details.md for combining LTI SSMs with Attention leading to substantial improvements.
