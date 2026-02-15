# References

This file contains only the references that were cited in the section notes.

## Arora et al., 2023
Simran Arora, Sabri Eyuboglu, Aman Timalsina, Isys Johnson, Michael Poli, James Zou, Atri Rudra, and Christopher Ré. Zoology: Measuring and improving recall in efficient language models. *arXiv preprint arXiv:2312.04927*, 2023.

**Cited in:** 03h_ablation-studies.md - Used as basis for fine-grained loss metrics ("AR-Hit" and "Others" slices) [p. 10]

## Bai et al., 2023
Yushi Bai, Xin Lv, Jiajie Zhang, Hongchang Lyu, Jiankai Tang, Zhidian Huang, Zhengxiao Du, Xiao Liu, Aohan Zeng, Lei Hou, et al. Longbench: A bilingual, multitask benchmark for long context understanding. *arXiv preprint arXiv:2308.14508*, 2023.

**Cited in:** 03f_contextual-hallucination-evaluation.md - Source of evaluation examples for question answering tasks [p. 9]

## Bertsch et al., 2024
Amanda Bertsch, Maor Ivgi, Uri Alon, Jonathan Berant, Matthew R. Gormley, and Graham Neubig. In-context learning with long-context models: An in-depth exploration. *arXiv:2405.00200*, 2024.

**Cited in:** 03e_in-context-learning.md - Evaluation protocol followed for many-shot in-context learning [p. 7]

## Bondarenko et al., 2024
Yelysei Bondarenko, Markus Nagel, and Tijmen Blankevoort. Quantizable transformers: Removing outliers by helping attention heads do nothing. *Advances in Neural Information Processing Systems*, 36, 2024.

**Cited in:** 03g_activation-outliers-analysis.md - Prior work on activation outliers in transformers [p. 9]

## Casanueva et al., 2020
Iñigo Casanueva, Tadas Temčinas, Daniela Gerz, Matthew Henderson, and Ivan Vulić. Efficient intent detection with dual sentence encoders. In *Proceedings of the 2nd Workshop on Natural Language Processing for Conversational AI*, pp. 38-45, 2020.

**Cited in:** 03e_in-context-learning.md - Banking-77 dataset with 77 classes [p. 7]

## Chuang et al., 2024
Yung-Sung Chuang, Linlu Qiu, Cheng-Yu Hsieh, Ranjay Krishna, Yoon Kim, and James Glass. Lookback lens: Detecting and mitigating contextual hallucinations in large language models using only attention maps. *arXiv preprint arXiv:2407.07071*, 2024.

**Cited in:** 03f_contextual-hallucination-evaluation.md - Evaluation protocol for contextual hallucination using GPT-4o judgments [p. 8]

## Cobbe et al., 2021
Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, et al. Training verifiers to solve math word problems. *arXiv preprint arXiv:2110.14168*, 2021.

**Cited in:** 08_appendix-c-mathematical-reasoning.md - GSM-8K math benchmark [p. 16]

## Dao, 2023
Tri Dao. FlashAttention-2: Faster attention with better parallelism and work partitioning. *arXiv preprint arXiv:2307.08691*, 2023.

**Cited in:** 06_appendix-a-implementation.md - FlashAttention2 base implementation [p. 15]

## Dao et al., 2022
Tri Dao, Dan Fu, Stefano Ermon, Atri Rudra, and Christopher Ré. Flashattention: Fast and memory-efficient exact attention with io-awareness. *Advances in Neural Information Processing Systems*, 35:16344-16359, 2022.

**Cited in:** 02a_differential-attention.md - FlashAttention reuse for model efficiency [p. 3]; 03g_activation-outliers-analysis.md - Opportunities for low-bit FlashAttention implementations [p. 9]; 04_conclusion.md - Easy implementation with FlashAttention [p. 10]; 06_appendix-a-implementation.md - FlashAttention implementation [p. 15]

## Dasigi et al., 2021
Pradeep Dasigi, Kyle Lo, Iz Beltagy, Arman Cohan, Noah A Smith, and Matt Gardner. A dataset of information-seeking questions and answers anchored in research papers. In *Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies*, pp. 4599-4610, 2021.

