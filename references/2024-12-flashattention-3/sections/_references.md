# References

This file contains only the references cited in the section notes.

## [3] GQA (p. 12)
Joshua Ainslie, James Lee-Thorp, Michiel de Jong, Yury Zemlyanskiy, Federico Lebrón, and Sumit Sanghai. GQA: Training generalized multi-query transformer models from multi-head checkpoints. arXiv preprint arXiv:2305.13245, 2023.

Cited in: 03_algorithm-continued.md, 07_appendix-a-related-work.md on grouped query attention

## [4] CudaDMA (p. 12)
Michael Bauer, Henry Cook, and Brucek Khailany. CudaDMA: Optimizing GPU Memory Bandwidth via Warp Specialization. In Proceedings of 2011 International Conference for High Performance Computing, Networking, Storage and Analysis, SC '11, New York, NY, USA, 2011. Association for Computing Machinery. ISBN 9781450307710. doi: 10.1145/2063384.2063400. URL https://doi.org/10.1145/2063384.2063400.

Cited in: 03_algorithm.md as related work on warp specialization

## [7] FP8 FlashAttention-2 blog (p. 13)
Ganesh Bikshandi and Jay Shah. Delivering 1 PFLOP/s of Performance with FP8 FlashAttention-2, 2024. URL https://research.colfax-intl.com/adding-fp8-to-flashattention/.

Cited in: 03c_low-precision-fp8.md as previous work on FP8 attention

## [9] QuIP (p. 13)
Jerry Chee, Yaohui Cai, Volodymyr Kuleshov, and Christopher M De Sa. QuIP: 2-bit quantization of large language models with guarantees. Advances in Neural Information Processing Systems, 36, 2024.

Cited in: 03c_low-precision-fp8.md, 07_appendix-a-related-work.md on incoherent processing for quantization

## [11] Vision transformers (p. 13)
Richard J Chen, Chengkuan Chen, Yicong Li, Tiffany Y Chen, Andrew D Trister, Rahul G Krishnan, and Faisal Mahmood. Scaling vision transformers to gigapixel images via hierarchical self-supervised learning. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages 16144–16155, 2022.

Cited in: 01_introduction.md on long-context applications

## [15] FlashAttention-2 (p. 13)
Tri Dao. FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning, 2023. URL https://arxiv.org/abs/2307.08691.

Cited in: 01_introduction.md, 02_background.md, 03_algorithm.md as the predecessor to FlashAttention-3

## [17] FlashAttention (p. 13)
Tri Dao, Daniel Y. Fu, Stefano Ermon, Atri Rudra, and Christopher Ré. FlashAttention: Fast and memory-efficient exact attention with IO-awareness. In Advances in Neural Information Processing Systems, 2022.

Cited in: 01_introduction.md, 02_background.md as the original FlashAttention paper

## [20] Int8 matrix multiplication (p. 13)
Tim Dettmers, Mike Lewis, Younes Belkada, and Luke Zettlemoyer. Llm.int8 (): 8-bit matrix multiplication for transformers at scale. CoRR abs/2208.07339, 2022.

Cited in: 01_introduction.md, 03c_low-precision-fp8.md, 04c_numerical-error-validation.md discussing outliers in LLMs

## [21] Is flash attention stable? (p. 13)
Alicia Golden, Samuel Hsia, Fei Sun, Bilge Acun, Basil Hosmer, Yejin Lee, Zachary DeVito, Jeff Johnson, Gu-Yeon Wei, David Brooks, et al. Is flash attention stable? arXiv preprint arXiv:2405.02803, 2024.

Cited in: 04c_numerical-error-validation.md on numerical error of FlashAttention

## [23] Conformer (p. 13)
Anmol Gulati, James Qin, Chung-Cheng Chiu, Niki Parmar, Yu Zhang, Jiahui Yu, Wei Han, Shibo Wang, Zhengdong Zhang, Yonghui Wu, et al. Conformer: Convolution-augmented transformer for speech recognition. arXiv preprint arXiv:2005.08100, 2020.

