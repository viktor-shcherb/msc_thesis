# References

References cited in the section notes, looked up from the paper's bibliography (p. 21-26).

---

### AI@Meta, 2024
AI@Meta. Llama 3 model card, 2024. URL https://github.com/meta-llama/llama3/blob/main/MODEL_CARD.md.
- Cited in 03_pre-training.md as LLaMA3 70B, a baseline for evaluation comparison.

### Ainslie et al., 2023
J. Ainslie, J. Lee-Thorp, M. de Jong, Y. Zemlyanskiy, F. Lebron, and S. Sanghai. Gqa: Training generalized multi-query transformer models from multi-head checkpoints. arXiv preprint arXiv:2305.13245, 2023.
- Cited in 01_introduction.md and 02_architecture.md as Grouped-Query Attention (GQA), an existing approach to reduce KV cache that compromises performance.

### Anthropic, 2023
Anthropic. Introducing Claude, 2023. URL https://www.anthropic.com/index/introducing-claude.
- Cited in 01_introduction.md as an example of rapid LLM development.

### Austin et al., 2021
J. Austin, A. Odena, M. Nye, M. Bosma, H. Michalewski, D. Dohan, E. Jiang, C. Cai, M. Terry, Q. Le, et al. Program synthesis with large language models. arXiv preprint arXiv:2108.07732, 2021.
- Cited in 03_pre-training.md as the source of the MBPP code benchmark.

### Bai et al., 2023
J. Bai, S. Bai, Y. Chu, Z. Cui, K. Dang, X. Deng, Y. Fan, W. Ge, Y. Han, F. Huang, B. Hui, L. Ji, M. Li, J. Lin, R. Lin, D. Liu, G. Liu, C. Lu, K. Lu, J. Ma, R. Men, X. Ren, X. Ren, C. Tan, S. Tan, J. Tu, P. Wang, S. Wang, W. Wang, S. Wu, B. Xu, J. Xu, A. Yang, H. Yang, J. Yang, S. Yang, Y. Yao, B. Yu, H. Yuan, Z. Yuan, J. Zhang, X. Zhang, Y. Zhang, Z. Zhang, C. Zhou, J. Zhou, X. Zhou, and T. Zhu. Qwen technical report. arXiv preprint arXiv:2309.16609, 2023.
- Cited in 03_pre-training.md as Qwen1.5 72B, a baseline for evaluation comparison.

### Bisk et al., 2020
Y. Bisk, R. Zellers, R. L. Bras, J. Gao, and Y. Choi. PIQA: reasoning about physical commonsense in natural language. In The Thirty-Fourth AAAI Conference on Artificial Intelligence, AAAI 2020, pages 7432-7439. AAAI Press, 2020.
- Cited in 03_pre-training.md as the PIQA benchmark for language understanding and reasoning evaluation.

### Chen et al., 2021
M. Chen, J. Tworek, H. Jun, Q. Yuan, H. P. de Oliveira Pinto, J. Kaplan, H. Edwards, Y. Burda, N. Joseph, G. Brockman, A. Ray, R. Puri, G. Krueger, M. Petrov, H. Khlaaf, G. Sastry, P. Mishkin, B. Chan, S. Gray, N. Ryder, M. Pavlov, A. Power, L. Kaiser, M. Bavarian, C. Winter, P. Tillet, F. P. Such, D. Cummings, M. Plappert, F. Chantzis, E. Barnes, A. Herbert-Voss, W. H. Guss, A. Nichol, A. Paino, N. Tezak, J. Tang, I. Babuschkin, S. Balaji, S. Jain, W. Saunders, C. Hesse, A. N. Carr, J. Leike, J. Achiam, V. Misra, E. Morikawa, A. Radford, M. Knight, M. Brundage, M. Murati, K. Mayer, P. Welinder, B. McGrew, D. Amodei, S. McCandlish, I. Sutskever, and W. Zaremba. Evaluating large language models trained on code. CoRR, abs/2107.03374, 2021.
- Cited in 03_pre-training.md as the source of the HumanEval code benchmark.

