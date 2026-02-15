# References

This file contains bibliographic information for citations that appear substantively in the section notes.

Format: Author (Year) - Full bibliographic information
- Where cited in notes and context

## Key Method Citations

**Dao (2023)** - Tri Dao. Flashattention-2: Faster attention with better parallelism and work partitioning, 2023.
- Cited in sections 01 and 04 for FlashAttention-2, and in section 09 for pretraining infrastructure

**Dao et al. (2022)** - Tri Dao, Daniel Y. Fu, Stefano Ermon, Atri Rudra, and Christopher Ré. Flashattention: Fast and memory-efficient exact attention with io-awareness. In NeurIPS, 2022.
- Cited in section 04 for the original FlashAttention implementation used for STRING

**Su et al. (2022)** - Jianlin Su, Yu Lu, Shengfeng Pan, Ahmed Murtadha, Bo Wen, and Yunfeng Liu. Reformer: Enhanced transformer with rotary position embedding, 2022.
- Cited in section 02 as the RoPE (Rotary Position Embedding) baseline method

**Su (2023)** - Jianlin Su. Rectified rotary position embeddings. https://github.com/bojone/rerope, 2023.
- Cited in sections 04 and 05 as the ReRoPE baseline method

**Jin et al. (2024)** - Hongye Jin, Xiaotian Han, Jingfeng Yang, Zhimeng Jiang, Zirui Liu, Chia-Yuan Chang, Huiyuan Chen, and Xia Hu. Llm maybe longlm: Self-extend llm context window without tuning, 2024.
- Cited in sections 04 and 05 as the Self-Extend baseline method

**An et al. (2024b)** - Shengnan An, Zexiong Ma, Zeqi Lin, Nanning Zheng, and Jian-Guang Lou. Make your llm fully utilize the context. 2024b. URL https://arxiv.org/abs/2404.16811.
- Cited in sections 05 as the DCA (Dynamic Context Adjustment) baseline method

**Peng et al. (2023)** - Bowen Peng, Jeffrey Quesnelle, Honglu Fan, and Enrico Shippole. Yarn: Efficient context window extension of large language models, 2023.
- Cited in sections 02 and 05 as the YaRN baseline method

**LocalLLaMA (2023a)** - LocalLLaMA. Dynamically scaled rope further increases performance of long context llama with zero fine-tuning, July 2023a. URL https://www.reddit.com/r/LocalLLaMA/comments/14mrgpr/dynamically_scaled_rope_further_increases/.
- Cited in section 05 as the NTK-Aware RoPE baseline method

## Benchmark Citations

**gkamradt (2023)** - gkamradt. Llmtest_needleinahaystack: Doing simple retrieval from llm models. https://github.com/gkamradt/LLMTest_NeedleInAHaystack/tree/main, 2023. [Online; accessed 29-December-2023].
- Cited in sections 03 and 05 as the Needle-in-a-Haystack (NIAH) benchmark

**Hsieh et al. (2024)** - Cheng-Ping Hsieh, Simeng Sun, Samuel Kriman, Shantanu Acharya, Dima Rekesh, Fei Jia, Yang Zhang, and Boris Ginsburg. Ruler: What's the real context size of your long-context language models?, 2024. URL https://arxiv.org/abs/2404.06654.
- Cited in sections 05 as the RULER benchmark for evaluating effective context length

**Zhang et al. (2024d)** - Xinrong Zhang, Yingfa Chen, Shengding Hu, Zihang Xu, Junhao Chen, Moo Khai Hao, Xu Han, Zhen Leng Thai, Shuo Wang, Zhiyuan Liu, and Maosong Sun. ∞bench: Extending long context evaluation beyond 100k tokens, 2024d. URL https://arxiv.org/abs/2402.13718.
- Cited in sections 05 as the InfiniteBench benchmark

## Model Citations

**Llama Team (2024)** - Llama Team. The llama 3 herd of models. CoRR, abs/2407.21783, 2024. doi: 10.48550/ARXIV.2407.21783. URL https://doi.org/10.48550/arXiv.2407.21783.
- Cited in sections 03 and 05 for Llama 3.1 models (8B, 70B, 128K context)

