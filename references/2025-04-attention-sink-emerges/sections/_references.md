# References

This file contains bibliographic information for works cited in the section notes.

## Ba et al., 2016
**Citation format in notes:** Ba et al., 2016; Ba et al. (2016)

Jimmy Lei Ba, Jamie Ryan Kiros, and Geoffrey E. Hinton. Layer normalization. *arXiv preprint arXiv:1607.06450*, 2016.

**Cited in:** 02_preliminaries.md (LN in transformer blocks), 07_effects-of-model-architecture.md (pre-norm and post-norm structure)

## Biderman et al., 2023
**Citation format in notes:** Biderman et al., 2023; Biderman et al. (2023)

Stella Biderman, Hailey Schoelkopf, Quentin Gregory Anthony, Herbie Bradley, Kyle O'Brien, Eric Hallahan, Mohammad Aflah Khan, Shivanshu Purohit, USVSN Sai Prashanth, Edward Raff, et al. Pythia: A suite for analyzing large language models across training and scaling. In *International Conference on Machine Learning*, pp. 2397–2430. PMLR, 2023.

**Cited in:** 03_properties-of-attention-sink.md (model scale evaluation)

## Bondarenko et al., 2023
**Citation format in notes:** Bondarenko et al., 2023; Bondarenko et al. (2023)

Yelysei Bondarenko, Markus Nagel, and Tijmen Blankevoort. Quantizable transformers: Removing outliers by helping attention heads do nothing. *Advances in Neural Information Processing Systems*, 36:75067–75096, 2023.

**Cited in:** 09_appendix-a-related-work.md (strong outliers in Transformer models, activation outliers, understanding attention sink, mitigation strategies)

## Brown et al., 2020
**Citation format in notes:** Brown et al., 2020; Brown et al. (2020)

Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel Ziegler, Jeffrey Wu, Clemens Winter, Chris Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, and Dario Amodei. Language models are few-shot learners. *Advances in neural information processing systems*, 33, 2020.

**Cited in:** 02_preliminaries.md (learnable PE)

## Cancedda, 2024
**Citation format in notes:** Cancedda, 2024; Cancedda (2024)

Nicola Cancedda. Spectral filters, dark signals, and attention sinks. *arXiv preprint arXiv:2402.09221*, 2024.

**Cited in:** 01_introduction.md (understanding attention sink, massive activations), 03_properties-of-attention-sink.md (first token massive activations), 09_appendix-a-related-work.md (FFNs in LLaMA2, massive activations)

## Chen et al., 2024
**Citation format in notes:** Chen et al., 2024; Chen et al. (2024)

Liang Chen, Haozhe Zhao, Tianyu Liu, Shuai Bai, Junyang Lin, Chang Zhou, and Baobao Chang. An image is worth 1/2 tokens after layer 2: plug-and-play inference acceleration for large vision-language models. *arXiv preprint arXiv:2403.06764*, 2024.

**Cited in:** 01_introduction.md (efficient inference application), 09_appendix-a-related-work.md (efficient inference application)

## Darcet et al., 2023
**Citation format in notes:** Darcet et al., 2023; Darcet et al. (2023)

Timothée Darcet, Maxime Oquab, Julien Mairal, and Piotr Bojanowski. Vision transformers need registers. *arXiv preprint arXiv:2309.16588*, 2023.

**Cited in:** 09_appendix-a-related-work.md (artifacts in attention maps in vision transformers)

## Dehghani et al., 2023
**Citation format in notes:** Dehghani et al., 2023; Dehghani et al. (2023)

Mostafa Dehghani, Josip Djolonga, Basil Mustafa, Piotr Pudlewski, Jonathan Heek, Justin Gilmer, Andreas Peter Steiner, Mathilde Caron, Robert Geirhos, Ibrahim Alabdulmohsin, et al. Scaling vision transformers to 22 billion parameters. In *International Conference on Machine Learning*, pp. 7480–7512. PMLR, 2023.

**Cited in:** 09_appendix-a-related-work.md (attention logit growth, qk-norm for attention entropy collapse)

## Dettmers et al., 2022
**Citation format in notes:** Dettmers et al., 2022; Dettmers et al. (2022)