### Clark et al., 2018
P. Clark, I. Cowhey, O. Etzioni, T. Khot, A. Sabharwal, C. Schoenick, and O. Tafjord. Think you have solved question answering? try arc, the AI2 reasoning challenge. CoRR, abs/1803.05457, 2018.
- Cited in 03_pre-training.md as the ARC benchmark for language understanding and reasoning evaluation.

### Cobbe et al., 2021
K. Cobbe, V. Kosaraju, M. Bavarian, M. Chen, H. Jun, L. Kaiser, M. Plappert, J. Tworek, J. Hilton, R. Nakano, et al. Training verifiers to solve math word problems. arXiv preprint arXiv:2110.14168, 2021.
- Cited in 03_pre-training.md as the source of the GSM8K math benchmark.

### Cui et al., 2019
Y. Cui, T. Liu, W. Che, L. Xiao, Z. Chen, W. Ma, S. Wang, and G. Hu. A span-extraction dataset for Chinese machine reading comprehension. In Proceedings of EMNLP-IJCNLP 2019, pages 5883-5889, 2019.
- Cited in 03_pre-training.md as the CMRC reading comprehension benchmark.

### Dai et al., 2024
D. Dai, C. Deng, C. Zhao, R. X. Xu, H. Gao, D. Chen, J. Li, W. Zeng, X. Yu, Y. Wu, Z. Xie, Y. K. Li, P. Huang, F. Luo, C. Ruan, Z. Sui, and W. Liang. Deepseekmoe: Towards ultimate expert specialization in mixture-of-experts language models. CoRR, abs/2401.06066, 2024.
- Cited in 01_introduction.md, 02_architecture.md, 02b_deepseek-moe.md, and 03_pre-training.md as the DeepSeekMoE architecture that DeepSeek-V2 adopts for FFNs.

### Dao, 2023
T. Dao. FlashAttention-2: Faster attention with better parallelism and work partitioning, 2023.
- Cited in 03_pre-training.md as the basis for optimized MLA implementation.

### DeepSeek-AI, 2024
DeepSeek-AI. Deepseek LLM: scaling open-source language models with longtermism. CoRR, abs/2401.02954, 2024.
- Cited in 01_introduction.md, 02_architecture.md, 03_pre-training.md, and 04_alignment.md as the prior DeepSeek 67B model release that DeepSeek-V2 builds upon and compares against.

### Dua et al., 2019
D. Dua, Y. Wang, P. Dasigi, G. Stanovsky, S. Singh, and M. Gardner. DROP: A reading comprehension benchmark requiring discrete reasoning over paragraphs. In Proceedings of NAACL-HLT 2019, pages 2368-2378, 2019.
- Cited in 03_pre-training.md as the DROP reading comprehension benchmark.

### Dubois et al., 2024
Y. Dubois, B. Galambosi, P. Liang, and T. B. Hashimoto. Length-controlled alpacaeval: A simple way to debias automatic evaluators. arXiv preprint arXiv:2404.04475, 2024.
- Cited in 01_introduction.md and 04_alignment.md as the AlpacaEval 2.0 open-ended conversation benchmark.

### Fedus et al., 2021
W. Fedus, B. Zoph, and N. Shazeer. Switch transformers: Scaling to trillion parameter models with simple and efficient sparsity. CoRR, abs/2101.03961, 2021.
- Cited in 02b_deepseek-moe.md as a source for the expert-level balance loss.

### Gao et al., 2020
L. Gao, S. Biderman, S. Black, L. Golding, T. Hoppe, C. Foster, J. Phang, H. He, A. Thite, N. Nabeshima, et al. The Pile: An 800GB dataset of diverse text for language modeling. arXiv preprint arXiv:2101.00027, 2020.
- Cited in 03_pre-training.md as the Pile language modeling benchmark.

### Google, 2023
Google. Introducing gemini: our largest and most capable ai model, 2023. URL https://blog.google/technology/ai/google-gemini-ai/.
- Cited in 01_introduction.md as an example of rapid LLM development.

### Gu et al., 2024
A. Gu, B. Roziere, H. Leather, A. Solar-Lezama, G. Synnaeve, and S. I. Wang. Cruxeval: A benchmark for code reasoning, understanding and execution, 2024.
- Cited in 03_pre-training.md as the CRUXEval code benchmark.

