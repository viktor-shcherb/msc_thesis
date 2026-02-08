# References

[1] Joshua Ainslie, James Lee-Thorp, Michiel de Jong, Yury Zemlyanskiy, Federico Lebron, and Sumit Sanghai. GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints. *arXiv preprint arXiv:2305.13245*, 2023.
- Cited in 01_introduction.md, 02_pretraining.md, 06_evaluations.md as the GQA attention mechanism used in Yi architecture.

[2] Jacob Austin, Augustus Odena, Maxwell Nye, Maarten Bosma, Henryk Michalewski, David Dohan, Ellen Jiang, Carrie Cai, Michael Terry, Quoc Le, et al. Program Synthesis With ILarge Language Models. *arXiv preprint arXiv:2108.07732*, 2021.
- Cited in 06_evaluations.md as the MBPP code benchmark.

[3] Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Kai Dang, Xiaodong Deng, Yang Fan, Wenbin Ge, Yu Han, Fei Huang, et al. Qwen Technical Report. 09 2023.
- Cited in 01_introduction.md as Qwen, a related model using similar architecture.

[4] Yonatan Bisk, Rowan Zellers, Ronan Le Bras, Jianfeng Gao, and Yejin Choi. PIQA: Reasoning about Physical Commonsense in Natural Language. *ArXiv*, abs/1911.11641, 2019.
- Cited in 06_evaluations.md as a commonsense reasoning benchmark.

[5] Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. Language models are few-shot learners. *Advances in neural information processing systems*, 33:1877-1901, 2020.
- Cited in 05_safety.md as a standard pretraining data safety practice reference.

[6] Lin Chen, Jisong Li, Xiaoyi Dong, Pan Zhang, Conghui He, Jiaqi Wang, Feng Zhao, and Dahua Lin. Sharegpt4v: Improving large multi-modal models with better captions. *arXiv preprint arXiv:2311.12793*, 2023.
- Cited in 07_capability-extension.md as a data source for Yi-VL Stage 3 training.

[7] Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde de Oliveira Pinto, Jared Kaplan, et al. Evaluating Large Language Models Trained on Code. *CoRR*, abs/2107.03374, 2021.
- Cited in 06_evaluations.md as the HumanEval code benchmark.

[8] Eunsol Choi, He He, Mohit Iyyer, Mark Yatskar, Wen tau Yih, Yejin Choi, Percy Liang, and Luke Zettlemoyer. QuAC: Question Answering in Context, 2018.
- Cited in 06_evaluations.md as a reading comprehension benchmark.

[9] Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Yunxuan Li, Xuezhi Wang, Mostafa Dehghani, Siddhartha Brahma, et al. Scaling instruction-finetuned language models. *arXiv preprint arXiv:2210.11416*, 2022.
- Cited in 01_introduction.md, 03_finetuning.md, 08_final-discussions.md as the FLAN instruction-scaling approach that Yi's finetuning deviates from.

[10] Christopher Clark, Kenton Lee, Ming-Wei Chang, Tom Kwiatkowski, Michael Collins, and Kristina Toutanova. BoolQ: Exploring the Surprising Difficulty of Natural Yes/No Questions, 2019.
- Cited in 06_evaluations.md as a reading comprehension benchmark.

[11] Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar Khot, Ashish Sabharwal, Carissa Schoenick, and Oyvind Tafjord. Think you have Solved Question Answering? Try ARC, the AI2 Reasoning Challenge, 2018.
- Cited in 06_evaluations.md as a commonsense reasoning benchmark (ARC).

[12] Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, et al. Training Verifiers to Solve Math Word Problems. *arXiv preprint arXiv:2110.14168*, 2021.
- Cited in 06_evaluations.md as the GSM8K math benchmark.

[13] Together Computer. Redpajama: an open dataset for training large language models, 2023.
- Cited in 01_introduction.md as an existing data pipeline that Yi's cleaning produces higher removal ratio than.

[14] Tri Dao. FlashAttention-2: Faster attention with better parallelism and work partitioning. 2023.
- Cited in 04_infrastructure.md as a kernel fusion technique for reducing memory access.

