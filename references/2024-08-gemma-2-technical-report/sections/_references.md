# References

This file lists only the references that are cited in the section notes.

## Achiam et al., 2023
J. Achiam, S. Adler, S. Agarwal, L. Ahmad, I. Akkaya, F. L. Aleman, D. Almeida, J. Altenschmidt, S. Altman, S. Anadkat, et al. Gpt-4 technical report. *arXiv preprint arXiv:2303.08774*, 2023.
- Cited in 01_introduction.md as an example of newest large models reaching unprecedented performance on reasoning benchmarks.

## Agarwal et al., 2024
R. Agarwal, N. Vieillard, Y. Zhou, P. Stanczyk, S. R. Garea, M. Geist, and O. Bachem. On-policy distillation of language models: Learning from self-generated mistakes. In *The Twelfth International Conference on Learning Representations*, 2024.
- Cited in 04_post-training.md for distillation from the teacher on the student's distribution during SFT.

## AI@Meta, 2024
AI@Meta. Llama 3 model card, 2024. URL https://github.com/meta-llama/llama3/blob/main/MODEL_CARD.md.
- Cited in 01_introduction.md noting latest small models require up to 15T tokens; cited in 06_evaluation.md as a comparable open model.

## Ainslie et al., 2023
J. Ainslie, J. Lee-Thorp, M. de Jong, Y. Zemlyanskiy, F. Lebron, and S. Sanghai. Gqa: Training generalized multi-query transformer models from multi-head checkpoints. *arXiv preprint arXiv:2305.13245*, 2023.
- Cited in 00_overview.md (abstract), 01_introduction.md, and 02_model-architecture.md for Grouped-Query Attention (GQA).

## Almazrouei et al., 2023
E. Almazrouei, H. Alobeidli, A. Alshamsi, A. Cappelli, R. Cojocaru, M. Debbah, Etienne Goffinet, D. Hesslow, J. Launay, Q. Malartic, D. Mazzotta, B. Noune, B. Pannier, and G. Penedo. The falcon series of open language models, 2023.
- Cited in 01_introduction.md as a comparable open model.

## Anil et al., 2023
R. Anil, A. M. Dai, O. Firat, M. Johnson, D. Lepikhin, A. Passos, S. Shakeri, E. Taropa, P. Bailey, Z. Chen, et al. Palm 2 technical report. *arXiv preprint arXiv:2305.10403*, 2023.
- Cited in 07_memorization-and-privacy.md as a prior study on memorization.

## Austin et al., 2021
J. Austin, A. Odena, M. I. Nye, M. Bosma, H. Michalewski, D. Dohan, E. Jiang, C. J. Cai, M. Terry, Q. V. Le, and C. Sutton. Program synthesis with large language models. *CoRR*, abs/2108.07732, 2021.
- Cited in 01_introduction.md as a coding evaluation domain.

## Barham et al., 2022
P. Barham, A. Chowdhery, J. Dean, S. Ghemawat, S. Hand, D. Hurt, M. Isard, H. Lim, R. Pang, S. Roy, B. Saeta, P. Schuh, R. Sepassi, L. E. Shafey, C. A. Thekkath, and Y. Wu. Pathways: Asynchronous distributed dataflow for ml, 2022.
- Cited in 03_pre-training.md for the Pathways approach used for data-replica reduction and single controller programming paradigm.

## Beltagy et al., 2020a
I. Beltagy, M. E. Peters, and A. Cohan. Longformer: The long-document transformer. *arXiv preprint arXiv:2004.05150*, 2020a.
- Cited in 00_overview.md (abstract), 01_introduction.md, and 02_model-architecture.md for interleaving local-global attentions / local sliding window attention.

## Beltagy et al., 2020b
I. Beltagy, M. E. Peters, and A. Cohan. Longformer: The long-document transformer. *CoRR*, abs/2004.05150, 2020b.
- Cited in 02_model-architecture.md alongside 2020a for sliding window attention.

## Bello et al., 2016
I. Bello, H. Pham, Q. V. Le, M. Norouzi, and S. Bengio. Neural combinatorial optimization with reinforcement learning. *CoRR*, abs/1611.09940, 2016.
- Cited in 02_model-architecture.md for logit soft-capping.