Tim Dettmers, Mike Lewis, Younes Belkada, and Luke Zettlemoyer. Gpt3. int8 (): 8-bit matrix multiplication for transformers at scale. *Advances in Neural Information Processing Systems*, 35:30318–30332, 2022.

**Cited in:** 09_appendix-a-related-work.md (channel-wise activation outlier)

## Devlin et al., 2019
**Citation format in notes:** Devlin et al., 2019; Devlin et al. (2019)

Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. Bert: Pre-training of deep bidirectional transformers for language understanding. In *Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers)*, pp. 4171–4186, 2019.

**Cited in:** 02_preliminaries.md (learnable PE), 09_appendix-a-related-work.md (encoder-only LMs)

## Devoto et al., 2024
**Citation format in notes:** Devoto et al., 2024; Devoto et al. (2024)

Alessio Devoto, Yu Zhao, Simone Scardapane, and Pasquale Minervini. A simple and effective $\ell_2$ norm-based strategy for KV cache compression. *arXiv preprint arXiv:2406.11430*, 2024.

**Cited in:** 03_properties-of-attention-sink.md (small $\ell_2$-norm of keys and values)

## Dubey et al., 2024
**Citation format in notes:** Dubey et al., 2024; Dubey et al. (2024)

Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Amy Yang, Angela Fan, et al. The llama 3 herd of models. *arXiv preprint arXiv:2407.21783*, 2024.

**Cited in:** 03_properties-of-attention-sink.md (LLaMA3-8B Base analysis, model scale evaluation)

## Gao et al., 2020
**Citation format in notes:** Gao et al., 2020; Gao et al. (2020)

Leo Gao, Stella Biderman, Sid Black, Laurence Golding, Travis Hoppe, Charles Foster, Jason Phang, Horace He, Anish Thite, Noa Nabeshima, et al. The pile: An 800gb dataset of diverse text for language modeling. *arXiv preprint arXiv:2101.00027*, 2020.

**Cited in:** 03_properties-of-attention-sink.md (Pile dataset domains), 04_effects-of-optimization.md (data distribution, validation loss)

## Ge et al., 2023
**Citation format in notes:** Ge et al., 2023; Ge et al. (2023)

Suyu Ge, Yunan Zhang, Liyuan Liu, Minjia Zhang, Jiawei Han, and Jianfeng Gao. Model tells you what to discard: Adaptive kv cache compression for llms. *arXiv preprint arXiv:2310.01801*, 2023.

**Cited in:** 01_introduction.md (KV cache optimization application), 09_appendix-a-related-work.md (KV cache optimization application)

## Guo et al., 2024a
**Citation format in notes:** Guo et al., 2024a; Guo et al. (2024a)

Tianyu Guo, Druv Pai, Yu Bai, Jiantao Jiao, Michael I Jordan, and Song Mei. Active-dormant attention heads: Mechanically demystifying extreme-token phenomena in llms. *arXiv preprint arXiv:2410.13835*, 2024a.

**Cited in:** 09_appendix-a-related-work.md (empirical and theoretical analysis of attention sink on BB task, mutual reinforcement mechanism)

## Guo et al., 2024b
**Citation format in notes:** Guo et al., 2024b; Guo et al. (2024b)

Zhiyu Guo, Hidetaka Kamigaito, and Taro Watanabe. Attention score is not all you need for token importance indicator in kv cache reduction: Value also matters. *arXiv preprint arXiv:2406.12335*, 2024b.

**Cited in:** 03_properties-of-attention-sink.md (observation about small $\ell_2$-norm of keys and values), 09_appendix-a-related-work.md (values associated with sink tokens are typically smaller)

## Han et al., 2024
**Citation format in notes:** Han et al., 2024; Han et al. (2024)

Chi Han, Qifan Wang, Hao Peng, Wenhan Xiong, Yu Chen, Heng Ji, and Sinong Wang. Lm-infinite: Zero-shot extreme length generalization for large language models. In *Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)*, pp. 4008–4024, 2024.

**Cited in:** 01_introduction.md (streaming/long context generation application), 09_appendix-a-related-work.md (significance of first few tokens, streaming/long context generation application)