[15] Tri Dao, Daniel Y. Fu, Stefano Ermon, Atri Rudra, and Christopher Re. FlashAttention: Fast and memory-efficient exact attention with IO-awareness. In *Advances in Neural Information Processing Systems*, 2022.
- Cited in 04_infrastructure.md as a kernel fusion technique for reducing memory access.

[16] Michiel de Jong, Yury Zemlyanskiy, Joshua Ainslie, Nicholas FitzGerald, Sumit Sanghai, Fei Sha, and William Cohen. FiDO: Fusion-in-Decoder Optimized for Stronger Performance and Faster Inference. *arXiv preprint arXiv:2212.08153*, 2022.
- Cited in 02_pretraining.md as a reference for Multi-Head Attention alternatives.

[17] DeepSeek-AI, Xiao Bi, Deli Chen, Guanting Chen, Shanhuang Chen, Damai Dai, et al. Deepseek llm: Scaling open-source language models with longtermism. 2024.
- Cited in 07_capability-extension.md for highlighting that computational budget allocation towards model scaling should be proportional to data quality.

[18] Tim Dettmers, Mike Lewis, Younes Belkada, and Luke Zettlemoyer. Llm. int8 (): 8-bit matrix multiplication for transformers at scale. *arXiv preprint arXiv:2208.07339*, 2022.
- Cited in 04_infrastructure.md for 8-bit KV cache quantization.

[19] Ning Ding, Yulin Chen, Bokai Xu, Yujia Qin, Zhi Zheng, Shengding Hu, Zhiyuan Liu, Maosong Sun, and Bowen Zhou. Enhancing chat language models by scaling high-quality instructional conversations. *arXiv preprint arXiv:2305.14233*, 2023.
- Cited in 01_introduction.md, 03_finetuning.md, 06_evaluations.md, 08_final-discussions.md as UltraChat, a data-intensive instruction tuning approach that Yi's finetuning deviates from.

[20] Guanting Dong, Hongyi Yuan, Keming Lu, Chengpeng Li, Mingfeng Xue, Dayiheng Liu, Wei Wang, Zheng Yuan, Chang Zhou, and Jingren Zhou. How abilities in large language models are affected by supervised fine-tuning data composition, 2023.
- Cited in 03_finetuning.md as motivation for the grid search approach to data mixture ratios.

[21] Yann Dubois, Xuechen Li, Rohan Taori, Tianyi Zhang, Ishaan Gulrajani, Jimmy Ba, Carlos Guestrin, Percy Liang, and Tatsunori B. Hashimoto. Alpacafarm: A simulation framework for methods that learn from human feedback, 2023.
- Cited in 06_evaluations.md as Davinci003 reference replies used in AlpacaEval.

[22] Yao Fu, Rameswar Panda, Xinyao Niu, Xiang Yue, Hannaneh Hajishirzi, Yoon Kim, and Hao Peng. Data engineering for scaling language models to 128k context. *arXiv preprint arXiv:2402.10171*, 2024.
- Cited in 01_introduction.md, 07_capability-extension.md as a concurrent work on long-context data engineering that Yi's context scaling approach follows.

[23] Gemini Gemini Team, Rohan Anil, Sebastian Borgeaud, Yonghui Wu, Jean-Baptiste Alayrac, Jiahui Yu, Radu Soricut, Johan Schalkwyk, Andrew M Dai, Anja Hauth, et al. Gemini: A family of highly capable multimodal models. *arXiv preprint arXiv:2312.11805*, 2023.
- Cited in 03_finetuning.md as supporting the observation that smaller, high-quality datasets yield superior results.

[24] Amelia Glaese, Nat McAleese, Maja Trebacz, John Aslanides, Vlad Firoiu, Timo Ewalds, Maribeth Rauh, Laura Weidinger, Martin Chadwick, Phoebe Thacker, et al. Improving alignment of dialogue agents via targeted human judgements. *arXiv preprint arXiv:2209.14375*, 2022.
- Cited in 05_safety.md as informing the safety taxonomy.

