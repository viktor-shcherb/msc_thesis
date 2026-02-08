# References

## Almazrouei et al. (2023)
E. Almazrouei, H. Alobeidli, A. Alshamsi, A. Cappelli, R. Cojocaru, M. Debbah, E. Goffinet, D. Heslow, J. Launay, Q. Malartic, B. Noune, B. Pannier, and G. Penedo. Falcon-40B: an open large language model with state-of-the-art performance, 2023.
- Cited in 05_scaling-deepseek-moe-16b.md as an open source baseline (Falcon 7B) on the Open LLM Leaderboard. Also referenced implicitly in 01_introduction.md Figure 1 data points.

## Artetxe et al. (2022)
M. Artetxe, S. Bhosale, N. Goyal, T. Mihaylov, M. Ott, S. Shleifer, X. V. Lin, J. Du, S. Iyer, R. Pasunuru, G. Anantharaman, X. Li, S. Chen, H. Akin, M. Baines, L. Martin, X. Zhou, P. S. Koura, B. O'Horo, J. Wang, L. Zettlemoyer, M. T. Diab, Z. Kozareva, and V. Stoyanov. Efficient large scale language modeling with mixtures of experts. In EMNLP 2022, pages 11699–11732. Association for Computational Linguistics, 2022.
- Cited in 06_alignment-deepseek-moe-16b.md as prior research indicating MoE models typically do not gain significantly from fine-tuning.

## Austin et al. (2021)
J. Austin, A. Odena, M. Nye, M. Bosma, H. Michalewski, D. Dohan, E. Jiang, C. Cai, M. Terry, Q. Le, et al. Program synthesis with large language models. arXiv preprint arXiv:2108.07732, 2021.
- Cited in 04_validation-experiments.md as the source of the MBPP code generation benchmark.

## Biderman et al. (2023)
S. Biderman, H. Schoelkopf, Q. G. Anthony, H. Bradley, K. O'Brien, E. Hallahan, M. A. Khan, S. Purohit, U. S. Prashanth, E. Raff, A. Skowron, L. Sutawika, and O. van der Wal. Pythia: A suite for analyzing large language models across training and scaling. In ICML 2023, volume 202 of Proceedings of Machine Learning Research, pages 2397–2430. PMLR, 2023.
- Cited in 01_introduction.md and 05_scaling-deepseek-moe-16b.md as an open source baseline (Pythia 2.8B) on the Open LLM Leaderboard.

## Bisk et al. (2020)
Y. Bisk, R. Zellers, R. L. Bras, J. Gao, and Y. Choi. PIQA: reasoning about physical commonsense in natural language. In The Thirty-Fourth AAAI Conference on Artificial Intelligence, AAAI 2020, pages 7432–7439. AAAI Press, 2020.
- Cited in 04_validation-experiments.md as the source of the PIQA benchmark.

## Black et al. (2021)
S. Black, L. Gao, P. Wang, C. Leahy, and S. Biderman. GPT-Neo: Large Scale Autoregressive Language Modeling with Mesh-Tensorflow, Mar. 2021.
- Cited in 01_introduction.md and 05_scaling-deepseek-moe-16b.md as an open source baseline (GPT-neo 2.7B) on the Open LLM Leaderboard.

## Brown et al. (2020)
T. B. Brown, B. Mann, N. Ryder, M. Subbiah, J. Kaplan, P. Dhariwal, A. Neelakantan, P. Shyam, G. Sastry, A. Askell, S. Agarwal, A. Herbert-Voss, G. Krueger, T. Henighan, R. Child, A. Ramesh, D. M. Ziegler, J. Wu, C. Winter, C. Hesse, M. Chen, E. Sigler, M. Litwin, S. Gray, B. Chess, J. Clark, C. Berner, S. McCandlish, A. Radford, I. Sutskever, and D. Amodei. Language models are few-shot learners. In Advances in Neural Information Processing Systems 33: NeurIPS 2020, 2020.
- Cited in 01_introduction.md as evidence that scaling language models yields stronger models.