**Liu et al. (2024a)** - Hao Liu, Wilson Yan, Matei Zaharia, and Pieter Abbeel. World model on million-length video and language with ringattention. arXiv preprint, 2024a.
- Cited in section 05 as LargeWorldModel (LWM-7B-base)

**Mistral.AI (2024)** - Mistral.AI. La plateforme, 2024. URL https://mistral.ai/news/la-plateforme/.
- Cited in section 05 for Mistral 7B model

**Touvron et al. (2023b)** - Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, et al. Llama 2: Open foundation and fine-tuned chat models. arXiv preprint arXiv:2307.09288, 2023b.
- Cited in section 05 (Table 2) as the baseline performance threshold in RULER

## Training and Architecture Citations

**Vaswani et al. (2017)** - Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and Illia Polosukhin. Attention is all you need, 2017.
- Cited in section 01 for the Transformer architecture

**Kaplan et al. (2020)** - Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B. Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jeffrey Wu, and Dario Amodei. Scaling laws for neural language models, 2020. URL https://arxiv.org/abs/2001.08361.
- Cited in section 03 for scaling law analysis methodology

**Lefaudeux et al. (2022)** - Benjamin Lefaudeux, Francisco Massa, Diana Liskovich, Wenhan Xiong, Vittorio Caggiano, Sean Naren, Min Xu, Jieru Hu, Marta Tintore, Susan Zhang, Patrick Labatut, Daniel Haziza, Luca Wehrstedt, Jeremy Reizenstein, and Grigory Sizov. xFormers: A modular and hackable transformer modelling library. https://github.com/facebookresearch/xformers, 2022.
- Cited in section 09 (A.2 Pretraining Setup) for xFormers optimization library

**Loshchilov & Hutter (2019)** - Ilya Loshchilov and Frank Hutter. Decoupled weight decay regularization, 2019. URL https://arxiv.org/abs/1711.05101.
- Cited in section 09 (A.2 Pretraining Setup) for AdamW optimizer

**Cerebras (2023)** - Cerebras. Slimpajama: A 627b token, cleaned and deduplicated version of redpajama, 2023. URL https://cerebras.ai/blog/slimpajama-a-627b-token-cleaned-and-deduplicated-version-of-redpajama.
- Cited in section 02 for the SlimPajama training dataset

**Bao et al. (2020)** - Hangbo Bao, Li Dong, Furu Wei, Wenhui Wang, Nan Yang, Xiaodong Liu, Yu Wang, Songhao Piao, Jianfeng Gao, Ming Zhou, and Hsiao-Wuen Hon. Unilm v2: Pseudo-masked language models for unified language model pre-training, 2020. URL https://arxiv.org/abs/2002.12804.
- Cited in section 02 for relative positional encodings (ALiBi)

**Beltagy et al. (2020)** - Iz Beltagy, Matthew E. Peters, and Arman Cohan. Longformer: The long-document transformer, 2020. URL https://arxiv.org/abs/2004.05150.
- Cited in section 01 (introduction) for sliding window attention, used as a component in STRING implementation

## Related Work - Long Context Scaling

**Jiang et al. (2024)** - Huiqiang Jiang, Yucheng Li, Chengruidong Zhang, Qianhui Wu, Xufang Luo, Surin Ahn, Zhenhua Han, Amir H. Abdi, Dongsheng Li, Chin-Yew Lin, Yuqing Yang, and Lili Qiu. Minference v1.0: Accelerating pre-filling for long-context llms via dynamic sparse attention, 2024. URL https://arxiv.org/abs/2407.02490.
- Cited in section 06 for sparse attention methods

**Gu & Dao (2023)** - Albert Gu and Tri Dao. Mamba: Linear-time sequence modeling with selective state spaces. arXiv preprint arXiv:2312.00752, 2023.
- Cited in section 06 for state space models

**Xiao et al. (2023; 2024)** - Guangxuan Xiao, Yuandong Tian, Beidi Chen, Song Han, and Mike Lewis. Efficient streaming language models with attention sinks, 2023. / Chaojun Xiao, Pengle Zhang, Xu Han, Guangxuan Xiao, Yankai Lin, Zhengyan Zhang, Zhiyuan Liu, Song Han, and Maosong Sun. Infllm: Training-free long-context extrapolation for llms with an efficient context memory, 2024.
- Cited in section 06 for infinite context methods (StreamingLLM, InfLLM)

