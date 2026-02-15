# References

This file contains bibliographic entries for works cited in the section notes.

## Architecture and training

**Vaswani et al., 2017**
A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, L. Kaiser, and I. Polosukhin. Attention is all you need. 2017.
- Cited in: 02_model-architecture.md (general transformer architecture)

**Ainslie et al., 2023**
J. Ainslie, J. Lee-Thorp, M. de Jong, Y. Zemlyanskiy, F. Lebron, and S. Sanghai. Gqa: Training generalized multi-query transformer models from multi-head checkpoints. arXiv preprint arXiv:2305.13245, 2023.
- Cited in: 02_model-architecture.md (Grouped-Query Attention)

**Zhang and Sennrich, 2019**
B. Zhang and R. Sennrich. Root mean square layer normalization. 2019.
- Cited in: 02_model-architecture.md (RMSNorm)

**Dehghani et al., 2023**
M. Dehghani, J. Djolonga, B. Mustafa, P. Padlewski, J. Heek, J. Gilmer, A. P. Steiner, M. Caron, R. Geirhos, I. Alabdulmohsin, et al. Scaling vision transformers to 22 billion parameters. In ICML, 2023.
- Cited in: 02_model-architecture.md (QK-norm inspiration)

**Wortsman et al., 2023**
M. Wortsman, P. J. Liu, L. Xiao, K. Everett, A. Alemi, B. Adlam, J. D. Co-Reyes, I. Gur, A. Kumar, R. Novak, et al. Small-scale proxies for large-scale transformer training instabilities. arXiv preprint arXiv:2309.14322, 2023.
- Cited in: 02_model-architecture.md (QK-norm inspiration)

**Chameleon Team, 2024**
Chameleon Team. Chameleon: Mixed-modal early-fusion foundation models. arXiv preprint arXiv:2405.09818, 2024.
- Cited in: 02_model-architecture.md (QK-norm inspiration)

**Beltagy et al., 2020**
I. Beltagy, M. E. Peters, and A. Cohan. Longformer: The long-document transformer. arXiv preprint arXiv:2004.05150, 2020.
- Cited in: 02_model-architecture.md (local sliding window self-attention)

**Chen et al., 2023**
S. Chen, S. Wong, L. Chen, and Y. Tian. Extending context window of large language models via positional interpolation. arXiv preprint arXiv:2306.15595, 2023.
- Cited in: 02_model-architecture.md, 06_enabling-long-context.md (positional interpolation / RoPE rescaling)

## Vision

**Zhai et al., 2023**
X. Zhai, B. Mustafa, A. Kolesnikov, and L. Beyer. Sigmoid loss for language image pre-training. In CVPR, 2023.
- Cited in: 01_introduction.md, 02_model-architecture.md, 08_vision-encoder.md (SigLIP encoder)

**Dosovitskiy, 2020**
A. Dosovitskiy. An image is worth 16x16 words: Transformers for image recognition at scale. arXiv preprint arXiv:2010.11929, 2020.
- Cited in: 02_model-architecture.md (Vision Transformer)

**Radford et al., 2021**
A. Radford, J. W. Kim, C. Hallacy, A. Ramesh, G. Goh, S. Agarwal, G. Sastry, A. Askell, P. Mishkin, J. Clark, et al. Learning transferable visual models from natural language supervision. In ICML, pages 8748-8763. PMLR, 2021.
- Cited in: 02_model-architecture.md (CLIP loss)

**Liu et al., 2024**
H. Liu, C. Li, Q. Wu, and Y. J. Lee. Visual instruction tuning. NeurIPS, 36, 2024.
- Cited in: 01_introduction.md (LLaVA, Pan and Scan inspiration)

**Steiner et al., 2024**
A. Steiner, A. S. Pinto, M. Tschannen, D. Keysers, X. Wang, Y. Bitton, A. Gritsenko, M. Minderer, A. Sherbondy, S. Long, S. Qin, R. Ingle, E. Bugliarello, S. Kazemzadeh, T. Mesnard, I. Alabdulmohsin, L. Beyer, and X. Zhai. PaliGemma 2: A Family of Versatile VLMs for Transfer. arXiv preprint arXiv:2412.03555, 2024.
- Cited in: 08_performance-evaluation.md, 20_appendix.md (fine-tuning protocol for PaliGemma 2)

## Pre-training and distillation

**Hinton et al., 2015**
G. Hinton, O. Vinyals, and J. Dean. Distilling the knowledge in a neural network. arXiv:1503.02531, 2015.
- Cited in: 01_introduction.md, 03_instruction-tuning.md (knowledge distillation)

**Chung et al., 2023**
H. W. Chung, N. Constant, X. Garcia, A. Roberts, Y. Tay, S. Narang, and O. Firat. Unimax: Fairer and more effective language sampling for large-scale multilingual pretraining, 2023.
- Cited in: 02_model-architecture.md (language representation balancing strategy)

