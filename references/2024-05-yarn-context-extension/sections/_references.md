# References

Only references cited in the section notes are included below.

[1] Mistrallite. URL https://huggingface.co/amazon/MistralLite.
- Cited in 08_appendix-b.md as a baseline NTK-aware ($\theta = 1$M) Mistral model.

[2] Introducing Qwen-7B: Open foundation and human-aligned models (of the state-of-the-arts). URL https://github.com/QwenLM/Qwen-7B/blob/main/tech_memo.md.
- Cited in 01_introduction.md as an example of a model using "Dynamic NTK" interpolation.

[3] Long-data collections. URL https://huggingface.co/datasets/togethercomputer/Long-Data-Collections.
- Cited in 08_appendix-b.md as training data for Mistral YaRN models.

[4] Z. Azerbayev, E. Ayers, and B. Piotrowski. Proof-pile, 2022. URL https://github.com/zhangir-azerbayev/proof-pile.
- Cited in 04_experiments.md as an evaluation dataset for long sequence language modeling.

[5] S. Black, S. Biderman, E. Hallahan, Q. Anthony, L. Gao, L. Golding, H. He, C. Leahy, K. McDonell, J. Phang, M. Pieler, U. S. Prashanth, S. Purohit, L. Reynolds, J. Tow, B. Wang, and S. Weinbach. GPT-NeoX-20B: An open-source autoregressive language model, 2022. arXiv: 2204.06745.
- Cited in 01_introduction.md as a model family using RoPE.

[6] bloc97. NTK-Aware Scaled RoPE allows LLaMA models to have extended (8k+) context size without any fine-tuning and minimal perplexity degradation., 2023. URL https://www.reddit.com/r/LocalLLaMA/comments/14lz7j5/ntkaware_scaled_rope_allows_llama_models_to_have/.
- Cited in 01_introduction.md, 03_methodology.md as the origin of "NTK-aware" interpolation.

[7] bloc97. Add NTK-Aware interpolation "by parts" correction, 2023. URL https://github.com/jquesnelle/scaled-rope/pull/1.
- Cited in 01_introduction.md, 03_methodology.md as the "NTK-by-parts" interpolation method.

[8] C. Chen. Transformer Inference Arithmetic, 2022. URL https://kipp.ly/blog/transformer-inference-arithmetic/.
- Cited in 03_methodology.md regarding kv-caching for Dynamic Scaling.

[9] S. Chen, S. Wong, L. Chen, and Y. Tian. Extending context window of large language models via positional interpolation, 2023. arXiv: 2306.15595.
- Cited in 01_introduction.md, 02_background-and-related-work.md, 03_methodology.md, 04_experiments.md as the Position Interpolation (PI) method.

[10] A. Chowdhery, S. Narang, J. Devlin, M. Bosma, G. Mishra, A. Roberts, P. Barham, H. W. Chung, C. Sutton, S. Gehrmann, P. Schuh, K. Shi, S. Tsvyashchenko, J. Maynez, A. Rao, P. Barnes, Y. Tay, N. Shazeer, V. Prabhakaran, E. Reif, N. Du, B. Hutchinson, R. Pope, J. Bradbury, J. Austin, M. Isard, G. Gur-Ari, P. Yin, T. Duke, A. Levskaya, S. Ghemawat, S. Dev, H. Michalewski, X. Garcia, V. Misra, K. Robinson, L. Fedus, D. Zhou, D. Ippolito, D. Luan, H. Lim, B. Zoph, A. Spiridonov, R. Sepassi, D. Dohan, S. Agrawal, M. Omernick, A. M. Dai, T. S. Pillai, M. Pellat, A. Lewkowycz, E. Moreira, R. Child, O. Polozov, K. Lee, Z. Zhou, X. Wang, B. Saeta, M. Diaz, O. Firat, M. Catasta, J. Wei, K. Meier-Hellstern, D. Eck, J. Dean, S. Petrov, and N. Fiedel. PaLM: Scaling language modeling with pathways, 2022. arXiv: 2204.02311.
- Cited in 01_introduction.md as a model family using RoPE.