### Hendrycks et al., 2020
D. Hendrycks, C. Burns, S. Basart, A. Zou, M. Mazeika, D. Song, and J. Steinhardt. Measuring massive multitask language understanding. arXiv preprint arXiv:2009.03300, 2020.
- Cited in 03_pre-training.md as the source of the MMLU benchmark.

### Hendrycks et al., 2021
D. Hendrycks, C. Burns, S. Kadavath, A. Arora, S. Basart, E. Tang, D. Song, and J. Steinhardt. Measuring mathematical problem solving with the math dataset. arXiv preprint arXiv:2103.03874, 2021.
- Cited in 03_pre-training.md as the source of the MATH benchmark.

### High-flyer, 2023
High-flyer. Hai-llm: An efficient and light-weight training framework for large models, 2023. URL https://www.high-flyer.cn/en/blog/hai-llm.
- Cited in 03_pre-training.md as the HAI-LLM training framework used for pre-training DeepSeek-V2.

### Hooper et al., 2024
C. Hooper, S. Kim, H. Mohammadzadeh, M. W. Mahoney, Y. S. Shao, K. Keutzer, and A. Gholami. Kvquant: Towards 10 million context length LLM inference with KV cache quantization. CoRR, abs/2401.18079, 2024.
- Cited in 03_pre-training.md for KV cache quantization used in DeepSeek-V2 inference deployment.

### Hu et al., 2024
S. Hu, Y. Tu, X. Han, C. He, G. Cui, X. Long, Z. Zheng, Y. Fang, Y. Huang, W. Zhao, et al. Minicpm: Unveiling the potential of small language models with scalable training strategies. arXiv preprint arXiv:2404.06395, 2024.
- Cited in 03_pre-training.md as a prior study that incorporates SFT data during pre-training, contrasted with DeepSeek-V2's approach.

### Huang et al., 2023
Y. Huang, Y. Bai, Z. Zhu, J. Zhang, J. Zhang, T. Su, J. Liu, C. Lv, Y. Zhang, J. Lei, et al. C-Eval: A multi-level multi-discipline chinese evaluation suite for foundation models. arXiv preprint arXiv:2305.08322, 2023.
- Cited in 03_pre-training.md as the C-Eval multi-subject multiple-choice benchmark.

### Jain et al., 2024
N. Jain, K. Han, A. Gu, W.-D. Li, F. Yan, T. Zhang, S. Wang, A. Solar-Lezama, K. Sen, and I. Stoica. Livecodebench: Holistic and contamination free evaluation of large language models for code. arXiv preprint arXiv:2403.07974, 2024.
- Cited in 04_alignment.md as the LiveCodeBench benchmark for evaluating chat models on code.

### Joshi et al., 2017
M. Joshi, E. Choi, D. Weld, and L. Zettlemoyer. TriviaQA: A large scale distantly supervised challenge dataset for reading comprehension. In Proceedings of ACL 2017, pages 1601-1611, 2017.
- Cited in 03_pre-training.md as the TriviaQA closed-book question answering benchmark.

### Kwiatkowski et al., 2019
T. Kwiatkowski, J. Palomaki, O. Redfield, M. Collins, A. P. Parikh, C. Alberti, D. Epstein, I. Polosukhin, J. Devlin, K. Lee, K. Toutanova, L. Jones, M. Kelcey, M. Chang, A. M. Dai, J. Uszkoreit, Q. Le, and S. Petrov. Natural questions: a benchmark for question answering research. Trans. Assoc. Comput. Linguistics, 7:452-466, 2019.
- Cited in 03_pre-training.md as the NaturalQuestions closed-book question answering benchmark.

### Kwon et al., 2023
W. Kwon, Z. Li, S. Zhuang, Y. Sheng, L. Zheng, C. H. Yu, J. E. Gonzalez, H. Zhang, and I. Stoica. Efficient memory management for large language model serving with pagedattention. In Proceedings of the ACM SIGOPS 29th Symposium on Operating Systems Principles, 2023.
- Cited in 04_alignment.md as vLLM, used as the inference backend for RL training efficiency.

