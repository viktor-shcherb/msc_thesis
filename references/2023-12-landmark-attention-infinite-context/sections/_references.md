# References

Only references cited in the section notes are included below.

---

**[2]** Anthropic. claude-v1.3-100k, Blog post 'Introducing 100K Context Windows'. https://www.anthropic.com/index/100k-context-windows, 2023.
- Cited in 02_related-work.md as example of commercial long-context model (100k tokens).

**[3]** Iz Beltagy, Matthew E. Peters, and Arman Cohan. Longformer: The long-document transformer.
- Cited in 02_related-work.md as a sparse attention method with dilated sliding window patterns.

**[4]** Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, and Dario Amodei. Language models are few-shot learners. In *Advances in Neural Information Processing Systems 33: NeurIPS 2020*, 2020.
- Cited in 01_introduction.md as evidence of large transformers' few-shot abilities.

**[5]** Aydar Bulatov, Yuri Kuratov, and Mikhail S. Burtsev. Recurrent memory transformer.
- Cited in 02_related-work.md as a recurrence-based memory method for Transformers.

**[6]** Mikhail S. Burtsev, Yuri Kuratov, Anton Peganov, and Grigory V. Sapunov. Memory transformer.
- Cited in 02_related-work.md as introducing special memory tokens prepended to input.

**[7]** Rewon Child, Scott Gray, Alec Radford, and Ilya Sutskever. Generating Long Sequences with Sparse Transformers, 2019. arXiv:1904.10509.
- Cited in 02_related-work.md as limiting attention to a local window around each token.

**[8]** Krzysztof Choromanski, Valerii Likhosherstov, David Dohan, Xingyou Song, Andreea Gane, Tamas Sarlos, Peter Hawkins, Jared Davis, Afroz Mohiuddin, Lukasz Kaiser, David Belanger, Lucy Colwell, and Adrian Weller. Rethinking Attention with Performers, November 2022. arXiv:2009.14794.
- Cited in 02_related-work.md as using a non-softmax kernel for efficient attention.

**[9]** Zihang Dai, Zhilin Yang, Yiming Yang, Jaime Carbonell, Quoc Le, and Ruslan Salakhutdinov. Transformer-XL: Attentive language models beyond a fixed-length context. In *Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics*, pages 2978-2988, Florence, Italy, 2019.
- Cited in 01_introduction.md, 02_related-work.md, 05_experiments.md as the primary recurrent-memory baseline (Transformer-XL).

**[10]** Tri Dao, Daniel Y. Fu, Stefano Ermon, Atri Rudra, and Christopher Re. FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness, June 2022.
- Cited in 04_memory-and-computation.md as compatible with the landmark method for further overhead reduction.

**[11]** Kelvin Guu, Kenton Lee, Zora Tung, Panupong Pasupat, and Ming-Wei Chang. REALM: Retrieval-augmented language model pre-training.
- Cited in 02_related-work.md as jointly training reader and retriever.

**[12]** Adi Haviv, Ori Ram, Ofir Press, Peter Izsak, and Omer Levy. Transformer Language Models without Positional Encodings Still Learn Positional Information, 2022. arXiv:2203.16634.
- Cited in 02_related-work.md as demonstrating that models learn positional encoding through causal masking.

**[13]** Gautier Izacard, Patrick Lewis, Maria Lomeli, Lucas Hosseini, Fabio Petroni, Timo Schick, Jane Dwivedi-Yu, Armand Joulin, Sebastian Riedel, and Edouard Grave. Atlas: Few-shot learning with retrieval augmented language models.
- Cited in 02_related-work.md as investigating retriever loss functions.

**[14]** Zhengbao Jiang, Luyu Gao, Jun Araki, Haibo Ding, Zhiruo Wang, Jamie Callan, and Graham Neubig. Retrieval as attention: End-to-end learning of retrieval and reading within a single transformer.
- Cited in 02_related-work.md as using attention to build a retriever with manually crafted rules.

**[15]** Jeff Johnson, Matthijs Douze, and Herve Jegou. Billion-scale similarity search with GPUs.
- Cited in 01_introduction.md, 03_methodology.md, 04_memory-and-computation.md as FAISS, a data structure for efficient nearest-neighbor retrieval.

**[16]** Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, and Wen-tau Yih. Dense passage retrieval for open-domain question answering. In *Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, pages 6769-6781, 2020.
- Cited in 02_related-work.md as a method for training retrievers and readers.

**[17]** Urvashi Khandelwal, Omer Levy, Dan Jurafsky, Luke Zettlemoyer, and Mike Lewis. Generalization through memorization: Nearest neighbor language models. In *8th International Conference on Learning Representations, ICLR 2020*, 2020.
- Cited in 02_related-work.md as kNN-LM, storing hidden representations for nearest-neighbor prediction.

**[18]** Omar Khattab, Christopher Potts, and Matei Zaharia. Relevance-guided supervision for OpenQA with ColBERT. *Transactions of the Association for Computational Linguistics*, 9:929-944, 2021.
- Cited in 02_related-work.md as using attention in the reader with manually crafted rules to build a retriever.

**[19]** Nikita Kitaev, Lukasz Kaiser, and Anselm Levskaya. Reformer: The efficient transformer. In *8th International Conference on Learning Representations, ICLR 2020*, 2020.
- Cited in 02_related-work.md as using locality-sensitive hashing for efficient attention.

**[20]** Olga Kovaleva, Alexey Romanov, Anna Rogers, and Anna Rumshisky. Revealing the dark secrets of BERT. In *Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)*, pages 4365-4374, 2019.
- Cited in 03_methodology.md as observing classic attention patterns that block-level retrieval may accommodate.