**Cited in:** 03f_contextual-hallucination-evaluation.md - Qasper single-document question answering dataset [p. 9]

## Fabbri et al., 2019
Alexander Richard Fabbri, Irene Li, Tianwei She, Suyi Li, and Dragomir Radev. Multi-news: A large-scale multi-document summarization dataset and abstractive hierarchical model. In *Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics*, pp. 1074-1084, 2019.

**Cited in:** 03f_contextual-hallucination-evaluation.md - MultiNews summarization dataset [p. 8]

## Fu et al., 2024
Yao Fu, Rameswar Panda, Xinyao Niu, Xiang Yue, Hanna Hajishirzi, Yoon Kim, and Hao Peng. Data engineering for scaling language models to 128k context. *ArXiv*, abs/2402.10171, 2024.

**Cited in:** 03c_long-context-evaluation.md - Training corpus up-sampled according to sequence length [p. 5]

## Gao et al., 2023
Leo Gao, Jonathan Tow, Baber Abbasi, Stella Biderman, Sid Black, Anthony DiPofi, Charles Foster, Laurence Golding, Jeffrey Hsu, Alain Le Noac'h, Haonan Li, Kyle McDonell, Niklas Muennighoff, Chris Ociepa, Jason Phang, Laria Reynolds, Hailey Schoelkopf, Aviya Skowron, Lintang Sutawika, Eric Tang, Anish Thite, Ben Wang, Kevin Wang, and Andy Zou. A framework for few-shot language model evaluation, 12 2023.

**Cited in:** 03a_language-modeling-evaluation.md - LM Eval Harness benchmark [p. 4]; 03g_activation-outliers-analysis.md - HellaSwag dataset for quantization evaluation [p. 9]; 07_appendix-b-language-modeling.md - LM Eval Harness benchmark [p. 16]

## Geng & Liu, 2023
Xinyang Geng and Hao Liu. OpenLLaMA: An open reproduction of LLaMA. https://github.com/openlm-research/open_llama, 2023.

**Cited in:** 03a_language-modeling-evaluation.md - OpenLLaMA-v2-3B baseline model [p. 4]

## Guo et al., 2025
Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, et al. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning. *arXiv preprint arXiv:2501.12948*, 2025.

**Cited in:** 08_appendix-c-mathematical-reasoning.md - DeepSeek-R1 for o1-style reasoning distillation [p. 16]

## Hendrycks et al., 2021
Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. Measuring mathematical problem solving with the math dataset. In *Thirty-fifth Conference on Neural Information Processing Systems Datasets and Benchmarks Track (Round 2)*, 2021.

**Cited in:** 08_appendix-c-mathematical-reasoning.md - MATH benchmark [p. 16]

## Ho et al., 2020
Xanh Ho, Anh-Khoa Duong Nguyen, Saku Sugawara, and Akiko Aizawa. Constructing a multi-hop qa dataset for comprehensive evaluation of reasoning steps. In *Proceedings of the 28th International Conference on Computational Linguistics*, pp. 6609-6625, 2020.

**Cited in:** 03f_contextual-hallucination-evaluation.md - 2WikiMultihopQA multi-document question answering dataset [p. 9]

## Hovy et al., 2001
Eduard Hovy, Laurie Gerber, Ulf Hermjakob, Chin-Yew Lin, and Deepak Ravichandran. Toward semantics-based answer pinpointing. In *Proceedings of the first international conference on Human language technology research*, 2001.

**Cited in:** 03e_in-context-learning.md - TREC dataset with 6 classes and TREC-fine with 50 classes [p. 7]

## Huang et al., 2024
Qidong Huang, Xiaoyi Dong, Pan Zhang, Bin Wang, Conghui He, Jiaqi Wang, Dahua Lin, Weiming Zhang, and Nenghai Yu. Opera: Alleviating hallucination in multi-modal large language models via over-trust penalty and retrospection-allocation. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, pp. 13418-13427, 2024.

**Cited in:** 03f_contextual-hallucination-evaluation.md - Prior work on misallocation of attention scores as cause of contextual hallucination [p. 9]