## He et al., 2016
**Citation format in notes:** He et al., 2016; He et al. (2016)

Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Deep residual learning for image recognition. In *Proceedings of the IEEE conference on computer vision and pattern recognition*, pp. 770–778, 2016.

**Cited in:** 07_effects-of-model-architecture.md (residual connections)

## He et al., 2024
**Citation format in notes:** He et al., 2024; He et al. (2024)

Bobby He, Lorenzo Noci, Daniele Paliotta, Imanol Schlag, and Thomas Hofmann. Understanding and minimising outlier features in transformer training. In *Advances in Neural Information Processing Systems*, 2024.

**Cited in:** 09_appendix-a-related-work.md (protected block, role of optimization in mitigating outliers)

## Huang et al., 2024
**Citation format in notes:** Huang et al., 2024; Huang et al. (2024)

Wei Huang, Haotong Qin, Yangdong Liu, Yawei Li, Xianglong Liu, Luca Benini, Michele Magno, and Xiaojuan Qi. Slim-llm: Salience-driven mixed-precision quantization for large language models. *arXiv preprint arXiv:2405.14917*, 2024.

**Cited in:** 01_introduction.md (model quantization application), 09_appendix-a-related-work.md (model quantization application)

## Jiang et al., 2023
**Citation format in notes:** Jiang et al., 2023; Jiang et al. (2023)

Albert Q Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Devendra Singh Chaplot, Diego de las Casas, Florian Bressand, Gianna Lengyel, Guillaume Lample, Lucile Saulnier, et al. Mistral 7b. *arXiv preprint arXiv:2310.06825*, 2023.

**Cited in:** 03_properties-of-attention-sink.md (Mistral model)

## Katharopoulos et al., 2020
**Citation format in notes:** Katharopoulos et al., 2020; Katharopoulos et al. (2020)

Angelos Katharopoulos, Apoorv Vyas, Nikolaos Pappas, and François Fleuret. Transformers are rnns: Fast autoregressive transformers with linear attention. In *International conference on machine learning*, pp. 5156–5165. PMLR, 2020.

**Cited in:** 07_effects-of-model-architecture.md (linear attention, kernel functions)

## Kazemnejad et al., 2024
**Citation format in notes:** Kazemnejad et al., 2024; Kazemnejad et al. (2024)

Amirhossein Kazemnejad, Inkit Padhi, Karthikeyan Natesan Ramamurthy, Payel Das, and Siva Reddy. The impact of positional encoding on length generalization in transformers. *Advances in Neural Information Processing Systems*, 36, 2024.

**Cited in:** 02_preliminaries.md (NoPE - no explicit positional embedding), 10_appendix-b-positional-embedding-formulations.md (NoPE definition)

## Liu et al., 2024a
**Citation format in notes:** Liu et al., 2024a; Liu et al. (2024a)

Referenced in 04_effects-of-optimization.md (implementation repo, experimental setup)

## Lin et al., 2024
**Citation format in notes:** Lin et al., 2024; Lin et al. (2024)

Haokun Lin, Haobo Xu, Yichen Wu, Jingzhi Cui, Yingtao Zhang, Linzhan Mou, Linqi Song, Zhenan Sun, and Ying Wei. Duquant: Distributing outliers via dual transformation makes stronger quantized llms. In *The Thirty-eighth Annual Conference on Neural Information Processing Systems*, 2024.

**Cited in:** 09_appendix-a-related-work.md (token-wise activation outlier)

## Liu et al., 2024b
**Citation format in notes:** Liu et al., 2024b; Liu et al. (2024b)

Ruikang Liu, Haoli Bai, Haokun Lin, Yuening Li, Han Gao, Zhengzhuo Xu, Lu Hou, Jun Yao, and Chun Yuan. Intactkv: Improving large language model quantization by keeping pivot tokens intact. *arXiv preprint arXiv:2403.01241*, 2024b.

**Cited in:** 01_introduction.md (model quantization application), 09_appendix-a-related-work.md (model quantization application)

## Loshchilov & Hutter, 2017
**Citation format in notes:** Loshchilov & Hutter, 2017; Loshchilov & Hutter (2017)