[25] Yash Goyal, Tejas Khot, Douglas Summers-Stay, Dhruv Batra, and Devi Parikh. Making the v in vqa matter: Elevating the role of image understanding in visual question answering. In *Proceedings of the IEEE conference on computer vision and pattern recognition*, pages 6904-6913, 2017.
- Cited in 07_capability-extension.md as a data source (VQAv2) for Yi-VL Stage 2 training.

[26] Danna Gurari, Qing Li, Abigale J Stangl, Anhong Guo, Chi Lin, Kristen Grauman, Jiebo Luo, and Jeffrey P Bigham. Vizwiz grand challenge: Answering visual questions from blind people. In *Proceedings of the IEEE conference on computer vision and pattern recognition*, pages 3608-3617, 2018.
- Cited in 07_capability-extension.md as a data source (VizWiz VQA) for Yi-VL Stage 3 training.

[27] Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn Song, and Jacob Steinhardt. Measuring Massive Multitask Language Understanding. *CoRR*, abs/2009.03300, 2020.
- Cited in 01_introduction.md, 06_evaluations.md as the MMLU benchmark.

[28] Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. Measuring Mathematical Problem Solving With the MATH Dataset. *arXiv preprint arXiv:2103.03874*, 2021.
- Cited in 06_evaluations.md as the MATH benchmark.

[29] Tom Henighan, Jared Kaplan, Mor Katz, Mark Chen, Christopher Hesse, Jacob Jackson, Heewoo Jun, Tom B. Brown, Prafulla Dhariwal, Scott Gray, Chris Hallacy, Benjamin Mann, Alec Radford, Aditya Ramesh, Nick Ryder, Daniel M. Ziegler, John Schulman, Dario Amodei, and Sam McCandlish. Scaling laws for autoregressive generative modeling. 2020.
- Cited in 07_capability-extension.md as a scaling laws study motivating depth upscaling.

[30] Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, et al. Training compute-optimal large language models. *arXiv preprint arXiv:2203.15556*, 2022.
- Cited in 01_introduction.md as Chinchilla; in 07_capability-extension.md as a scaling laws reference.

[31] Yuzhen Huang, Yuzhuo Bai, Zhihao Zhu, Junlei Zhang, Jinghan Zhang, Tangjun Su, Junteng Liu, Chuancheng Lv, Yikai Zhang, Jiayi Lei, et al. C-eval: A multi-level multi-discipline chinese evaluation suite for foundation models. *arXiv preprint arXiv:2305.08322*, 2023.
- Cited in 06_evaluations.md as the C-Eval Chinese benchmark.

[32] Drew A Hudson and Christopher D Manning. Gqa: A new dataset for real-world visual reasoning and compositional question answering. In *Proceedings of the IEEE/CVF conference on computer vision and pattern recognition*, pages 6700-6709, 2019.
- Cited in 07_capability-extension.md as a data source (GQA) for Yi-VL Stage 3 training.

[33] Gabriel Ilharco, Mitchell Wortsman, Ross Wightman, Cade Gordon, Nicholas Carlini, Rohan Taori, Achal Dave, Vaishaal Shankar, Hongseok Namkoong, John Miller, Hannaneh Hajishirzi, Ali Farhadi, and Ludwig Schmidt. Openclip, July 2021.
- Cited in 07_capability-extension.md as the CLIP ViT-H/14 model used to initialize the Vision Transformer.

[34] Neel Jain, Ping-yeh Chiang, Yuxin Wen, John Kirchenbauer, Hong-Min Chu, Gowthami Somepalli, Brian R Bartoldson, Bhavya Kailkhura, Avi Schwarzschild, Aniruddha Saha, et al. Neftune: Noisy embeddings improve instruction finetuning. *arXiv preprint arXiv:2310.05914*, 2023.
- Cited in 03_finetuning.md as the NEFTune technique used during training.

[35] Jiaming Ji, Mickel Liu, Juntao Dai, Xuehai Pan, Chi Zhang, Ce Bian, Chi Zhang, Ruiyang Sun, Yizhou Wang, and Yaodong Yang. Beavertails: Towards improved safety alignment of llm via a human-preference dataset, 2023.
- Cited in 05_safety.md as informing the safety taxonomy.

[36] Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B. Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jeffrey Wu, and Dario Amodei. Scaling laws for neural language models. 2020.
- Cited in 07_capability-extension.md as a scaling laws study motivating depth upscaling.