**Kudo and Richardson, 2018**
T. Kudo and J. Richardson. SentencePiece: A simple and language independent subword tokenizer and detokenizer for neural text processing. 2018.
- Cited in: 02_model-architecture.md (tokenizer)

**Sachdeva et al., 2024**
N. Sachdeva, B. Coleman, W.-C. Kang, J. Ni, L. Hong, E. H. Chi, J. Caverlee, J. McAuley, and D. Z. Cheng. How to train data-efficient llms. arXiv preprint arXiv:2402.09668, 2024.
- Cited in: 02_model-architecture.md (quality reweighing step)

**Jacob et al., 2018**
B. Jacob, S. Kligys, B. Chen, M. Zhu, M. Tang, A. Howard, H. Adam, and D. Kalenichenko. Quantization and training of neural networks for efficient integer-arithmetic-only inference. In CVPR, 2018.
- Cited in: 02_model-architecture.md (Quantization Aware Training)

## Compute infrastructure

**Ren et al., 2021**
J. Ren, S. Rajbhandari, R. Y. Aminabadi, O. Ruwase, S. Yang, M. Zhang, D. Li, and Y. He. Zero-offload: Democratizing billion-scale model training. In USENIX, 2021.
- Cited in: 02_model-architecture.md (ZeRO-3 optimizer state sharding)

**Barham et al., 2022**
P. Barham, A. Chowdhery, J. Dean, S. Ghemawat, S. Hand, D. Hurt, M. Isard, H. Lim, R. Pang, S. Roy, B. Saeta, P. Schuh, R. Sepassi, L. E. Shafey, C. A. Thekkath, and Y. Wu. Pathways: Asynchronous distributed dataflow for ml, 2022.
- Cited in: 02_model-architecture.md (Pathways approach for multi-pod training)

**Roberts et al., 2023**
A. Roberts, H. W. Chung, G. Mishra, A. Levskaya, J. Bradbury, D. Andor, S. Narang, B. Lester, C. Gaffney, A. Mohiuddin, et al. Scaling up models and data with t5x and seqio. JMLR, 2023.
- Cited in: 02_model-architecture.md (Jax single controller paradigm)

**Xu et al., 2021**
Y. Xu, H. Lee, D. Chen, B. A. Hechtman, Y. Huang, R. Joshi, M. Krikun, D. Lepikhin, A. Ly, M. Maggioni, R. Pang, N. Shazeer, S. Wang, T. Wang, Y. Wu, and Z. Chen. GSPMD: general and scalable parallelization for ML computation graphs. 2021.
- Cited in: 02_model-architecture.md (GSPMD partitioner)

**XLA, 2019**
Xla: Optimizing compiler for tensorflow, 2019. URL https://www.tensorflow.org/xla.
- Cited in: 02_model-architecture.md (MegaScale XLA compiler)

## Post-training / instruction-tuning

**Agarwal et al., 2024**
R. Agarwal, N. Vieillard, Y. Zhou, P. Stanczyk, S. R. Garea, M. Geist, and O. Bachem. On-policy distillation of language models: Learning from self-generated mistakes. In ICLR, 2024.
- Cited in: 03_instruction-tuning.md (improved knowledge distillation)

**Anil et al., 2018**
R. Anil, G. Pereyra, A. Passos, R. Ormandi, G. E. Dahl, and G. E. Hinton. Large scale distributed neural network training through online distillation. arXiv preprint arXiv:1804.03235, 2018.
- Cited in: 03_instruction-tuning.md (knowledge distillation)

**Sessa et al., 2024**
P. G. Sessa, R. Dadashi, L. Hussenot, J. Ferret, N. Vieillard, A. Ramé, B. Shariari, S. Perrin, A. Friesen, G. Cideron, S. Girgin, P. Stanczyk, A. Michi, D. Sinopalnikov, S. Ramos, S. Heliou, A. Severyn, M. Hoffman, N. Momchev, and O. Bachem. Bond: Aligning llms with best-of-n distillation, 2024.
- Cited in: 03_instruction-tuning.md (BOND for RL finetuning)

**Rame et al., 2024a**
A. Rame, J. Ferret, N. Vieillard, R. Dadashi, L. Hussenot, P.-L. Cedoz, P. G. Sessa, S. Girgin, A. Douillard, and O. Bachem. WARP: On the benefits of weight averaged rewarded policies, 2024a.
- Cited in: 03_instruction-tuning.md (WARP for RL finetuning)

**Rame et al., 2024b**
A. Rame, N. Vieillard, L. Hussenot, R. Dadashi, G. Cideron, O. Bachem, and J. Ferret. WARM: On the benefits of weight averaged reward models. In ICML, 2024b.
- Cited in: 03_instruction-tuning.md (WARM for RL finetuning, weight averaged reward models)