## Brown et al., 2020
T. B. Brown, B. Mann, N. Ryder, M. Subbiah, J. Kaplan, P. Dhariwal, A. Neelakantan, P. Shyam, G. Sastry, A. Askell, S. Agarwal, A. Herbert-Voss, G. Krueger, T. Henighan, R. Child, A. Ramesh, D. M. Ziegler, J. Wu, C. Winter, C. Hesse, M. Chen, E. Sigler, M. Litwin, S. Gray, B. Chess, J. Clark, C. Berner, S. McCandlish, A. Radford, I. Sutskever, and D. Amodei. Language models are few-shot learners. *CoRR*, abs/2005.14165, 2020.
- Cited in 01_introduction.md for LLM capabilities and emergent capabilities at scale.

## Carlini et al., 2022
N. Carlini, D. Ippolito, M. Jagielski, K. Lee, F. Tramer, and C. Zhang. Quantifying memorization across neural language models. *arXiv preprint arXiv:2202.07646*, 2022.
- Cited in 07_memorization-and-privacy.md as a prior study on memorization.

## Chen et al., 2021
M. Chen, J. Tworek, H. Jun, Q. Yuan, H. P. de Oliveira Pinto, J. Kaplan, H. Edwards, Y. Burda, N. Joseph, G. Brockman, A. Ray, R. Puri, G. Krueger, M. Petrov, H. Khlaaf, G. Sastry, P. Mishkin, B. Chan, S. Gray, N. Ryder, M. Pavlov, A. Power, L. Kaiser, M. Bavarian, C. Winter, P. Tillet, F. P. Such, D. Cummings, M. Plappert, F. Chantzis, E. Barnes, A. Herbert-Voss, W. H. Guss, A. Nichol, A. Paino, N. Tezak, J. Tang, I. Babuschkin, S. Balaji, S. Jain, W. Saunders, C. Hesse, A. N. Carr, J. Leike, J. Achiam, V. Misra, E. Morikawa, A. Radford, M. Knight, M. Brundage, M. Murati, K. Mayer, P. Welinder, B. McGrew, D. Amodei, S. McCandlish, I. Sutskever, and W. Zaremba. Evaluating large language models trained on code. *CoRR*, abs/2107.03374, 2021.
- Cited in 01_introduction.md as a coding evaluation domain.

## Chiang et al., 2024
W.-L. Chiang, L. Zheng, Y. Sheng, A. N. Angelopoulos, T. Li, D. Li, H. Zhang, B. Zhu, M. Jordan, J. E. Gonzalez, and I. Stoica. Chatbot arena: An open platform for evaluating llms by human preference, 2024.
- Cited in 06_evaluation.md for the LMSYS Chatbot Arena evaluation.

## Clark et al., 2019
C. Clark, K. Lee, M. Chang, T. Kwiatkowski, M. Collins, and K. Toutanova. Boolq: Exploring the surprising difficulty of natural yes/no questions. *CoRR*, abs/1905.10044, 2019.
- Cited in 01_introduction.md as a question answering evaluation domain.

## Cobbe et al., 2021
K. Cobbe, V. Kosaraju, M. Bavarian, M. Chen, H. Jun, L. Kaiser, M. Plappert, J. Tworek, J. Hilton, R. Nakano, C. Hesse, and J. Schulman. Training verifiers to solve math word problems. *CoRR*, abs/2110.14168, 2021.
- Cited in 01_introduction.md as a mathematics and science evaluation domain.

## Gemini Team, 2023
Gemini Team. Gemini: A family of highly capable multimodal models, 2023.
- Cited in 03_pre-training.md for data mixture determination approach; cited in 08_responsibility-safety-security.md for safety policies alignment.

## Gemini Team, 2024
Gemini Team. Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context, 2024.
- Cited in 01_introduction.md for multimodal/multilingual capabilities and 1M+ context; cited in 03_pre-training.md for knowledge distillation; cited in 07_memorization-and-privacy.md for memorization evaluation; cited in 08_responsibility-safety-security.md for safety processes.

## Gemma Team, 2024
Gemma Team. Gemma: Open models based on gemini research and technology, 2024.
- Cited extensively across 01_introduction.md, 02_model-architecture.md, 03_pre-training.md, 04_post-training.md, 06_evaluation.md, 07_memorization-and-privacy.md, and 08_responsibility-safety-security.md as the predecessor Gemma 1 model.

## Gu et al., 2024
Y. Gu, L. Dong, F. Wei, and M. Huang. Minillm: Knowledge distillation of large language models. In *The Twelfth International Conference on Learning Representations*, 2024.
- Cited in 04_post-training.md for distillation from teacher on student's distribution during SFT.

## Hendrycks et al., 2020
D. Hendrycks, C. Burns, S. Basart, A. Zou, M. Mazeika, D. Song, and J. Steinhardt. Measuring massive multitask language understanding. *CoRR*, abs/2009.03300, 2020.
- Cited in 01_introduction.md as a mathematics and science evaluation domain (MMLU).