Referenced in 04_effects-of-optimization.md (AdamW optimizer)

## Ouyang et al., 2022
**Citation format in notes:** Ouyang et al., 2022; Ouyang et al. (2022)

Referenced in 01_introduction.md (instruction tuning, pre-training motivation), 03_properties-of-attention-sink.md (instruction tuning)

## Miller, 2023
**Citation format in notes:** Miller, 2023; Miller (2023)

Evan Miller. Attention is off by one. *URL https://www.evanmiller.org/attention-is-off-by-one.html*, 2023.

**Cited in:** 09_appendix-a-related-work.md (softmax-off-by-one)

## Press et al., 2021
**Citation format in notes:** Press et al., 2021; Press et al. (2021)

Ofir Press, Noah A Smith, and Mike Lewis. Train short, test long: Attention with linear biases enables input length extrapolation. *arXiv preprint arXiv:2108.12409*, 2021.

**Cited in:** 02_preliminaries.md (ALiBi positional embedding), 10_appendix-b-positional-embedding-formulations.md (ALiBi definition)

## Radford et al., 2019
**Citation format in notes:** Radford et al., 2019; Radford et al. (2019)

Referenced in 03_properties-of-attention-sink.md (GPT2 model family)

## Raffel et al., 2020
**Citation format in notes:** Raffel et al., 2020; Raffel et al. (2020)

Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, and Peter J Liu. Exploring the limits of transfer learning with a unified text-to-text transformer. *Journal of machine learning research*, 21(140):1–67, 2020.

**Cited in:** 02_preliminaries.md (relative PE), 10_appendix-b-positional-embedding-formulations.md (relative PE in T5)

## Shazeer, 2020
**Citation format in notes:** Shazeer, 2020; Shazeer (2020)

Referenced in 04_effects-of-optimization.md (SwiGLU activation)

## Su et al., 2024
**Citation format in notes:** Su et al., 2024; Su et al. (2024)

Jianlin Su, Murtadha Ahmed, Yu Lu, Shengfeng Pan, Wen Bo, and Yunfeng Liu. Roformer: Enhanced transformer with rotary position embedding. *Neurocomputing*, 568:127063, 2024.

**Cited in:** 02_preliminaries.md (Rotary PE), 03_properties-of-attention-sink.md (Rotary), 04_effects-of-optimization.md (Rotary), 08_future-work.md (attention sink on word tokens), 10_appendix-b-positional-embedding-formulations.md (Rotary definition)

## Sun et al., 2024
**Citation format in notes:** Sun et al., 2024; Sun et al. (2024)

Mingjie Sun, Xinlei Chen, J Zico Kolter, and Zhuang Liu. Massive activations in large language models. *arXiv preprint arXiv:2402.17762*, 2024.

**Cited in:** 01_introduction.md (massive activations, attention sink on word tokens), 03_properties-of-attention-sink.md (massive activations), 07_effects-of-model-architecture.md (learnable parameters in attention, KV biases), 08_future-work.md (attention sink on word tokens), 09_appendix-a-related-work.md (massive activations, token-wise activation outlier, attention sink at first position, implicit biases in keys and values)

## Touvron et al., 2023
**Citation format in notes:** Touvron et al., 2023; Touvron et al. (2023)

Referenced in 03_properties-of-attention-sink.md (LLaMA2 Base model family)

## Vaswani et al., 2017
**Citation format in notes:** Vaswani et al., 2017; Vaswani et al. (2017)

Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz Kaiser, and Illia Polosukhin. Attention is all you need. *Advances in neural information processing systems*, 30, 2017.

**Cited in:** 02_preliminaries.md (absolute PE), 09_appendix-a-related-work.md (Transformer models), 10_appendix-b-positional-embedding-formulations.md (absolute PE definition)

## Wan et al., 2024
**Citation format in notes:** Wan et al., 2024; Wan et al. (2024)

Zhongwei Wan, Ziang Wu, Che Liu, Jinfa Huang, Zhihong Zhu, Peng Jin, Longyue Wang, and Li Yuan. Look-m: Look-once optimization in kv cache for efficient multimodal long-context inference. *arXiv preprint arXiv:2406.18139*, 2024.