**Gehring et al., 2024**
J. Gehring, K. Zheng, J. Copet, V. Mella, T. Cohen, and G. Synnaeve. Rlef: Grounding code llms in execution feedback with reinforcement learning. arXiv preprint arXiv:2410.02089, 2024.
- Cited in: 03_instruction-tuning.md (code execution feedback)

**DeepSeek-AI, 2025**
DeepSeek-AI. Deepseek-r1: Incentivizing reasoning learning, 2025.
- Cited in: 03_instruction-tuning.md (ground-truth rewards for math)

**Lambert et al., 2024**
N. Lambert, J. Morrison, V. Pyatkin, S. Huang, H. Ivison, F. Brahman, L. J. V. Miranda, A. Liu, N. Dziri, S. Lyu, et al. T\"ulu 3: Pushing frontiers in open language model post-training. arXiv preprint arXiv:2411.15124, 2024.
- Cited in: 03_instruction-tuning.md (ground-truth rewards for math)

## Gemma/Gemini family

**Gemma Team, 2024a**
Gemma Team. Gemma: Open models based on gemini research and technology, 2024a.
- Cited in: 01_introduction.md (prior Gemma models), 09_memorization-and-privacy.md, 10_responsibility-safety-security.md

**Gemma Team, 2024b**
Gemma Team. Gemma 2: Improving open language models at a practical size. arXiv preprint arXiv:2408.00118, 2024b.
- Cited in: 01_introduction.md (Gemma 2), 09_memorization-and-privacy.md (memorization measurement methodology)

**Gemini Team, 2023**
Gemini Team. Gemini: A family of highly capable multimodal models, 2023.
- Cited in: 01_introduction.md (Gemini frontier models), 09_memorization-and-privacy.md, 10_responsibility-safety-security.md

**Gemini Team, 2024**
Gemini Team. Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context, 2024.
- Cited in: 08_performance-evaluation.md (evaluation protocol), 09_memorization-and-privacy.md, 10_responsibility-safety-security.md

## Evaluation and Leaderboards

**Chiang et al., 2024**
W.-L. Chiang, L. Zheng, Y. Sheng, A. N. Angelopoulos, T. Li, D. Li, H. Zhang, B. Zhu, M. Jordan, J. E. Gonzalez, and I. Stoica. Chatbot arena: An open platform for evaluating llms by human preference, 2024.
- Cited in: 04_evaluation-of-final-models.md (LMSYS Chatbot Arena)

**Mirzadeh et al., 2024**
I. Mirzadeh, K. Alizadeh, H. Shahrokhi, O. Tuzel, S. Bengio, and M. Farajtabar. Gsm-symbolic: Understanding the limitations of mathematical reasoning in large language models. arXiv preprint arXiv:2410.05229, 2024.
- Cited in: 05_ablations.md (risk of contamination in benchmark probes)

## Memorization and privacy

**Biderman et al., 2023**
S. Biderman, U. Prashanth, L. Sutawika, H. Schoelkopf, Q. Anthony, S. Purohit, and E. Raff. Emergent and predictable memorization in large language models. NeurIPS, 36: 28072-28090, 2023.
- Cited in: 09_memorization-and-privacy.md

**Carlini et al., 2021**
N. Carlini, F. Tramer, E. Wallace, M. Jagielski, A. Herbert-Voss, K. Lee, A. Roberts, T. Brown, D. Song, U. Erlingsson, et al. Extracting training data from large language models. In USENIX, 2021.
- Cited in: 09_memorization-and-privacy.md

**Carlini et al., 2022**
N. Carlini, D. Ippolito, M. Jagielski, K. Lee, F. Tramer, and C. Zhang. Quantifying memorization across neural language models. arXiv preprint arXiv:2202.07646, 2022.
- Cited in: 09_memorization-and-privacy.md

**Ippolito et al., 2022**
D. Ippolito, F. Tramer, M. Nasr, C. Zhang, M. Jagielski, K. Lee, C. A. Choquette-Choo, and N. Carlini. Preventing verbatim memorization in language models gives a false sense of privacy. arXiv preprint arXiv:2210.17546, 2022.
- Cited in: 09_memorization-and-privacy.md

**Nasr et al., 2023**
M. Nasr, N. Carlini, J. Hayase, M. Jagielski, A. F. Cooper, D. Ippolito, C. A. Choquette-Choo, E. Wallace, F. Tramer, and K. Lee. Scalable extraction of training data from (production) language models. arXiv preprint arXiv:2311.17035, 2023.
- Cited in: 09_memorization-and-privacy.md (discoverable extraction methodology)