## Chen et al. (2021)
M. Chen, J. Tworek, H. Jun, Q. Yuan, H. P. de Oliveira Pinto, J. Kaplan, H. Edwards, Y. Burda, N. Joseph, G. Brockman, A. Ray, R. Puri, G. Krueger, M. Petrov, H. Khlaaf, G. Sastry, P. Mishkin, B. Chan, S. Gray, N. Ryder, M. Pavlov, A. Power, L. Kaiser, M. Bavarian, C. Winter, P. Tillet, F. P. Such, D. Cummings, M. Plappert, F. Chantzis, E. Barnes, A. Herbert-Voss, W. H. Guss, A. Nichol, A. Paino, N. Tezak, J. Tang, I. Babuschkin, S. Balaji, S. Jain, W. Saunders, C. Hesse, A. N. Carr, J. Leike, J. Achiam, V. Misra, E. Morikawa, A. Radford, M. Knight, M. Brundage, M. Murati, K. Mayer, P. Welinder, B. McGrew, D. Amodie, S. McCandlish, I. Sutskever, and W. Zaremba. Evaluating large language models trained on code. CoRR, abs/2107.03374, 2021.
- Cited in 04_validation-experiments.md as the source of the HumanEval code generation benchmark.

## Clark et al. (2018)
P. Clark, I. Cowhey, O. Etzioni, T. Khot, A. Sabharwal, C. Schoenick, and O. Tafjord. Think you have solved question answering? Try ARC, the AI2 reasoning challenge. CoRR, abs/1803.05457, 2018.
- Cited in 04_validation-experiments.md and 05_scaling-deepseek-moe-16b.md as the source of the ARC-easy and ARC-challenge benchmarks.

## Cobbe et al. (2021)
K. Cobbe, V. Kosaraju, M. Bavarian, M. Chen, H. Jun, L. Kaiser, M. Plappert, J. Tworek, J. Hilton, R. Nakano, et al. Training verifiers to solve math word problems. arXiv preprint arXiv:2110.14168, 2021.
- Cited in 05_scaling-deepseek-moe-16b.md as the source of the GSM8K math reasoning benchmark.

## Dai et al. (2022a)
D. Dai, L. Dong, Y. Hao, Z. Sui, B. Chang, and F. Wei. Knowledge neurons in pretrained transformers. In Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), ACL 2022, pages 8493–8502. Association for Computational Linguistics, 2022a.
- Cited in 05_scaling-deepseek-moe-16b.md as supporting the proposition that FFNs in Transformers exhibit knowledge memorization capability.

## Dai et al. (2022b)
D. Dai, L. Dong, S. Ma, B. Zheng, Z. Sui, B. Chang, and F. Wei. Stablemoe: Stable routing strategy for mixture of experts. In Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), ACL 2022, pages 7085–7095. Association for Computational Linguistics, 2022b.
- Cited in 08_related-work.md as using fixed routing strategies for more stable routing and training.

## DeepSeek-AI (2024)
DeepSeek-AI. Deepseek llm: Scaling open-source language models with longtermism. arXiv preprint arXiv:2401.02954, 2024.
- Cited in 01_introduction.md, 05_scaling-deepseek-moe-16b.md, and 07_deepseek-moe-145b-ongoing.md as the source of the DeepSeek 7B and DeepSeek 67B dense model details.

## Du et al. (2022)
N. Du, Y. Huang, A. M. Dai, S. Tong, D. Lepikhin, Y. Xu, M. Krikun, Y. Zhou, A. W. Yu, O. Firat, B. Zoph, L. Fedus, M. P. Bosma, Z. Zhou, T. Wang, Y. E. Wang, K. Webster, M. Pellat, K. Robinson, K. S. Meier-Hellstern, T. Duke, L. Dixon, K. Zhang, Q. V. Le, Y. Wu, Z. Chen, and C. Cui. Glam: Efficient scaling of language models with mixture-of-experts. In ICML 2022, volume 162 of Proceedings of Machine Learning Research, pages 5547–5569. PMLR, 2022.
- Cited in 01_introduction.md, 02_preliminaries.md, and 08_related-work.md as one of the successful attempts at scaling MoE language models (GLaM).