## Jaech et al., 2024
Aaron Jaech, Adam Kalai, Adam Lerer, Adam Richardson, Ahmed El-Kishky, Aiden Low, Alec Helyar, Aleksander Madry, Alex Beutel, Alex Carney, et al. Openai o1 system card. *arXiv preprint arXiv:2412.16720*, 2024.

**Cited in:** 08_appendix-c-mathematical-reasoning.md - o1-style reasoning capability [p. 16]

## Kamradt, 2023
Greg Kamradt. Needle in a Haystack - pressure testing LLMs. https://github.com/gkamradt/LLMTest_NeedleInAHaystack/tree/main, 2023.

**Cited in:** 01_introduction.md - LLMs face challenges in retrieving key information [p. 1]; 03d_key-information-retrieval.md - Needle-In-A-Haystack test [p. 6]

## Kaplan et al., 2020
Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B. Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jeffrey Wu, and Dario Amodei. Scaling laws for neural language models. *CoRR*, abs/2001.08361, 2020.

**Cited in:** 03b_scalability-compared-with-transformer.md - Scaling law fits well in this configuration [p. 5]

## Koncel-Kedziorski et al., 2016
Rik Koncel-Kedziorski, Subhro Roy, Aida Amini, Nate Kushman, and Hannaneh Hajishirzi. Mawps: A math word problem repository. In *Proceedings of the 2016 conference of the north american chapter of the association for computational linguistics: human language technologies*, pp. 1152-1157, 2016.

**Cited in:** 08_appendix-c-mathematical-reasoning.md - MAWPS math benchmark [p. 16]

## Laplante et al., 2018
Philip A Laplante, Robin Cravey, Lawrence P Dunleavy, James L Antonakos, Rodney LeRoy, Jack East, Nicholas E Buris, Christopher J Conant, Lawrence Fryda, Robert William Boyd, et al. Comprehensive dictionary of electrical engineering. CRC Press, 2018.

**Cited in:** 02a_differential-attention.md - Differential amplifiers analogy in electrical engineering [p. 3]

## Larson et al., 2019
Stefan Larson, Anish Mahendran, Joseph J Peper, Christopher Clarke, Andrew Lee, Parker Hill, Jonathan K Kummerfeld, Kevin Leach, Michael A Laurenzano, Lingjia Tang, et al. An evaluation dataset for intent classification and out-of-scope prediction. In *Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)*, pp. 1311-1316, 2019.

**Cited in:** 03e_in-context-learning.md - Clinic-150 dataset with 150 classes [p. 7]

## Li et al., 2024
Haoran Li, Qingxiu Dong, Zhengyang Tang, Chaojun Wang, Xingxing Zhang, Haoyang Huang, Shaohan Huang, Xiaolong Huang, Zeqiang Huang, Dongdong Zhang, et al. Synthetic data (almost) from scratch: Generalized instruction tuning for language models. *arXiv preprint arXiv:2402.13064*, 2024.

**Cited in:** 08_appendix-c-mathematical-reasoning.md - Synthetic math data for training [p. 16]

## Lin et al., 2023
Zhiqi Lin, Youshan Miao, Guodong Liu, Xiaoxiang Shi, Quanlu Zhang, Fan Yang, Saeed Maleki, Yi Zhu, Xu Cao, Cheng Li, Mao Yang, Lintao Zhang, and Lidong Zhou. SuperScaler: Supporting flexible DNN parallelization via a unified abstraction, 2023.

**Cited in:** 05_acknowledgement.md - CUBE internal version for long-sequence training [p. 11]

## Liu et al., 2024a
Hao Liu, Wilson Yan, Matei Zaharia, and Pieter Abbeel. World model on million-length video and language with ringattention. *arXiv preprint arXiv:2402.08268*, 2024a.

**Cited in:** 03d_key-information-retrieval.md - LWM multi-needle evaluation protocol [p. 6]

## Liu et al., 2024b
Nelson F Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, and Percy Liang. Lost in the middle: How language models use long contexts. *Transactions of the Association for Computational Linguistics*, 12:157-173, 2024b.

**Cited in:** 01_introduction.md - LLMs face challenges in retrieving key information from context [p. 1]