**Anil et al., 2023**
R. Anil, A. M. Dai, O. Firat, M. Johnson, D. Lepikhin, A. Passos, S. Shakeri, E. Taropa, P. Bailey, Z. Chen, et al. Palm 2 technical report. arXiv preprint arXiv:2305.10403, 2023.
- Cited in: 09_memorization-and-privacy.md (prior memorization audits)

**Chowdhery et al., 2022**
A. Chowdhery, S. Narang, J. Devlin, M. Bosma, G. Mishra, A. Roberts, P. Barham, H. W. Chung, C. Sutton, S. Gehrmann, ... and N. Fiedel. Palm: Scaling language modeling with pathways. 2022.
- Cited in: 09_memorization-and-privacy.md (prior memorization audits)

**LLaMa Team, 2024**
LLaMa Team. The llama 3 herd of models. arXiv preprint arXiv:2407.21783, 2024.
- Cited in: 09_memorization-and-privacy.md (prior memorization audits)

## Safety and responsibility

**Weidinger et al., 2021**
L. Weidinger, J. Mellor, M. Rauh, C. Griffin, J. Uesato, P.-S. Huang, M. Cheng, M. Glaese, B. Balle, A. Kasirzadeh, Z. Kenton, S. Brown, W. Hawkins, T. Stepleton, C. Biles, A. Birhane, J. Haas, L. Rimell, L. A. Hendricks, W. Isaac, S. Legassick, G. Irving, and I. Gabriel. Ethical and social risks of harm from language models, 2021.
- Cited in: 10_responsibility-safety-security.md (risks of open models)

**Lin et al., 2024**
Z. Lin, J. Cui, X. Liao, and X. Wang. Malla: Demystifying real-world large language model integrated malicious services, 2024.
- Cited in: 10_responsibility-safety-security.md (evolving risks of multimodal LLMs)

**Phuong et al., 2024**
M. Phuong, M. Aitchison, E. Catt, S. Cogan, A. Kaskasoli, V. Krakovna, D. Lindner, M. Rahtz, Y. Assael, S. Hodkinson, H. Howard, T. Lieberum, R. Kumar, M. A. Raad, A. Webson, L. Ho, S. Lin, S. Farquhar, M. Hutter, G. Deletang, A. Ruoss, S. El-Sayed, S. Brown, A. Dragan, R. Shah, A. Dafoe, and T. Shevlane. Evaluating frontier models for dangerous capabilities, 2024.
- Cited in: 10_responsibility-safety-security.md (extreme risk evaluations)

**Shevlane et al., 2023**
T. Shevlane, S. Farquhar, B. Garfinkel, M. Phuong, J. Whittlestone, J. Leung, D. Kokotajlo, N. Marchal, M. Anderljung, N. Kolt, L. Ho, D. Siddarth, S. Avin, W. Hawkins, B. Kim, I. Gabriel, V. Bolina, J. Clark, Y. Bengio, P. Christiano, and A. Dafoe. Model evaluation for extreme risks. 2023.
- Cited in: 10_responsibility-safety-security.md (extreme risk evaluations)

## Benchmark references

**Zellers et al., 2019**
R. Zellers, A. Holtzman, Y. Bisk, A. Farhadi, and Y. Choi. HellaSwag: Can a machine really finish your sentence? In ACL, 2019.
- Cited in: 20_appendix.md (HellaSwag benchmark)

**Clark et al., 2019**
C. Clark, K. Lee, M. Chang, T. Kwiatkowski, M. Collins, and K. Toutanova. Boolq: Exploring the surprising difficulty of natural yes/no questions. CoRR, abs/1905.10044, 2019.
- Cited in: 20_appendix.md (BoolQ benchmark)

**Bisk et al., 2019**
Y. Bisk, R. Zellers, R. L. Bras, J. Gao, and Y. Choi. PIQA: reasoning about physical commonsense in natural language. CoRR, abs/1911.11641, 2019.
- Cited in: 20_appendix.md (PIQA benchmark)

**Sap et al., 2019**
M. Sap, H. Rashkin, D. Chen, R. L. Bras, and Y. Choi. Socialiqa: Commonsense reasoning about social interactions. CoRR, abs/1904.09728, 2019.
- Cited in: 20_appendix.md (SIQA benchmark)

**Joshi et al., 2017**
M. Joshi, E. Choi, D. S. Weld, and L. Zettlemoyer. Triviaqa: A large scale distantly supervised challenge dataset for reading comprehension. CoRR, abs/1705.03551, 2017.
- Cited in: 20_appendix.md (TriviaQA benchmark)

**Kwiatkowski et al., 2019**
T. Kwiatkowski, J. Palomaki, O. Redfield, M. Collins, A. Parikh, C. Alberti, D. Epstein, I. Polosukhin, J. Devlin, K. Lee, K. Toutanova, L. Jones, M. Kelcey, M.-W. Chang, A. M. Dai, J. Uszkoreit, Q. Le, and S. Petrov. Natural questions: A benchmark for question answering research. ACL, 2019.
- Cited in: 20_appendix.md (Natural Questions benchmark)