## Related Work - Length Extrapolation

**Press et al. (2022)** - Ofir Press, Noah A. Smith, and Mike Lewis. Train short, test long: Attention with linear biases enables input length extrapolation, 2022.
- Cited in section 06 for ALiBi extrapolation method

**Zhu et al. (2023)** - Dawei Zhu, Nan Yang, Liang Wang, Yifan Song, Wenhao Wu, Furu Wei, and Sujian Li. Pose: Efficient context window extension of llms via positional skip-wise training, 2023.
- Cited in section 06 for position index randomization method

**Chen et al. (2023)** - Guanzheng Chen, Xin Li, Zaiqiao Meng, Shangsong Liang, and Lidong Bing. Clex: Continuous length extrapolation for large language models, 2023.
- Cited in section 02 for continuous length extrapolation

## Commercial Model Citations

**OpenAI (2023)** - OpenAI. Gpt-4 technical report, 2023.
- Cited in sections 01 and 05 for GPT-4 comparison

**Anthropic (2023)** - Anthropic. Introducing 100K Context Windows, 2023. URL https://www.anthropic.com/index/100k-context-windows.
- Cited in sections 01 and 05 for Claude 2 comparison

**Moonshot AI (2023)** - Moonshot AI. Kimi chat. https://kimi.moonshot.cn/, 2023.
- Cited in section 05 for Kimi-chat comparison

## Additional Model and Application Citations

**Bai et al. (2023)** - Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Kai Dang, Xiaodong Deng, Yang Fan, Wenbin Ge, Yu Han, Fei Huang, Binyuan Hui, Luo Ji, Mei Li, Junyang Lin, Runji Lin, Dayiheng Liu, Gao Liu, Chengqiang Lu, Keming Lu, Jianxin Ma, Rui Men, Xingzhang Ren, Xuancheng Ren, Chuanqi Tan, Sinan Tan, Jianhong Tu, Peng Wang, Shijie Wang, Wei Wang, Shengguang Wu, Benfeng Xu, Jin Xu, An Yang, Hao Yang, Jian Yang, Shusheng Yang, Yang Yao, Bowen Yu, Hongyi Yuan, Zheng Yuan, Jianwei Zhang, Xingxuan Zhang, Yichang Zhang, Zhenru Zhang, Chang Zhou, Jingren Zhou, Xiaohuan Zhou, and Tianhang Zhu. Qwen technical report. arXiv preprint arXiv:2309.16609, 2023.
- Cited in section 01 for Qwen models with long context

**Bai et al. (2024)** - Yushi Bai, Xin Lv, Jiajie Zhang, Yuze He, Ji Qi, Lei Hou, Jie Tang, Yuxiao Dong, and Juanzi Li. Longalign: A recipe for long context alignment of large language models, 2024. URL https://arxiv.org/abs/2401.18058.
- Cited in section 01 for data engineering techniques for long-context training

**Xiong et al. (2023)** - Wenhan Xiong, Jingyu Liu, Igor Molybog, Hejia Zhang, Prajjwal Bhargava, Rui Hou, Louis Martin, Rashi Rungta, Karthik Abinav Sankararaman, Barlas Oguz, Madian Khabsa, Han Fang, Yashar Mehdad, Sharan Narang, Kshitiz Malik, Angela Fan, Shruti Bhosale, Sergey Edunov, Mike Lewis, Sinong Wang, and Hao Ma. Effective long-context scaling of foundation models. CoRR, abs/2309.16039, 2023. URL https://doi.org/10.48550/arXiv.2309.16039.
- Cited in section 01 for long-context scaling

**Fang et al. (2022; should be 2024b)** - Yao Fu, Rameswar Panda, Xinyao Niu, Xiang Yue, Hannaneh Hajishirzi, Yoon Kim, and Hao Peng. Data engineering for scaling language models to 128k context. 2024b. URL https://arxiv.org/abs/2402.10171.
- Cited in sections 01 and 06 for data engineering techniques for long-context training