## Dua et al. (2019)
D. Dua, Y. Wang, P. Dasigi, G. Stanovsky, S. Singh, and M. Gardner. DROP: A reading comprehension benchmark requiring discrete reasoning over paragraphs. In NAACL-HLT 2019, Volume 1 (Long and Short Papers), pages 2368–2378. Association for Computational Linguistics, 2019.
- Cited in 05_scaling-deepseek-moe-16b.md as the source of the DROP reading comprehension benchmark.

## Fedus et al. (2021)
W. Fedus, B. Zoph, and N. Shazeer. Switch transformers: Scaling to trillion parameter models with simple and efficient sparsity. CoRR, abs/2101.03961, 2021.
- Cited in 01_introduction.md, 02_preliminaries.md, 04_validation-experiments.md, 06_alignment-deepseek-moe-16b.md, and 08_related-work.md as a pioneer top-1 MoE routing strategy (Switch Transformer).

## Gao et al. (2020)
L. Gao, S. Biderman, S. Black, L. Golding, T. Hoppe, C. Foster, J. Phang, H. He, A. Thite, N. Nabeshima, et al. The Pile: An 800GB dataset of diverse text for language modeling. arXiv preprint arXiv:2101.00027, 2020.
- Cited in 04_validation-experiments.md, 05_scaling-deepseek-moe-16b.md, and 06_alignment-deepseek-moe-16b.md as the source of the Pile language modeling benchmark.

## Geng and Liu (2023)
X. Geng and H. Liu. Openllama: An open reproduction of llama, May 2023.
- Cited in 01_introduction.md and 05_scaling-deepseek-moe-16b.md as an open source baseline (Open LLaMA 3B/7B) on the Open LLM Leaderboard.

## Harlap et al. (2018)
A. Harlap, D. Narayanan, A. Phanishayee, V. Seshadri, N. R. Devanur, G. R. Ganger, and P. B. Gibbons. Pipedream: Fast and efficient pipeline parallel DNN training. CoRR, abs/1806.03377, 2018.
- Cited in 04_validation-experiments.md as the source of PipeDream pipeline parallelism.

## Hendrycks et al. (2020)
D. Hendrycks, C. Burns, S. Basart, A. Zou, M. Mazeika, D. Song, and J. Steinhardt. Measuring massive multitask language understanding. arXiv preprint arXiv:2009.03300, 2020.
- Cited in 05_scaling-deepseek-moe-16b.md as the source of the MMLU benchmark.

## Hendrycks et al. (2021)
D. Hendrycks, C. Burns, S. Kadavath, A. Arora, S. Basart, E. Tang, D. Song, and J. Steinhardt. Measuring mathematical problem solving with the math dataset, 2021.
- Cited in 05_scaling-deepseek-moe-16b.md as the source of the MATH benchmark.

## High-Flyer (2023)
High-Flyer. Hai-llm: An efficient and lightweight tool for training large models, 2023. URL https://www.high-flyer.cn/en/blog/hai-llm.
- Cited in 04_validation-experiments.md as the training framework (HAI-LLM) used for experiments.

## Hochreiter and Schmidhuber (1997)
S. Hochreiter and J. Schmidhuber. Long short-term memory. Neural Computing, 9(8):1735–1780, 1997.
- Cited in 08_related-work.md as the LSTM architecture used in early MoE language models by Shazeer et al. (2017).

## Hoffmann et al. (2022)
J. Hoffmann, S. Borgeaud, A. Mensch, E. Buchatskaya, T. Cai, E. Rutherford, D. de Las Casas, L. A. Hendricks, J. Welbl, A. Clark, T. Hennigan, E. Noland, K. Millican, G. van den Driessche, B. Damoc, A. Guy, S. Osindero, K. Simonyan, E. Elsen, J. W. Rae, O. Vinyals, and L. Sifre. Training compute-optimal large language models. CoRR, abs/2203.15556, 2022.
- Cited in 01_introduction.md as evidence that scaling language models yields stronger models.

## Huang et al. (2023)
Y. Huang, Y. Bai, Z. Zhu, J. Zhang, J. Zhang, T. Su, J. Liu, C. Lv, Y. Zhang, J. Lei, et al. C-Eval: A multi-level multi-discipline chinese evaluation suite for foundation models. arXiv preprint arXiv:2305.08322, 2023.
- Cited in 05_scaling-deepseek-moe-16b.md as the source of the CEval Chinese benchmark.