### Lai et al., 2017
G. Lai, Q. Xie, H. Liu, Y. Yang, and E. H. Hovy. RACE: large-scale reading comprehension dataset from examinations. In Proceedings of EMNLP 2017, pages 785-794, 2017.
- Cited in 03_pre-training.md as the RACE reading comprehension benchmark.

### Lepikhin et al., 2021
D. Lepikhin, H. Lee, Y. Xu, D. Chen, O. Firat, Y. Huang, M. Krikun, N. Shazeer, and Z. Chen. Gshard: Scaling giant models with conditional computation and automatic sharding. In 9th International Conference on Learning Representations, ICLR 2021.
- Cited in 01_introduction.md, 02b_deepseek-moe.md, and 03_pre-training.md as the GShard conventional MoE architecture that DeepSeekMoE outperforms, and as a source for expert-level balance loss and expert parallelism.

### Li et al., 2021
W. Li, F. Qi, M. Sun, X. Yi, and J. Zhang. Ccpm: A chinese classical poetry matching dataset, 2021.
- Cited in 03_pre-training.md as the CCPM Chinese understanding and culture benchmark.

### Li et al., 2023
H. Li, Y. Zhang, F. Koto, Y. Yang, H. Zhao, Y. Gong, N. Duan, and T. Baldwin. CMMLU: Measuring massive multitask language understanding in Chinese. arXiv preprint arXiv:2306.09212, 2023.
- Cited in 03_pre-training.md as the CMMLU multi-subject multiple-choice benchmark.

### Liu et al., 2023
X. Liu, X. Lei, S. Wang, Y. Huang, Z. Feng, B. Wen, J. Cheng, P. Ke, Y. Xu, W. L. Tam, X. Zhang, L. Sun, H. Wang, J. Zhang, M. Huang, Y. Dong, and J. Tang. Alignbench: Benchmarking chinese alignment of large language models. CoRR, abs/2311.18743, 2023.
- Cited in 01_introduction.md and 04_alignment.md as the AlignBench benchmark for Chinese open-ended generation evaluation.

### Loshchilov and Hutter, 2017
I. Loshchilov and F. Hutter. Decoupled weight decay regularization. arXiv preprint arXiv:1711.05101, 2017.
- Cited in 03_pre-training.md as the AdamW optimizer used for training.

### Mistral, 2024
Mistral. Cheaper, better, faster, stronger: Continuing to push the frontier of ai and making it accessible to all, 2024. URL https://mistral.ai/news/mixtral-8x22b.
- Cited in 03_pre-training.md as Mixtral 8x22B, a baseline for evaluation comparison.

### OpenAI, 2022
OpenAI. Introducing ChatGPT, 2022. URL https://openai.com/blog/chatgpt.
- Cited in 01_introduction.md as an example of rapid LLM development.

### OpenAI, 2023
OpenAI. GPT4 technical report. arXiv preprint arXiv:2303.08774, 2023.
- Cited in 01_introduction.md as an example of rapid LLM development.

### Ouyang et al., 2022
L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. Wainwright, P. Mishkin, C. Zhang, S. Agarwal, K. Slama, A. Ray, et al. Training language models to follow instructions with human feedback. Advances in neural information processing systems, 35:27730-27744, 2022.
- Cited in 04_alignment.md as the source for the "alignment tax" phenomenon observed during RL training.

### Peng et al., 2023
B. Peng, J. Quesnelle, H. Fan, and E. Shippole. Yarn: Efficient context window extension of large language models. arXiv preprint arXiv:2309.00071, 2023.
- Cited in 03_pre-training.md as the YaRN method used for extending context from 4K to 128K.

### Qi et al., 2023
P. Qi, X. Wan, G. Huang, and M. Lin. Zero bubble pipeline parallelism. arXiv preprint arXiv:2401.10241, 2023.
- Cited in 03_pre-training.md as the zero-bubble pipeline parallelism technique used in the training infrastructure.