**Li et al. (2024a)** - Dacheng Li, Rulin Shao, Anze Xie, Eric P. Xing, Xuezhe Ma, Ion Stoica, Joseph E. Gonzalez, and Hao Zhang. Distflashattn: Distributed flash attention for long-context llms training, 2024a. URL https://arxiv.org/abs/2310.03294.
- Cited in section 01 for efficient training methods

**Liu et al. (2023)** - Hao Liu, Matei Zaharia, and Pieter Abbeel. Ring attention with blockwise transformers for near-infinite context, 2023. URL https://arxiv.org/abs/2310.01889.
- Cited in section 01 for efficient attention calculation

**Touvron et al. (2023a)** - Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, Aurelien Rodriguez, Armand Joulin, Edouard Grave, and Guillaume Lample. Llama: Open and efficient foundation language models, 2023a.
- Cited in section 01 for original Llama model with 2K context

**Hu et al. (2024)** - Zhiyuan Hu, Yuliang Liu, Jinman Zhao, Suyuchen Wang, Yan Wang, Wei Shen, Qing Gu, Anh Tuan Luu, See-Kiong Ng, Zhiwei Jiang, and Bryan Hooi. Longrecipe: Recipe for efficient long context generalization in large language models, 2024. URL https://arxiv.org/abs/2409.00509.
- Cited in sections 01 and 06 for continual training with long data

**Zhao et al. (2024)** - Liang Zhao, Tianwei Wei, Liang Zeng, Cheng Cheng, Liu Yang, Peng Cheng, Lijie Wang, Chenxia Li, Xuejie Wu, Bo Zhu, Yimeng Gian, Rui Hu, Shuicheng Yan, Han Fang, and Yahui Zhou. Longskywork: A training recipe for efficiently extending context length in large language models, 2024. URL https://arxiv.org/abs/2406.00605.
- Cited in sections 01 and 06 for continual training approaches

**Lv et al. (2024)** - Kai Lv, Xiaoran Liu, Qipeng Guo, Hang Yan, Conghui He, Xipeng Qiu, and Dahua Lin. Longwanjuan: Towards systematic measurement for long text quality, 2024.
- Cited in section 01 for data quality in long-context training

**An et al. (2023)** - Chenxin An, Shansan Gong, Ming Zhong, Mukai Li, Jun Zhang, Lingpeng Kong, and Xipeng Qiu. L-eval: Instituting standardized evaluation for long context language models. arXiv preprint arXiv:2307.11088, 2023.
- Cited in section 01 for discrepancy between theoretical and practical context lengths

**Li et al. (2024b)** - Tianle Li, Ge Zhang, Quy Duc Do, Xiang Yue, and Wenhu Chen. Long-context llms struggle with long in-context learning, 2024b. URL https://arxiv.org/abs/2404.02060.
- Cited in section 01 for effective context utilization gaps

**Wang et al. (2024a)** - Mingzhe Wang, Longze Chen, Cheng Fu, Shengyi Liao, Xinghua Zhang, Bingli Wu, Haiyang Yu, Nan Xu, Lei Zhang, Run Luo, Yunshui Li, Lei Zhang, Run Luo, Yunshui Li, Fei Huang, and Yongbin Li. Leave no document behind: Benchmarking long-context llms with extended multi-doc qa, 2024a. URL https://arxiv.org/abs/2406.17419.
- Cited in section 01 for discrepancy between claimed and effective context lengths

**Geng & Liu (2023)** - Xinyang Geng and Hao Liu. Openllama: An open reproduction of llama, May 2023. URL https://github.com/openlm-research/open_llama.
- Cited in section 02 for use of SlimPajama corpus

**Zhang et al. (2024b)** - Peiyuan Zhang, Kaichen Zhang, Bo Li, Guangtao Zeng, Jingkang Yang, Yuanhan Zhang, Ziyue Wang, Haoran Tan, Chunyuan Li, and Ziwei Liu. Long context transfer from language to vision. arXiv preprint arXiv:2406.16852, 2024c. URL https://arxiv.org/abs/2406.16852.
- Cited in section 02 for use of SlimPajama corpus