**Chollet, 2019**
F. Chollet. On the measure of intelligence. arXiv preprint arXiv:1911.01547, 2019.
- Cited in: 20_appendix.md (ARC-C and ARC-E benchmarks)

**Sakaguchi et al., 2019**
K. Sakaguchi, R. L. Bras, C. Bhagavatula, and Y. Choi. WINOGRANDE: an adversarial winograd schema challenge at scale. CoRR, abs/1907.10641, 2019.
- Cited in: 20_appendix.md (WinoGrande benchmark)

**Suzgun et al., 2022**
M. Suzgun, N. Scales, N. Scharli, S. Gehrmann, Y. Tay, H. W. Chung, A. Chowdhery, Q. V. Le, E. H. Chi, D. Zhou, and J. Wei. Challenging big-bench tasks and whether chain-of-thought can solve them, 2022.
- Cited in: 20_appendix.md (BBH benchmark)

**Dua et al., 2019**
D. Dua, Y. Wang, P. Dasigi, G. Stanovsky, S. Singh, and M. Gardner. DROP: A reading comprehension benchmark requiring discrete reasoning over paragraphs. In ACL, 2019.
- Cited in: 20_appendix.md (DROP benchmark)

**Hendrycks et al., 2020**
D. Hendrycks, C. Burns, S. Basart, A. Zou, M. Mazeika, D. Song, and J. Steinhardt. Measuring massive multitask language understanding. CoRR, abs/2009.03300, 2020.
- Cited in: 20_appendix.md (MMLU benchmark)

**Wang et al., 2024**
Y. Wang, X. Ma, G. Zhang, Y. Ni, A. Chandra, S. Guo, W. Ren, A. Arulraj, X. He, Z. Jiang, et al. Mmlu-pro: A more robust and challenging multi-task language understanding benchmark. In NeurIPS, 2024.
- Cited in: 20_appendix.md (MMLU-Pro benchmark)

**Zhong et al., 2023**
W. Zhong, R. Cui, Y. Guo, Y. Liang, S. Lu, Y. Wang, A. Saied, W. Chen, and N. Duan. Agieval: A human-centric benchmark for evaluating foundation models, 2023.
- Cited in: 20_appendix.md (AGIEval benchmark)

**Hendrycks et al., 2021**
D. Hendrycks, C. Burns, S. Kadavath, A. Arora, S. Basart, E. Tang, D. Song, and J. Steinhardt. Measuring mathematical problem solving with the math dataset. NeurIPS, 2021.
- Cited in: 20_appendix.md (MATH benchmark)

**Rein et al., 2023**
D. Rein, B. L. Hou, A. C. Stickland, J. Petty, R. Y. Pang, J. Dirani, J. Michael, and S. R. Bowman. Gpqa: A graduate-level google-proof q&a benchmark. ArXiv, abs/2311.12022, 2023.
- Cited in: 20_appendix.md (GPQA benchmark)

**Cobbe et al., 2021**
K. Cobbe, V. Kosaraju, M. Bavarian, M. Chen, H. Jun, L. Kaiser, M. Plappert, J. Tworek, J. Hilton, R. Nakano, C. Hesse, and J. Schulman. Training verifiers to solve math word problems. CoRR, abs/2110.14168, 2021.
- Cited in: 20_appendix.md (GSM8K benchmark)

**Austin et al., 2021**
J. Austin, A. Odena, M. I. Nye, M. Bosma, H. Michalewski, D. Dohan, E. Jiang, C. J. Cai, M. Terry, Q. V. Le, and C. Sutton. Program synthesis with large language models. CoRR, abs/2108.07732, 2021.
- Cited in: 20_appendix.md (MBPP benchmark)

**Chen et al., 2021**
G. Sastry, P. Mishkin, B. Chan, S. Gray, N. Ryder, M. Pavlov, A. Power, L. Kaiser, M. Bavarian, C. Winter, P. Tillet, F. P. Such, D. Cummings, M. Plappert, F. Chantzis, E. Barnes, A. Herbert-Voss, W. H. Guss, A. Nichol, A. Paino, N. Tezak, J. Tang, I. Babuschkin, S. Balaji, S. Jain, W. Saunders, C. Hesse, A. N. Carr, J. Leike, J. Achiam, V. Misra, E. Morikawa, A. Radford, M. Knight, M. Brundage, M. Murati, K. Mayer, P. Welinder, B. McGrew, D. Amodei, S. McCandlish, I. Sutskever, and W. Zaremba. Evaluating large language models trained on code. CoRR, abs/2107.03374, 2021.
- Cited in: 20_appendix.md (HumanEval benchmark)