### Rajbhandari et al., 2020
S. Rajbhandari, J. Rasley, O. Ruwase, and Y. He. Zero: Memory optimizations toward training trillion parameter models. In SC20: International Conference for High Performance Computing, Networking, Storage and Analysis, pages 1-16. IEEE, 2020.
- Cited in 03_pre-training.md as ZeRO-1 data parallelism used in the training infrastructure.

### Riquelme et al., 2021
C. Riquelme, J. Puigcerver, B. Mustafa, M. Neumann, R. Jenatton, A. S. Pinto, D. Keysers, and N. Houlsby. Scaling vision with sparse mixture of experts. In Advances in Neural Information Processing Systems 34: NeurIPS 2021, pages 8583-8595, 2021.
- Cited in 02b_deepseek-moe.md as inspiration for the token-dropping strategy where tokens with the lowest affinity scores are dropped.

### Sakaguchi et al., 2019
K. Sakaguchi, R. L. Bras, C. Bhagavatula, and Y. Choi. Winogrande: An adversarial winograd schema challenge at scale, 2019.
- Cited in 03_pre-training.md as the WinoGrande reference disambiguation benchmark.

### Shao et al., 2024
Z. Shao, P. Wang, Q. Zhu, R. Xu, J. Song, M. Zhang, Y. Li, Y. Wu, and D. Guo. Deepseekmath: Pushing the limits of mathematical reasoning in open language models. arXiv preprint arXiv:2402.03300, 2024.
- Cited in 01_introduction.md and 04_alignment.md as the source of Group Relative Policy Optimization (GRPO) used for RL alignment.

### Shazeer, 2019
N. Shazeer. Fast transformer decoding: One write-head is all you need. CoRR, abs/1911.02150, 2019.
- Cited in 01_introduction.md and 02_architecture.md as Multi-Query Attention (MQA), an existing approach to reduce KV cache.

### Shazeer et al., 2017
N. Shazeer, A. Mirhoseini, K. Maziarz, A. Davis, Q. V. Le, G. E. Hinton, and J. Dean. Outrageously large neural networks: The sparsely-gated mixture-of-experts layer. In 5th International Conference on Learning Representations, ICLR 2017.
- Cited in 02b_deepseek-moe.md for the risk of routing collapse in unbalanced expert loads.

### Su et al., 2024
J. Su, M. Ahmed, Y. Lu, S. Pan, W. Bo, and Y. Liu. Roformer: Enhanced transformer with rotary position embedding. Neurocomputing, 568:127063, 2024.
- Cited in 02_architecture.md and 03_pre-training.md as Rotary Position Embedding (RoPE) used in DeepSeek-V2.

### Sun et al., 2019
K. Sun, D. Yu, D. Yu, and C. Cardie. Investigating prior knowledge for challenging chinese machine reading comprehension, 2019.
- Cited in 03_pre-training.md as the C3 reading comprehension benchmark.

### Suzgun et al., 2022
M. Suzgun, N. Scales, N. Scharli, S. Gehrmann, Y. Tay, H. W. Chung, A. Chowdhery, Q. V. Le, E. H. Chi, D. Zhou, et al. Challenging big-bench tasks and whether chain-of-thought can solve them. arXiv preprint arXiv:2210.09261, 2022.
- Cited in 03_pre-training.md as the BigBench Hard (BBH) benchmark.

### Vaswani et al., 2017
A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, L. Kaiser, and I. Polosukhin. Attention is all you need. Advances in neural information processing systems, 30, 2017.
- Cited in 01_introduction.md and 02_architecture.md as the original Transformer architecture that DeepSeek-V2 builds upon.

### Wei et al., 2022
J. Wei, Y. Tay, R. Bommasani, C. Raffel, B. Zoph, S. Borgeaud, D. Yogatama, M. Bosma, D. Zhou, D. Metzler, et al. Emergent abilities of large language models. arXiv preprint arXiv:2206.07682, 2022.
- Cited in 01_introduction.md for the observation that LLMs exhibit emergent capabilities as parameters increase.

### Wei et al., 2023
T. Wei, J. Luan, W. Liu, S. Dong, and B. Wang. Cmath: Can your language model pass chinese elementary school math test?, 2023.
- Cited in 03_pre-training.md as the CMath Chinese math benchmark.