## Loshchilov & Hutter, 2019
Ilya Loshchilov and Frank Hutter. Decoupled weight decay regularization. In *International Conference on Learning Representations*, 2019.

**Cited in:** 03a_language-modeling-evaluation.md - AdamW optimizer [p. 4]; 10_appendix-e-hyperparameters-section-3-2.md - AdamW optimizer [p. 18]; 12_appendix-g-gradient-flow.md - AdamW invariance to gradient magnitude [p. 21]

## Lu et al., 2022
Yao Lu, Max Bartolo, Alastair Moore, Sebastian Riedel, and Pontus Stenetorp. Fantastically ordered prompts and where to find them: Overcoming few-shot prompt order sensitivity. In *Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics*, pp. 8086-8098, Dublin, Ireland, May 2022. Association for Computational Linguistics.

**Cited in:** 03e_in-context-learning.md - Prior work on Transformer being distracted by order permutations in in-context learning [p. 8]

## Lu et al., 2023
Pan Lu, Liang Qiu, Kai-Wei Chang, Ying Nian Wu, Song-Chun Zhu, Tanmay Rajpurohit, Peter Clark, and Ashwin Kalyan. Dynamic prompt learning via policy gradient for semi-structured mathematical reasoning. In *ICLR*, 2023.

**Cited in:** 08_appendix-c-mathematical-reasoning.md - TABMWP math benchmark [p. 16]

## Miao et al., 2020
Shen-Yun Miao, Chao-Chun Liang, and Keh-Yih Su. A diverse corpus for evaluating and developing english math word problem solvers. In *Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics*, pp. 975-984, 2020.

**Cited in:** 08_appendix-c-mathematical-reasoning.md - ASDiv math benchmark [p. 16]

## Naderi et al., 2024
Alireza Naderi, Thiziri Nait Saada, and Jared Tanner. Mind the gap: a spectral analysis of rank collapse and signal propagation in attention layers, 2024.

**Cited in:** 02a_differential-attention.md - Differential attention makes spectral distribution of attention matrices more balanced, resolving rank collapse [p. 3]

## Narayan et al., 2018
Shashi Narayan, Shay B Cohen, and Mirella Lapata. Don't give me the details, just the summary! topic-aware convolutional neural networks for extreme summarization. In *Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing*. Association for Computational Linguistics, 2018.

**Cited in:** 03f_contextual-hallucination-evaluation.md - XSum summarization dataset [p. 8]

## Open-R1, 2025
Open-R1. Openthoughts-114k-math, 2025. URL https://huggingface.co/datasets/open-r1/OpenThoughts-114k-math.

**Cited in:** 08_appendix-c-mathematical-reasoning.md - OpenThoughts-114K-Math dataset [p. 17]

## OpenAI, 2024
OpenAI. Hello, gpt-4o. https://openai.com/index/hello-gpt-4o, 2024.

**Cited in:** 03f_contextual-hallucination-evaluation.md - GPT-4o used for hallucination judgments [p. 8]

## OpenThoughts, 2025
OpenThoughts. Open Thoughts. https://open-thoughts.ai, January 2025.

**Cited in:** 08_appendix-c-mathematical-reasoning.md - OpenThoughts-114K dataset [p. 17]

## Patel et al., 2021
Arkil Patel, Satwik Bhattamishra, and Navin Goyal. Are nlp models really able to solve simple math word problems? In *Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies*, pp. 2080-2094, 2021.

**Cited in:** 08_appendix-c-mathematical-reasoning.md - SVAMP math benchmark [p. 16]

## Qin et al., 2022
Zhen Qin, Xiaodong Han, Weixuan Sun, Dongxu Li, Lingpeng Kong, Nick Barnes, and Yiran Zhong. The devil in linear transformer. In *Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing*, pp. 7025-7041, 2022.

**Cited in:** 02a_differential-attention.md - Headwise normalization improves gradient statistics [p. 3]

## Ramachandran et al., 2017
Prajit Ramachandran, Barret Zoph, and Quoc V. Le. Swish: a self-gated activation function. *arXiv: Neural and Evolutionary Computing*, 2017.