Cited in: 01_introduction.md on audio as a long-context modality

## [25] Video diffusion (p. 13)
Jonathan Ho, Tim Salimans, Alexey Gritsenko, William Chan, Mohammad Norouzi, and David J Fleet. Video diffusion models. Advances in Neural Information Processing Systems, 35:8633–8646, 2022.

Cited in: 01_introduction.md on long-context applications

## [33] Kivi (p. 14)
Zirui Liu, Jiayi Yuan, Hongye Jin, Shaochen Zhong, Zhaozhuo Xu, Vladimir Braverman, Beidi Chen, and Xia Hu. Kivi: A tuning-free asymmetric 2bit quantization for kv cache. arXiv preprint arXiv:2402.02750, 2024.

Cited in: 03c_low-precision-fp8.md discussing KV cache quantization

## [34] Nvidia Hopper GPU Architecture (p. 14)
Weile Luo, Ruibo Fan, Zeyu Li, Dayou Du, Qiang Wang, and Xiaowen Chu. Benchmarking and Dissecting the Nvidia Hopper GPU Architecture, 2023. URL https://arxiv.org/abs/2402.13499.

Cited in: 02_background.md describing Hopper architecture

## [37] FP8 formats (p. 14)
Paulius Micikevicius, Dusan Stosic, Neil Burgess, Marius Cornea, Pradeep Dubey, Richard Grisenthwaite, Sangwon Ha, Alexander Heinecke, Patrick Judd, John Kamalu, et al. Fp8 formats for deep learning. arXiv preprint arXiv:2209.05433, 2022.

Cited in: 03c_low-precision-fp8.md discussing FP8 format specifications

## [38] CUDA Programming Guide (p. 14)
NVIDIA. CUDA Programming Guide Version 12.4, 2024. URL https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html.

Cited in: 02_background.md for GPU programming concepts

## [39] Accelerating transformers with cuDNN 9 (p. 14)
Nvidia. Accelerating transformers with nvidia cudnn 9. Nvidia blog, 2024. URL https://developer.nvidia.com/blog/accelerating-transformers-with-nvidia-cudnn-9/.

Cited in: 03_algorithm.md, 04a_benchmarking-attention.md discussing cuDNN kernels

## [46] Matrix Transpose in CUTLASS (p. 15)
Colfax Research. Tutorial: Matrix Transpose in CUTLASS, 2024. URL https://research.colfax-intl.com/tutorial-matrix-transpose-in-cutlass/.

Cited in: 03c_low-precision-fp8.md on kernel transpose technique

## [51] Fast transformer decoding (p. 15)
Noam Shazeer. Fast transformer decoding: One write-head is all you need. arXiv preprint arXiv:1911.02150, 2019.

Cited in: 03_algorithm-continued.md, 07_appendix-a-related-work.md on multi-query attention

## [52] ThunderKittens (p. 15)
Benjamin Spector, Aaryan Singhal, Simran Arora, and Christopher Ré. 2024. URL https://github.com/HazyResearch/ThunderKittens.

Cited in: 01_introduction.md on Hopper-specific instructions and tile-based abstractions for attention

## [54] Massive activations (p. 15)
Mingjie Sun, Xinlei Chen, J Zico Kolter, and Zhuang Liu. Massive activations in large language models. arXiv preprint arXiv:2402.17762, 2024.

Cited in: 01_introduction.md, 03c_low-precision-fp8.md, 04c_numerical-error-validation.md discussing outliers in LLMs

## [57] CUTLASS (p. 15)
Vijay Thakkar, Pradeep Ramani, Cris Cecka, Aniket Shivam, Honghao Lu, Ethan Yan, Jack Kosaian, Mark Hoemmen, Haicheng Wu, Andrew Kerr, Matt Nicely, Duane Merrill, Dustyn Blasig, Fengqi Qiao, Piotr Majcher, Paul Springer, Markus Holmerbach, Jin Wang, and Manish Gupta. CUTLASS, January 2023. URL https://github.com/NVIDIA/cutlass.