[37] Sahar Kazemzadeh, Vicente Ordonez, Mark Matten, and Tamara Berg. Referitgame: Referring to objects in photographs of natural scenes. In *Proceedings of the 2014 conference on empirical methods in natural language processing (EMNLP)*, pages 787-798, 2014.
- Cited in 07_capability-extension.md as a data source (RefCOCO) for Yi-VL Stage 2 training.

[38] Dahyun Kim, Chanjun Park, Sanghoon Kim, Wonsung Lee, Wonho Song, Yunsu Kim, Hyeonwoo Kim, Yungi Kim, Hyeonju Lee, Jihoo Kim, Changbae Ahn, Seonghoon Yang, Sukyung Lee, Hyunbyung Park, Gyoungjin Gim, Mikyoung Cha, Hwalsuk Lee, and Sunghun Kim. Solar 10.7b: Scaling large language models with simple yet effective depth up-scaling. 2023.
- Cited in 01_introduction.md, 07_capability-extension.md as the depth up-scaling methodology that Yi-9B follows.

[39] Ranjay Krishna, Yuke Zhu, Oliver Groth, Justin Johnson, Kenji Hata, Joshua Kravitz, Stephanie Chen, Yannis Kalantidis, Li-Jia Li, David A Shamma, et al. Visual genome: Connecting language and vision using crowdsourced dense image annotations. *International journal of computer vision*, 123:32-73, 2017.
- Cited in 07_capability-extension.md as a data source (Visual Genome) for Yi-VL Stage 3 training.

[40] Taku Kudo and John Richardson. SentencePiece: A Simple and Language Independent Subword Tokenizer and Detokenizer for Neural Text Processing. *arXiv preprint arXiv:1808.06226*, 2018.
- Cited in 02_pretraining.md as the tokenization framework used by Yi.

[41] Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu, Joseph E. Gonzalez, Hao Zhang, and Ion Stoica. Efficient Memory Management for Large Language Model Serving with PagedAttention. *arXiv preprint arXiv:2309.06180*, 2023.
- Cited in 01_introduction.md, 04_infrastructure.md as the PagedAttention technique for efficient inference.

[42] Haonan Li, Yixuan Zhang, Fajri Koto, Yifei Yang, Hai Zhao, Yeyun Gong, Nan Duan, and Timothy Baldwin. CMMLU: Measuring Massive Multitask Language Understanding in Chinese. *arXiv preprint arXiv:2306.09212*, 2023.
- Cited in 06_evaluations.md as the CMMLU Chinese benchmark.

[43] Shenggui Li, Fuzhao Xue, Chaitanya Baranwal, Yongbin Li, and Yang You. Sequence parallelism: Long sequence training from system perspective. *arXiv preprint arXiv:2105.13120*, 2021.
- Cited in 07_capability-extension.md for sequence parallelism used in long-context continual pretraining.

[44] Xuechen Li, Tianyi Zhang, Yann Dubois, Rohan Taori, Ishaan Gulrajani, Carlos Guestrin, Percy Liang, and Tatsunori B. Hashimoto. Alpacaeval: An automatic evaluator of instruction-following models. 2023.
- Cited in 06_evaluations.md as the AlpacaEval evaluation platform.

[45] LinkSoul-AI. Chinese llava. https://github.com/LinkSoul-AI/Chinese-LLaVA, 2023.
- Cited in 07_capability-extension.md as a data source (CLLaVA) for Yi-VL Stage 2 training.

[46] Haotian Liu, Chunyuan Li, Yuheng Li, and Yong Jae Lee. Improved baselines with visual instruction tuning. *arXiv preprint arXiv:2310.03744*, 2023.
- Cited in 07_capability-extension.md as inspiration (LLaVA) for the Yi-VL architecture.

[47] Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee. Visual instruction tuning. *arXiv preprint arXiv:2304.08485*, 2023.
- Cited in 01_introduction.md, 07_capability-extension.md as the LLaVA method that Yi-VL follows and improves upon.