[11] P. Clark, I. Cowhey, O. Etzioni, T. Khot, A. Sabharwal, C. Schoenick, and O. Tafjord. Think you have solved question answering? try ARC, the AI2 Reasoning Challenge, 2018. arXiv: 1803.05457.
- Cited in 04_experiments.md as one of the standardized benchmarks (25-shot ARC-Challenge).

[12] T. Computer. Redpajama: An open source recipe to reproduce llama training dataset, 2023. URL https://github.com/togethercomputer/RedPajama-Data.
- Cited in 04_experiments.md (footnote 5) as the dataset used to train LLongMA-2; cited in 07_appendix-a.md as the dataset used for pre-softmax scaling experiments.

[13] T. Dao. Flashattention-2: Faster attention with better parallelism and work partitioning, 2023. arXiv: 2307.08691.
- Cited in 02_background-and-related-work.md, 03_methodology.md, 04_experiments.md as Flash Attention 2, used in training and noted for compatibility with YaRN.

[14] emozilla. Dynamically Scaled RoPE further increases performance of long context LLaMA with zero fine-tuning, 2023. URL https://www.reddit.com/r/LocalLLaMA/comments/14mrgpr/dynamically_scaled_rope_further_increases/.
- Cited in 01_introduction.md, 03_methodology.md as the "Dynamic NTK" interpolation method first appearing as a reddit post.

[15] J. Gehring, M. Auli, D. Grangier, D. Yarats, and Y. N. Dauphin. Convolutional sequence to sequence learning, 2017. arXiv: 1705.03122.
- Cited in 01_introduction.md as an improvement to the original sinusoidal position encoding (learnable absolute position encoding).

[16] C. Han, Q. Wang, W. Xiong, Y. Chen, H. Ji, and S. Wang. LM-Infinite: Simple on-the-fly length generalization for large language models, 2023. arXiv: 2308.16137.
- Cited in 02_background-and-related-work.md as a concurrent work proposing similar ideas to YaRN for on-the-fly length generalization.

[17] D. Hendrycks, C. Burns, S. Basart, A. Zou, M. Mazeika, D. Song, and J. Steinhardt. Measuring massive multitask language understanding. *Proceedings of the International Conference on Learning Representations (ICLR)*, 2021.
- Cited in 04_experiments.md as one of the standardized benchmarks (5-shot MMLU).

[18] L. Huang, S. Cao, N. Parulian, H. Ji, and L. Wang. Efficient attentions for long document summarization. In *Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies*, pages 1419-1436. Association for Computational Linguistics, June 2021.
- Cited in 04_experiments.md as the GovReport evaluation dataset for long sequence language modeling.

[19] Hugging Face. Open LLM Leaderboard, 2023. URL https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard.
- Cited in 04_experiments.md as the standardized benchmark suite used for evaluation.

[20] A. Q. Jiang, A. Sablayrolles, A. Mensch, C. Bamford, D. S. Chaplot, D. de las Casas, F. Bressand, G. Lengyel, G. Lample, L. Saulnier, L. R. Lavaud, M.-A. Lachaux, P. Stock, T. L. Scao, T. Lavril, T. Wang, T. Lacroix, and W. E. Sayed. Mistral 7b, 2023.
- Cited in 08_appendix-b.md as the Mistral 7B v0.1 base model extended with YaRN.

[21] kaiokendev. Things I'm learning while training superhot., 2023. URL https://kaiokendev.github.io/til#extending-context-to-8k.
- Cited in 01_introduction.md, 02_background-and-related-work.md as the concurrent proposal of Position Interpolation.

[22] A. Kazemnejad, I. Padhi, K. N. Ramamurthy, P. Das, and S. Reddy. The impact of positional encoding on length generalization in transformers, 2023. arXiv: 2305.19466.
- Cited in 01_introduction.md regarding inability of positional encodings to generalize past training context.

