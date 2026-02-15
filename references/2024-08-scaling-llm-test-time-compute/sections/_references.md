# References

Only references actually cited in the section notes are included below.

---

**[1]** Training revision models with synthetic data. Coming soon, 2024.
- Cited in 06_refining-proposal-distribution.md (recipe for pairing correct answers with incorrect ones for revision finetuning data) and 09_acknowledgements.md (edit distance based sampling).

**[2]** C. Andrieu, N. De Freitas, A. Doucet, and M. I. Jordan. An introduction to MCMC for machine learning. 2003.
- Cited in 02_unified-perspective.md as analogy to MCMC sampling from complex target distributions.

**[3]** R. Anil, A. M. Dai, O. Firat, M. Johnson, D. Lepikhin, A. Passos, S. Shakeri, E. Taropa, P. Bailey, Z. Chen, E. Chu, J. H. Clark, L. E. Shafey, Y. Huang, K. Meier-Hellstern, G. Mishra, E. Moreira, M. Omernick, K. Robinson, S. Ruder, Y. Tay, K. Xiao, Y. Xu, Y. Zhang, G. H. Abrego, J. Ahn, J. Austin, P. Barham, J. Botha, J. Bradbury, S. Brahma, K. Brooks, M. Catasta, Y. Cheng, C. Cherry, C. A. Choquette-Choo, A. Chowdhery, C. Crepy, S. Dave, M. Dehghani, S. Dev, J. Devlin, M. Diaz, N. Du, E. Dyer, V. Feinberg, F. Feng, V. Fienber, M. Freitag, X. Garcia, S. Gehrmann, L. Gonzalez, G. Gur-Ari, S. Hand, H. Hashemi, L. Hou, J. Howland, A. Hu, J. Hui, J. Hurwitz, M. Isard, A. Ittycheriah, M. Jagielski, W. Jia, K. Kenealy, M. Krikun, S. Kudugunta, C. Lan, K. Lee, B. Lee, E. Li, M. Li, W. Li, Y. Li, J. Li, H. Lim, Z. Lin, Z. Liu, F. Liu, M. Maggioni, A. Mahendru, J. Maynez, V. Misra, M. Moussalem, Z. Nado, J. Nham, E. Ni, A. Nystrom, A. Parrish, M. Pellat, M. Polacek, A. Polozov, R. Pope, S. Qiao, E. Reif, B. Richter, P. Riley, A. C. Ros, A. Roy, B. Saeta, R. Samuel, R. Shelby, A. Slone, D. Smilkov, D. R. So, D. Sohn, S. Tokumine, D. Valter, V. Vasudevan, K. Vodrahalli, X. Wang, P. Wang, Z. Wang, T. Wang, J. Wieting, Y. Wu, K. Xu, Y. Xu, L. Xue, P. Yin, J. Yu, Q. Zhang, S. Zheng, C. Zheng, W. Zhou, D. Zhou, S. Petrov, and Y. Wu. Palm 2 technical report, 2023.
- Cited in 01_introduction.md and 04_experimental-setup.md as the base model family (PaLM 2-S* Codey).

**[4]** Y. Bai, S. Kadavath, S. Kundu, A. Askell, J. Kernion, A. Jones, A. Chen, A. Goldie, A. Mirhoseini, C. McKinnon, C. Chen, C. Olsson, C. Olah, D. Hernandez, D. Drain, D. Ganguli, D. Li, E. Tran-Johnson, E. Perez, J. Kerr, J. Mueller, J. Ladish, J. Landau, K. Ndousse, K. Lukosuite, L. Lovitt, M. Sellitto, N. Elhage, N. Schiefer, N. Mercado, N. DasSarma, R. Lasenby, R. Larson, S. Ringer, S. Johnston, S. Kravec, S. E. Showk, S. Fort, T. Lanham, T. Telleen-Lawton, T. Conerly, T. Henighan, T. Hume, S. R. Bowman, Z. Hatfield-Dodds, B. Mann, D. Amodei, N. Joseph, S. McCandlish, T. Brown, and J. Kaplan. Constitutional AI: Harmlessness from AI feedback, 2022.
- Cited in 01_introduction.md and 02_unified-perspective.md as prior work on self-critique.