[48] Wei Liu, Weihao Zeng, Keqing He, Yong Jiang, and Junxian He. What makes good data for alignment? a comprehensive study of automatic data selection in instruction tuning. *arXiv preprint arXiv:2312.15685*, 2023.
- Cited in 03_finetuning.md as DEITA, a data-selection approach that aligns with Yi's finetuning philosophy.

[49] Keming Lu, Hongyi Yuan, Zheng Yuan, Runji Lin, Junyang Lin, Chuanqi Tan, Chang Zhou, and Jingren Zhou. #instag: Instruction tagging for analyzing supervised fine-tuning of large language models, 2023.
- Cited in 03_finetuning.md as InsTag, inspiring the instruction tagging system for diversity.

[50] Todor Mihaylov, Peter Clark, Tushar Khot, and Ashish Sabharwal. Can a Suit of Armor Conduct Electricity? A New Dataset for Open Book Question Answering, 2018.
- Cited in 06_evaluations.md as the OpenBookQA benchmark.

[51] Anand Mishra, Shashank Shekhar, Ajeet Kumar Singh, and Anirban Chakraborty. Ocr-vqa: Visual question answering by reading text in images. In *2019 international conference on document analysis and recognition (ICDAR)*, pages 947-952. IEEE, 2019.
- Cited in 07_capability-extension.md as a data source (OCR-VQA) for Yi-VL Stage 3 training.

[52] Thuat Nguyen, Chien Van Nguyen, Viet Dac Lai, Hieu Man, Nghia Trung Ngo, Franck Dernoncourt, Ryan A Rossi, and Thien Huu Nguyen. CulturaX: A Cleaned, Enormous, and Multilingual Dataset for Large Language Models in 167 Languages. *arXiv preprint arXiv:2309.09400*, 2023.
- Cited in 02_pretraining.md for filtering thresholds based on statistical analysis.

[53] OpenAI. ChatML, 2022.
- Cited in 03_finetuning.md as the ChatML-style format used for data formatting.

[54] Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al. Training Language Models to Follow Instructions with Human Feedback. *Advances in Neural Information Processing Systems*, 35:27730-27744, 2022.
- Cited in 04_infrastructure.md as PPO, used in the finetuning framework for multi-model orchestration.

[55] Keiran Paster. Testing language models on a held-out high school national finals exam. 2023.
- Cited in 06_evaluations.md as the Hungarian high school mathematics exam evaluation.

[56] Guilherme Penedo, Quentin Malartic, Daniel Hesslow, Ruxandra Cojocaru, Alessandro Cappelli, Hamza Alobeidli, Baptiste Pannier, Ebtesam Almazrouei, and Julien Launay. The RefinedWeb Dataset for Falcon LLM: Outperforming Curated Corpora with Web Data, and Web Data Only, 2023.
- Cited in 01_introduction.md, 02_pretraining.md as RefinedWeb/Falcon, an existing data pipeline that Yi improves upon.

[57] Reiner Pope, Sholto Douglas, Aakanksha Chowdhery, Jacob Devlin, James Bradbury, Jonathan Heek, Kefan Xiao, Shivani Agrawal, and Jeff Dean. Efficiently Scaling Transformer Inference. *Proceedings of Machine Learning and Systems*, 5, 2023.
- Cited in 02_pretraining.md as a reference for Multi-Head Attention alternatives.

[58] Jack W Rae, Sebastian Borgeaud, Trevor Cai, Katie Millican, Jordan Hoffmann, Francis Song, John Aslanides, Sarah Henderson, Roman Ring, Susannah Young, et al. Scaling Language Models: Methods, Analysis & Insights from Training Gopher. *arXiv preprint arXiv:2112.11446*, 2021.
- Cited in 02_pretraining.md for repeated text filtering; in 05_safety.md as a standard pretraining data safety practice.

[59] Rafael Rafailov, Archit Sharma, Eric Mitchell, Stefano Ermon, Christopher D Manning, and Chelsea Finn. Direct preference optimization: Your language model is secretly a reward model. *arXiv preprint arXiv:2305.18290*, 2023.
- Cited in 04_infrastructure.md as the DPO method supported by the finetuning framework.