## Jacobs et al. (1991)
R. A. Jacobs, M. I. Jordan, S. J. Nowlan, and G. E. Hinton. Adaptive mixtures of local experts. Neural Computing, 3(1):79–87, 1991.
- Cited in 01_introduction.md and 08_related-work.md as the original proposal of the Mixture of Experts technique.

## Jordan and Jacobs (1994)
M. I. Jordan and R. A. Jacobs. Hierarchical mixtures of experts and the EM algorithm. Neural Computing, 6(2):181–214, 1994.
- Cited in 01_introduction.md and 08_related-work.md as further development of the MoE technique.

## Joshi et al. (2017)
M. Joshi, E. Choi, D. Weld, and L. Zettlemoyer. TriviaQA: A Large Scale Distantly Supervised Challenge Dataset for Reading Comprehension. arXiv e-prints, art. arXiv:1705.03551, 2017.
- Cited in 04_validation-experiments.md as the source of the TriviaQA benchmark.

## Korthikanti et al. (2023)
V. A. Korthikanti, J. Casper, S. Lym, L. McAfee, M. Andersch, M. Shoeybi, and B. Catanzaro. Reducing activation recomputation in large transformer models. Proceedings of Machine Learning and Systems, 5, 2023.
- Cited in 04_validation-experiments.md as one of the tensor parallelism strategies integrated in the training framework.

## Kwiatkowski et al. (2019)
T. Kwiatkowski, J. Palomaki, O. Redfield, M. Collins, A. Parikh, C. Alberti, D. Epstein, I. Polosukhin, M. Kelcey, J. Devlin, K. Lee, K. N. Toutanova, L. Jones, M.-W. Chang, A. Dai, J. Uszkoreit, Q. Le, and S. Petrov. Natural questions: a benchmark for question answering research. Transactions of the Association for Computational Linguistics, 2019.
- Cited in 04_validation-experiments.md as the source of the NaturalQuestions benchmark.

## Lai et al. (2017)
G. Lai, Q. Xie, H. Liu, Y. Yang, and E. H. Hovy. RACE: large-scale reading comprehension dataset from examinations. In EMNLP 2017, pages 785–794. Association for Computational Linguistics, 2017.
- Cited in 04_validation-experiments.md as the source of the RACE-middle and RACE-high reading comprehension benchmarks.

## Lepikhin et al. (2021)
D. Lepikhin, H. Lee, Y. Xu, D. Chen, O. Firat, Y. Huang, M. Krikun, N. Shazeer, and Z. Chen. Gshard: Scaling giant models with conditional computation and automatic sharding. In 9th International Conference on Learning Representations, ICLR 2021. OpenReview.net, 2021.
- Cited in 01_introduction.md, 02_preliminaries.md, 04_validation-experiments.md, and 08_related-work.md as a pioneer top-2 MoE routing strategy (GShard) and expert parallelism approach.

## Li et al. (2023)
H. Li, Y. Zhang, F. Koto, Y. Yang, H. Zhao, Y. Gong, N. Duan, and T. Baldwin. CMMLU: Measuring massive multitask language understanding in Chinese. arXiv preprint arXiv:2306.09212, 2023.
- Cited in 05_scaling-deepseek-moe-16b.md as the source of the CMMLU Chinese benchmark.

## Lin et al. (2021)
J. Lin, R. Men, A. Yang, C. Zhou, M. Ding, Y. Zhang, P. Wang, A. Wang, L. Jiang, X. Jia, J. Zhang, J. Zhang, X. Zou, Z. Li, X. Deng, J. Liu, J. Xue, H. Zhou, J. Ma, J. Yu, Y. Li, W. Lin, J. Zhou, J. Tang, and H. Yang. M6: A chinese multimodal pretrainer. CoRR, abs/2103.00823, 2021.
- Cited in 08_related-work.md as a large-scale language or multimodal model based on existing MoE architectures.