**Cited in:** 02_differential-transformer.md - SwiGLU activation [p. 2]; 03b_scalability-compared-with-transformer.md - SwiGLU in augmented Transformer [p. 5]; 07_appendix-b-language-modeling.md - SwiGLU activation function [p. 16]

## Ratner et al., 2023
Nir Ratner, Yoav Levine, Yonatan Belinkov, Ori Ram, Inbal Magar, Omri Abend, Ehud Karpas, Amnon Shashua, Kevin Leyton-Brown, and Yoav Shoham. Parallel context windows for large language models. In *Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics*, pp. 6383-6402, 2023.

**Cited in:** 03e_in-context-learning.md - Constrained decoding method [p. 7]

## Ravi et al., 2024
Selvan Sunitha Ravi, Bartosz Mielczarek, Anand Kannappan, Douwe Kiela, and Rebecca Qian. Lynx: An open source hallucination evaluation model. *arXiv preprint arXiv:2407.08488*, 2024.

**Cited in:** 03f_contextual-hallucination-evaluation.md - Prior work validating GPT-4o hallucination evaluation protocol [p. 8]

## Reid et al., 2024
Machel Reid, Nikolay Savinov, Denis Teplyashin, Dmitry Lepikhin, Timothy Lillicrap, Jean-baptiste Alayrac, Radu Soricut, Angeliki Lazaridou, Orhan Firat, Julian Schrittwieser, et al. Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context. *arXiv preprint arXiv:2403.05530*, 2024.

**Cited in:** 03c_long-context-evaluation.md - Cumulative average NLL evaluation method [p. 5]; 03d_key-information-retrieval.md - Gemini 1.5 multi-needle evaluation protocol [p. 6]

## See et al., 2017
Abigail See, Peter J Liu, and Christopher D Manning. Get to the point: Summarization with pointer-generator networks. In *Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics*. Association for Computational Linguistics, 2017.

**Cited in:** 03f_contextual-hallucination-evaluation.md - CNN/DM summarization dataset [p. 8]

## Shah et al., 2024
Jay Shah, Ganesh Bikshandi, Ying Zhang, Vijay Thakkar, Pradeep Ramani, and Tri Dao. Flashattention-3: Fast and accurate attention with asynchrony and low-precision. *arXiv preprint arXiv:2407.08608*, 2024.

**Cited in:** 06_appendix-a-implementation.md - FlashAttention3 improvements [p. 15]

## Shazeer, 2020
Noam Shazeer. Glu variants improve transformer. *arXiv preprint arXiv:2002.05202*, 2020.

**Cited in:** 02_differential-transformer.md - SwiGLU activation [p. 2]; 03b_scalability-compared-with-transformer.md - SwiGLU in augmented Transformer [p. 5]; 07_appendix-b-language-modeling.md - SwiGLU activation function [p. 16]

## Su et al., 2021
Jianlin Su, Yu Lu, Shengfeng Pan, Bo Wen, and Yunfeng Liu. Roformer: Enhanced transformer with rotary position embedding. *arXiv preprint arXiv:2104.09864*, 2021.

**Cited in:** 03c_long-context-evaluation.md - RoPE positional encoding [p. 5]

## Sun et al., 2024
Mingjie Sun, Xinlei Chen, J Zico Kolter, and Zhuang Liu. Massive activations in large language models. In *ICLR 2024 Workshop on Mathematical and Empirical Understanding of Foundation Models*, 2024.

**Cited in:** 03g_activation-outliers-analysis.md - Prior work on activation outliers in transformers [p. 9]

## Tang et al., 2024
Zhengyang Tang, Xingxing Zhang, Benyou Wang, and Furu Wei. Mathscale: scaling instruction tuning for mathematical reasoning. In *Proceedings of the 41st International Conference on Machine Learning*, pp. 47885-47900, 2024.

**Cited in:** 08_appendix-c-mathematical-reasoning.md - CollegeMath benchmark [p. 16]

## Touvron et al., 2023
Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, et al. Llama: Open and efficient foundation language models. *arXiv preprint arXiv:2302.13971*, 2023.

