# References

This file contains only the references that were cited in the section notes.

## Main Citations from Sections

### From Introduction (01_introduction.md)

**Hao et al., 2022**: Not visible in provided pages

**Chen et al., 2023a**: Shouyuan Chen, Sherman Wong, Liangjian Chen, and Yuandong Tian. Extending context window of large language models via positional interpolation. ArXiv, abs/2306.15595, 2023a. URL https://api.semanticscholar.org/CorpusID:259262376.
- Cited as one of the methods for extending context window via positional interpolation

**Peng et al., 2023a**: Not fully visible in provided pages (refers to RWKV architecture)

**Peng et al., 2023b**: Not fully visible in provided pages

**Ratner et al., 2023**: Not visible in provided pages

**Xiong et al., 2023**: Not visible in provided pages

**Xiao et al., 2024**: Not visible in provided pages

**Jin et al., 2024**: Not visible in provided pages

**Press et al., 2022**: Ofir Press, Noah A Smith, and Mike Lewis. Train short, test long: Attention with linear biases enables input length extrapolation. 2022.
- Cited as the ALiBi embeddings approach for training with short sequences and applying to longer sequences

**Su et al., 2024**: Reference to RoPE embeddings

**Fu et al., 2024**: Yao Fu, Rameswar Panda, Xinyao Niu, Xiang Yue, Hannaneh Hajishirzi, Yoon Kim, and Hao Peng. Data engineering for scaling language models to 128k context. arXiv preprint arXiv:2402.10171, 2024.
- Cited as one of the approaches helping models extrapolate to 128K window size

**Lin et al., 2024**: Not visible in provided pages

**Ding et al., 2024**: Yiran Ding, Li Lyna Zhang, Chengruidong Zhang, Yuanyuan Xu, Ning Shang, Jiahang Xu, Fan Yang, and Mao Yang. Longrope: Extending llm context window beyond 2 million tokens. arXiv preprint arXiv:2402.13753, 2024.
- Cited as extending context window to 2M tokens

**Orvieto et al., 2023**: Not visible in provided pages

**Gu & Dao, 2023**: Reference to Mamba architecture - one of the RNN-like architectures to decrease attention complexity
- Cited in Table 2 and discussion of non-Transformer models

**Chen et al., 2023b**: Yukang Chen, Shengju Qian, Haotian Tang, Xin Lai, Zhijian Liu, Song Han, and Jiaya Jia. Longlora: Efficient fine-tuning of long-context large language models. In The Twelfth International Conference on Learning Representations, 2023b.
- Cited as incorporating techniques into open-source LLMs

**Tworkowski et al., 2023**: Not fully visible in provided pages

**Mohtashami & Jaggi, 2023**: Not visible in provided pages

**Li et al., 2023a**: Not visible in provided pages

**Team et al., 2023**: Not visible in provided pages

**Dasigi et al., 2021**: Pradeep Dasigi, Kyle Lo, Iz Beltagy, Arman Cohan, Noah A Smith, and Matt Gardner. A dataset of information-seeking questions and answers anchored in research papers. In Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, pp. 4599–4610, 2021.
- Cited as the Qasper dataset for long document QA

**Nallapat et al., 2017**: Not visible in provided pages

**Anil et al., 2022**: Cem Anil, Yuhuai Wu, Anders Johan Andreassen, Aitor Lewkowycz, Vedant Misra, Vinay Venkatesh Ramasesh, Ambrose Slone, Guy Gur-Ari, Ethan Dyer, and Behnam Neyshabur. Exploring length generalization in large language models. In Alice H. Oh, Alekh Agarwal, Danielle Belgrave, and Kyunghyun Cho (eds.), Advances in Neural Information Processing Systems, 2022. URL https://openreview.net/forum?id=zSyVVeX7bC4.
- Cited regarding in-context learning on extreme-label classification tasks

**Milos et al., 2023**: Not visible in provided pages (cited regarding extreme-label classification)

**Sileo et al., 2019**: Reference to Discovery dataset - automatically discovers sentence pairs with relevant discourse markers, 174 discourse markers with at least 10K examples each
- Cited multiple times regarding the Discovery dataset