Cited in: 02_background.md, 03_algorithm.md, 03c_low-precision-fp8.md, 04_empirical-validation.md on CUTLASS library usage

## [58] Quip# (p. 16)
Albert Tseng, Jerry Chee, Qingyao Sun, Volodymyr Kuleshov, and Christopher De Sa. Quip#: Even better llm quantization with hadamard incoherence and lattice codebooks. arXiv preprint arXiv:2402.04396, 2024.

Cited in: 03c_low-precision-fp8.md on incoherent processing

## [59] Attention is all you need (p. 16)
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz Kaiser, and Illia Polosukhin. Attention is all you need. Advances in neural information processing systems, 30, 2017.

Cited in: 01_introduction.md, 02_background.md as the foundational Transformer paper

## [62] ReAct (p. 16)
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao. React: Synergizing reasoning and acting in language models. arXiv preprint arXiv:2210.03629, 2022.

Cited in: 01_introduction.md on long-context applications

## [1] Abdelfattah et al. high performance batched GEMM (p. 17)
Abdelfattah et al. presents a high performance batched GEMM kernel on K40c Graphics Processing Units (GPU) for both fixed and variable sizes.

Cited in: 07_appendix-a-related-work.md on hardware-aware algorithms

## [2] Jamba (p. 17)
Jamba - medium to large-scale model using alternative architectures.

Cited in: 07_appendix-a-related-work.md on alternative architectures

## [5] xLSTM (p. 17)
xLSTM - alternative architecture with learnable weighting for recurrence that can match Transformers at small/medium scale.

Cited in: 07_appendix-a-related-work.md on alternative architectures

## [6] Sliding window attention (p. 17)
Sliding window approach for sparse attention pattern selection.

Cited in: 07_appendix-a-related-work.md on attention variants

## [8] Ring attention variants (p. 17)
Variants of Ring attention for distributed attention computation.

Cited in: 07_appendix-a-related-work.md on distributed attention

## [10] Combined sparse and low-rank (p. 17)
Method combining sparse and low-rank approximation for better quality.

Cited in: 07_appendix-a-related-work.md on attention approximation methods

## [12] Fixed pattern sparse attention (p. 17)
Fixed pattern approach for choosing zero entries in sparse attention.

Cited in: 07_appendix-a-related-work.md on sparse attention

## [13] Performers / Random projection (p. 13)
Krzysztof Choromanski, Valerii Likhosherstov, David Dohan, Xingyou Song, Andreea Gane, Tamas Sarlos, Peter Hawkins, Jared Davis, Afroz Mohiuddin, Lukasz Kaiser, et al. Rethinking attention with performers. In The International Conference on Learning Representations (ICLR), 2021.

Cited in: 07_appendix-a-related-work.md on random projection for low-rank attention

## [16] Token-mixing matrix (p. 17)
Work on generalizations of linear attention through the lens of token-mixing matrix structure.

Cited in: 07_appendix-a-related-work.md on alternative architectures

## [19] Multi-head latent attention (p. 17)
Multi-head latent attention parameterizes K and V as low-rank projections of shared latent matrix.

Cited in: 07_appendix-a-related-work.md on KV cache reduction

## [22] Mamba (p. 13)
Albert Gu and Tri Dao. Mamba: Linear-time sequence modeling with selective state spaces. 2023.

Cited in: 01_introduction.md, 07_appendix-a-related-work.md on alternative architectures

## [26] KV cache compression (p. 17)
Work on compressing KV cache to 4-, 3-, or 2-bits for inference.

Cited in: 07_appendix-a-related-work.md on low-precision attention

## [27] Linear attention (p. 14)
Angelos Katharopoulos, Apoorv Vyas, Nikolaos Pappas, and Francois Fleuret. Transformers are RNNs: Fast autoregressive transformers with linear attention. In International Conference on Machine Learning, pages 5156-5165. PMLR, 2020.