**[5]** C. Blakeney, M. Paul, B. W. Larsen, S. Owen, and J. Frankle. Does your data spark joy? Performance gains from domain upsampling at the end of training, 2024. URL https://arxiv.org/abs/2406.03476.
- Cited in 01_introduction.md (footnote on future LLMs being more effective at verification/revision due to targeted data).

**[6]** G. Chen, M. Liao, C. Li, and K. Fan. Alphamath almost zero: Process supervision without process, 2024.
- Cited in 02_unified-perspective.md and 05_scaling-via-verifiers.md as related work on process-based verifiers and tree search.

**[7]** K. Cobbe, V. Kosaraju, M. Bavarian, M. Chen, H. Jun, L. Kaiser, M. Plappert, J. Tworek, J. Hilton, R. Nakano, C. Hesse, and J. Schulman. Training verifiers to solve math word problems, 2021.
- Cited in 01_introduction.md and 02_unified-perspective.md as canonical best-of-N sampling with verifiers.

**[8]** Y. Du, S. Li, A. Torralba, J. B. Tenenbaum, and I. Mordatch. Improving factuality and reasoning in language models through multiagent debate, 2023.
- Cited in 01_introduction.md and 02_unified-perspective.md as prior work on self-critique/debate.

**[9]** J. S. B. T. Evans. Heuristic and analytic processes in reasoning. *British Journal of Psychology*, 75(4):451-468, 1984.
- Cited in 01_introduction.md as motivation for humans thinking longer on difficult problems.

**[10]** X. Feng, Z. Wan, M. Wen, S. M. McAleer, Y. Wen, W. Zhang, and J. Wang. Alphazero-like tree-search can guide large language model decoding and training, 2024.
- Cited in 02_unified-perspective.md and 05_scaling-via-verifiers.md (BFS-V beam search implementation).

**[13]** D. Hendrycks, C. Burns, S. Kadavath, A. Arora, S. Basart, E. Tang, D. Song, and J. Steinhardt. Measuring mathematical problem solving with the MATH dataset, 2021.
- Cited in 01_introduction.md and 04_experimental-setup.md as the benchmark used (MATH).

**[14]** J. Hoffmann, S. Borgeaud, A. Mensch, E. Buchatskaya, T. Cai, E. Rutherford, D. de Las Casas, L. A. Hendricks, J. Welbl, A. Clark, T. Hennigan, E. Noland, K. Millican, G. van den Driessche, B. Damoc, A. Guy, S. Osindero, K. Simonyan, E. Elsen, J. W. Rae, O. Vinyals, and L. Sifre. Training compute-optimal large language models, 2022.
- Cited in 07_exchanging-pretraining-test-time.md for the pretraining FLOPs approximation X = 6ND_pretrain and the design decision of allocating compute to data vs. parameters.

**[15]** J. Huang, X. Chen, S. Mishra, H. S. Zheng, A. W. Yu, X. Song, and D. Zhou. Large language models cannot self-correct reasoning yet, 2023.
- Cited in 01_introduction.md (negative results for test-time strategies on reasoning) and 06_refining-proposal-distribution.md (prompting LLMs to self-correct is largely ineffective).

**[17]** D. Kahneman. Maps of bounded rationality: Psychology for behavioral economics. *The American Economic Review*, 93(5):1449-1475, 2003.
- Cited in 01_introduction.md as motivation for humans thinking longer on difficult problems.

**[18]** D. Kahneman. *Thinking, Fast and Slow*. Farrar, Straus and Giroux, New York, first paperback edition, 2013.
- Cited in 01_introduction.md as motivation for humans thinking longer on difficult problems.

**[21]** Y. Li, Z. Lin, S. Zhang, Q. Fu, B. Chen, J.-G. Lou, and W. Chen. Making large language models better reasoners with step-aware verifier, 2023.
- Cited in 05_scaling-via-verifiers.md for the "best-of-N weighted" inter-answer aggregation method.

**[22]** H. Lightman, V. Kosaraju, Y. Burda, H. Edwards, B. Baker, T. Lee, J. Leike, J. Schulman, I. Sutskever, and K. Cobbe. Let's verify step by step, 2023.
- Cited extensively in 01_introduction.md, 02_unified-perspective.md, 03_scaling-test-time-computation.md, 04_experimental-setup.md, and 05_scaling-via-verifiers.md as the foundational PRM training work, PRM800k dataset, difficulty binning procedure, and step-wise verification.

