# References

## [1]
Joshua Ainslie, James Lee-Thorp, Michiel de Jong, Yury Zemlyanskiy, Federico Lebron, and Sumit Sanghai. GQA: Training generalized multi-query transformer models from multi-head checkpoints. *arXiv preprint arXiv:2305.13245*, 2023.
- Cited in 02_background.md (grouped-query attention variant) and 03_flashattention-2.md (GQA support in FlashAttention-2)

## [2]
Iz Beltagy, Matthew E Peters, and Arman Cohan. Longformer: The long-document transformer. *arXiv preprint arXiv:2004.05150*, 2020.
- Cited in 01_introduction.md as one of the approximate attention methods proposed to reduce computational requirement

## [3]
Beidi Chen, Tri Dao, Eric Winsor, Zhao Song, Atri Rudra, and Christopher Re. Scatterbrain: Unifying sparse and low-rank attention. In *Advances in Neural Information Processing Systems (NeurIPS)*, 2021.
- Cited in 01_introduction.md as one of the approximate attention methods

## [4]
Krzysztof Marcin Choromanski, Valerii Likhosherstov, David Dohan, Xingyou Song, Andreea Gane, Tamas Sarlos, Peter Hawkins, Jared Quincy Davis, Afroz Mohiuddin, Lukasz Kaiser, et al. Rethinking attention with performers. In *International Conference on Learning Representations (ICLR)*, 2020.
- Cited in 01_introduction.md as one of the approximate attention methods

## [5]
Tri Dao, Daniel Y. Fu, Stefano Ermon, Atri Rudra, and Christopher Re. FlashAttention: Fast and memory-efficient exact attention with IO-awareness. In *Advances in Neural Information Processing Systems*, 2022.
- Cited in 00_overview.md (abstract), 01_introduction.md (original FlashAttention proposal), 02_background.md (algorithm description), 03_flashattention-2.md (correctness proof reference)

## [6]
Zhe Jia and Peter Van Sandt. Dissecting the Ampere GPU architecture via microbenchmarking. GPU Technology Conference, 2021.
- Cited in 02_background.md for A100 GPU memory hierarchy specifications (SRAM bandwidth estimate)

## [7]
Zhe Jia, Marco Maggioni, Benjamin Staiger, and Daniele P Scarpazza. Dissecting the nvidia Volta GPU architecture via microbenchmarking. *arXiv preprint arXiv:1804.06826*, 2018.
- Cited in 02_background.md for GPU memory hierarchy specifications

## [8]
Angelos Katharopoulos, Apoorv Vyas, Nikolaos Pappas, and Francois Fleuret. Transformers are RNNs: Fast autoregressive transformers with linear attention. In *International Conference on Machine Learning*, pages 5156-5165. PMLR, 2020.
- Cited in 01_introduction.md as one of the approximate attention methods

## [9]
Nikita Kitaev, Lukasz Kaiser, and Anselm Levskaya. Reformer: The efficient transformer. In *The International Conference on Machine Learning (ICML)*, 2020.
- Cited in 01_introduction.md as one of the approximate attention methods

## [10]
Benjamin Lefaudeux, Francisco Massa, Diana Liskovich, Wenhan Xiong, Vittorio Caggiano, Sean Naren, Min Xu, Jieru Hu, Marta Tintore, Susan Zhang, Patrick Labatut, and Daniel Haziza. xformers: A modular and hackable transformer modelling library. https://github.com/facebookresearch/xformers, 2022.
- Cited in 06_acknowledgements.md (Daniel Haziza's implementation of FlashAttention in xformers library)

## [11]
Maxim Milakov and Natalia Gimelshein. Online normalizer calculation for softmax. *arXiv preprint arXiv:1805.02867*, 2018.
- Cited in 02_background.md as the origin of the online softmax technique used in FlashAttention

## [12]
OpenAI. GPT-4 technical report. *ArXiv*, abs/2303.08774, 2023.
- Cited in 01_introduction.md as example of a model with long context (32k)

## [13]
Markus N Rabe and Charles Staats. Self-attention does not need O(n^2) memory. *arXiv preprint arXiv:2112.05682*, 2021.
- Cited in 02_background.md for use of online softmax in attention computation

## [14]
Aurko Roy, Mohammad Saffar, Ashish Vaswani, and David Grangier. Efficient content-based sparse attention with routing transformers. *Transactions of the Association for Computational Linguistics*, 9:53-68, 2021.
- Cited in 01_introduction.md as one of the approximate attention methods

## [15]
Noam Shazeer. Fast transformer decoding: One write-head is all you need. *arXiv preprint arXiv:1911.02150*, 2019.
- Cited in 02_background.md and 03_flashattention-2.md for multi-query attention (MQA)

## [16]
Mohammad Shoeybi, Mostofa Patwary, Raul Puri, Patrick LeGresley, Jared Casper, and Bryan Catanzaro. Megatron-LM: Training multi-billion parameter language models using model parallelism. *arXiv preprint arXiv:1909.08053*, 2019.
- Cited in 04_empirical-validation.md for the FLOPs calculation formula used to measure training throughput

## [17]
Philippe Tillet, Hsiang-Tsung Kung, and David Cox. Triton: an intermediate language and compiler for tiled neural network computations. In *Proceedings of the 3rd ACM SIGPLAN International Workshop on Machine Learning and Programming Languages*, pages 10-19, 2019.
- Cited in 03_flashattention-2.md (Phil Tillet's Triton implementation of FlashAttention with loop reordering and sequence-length parallelism) and 06_acknowledgements.md

## [18]
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Lukasz Kaiser, and Illia Polosukhin. Attention is all you need. *Advances in neural information processing systems*, 30, 2017.
- Cited in 01_introduction.md as the original Transformer paper

## [19]
Sinong Wang, Belinda Z Li, Madian Khabsa, Han Fang, and Hao Ma. Linformer: Self-attention with linear complexity. *arXiv preprint arXiv:2006.04768*, 2020.
- Cited in 01_introduction.md as one of the approximate attention methods

## [20]
Manzil Zaheer, Guru Guruganesh, Kumar Avinava Dubey, Joshua Ainslie, Chris Alberti, Santiago Ontanon, Philip Pham, Anirudh Ravula, Qifan Wang, Li Yang, et al. Big bird: Transformers for longer sequences. *Advances in Neural Information Processing Systems*, 33, 2020.
- Cited in 01_introduction.md as one of the approximate attention methods