Cited in: 01_introduction.md, 07_appendix-a-related-work.md on attention approximation and alternative architectures

## [28] Hashing-based sparse attention (p. 17)
Dynamic sparse attention pattern selection through hashing.

Cited in: 07_appendix-a-related-work.md on sparse attention

## [31] Ring attention (p. 17)
Ring attention - distributed attention method reaching up to 1 million context length.

Cited in: 07_appendix-a-related-work.md on distributed attention

## [32] Ring attention variants (p. 17)
Additional Ring attention variant work.

Cited in: 07_appendix-a-related-work.md on distributed attention

## [35] MEGA (p. 17)
MEGA - alternative architecture building on linear attention with sophisticated recurrences.

Cited in: 07_appendix-a-related-work.md on alternative architectures

## [36] Megalodon (p. 14)
Xuezhe Ma, Xiaomeng Yang, Wenhan Xiong, Beidi Chen, Lili Yu, Hao Zhang, Jonathan May, Luke Zettlemoyer, Omer Levy, and Chunting Zhou. Megalodon: Efficient llm pretraining and inference with unlimited context length. arXiv preprint arXiv:2404.08801, 2024.

Cited in: 07_appendix-a-related-work.md on alternative architectures (medium to large-scale models)

## [41] Stream-K and Lightning (p. 17)
Work on load balancing strategies for GPU kernels.

Cited in: 07_appendix-a-related-work.md on hardware-aware algorithms

## [42] RWKV (p. 15)
Bo Peng, Eric Alcaide, Quentin Anthony, Alon Albalak, Samuel Arcadinho, Huanqi Cao, Xin Cheng, Michael Chung, Matteo Grella, Kranthi Kiran GV, et al. RWKV: Reinventing RNNs for the Transformer era. arXiv preprint arXiv:2305.13048, 2023.

Cited in: 01_introduction.md, 07_appendix-a-related-work.md on alternative architectures

## [43] Yarn (p. 15)
Bowen Peng, Jeffrey Quesnelle, Honglu Fan, and Enrico Shippole. Yarn: Efficient context window extension of large language models. arXiv preprint arXiv:2309.00071, 2023.

Cited in: 01_introduction.md on long document modeling

## [44] Random projection (p. 17)
Random projection approach for low-rank attention.

Cited in: 07_appendix-a-related-work.md on low-rank attention

## [45] Self-attention O(n) memory (p. 15)
Markus N Rabe and Charles Staats. Self-attention does not need O(n^2) memory. arXiv preprint arXiv:2112.05682, 2021.

Cited in: 01_introduction.md on software optimization for attention

## [47] Routing-based sparse attention (p. 17)
Dynamic sparse attention pattern selection through routing.

Cited in: 07_appendix-a-related-work.md on sparse attention

## [49] LeanAttention (p. 17)
LeanAttention - hardware-aware algorithm with smarter load balancing for near-peak occupancy.

Cited in: 07_appendix-a-related-work.md on hardware-aware algorithms

## [56] Efficient transformers survey (p. 15)
Yi Tay, Mostafa Dehghani, Dara Bahri, and Donald Metzler. Efficient transformers: A survey. arXiv preprint arXiv:2009.06732, 2020.

Cited in: 01_introduction.md, 07_appendix-a-related-work.md on attention approximation methods

## [60] Mamba2-hybrid (p. 17)
Mamba2-hybrid - large-scale model (>65M parameters) using alternative architectures with attention layers.

Cited in: 07_appendix-a-related-work.md on alternative architectures

## [61] Random projection (p. 17)
Yunyang Xiong, Zhanpeng Zeng, Rudrasis Chakraborty, Mingxing Tan, Glenn Fung, Yin Li, and Vikas Singh. Nystromformer: A nystom-based algorithm for approximating self-attention. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 35, page 14138, 2021.

Cited in: 07_appendix-a-related-work.md on low-rank attention