**[23]** A. Madaan, N. Tandon, P. Gupta, S. Hallinan, L. Gao, S. Wiegreffe, U. Alon, N. Dziri, S. Prabhumoye, Y. Yang, S. Gupta, B. P. Majumder, K. Hermann, S. Welleck, A. Yazdanbakhsh, and P. Clark. Self-refine: Iterative refinement with self-feedback, 2023.
- Cited in 01_introduction.md and 02_unified-perspective.md as prior work on self-critique. Cited in 08_discussion-future-work.md as a technique (critique and revise) not studied in this work.

**[24]** N. McAleese, R. Pokorny, J. F. Ceron Uribe, E. Nitishinskaya, M. Trebacz, and J. Leike. LLM critics help catch LLM bugs. *OpenAI*, 2024.
- Cited in 01_introduction.md (footnote on future LLMs being more effective at verification).

**[28]** Y. Qu, T. Zhang, N. Garg, and A. Kumar. Recursive introspection: Teaching foundation models how to self-improve. 2024.
- Cited extensively in 01_introduction.md, 02_unified-perspective.md, and 06_refining-proposal-distribution.md as the primary recipe for finetuning revision models; the authors build on this approach.

**[29]** N. Sardana and J. Frankle. Beyond chinchilla-optimal: Accounting for inference in language model scaling laws, 2023.
- Cited in 07_exchanging-pretraining-test-time.md for the inference FLOPs approximation Y = 2ND_inference and compute-optimal scaling of pretraining compute.

**[30]** W. Saunders, C. Yeh, J. Wu, S. Bills, L. Ouyang, J. Ward, and J. Leike. Self-critiquing models for assisting human evaluators, 2022.
- Cited in 01_introduction.md and 02_unified-perspective.md as prior work on self-critique.

**[31]** A. Setlur, S. Garg, X. Geng, N. Garg, V. Smith, and A. Kumar. RL on incorrect synthetic data scales the efficiency of LLM math reasoning by eight-fold. *arXiv preprint arXiv:2406.14532*, 2024.
- Cited in 05_scaling-via-verifiers.md as recent work where PRM per-step predictions correspond to value estimates of reward-to-go.

**[33]** A. Sharma, S. Keh, E. Mitchell, C. Finn, K. Arora, and T. Kollar. A critical evaluation of AI feedback for aligning large language models, 2024. URL https://arxiv.org/abs/2402.12366.
- Cited in 01_introduction.md (footnote on capability-specific finetuning being necessary).

**[34]** N. Shinn, F. Cassano, E. Berman, A. Gopinath, K. Narasimhan, and S. Yao. Reflexion: Language agents with verbal reinforcement learning, 2023.
- Cited in 01_introduction.md as prior work showing test-time capability can unlock agentic tasks.

**[35]** A. Singh, J. D. Co-Reyes, R. Agarwal, A. Anand, P. Patil, X. Garcia, P. J. Liu, J. Harrison, J. Lee, K. Xu, A. Parisi, A. Kumar, A. Alemi, A. Rizkowsky, A. Nova, B. Adlam, B. Bohnet, G. Elsayed, H. Sedghi, I. Mordatch, I. Simpson, I. Gur, J. Snoek, J. Pennington, J. Hron, K. Kenealy, K. Swersky, K. Mahajan, L. Culp, L. Xiao, M. L. Bileschi, N. Constant, R. Novak, R. Liu, T. Warkentin, Y. Qian, Y. Bansal, E. Dyer, B. Neyshabur, J. Sohl-Dickstein, and N. Fiedel. Beyond human data: Scaling self-training for problem-solving with language models, 2024.
- Cited in 02_unified-perspective.md as RL-inspired finetuning methods (STaR/ReST^EM) for improving the proposal distribution.

**[36]** C. Snell, E. Wallace, D. Klein, and S. Levine. Predicting emergent capabilities by finetuning. *Conference on Language Modeling 2024*, 2024.
- Cited in 01_introduction.md (footnote on future LLMs being more effective at verification/revision).

**[37]** K. Stechly, M. Marquez, and S. Kambhampati. GPT-4 doesn't know it's wrong: An analysis of iterative prompting for reasoning problems, 2023.
- Cited in 01_introduction.md as negative results for test-time strategies.

**[38]** R. S. Sutton and A. G. Barto. *Reinforcement Learning: An Introduction*. Second edition, 2018.
- Cited in 05_scaling-via-verifiers.md (lookahead search as a special case of MCTS).