## Hinton et al., 2015
G. Hinton, O. Vinyals, and J. Dean. Distilling the knowledge in a neural network. *arXiv preprint arXiv:1503.02531*, 2015.
- Cited in 00_overview.md (abstract) and 01_introduction.md for the knowledge distillation method.

## Hoffmann et al., 2022
J. Hoffmann, S. Borgeaud, A. Mensch, E. Buchatskaya, T. Cai, E. Rutherford, D. d. L. Casas, L. A. Hendricks, J. Welbl, A. Clark, et al. Training compute-optimal large language models. *arXiv preprint arXiv:2203.15556*, 2022.
- Cited in 01_introduction.md for logarithmic scaling with dataset size and compute-optimal training quantities.

## Ippolito et al., 2022
D. Ippolito, F. Tramer, M. Nasr, C. Zhang, M. Jagielski, K. Lee, C. A. Choquette-Choo, and N. Carlini. Preventing verbatim memorization in language models gives a false sense of privacy. *arXiv preprint arXiv:2210.17546*, 2022.
- Cited in 07_memorization-and-privacy.md for approximate match criteria using edit distance.

## Jiang et al., 2023
A. Q. Jiang, A. Sablayrolles, A. Mensch, C. Bamford, D. S. Chaplot, D. de las Casas, F. Bressand, G. Lengyel, G. Lample, L. Saulnier, L. R. Lavaud, M.-A. Lachaux, P. Stock, T. L. Scao, T. Lavril, T. Wang, T. Lacroix, and W. E. Sayed. Mistral 7b, 2023.
- Cited in 01_introduction.md for small-scale model performance increases and as a comparable model.

## Kahng et al., 2024
M. Kahng, I. Tenney, M. Pushkarna, M. X. Liu, J. Wexler, E. Reif, K. Kallarackal, M. Chang, M. Terry, and L. Dixon. Llm comparator: Visual analytics for side-by-side evaluation of large language models, 2024.
- Cited in 08_responsibility-safety-security.md as a tool in the Responsible Generative AI Toolkit.

## Kinniment et al., 2024
M. Kinniment, L. J. K. Sato, H. Du, B. Goodrich, M. Hasin, L. Chan, L. H. Miles, T. R. Lin, H. Wijk, J. Burget, A. Ho, E. Barnes, and P. Christiano. Evaluating language-model agents on realistic autonomous tasks, 2024.
- Cited in 08_responsibility-safety-security.md for the definition of self-proliferation.

## Kudugunta et al., 2023
S. Kudugunta, I. Caswell, B. Zhang, X. Garcia, C. A. Choquette-Choo, K. Lee, D. Xin, A. Kusupati, R. Stella, A. Bapna, et al. Madlad-400: A multilingual and document-level large audited dataset. *arXiv preprint arXiv:2309.04662*, 2023.
- Cited in 07_memorization-and-privacy.md as a prior study on memorization.

## Kudo and Richardson, 2018
T. Kudo and J. Richardson. SentencePiece: A simple and language independent subword tokenizer and detokenizer for neural text processing. In *Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing: System Demonstrations*, pages 66-71, Brussels, Belgium, Nov. 2018. Association for Computational Linguistics.
- Cited in 03_pre-training.md for the tokenizer used.

## Kwiatkowski et al., 2019
T. Kwiatkowski, J. Palomaki, O. Redfield, M. Collins, A. Parikh, C. Alberti, D. Epstein, I. Polosukhin, J. Devlin, K. Lee, K. Toutanova, L. Jones, M. Kelcey, M.-W. Chang, A. M. Dai, J. Uszkoreit, Q. Le, and S. Petrov. Natural questions: A benchmark for question answering research. *Transactions of the Association for Computational Linguistics*, 7:452-466, 2019.
- Cited in 01_introduction.md as a question answering evaluation domain.

## Lin et al., 2024
Z. Lin, J. Cui, X. Liao, and X. Wang. Demystifying real-world large language model integrated malicious services, 2024.
- Cited in 08_responsibility-safety-security.md for monitoring evolving risks of LLMs.

## Luong et al., 2015
M. Luong, H. Pham, and C. D. Manning. Effective approaches to attention-based neural machine translation. *CoRR*, abs/1508.04025, 2015.
- Cited in 02_model-architecture.md for global attention.