## Multimodal benchmarks

**Chen et al., 2015**
X. Chen, H. Fang, T.-Y. Lin, R. Vedantam, S. Gupta, P. Dollar, and C. L. Zitnick. Microsoft coco captions: Data collection and evaluation server. ArXiv, abs/1504.00325, 2015.
- Cited in: 20_appendix.md (COCO Caption benchmark)

**Mathew et al., 2020**
M. Mathew, D. Karatzas, R. Manmatha, and C. V. Jawahar. Docvqa: A dataset for vqa on document images. WACV, 2020.
- Cited in: 20_appendix.md (DocVQA benchmark)

**Mathew et al., 2022**
M. Mathew, V. Bagal, R. Tito, D. Karatzas, E. Valveny, and C. Jawahar. Infographicvqa. In WACV, 2022.
- Cited in: 20_appendix.md (InfographicVQA benchmark)

**Yue et al., 2023**
X. Yue, Y. Ni, K. Zhang, T. Zheng, R. Liu, G. Zhang, S. Stevens, D. Jiang, W. Ren, Y. Sun, C. Wei, B. Yu, R. Yuan, R. Sun, M. Yin, B. Zheng, Z. Yang, Y. Liu, W. Huang, H. Sun, Y. Su, and W. Chen. Mmmu: A massive multi-discipline multimodal understanding and reasoning benchmark for expert agi. CVPR, 2023.
- Cited in: 20_appendix.md (MMMU benchmark)

**Singh et al., 2019**
A. Singh, V. Natarjan, M. Shah, Y. Jiang, X. Chen, D. Parikh, and M. Rohrbach. Towards vqa models that can read. In CVPR, 2019.
- Cited in: 20_appendix.md (TextVQA benchmark)

**Rea**
RealWorldQA benchmark (no full reference provided in paper).
- Cited in: 20_appendix.md (RealWorldQA benchmark)

**Kazemi et al., 2024a**
M. Kazemi, N. Dikkala, A. Anand, P. Devic, I. Dasgupta, F. Liu, B. Fatemi, P. Awasthi, D. Guo, S. Gollapudi, and A. Qureshi. Remi: A dataset for reasoning with multiple images. ArXiv, abs/2406.09175, 2024a.
- Cited in: 20_appendix.md (ReMI benchmark)

**Kembhavi et al., 2016**
A. Kembhavi, M. Salvato, E. Kolve, M. Seo, H. Hajishirzi, and A. Farhadi. A diagram is worth a dozen images. ArXiv, abs/1603.07396, 2016.
- Cited in: 08_performance-evaluation.md, 20_appendix.md (AI2D benchmark)

**Masry et al., 2022**
A. Masry, X. L. Do, J. Q. Tan, S. Joty, and E. Hoque. ChartQA: A benchmark for question answering about charts with visual and logical reasoning. ACL, 2022.
- Cited in: 08_performance-evaluation.md, 20_appendix.md (ChartQA benchmark)

**Goyal et al., 2017**
Y. Goyal, T. Khot, D. Summers-Stay, D. Batra, and D. Parikh. Making the V in VQA matter: Elevating the role of image understanding in Visual Question Answering. In CVPR, 2017.
- Cited in: 08_performance-evaluation.md, 20_appendix.md (VQA v2 benchmark)

**Fu et al., 2024**
X. Fu, Y. Hu, B. Li, Y. Feng, H. Wang, X. Lin, D. Roth, N. A. Smith, W.-C. Ma, and R. Krishna. Blink: Multimodal large language models can see but not perceive. ArXiv, abs/2404.12390, 2024.
- Cited in: 08_performance-evaluation.md, 20_appendix.md (BLINK benchmark)

**Marino et al., 2019**
K. Marino, M. Rastegari, A. Farhadi, and R. Mottaghi. Ok-vqa: A visual question answering benchmark requiring external knowledge. In CVPR, 2019.
- Cited in: 08_performance-evaluation.md, 20_appendix.md (OK-VQA benchmark)

**Acharya et al., 2019**
M. Acharya, K. Kafle, and C. Kanan. Tallyqa: Answering complex counting questions. In AAAI, 2018.
- Cited in: 08_performance-evaluation.md, 20_appendix.md (TallyQA benchmark)

**Yang et al., 2019**
K. Yang, O. Russakovsky, and J. Deng. Spatialsense: An adversarially crowdsourced benchmark for spatial relation recognition. ICCV, 2019.
- Cited in: 08_performance-evaluation.md, 20_appendix.md (SpatialSense VQA benchmark)

**Paiss et al., 2023**
R. Paiss, A. Ephrat, O. Tov, S. Zada, I. Mosseri, M. Irani, and T. Dekel. Teaching clip to count to ten. ICCV, 2023.
- Cited in: 08_performance-evaluation.md, 20_appendix.md (CountBench VQA benchmark)