## Lin et al. (2022)
S. Lin, J. Hilton, and O. Evans. TruthfulQA: Measuring how models mimic human falsehoods. In Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), ACL 2022, pages 3214–3252. Association for Computational Linguistics, 2022.
- Cited in 05_scaling-deepseek-moe-16b.md as one of the benchmarks in the Open LLM Leaderboard.

## Loshchilov and Hutter (2019)
I. Loshchilov and F. Hutter. Decoupled weight decay regularization. In 7th International Conference on Learning Representations, ICLR 2019. OpenReview.net, 2019.
- Cited in 04_validation-experiments.md, 05_scaling-deepseek-moe-16b.md, 06_alignment-deepseek-moe-16b.md, and 07_deepseek-moe-145b-ongoing.md as the AdamW optimizer used throughout training.

## Narayanan et al. (2021)
D. Narayanan, M. Shoeybi, J. Casper, P. LeGresley, M. Patwary, V. Korthikanti, D. Vainbrand, P. Kashinkunti, J. Bernauer, B. Catanzaro, et al. Efficient large-scale language model training on gpu clusters using megatron-lm. In Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis, pages 1–15, 2021.
- Cited in 04_validation-experiments.md as one of the tensor parallelism strategies integrated in the training framework.

## OpenAI (2023)
OpenAI. GPT-4 technical report. CoRR, abs/2303.08774, 2023.
- Cited in 01_introduction.md as evidence that scaling language models yields stronger models.

## Rajbhandari et al. (2020)
S. Rajbhandari, J. Rasley, O. Ruwase, and Y. He. Zero: memory optimizations toward training trillion parameter models. In Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis, SC 2020, page 20. IEEE/ACM, 2020.
- Cited in 04_validation-experiments.md as the ZeRO data parallelism strategy integrated in the training framework.

## Rajbhandari et al. (2022)
S. Rajbhandari, C. Li, Z. Yao, M. Zhang, R. Y. Aminabadi, A. A. Awan, J. Rasley, and Y. He. Deepspeed-moe: Advancing mixture-of-experts inference and training to power next-generation AI scale. In ICML 2022, volume 162 of Proceedings of Machine Learning Research, pages 18332–18346. PMLR, 2022.
- Cited in 03_deepseek-moe-architecture.md as the prototype of shared expert isolation, derived from an engineering perspective.

## Ren et al. (2023)
X. Ren, P. Zhou, X. Meng, X. Huang, Y. Wang, W. Wang, P. Li, X. Zhang, A. Podolskiy, G. Arshinov, A. Bout, I. Piontkovskaya, J. Wei, X. Jiang, T. Su, Q. Liu, and J. Yao. Pangu-Sigma: Towards trillion parameter language model with sparse heterogeneous computing. CoRR, abs/2303.10845, 2023.
- Cited in 08_related-work.md as a large-scale model based on existing MoE architectures.

## Roller et al. (2021)
S. Roller, S. Sukhbaatar, A. Szlam, and J. Weston. Hash layers for large sparse models. CoRR, abs/2106.04426, 2021.
- Cited in 04_validation-experiments.md and 08_related-work.md as an MoE architecture using top-1 hash routing (Hash Layer).

## Sakaguchi et al. (2019)
K. Sakaguchi, R. L. Bras, C. Bhagavatula, and Y. Choi. Winogrande: An adversarial winograd schema challenge at scale, 2019.
- Cited in 05_scaling-deepseek-moe-16b.md as the source of the WinoGrande benchmark.

## Scao et al. (2022)
T. L. Scao, A. Fan, C. Akiki, E. Pavlick, S. Ilic, D. Hesslow, R. Castagne, A. S. Luccioni, F. Yvon, M. Galle, J. Tow, et al. BLOOM: A 176b-parameter open-access multilingual language model. CoRR, abs/2211.05100, 2022.
- Cited in 01_introduction.md and 05_scaling-deepseek-moe-16b.md as an open source baseline (BLOOM 3B) on the Open LLM Leaderboard.

## Sennrich et al. (2016)
R. Sennrich, B. Haddow, and A. Birch. Neural machine translation of rare words with subword units. In Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics, ACL 2016, Volume 1: Long Papers. The Association for Computer Linguistics, 2016.
- Cited in 04_validation-experiments.md as the source of the byte pair encoding (BPE) tokenization method.