**Cited in:** 02_differential-transformer.md - Pre-RMSNorm and SwiGLU improvements following LLaMA [p. 2]; 03a_language-modeling-evaluation.md - StableLM-3B-4E1T recipe [p. 4]; 03b_scalability-compared-with-transformer.md - Augmented Transformer architecture as in LLaMA [p. 5]; 07_appendix-b-language-modeling.md - LLaMA augmented Transformer architecture [p. 16]

## Tow, 2023
Jonathan Tow. StableLM Alpha v2 models. https://huggingface.co/stabilityai/stablelm-base-alpha-3b-v2, 2023.

**Cited in:** 03a_language-modeling-evaluation.md - StableLM-base-alpha-3B-v2 baseline model [p. 4]

## Tow et al., 2023
Jonathan Tow, Marco Bellagente, Dakota Mahan, and Carlos Riquelme. StableLM 3B 4E1T. https://aka.ms/StableLM-3B-4E1T, 2023.

**Cited in:** 03a_language-modeling-evaluation.md - StableLM-3B-4E1T baseline model and training recipe [p. 4]

## Vaswani et al., 2017
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and Illia Polosukhin. Attention is all you need. In *Advances in Neural Information Processing Systems 30: Annual Conference on Neural Information Processing Systems 2017, 4-9 December 2017, Long Beach, CA, USA*, 2017.

**Cited in:** 01_introduction.md - Transformer original work [p. 1]; 02_differential-transformer.md - Conventional softmax attention comparison [p. 2]; 02a_differential-attention.md - Multi-head mechanism [p. 3]; 07_appendix-b-language-modeling.md - Transformer baseline comparison [p. 16]

## Wan et al., 2024
Zhongwei Wan, Xin Wang, Che Liu, Samiul Alam, Yu Zheng, Jiachen Liu, Zhongnan Qu, Shen Yan, Yi Zhu, Quanlu Zhang, Mosharaf Chowdhury, and Mi Zhang. Efficient large language models: A survey. *Transactions on Machine Learning Research*, 2024.

**Cited in:** 03g_activation-outliers-analysis.md - Absmax quantization method [p. 9]

## Wang et al., 2023
Hongyu Wang, Shuming Ma, Shaohan Huang, Li Dong, Wenhui Wang, Zhiliang Peng, Yu Wu, Payal Bajaj, Saksham Singhal, Alon Benhaim, et al. Magneto: A foundation Transformer. In *International Conference on Machine Learning*, pp. 36077-36092. PMLR, 2023.

**Cited in:** 02a_differential-attention.md - Headwise normalization improves gradient statistics [p. 3]

## Wu & He, 2018
Yuxin Wu and Kaiming He. Group normalization. In *Proceedings of the European conference on computer vision (ECCV)*, pp. 3-19, 2018.

**Cited in:** 02a_differential-attention.md - GroupNorm applied to each head independently [p. 3]

## Yang et al., 2018
Zhilin Yang, Peng Qi, Saizheng Zhang, Yoshua Bengio, William Cohen, Ruslan Salakhutdinov, and Christopher D Manning. Hotpotqa: A dataset for diverse, explainable multi-hop question answering. In *Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing*, pp. 2369-2380, 2018.

**Cited in:** 03f_contextual-hallucination-evaluation.md - HotpotQA multi-document question answering dataset [p. 9]

## Zhang & Sennrich, 2019
Biao Zhang and Rico Sennrich. Root mean square layer normalization. *Advances in Neural Information Processing Systems*, 32, 2019.

**Cited in:** 02_differential-transformer.md - Pre-RMSNorm [p. 2]; 02a_differential-attention.md - RMSNorm for LN in multi-head attention [p. 3]; 02b_overall-architecture.md - RMSNorm [p. 4]; 03b_scalability-compared-with-transformer.md - RMSNorm in augmented Transformer [p. 5]; 07_appendix-b-language-modeling.md - RMSNorm normalization method [p. 16]

## Zhang et al., 2023
Beichen Zhang, Kun Zhou, Xilin Wei, Xin Zhao, Jing Sha, Shijin Wang, and Ji-Rong Wen. Evaluating and improving tool-augmented computation-intensive math reasoning. *Advances in Neural Information Processing Systems*, 36:23570-23589, 2023.

**Cited in:** 08_appendix-c-mathematical-reasoning.md - CARP math benchmark [p. 16]