**Cited in:** 01_introduction.md (KV cache optimization application), 09_appendix-a-related-work.md (KV cache optimization application)

## Wang et al., 2022
**Citation format in notes:** Wang et al., 2022; Wang et al. (2022)

Referenced in 06_effects-of-loss-function.md (prefix language modeling motivation)

## Wortsman et al., 2023
**Citation format in notes:** Wortsman et al., 2023; Wortsman et al. (2023)

Mitchell Wortsman, Peter J Liu, Lechao Xiao, Katie Everett, Alex Alemi, Ben Adlam, John D Co-Reyes, Izzeddin Gur, Abhishek Kumar, Roman Novak, et al. Small-scale proxies for large-scale transformer training instabilities. *arXiv preprint arXiv:2309.14322*, 2023.

**Cited in:** 09_appendix-a-related-work.md (attention logit growth)

## Wu & Tu, 2024
**Citation format in notes:** Wu & Tu, 2024; Wu & Tu (2024)

Haoyu Wu and Kewei Tu. Layer-condensed kv cache for efficient inference of large language models. *arXiv preprint arXiv:2405.10637*, 2024.

**Cited in:** 01_introduction.md (KV cache optimization application), 09_appendix-a-related-work.md (KV cache optimization application)

## Xiao et al., 2023a
**Citation format in notes:** Xiao et al., 2023a; Xiao et al. (2023a)

Guangxuan Xiao, Ji Lin, Mickael Seznec, Hao Wu, Julien Demouth, and Song Han. Smoothquant: Accurate and efficient post-training quantization for large language models. In *International Conference on Machine Learning*, pp. 38087–38099. PMLR, 2023a.

**Cited in:** 09_appendix-a-related-work.md (channel-wise activation outlier)

## Xiao et al., 2023b
**Citation format in notes:** Xiao et al., 2023b; Xiao et al. (2023b)

Guangxuan Xiao, Yuandong Tian, Beidi Chen, Song Han, and Mike Lewis. Efficient streaming language models with attention sinks. *arXiv preprint arXiv:2309.17453*, 2023b.

**Cited in:** 01_introduction.md (attention sink phenomenon, applications), 02_preliminaries.md (attention sink definition), 03_properties-of-attention-sink.md (threshold-based metrics), 05_effects-of-data-distribution.md (learnable token in first position), 07_effects-of-model-architecture.md (learnable sink token), 09_appendix-a-related-work.md (introducing term attention sink, softmax-off-by-one, streaming/long context generation application)

## Yang et al., 2024
**Citation format in notes:** Yang et al., 2024; Yang et al. (2024)

Shuai Yang, Yuying Ge, Yang Li, Yukang Chen, Yixiao Ge, Ying Shan, and Yingcong Chen. Seed-story: Multimodal long story generation with large language model. *arXiv preprint arXiv:2407.08683*, 2024.

**Cited in:** 01_introduction.md (streaming/long context generation application), 09_appendix-a-related-work.md (streaming/long context generation application)

## Yin et al., 2024
**Citation format in notes:** Yin et al., 2024; Yin et al. (2024)

Qingyu Yin, Xuzheng He, Xiang Zhuang, Yu Zhao, Jianhua Yao, Xiaoyu Shen, and Qiang Zhang. Stablemask: Refining causal masking in decoder-only transformer. *arXiv preprint arXiv:2402.04779*, 2024.

**Cited in:** 09_appendix-a-related-work.md (refining causal mask with pseudo-attention to reduce attention sink)

## Yu et al., 2024
**Citation format in notes:** Yu et al., 2024; Yu et al. (2024)

Zhongzhi Yu, Zheng Wang, Yonggan Fu, Huihong Shi, Khalid Shaikh, and Yingyan Celine Lin. Unveiling and harnessing hidden attention sinks: Empowering the acceleration of text generation without model retraining. *arXiv preprint arXiv:2406.15765*, 2024.

**Cited in:** 01_introduction.md (attention sink on word tokens), 08_future-work.md (attention sink on word tokens), 09_appendix-a-related-work.md (attention sink at first position in auto-regressive LMs)