## Shazeer (2019)
N. Shazeer. Fast transformer decoding: One write-head is all you need. CoRR, abs/1911.02150, 2019.
- Cited in 05_scaling-deepseek-moe-16b.md as the multi-query attention mechanism; DeepSeek 7B MQA variant also struggled in MMLU-like tasks.

## Shazeer et al. (2017)
N. Shazeer, A. Mirhoseini, K. Maziarz, A. Davis, Q. V. Le, G. E. Hinton, and J. Dean. Outrageously large neural networks: The sparsely-gated mixture-of-experts layer. In 5th International Conference on Learning Representations, ICLR 2017. OpenReview.net, 2017.
- Cited in 01_introduction.md, 03b_load-balance-consideration.md, and 08_related-work.md as the work that introduced MoE into language model training and identified the risk of routing collapse.

## Shen et al. (2023)
S. Shen, L. Hou, Y. Zhou, N. Du, S. Longpre, J. Wei, H. W. Chung, B. Zoph, W. Fedus, X. Chen, T. Vu, Y. Wu, W. Chen, A. Webson, Y. Li, V. Zhao, H. Yu, K. Keutzer, T. Darrell, and D. Zhou. Flan-moe: Scaling instruction-finetuned language models with sparse mixture of experts. CoRR, abs/2305.14705, 2023.
- Cited in 06_alignment-deepseek-moe-16b.md as presenting findings that MoE models can benefit from instruction tuning.

## Shoeybi et al. (2019)
M. Shoeybi, M. Patwary, R. Puri, P. LeGresley, J. Casper, and B. Catanzaro. Megatron-lm: Training multi-billion parameter language models using model parallelism. arXiv preprint arXiv:1909.08053, 2019.
- Cited in 04_validation-experiments.md as one of the tensor parallelism strategies integrated in the training framework.

## Suzgun et al. (2022)
M. Suzgun, N. Scales, N. Scharli, S. Gehrmann, Y. Tay, H. W. Chung, A. Chowdhery, Q. V. Le, E. H. Chi, D. Zhou, et al. Challenging big-bench tasks and whether chain-of-thought can solve them. arXiv preprint arXiv:2210.09261, 2022.
- Cited in 06_alignment-deepseek-moe-16b.md as the source of the BBH benchmark.

## Tillet et al. (2019)
P. Tillet, H. T. Kung, and D. Cox. Triton: An intermediate language and compiler for tiled neural network computations. In Proceedings of the 3rd ACM SIGPLAN International Workshop on Machine Learning and Programming Languages, MAPL 2019, page 10–19. Association for Computing Machinery, 2019.
- Cited in 04_validation-experiments.md as the framework used for developing GPU kernels for gating algorithms.

## Together-AI (2023)
Together-AI. Redpajama-data: An open source recipe to reproduce llama training dataset, April 2023.
- Cited in 01_introduction.md and 05_scaling-deepseek-moe-16b.md as an open source baseline (RedPajama-INCITE 3B/7B) on the Open LLM Leaderboard.

## Touvron et al. (2023a)
H. Touvron, T. Lavril, G. Izacard, X. Martinet, M. Lachaux, T. Lacroix, B. Roziere, N. Goyal, E. Hambro, F. Azhar, A. Rodriguez, A. Joulin, E. Grave, and G. Lample. Llama: Open and efficient foundation language models. CoRR, abs/2302.13971, 2023a.
- Cited in 01_introduction.md and 05_scaling-deepseek-moe-16b.md as evidence that scaling yields stronger models and as a baseline (LLaMA 7B).

## Touvron et al. (2023b)
H. Touvron, L. Martin, K. Stone, P. Albert, A. Almahairi, Y. Babaei, N. Bashlykov, S. Batra, P. Bhargava, S. Bhosale, et al. Llama 2: Open foundation and fine-tuned chat models. CoRR, abs/2307.09288, 2023b.
- Cited in 01_introduction.md, 05_scaling-deepseek-moe-16b.md, and 06_alignment-deepseek-moe-16b.md as a key comparison baseline (LLaMA2 7B) and source of the official LLaMA2 Chat model.