**Kenton & Toutanova, 2019**: Reference to BERT model
- Cited as achieving 87% on Discovery task

### From Related Work (02_related-work.md)

**Dong et al., 2023**: Qingxiu Dong, Lei Li, Damai Dai, Ce Zheng, Zhiyong Wu, Baobao Chang, Xu Sun, Jingjing Xu, Lei Li, and Zhifang Sui. A survey on in-context learning, 2023.
- Cited regarding ICL as favored approach

**Liu et al., 2022**: Jiachang Liu, Dinghan Shen, Yizhe Zhang, Bill Dolan, Lawrence Carin, and Weizhu Chen. What makes good in-context examples for GPT-3? In Proceedings of Deep Learning Inside Out (DeeLIO 2022): The 3rd Workshop on Knowledge Extraction and Integration for Deep Learning Architectures, pp. 100-114, Dublin, Ireland and Online, May 2022. doi: 10.18653/v1/2022.deelio-1.10. URL https://aclanthology.org/2022.deelio-1.10.
- Cited for enhancing ICL performance with more demonstration examples in Related Work

**Wu et al., 2023**: Not visible in provided pages

**Liu et al., 2023**: Reference to Lost in the Middle phenomenon - showing that longer input prompts can diminish performance
- Cited multiple times, including in exploratory experiments section

**Peng et al., 2023c**: Not visible in provided pages

**Li et al., 2023c**: Not visible in provided pages

**Wang et al., 2023**: Not visible in provided pages

**Rozière et al., 2024**: Not visible in provided pages

**Su et al., 2021**: Reference to relative rotary positional embedding (RoPE)

**Hao et al., 2022**: Not visible in provided pages (sliding memory window)

**Zhu et al., 2024**: Not visible in provided pages

**Tay et al., 2021**: Reference to Long-Range Arena - includes tasks for evaluating sequences ranging from 1K to 16K tokens
- Cited in long context evaluation section

**Bai et al., 2023b**: Yushi Bai, Xin Lv, Jiajie Zhang, Hongchang Lyu, Jiankai Tang, Zhidian Huang, Zhengxiao Du, Xiao Liu, Aohan Zeng, Lei Hou, Yuxiao Dong, Jie Tang, and Juanzi Li. Longbench: A bilingual, multitask benchmark for long context understanding, 2023b.
- Cited as LongBench benchmark with 21 bilingual datasets, average 6k words

**An et al., 2023**: Chenxin An, Shansan Gong, Ming Zhong, Xingjian Zhao, Mukai Li, Jun Zhang, Lingpeng Kong, and Xipeng Qiu. L-eval: Instituting standardized evaluation for long context language models, 2023.
- Cited as L-Eval Benchmark supporting 20 sub-tasks with 3K to 200K tokens

**Li et al., 2023b**: Reference to LooGLE - focuses on summarization and long dependency QA, test instances exceeding 100k words

**Zhang et al., 2024**: Reference to ∞Bench - encompasses 12 tasks with average length of 200K tokens

**Levy et al., 2024**: Not visible in provided pages (explores impact of extending input lengths on reasoning)

**Zhang et al., 2017**: Reference to TacRED dataset
- Cited as extreme-label classification in real-world domains

**Demszky et al., 2020**: Dorottya Demszky, Dana Movsliowitz-Attias, Jeongwoo Ko, Alan Cowen, Gaurav Nemade, and Sujith Ravi. GoEmotions: A dataset of fine-grained emotions. In Dan Jurafsky, Joyce Chai, Natalie Schluter, and Joel Tetreault (eds.), Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, pp. 4040–4054, Online, July 2020. Association for Computational Linguistics. doi: 10.18653/v1/2020.acl-main.372. URL https://aclanthology.org/2020.acl-main.372/.
- Cited as GoEmotions dataset