### Xu et al., 2020
L. Xu, H. Hu, X. Zhang, L. Li, C. Cao, Y. Li, Y. Xu, K. Sun, D. Yu, C. Yu, Y. Tian, Q. Dong, W. Liu, B. Shi, Y. Cui, J. Li, J. Zeng, R. Wang, W. Xie, Y. Li, Y. Patterson, Z. Tian, Y. Zhang, H. Zhou, S. Liu, Z. Zhao, Q. Zhao, C. Yue, X. Zhang, Z. Yang, K. Richardson, and Z. Lan. CLUE: A chinese language understanding evaluation benchmark. In Proceedings of the 28th International Conference on Computational Linguistics, COLING 2020, pages 4762-4772, 2020.
- Cited in 03_pre-training.md as the CLUEWSC reference disambiguation benchmark.

### Young et al., 2024
A. Young, B. Chen, C. Li, C. Huang, G. Zhang, G. Zhang, H. Li, J. Zhu, J. Chen, J. Chang, et al. Yi: Open foundation models by 01. ai. arXiv preprint arXiv:2403.04652, 2024.
- Cited in 04_alignment.md in the discussion about the necessity of a large SFT corpus, arguing fewer than 10K instances are sufficient.

### Zellers et al., 2019
R. Zellers, A. Holtzman, Y. Bisk, A. Farhadi, and Y. Choi. HellaSwag: Can a machine really finish your sentence? In Proceedings of the 57th Conference of the Association for Computational Linguistics, ACL 2019, pages 4791-4800, 2019.
- Cited in 03_pre-training.md as the HellaSwag language understanding and reasoning benchmark.

### Zhao et al., 2023
Y. Zhao, C. Lin, K. Zhu, Z. Ye, L. Chen, S. Zheng, L. Ceze, A. Krishnamurthy, T. Chen, and B. Kasikci. Atom: Low-bit quantization for efficient and accurate LLM serving. CoRR, abs/2310.19102, 2023.
- Cited in 03_pre-training.md for KV cache quantization used in DeepSeek-V2 inference deployment.

### Zheng et al., 2019
C. Zheng, M. Huang, and A. Sun. Chid: A large-scale chinese idiom dataset for cloze test. In Proceedings of the 57th Conference of the Association for Computational Linguistics, ACL 2019, pages 778-787, 2019.
- Cited in 03_pre-training.md as the CHID Chinese understanding and culture benchmark.

### Zheng et al., 2023
L. Zheng, W.-L. Chiang, Y. Sheng, S. Zhuang, Z. Wu, Y. Zhuang, Z. Lin, Z. Li, D. Li, E. P. Xing, H. Zhang, J. E. Gonzalez, and I. Stoica. Judging llm-as-a-judge with mt-bench and chatbot arena, 2023.
- Cited in 01_introduction.md and 04_alignment.md as the MT-Bench open-ended conversation benchmark.

### Zhong et al., 2023
W. Zhong, R. Cui, Y. Guo, Y. Liang, S. Lu, Y. Wang, A. Saied, W. Chen, and N. Duan. AGIEval: A human-centric benchmark for evaluating foundation models. CoRR, abs/2304.06364, 2023.
- Cited in 03_pre-training.md as the AGIEval standardized exams benchmark.

### Zhou et al., 2023
J. Zhou, T. Lu, S. Mishra, S. Brahma, S. Basu, Y. Luan, D. Zhou, and L. Hou. Instruction-following evaluation for large language models. arXiv preprint arXiv:2311.07911, 2023.
- Cited in 04_alignment.md as the IFEval instruction-following evaluation benchmark.

### Zhou et al., 2024
C. Zhou, P. Liu, P. Xu, S. Iyer, J. Sun, Y. Mao, X. Ma, A. Efrat, P. Yu, L. Yu, et al. Lima: Less is more for alignment. Advances in Neural Information Processing Systems, 36, 2024.
- Cited in 04_alignment.md in the discussion arguing fewer than 10K SFT instances are sufficient.
