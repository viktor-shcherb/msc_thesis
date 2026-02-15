# References

This file contains only the references that are cited in the section notes.

## [1] Anthropic
Anthropic. Model card and evaluations for claude models, July 2023. URL https://www.anthropic.com/product.

**Cited in:** 01_introduction.md (recent advances in long-context language modeling); 05_intrinsic-and-influence.md (extractive QA evaluation methodology)

## [2] Qwen
Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Kai Dang, Xiaodong Deng, Yang Fan, Wenbin Ge, Yu Han, Fei Huang, et al. Qwen technical report. arXiv preprint arXiv:2309.16609, 2023.

**Cited in:** 01_introduction.md (model family studied); 03_detecting-retrieval-head-continued.md (Qwen1.5-14B-Chat alignment study)

## [3] Transformer Circuits Thread
Trenton Bricken, Adly Templeton, Joshua Batson, Brian Chen, Adam Jermyn, Tom Conerly, Nick Turner, Cem Anil, Carson Denison, Amanda Askell, Robert Lasenby, Yifan Wu, Shauna Kravec, Nicholas Schiefer, Tim Maxwell, Nicholas Joseph, Zac Hatfield-Dodds, Alex Tamkin, Karina Nguyen, Brayden McLean, Josiah E Burke, Tristan Hume, Shan Carter, Tom Henighan, and Christopher Olah. Towards monosemantic feature directions in transformer circuits. Transformer Circuits Thread, 2023. https://transformer-circuits.pub/2023/monosemantic-features/index.html.

**Cited in:** 01_introduction.md (mechanistic interpretability field)

## [4] GSM8K
Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, Christopher Hesse, and John Schulman. Training verifiers to solve math word problems, 2021.

**Cited in:** 05_intrinsic-and-influence.md (chain-of-thought reasoning evaluation)

## [5] Griffin
Soham De, Samuel L Smith, Anushan Fernando, Aleksandar Botev, George Cristian-Muraru, Albert Gu, Ruba Haroun, Leonard Berrada, Yutian Chen, Srivatsan Srinivasan, et al. Griffin: Mixing gated linear recurrences with local attention for efficient language models. arXiv preprint arXiv:2402.19427, 2024.

**Cited in:** 06_discussions.md (hybrid architectures)

## [6] Data engineering for scaling language models
Yao Fu, Rameswar Panda, Xinyao Niu, Xiang Yue, Hannaneh Hajishirzi, Yoon Kim, and Hao Peng. Data engineering for scaling language models to 128k context. arXiv preprint arXiv:2402.10171, 2024.

**Cited in:** 01_introduction.md (recent advances in long-context language modeling); 03_detecting-retrieval-head-continued.md (Llama-2-7B-80K and Llama-2-13B-60K continued pretraining); 04_basic-properties-continued.md (intrinsic property)

## [7] Model tells you what to discard
Suyu Ge, Yunan Zhang, Liyuan Liu, Minjia Zhang, Jiawei Han, and Jianfeng Gao. Model tells you what to discard: Adaptive kv cache compression for llms. arXiv preprint arXiv:2310.01801, 2023.

**Cited in:** 01_introduction.md (KV cache compression)

## [8] Transformer feed-forward layers are key-value memories
Mor Geva, Roei Schuster, Jonathan Berant, and Omer Levy. Transformer feed-forward layers are key-value memories. arXiv preprint arXiv:2012.14913, 2020.

**Cited in:** 05_intrinsic-and-influence.md (FFN layers store knowledge); 06_discussions.md (FFN layers for storing knowledge)

## [9] Mamba
Albert Gu and Tri Dao. Mamba: Linear-time sequence modeling with selective state spaces. arXiv preprint arXiv:2312.00752, 2023.

**Cited in:** 06_discussions.md (state space models)

## [10] CopyNet
Jiatao Gu, Zhengdong Lu, Hang Li, and Victor O.K. Li. Incorporating copying mechanism in sequence-to-sequence learning. In Katrin Erk and Noah A. Smith, editors, Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 1631–1640, Berlin, Germany, August 2016. Association for Computational Linguistics. doi: 10.18653/v1/P16-1154. URL https://aclanthology.org/P16-1154.

**Cited in:** 01_introduction.md (inspiration for retrieval head concept)

## [11] MMLU
Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn Song, and Jacob Steinhardt. Measuring massive multitask language understanding. In International Conference on Learning Representations, 2020.

**Cited in:** 05_intrinsic-and-influence.md (chain-of-thought reasoning evaluation)

## [12] Mistral 7B
Albert Q Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Devendra Singh Chaplot, Diego de las Casas, Florian Bressand, Gianna Lengyel, Guillaume Lample, Lucile Saulnier, et al. Mistral 7b. arXiv preprint arXiv:2310.06825, 2023.

**Cited in:** 01_introduction.md (model family studied); 06_discussions.md (sliding window attention in v0.1 cannot pass needle-in-a-haystack)