**Zhu et al. (2024)** - Zhenyu (Allen) Zhang, Runjin Chen, Shiwei Liu, Zhewei Yao, Olatunji Ruwase, Beidi Chen, Xiaoxia Wu, and Zhangyang Wang. Found in the middle: How language models use long contexts better via plug-and-play positional encoding. ArXiv, abs/2403.04797, 2024e. URL https://api.semanticscholar.org/CorpusID:268296885.
- Cited in section 01 for challenges in modeling long-range dependencies

**Wu et al. (2024)** - Wenhao Wu, Yizhong Wang, Yao Fu, Xiang Yue, Dawei Zhu, and Sujian Li. Long context alignment with short instructions and synthesized positions, 2024. URL https://arxiv.org/abs/2405.03939.
- Cited in sections 01 and 06 for challenges in long-range modeling and continual training

## Architecture and Attention Citations

**Radford et al. (2018)** - Alec Radford, Karthik Narasimhan, Tim Salimans, and Ilya Sutskever. Improving language understanding by generative pre-training, 2018.
- Cited in section 02 for self-attention mechanisms lacking positional information

**Dai et al. (2019)** - Zihang Dai, Zhilin Yang, Yiming Yang, Jaime Carbonell, Quoc V. Le, and Ruslan Salakhutdinov. Transformer-xl: Attentive language models beyond a fixed-length context, 2019.
- Cited in section 02 for self-attention mechanisms

**Liu et al. (2021)** - Ze Liu, Yutong Lin, Yue Cao, Han Hu, Yixuan Wei, Zheng Zhang, Stephen Lin, and Baining Guo. Swin transformer: Hierarchical vision transformer using shifted windows, 2021. URL https://arxiv.org/abs/2103.14030.
- Cited in section 02 for inherent lack of positional information in attention

**Sun et al. (2022)** - Yutao Sun, Li Dong, Barun Patra, Shuming Ma, Shaohan Huang, Alon Benhaim, Vishrav Chaudhary, Xia Song, and Furu Wei. A length-extrapolatable transformer, 2022.
- Cited in section 02 for positional encoding

**Raffel et al. (2023; should be 2020)** - Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, and Peter J. Liu. Exploring the limits of transfer learning with a unified text-to-text transformer, 2023. URL https://arxiv.org/abs/1910.10683.
- Cited in sections 02 and 06 for T5-bias and relative positional encodings

**Hui et al. (2024)** - Binyuan Hui, Jian Yang, Zeyu Cui, Jiaxi Yang, Dayiheng Liu, Lei Zhang, Tianyu Liu, Jiajun Zhang, Bowen Yu, Kai Dang, et al. Qwen2. 5-coder technical report. arXiv preprint arXiv:2409.12186, 2024.
- Cited in section 02 for Qwen using RoPE

**Mohtashami & Jaggi (2023)** - Amirkeivan Mohtashami and Martin Jaggi. Landmark attention: Random-access infinite context length for transformers. arXiv preprint arXiv:2305.16300, 2023.
- Cited in section 03 for 6-digit needle format in NIAH

## Related Work - Efficient Architectures

**Jiang et al. (2024)** - Huiqiang Jiang, Yucheng Li, Chengruidong Zhang, Qianhui Wu, Xufang Luo, Surin Ahn, Zhenhua Han, Amir H. Abdi, Dongsheng Li, Chin-Yew Lin, Yuqing Yang, and Lili Qiu. Minference v1.0: Accelerating pre-filling for long-context llms via dynamic sparse attention, 2024. URL https://arxiv.org/abs/2407.02490.
- Cited in section 06 for sparse attention methods

**Fu et al. (2024a)** - Tianyu Fu, Haofeng Huang, Xuefei Ning, Genghan Zhang, Boju Chen, Tianqi Wu, Hongyi Wang, Zixiao Huang, Shiyao Li, Shengen Yan, Guohao Dai, Huazhong Yang, and Yu Wang. Moa: Mixture of sparse attention for automatic large scale compression. ArXiv, abs/2406.14909, 2024a. URL https://api.semanticscholar.org/CorpusID:270688596.
- Cited in section 06 for sparse attention optimization