**Ding et al., 2021**: Ning Ding, Guangwei Xu, Yulin Chen, Xiaobin Wang, Xu Han, Pengjun Xie, Haitao Zheng, and Zhiyuan Liu. Few-NERD: A few-shot named entity recognition dataset. In Chengqing Zong, Fei Xia, Wenjie Li, and Roberto Navigli (eds.), Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers), pp. 3198–3213, Online, August 2021. Association for Computational Linguistics. doi: 10.18653/v1/2021.acl-long.248. URL https://aclanthology.org/2021.acl-long.248.
- Cited as Few-NERD dataset

**Bhatia et al., 2015**: Kush Bhatia, Himanshu Jain, Purushottam Kar, Manik Varma, and Prateek Jain. Sparse local embeddings for extreme multi-label classification. In Neural Information Processing Systems, 2015. URL https://api.semanticscholar.org/CorpusID:11419932.
- Cited as embedding-based approach for extreme-label classification

**Vulić et al., 2021**: Not visible in provided pages

### From Long In-context Evaluation (03_long-in-context-evaluation.md)

**Casanueva et al., 2020**: Iñigo Casanueva, Tadas Temčinas, Daniela Gerz, Matthew Henderson, and Ivan Vulić. Efficient intent detection with dual sentence encoders. In Tsung-Hsien Wen, Asli Celikyilmaz, Zhou Yu, Alexandros Papangelis, Mihail Eric, Anuj Kumar, Iñigo Casanueva, and Rushin Shah (eds.), Proceedings of the 2nd Workshop on Natural Language Processing for Conversational AI, pp. 38–45, Online, July 2020. Association for Computational Linguistics. doi: 10.18653/v1/2020.nlp4convai-1.5. URL https://aclanthology.org/2020.nlp4convai-1.5.
- Cited as BANKING77 dataset

**Yu et al., 2020**: Reference to DialogRE dataset - human-annotated dialogue-based relation extraction from Friends

### From Exploratory Experiment (04_exploratory-experiment.md)

No new citations beyond those already listed above.

## Additional References from PDF (pages 10-11)

The following additional references appear in the References section of the PDF but were not explicitly cited in the section notes:

**Claude 3 model family** (p. 10): The claude 3 model family: Opus, sonnet, haiku. URL https://api.semanticscholar.org/CorpusID:268232499.
- Listed as reference for API-based models

**Josh Achiam et al., 2023** (p. 10): Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, et al. Gpt-4 technical report. arXiv preprint arXiv:2303.08774, 2023.
- Listed as reference for GPT-4

**01. AI, et al., 2024** (p. 10): 01. AI, ..., Alex Young, Bei Chen, Chao Li, Chengen Huang, Ge Zhang, Guanwei Zhang, Heng Li, Jiangcheng Zhu, Jianqun Chen, Jing Chang, Kaidong Yu, Peng Liu, Qiang Liu, Shawn Yue, Senbin Yang, Shiming Yang, Yaohui Li, Yichang Zhang, Xiaobo Xie, Wenhao Huang, Xiaohu Xie, Xinyang Niu, Pengcheng Nie, Yuchi Xu, Yudong Liu, Yue Wang, Yuxuan Cai, Zhenyu Gu, Zhiyuan Liu, and Zonghong Dai. Yi: Open foundation models by 01.ai, 2024.
- Listed as reference for Yi models

**Cai et al., 2024** (p. 11): Zheng Cai, Maosong Cao, Haojiong Chen, ..., Yu Qiao, and Dahua Lin. Internlm2 technical report. arXiv preprint arXiv:2403.17297, 2024.
- Listed as reference for InternLM2

**Bai et al., 2023a**: Yushi Bai, Xin Lv, Jiajie Zhang, Hongchang Lyu, Jiankai Tang, Zhidian Huang, Zhengxiao Du, Xiao Liu, Aohan Zeng, Lei Hou, Yuxiao Dong, Jie Tang, and Juanzi Li. Longbench: A bilingual, multitask benchmark for long context understanding, 2023b.
- Cited as reference in bibliography (p. 11)