## Multilingual benchmarks

**Shi et al., 2023**
F. Shi, M. Suzgun, M. Freitag, X. Wang, S. Srivats, S. Vosoughi, H. W. Chung, Y. Tay, S. Ruder, D. Zhou, D. Das, and J. Wei. Language models are multilingual chain-of-thought reasoners. In ICLR, 2023.
- Cited in: 08_performance-evaluation.md, 20_appendix.md (MGSM benchmark)

**Singh et al., 2024b**
S. Singh, A. Romanou, C. Fourrier, D. I. Adelani, J. G. Ngui, D. Vila-Suero, P. Limkonchotiwat, K. Marchisio, W. Q. Leong, Y. Susanto, R. Ng, S. Longpre, W.-Y. Ko, M. Smith, A. Bosselut, A. Oh, A. F. T. Martins, L. Choshen, D. Ippolito, E. Ferrante, M. Fadaee, B. Ermis, and S. Hooker. Global mmlu: Understanding and addressing cultural and linguistic biases in multilingual evaluation, 2024b.
- Cited in: 08_performance-evaluation.md, 20_appendix.md (Global-MMLU-Lite benchmark)

**Deutsch et al., 2025**
D. Deutsch, E. Briakou, I. Caswell, M. Finkelstein, R. Galor, J. Juraska, G. Kovacs, A. Lui, R. Rei, J. Riesa, S. Rijhwani, P. Riley, E. Salesky, F. Trabelsi, S. Winkler, B. Zhang, and M. Freitag. Wmt24++: Expanding the language coverage of wmt24 to 55 languages & dialects, 2025.
- Cited in: 08_performance-evaluation.md, 20_appendix.md (WMT24++ benchmark)

**Goyal et al., 2022**
N. Goyal, C. Gao, V. Chaudhary, P.-J. Chen, G. Wenzek, D. Ju, S. Krishnan, M. Ranzato, F. Guzman, and A. Fan. The flores-101 evaluation benchmark for low-resource and multilingual machine translation. ACL, 2022.
- Cited in: 08_performance-evaluation.md, 20_appendix.md (FLoRes benchmark)

**Artetxe et al., 2020**
M. Artetxe, S. Ruder, and D. Yogatama. On the cross-lingual transferability of monolingual representations. In ACL, 2020.
- Cited in: 08_performance-evaluation.md, 20_appendix.md (XQuAD benchmark)

**Goldman et al., 2025**
O. Goldman, U. Shaham, D. Malkin, S. Eiger, A. Hassidim, Y. Matias, J. Maynez, A. M. Gilady, J. Riesa, S. Rijhwani, L. Rimell, I. Szpektor, R. Tsarfaty, and M. Eyal. Eclektic: a novel challenge set for evaluation of cross-lingual knowledge transfer, 2025.
- Cited in: 08_performance-evaluation.md, 20_appendix.md (ECLeKTic benchmark)

**Singh et al., 2024a**
H. Singh, N. Gupta, S. Bharadwaj, D. Tewari, and P. Talukdar. Indicgenbench: a multilingual benchmark to evaluate generation capabilities of llms on indic languages. arXiv preprint arXiv:2404.16816, 2024a.
- Cited in: 08_performance-evaluation.md, 20_appendix.md (IndicGenBench benchmark)

**Asai et al., 2020**
A. Asai, J. Kasai, J. H. Clark, K. Lee, E. Choi, and H. Hajishirzi. Xor qa: Cross-lingual open-retrieval question answering. arXiv preprint arXiv:2010.11856, 2020.
- Cited in: 08_performance-evaluation.md, 20_appendix.md (XOR QA benchmark)

## Long context benchmarks

**Hsieh et al., 2024**
C.-P. Hsieh, S. Sun, S. Kriman, S. Acharya, D. Rekesh, F. Jia, Y. Zhang, and B. Ginsburg. Ruler: What's the real context size of your long-context language models? arXiv preprint arXiv:2404.06654, 2024.
- Cited in: 08_performance-evaluation.md, 20_appendix.md (RULER benchmark)

**Vodrahalli et al., 2024**
K. Vodrahalli, S. Ontanon, N. Tripuraneni, K. Xu, S. Jain, R. Shivanna, J. Hui, N. Dikkala, M. Kazemi, B. Fatemi, et al. Michelangelo: Long context evaluations beyond haystacks via latent structure queries. arXiv preprint arXiv:2409.12640, 2024.
- Cited in: 08_performance-evaluation.md, 20_appendix.md (MRCR benchmark)

## IT model benchmarks