**Song et al. (2023)** - Kaiqiang Song, Xiaoyang Wang, Sangwoo Cho, Xiaoman Pan, and Dong Yu. Zebra: Extending context window with layerwise grouped local-global attention, 2023.
- Cited in section 06 for sparse attention approaches

**Yang et al. (2024)** - Shuo Yang, Ying Sheng, Joseph E. Gonzalez, Ion Stoica, and Lianmin Zheng. Post-training sparse attention with double sparsity. ArXiv, abs/2408.07092, 2024. URL https://api.semanticscholar.org/CorpusID:271865443.
- Cited in section 06 for sparse attention methods

**Zhu et al. (2024b)** - Qianchao Zhu, Jiangfei Duan, Chang Chen, Siran Liu, Xiuhong Li, Guanyu Feng, Xin Lv, Huanqi Cao, Xiao Chuanfu, Xingcheng Zhang, Dahua Lin, and Chao Yang. Sampleattention: Near-lossless acceleration of long context llm inference with adaptive structured sparse attention, 2024b. URL https://arxiv.org/abs/2406.15486.
- Cited in section 06 for sparse attention

**Yuan et al. (2024)** - Danlong Yuan, Jiahao Liu, Bei Li, Huishuai Zhang, Jingang Wang, Xunliang Cai, and Dongyan Zhao. Remamba: Equip mamba with effective long-sequence modeling. arXiv preprint arXiv:2408.15496, 2024.
- Cited in section 06 for state space models

**Lieber et al. (2024)** - Opher Lieber, Barak Lenz, Hofit Bata, Gal Cohen, Jhonathan Osin, Itay Dalmedigos, Erez Safahi, Shaked Meirom, Yonatan Belinkov, Shai Shalev-Shwartz, et al. Jamba: A hybrid transformer-mamba language model. arXiv preprint arXiv:2403.19887, 2024.
- Cited in section 06 for state space model architectures

**Gao et al. (2024)** - Chaochen Gao, Xing Wu, Qingfang Fu, and Songlin Hu. Quest: Query-centric data synthesis approach for long-context scaling of large language model. ArXiv, abs/2405.19846, 2024. URL https://api.semanticscholar.org/CorpusID:270123337.
- Cited in section 06 for continual training with long data

**Ding et al. (2023)** - Jiayu Ding, Shuming Ma, Li Dong, Xingxing Zhang, Shaohan Huang, Wenhui Hu, and Furu Wei. Longnet: Scaling transformers to 1,000,000,000 tokens, 2023.
- Cited in sections 01 and 06 for efficient architectures (sliding window attention, sparse attention)

**Dong et al. (2024)** - Harry Dong, Xinyu Yang, Zhenyu (Allen) Zhang, Zhangyang Wang, Yuejie Chi, and Beidi Chen. Get more with less: Synthesizing recurrence with kv cache compression for efficient llm inference. ArXiv, abs/2402.09398, 2024. URL https://api.semanticscholar.org/CorpusID:267657553.
- Cited in section 06 for infinite context methods (KV cache compression)

**Han et al. (2023)** - Chi Han, Qifan Wang, Wenhan Xiong, Yu Chen, Heng Ji, and Sinong Wang. Lm-infinite: Simple on-the-fly length generalization for large language models, 2023.
- Cited in section 06 for infinite context methods

**Zhang et al. (2024a)** - Peitian Zhang, Zheng Liu, Shitao Xiao, Ninglu Shao, Qiwei Ye, and Zhicheng Dou. Soaring from 4k to 400k: Extending llm's context with activation beacon. ArXiv, abs/2401.03462, 2024a. URL https://api.semanticscholar.org/CorpusID:266844488.
- Cited in section 06 for long-context extension methods

**Cai et al. (2024)** - Zefan Cai, Yichi Zhang, Bofei Gao, Yuliang Liu, Tianyu Liu, Keming Lu, Wayne Xiong, Yue Dong, Baobao Chang, Junjie Hu, and Wen Xiao. Pyramidkv: Dynamic kv cache compression based on pyramidal information funneling. ArXiv, abs/2406.02069, 2024. URL https://api.semanticscholar.org/CorpusID:270226243.
- Cited in section 06 for KV cache compression