**Casanueva et al., 2020**: Iñigo Casanueva, Tadas Temčinas, Daniela Gerz, Matthew Henderson, and Ivan Vulić. Efficient intent detection with dual sentence encoders. In Tsung-Hsien Wen, Asli Celikyilmaz, Zhou Yu, Alexandros Papangelis, Mihail Eric, Anuj Kumar, Iñigo Casanueva, and Rushin Shah (eds.), Proceedings of the 2nd Workshop on Natural Language Processing for Conversational AI, pp. 38–45, Online, July 2020. Association for Computational Linguistics. doi: 10.18653/v1/2020.nlp4convai-1.5. URL https://aclanthology.org/2020.nlp4convai-1.5.
- Cited for BANKING77 dataset in Table 1 and section 3.1

**Chen et al., 2023a**: Shouyuan Chen, Sherman Wong, Liangjian Chen, and Yuandong Tian. Extending context window of large language models via positional interpolation. ArXiv, abs/2306.15595, 2023a. URL https://api.semanticscholar.org/CorpusID:259262376.
- Cited for extending context window via positional interpolation in Introduction and Related Work

**Chen et al., 2023b**: Yukang Chen, Shengju Qian, Haotian Tang, Xin Lai, Zhijian Liu, Song Han, and Jiaya Jia. Longlora: Efficient fine-tuning of long-context large language models. In The Twelfth International Conference on Learning Representations, 2023b.
- Cited for incorporating long-context techniques into open-source LLMs

**Dasigi et al., 2021**: Pradeep Dasigi, Kyle Lo, Iz Beltagy, Arman Cohan, Noah A Smith, and Matt Gardner. A dataset of information-seeking questions and answers anchored in research papers. In Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, pp. 4599–4610, 2021.
- Cited as the Qasper dataset for long document QA

**Demszky et al., 2020**: Dorottya Demszky, Dana Movsliowitz-Attias, Jeongwoo Ko, Alan Cowen, Gaurav Nemade, and Sujith Ravi. GoEmotions: A dataset of fine-grained emotions. In Dan Jurafsky, Joyce Chai, Natalie Schluter, and Joel Tetreault (eds.), Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, pp. 4040–4054, Online, July 2020. Association for Computational Linguistics. doi: 10.18653/v1/2020.acl-main.372. URL https://aclanthology.org/2020.acl-main.372/.
- Cited as GoEmotions dataset in Table 1 and section 3.1

**Ding et al., 2021**: Ning Ding, Guangwei Xu, Yulin Chen, Xiaobin Wang, Xu Han, Pengjun Xie, Haitao Zheng, and Zhiyuan Liu. Few-NERD: A few-shot named entity recognition dataset. In Chengqing Zong, Fei Xia, Wenjie Li, and Roberto Navigli (eds.), Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers), pp. 3198–3213, Online, August 2021. Association for Computational Linguistics. doi: 10.18653/v1/2021.acl-long.248. URL https://aclanthology.org/2021.acl-long.248.
- Cited as Few-NERD dataset in Table 1 and section 3.1

**Ding et al., 2024**: Yiran Ding, Li Lyna Zhang, Chengruidong Zhang, Yuanyuan Xu, Ning Shang, Jiahang Xu, Fan Yang, and Mao Yang. Longrope: Extending llm context window beyond 2 million tokens. arXiv preprint arXiv:2402.13753, 2024.
- Cited for extending context window to 2M tokens in Introduction

**Dong et al., 2023**: Qingxiu Dong, Lei Li, Damai Dai, Ce Zheng, Zhiyong Wu, Baobao Chang, Xu Sun, Jingjing Xu, Lei Li, and Zhifang Sui. A survey on in-context learning, 2023.
- Cited regarding ICL as favored approach in Related Work

**Fu et al., 2024**: Yao Fu, Rameswar Panda, Xinyao Niu, Xiang Yue, Hannaneh Hajishirzi, Yoon Kim, and Hao Peng. Data engineering for scaling language models to 128k context. arXiv preprint arXiv:2402.10171, 2024.
- Cited for helping models extrapolate to 128K window size in Introduction

**Gu & Dao, 2023**: Albert Gu and Tri Dao. Mamba: Linear-time sequence modeling with selective state spaces. arXiv preprint arXiv:2312.00752, 2023.
- Cited as Mamba architecture - RNN-like architecture to decrease attention complexity in Table 2 and Introduction