## Vaswani et al. (2017)
A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, L. Kaiser, and I. Polosukhin. Attention is all you need. In Advances in Neural Information Processing Systems 30: NeurIPS 2017, pages 5998–6008, 2017.
- Cited in 01_introduction.md as the Transformer architecture upon which MoE applications are built.

## Wang and Komatsuzaki (2021)
B. Wang and A. Komatsuzaki. GPT-J-6B: A 6 Billion Parameter Autoregressive Language Model, May 2021.
- Cited in 01_introduction.md and 05_scaling-deepseek-moe-16b.md as an open source baseline (GPT-J 6B) on the Open LLM Leaderboard.

## Xu et al. (2020)
L. Xu, H. Hu, X. Zhang, L. Li, C. Cao, Y. Li, Y. Xu, K. Sun, D. Yu, C. Yu, Y. Tian, Q. Dong, W. Liu, B. Shi, Y. Cui, J. Li, J. Zeng, R. Wang, W. Xie, Y. Li, Y. Patterson, Z. Tian, Y. Zhang, H. Zhou, S. Liu, Z. Zhao, Q. Zhao, C. Yue, X. Zhang, Z. Yang, K. Richardson, and Z. Lan. CLUE: A chinese language understanding evaluation benchmark. In Proceedings of the 28th International Conference on Computational Linguistics, COLING 2020, pages 4762–4772. International Committee on Computational Linguistics, 2020.
- Cited in 05_scaling-deepseek-moe-16b.md as the source of the CLUEWSC Chinese disambiguation benchmark.

## Xue et al. (2023)
F. Xue, Z. Zheng, Y. Fu, J. Ni, Z. Zheng, W. Zhou, and Y. You. Openmoe: Open mixture-of-experts language models. https://github.com/XueFuzhao/OpenMoE, 2023.
- Cited in 08_related-work.md as a large-scale model based on existing MoE architectures.

## Zellers et al. (2019)
R. Zellers, A. Holtzman, Y. Bisk, A. Farhadi, and Y. Choi. HellaSwag: Can a machine really finish your sentence? In Proceedings of the 57th Conference of the Association for Computational Linguistics, ACL 2019, pages 4791–4800. Association for Computational Linguistics, 2019.
- Cited in 04_validation-experiments.md as the source of the HellaSwag benchmark.

## Zhang et al. (2022)
S. Zhang, S. Roller, N. Goyal, M. Artetxe, M. Chen, S. Chen, C. Dewan, M. Diab, X. Li, X. V. Lin, T. Mihaylov, M. Ott, S. Shleifer, K. Shuster, D. Simig, P. S. Koura, A. Sridhar, T. Wang, and L. Zettlemoyer. Opt: Open pre-trained transformer language models, 2022.
- Cited in 01_introduction.md and 05_scaling-deepseek-moe-16b.md as an open source baseline (OPT 2.7B) on the Open LLM Leaderboard.

## Zheng et al. (2019)
C. Zheng, M. Huang, and A. Sun. Chid: A large-scale chinese idiom dataset for cloze test. In Proceedings of the 57th Conference of the Association for Computational Linguistics, ACL 2019, pages 778–787. Association for Computational Linguistics, 2019.
- Cited in 05_scaling-deepseek-moe-16b.md and 06_alignment-deepseek-moe-16b.md as the source of the CHID Chinese idiom completion benchmark.

## Zhou et al. (2022)
Y. Zhou, T. Lei, H. Liu, N. Du, Y. Huang, V. Zhao, A. M. Dai, Z. Chen, Q. V. Le, and J. Laudon. Mixture-of-experts with expert choice routing. In NeurIPS, 2022.
- Cited in 08_related-work.md as proposing an expert-choice routing strategy where each token can be assigned to different numbers of experts.

## Zoph (2022)
B. Zoph. Designing effective sparse expert models. In IEEE International Parallel and Distributed Processing Symposium, IPDPS Workshops 2022, page 1044. IEEE, 2022.
- Cited in 01_introduction.md, 02_preliminaries.md, and 08_related-work.md as focusing on training instability and fine-tuning difficulty in MoE models (ST-MoE).