## Zhang & Sennrich, 2019
**Citation format in notes:** Zhang & Sennrich, 2019; Zhang & Sennrich (2019)

Referenced in 02_preliminaries.md (LN), 03_properties-of-attention-sink.md (RMSNorm), 04_effects-of-optimization.md (RMSNorm), 07_effects-of-model-architecture.md (LN)

## Zhang et al., 2022
**Citation format in notes:** Zhang et al., 2022

Referenced in 03_properties-of-attention-sink.md (OPT model family)

## Zhang et al., 2024a
**Citation format in notes:** Zhang et al., 2024a

Referenced in 04_effects-of-optimization.md (implementation repo)

## Zhai et al., 2023
**Citation format in notes:** Zhai et al., 2023; Zhai et al. (2023)

Shuangfei Zhai, Tatiana Likhomanenko, Etai Littwin, Dan Busbridge, Jason Ramapuram, Yizhe Zhang, Jiatao Gu, and Joshua M Susskind. Stabilizing transformer training by preventing attention entropy collapse. In *International Conference on Machine Learning*, pp. 40770–40803. PMLR, 2023.

**Cited in:** 09_appendix-a-related-work.md (attention entropy collapse, σReparam)

## Zhang et al., 2024b
**Citation format in notes:** Zhang et al., 2024b; Zhang et al. (2024b)

Zhenyu Zhang, Shiwei Liu, Runjin Chen, Bhavya Kailkhura, Beidi Chen, and Atlas Wang. Q-hitter: A better token oracle for efficient llm inference via sparse-quantized kv cache. *Proceedings of Machine Learning and Systems*, 6:381–394, 2024b.

**Cited in:** 01_introduction.md (efficient inference application), 09_appendix-a-related-work.md (efficient inference application)

## Ding et al., 2023
**Citation format in notes:** Ding et al., 2023; Ding et al. (2023)

Ning Ding, Yulin Chen, Bokai Xu, Yujia Qin, Zhi Zheng, Shengding Hu, Zhiyuan Liu, Maosong Sun, and Bowen Zhou. Enhancing chat language models by scaling high-quality instructional conversations. *arXiv preprint arXiv:2305.14233*, 2023.

**Cited in:** 13_appendix-e-more-experiments-after-pre-training.md (UltraChat dataset)

## Fedus et al., 2022
**Citation format in notes:** Fedus et al., 2022; Fedus et al. (2022)

William Fedus, Barret Zoph, and Noam Shazeer. Switch transformers: Scaling to trillion parameter models with simple and efficient sparsity. *Journal of Machine Learning Research*, 23(120):1–39, 2022.

**Cited in:** 11_appendix-c-attention-sink-in-open-sourced-lms.md (Jamba MoE layers)

## Gao et al., 2024
**Citation format in notes:** Gao et al., 2024; Gao et al. (2024)

Leo Gao, Jonathan Tow, Baber Abbasi, Stella Biderman, Sid Black, Anthony DiPofi, Charles Foster, Laurence Golding, Jeffrey Hsu, Alain Le Noac'h, Haonan Li, Kyle McDonell, Niklas Muennighoff, Chris Ociepa, Jason Phang, Laria Reynolds, Hailey Schoelkopf, Aviya Skowron, Lintang Sutawika, Eric Tang, Anish Thite, Ben Wang, Kevin Wang, and Andy Zou. A framework for few-shot language model evaluation, 07 2024.

**Cited in:** 11_appendix-c-attention-sink-in-open-sourced-lms.md (LM evaluation platform for downstream tasks)

## Gu & Dao, 2023
**Citation format in notes:** Gu & Dao, 2023; Gu & Dao (2023)

Albert Gu and Tri Dao. Mamba: Linear-time sequence modeling with selective state spaces. *arXiv preprint arXiv:2312.00752*, 2023.

**Cited in:** 11_appendix-c-attention-sink-in-open-sourced-lms.md (Mamba layers in Jamba)

## Hendrycks & Gimpel, 2016
**Citation format in notes:** Hendrycks & Gimpel, 2016; Hendrycks & Gimpel (2016)