**Kenton & Toutanova, 2019**: Jacob Devlin Ming-Wei Chang Kenton and Lee Kristina Toutanova. Bert: Pre-training of deep bidirectional transformers for language understanding. In Proceedings of NAACL-HLT, pp. 4171–4186, 2019.
- Cited as achieving 87% on Discovery task in Introduction

**Liu et al., 2023**: Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, and Percy Liang. Lost in the middle: How language models use long contexts. Transactions of the Association for Computational Linguistics, 12:157–173, 2023. URL https://api.semanticscholar.org/CorpusID:259360665.
- Cited as Lost in the Middle phenomenon in Related Work and Exploratory Experiment

**Peng et al., 2023a**: Bo Peng, Eric Alcaide, Quentin Anthony, Alon Albalak, Samuel Arcadinho, Stella Biderman, Huanqi Cao, Xin Cheng, Michael Chung, Leon Derczynski, et al. Rwkv: Reinventing rnns for the transformer era. In Findings of the Association for Computational Linguistics: EMNLP 2023, pp. 14048–14077, 2023a.
- Cited as RWKV architecture in Table 2 and Introduction

**Press et al., 2022**: Ofir Press, Noah A Smith, and Mike Lewis. Train short, test long: Attention with linear biases enables input length extrapolation. In International Conference on Learning Representations, 2022. URL https://openreview.net/forum?id=R8sQPpGCv0.
- Cited as ALiBi embeddings approach in Introduction and Related Work

**Sileo et al., 2019**: Damien Sileo, Tim Van De Cruys, Camille Pradel, and Philippe Muller. Mining discourse markers for unsupervised sentence representation learning. In Jill Burstein, Christy Doran, and Thamar Solorio (eds.), Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers), pp. 3477–3486, Minneapolis, Minnesota, June 2019. Association for Computational Linguistics. doi: 10.18653/v1/N19-1351. URL https://aclanthology.org/N19-1351.
- Cited as Discovery dataset in Table 1 and throughout paper

**Su et al., 2021**: Jianlin Su, Yu Lu, Shengfeng Pan, Bo Wen, and Yunfeng Liu. Roformer: Enhanced transformer with rotary position embedding. ArXiv, abs/2104.09864, 2021. URL https://api.semanticscholar.org/CorpusID:233307138.
- Cited as relative rotary positional embedding (RoPE) in Related Work

**Tay et al., 2021**: Yi Tay, Mostafa Dehghani, Samira Abnar, Yikang Shen, Dara Bahri, Philip Pham, Jinfeng Rao, Liu Yang, Sebastian Ruder, and Donald Metzler. Long range arena : A benchmark for efficient transformers. In International Conference on Learning Representations, 2021. URL https://openreview.net/forum?id=qVyeW-grC2k.
- Cited as Long-Range Arena benchmark in Related Work

**Yu et al., 2020**: Dian Yu, Kai Sun, Claire Cardie, and Dong Yu. Dialogue-based relation extraction. In Dan Jurafsky, Joyce Chai, Natalie Schluter, and Joel Tetreault (eds.), Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, pp. 4927–4940, Online, July 2020. Association for Computational Linguistics. doi: 10.18653/v1/2020.acl-main.444. URL https://aclanthology.org/2020.acl-main.444.
- Cited as DialogRE dataset in Table 1 and section 3.1

**Zhang et al., 2017**: Yuhao Zhang, Victor Zhong, Danqi Chen, Gabor Angeli, and Christopher D. Manning. Position-aware attention and supervised data improve slot filling. In Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing (EMNLP 2017), pp. 35–45, 2017. URL https://nlp.stanford.edu/pubs/zhang2017tacred.pdf.
- Cited as TacRED dataset in Table 1, section 3.1, and Related Work

**Hao et al., 2022**: Yaru Hao, Yutao Sun, Li Dong, Zhixiong Han, Yuxian Gu, and Furu Wei. Structured prompting: Scaling in-context learning to 1, 000 examples. ArXiv, abs/2212.06713, 2022. URL https://api.semanticscholar.org/CorpusID:254591686.
- Cited for context window sliding methodology in Introduction [p. 12]