## [14] Performers (p. 13)
Krzysztof Marcin Choromanski, Valerii Likhosherstov, David Dohan, Xingyou Song, Andreea Gane, Tamas Sarlos, Peter Hawkins, Jared Quincy Davis, Afroz Mohiuddin, Lukasz Kaiser, et al. Rethinking attention with performers. In International Conference on Learning Representations (ICLR), 2020.

Cited in: 01_introduction.md on attention approximation methods

## [18] H3 / Hungry Hungry Hippos (p. 13)
Tri Dao, Daniel Y Fu, Khaled K Saab, Armin W Thomas, Atri Rudra, and Christopher Re. Hungry hungry hippos: Towards language modeling with state space models. In The International Conference on Learning Representations (ICLR), 2023.

Cited in: 07_appendix-a-related-work.md on alternative architectures (H3)

## [24] LongT5 (p. 14)
Mandy Guo, Joshua Ainslie, David Uthus, Santiago Ontanon, Jianmo Ni, Yun-Hsuan Sung, and Yinfei Yang. Longt5: Efficient text-to-text transformer for long sequences. arXiv preprint arXiv:2112.07916, 2021.

Cited in: 01_introduction.md on long document modeling

## [29] PagedAttention (p. 14)
Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu, Joseph Gonzalez, Hao Zhang, and Ion Stoica. Efficient memory management for large language model serving with pagedattention. In Proceedings of the 29th Symposium on Operating Systems Principles, pages 611-626, 2023.

Cited in: 01_introduction.md on software optimization for attention

## [30] StarCoder (p. 14)
Raymond Li, Loubna Ben Allal, Yangtian Zi, Niklas Muennighoff, Denis Kocetkov, Chenghao Mou, Marc Marone, Christopher Akiki, Jia Li, Jenny Chim, et al. Starcoder: may the source be with you! arXiv preprint arXiv:2305.06161, 2023.

Cited in: 01_introduction.md on large codebases

## [40] PTX ISA (p. 14)
NVIDIA. Parallel Thread Execution ISA Version 8.4, 2024. URL https://docs.nvidia.com/cuda/pdf/ptx_isa_8.4.pdf.

Cited in: 02_background.md, 02_background-continued.md on WGMMA and setmaxnreg instructions

## [48] Code Llama (p. 15)
Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, Sten Sootla, Itai Gat, Xiaoqing Ellen Tan, Yossi Adi, Jingyu Liu, Tal Remez, Jeremy Rapin, et al. Code llama: Open foundation models for code. arXiv preprint arXiv:2308.12950, 2023.

Cited in: 01_introduction.md on large codebases

## [50] Scrolls (p. 15)
Uri Shaham, Elad Segal, Maor Ivgi, Avia Efrat, Ori Yoran, Adi Haviv, Ankit Gupta, Wenhan Xiong, Mor Geva, Jonathan Berant, et al. Scrolls: Standardized comparison over long language sequences. arXiv preprint arXiv:2201.03533, 2022.

Cited in: 01_introduction.md on long document modeling

## [55] Retnet (p. 15)
Yutao Sun, Li Dong, Shaohan Huang, Shuming Ma, Yuqing Xia, Jilong Xue, Jianyong Wang, and Furu Wei. Retentive network: A successor to transformer for large language models. arXiv preprint arXiv:2307.08621, 2023.

Cited in: 01_introduction.md, 07_appendix-a-related-work.md on alternative architectures

## [63] Big Bird (p. 16)
Manzil Zaheer, Guru Guruganesh, Kumar Avinava Dubey, Joshua Ainslie, Chris Alberti, Santiago Ontanon, Philip Pham, Anirudh Ravula, Qifan Wang, Li Yang, et al. Big bird: Transformers for longer sequences. Advances in Neural Information Processing Systems, 33, 2020.

Cited in: 07_appendix-a-related-work.md on combined sparse and low-rank attention approximation

## [64] Zamba (p. 16)
Zyphra. Zyphra unveils zamba: A compact 7b ssm hybrid model. Zyphra blog, 2024.

Cited in: 07_appendix-a-related-work.md on alternative architectures (medium to large-scale models)