[23] S. Lin, J. Hilton, and O. Evans. TruthfulQA: Measuring how models mimic human falsehoods. In *Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 3214-3252, May 2022.
- Cited in 04_experiments.md as one of the standardized benchmarks (0-shot TruthfulQA).

[24] I. Loshchilov and F. Hutter. Decoupled weight decay regularization. In *International Conference on Learning Representations*, 2019.
- Cited in 04_experiments.md as the AdamW optimizer used for training.

[25] A. Mohtashami and M. Jaggi. Landmark attention: Random-access infinite context length for transformers, 2023. arXiv: 2305.16300.
- Cited in 04_experiments.md as the definition of the passkey retrieval evaluation task.

[26] A. Paszke, S. Gross, F. Massa, A. Lerer, J. Bradbury, G. Chanan, T. Killeen, Z. Lin, N. Gimelshein, L. Antiga, A. Desmaison, A. Kopf, E. Yang, Z. DeVito, M. Raison, A. Tejani, S. Chilamkurthy, B. Steiner, L. Fang, J. Bai, and S. Chintala. PyTorch: An imperative style, high-performance deep learning library. In *NeurIPS*, pages 8024-8035, 2019.
- Cited in 04_experiments.md as the framework used for training.

[27] O. Press, N. Smith, and M. Lewis. Train Short, Test Long: Attention with linear biases enables input length extrapolation. In *International Conference on Learning Representations*, 2022.
- Cited in 01_introduction.md as ALiBi positional encoding; cited in 04_experiments.md for the sliding window perplexity evaluation method with $S = 256$.

[28] J. Quesnelle, E. Shippole, and "Kaiokendev". Llongma: Scaling rotary embeddings through linear positional interpolation. https://huggingface.co/conceptofmind/LLongMA-2-7b/, 2023.
- Cited in 04_experiments.md (footnote 5) as the PI-based Llama-2 7b fine-tuned model (LLongMA-2).

[29] J. W. Rae, A. Potapenko, S. M. Jayakumar, C. Hillier, and T. P. Lillicrap. Compressive transformers for long-range sequence modelling. In *International Conference on Learning Representations*, 2020.
- Cited in 04_experiments.md, 06_reproducibility.md as the PG19 training dataset.

[30] A. Roberts, C. Raffel, C. Lee, M. Matena, N. Shazeer, P. J. Liu, S. Narang, W. Li, and Y. Zhou. Exploring the limits of transfer learning with a unified text-to-text transformer. Technical report, Google, 2019.
- Cited in 01_introduction.md as T5 Relative Bias positional encoding method.

[31] B. Roziere, J. Gehring, F. Gloeckle, S. Sootla, I. Gat, X. E. Tan, Y. Adi, J. Liu, T. Remez, J. Rapin, A. Kozhevnikov, I. Evtimov, J. Bitton, M. Bhatt, C. C. Ferrer, A. Grattafiori, W. Xiong, A. Defossez, J. Copet, F. Azhar, H. Touvron, L. Martin, N. Usunier, T. Scialom, and G. Synnaeve. Code Llama: Open foundation models for code, 2023. arXiv: 2308.12950.
- Cited in 01_introduction.md, 03_methodology.md, 04_experiments.md as Code Llama using "NTK-aware" scaling and as a baseline for comparison.

[32] P. Shaw, J. Uszkoreit, and A. Vaswani. Self-attention with relative position representations. In *Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 2 (Short Papers)*, pages 464-468, New Orleans, Louisiana, June 2018. Association for Computational Linguistics.
- Cited in 01_introduction.md regarding relative positional encoding schemes.

[33] J. Su. Rectified rotary position embeddings. https://github.com/bojone/rerope, 2023.
- Cited in 02_background-and-related-work.md as a related work aiming to extend context size with RoPE (ReRoPE).

[34] J. Su, Y. Lu, S. Pan, A. Murtadha, B. Wen, and Y. Liu. RoFormer: Enhanced transformer with rotary position embedding, 2022. arXiv: 2104.09864.
- Cited in 01_introduction.md, 02_background-and-related-work.md as the original Rotary Position Embedding paper.