## [13] Mixtral of experts
Albert Q Jiang, Alexandre Sablayrolles, Antoine Roux, Arthur Mensch, Blanche Savary, Chris Bamford, Devendra Singh Chaplot, Diego de las Casas, Emma Bou Hanna, Florian Bressand, et al. Mixtral of experts. arXiv preprint arXiv:2401.04088, 2024.

**Cited in:** 01_introduction.md (sparse upcycling); 03_detecting-retrieval-head-continued.md (Mixtral-8x7B-v0.1 sparse upcycling study)

## [14] Needle in a haystack
Greg Kamradt. Needle in a haystack - pressure testing llms. https://github.com/gkamradt/LLMTest_NeedleInAHaystack, 2023.

**Cited in:** 01_introduction.md (needle-in-a-haystack test)

## [15] GEAR
Hao Kang, Qingru Zhang, Souvik Kundu, Geonhwa Jeong, Zaoxing Liu, Tushar Krishna, and Tuo Zhao. Gear: An efficient kv cache compression recipefor near-lossless generative inference of llm. arXiv preprint arXiv:2403.05527, 2024.

**Cited in:** 01_introduction.md (KV cache compression)

## [16] Sparse upcycling
Aran Komatsuzaki, Joan Puigcerver, James Lee-Thorp, Carlos Riquelme Ruiz, Basil Mustafa, Joshua Ainslie, Yi Tay, Mostafa Dehghani, and Neil Houlsby. Sparse upcycling: Training mixture-of-experts from dense checkpoints. arXiv preprint arXiv:2212.05055, 2022.

**Cited in:** 01_introduction.md (sparse upcycling); 03_detecting-retrieval-head-continued.md (Mixtral sparse upcycling)

## [17] In search of needles in a 10m haystack
Yuri Kuratov, Aydar Bulatov, Petr Anokhin, Dmitry Sorokin, Artyom Sorokin, and Mikhail Burtsev. In search of needles in a 10m haystack: Recurrent memory finds what llms miss. arXiv preprint arXiv:2402.10790, 2024.

**Cited in:** 01_introduction.md (multi-step retrieval and reasoning tasks)

## [18] Mistral 7B Instruct v0.2
Mistral. Model card for mistral-7b-instruct-v0.2, April 2024. URL https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2.

**Cited in:** 05_intrinsic-and-influence.md (primary model for downstream task experiments); 06_discussions.md (full attention in v0.2 enables needle test passing)

## [19] In-context learning and induction heads
Catherine Olsson, Nelson Elhage, Neel Nanda, Nicholas Joseph, Nova DasSarma, Tom Henighan, Ben Mann, Amanda Askell, Yuntao Bai, Anna Chen, et al. In-context learning and induction heads. arXiv preprint arXiv:2209.11895, 2022.

**Cited in:** 01_introduction.md (induction heads concept); 06_discussions.md (induction heads search repeated patterns)

## [20] Gemini 1.5
Machel Reid, Nikolay Savinov, Denis Teplyashin, Dmitry Lepikhin, Timothy Lillicrap, Jean-baptiste Alayrac, Radu Soricut, Angeliki Lazaridou, Orhan Firat, Julian Schrittwieser, et al. Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context. arXiv preprint arXiv:2403.05530, 2024.

**Cited in:** 01_introduction.md (recent advances in long-context language modeling)

## [21] Llama 2
Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, et al. Llama 2: Open foundation and fine-tuned chat models. arXiv preprint arXiv:2307.09288, 2023.

**Cited in:** 01_introduction.md (model family studied)

## [22] Linformer
Sinong Wang, Belinda Z Li, Madian Khabsa, Han Fang, and Hao Ma. Linformer: Self-attention with linear complexity. arXiv preprint arXiv:2006.04768, 2020.

**Cited in:** 06_discussions.md (linear attention)

## [23] Chain-of-thought prompting
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed H. Chi, Quoc V. Le, and Denny Zhou. Chain-of-thought prompting elicits reasoning in large language models. In Sammi Koyejo, S. Mohamed, A. Agarwal, Danielle Belgrave, K. Cho, and A. Oh, editors, Advances in Neural Information Processing Systems 2022, NeurIPS 2022, New Orleans, LA, USA, November 28 - December 9, 2022, 2022. URL https://openreview.net/forum?id=_VjQlMeSB_J.

**Cited in:** 05_intrinsic-and-influence.md (chain-of-thought reasoning); 07_conclusions.md (chain-of-thought reasoning)

## [24] Attention sinks and efficient streaming
Guangxuan Xiao, Yuandong Tian, Beidi Chen, Song Han, and Mike Lewis. Efficient streaming language models with attention sinks. arXiv preprint arXiv:2309.17453, 2023.

**Cited in:** 01_introduction.md (context-compression methods); 05_intrinsic-and-influence.md (attention sink phenomenon); 06_discussions.md (local attention)

## [25] Yi foundation models
Alex Young, Bei Chen, Chao Li, Chengen Huang, Ge Zhang, Guanwei Zhang, Heng Li, Jiangcheng Zhu, Jianqun Chen, Jing Chang, et al. Yi: Open foundation models by 01. ai. arXiv preprint arXiv:2403.04652, 2024.

**Cited in:** 01_introduction.md (Yi model family)