**Kazemi et al., 2025**
M. Kazemi, B. Fatemi, H. Bansal, J. Palowitch, C. Anastasiou, S. V. Mehta, L. K. Jain, V. Aglietti, D. Jindal, P. Chen, et al. Big-bench extra hard. arXiv preprint arXiv:2502.19187, 2025.
- Cited in: 08_performance-evaluation.md (BBEH benchmark)

**Fatemi et al., 2024**
B. Fatemi, M. Kazemi, A. Tsitsulin, K. Malkan, J. Yim, J. Palowitch, S. Seo, J. Halcrow, and B. Perozzi. Test of time: A benchmark for evaluating llms on temporal reasoning. arXiv preprint arXiv:2406.09170, 2024.
- Cited in: 08_performance-evaluation.md (reasoning task in BBEH)

**Hessel et al., 2022**
J. Hessel, A. Marasovic, J. D. Hwang, L. Lee, J. Da, R. Zellers, R. Mankoff, and Y. Choi. Do androids laugh at electric sheep? humor" understanding" benchmarks from the new yorker caption contest. arXiv preprint arXiv:2209.06293, 2022.
- Cited in: 08_performance-evaluation.md (reasoning task in BBEH)

**Kazemi et al., 2023**
M. Kazemi, H. Alvari, A. Anand, J. Wu, X. Chen, and R. Soricut. Geomverse: A systematic evaluation of large models for geometric reasoning. arXiv preprint arXiv:2312.12241, 2023.
- Cited in: 08_performance-evaluation.md (reasoning task in BBEH)

**Kazemi et al., 2024b**
M. Kazemi, Q. Yuan, D. Bhatia, N. Kim, X. Xu, V. Imbrasaite, and D. Ramachandran. Boardgameqa: A dataset for natural language reasoning with contradictory information. NeurIPS, 36, 2024b.
- Cited in: 08_performance-evaluation.md (reasoning task in BBEH)

**Kiciman et al., 2023**
E. Kiciman, R. Ness, A. Sharma, and C. Tan. Causal reasoning and large language models: Opening a new frontier for causality. arXiv preprint arXiv:2305.00050, 2023.
- Cited in: 08_performance-evaluation.md (reasoning task in BBEH)

**Nie et al., 2024**
A. Nie, Y. Zhang, A. S. Amdekar, C. Piech, T. B. Hashimoto, and T. Gerstenberg. Moca: Measuring human-language model alignment on causal and moral judgment tasks. NeurIPS, 36, 2024.
- Cited in: 08_performance-evaluation.md (reasoning task in BBEH)

**Sanchez et al., 2024**
E. Sanchez, B. Alastruey, C. Ropers, P. Stenetorp, M. Artetxe, and M. R. Costa-jussa. Linguini: A benchmark for language-agnostic linguistic reasoning. arXiv preprint arXiv:2409.12126, 2024.
- Cited in: 08_performance-evaluation.md (reasoning task in BBEH)

**Shah et al., 2024**
K. Shah, N. Dikkala, X. Wang, and R. Panigrahy. Causal language modeling can elicit search and reasoning capabilities on logic puzzles. arXiv preprint arXiv:2409.10502, 2024.
- Cited in: 08_performance-evaluation.md (reasoning task in BBEH)

**Tyen et al., 2023**
G. Tyen, H. Mansoor, P. Chen, T. Mak, and V. Carbune. Llms cannot find reasoning errors, but can correct them! arXiv preprint arXiv:2311.08516, 2023.
- Cited in: 08_performance-evaluation.md (reasoning task in BBEH)

**White et al., 2024**
C. White, S. Dooley, M. Roberts, A. Pal, B. Feuer, S. Jain, R. Schwartz-Ziv, N. Jain, K. Saifullah, S. Naidu, et al. Livebench: A challenging, contamination-free llm benchmark. arXiv preprint arXiv:2406.19314, 2024.
- Cited in: 08_performance-evaluation.md (reasoning task in BBEH)

**Yamada et al., 2023**
Y. Yamada, Y. Bao, A. K. Lampinen, J. Kasai, and I. Yildirim. Evaluating spatial understanding of large language models. arXiv preprint arXiv:2310.14540, 2023.
- Cited in: 08_performance-evaluation.md (reasoning task in BBEH)

**Zhang et al., 2024**
J. Zhang, L. Jain, Y. Guo, J. Chen, K. L. Zhou, S. Suresh, A. Wagenmaker, S. Sievert, T. Rogers, K. Jamieson, et al. Humor in ai: Massive scale crowd-sourced preferences and benchmarks for cartoon captioning. arXiv preprint arXiv:2406.10522, 2024.
- Cited in: 08_performance-evaluation.md (reasoning task in BBEH)

**Macknight et al.**
Macknight, Aung, and Gomes. Personal Communication.
- Cited in: 10_responsibility-safety-security.md (CBRN chemical hazards evaluation)