**Jin et al., 2024**: Hongye Jin, Xiaotian Han, Jingfeng Yang, Zhimeng Jiang, Zirui Liu, Chia-Yuan Chang, Huiyuan Chen, and Xia Hu. Llm maybe longllm: Self-extend llm context window without tuning, 2024.
- Cited for extending long context in Introduction [p. 12]

**Ratner et al., 2023**: Nir Ratner, Yoav Levine, Yonatan Belinkov, Ori Ram, Inbal Magar, Omri Abend, Ehud Karpas, Amnon Shashua, Kevin Leyton-Brown, and Yoav Shoham. Parallel context windows for large language models. In Anna Rogers, Jordan Boyd-Graber, and Naoaki Okazaki (eds.), Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 6383–6402, Toronto, Canada, July 2023. Association for Computational Linguistics. doi: 10.18653/v1/2023.acl-long.352. URL https://aclanthology.org/2023.acl-long.352.
- Cited for parallel context windows methodology in Introduction and Related Work [p. 13]

**Orvieto et al., 2023**: Antonio Orvieto, Samuel L. Smith, Albert Gu, Anushan Fernando, Caglar Gulcehre, Razvan Pascanu, and Soham De. Resurrecting recurrent neural networks for long sequences. ArXiv, abs/2303.06349, 2023. URL https://api.semanticscholar.org/CorpusID:257340878.
- Cited for recurrent models approach in Introduction [p. 13]

**Tworkowski et al., 2023**: Szymon Tworkowski, Konrad Staniszewski, Mikołaj Pacek, Yuhuai Wu, Henryk Michalewski, and Piotr Miłoś. Focused transformer: Contrastive training for context scaling, 2023.
- Cited for incorporating long-context techniques into open-source LLMs in Introduction [p. 15]

**Mohtashami & Jaggi, 2023**: Amirkeivan Mohtashami and Martin Jaggi. Landmark attention: Random-access infinite context length for transformers. In Workshop on Efficient Systems for Foundation Models@ ICML2023, 2023.
- Cited for passkey retrieval evaluation in Introduction [p. 12]

**Li et al., 2023a**: Dawei Zhu, Nan Yang, Liang Wang, Yifan Song, Wenhao Wu, Furu Wei, and Sujian Li. PosE: Efficient context window extension of LLMs via positional skip-wise training. In The Twelfth International Conference on Learning Representations, 2024. URL https://openreview.net/forum?id=3Zlgxuag0rA.
- Cited for passkey retrieval evaluation in Introduction [p. 16]

**Team et al., 2023**: Gemini Team, Rohan Anil, Sebastian Borgeaud, Yonghui Wu, Jean-Baptiste Alayrac, Jiahui Yu, Radu Soricut, et al. Gemini: a family of highly capable multimodal models. arXiv preprint arXiv:2312.11805, 2023.
- Cited for needle-in-a-haystack evaluation in Introduction [p. 15]

**Nallapat et al., 2017**: Ramesh Nallapati, Feifei Zhai, and Bowen Zhou. Summarunner: A recurrent neural network based sequence model for extractive summarization of documents. In Proceedings of the AAAI conference on artificial intelligence, volume 31, 2017.
- Cited for position bias in summarization in Introduction [p. 12]

**Anil et al., 2022**: Cem Anil, Yuhuai Wu, Anders Johan Andreassen, Aitor Lewkowycz, Vedant Misra, Vinay Venkatesh Ramasesh, Ambrose Slone, Guy Gur-Ari, Ethan Dyer, and Behnam Neyshabur. Exploring length generalization in large language models. In Alice H. Oh, Alekh Agarwal, Danielle Belgrave, and Kyunghyun Cho (eds.), Advances in Neural Information Processing Systems, 2022. URL https://openreview.net/forum?id=zSyVVeX7bC4.
- Cited regarding in-context learning on extreme-label classification tasks in Introduction [not visible on provided pages]

**Milos et al., 2023**: Aristides Milios, Siva Reddy, and Dzmitry Bahdanau. In-context learning for text classification with many labels, 2023.
- Cited regarding extreme-label classification in Introduction and Related Work [p. 12]