[60] Samyam Rajbhandari, Jeff Rasley, Olatunji Ruwase, and Yuxiong He. ZeRO: Memory Optimizations Toward Training Trillion Parameter Models. In *SC20: International Conference for High Performance Computing, Networking, Storage and Analysis*, pages 1-16. IEEE, 2020.
- Cited in 01_introduction.md, 04_infrastructure.md as ZeRO-1 for memory optimization via optimizer state partitioning.

[61] Pranav Rajpurkar, Jian Zhang, Konstantin Lopyrev, and Percy Liang. SQuAD: 100,000+ Questions for Machine Comprehension of Text, 2016.
- Cited in 06_evaluations.md as a reading comprehension benchmark.

[62] Keisuke Sakaguchi, Ronan Le Bras, Chandra Bhagavatula, and Yejin Choi. WinoGrande: An Adversarial Winograd Schema Challenge at Scale, 2019.
- Cited in 06_evaluations.md as a commonsense reasoning benchmark.

[63] Maarten Sap, Hannah Rashkin, Derek Chen, Ronan LeBras, and Yejin Choi. SocialIQA: Commonsense Reasoning about Social Interactions, 2019.
- Cited in 06_evaluations.md as a commonsense reasoning benchmark (SIQA).

[64] Nikhil Sardana and Jonathan Frankle. Beyond chinchilla-optimal: Accounting for inference in language model scaling laws. *arXiv preprint arXiv:2401.00448*, 2023.
- Cited in 01_introduction.md as the post-Chinchilla optimal regime that justifies overtraining on more tokens.

[65] Rylan Schaeffer, Brando Miranda, and Sanmi Koyejo. Are emergent abilities of large language models a mirage? *Advances in Neural Information Processing Systems*, 36, 2024.
- Cited in 06_evaluations.md regarding discussions of whether emergent ability is an artifact of measurement.

[66] Christoph Schuhmann, Richard Vencu, Romain Beaumont, Robert Kaczmarczyk, Clayton Mullis, Aarush Katta, Theo Coombes, Jenia Jitsev, and Aran Komatsuzaki. Laion-400m: Open dataset of clip-filtered 400 million image-text pairs. *arXiv preprint arXiv:2111.02114*, 2021.
- Cited in 07_capability-extension.md as the LAION-400M dataset used in Yi-VL Stage 1 and 2 training.

[67] Noam Shazeer. Fast Transformer Decoding: One Write-Head is All You Need. *arXiv preprint arXiv:1911.02150*, 2019.
- Cited in 02_pretraining.md as a reference for Multi-Head Attention alternatives.

[68] Noam Shazeer. GLU Variants Improve Transformer. *arXiv preprint arXiv:2002.05202*, 2020.
- Cited in 01_introduction.md, 02_pretraining.md as the SwiGLU activation function used in Yi.

[69] Yusuxke Shibata, Takuya Kida, Shuichi Fukamachi, Masayuki Takeda, Ayumi Shinohara, Takeshi Shinohara, and Setsuo Arikawa. Byte Pair Encoding: A Text Compression Scheme That Accelerates Pattern Matching. Technical report, Technical Report DOI-TR-161, Department of Informatics, Kyushu University, 1999.
- Cited in 02_pretraining.md as the BPE tokenization algorithm.

[70] Mohammad Shoeybi, Mostofa Patwary, Raul Puri, Patrick LeGresley, Jared Casper, and Bryan Catanzaro. Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism. *arXiv preprint arXiv:1909.08053*, 2019.
- Cited in 01_introduction.md, 04_infrastructure.md as Megatron, used for tensor/pipeline parallel training.

[71] Oleksii Sidorov, Ronghang Hu, Marcus Rohrbach, and Amanpreet Singh. Textcaps: a dataset for image captioning with reading comprehension. In *Computer Vision--ECCV 2020*, pages 742-758. Springer, 2020.
- Cited in 07_capability-extension.md as a data source (TextCaps) for Yi-VL Stage 3 training.

[72] Aarohi Srivastava, Abhinav Rastogi, Abhishek Rao, et al. Beyond the Imitation Game: Quantifying and Extrapolating the Capabilities of Language Models, 2023.
- Cited in 06_evaluations.md as the BigBench benchmark.