**[41]** H. Touvron, L. Martin, K. Stone, P. Albert, A. Almahairi, Y. Babaei, N. Bashlykov, S. Batra, P. Bhargava, S. Bhosale, D. Bikel, L. Blecher, C. C. Ferrer, M. Chen, G. Cucurull, D. Esiobu, J. Fernandes, J. Fu, W. Fu, B. Fuller, C. Gao, V. Goswami, N. Goyal, A. Hartshorn, S. Hosseini, R. Hou, H. Inan, M. Kardas, V. Kerkez, M. Khabsa, I. Kloumann, A. Korenev, P. S. Koura, M.-A. Lachaux, T. Lavril, J. Lee, D. Liskovich, Y. Lu, Y. Mao, X. Martinet, T. Mihaylov, P. Mishra, I. Molybog, Y. Nie, A. Poulton, J. Reizenstein, R. Rungta, K. Saladi, A. Schelten, R. Silva, E. M. Smith, R. Subramanian, X. E. Tan, B. Tang, R. Taylor, A. Williams, J. X. Kuan, P. Xu, Z. Yan, I. Zarov, Y. Zhang, A. Fan, M. Kambadur, S. Narang, A. Rodriguez, R. Stojnic, S. Edunov, and T. Scialom. Llama 2: Open foundation and fine-tuned chat models, 2023. URL https://arxiv.org/abs/2307.09288.
- Cited in 07_exchanging-pretraining-test-time.md as the LLaMA series approach to scaling (parameters scaled up, data fixed).

**[42]** J. Uesato, N. Kushman, R. Kumar, F. Song, N. Siegel, L. Wang, A. Creswell, G. Irving, and I. Higgins. Solving math word problems with process- and outcome-based feedback, 2022.
- Cited in 05_scaling-via-verifiers.md as original PRM training work using human crowd-worker labels.

**[43]** K. Valmeekam, M. Marquez, and S. Kambhampati. Can large language models really improve by self-critiquing their own plans?, 2023.
- Cited in 01_introduction.md as negative results for test-time strategies.

**[45]** P. Wang, L. Li, Z. Shao, R. X. Xu, D. Dai, Y. Li, D. Chen, Y. Wu, and Z. Sui. Math-shepherd: Verify and reinforce LLMs step-by-step without human annotations, 2023.
- Cited in 01_introduction.md, 02_unified-perspective.md, and 05_scaling-via-verifiers.md for supervising PRMs without human labels using Monte Carlo rollout estimates.

**[47]** J. Wei, X. Wang, D. Schuurmans, M. Bosma, B. Ichter, F. Xia, E. Chi, Q. Le, and D. Zhou. Chain-of-thought prompting elicits reasoning in large language models, 2023.
- Cited in 01_introduction.md as prior work showing test-time capability can unlock reasoning tasks.

**[48]** S. Yao, D. Yu, J. Zhao, I. Shafran, T. L. Griffiths, Y. Cao, and K. Narasimhan. Tree of thoughts: Deliberate problem solving with large language models, 2023.
- Cited in 01_introduction.md, 02_unified-perspective.md, and 05_scaling-via-verifiers.md (BFS-V beam search and tree search over solutions).

**[11]** L. Gao, A. Madaan, S. Zhou, U. Alon, P. Liu, Y. Yang, J. Callan, and G. Neubig. PAL: Program-aided language models, 2023. URL https://arxiv.org/abs/2211.10435.
- Cited in 10_appendix-a-related-work.md as an example of augmenting LMs with reasoning tools at test-time.

**[12]** S. Goyal, Z. Ji, A. S. Rawat, A. K. Menon, S. Kumar, and V. Nagarajan. Think before you speak: Training language models with pause tokens, 2024. URL https://arxiv.org/abs/2310.02226.
- Cited in 10_appendix-a-related-work.md as work on learning thought tokens in an unsupervised manner.

**[16]** A. L. Jones. Scaling scaling laws with board games, 2021. URL https://arxiv.org/abs/2104.03113.
- Cited in 10_appendix-a-related-work.md as prior work studying the tradeoff between train-time and test-time compute using MCTS on the board game Hex.