[35] Y. Sun, L. Dong, B. Patra, S. Ma, S. Huang, A. Benhaim, V. Chaudhary, X. Song, and F. Wei. A length-extrapolatable transformer, 2022. arXiv: 2212.10554.
- Cited in 01_introduction.md as XPos, a relative positional encoding method.

[36] M. Tancik, P. P. Srinivasan, B. Mildenhall, S. Fridovich-Keil, N. Raghavan, U. Singhal, R. Ramamoorthi, J. T. Barron, and R. Ng. Fourier features let networks learn high frequency functions in low dimensional domains. In *Proceedings of the 34th International Conference on Neural Information Processing Systems*, NIPS'20, Red Hook, NY, USA, 2020. Curran Associates Inc. ISBN 9781713829546.
- Cited in 03_methodology.md regarding NTK theory and the relationship between RoPE and Fourier Features.

[37] Together.ai. LLaMA-2-7B-32K, 2023. URL https://huggingface.co/togethercomputer/LLaMA-2-7B-32K.
- Cited in 04_experiments.md as a baseline model (Together LLaMA-2-7B-32K).

[38] H. Touvron, T. Lavril, G. Izacard, X. Martinet, M.-A. Lachaux, T. Lacroix, B. Roziere, N. Goyal, E. Hambro, F. Azhar, A. Rodriguez, A. Joulin, E. Grave, and G. Lample. LLaMA: Open and efficient foundation language models, 2023. arXiv: 2302.13971.
- Cited in 01_introduction.md as a model family using RoPE.

[39] H. Touvron, L. Martin, K. Stone, P. Albert, A. Almahairi, Y. Babaei, N. Bashlykov, S. Batra, P. Bhargava, S. Bhosale, D. Bikel, L. Blecher, C. C. Ferrer, M. Chen, G. Cucurull, D. Esiobu, J. Fernandes, J. Fu, W. Fu, B. Fuller, C. Gao, V. Goswami, N. Goyal, A. Hartshorn, S. Hosseini, R. Hou, H. Inan, M. Kardas, V. Kerkez, M. Khabsa, I. Kloumann, A. Korenev, P. S. Koura, M.-A. Lachaux, T. Lavril, J. Lee, D. Liskovich, Y. Lu, Y. Mao, X. Martinet, T. Mihaylov, P. Mishra, I. Molybog, Y. Nie, A. Poulton, J. Reizenstein, R. Rungta, K. Saladi, A. Schelten, R. Silva, E. M. Smith, R. Subramanian, X. E. Tan, B. Tang, R. Taylor, A. Williams, J. X. Kuan, P. Xu, Z. Yan, I. Zarov, Y. Zhang, A. Fan, M. Kambadur, S. Narang, A. Rodriguez, R. Stojnic, S. Edunov, and T. Scialom. Llama 2: Open foundation and fine-tuned chat models, 2023.
- Cited in 04_experiments.md as the base model used for fine-tuning.

[40] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, L. Kaiser, and I. Polosukhin. Attention is all you need. In *Advances in Neural Information Processing Systems*, volume 30. Curran Associates, Inc., 2017.
- Cited in 01_introduction.md as the foundation for transformer-based LLMs.

[41] R. Zellers, A. Holtzman, Y. Bisk, A. Farhadi, and Y. Choi. HellaSwag: Can a machine really finish your sentence? In *Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics*, 2019.
- Cited in 04_experiments.md as one of the standardized benchmarks (10-shot HellaSwag).

[42] Y. Zhao, A. Gu, R. Varma, L. Luo, C.-C. Huang, M. Xu, L. Wright, H. Shojanazeri, M. Ott, S. Shleifer, A. Desmaison, C. Balioglu, B. Nguyen, G. Chauhan, Y. Hao, and S. Li. PyTorch FSDP: Experiences on scaling fully sharded data parallel, 2023. arXiv: 2304.11277.
- Cited in 04_experiments.md as the distributed training strategy used (Fully Sharded Data Parallelism).