**Lin et al. (2024a)** - Bin Lin, Tao Peng, Chen Zhang, Minmin Sun, Lanbo Li, Hanyu Zhao, Wencong Xiao, Qi Xu, Xiafei Qiu, Shen Li, Zhigang Ji, Yong Li, and Wei Lin. Infinite-llm: Efficient llm service for long context with distattention and distributed kv cache. ArXiv, abs/2401.02669, 2024a. URL https://api.semanticscholar.org/CorpusID:266818470.
- Cited in section 06 for infinite context methods

**Lin et al. (2024b)** - Hongzhan Lin, Ang Lv, Yuhan Chen, Chen Zhu, Yang Song, Hengshu Zhu, and Rui Yan. Mixture of in-context experts enhance llms' long context awareness. ArXiv, abs/2406.19598, 2024b. URL https://api.semanticscholar.org/CorpusID:270845965.
- Cited in sections 01 and 06 for RoPE base frequency correction and long context awareness

## Related Work - Length Extrapolation Methods

**Han et al. (2024)** - Chi Han, Qifan Wang, Hao Peng, Wenhan Xiong, Yu Chen, Heng Ji, and Sinong Wang. Lm-infinite: Zero-shot extreme length generalization for large language models. In Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), pp. 3991–4008, 2024.
- Cited in section 06 for length extrapolation

**An et al. (2024a)** - Chenxin An, Fei Huang, Jun Zhang, Shansan Gong, Xipeng Qiu, Chang Zhou, and Lingpeng Kong. Training-free long-context scaling of large language models, 2024a.
- Cited in sections 04, 05, and 06 for training-free extrapolation methods

**Ma et al. (2024; should have suffix)** - Xindian Ma, Wenyuan Liu, Peng Zhang, and Nan Xu. 3d-rpe: Enhancing long-context modeling through 3d rotary position encoding. ArXiv, abs/2406.09897, 2024. URL https://api.semanticscholar.org/CorpusID:270312302.
- Cited in section 06 for position encoding extrapolation

**Men et al. (2024)** - Xin Men, Mingyu Xu, Bingning Wang, Qingyu Zhang, Hongyu Lin, Xianpei Han, and Weipeng Chen. Base of rope bounds context length. ArXiv, abs/2405.14591, 2024. URL https://api.semanticscholar.org/CorpusID:269811770.
- Cited in section 06 for RoPE base frequency analysis

**Zhong et al. (2024)** - Meizhi Zhong, Chen Zhang, Yikun Lei, Xikai Liu, Yan Gao, Yao Hu, Kehai Chen, and Min Zhang. Understanding the rope extensions of long-context llms: An attention perspective. ArXiv, abs/2406.13282, 2024. URL https://api.semanticscholar.org/CorpusID:270820800.
- Cited in section 06 for understanding RoPE extensions

**Wang et al. (2024b)** - Suyuchen Wang, Ivan Kobyzev, Peng Lu, Mehdi Rezagholizadeh, and Bang Liu. Resonance rope: Improving context length generalization of large language models. In Annual Meeting of the Association for Computational Linguistics, 2024b. URL https://api.semanticscholar.org/CorpusID:268201728.
- Cited in sections 05 and 06 for RoPE extrapolation methods

**Zheng et al. (2024)** - Chuanyang Zheng, Yihang Gao, Han Shi, Minbin Huang, Jingyao Li, Jing Xiong, Xiaozhe Ren, Michael Ng, Xin Jiang, Zhenguo Li, and Yu Li. Dape: Data-adaptive positional encoding for length extrapolation, 2024. URL https://arxiv.org/abs/2405.14722.
- Cited in section 05 for NIAH evaluation

**Liu et al. (2024b)** - Xiaoran Liu, Qipeng Guo, Yuerong Song, Zhigeng Liu, Kai Lv, Hang Yan, Linlin Li, Qun Liu, and Xipeng Qiu. Farewell to length extrapolation, a training-free infinite context with finite attention scope. ArXiv, abs/2407.15176, 2024b. URL https://api.semanticscholar.org/CorpusID:271328963.
- Cited in section 05 for NIAH evaluation