**[19]** L. Kocsis and C. Szepesvari. Bandit based monte-carlo planning. In *European conference on machine learning*, pages 282-293. Springer, 2006.
- Cited in 10_appendix-a-related-work.md as RL literature methods (MCTS) for navigating the tradeoff between test-time and training-time compute.

**[20]** A. Lewkowycz, A. Andreassen, D. Dohan, E. Dyer, H. Michalewski, V. Ramasesh, A. Slone, C. Anil, I. Schlag, T. Gutman-Solo, Y. Wu, B. Neyshabur, G. Gur-Ari, and V. Misra. Solving quantitative reasoning problems with language models, 2022.
- Cited in 10_appendix-a-related-work.md as work showing improved LLM performance on mathematical reasoning tasks.

**[25]** OpenAI. GPT-4 technical report, 2024.
- Cited in 10_appendix-a-related-work.md as work showing improved LLM performance on mathematical reasoning tasks.

**[26]** Y. Qin, S. Liang, Y. Ye, K. Zhu, L. Yan, Y. Lu, Y. Lin, X. Cong, X. Tang, B. Qian, S. Zhao, L. Hong, R. Tian, R. Xie, J. Zhou, M. Gerstein, D. Li, Z. Liu, and M. Sun. Toolllm: Facilitating large language models to master 16000+ real-world apis, 2023. URL https://arxiv.org/abs/2307.16789.
- Cited in 10_appendix-a-related-work.md as an example of augmenting LMs with reasoning tools at test-time.

**[27]** C. Qu, S. Dai, X. Wei, H. Cai, S. Wang, D. Yin, J. Xu, and J.-R. Wen. Tool learning with large language models: A survey, 2024. URL https://arxiv.org/abs/2405.17935.
- Cited in 10_appendix-a-related-work.md as an example of augmenting LMs with reasoning tools at test-time.

**[32]** Z. Shao, P. Wang, Q. Zhu, R. Xu, J. Song, X. Bi, H. Zhang, M. Zhang, Y. K. Li, Y. Wu, and D. Guo. Deepseekmath: Pushing the limits of mathematical reasoning in open language models, 2024.
- Cited in 10_appendix-a-related-work.md as work showing improved LLM performance on mathematical reasoning tasks and improving proposal distribution via targeted RL finetuning.

**[39]** G. Team. Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context, 2024.
- Cited in 10_appendix-a-related-work.md as work showing improved LLM performance on mathematical reasoning tasks.

**[40]** Y. Tian, B. Peng, L. Song, L. Jin, D. Yu, H. Mi, and D. Yu. Toward self-improvement of llms via imagination, searching, and criticizing, 2024.
- Cited in 10_appendix-a-related-work.md as work on enabling LLMs to benefit from additional test-time computation by finetuning verifiers.

**[44]** P. Villalobos and D. Atkinson. Trading off compute in training and inference, 2023. URL https://epochai.org/blog/trading-off-compute-in-training-and-inference. Accessed: 2024-07-03.
- Cited in 10_appendix-a-related-work.md as survey work analyzing the tradeoff between training and inference across multiple domains.

**[46]** R. Wang, E. Zelikman, G. Poesia, Y. Pu, N. Haber, and N. D. Goodman. Hypothesis search: Inductive reasoning with language models, 2024. URL https://arxiv.org/abs/2309.05660.
- Cited in 10_appendix-a-related-work.md as work conducting hierarchical hypothesis search to enable inductive reasoning capabilities.

**[49]** Z. Yuan, H. Yuan, C. Li, G. Dong, K. Lu, C. Tan, C. Zhou, and J. Zhou. Scaling relationship on learning mathematical reasoning with large language models, 2023.
- Cited in 10_appendix-a-related-work.md as work improving proposal distribution via targeted RL finetuning.

**[50]** E. Zelikman, Y. Wu, J. Mu, and N. D. Goodman. Star: Bootstrapping reasoning with reasoning, 2022.
- Cited in 02_unified-perspective.md as RL-inspired finetuning methods (STaR) for improving the proposal distribution. Also cited in 10_appendix-a-related-work.md as work improving proposal distribution via targeted RL finetuning.

**[51]** E. Zelikman, G. Harik, Y. Shao, V. Jayasiri, N. Haber, and N. D. Goodman. Quiet-star: Language models can teach themselves to think before speaking, 2024. URL https://arxiv.org/abs/2403.09629.
- Cited in 10_appendix-a-related-work.md as work on learning thought tokens in an unsupervised manner.