[73] Jianlin Su, Yu Lu, Shengfeng Pan, Ahmed Murtadha, Bo Wen, and Yunfeng Liu. Roformer: Enhanced Transformer with Rotary Position Embedding. *arXiv preprint arXiv:2104.09864*, 2021.
- Cited in 02_pretraining.md as the RoPE positional embedding used in Yi.

[74] Mirac Suzgun, Nathan Scales, Nathanael Scharli, Sebastian Gehrmann, Yi Tay, Hyung Won Chung, Aakanksha Chowdhery, Quoc V Le, Ed H Chi, Denny Zhou, et al. Challenging Big-Bench Tasks and Whether Chain-of-Thought can Solve Them. *arXiv preprint arXiv:2210.09261*, 2022.
- Cited in 06_evaluations.md as the BBH (BIG-Bench Hard) benchmark.

[75] Alon Talmor, Jonathan Herzig, Nicholas Lourie, and Jonathan Berant. CommonsenseQA: A Question Answering Challenge Targeting Commonsense Knowledge, 2019.
- Cited in 06_evaluations.md as a commonsense reasoning benchmark (CSQA).

[76] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothee Lacroix, Baptiste Roziere, Naman Goyal, Eric Hambro, Faisal Azhar, et al. Llama: Open and efficient foundation language models. *arXiv preprint arXiv:2302.13971*, 2023.
- Cited in 02_pretraining.md as LLaMA, whose data mixture is compared to Yi's.

[77] Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, et al. Llama 2: Open Foundation and Fine-Tuned Chat Models, 2023.
- Cited in 01_introduction.md, 02_pretraining.md, 03_finetuning.md, 05_safety.md, 06_evaluations.md as LLaMA 2, which Yi's architecture is based on and compared against.

[78] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and Illia Polosukhin. Attention Is All You Need. *Advances in Neural Information Processing Systems*, 06 2017.
- Cited in 01_introduction.md, 02_pretraining.md as the original Transformer architecture paper.

[79] Guillaume Wenzek, Marie-Anne Lachaux, Alexis Conneau, Vishrav Chaudhary, Francisco Guzman, Armand Joulin, and Edouard Grave. CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data. *arXiv preprint arXiv:1911.00359*, 11 2019.
- Cited in 02_pretraining.md as the CCNet pipeline used for language identification and perplexity scoring.

[80] Guillaume Wenzek, Marie-Anne Lachaux, Alexis Conneau, Vishrav Chaudhary, Francisco Guzman, Armand Joulin, and Edouard Grave. CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data. *arXiv preprint arXiv:1911.00359*, 2019.
- Cited in 01_introduction.md, 02_pretraining.md as CCNet, an existing data pipeline that Yi's cleaning improves upon.

[81] Xiaoxia Wu, Cheng Li, Reza Yazdani Aminabadi, Zhewei Yao, and Yuxiong He. Understanding int4 quantization for transformer models: Latency speedup, composability, and failure cases. *arXiv preprint arXiv:2301.12017*, 2023.
- Cited in 01_introduction.md, 04_infrastructure.md for 4-bit model quantization enabling consumer-grade deployment.

[82] Wenhan Xiong, Jingyu Liu, Igor Molybog, Hejia Zhang, Prajjwal Bhargava, Rui Hou, Louis Martin, Rashi Rungta, Karthik Abinav Sankararaman, Barlas Oguz, et al. Effective long-context scaling of foundation models. *arXiv preprint arXiv:2309.16039*, 2023.
- Cited in 01_introduction.md, 02_pretraining.md as the RoPE ABF (adjusted base frequency) method for long context.

[83] Can Xu, Qingfeng Sun, Kai Zheng, Xiubo Geng, Pu Zhao, Jiazhan Feng, Chongyang Tao, and Daxin Jiang. Wizardlm: Empowering large language models to follow complex instructions. *arXiv preprint arXiv:2304.12244*, 2023.
- Cited in 03_finetuning.md as WizardLM, inspiring compound instruction development.