## Macknight et al., 2024
Macknight, Aung, and Gomes. Personal Communication, 2024.
- Cited in 08_responsibility-safety-security.md for chemical hazard evaluation approach.

## Mozes et al., 2023
M. Mozes, J. Hoffmann, K. Tomanek, M. Kouate, N. Thain, A. Yuan, T. Bolukbasi, and L. Dixon. Towards agile text classifiers for everyone. 2023.
- Cited in 08_responsibility-safety-security.md for building customized classifiers with Gemma using parameter efficient fine tuning.

## Nasr et al., 2023
M. Nasr, N. Carlini, J. Hayase, M. Jagielski, A. F. Cooper, D. Ippolito, C. A. Choquette-Choo, E. Wallace, F. Tramer, and K. Lee. Scalable extraction of training data from (production) language models. *arXiv preprint arXiv:2311.17035*, 2023.
- Cited in 07_memorization-and-privacy.md for vulnerability to attacks causing memorized training data production.

## Phuong et al., 2024
M. Phuong, M. Aitchison, E. Catt, S. Cogan, A. Kaskasoli, V. Krakovna, D. Lindner, M. Rahtz, Y. Assael, S. Hodkinson, H. Howard, T. Lieberum, R. Kumar, M. A. Raad, A. Webson, L. Ho, S. Lin, S. Farquhar, M. Hutter, G. Deletang, A. Ruoss, S. El-Sayed, S. Brown, A. Dragan, R. Shah, A. Shah, and T. Shevlane. Evaluating frontier models for dangerous capabilities, 2024.
- Cited in 08_responsibility-safety-security.md for assurance evaluation methodology and self-proliferation tasks.

## Radford et al., 2019
A. Radford, J. Wu, R. Child, D. Luan, D. Amodei, and I. Sutskever. Language models are unsupervised multitask learners, 2019.
- Cited in 01_introduction.md for LLM capabilities in language understanding, generation, and reasoning.

## Raffel et al., 2019
C. Raffel, N. Shazeer, A. Roberts, K. Lee, S. Narang, M. Matena, Y. Zhou, W. Li, and P. J. Liu. Exploring the limits of transfer learning with a unified text-to-text transformer. *CoRR*, abs/1910.10683, 2019.
- Cited in 01_introduction.md for LLM capabilities in language understanding, generation, and reasoning.

## Ramé et al., 2024
A. Ramé, J. Ferret, N. Vieillard, R. Dadashi, L. Hussenot, P.-L. Cedoz, P. G. Sessa, S. Girgin, A. Douillard, and O. Bachem. Warp: On the benefits of weight averaged rewarded policies. 2024.
- Cited in 04_post-training.md for model averaging/merging.

## Ren et al., 2021
J. Ren, S. Rajbhandari, R. Y. Aminabadi, O. Ruwase, S. Yang, M. Zhang, D. Li, and Y. He. {Zero-offload}: Democratizing {billion-scale} model training. In *2021 USENIX Annual Technical Conference (USENIX ATC 21)*, pages 551-564, 2021.
- Cited in 03_pre-training.md for optimizer state sharding techniques similar to ZeRO-3.

## Roberts et al., 2023
A. Roberts, H. W. Chung, G. Mishra, A. Levskaya, J. Bradbury, D. Andor, S. Narang, B. Lester, C. Gaffney, A. Mohiuddin, et al. Scaling up models and data with t5x and seqio. *Journal of Machine Learning Research*, 24(377):1-8, 2023.
- Cited in 03_pre-training.md for the single controller programming paradigm of Jax.

## Sakaguchi et al., 2019
K. Sakaguchi, R. L. Bras, C. Bhagavatula, and Y. Choi. WINOGRANDE: an adversarial winograd schema challenge at scale. *CoRR*, abs/1907.10641, 2019.
- Cited in 01_introduction.md as a commonsense reasoning evaluation domain.

## Shazeer, 2020
N. Shazeer. GLU variants improve transformer. *CoRR*, abs/2002.05202, 2020.
- Cited in 02_model-architecture.md for the approximated GeGLU non-linearity.

## Shevlane et al., 2023
T. Shevlane, S. Farquhar, B. Garfinkel, M. Phuong, J. Whittlestone, J. Leung, D. Kokotajlo, N. Marchal, M. Anderljung, N. Kolt, L. Ho, D. Siddarth, S. Avin, W. Hawkins, B. Kim, I. Gabriel, V. Bolina, J. Clark, Y. Bengio, P. Christiano, and A. Dafoe. Model evaluation for extreme risks, 2023.
- Cited in 08_responsibility-safety-security.md for capabilities relevant to extreme risks.