Dan Hendrycks and Kevin Gimpel. Gaussian error linear units (gelus). *arXiv preprint arXiv:1606.08415*, 2016.

**Cited in:** 12_appendix-d-more-experiments-in-lm-pre-training.md (GeLU activation function)

## Kaul et al., 2024
**Citation format in notes:** Kaul et al., 2024; Kaul et al. (2024)

Prannay Kaul, Chengcheng Ma, Ismail Elezi, and Jiankang Deng. From attention to activation: Unravelling the enigmas of large language models. *arXiv preprint arXiv:2410.17174*, 2024.

**Cited in:** 09_appendix-a-related-work.md (concurrent study on distinct outlier types, softmax-off-by-one, OrthoAdam)

## Kingma & Ba, 2014
**Citation format in notes:** Kingma & Ba, 2014; Kingma & Ba (2014)

Diederik Kingma and Jimmy Ba. Adam: A method for stochastic optimization. *arXiv preprint arXiv:1412.6980*, 2014.

**Cited in:** 12_appendix-d-more-experiments-in-lm-pre-training.md (Adam optimizer)

## Lieber et al., 2024
**Citation format in notes:** Lieber et al., 2024; Lieber et al. (2024)

Opher Lieber, Barak Lenz, Hofit Bata, Gal Cohen, Jhonatan Osin, Itay Dalmedigos, Erez Safahi, Shaked Meirom, Yonatan Belinkov, Shai Shalev-Shwartz, et al. Jamba: A hybrid transformer-mamba language model. *arXiv preprint arXiv:2403.19887*, 2024.

**Cited in:** 11_appendix-c-attention-sink-in-open-sourced-lms.md (Jamba-v0.1 model)

## Ramachandran et al., 2017
**Citation format in notes:** Ramachandran et al., 2017; Ramachandran et al. (2017)

Prajit Ramachandran, Barret Zoph, and Quoc V Le. Searching for activation functions. *arXiv preprint arXiv:1710.05941*, 2017.

**Cited in:** 12_appendix-d-more-experiments-in-lm-pre-training.md (Swish activation function)

## Ramapuram et al., 2024
**Citation format in notes:** Ramapuram et al., 2024; Ramapuram et al. (2024)

Jason Ramapuram, Federico Danieli, Eeshan Dhekane, Floris Weers, Dan Busbridge, Pierre Ablin, Tatiana Likhomanenko, Jagrit Digani, Zijin Gu, Amitis Shidani, et al. Theory, analysis, and best practices for sigmoid self-attention. *arXiv preprint arXiv:2409.04431*, 2024.

**Cited in:** 13_appendix-e-more-experiments-after-pre-training.md (theory and practices for sigmoid attention)

## Shazeer et al., 2017
**Citation format in notes:** Shazeer et al., 2017; Shazeer et al. (2017)

Noam Shazeer, Azalia Mirhoseini, Krzysztof Maziarz, Andy Davis, Quoc Le, Geoffrey Hinton, and Jeff Dean. Outrageously large neural networks: The sparsely-gated mixture-of-experts layer. *arXiv preprint arXiv:1701.06538*, 2017.

**Cited in:** 11_appendix-c-attention-sink-in-open-sourced-lms.md (MoE layers in Jamba)

## Team et al., 2024
**Citation format in notes:** Team et al., 2024; Team et al. (2024)

Jamba Team, Barak Lenz, Alan Arazi, Amir Bergman, Avshalom Manevich, Barak Peleg, Ben Aviram, Chen Almagor, Clara Fridman, Dan Padnos, et al. Jamba-1.5: Hybrid transformer-mamba models at scale. *arXiv preprint arXiv:2408.12570*, 2024.

**Cited in:** 11_appendix-c-attention-sink-in-open-sourced-lms.md (Jamba-1.5 Mini model)

## Zellers et al., 2019
**Citation format in notes:** Zellers et al., 2019; Zellers et al. (2019)

Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali Farhadi, and Yejin Choi. Hellaswag: Can a machine really finish your sentence? *arXiv preprint arXiv:1905.07830*, 2019.

**Cited in:** 11_appendix-c-attention-sink-in-open-sourced-lms.md (HellaSwag downstream LM task)