**[22]** Ilya Loshchilov and Frank Hutter. Decoupled weight decay regularization. In *7th International Conference on Learning Representations, ICLR 2019*, 2019.
- Cited in 05_experiments.md as the AdamW optimizer used for training.

**[23]** Pedro Henrique Martins, Zita Marinho, and Andre F. T. Martins. Infinite memory transformer.
- Cited in 02_related-work.md as mapping input to a continuous space for memory sampling.

**[24]** Jesse Mu, Xiang Lisa Li, and Noah Goodman. Learning to Compress Prompts with Gist Tokens, 2023. arXiv:2304.08467.
- Cited in 02_related-work.md as simultaneous work proposing "gist" tokens that cannot remember specific details.

**[25]** OpenAI. GPT-4 Technical Report. arXiv, 2023.
- Cited in 01_introduction.md and 02_related-work.md as a commercial model with 32k context length.

**[27]** Ofir Press, Noah A. Smith, and Mike Lewis. Train short, test long: Attention with linear biases enables input length extrapolation. In *The Tenth International Conference on Learning Representations, ICLR 2022*, 2022.
- Cited in 02_related-work.md as documenting Transformers' inability to extrapolate to longer contexts.

**[28]** Alec Radford, Jeff Wu, Rewon Child, David Luan, Dario Amodei, and Ilya Sutskever. Language models are unsupervised multitask learners. 2019.
- Cited in 05_experiments.md as the GPT-2 architecture and tokenizer used for experiments.

**[29]** Jack W. Rae, Anna Potapenko, Siddhant M. Jayakumar, Chloe Hillier, and Timothy P. Lillicrap. Compressive transformers for long-range sequence modelling. In *8th International Conference on Learning Representations, ICLR 2020*, 2020.
- Cited in 05_experiments.md as the PG-19 dataset (3.7B tokens of English books).

**[30]** Hongyu Ren, Hanjun Dai, Zihang Dai, Mengjiao Yang, Jure Leskovec, Dale Schuurmans, and Bo Dai. Combiner: Full Attention Transformer with Sparse Computation Cost, October 2021. arXiv:2107.05768.
- Cited in 02_related-work.md as using hierarchical attention with heuristic reductions like max-pooling.

**[31]** Keshav Santhanam, Omar Khattab, Jon Saad-Falcon, Christopher Potts, and Matei Zaharia. ColBERTv2: Effective and efficient retrieval via lightweight late interaction. In *Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies*, pages 3715-3734, 2022.
- Cited in 02_related-work.md as using attention in the reader with manually crafted rules.

**[33]** Jianlin Su, Yu Lu, Shengfeng Pan, Ahmed Murtadha, Bo Wen, and Yunfeng Liu. RoFormer: Enhanced transformer with rotary position embedding.
- Cited in 03_methodology.md as the Rotary positional encoding (RoPE) used in experiments.

**[36]** Yutao Sun, Li Dong, Barun Patra, Shuming Ma, Shaohan Huang, Alon Benhaim, Vishrav Chaudhary, Xia Song, and Furu Wei. A Length-Extrapolatable Transformer, 2022. arXiv:2212.10554.
- Cited in 02_related-work.md as a method for context length extrapolation that weakens long-range attention scores.

**[37]** Philippe Tillet, Hsiang-Tsung Kung, and David Cox. Triton: an intermediate language and compiler for tiled neural network computations. In *Proceedings of the 3rd ACM SIGPLAN International Workshop on Machine Learning and Programming Languages*, pages 10-19, 2019.
- Cited in 04_memory-and-computation.md as the framework used for the efficient implementation.

**[38]** Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothee Lacroix, Baptiste Roziere, Naman Goyal, Eric Hambro, Faisal Azhar, Aurelien Rodriguez, Armand Joulin, Edouard Grave, and Guillaume Lample. LLaMA: Open and Efficient Foundation Language Models, 2023. arXiv:2302.13971.
- Cited in 01_introduction.md and 05_experiments.md as the LLaMA 7B model fine-tuned with landmarks.

**[39]** Sinong Wang, Belinda Z Li, Madian Khabsa, Han Fang, and Hao Ma. Linformer: Self-attention with linear complexity. *arXiv preprint arXiv:2006.04768*, 2020.
- Cited in 02_related-work.md as using a low-rank approximation of the attention matrix.

**[40]** Qingyang Wu, Zhenzhong Lan, Kun Qian, Jing Gu, Alborz Geramifard, and Zhou Yu. Memformer: A memory-augmented transformer for sequence modeling.
- Cited in 02_related-work.md as a recurrence-based memory method for Transformers.

**[41]** Yuhuai Wu, Markus Norman Rabe, DeLesley Hutchins, and Christian Szegedy. Memorizing transformers. In *The Tenth International Conference on Learning Representations, ICLR 2022*, 2022.
- Cited in 02_related-work.md as Memorizing Transformer performing nearest-neighbor search over previous keys.

**[42]** Manzil Zaheer, Guru Guruganesh, Kumar Avinava Dubey, Joshua Ainslie, Chris Alberti, Santiago Ontanon, Philip Pham, Anirudh Ravula, Qifan Wang, Li Yang, and Amr Ahmed. Big bird: Transformers for longer sequences. In *Advances in Neural Information Processing Systems 33: NeurIPS 2020*, 2020.
- Cited in 02_related-work.md as BigBird, attending to random subset of tokens plus globally accessible tokens.