**Bhatia et al., 2015**: Kush Bhatia, Himanshu Jain, Purushottam Kar, Manik Varma, and Prateek Jain. Sparse local embeddings for extreme multi-label classification. In Neural Information Processing Systems, 2015. URL https://api.semanticscholar.org/CorpusID:11419932.
- Cited as embedding-based approach for extreme-label classification in Related Work [p. 11]

**Wu et al., 2023**: Zhiyong Wu, Yaoxiang Wang, Jiacheng Ye, and Lingpeng Kong. Self-adaptive in-context learning: An information compression perspective for in-context example selection and ordering, 2023.
- Cited in Related Work for ICL demonstrations [p. 16]

**Peng et al., 2023c**: Hao Peng, Xiaozhi Wang, Jianhui Chen, Weikai Li, Yunjia Qi, Zimu Wang, Zhili Wu, Kaisheng Zeng, Bin Xu, Lei Hou, and Juanzi Li. When does in-context learning fall short and why? a study on specification-heavy tasks, 2023c.
- Cited in Related Work regarding ICL falling short on specification-heavy tasks [p. 13]

**Li et al., 2023c**: Dacheng Li, Rulin Shao, Anze Xie, Ying Sheng, Lianmin Zheng, Joseph Gonzalez, Ion Stoica, Xuezhe Ma, and Hao Zhang. How long can context length of open-source LLMs truly promise? In NeurIPS 2023 Workshop on Instruction Tuning and Instruction Following, 2023a. URL https://openreview.net/forum?id=Lywi1fNMV5.
- Cited in Related Work for memory augmentation and extrapolation techniques to support ICL [p. 12]

**Wang et al., 2023**: Weizhi Wang, Li Dong, Hao Cheng, Xiaodong Liu, Xifeng Yan, Jianfeng Gao, and Furu Wei. Augmenting language models with long-term memory. In Thirty-seventh Conference on Neural Information Processing Systems, 2023. URL https://openreview.net/forum?id=BryMFPR4L6.
- Cited in Related Work for memory augmentation and extrapolation techniques to support ICL [p. 16]

**Rozière et al., 2024**: Baptiste Rozière, Jonas Gehring, Fabian Gloeckle, Sten Sootla, Itai Gat, Xiaoqing Ellen Tan, Yossi Adi, Jingyu Liu, Romain Sauvestre, Tal Remez, Jérémy Rapin, Artyom Kozhevnikov, Ivan Evtimov, Joanna Bitton, Manish Bhatt, Cristian Canton Ferrer, Aaron Grattafiori, Wenhan Xiong, Alexandre Défossez, Jade Copet, Faisal Azhar, Hugo Touvron, Louis Martin, Nicolas Usunier, Thomas Scialom, and Gabriel Synnaeve. Code llama: Open foundation models for code, 2024.
- Cited in Related Work for continued fine-tuning with longer context [p. 15]

**Su et al., 2024**: Jianlin Su, Murtadha Ahmed, Yu Lu, Shengfeng Pan, Wen Bo, and Yunfeng Liu. Roformer: Enhanced transformer with rotary position embedding. Neurocomputing, 568:127063, 2024.
- Cited for RoPE embeddings in Introduction [p. 15]

**Zhu et al., 2024**: Dawei Zhu, Nan Yang, Liang Wang, Yifan Song, Wenhao Wu, Furu Wei, and Sujian Li. PoSE: Efficient context window extension of LLMs via positional skip-wise training. In The Twelfth International Conference on Learning Representations, 2024. URL https://openreview.net/forum?id=3Zlgxuag0rA.
- Cited in Related Work for sliding memory window [p. 16]

**Li et al., 2023b**: Jiaqi Li, Mengmeng Wang, Zilong Zheng, and Muhan Zhang. Loogle: Can long-context language models understand long contexts?, 2023b.
- Cited as LooGLE benchmark in Related Work [p. 12]

