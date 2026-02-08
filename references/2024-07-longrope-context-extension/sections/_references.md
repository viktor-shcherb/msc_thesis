# References

Only references actually cited in the section notes are listed below.

## (mis, 2024)
Long-data collections, 2024. URL https://huggingface.co/datasets/togethercomputer/RedPajama-Data-1T.
- Cited in 04_experiments.md as the Mistral fine-tuning dataset (Together Computer's Long-Data Collections)

## (Amazon, 2023)
Amazon. Mistrallite, 2023. URL https://huggingface.co/amazon/MistralLite.
- Cited in 04_experiments.md (Table 8b) as MistralLite baseline

## (Azerbayev et al., 2022)
Azerbayev, Z., Ayers, E., and Piotrowski, B. Proof-pile, 2022. URL https://github.com/zhangir-azerbayev/ProofNet.
- Cited in 02_non-uniformity-in-positional-interpolation.md as the Proof-pile dataset

## (Borgeaud et al., 2022)
Borgeaud, S., Mensch, A., Hoffmann, J., Cai, T., Rutherford, E., Millican, K., Van Den Driessche, G. B., Lespiau, J.-B., Damoc, B., Clark, A., et al. Improving language models by retrieving from trillions of tokens. In *International conference on machine learning*, pp. 2206-2240. PMLR, 2022.
- Cited in 05_related-works.md as a retrieval-based approach for long context

## (Chen et al., 2023a)
Chen, S., Wong, S., Chen, L., and Tian, Y. Extending context window of large language models via positional interpolation. *arXiv preprint arXiv:2306.15595*, 2023a.
- Cited in 01_introduction.md as PI (Position Interpolation), a key prior method
- Cited in 02_non-uniformity-in-positional-interpolation.md for PI definition and comparison
- Cited in 03_longrope.md as a known issue of positional interpolation (shorter context window recovery)
- Cited in 07_appendix.md as a passkey retrieval format source

## (Chen et al., 2023b)
Chen, Y., Qian, S., Tang, H., Lai, X., Liu, Z., Han, S., and Jia, J. Longlora: Efficient fine-tuning of long-context large language models. *arXiv:2309.12307*, 2023b.
- Cited in 01_introduction.md as a recent long-context extension method
- Cited in 04_experiments.md as the LongLoRA baseline
- Cited in 05_related-works.md as an efficient fine-tuning approach
- Cited in 07_appendix.md as a passkey retrieval format source

## (Clark et al., 2018)
Clark, P., Cowhey, I., Etzioni, O., Khot, T., Sabharwal, A., Schoenick, C., and Tafjord, O. Think you have solved question answering? try arc, the ai2 reasoning challenge. *arXiv:1803.05457v1*, 2018.
- Cited in 04_experiments.md as the ARC-Challenge benchmark (25-shot)

## (Computer, 2023)
Computer, T. Redpajama: An open source recipe to reproduce llama training dataset, 2023. URL https://github.com/togethercomputer/RedPajama-Data.
- Cited in 04_experiments.md as the LLaMA2 fine-tuning dataset

## (Dao, 2023)
Dao, T. FlashAttention-2: Faster attention with better parallelism and work partitioning. 2023.
- Cited in 07_appendix.md as Flash Attention-2, used to accelerate training and inference

## (Gao et al., 2020)
Gao, L., Biderman, S., Black, S., Golding, L., Hoppe, T., Foster, C., Phang, J., He, H., Thite, A., Nabeshima, N., Presser, S., and Leahy, C. The Pile: An 800gb dataset of diverse text for language modeling. *arXiv preprint arXiv:2101.00027*, 2020.
- Cited in 04_experiments.md as the source of PG19, Books3, and Pile-Books3 datasets
- Cited in 02_non-uniformity-in-positional-interpolation.md (PG19 validation set for search)

## (Guo et al., 2020)
Guo, Z., Zhang, X., Mu, H., Heng, W., Liu, Z., Wei, Y., and Sun, J. Single path one-shot neural architecture search with uniform sampling. In *Computer Vision--ECCV 2020*, pp. 544-560. Springer, 2020.
- Cited in 03_longrope.md as the evolution search method used

## (Han et al., 2023)
Han, C., Wang, Q., Xiong, W., Chen, Y., Ji, H., and Wang, S. Lm-infinite: Simple on-the-fly length generalization for large language models. *arXiv preprint arXiv:2308.16137*, 2023.
- Cited in 02_non-uniformity-in-positional-interpolation.md as evidence for initial tokens receiving large attention scores
- Cited in 05_related-works.md as an attention-based context extension approach

## (Hendrycks et al., 2020)
Hendrycks, D., Burns, C., Basart, S., Zou, A., Mazeika, M., Song, D., and Steinhardt, J. Measuring massive multitask language understanding. *arXiv preprint arXiv:2009.03300*, 2020.
- Cited in 04_experiments.md as the MMLU benchmark (5-shot)

## (Huang et al., 2023)
Huang, X., Zhang, L. L., Cheng, K.-T., Yang, F., and Yang, M. Fewer is more: Boosting llm reasoning with reinforced context pruning. 2023. URL https://api.semanticscholar.org/CorpusID:266210460.
- Cited in 01_introduction.md as a scenario requiring long context (in-context learning)

## (Jacot et al., 2018)
Jacot, A., Gabriel, F., and Hongler, C. Neural tangent kernel: Convergence and generalization in neural networks. *Advances in neural information processing systems*, 31, 2018.
- Cited in 02_non-uniformity-in-positional-interpolation.md as theoretical basis for NTK-based interpolation
- Cited in 03_longrope.md as basis for the monotonically non-decreasing constraint

## (Jiang et al., 2023)
Jiang, A. Q., Sablayrolles, A., Mensch, A., Bamford, C., Chaplot, D. S., de las Casas, D., Bressand, F., Lengyel, G., Lample, G., Saulnier, L., Lavaud, L. R., Lachaux, M.-A., Stock, P., Scao, T. L., Lavril, T., Wang, T., Lacroix, T., and Sayed, W. E. Mistral 7b, 2023.
- Cited in 01_introduction.md as the Mistral model used in progressive extension

## (Lin et al., 2021)
Lin, S., Hilton, J., and Evans, O. Truthfulqa: Measuring how models mimic human falsehoods. *arXiv preprint arXiv:2109.07958*, 2021.
- Cited in 04_experiments.md as the TruthfulQA benchmark (0-shot)

## (Lin et al., 2023)
Lin, Z., Miao, Y., Liu, G., Shi, X., Zhang, Q., Yang, F., Maleki, S., Zhu, Y., Cao, X., Li, C., et al. Superscaler: Supporting flexible dnn parallelization via a unified abstraction. *arXiv preprint arXiv:2301.08984*, 2023.
- Cited in 04_experiments.md as the distributed training system used for 128k context
- Cited in 07_appendix.md as CUBE, the internal platform for reducing training/inference costs beyond 512k

## (Liu et al., 2023)
Liu, X., Yan, H., Zhang, S., An, C., Qiu, X., and Lin, D. Scaling laws of rope-based extrapolation. *arXiv preprint arXiv:2310.05209*, 2023.
- Cited in 01_introduction.md as a recent long-context extension method
- Cited in 05_related-works.md as ScaledRoPE approach

## (LocalLLaMA, 2023a)
LocalLLaMA. Dynamically scaled rope further increases performance of long context llama with zero fine-tuning, 2023a. URL https://www.reddit.com/r/LocalLLaMA/comments/14mrgpr/dynamically_scaled_rope_further_increases/.
- Cited in 01_introduction.md as Dynamic NTK
- Cited in 02_non-uniformity-in-positional-interpolation.md for NTK-based interpolation description

## (LocalLLaMA, 2023b)
LocalLLaMA. Ntk-aware scaled rope allows llama models to have extended (8k+) context size without any fine-tuning and minimal perplexity degration, 2023b. URL https://www.reddit.com/r/LocalLLaMA/comments/14lz7j5/ntkaware_scaled_rope_allows_llama_models_to_have/.
- Cited in 01_introduction.md as NTK
- Cited in 02_non-uniformity-in-positional-interpolation.md for NTK-based interpolation description
- Cited in 03_longrope.md as basis for monotonicity constraint (NTK theory)

## (Madaan et al., 2023)
Madaan, A., Tandon, N., Gupta, P., Hallinan, S., Gao, L., Wiegreffe, S., Alon, U., Dziri, N., Prabhumoye, S., Yang, Y., Gupta, S., Majumder, B. P., Hermann, K., Welleck, S., Yazdanbakhsh, A., and Clark, P. Self-refine: Iterative refinement with self-feedback, 2023.
- Cited in 01_introduction.md as an LLM agent scenario requiring long context

## (Mohtashami & Jaggi, 2023)
Mohtashami, A. and Jaggi, M. Landmark attention: Random-access infinite context length for transformers. *arXiv preprint arXiv:2305.16300*, 2023.
- Cited in 04_experiments.md as the source of the passkey retrieval evaluation task
- Cited in 07_appendix.md as a passkey retrieval format source

## (OpenAI et al., 2023)
OpenAI, et al. Gpt-4 technical report, 2023.
- Cited in 01_introduction.md as example of successful LLMs

## (Park et al., 2023)
Park, J. S., O'Brien, J., Cai, C. J., Morris, M. R., Liang, P., and Bernstein, M. S. Generative agents: Interactive simulacra of human behavior. In *Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology*, pp. 1-22, 2023.
- Cited in 01_introduction.md as an LLM agent scenario requiring long context

## (Peng et al., 2023)
Peng, B., Quesnelle, J., Fan, H., and Shippole, E. Yarn: Efficient context window extension of large language models. *arXiv preprint arXiv:2309.00071*, 2023.
- Cited in 01_introduction.md as YaRN, a key prior method
- Cited in 02_non-uniformity-in-positional-interpolation.md for YaRN definition and comparison
- Cited in 04_experiments.md as YaRN baseline and for Mistral fine-tuning settings
- Cited in 07_appendix.md as a passkey retrieval format source

## (Rae et al., 2019)
Rae, J. W., Potapenko, A., Jayakumar, S. M., Hillier, C., and Lillicrap, T. P. Compressive transformers for long-range sequence modelling. *arXiv preprint*, 2019. https://arxiv.org/abs/1911.05507.
- Cited in 04_experiments.md as the Proof-pile dataset source
- Cited in 02_non-uniformity-in-positional-interpolation.md (PG19 validation set)

## (Ratner et al., 2022)
Ratner, N., Levine, Y., Belinkov, Y., Ram, O., Abend, O., Karpas, E., Shashua, A., Leyton-Brown, K., and Shoham, Y. Parallel context windows improve in-context learning of large language models. *arXiv preprint arXiv:2212.10947*, 2022.
- Cited in 05_related-works.md as an attention-based context extension approach

## (Roziere et al., 2023)
Roziere, B., Gehring, J., Gloeckle, F., Sootla, S., Gat, I., Tan, X. E., Adi, Y., Liu, J., Remez, T., Rapin, J., et al. Code llama: Open foundation models for code, 2023.
- Cited in 04_experiments.md as the Code LLaMA baseline
- Cited in 05_related-works.md as a fine-tuning based approach

## (Su et al., 2021)
Su, J., Lu, Y., Pan, S., Murtadha, A., Wen, B., and Liu, Y. Roformer: Enhanced transformer with rotary position embedding. *arXiv preprint arXiv:2104.09864*, 2021.
- Cited in 01_introduction.md as the original RoPE paper
- Cited in 02_non-uniformity-in-positional-interpolation.md for the RoPE definition

## (Tancik et al., 2020)
Tancik, M., Srinivasan, P., Mildenhall, B., Fridovich-Keil, S., Raghavan, N., Singhal, U., Ramamoorthi, R., Barron, J., and Ng, R. Fourier features let networks learn high frequency functions in low dimensional domains. *Advances in Neural Information Processing Systems*, 33: 7537-7547, 2020.
- Cited in 02_non-uniformity-in-positional-interpolation.md as theoretical basis for NTK interpretation
- Cited in 03_longrope.md as basis for monotonicity constraint

## (Together, 2023)
Together. URL https://huggingface.co/togethercomputer/LLaMA-2-7B-32K, 2023.
- Cited in 04_experiments.md as the Together-32k baseline

## (Touvron et al., 2023)
Touvron, H., Martin, L., Stone, K., Albert, P., Almahairi, A., et al. Llama 2: Open foundation and fine-tuned chat models, 2023.
- Cited in 01_introduction.md as the LLaMA2 model with 4096 context limit

## (Tworkowski et al., 2023)
Tworkowski, S., Staniszewski, K., Pacek, M., Wu, Y., Michalewski, H., and Milos, P. Focused transformer: Contrastive training for context scaling. 2023.
- Cited in 05_related-works.md as a retrieval-based approach

## (Wang et al., 2023)
Wang, W., Dong, L., Cheng, H., Liu, X., Yan, X., Gao, J., and Wei, F. Augmenting language models with long-term memory. *arXiv preprint arXiv:2306.07174*, 2023.
- Cited in 05_related-works.md as a retrieval-based approach

## (Xiao et al., 2023)
Xiao, G., Tian, Y., Chen, B., Han, S., and Lewis, M. Efficient streaming language models with attention sinks. *arXiv*, 2023.
- Cited in 02_non-uniformity-in-positional-interpolation.md as Streaming LLM (evidence for initial tokens receiving large attention scores)
- Cited in 05_related-works.md as an attention-based context extension approach

## (Xiong et al., 2023)
Xiong, W., Liu, J., Molybog, I., Zhang, H., Bhargava, P., Hou, R., Martin, L., Rungta, R., Sankararaman, K. A., Oguz, B., et al. Effective long-context scaling of foundation models, 2023.
- Cited in 05_related-works.md as LLaMA2 Long, a fine-tuning based approach

## (Zellers et al., 2019)
Zellers, R., Holtzman, A., Bisk, Y., Farhadi, A., and Choi, Y. Hellaswag: Can a machine really finish your sentence? In *Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics*, 2019.
- Cited in 04_experiments.md as the HellaSwag benchmark (10-shot)

## (Zhang et al., 2024)
Zhang, P., Liu, Z., Xiao, S., Shao, N., Ye, Q., and Dou, Z. Soaring from 4k to 400k: Extending llm's context with activation beacon. *arXiv preprint arXiv:2401.03462*, 2024.
- Cited in 01_introduction.md as a recent long-context extension method

## (Zhu et al., 2023)
Zhu, D., Yang, N., Wang, L., Song, Y., Wu, W., Wei, F., and Li, S. Pose: Efficient context window extension of llms via positional skip-wise training, 2023.
- Cited in 05_related-works.md as PoSE, an efficient fine-tuning approach
- Cited in 07_appendix.md as a passkey retrieval format source

## (Face, 2024)
Face, H. Open llm leaderboard, 2024. URL https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard.
- Cited in 04_experiments.md as the evaluation platform for standard benchmarks