[84] Aiyuan Yang, Bin Xiao, Bingning Wang, Borong Zhang, Ce Bian, Chao Yin, Chenxu Lv, et al. Baichuan 2: Open Large-scale Language Models. 09 2023.
- Cited in 01_introduction.md as Baichuan, a related model using similar architecture.

[85] Peter Young, Alice Lai, Micah Hodosh, and Julia Hockenmaier. From image descriptions to visual denotations: New similarity metrics for semantic inference over event descriptions. *Transactions of the Association for Computational Linguistics*, 2:67-78, 2014.
- Cited in 07_capability-extension.md as a data source (Flickr) for Yi-VL Stage 2 training.

[86] Gyeong-In Yu, Joo Seong Jeong, Geon-Woo Kim, Soojeong Kim, and Byung-Gon Chun. Orca: A Distributed Serving System for Transformer-Based Generative Models. In *16th USENIX Symposium on Operating Systems Design and Implementation (OSDI 22)*, pages 521-538, 2022.
- Cited in 04_infrastructure.md for dynamic batching.

[87] Yijiong Yu, Zhe Zhou, Zhixiao Qi, and Yongfeng Huang. Paraphrasing the original text makes high accuracy long-context qa. *arXiv preprint arXiv:2312.11193*, 2023.
- Cited in 07_capability-extension.md as a data engineering practice followed for long-context training.

[88] Ji Yunjie, Deng Yong, Gong Yan, Peng Yiping, Niu Qiang, Zhang Lei, Ma Baochang, and Li Xiangang. Exploring the impact of instruction data scaling on large language models: An empirical study on real-world use cases. *arXiv preprint arXiv:2303.14742*, 2023.
- Cited in 06_evaluations.md as Belle-eval, an open-source evaluation dataset.

[89] Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali Farhadi, and Yejin Choi. HellaSwag: Can a Machine Really Finish Your Sentence?, 2019.
- Cited in 06_evaluations.md as a commonsense reasoning benchmark.

[90] Xiaotian Zhang, Chunyang Li, Yi Zong, Zhengyu Ying, Liang He, and Xipeng Qiu. Evaluating the Performance of Large Language Models on GAOKAO Benchmark. *arXiv preprint arXiv:2305.12474*, 2023.
- Cited in 06_evaluations.md as the Gaokao-Bench Chinese benchmark.

[91] Yanzhe Zhang, Ruiyi Zhang, Jiuxiang Gu, Yufan Zhou, Nedim Lipka, Diyi Yang, and Tong Sun. Llavar: Enhanced visual instruction tuning for text-rich image understanding. *arXiv preprint arXiv:2306.17107*, 2023.
- Cited in 07_capability-extension.md as a data source (LLaVAR) for Yi-VL Stage 2 training.

[92] Huaixiu Steven Zheng, Swaroop Mishra, Xinyun Chen, Heng-Tze Cheng, Ed H. Chi, Quoc V Le, and Denny Zhou. Take a step back: Evoking reasoning via abstraction in large language models, 2023.
- Cited in 03_finetuning.md as inspiring the "Step-Back" CoT data formatting pattern.

[93] Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric. P Xing, Hao Zhang, Joseph E. Gonzalez, and Ion Stoica. Judging llm-as-a-judge with mt-bench and chatbot arena, 2023.
- Cited in 01_introduction.md, 06_evaluations.md as the LMSys Chatbot Arena / MT-Bench evaluation platform.

[94] Chunting Zhou, Pengfei Liu, Puxin Xu, Srini Iyer, Jiao Sun, Yuning Mao, Xuezhe Ma, Avia Efrat, Ping Yu, Lili Yu, Susan Zhang, Gargi Ghosh, Mike Lewis, Luke Zettlemoyer, and Omer Levy. Lima: Less is more for alignment, 2023.
- Cited in 01_introduction.md, 03_finetuning.md as LIMA, the handcrafting-style finetuning approach that Yi aligns with.

[95] Yuke Zhu, Oliver Groth, Michael Bernstein, and Li Fei-Fei. Visual7w: Grounded question answering in images. In *Proceedings of the IEEE conference on computer vision and pattern recognition*, pages 4995-5004, 2016.
- Cited in 07_capability-extension.md as a data source (Visual7w) for Yi-VL Stage 2 training.