**Zhang et al., 2024**: Xinrong Zhang, Yingfa Chen, Shengding Hu, Zihang Xu, Junhao Chen, Moo Khai Hao, Xu Han, Zhen Leng Thai, Shuo Wang, Zhiyuan Liu, and Maosong Sun. ∞bench: Extending long context evaluation beyond 100k tokens, 2024.
- Cited as ∞Bench benchmark in Related Work [p. 16]

**Levy et al., 2024**: Mosh Levy, Alon Jacoby, and Yoav Goldberg. Same task, more tokens: the impact of input length on the reasoning performance of large language models, 2024.
- Cited in Related Work for exploring impact of extending input lengths [p. 12]

**Vulić et al., 2021**: Ivan Vulić, Pei-Hao Su, Samuel Coope, Daniela Gerz, Paweł Budzianowski, Iñigo Casanueva, Nikola Mrkšić, and Tsung-Hsien Wen. ConvFiT: Conversational fine-tuning of pretrained language models. In Marie-Francine Moens, Xuanjing Huang, Lucia Specia, and Scott Wen-tau Yih (eds.), Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing, pp. 1151–1168, Online and Punta Cana, Dominican Republic, November 2021. Association for Computational Linguistics. doi: 10.18653/v1/2021.emnlp-main.88. URL https://aclanthology.org/2021.emnlp-main.88.
- Cited in Related Work for extreme-label classification methods [p. 16]

**Lin et al., 2024**: Not fully found in pages 11-16, appears as multiple Liu entries

**Xiong et al., 2023**: Wenhan Xiong, Jingyu Liu, Igor Molybog, Hejia Zhang, Prajjwal Bhargava, Rui Hou, Louis Martin, Rashi Rungta, Karthik Abinav Sankararaman, Barlas Oguz, et al. Effective long-context scaling of foundation models. arXiv preprint arXiv:2309.16039, 2023.
- Cited for helping models extrapolate to longer contexts in Introduction [p. 16]

**Xiao et al., 2024**: Guangxuan Xiao, Yuandong Tian, Beidi Chen, Song Han, and Mike Lewis. Efficient streaming language models with attention sinks. In The Twelfth International Conference on Learning Representations, 2024. URL https://openreview.net/forum?id=NG7sS5IzV.
- Cited for extending long context in Introduction [p. 16]

**Peng et al., 2023b**: Bowen Peng, Jeffrey Quesnelle, Honglu Fan, and Enrico Shippole. Yarn: Efficient context window extension of large language models, 2023b.
- Cited for extending long context in Introduction [p. 13]

**An et al., 2023**: Chenxin An, Shansan Gong, Ming Zhong, Xingjian Zhao, Mukai Li, Jun Zhang, Lingpeng Kong, and Xipeng Qiu. L-eval: Instituting standardized evaluation for long context language models, 2023.
- Previously listed, no update needed

### Additional References from pages 16-19 (Appendix)

**Demszky et al., 2020** [p. 16]: Dorottya Demszky, Dana Movsliowitz-Attias, Jeongwoo Ko, Alan Cowen, Gaurav Nemade, and Sujith Ravi. GoEmotions: A dataset of fine-grained emotions. In Dan Jurafsky, Joyce Chai, Natalie Schluter, and Joel Tetreault (eds.), Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, pp. 4040–4054, Online, July 2020. Association for Computational Linguistics. doi: 10.18653/v1/2020.acl-main.372. URL https://aclanthology.org/2020.acl-main.372/.
- Cited in Appendix A.1 describing the GoEmotions dataset (58k English comments, 27 emotion categories, 28 tokens average)

**Ding et al., 2021** [p. 16]: Ning Ding, Guangwei Xu, Yulin Chen, Xiaobin Wang, Xu Han, Pengjun Xie, Haitao Zheng, and Zhiyuan Liu. Few-NERD: A few-shot named entity recognition dataset. In Chengqing Zong, Fei Xia, Wenjie Li, and Roberto Navigli (eds.), Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers), pp. 3198–3213, Online, August 2021. Association for Computational Linguistics. doi: 10.18653/v1/2021.acl-long.248. URL https://aclanthology.org/2021.acl-long.248.
- Cited in Appendix A.1 describing the Few-NERD dataset (8 coarse-grained and 66 fine-grained entity types, 61 tokens average)