## Su et al., 2021
J. Su, Y. Lu, S. Pan, B. Wen, and Y. Liu. Roformer: Enhanced transformer with rotary position embedding. *CoRR*, abs/2104.09864, 2021.
- Cited in 02_model-architecture.md for Rotary Position Embeddings (RoPE).

## Suzgun et al., 2022
M. Suzgun, N. Scales, N. Scharli, S. Gehrmann, Y. Tay, H. W. Chung, A. Chowdhery, Q. V. Le, E. H. Chi, D. Zhou, and J. Wei. Challenging big-bench tasks and whether chain-of-thought can solve them, 2022.
- Cited in 01_introduction.md as a commonsense reasoning evaluation domain.

## Team, 2024 (Qwen)
Q. Team. Introducing qwen1.5, February 2024. URL https://qwenlm.github.io/blog/qwen1.5/.
- Cited in 06_evaluation.md as a baseline model (Qwen1.5 34B).

## Tenney et al., 2020
I. Tenney, J. Wexler, J. Bastings, T. Bolukbasi, A. Coenen, S. Gehrmann, E. Jiang, M. Pushkarna, C. Radebaugh, E. Reif, and A. Yuan. The language interpretability tool: Extensible, interactive visualizations and analysis for nlp models, 2020.
- Cited in 08_responsibility-safety-security.md for the Learning Interpretability Tool used in the prompt-debugging platform.

## Touvron et al., 2023
H. Touvron, T. Lavril, G. Izacard, X. Martinet, M.-A. Lachaux, T. Lacroix, B. Roziere, N. Goyal, E. Hambro, F. Azhar, A. Rodriguez, A. Joulin, E. Grave, and G. Lample. Llama: Open and efficient foundation language models, 2023.
- Cited in 01_introduction.md for small-scale model performance increases from increasing training length.

## Vaswani et al., 2017
A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, L. Kaiser, and I. Polosukhin. Attention is all you need. *CoRR*, abs/1706.03762, 2017.
- Cited in 02_model-architecture.md for the decoder-only transformer architecture.

## Weidinger et al., 2021
L. Weidinger, J. Mellor, M. Rauh, C. Griffin, J. Uesato, P.-S. Huang, M. Cheng, M. Glaese, B. Balle, A. Kasirzadeh, Z. Kenton, S. Brown, W. Hawkins, T. Stepleton, C. Biles, A. Birhane, J. Haas, L. Rimell, L. A. Hendricks, W. Isaac, S. Legassick, G. Irving, and I. Gabriel. Ethical and social risks of harm from language models, 2021.
- Cited in 08_responsibility-safety-security.md for risks of malicious uses of AI.

## xAI, 2024
xAI. grok-1, 2024. URL https://github.com/xai-org/grok-1.
- Cited in 01_introduction.md as a comparable open model.

## XLA, 2019
XLA. Xla: Optimizing compiler for tensorflow, 2019. URL https://www.tensorflow.org/xla.
- Cited in 03_pre-training.md for the MegaScale XLA compiler used in training.

## Xu et al., 2021
Y. Xu, H. Lee, D. Chen, B. A. Hechtman, Y. Huang, R. Joshi, M. Krikun, D. Lepikhin, A. Ly, M. Maggioni, R. Pang, N. Shazeer, S. Wang, T. Wang, Y. Wu, and Z. Chen. GSPMD: general and scalable parallelization for ML computation graphs. *CoRR*, abs/2105.04663, 2021.
- Cited in 03_pre-training.md for the GSPMD partitioner used for training step computation.

## Yang et al., 2023
J. Yang, A. Prabhakar, K. Narasimhan, and S. Yao. Intercode: Standardizing and benchmarking interactive coding with execution feedback, 2023.
- Cited in 08_responsibility-safety-security.md for the InterCode-CTF cybersecurity evaluation.

## Zhang and Sennrich, 2019
B. Zhang and R. Sennrich. Root mean square layer normalization. *CoRR*, abs/1910.07467, 2019.
- Cited in 02_model-architecture.md for RMSNorm used to normalize transformer sub-layers.

## Zheng et al., 2023
L. Zheng, W.-L. Chiang, Y. Sheng, T. Li, S. Zhuang, Z. Wu, Y. Zhuang, Z. Li, Z. Lin, E. Xing, et al. Lmsys-chat-1m: A large-scale real-world llm conversation dataset. *arXiv preprint arXiv:2309.11998*, 2023.
- Cited in 04_post-training.md as the source of prompts (but not answers) used in post-training data.
