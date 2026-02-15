# References

Only references cited in the section notes are included below.

## A

- **Agarwal et al., 2024** — Rishabh Agarwal, Avi Singh, Lei M Zhang, Bernd Bohnet, Stephanie Chan, Ankesh Anand, Zaheer Abbas, Azade Nova, John D Co-Reyes, Eric Chu, et al. "Many-shot in-context learning." *arXiv preprint arXiv:2404.11018*, 2024.
  - Cited in 02_related-work.md as an example of many-shot in-context learning research for long contexts.

- **Abdin et al., 2024** — Marah Abdin, Sam Ade Jacobs, et al. "Phi-3 technical report: A highly capable language model locally on your phone." *arXiv preprint arXiv:2404.14219*, 2024.
  - Cited in 09_appendix-a-models.md as the Phi3-medium model.

- **AI21, 2024** — AI21. "Introducing jamba: Ai21's groundbreaking ssm-transformer model." 2024. URL https://www.ai21.com/blog/announcing-jamba.
  - Cited in 01_introduction.md as a prior work using synthetic tasks (passkey retrieval, NIAH) for evaluating long-context LMs. Cited in 09_appendix-a-models.md for Jamba-base model.

- **An et al., 2024** — Chenxin An, Shansan Gong, Ming Zhong, Mukai Li, Jun Zhang, Lingpeng Kong, and Xipeng Qiu. "L-eval: Instituting standardized evaluation for long context language models." In *ICLR*, 2024.
  - Cited in 02_related-work.md as the L-Eval benchmark using realistic data filtered manually to ensure quality.

- **Anthropic, 2023** — Anthropic. "Long context prompting for Claude 2.1." *Blog*, 2023. URL https://www.anthropic.com/index/claude-2-1-prompting.
  - Cited in 03_ruler-benchmark.md as a prior work using needle-in-a-haystack to evaluate long-context LMs.

- **Anthropic, 2024** — Anthropic. "Introducing the next generation of claude." 2024. URL https://www.anthropic.com/news/claude-3-family.
  - Cited in 01_introduction.md as a prior work using synthetic tasks for evaluating long-context LMs.

- **Arora et al., 2024** — Simran Arora, Sabri Eyuboglu, Aman Timalsina, Isys Johnson, Michael Poli, James Zou, Atri Rudra, and Christopher Re. "Zoology: Measuring and improving recall in efficient language models." In *ICLR*, 2024.
  - Cited in 03_ruler-benchmark.md for the multi-query associative recall task setup used in MQ-NIAH, and as having extensively studied associative recall.

## B

- **Bai et al., 2023** — Yushi Bai et al. "LongBench: A bilingual, multitask benchmark for long context understanding." *arXiv:2308.14508*, 2023.
  - Cited in 01_introduction.md and 02_related-work.md as the LongBench benchmark; cited in 01_introduction.md as a benchmark whose reliance on parametric knowledge RULER avoids.

- **Beck et al., 2024** — Maximilian Beck, Korbinian Poppel, Markus Spanring, Andreas Auer, Oleksandra Prudnikova, Michael Kopp, Gunter Klambauer, Johannes Brandstetter, and Sepp Hochreiter. "xLSTM: Extended long short-term memory." *arXiv preprint arXiv:2405.04517*, 2024.
  - Cited in 02_related-work.md as a novel architecture for long-context input.

- **Bertsch et al., 2024** — Amanda Bertsch, Maor Ivgi, Uri Alon, Jonathan Berant, Matthew R Gormley, and Graham Neubig. "In-context learning with long-context models: An in-depth exploration." *arXiv preprint arXiv:2405.00200*, 2024.
  - Cited in 02_related-work.md as an example of many-shot in-context learning research.

- **Bulatov et al., 2023** — Aydar Bulatov, Yuri Kuratov, and Mikhail S Burtsev. "Scaling Transformer to 1M tokens and beyond with RMT." *arXiv:2304.11062*, 2023.
  - Cited in 02_related-work.md as a recurrence-based method for caching previous context.

## C

- **Castillo et al., 2024** — David Castillo, Joseph Davidson, Finlay Gray, Jose Solorzano, and Marek Rosa. "Introducing GoodAI LTM benchmark." *Blog*, 2024. URL https://www.goodai.com/introducing-goodai-ltm-benchmark/.
  - Cited in 02_related-work.md as the LTM benchmark for evaluating long-term conversations.

- **Chen et al., 2023** — Shouyuan Chen, Sherman Wong, Liangjian Chen, and Yuandong Tian. "Extending context window of large language models via positional interpolation." In *ICLR*, 2023.
  - Cited in 01_introduction.md as enabling scaling up context length; cited in 02_related-work.md as a RoPE variant for length extrapolation.

- **Chen et al., 2024** — Yukang Chen, Shengju Qian, Haotian Tang, Xin Lai, Zhijian Liu, Song Han, and Jiaya Jia. "LongLoRA: Efficient fine-tuning of long-context large language models." In *ICLR*, 2024.
  - Cited in 02_related-work.md as shifted sparse attention for efficient context scaling.

- **Child et al., 2019** — Rewon Child, Scott Gray, Alec Radford, and Ilya Sutskever. "Generating long sequences with sparse Transformers." *arXiv:1904.10509*, 2019.
  - Cited in 02_related-work.md as an early sparse attention mechanism.

- **Cohere, 2024** — Cohere. "Command R+." 2024. URL https://docs.cohere.com/docs/command-r-plus#model-details.
  - Cited in 09_appendix-a-models.md as the Command-R-plus model.

## D

- **Databricks, 2024** — Databricks. "Introducing DBRX: A new state-of-the-art open LLM." 2024. URL https://www.databricks.com/blog/introducing-dbrx-new-state-of-the-art-open-llm.
  - Cited in 09_appendix-a-models.md as the DBRX model.

- **Dao et al., 2022** — Tri Dao, Daniel Y. Fu, Stefano Ermon, Atri Rudra, and Christopher Re. "FlashAttention: Fast and memory-efficient exact attention with IO-awareness." In *NeurIPS*, 2022.
  - Cited in 01_introduction.md and 02_related-work.md as a key engineering advancement enabling long-context scaling.

- **Dao, 2023** — Tri Dao. "FlashAttention-2: Faster attention with better parallelism and work partitioning." *arXiv:2307.08691*, 2023.
  - Cited in 02_related-work.md as Flash Attention v2 for reducing memory footprint.

- **Ding et al., 2023** — Jiayu Ding et al. "LongNet: Scaling Transformers to 1,000,000,000 tokens." *arXiv:2307.02486*, 2023.
  - Cited in 02_related-work.md as dilated attention for efficient context scaling.

- **Ding et al., 2024** — Yiran Ding et al. "LongRoPE: Extending LLM context window beyond 2 million tokens." *arXiv:2402.13753*, 2024.
  - Cited in 02_related-work.md as a RoPE variant for length extrapolation.

- **Dong et al., 2023** — Zican Dong, Tianyi Tang, Junyi Li, Wayne Xin Zhao, and Ji-Rong Wen. "Bamboo: A comprehensive benchmark for evaluating long text modeling capacities of large language models." *arXiv:2309.13345*, 2023.
  - Cited in 02_related-work.md as proposing to use documents posted online after a cutoff date to isolate parametric knowledge.

## F

- **Fu et al., 2023a** — Daniel Y. Fu, Tri Dao, Khaled K. Saab, Armin W. Thomas, Atri Rudra, and Christopher Re. "Hungry Hungry Hippos: Towards language modeling with state space models." In *ICLR*, 2023a.
  - Cited in 02_related-work.md as a novel architecture for long-context input.

- **Fu et al., 2023b** — Daniel Y. Fu et al. "Simple hardware-efficient long convolutions for sequence modeling." *ICML*, 2023b.
  - Cited in 02_related-work.md as a novel architecture for long-context input.

- **Fu et al., 2024** — Yao Fu et al. "Data engineering for scaling language models to 128k context." *arXiv:2402.10171*, 2024.
  - Cited in 01_introduction.md as an AI system engineering advancement enabling context length scaling.

## G

- **GLM et al., 2024** — Team GLM, Aohan Zeng, Bin Xu, et al. "ChatGLM: A family of large language models from glm-130b to glm-4 all tools." 2024.
  - Cited in 09_appendix-a-models.md as the GLM4 model.

- **Goldman et al., 2024** — Omer Goldman, Alon Jacovi, Aviv Slobodkin, Aviya Maimon, Ido Dagan, and Reut Tsarfaty. "Is it really long context if all you need is retrieval? towards genuinely difficult long context nlp." *arXiv preprint arXiv:2407.00402*, 2024.
  - Cited in 03_ruler-benchmark.md for comprehensive discussion on evaluation task design for long-context language models.

- **Graves et al., 2014** — Alex Graves, Greg Wayne, and Ivo Danihelka. "Neural Turing machines." *arXiv:1410.5401*, 2014.
  - Cited in 03_ruler-benchmark.md as having extensively studied associative recall tasks.

- **Gu et al., 2022** — Albert Gu, Karan Goel, and Christopher Re. "Efficiently modeling long sequences with structured state spaces." In *ICLR*, 2022.
  - Cited in 02_related-work.md as a novel architecture for long-context input.

- **Gu & Dao, 2023** — Albert Gu and Tri Dao. "Mamba: Linear-time sequence modeling with selective state spaces." *arXiv:2312.00752*, 2023.
  - Cited in 02_related-work.md and 06_model-analysis.md as the Mamba architecture; evaluated as non-Transformer baseline in Section 6.

## H

- **Han et al., 2023** — Chi Han, Qifan Wang, Wenhan Xiong, Yu Chen, Heng Ji, and Sinong Wang. "Lm-infinite: Simple on-the-fly length generalization for large language models." *arXiv:2308.16137*, 2023.
  - Cited in 02_related-work.md as an attention sinks method for efficient context scaling.

- **Hopfield, 1982** — John J. Hopfield. "Neural networks and physical systems with emergent collective computational abilities." *Proc of the National Academy of Sciences of the United States of America*, 79 8: 2554-8, 1982.
  - Cited in 03_ruler-benchmark.md as having extensively studied associative recall tasks.

## I

- **Ivgi et al., 2023** — Maor Ivgi, Uri Shaham, and Jonathan Berant. "Efficient long-text understanding with short-text models." *Transactions of the ACL*, 11:284-299, 2023.
  - Cited in 01_introduction.md and 03_ruler-benchmark.md as the real-world adaptation of NIAH for QA tasks.

## J

- **Jacobs et al., 2023** — Sam Ade Jacobs et al. "DeepSpeed Ulysses: System optimizations for enabling training of extreme long sequence Transformer models." *arXiv:2309.14509*, 2023.
  - Cited in 01_introduction.md as an AI system engineering advancement.

- **Jaszczur et al., 2021** — Sebastian Jaszczur et al. "Sparse is enough in scaling transformers." In *NeurIPS*, 2021.
  - Cited in 02_related-work.md as a sparse attention mechanism.

- **Jiang et al., 2023** — Huiqiang Jiang et al. "LongLLMLingua: Accelerating and enhancing LLMs in long context scenarios via prompt compression." *arXiv:2310.06839*, 2023.
  - Cited in 02_related-work.md as preserving salient information via compression.

- **Jiang et al., 2024** — Albert Q Jiang et al. "Mixtral of experts." *arXiv:2401.04088*, 2024.
  - Cited in 09_appendix-a-models.md as the Mixtral-8x22B and Mixtral-base models.

## K

- **Kamradt, 2023** — Gregory Kamradt. "Needle In A Haystack - pressure testing LLMs." *Github*, 2023. URL https://github.com/gkamradt/LLMTest_NeedleInAHaystack/tree/main.
  - Cited in 01_introduction.md, 02_related-work.md, 03_ruler-benchmark.md, and 08_limitations.md as the original NIAH test.

- **Karpinska et al., 2024** — Marzena Karpinska, Katherine Thai, Kyle Lo, Tanya Goyal, and Mohit Iyyer. "One thousand and one pairs: A 'novel' challenge for long-context language models." *arXiv preprint arXiv:2406.16264*, 2024.
  - Cited in 02_related-work.md and 08_limitations.md as the NoCHA benchmark emphasizing reasoning and instruction-following.

- **Karttunen, 1969** — Lauri Karttunen. "Discourse referents." In *COLING*, 1969.
  - Cited in 03_ruler-benchmark.md for establishing chains of references co-referring to the same entity.

- **Kingsley Zipf, 1932** — George Kingsley Zipf. *Selected studies of the principle of relative frequency in language.* Harvard university press, 1932.
  - Cited in 03_ruler-benchmark.md (footnote 4) as inspiration for the Zeta distribution used in FWE.

- **Kuratov et al., 2024** — Yuri Kuratov, Aydar Bulatov, Petr Anokhin, Ivan Rodkin, Dmitry Sorokin, Artyom Sorokin, and Mikhail Burtsev. "Babilong: Testing the limits of LLMs with long context reasoning-in-a-haystack." *arXiv:2406.10149*, 2024.
  - Cited in 02_related-work.md as investigating fact reasoning in long contexts.

- **Kwon et al., 2023** — Woosuk Kwon et al. "Efficient memory management for large language model serving with paged attention." In *Proc. of the ACM SIGOPS 29th Symposium on Operating Systems Principles*, 2023.
  - Cited in 04_experiments-results.md as vLLM, the LLM serving system used for inference.

## L

- **Lee et al., 2024** — Jinhyuk Lee, Anthony Chen, Zhuyun Dai, Dheeru Dua, Devendra Singh Sachan, Michael Boratko, Yi Luan, Sebastien MR Arnold, Vincent Perot, Siddharth Dalmia, et al. "Can long-context language models subsume retrieval, rag, sql, and more?" *arXiv preprint arXiv:2406.13121*, 2024.
  - Cited in 02_related-work.md as retrieval-based synthetic task research.

- **Levy et al., 2024** — Mosh Levy, Alon Jacoby, and Yoav Goldberg. "Same task, more tokens: the impact of input length on the reasoning performance of large language models." *arXiv preprint arXiv:2402.14848*, 2024.
  - Cited in 02_related-work.md and 08_limitations.md as FlenQA, demonstrating degrading performance when increasing task input length to a few thousand tokens.

- **Li et al., 2023a** — Dacheng Li, Rulin Shao, et al. "How long can open-source LLMs truly promise on context length?" 2023a. URL https://lmsys.org/blog/2023-06-29-longchat.
  - Cited in 02_related-work.md as retrieval-based synthetic task research. Cited in 09_appendix-a-models.md as the LongChat model.

- **Li et al., 2023b** — Jiaqi Li, Mengmeng Wang, Zilong Zheng, and Muhan Zhang. "Loogle: Can long-context language models understand long contexts?" *arXiv:2311.04939*, 2023b.
  - Cited in 02_related-work.md as proposing to use extremely low-resource materials to isolate parametric knowledge.

- **Liu et al., 2023** — Hao Liu, Matei Zaharia, and Pieter Abbeel. "Ring attention with blockwise Transformers for near-infinite context." In *ICLR*, 2023.
  - Cited in 02_related-work.md as Ring Attention for reducing memory footprint.

- **Liu et al., 2024a** — Hao Liu, Wilson Yan, Matei Zaharia, and Pieter Abbeel. "World model on million-length video and language with Ring Attention." *arXiv:2402.08268*, 2024a.
  - Cited in 01_introduction.md as enabling scaling up context length; cited in 03_ruler-benchmark.md (footnote) for the needle format; cited in 05_task-error-analysis.md for consistency with previous works on incomplete retrieval; cited in 06_model-analysis.md as the LargeWorldModels (LWM) suite; cited in 09_appendix-a-models.md as the LWM and LWM-base models.

- **Liu et al., 2024b** — Jiaheng Liu et al. "E2-LLM: Efficient and extreme length extension of large language models." *arXiv:2401.06951*, 2024b.
  - Cited in 02_related-work.md as a RoPE variant for length extrapolation.

- **Liu et al., 2024c** — Jiawei Liu, Jia Le Tian, Vijay Daita, Yuxiang Wei, Yifeng Ding, Yuhan Katherine Wang, Jun Yang, and Lingming Zhang. "Repoqa: Evaluating long context code understanding." *arXiv preprint arXiv:2406.06025*, 2024c.
  - Cited in 02_related-work.md as investigating code understanding in long contexts.

- **Liu et al., 2024d** — Nelson F Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, and Percy Liang. "Lost in the middle: How language models use long contexts." *Transactions of the ACL*, 12:157-173, 2024d.
  - Cited in 02_related-work.md and 08_limitations.md for the lost-in-the-middle phenomenon.

## M

- **Meta AI, 2024a** — Meta AI. "Llama 3 model card." 2024a. URL https://github.com/meta-llama/llama3/blob/main/MODEL_CARD.md.
  - Cited in 09_appendix-a-models.md as the GradientAI/Llama3 model.

- **Meta AI, 2024b** — Meta AI. "Llama 3.1 model card." 2024b. URL https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md.
  - Cited in 09_appendix-a-models.md as the Llama3.1 (70B) and Llama3.1 (8B) models.

- **Mistral AI, 2023** — Mistral AI. "La plateforme." 2023. URL https://mistral.ai/news/la-plateforme/.
  - Cited in 09_appendix-a-models.md as the Mistral-base model.

- **Mistral AI, 2024a** — Mistral AI. "Mistral-7B-Instruct-v0.2." 2024a.
  - Cited in 09_appendix-a-models.md as the Mistral-v0.2 model.

- **Martins et al., 2022** — Pedro Henrique Martins, Zita Marinho, and Andre Martins. "Infinity-former: Infinite memory Transformer." In *Proc. of the 60th Annual Meeting of the ACL (Volume 1: Long Papers)*, 2022.
  - Cited in 02_related-work.md as a recurrence-based method for caching previous context.

- **Mohtashami & Jaggi, 2023** — Amirkeivan Mohtashami and Martin Jaggi. "Landmark attention: Random-access infinite context length for Transformers." In *Workshop on Efficient Systems for Foundation Models @ ICML*, 2023.
  - Cited in 01_introduction.md, 02_related-work.md, and 03_ruler-benchmark.md for passkey retrieval; cited in 03_ruler-benchmark.md (footnote 3) for noise sentence format.

## N

- **Ng, 2010** — Vincent Ng. "Supervised noun phrase coreference research: The first fifteen years." In *Proc. of the 48th Annual Meeting of the ACL*, 2010.
  - Cited in 03_ruler-benchmark.md for coreference chain resolution in the variable tracking task.

## O

- **Olsson et al., 2022** — Catherine Olsson et al. "In-context learning and induction heads." *Transformer Circuits Thread*, 2022.
  - Cited in 03_ruler-benchmark.md as having extensively studied associative recall tasks.

- **OpenAI: Josh Achiam et al., 2023** — OpenAI: Josh Achiam et al. "GPT-4 technical report." *arXiv:2303.08774*, 2023.
  - Cited in 01_introduction.md as one of the models benchmarked.

## P

- **Peng et al., 2023** — Bo Peng et al. "RWKV: Reinventing RNNs for the transformer era." In *EMNLP*, 2023.
  - Cited in 02_related-work.md and 06_model-analysis.md as the RWKV architecture; evaluated as non-Transformer baseline in Section 6.

- **Peng et al., 2024** — Bowen Peng, Jeffrey Quesnelle, Honglu Fan, and Enrico Shippole. "YaRN: Efficient context window extension of large language models." In *ICLR*, 2024.
  - Cited in 02_related-work.md as a RoPE variant for length extrapolation.

- **Poli et al., 2023** — Michael Poli, Stefano Massaroli, Eric Nguyen, Daniel Y Fu, Tri Dao, Stephen Baccus, Yoshua Bengio, Stefano Ermon, and Christopher Re. "Hyena hierarchy: Towards larger convolutional language models." In *ICML*, 2023.
  - Cited in 02_related-work.md as a novel architecture for long-context input.

- **Press et al., 2022** — Ofir Press, Noah Smith, and Mike Lewis. "Train short, test long: Attention with linear biases enables input length extrapolation." In *ICLR*, 2022.
  - Cited in 02_related-work.md as ALiBi, a novel position embedding method for length extrapolation.

## R

- **Rajpurkar et al., 2018** — Pranav Rajpurkar, Robin Jia, and Percy Liang. "Know what you don't know: Unanswerable questions for SQuAD." In *Proc. of the 56th Annual Meeting of the ACL (Volume 2: Short Papers)*, 2018.
  - Cited in 03_ruler-benchmark.md as a short-context QA dataset extended to simulate long-context input.

- **Reid et al., 2024** — Machel Reid et al. "Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context." *arXiv:2403.05530*, 2024.
  - Cited in 01_introduction.md, 03_ruler-benchmark.md, and 05_task-error-analysis.md as a prior work using NIAH for evaluation and as the Gemini model.

- **Ribeiro et al., 2020** — Marco Tulio Ribeiro, Tongshuang Wu, Carlos Guestrin, and Sameer Singh. "Beyond accuracy: Behavioral testing of NLP models with CheckList." In *Proc. of the 58th Annual Meeting of the ACL*, 2020.
  - Cited in 01_introduction.md for behavioral testing framework that RULER builds upon.

## S

- **Shaham et al., 2023** — Uri Shaham, Maor Ivgi, Avia Efrat, Jonathan Berant, and Omer Levy. "ZeroSCROLLS: A zero-shot benchmark for long text understanding." In *EMNLP*, 2023.
  - Cited in 01_introduction.md and 02_related-work.md as the ZeroSCROLLS benchmark.

- **Su et al., 2023** — Jianlin Su, Yu Lu, Shengfeng Pan, Ahmed Murtadha, Bo Wen, and Yunfeng Liu. "RoFormer: Enhanced Transformer with rotary position embedding." *arXiv:2104.09864*, 2023.
  - Cited in 02_related-work.md as the original RoPE position embedding.

- **Sun et al., 2022** — Simeng Sun, Katherine Thai, and Mohit Iyyer. "ChapterBreak: A challenge dataset for long-range language models." In *Proc. of the 2022 Conference of the North American Chapter of the ACL: Human Language Technologies*, 2022.
  - Cited in 02_related-work.md as investigating long-range discourse modeling.

- **Sun et al., 2023a** — Yutao Sun, Li Dong, Shaohan Huang, Shuming Ma, Yuqing Xia, Jilong Xue, Jianyong Wang, and Furu Wei. "Retentive network: A successor to Transformer for large language models." *arXiv:2307.08621*, 2023a.
  - Cited in 02_related-work.md as a novel architecture for long-context input.

- **Sun et al., 2023b** — Yutao Sun, Li Dong, Barun Patra, Shuming Ma, Shaohan Huang, Alon Benhaim, Vishrav Chaudhary, Xia Song, and Furu Wei. "A length-extrapolatable Transformer." In *Proc. of the 61st Annual Meeting of the ACL (Volume 1: Long Papers)*, 2023b.
  - Cited in 02_related-work.md as xPOS, a novel position embedding method.

- **Sun et al., 2024** — Yutao Sun, Li Dong, Yi Zhu, Shaohan Huang, Wenhui Wang, Shuming Ma, Quanlu Zhang, Jianyong Wang, and Furu Wei. "You only cache once: Decoder-decoder architectures for language models." *arXiv preprint arXiv:2405.05254*, 2024.
  - Cited in 02_related-work.md as a novel architecture for long-context input.

## T

- **Together AI, 2023a** — Together AI. "Preparing for the era of 32k context: Early learnings and explorations." 2023a. URL https://www.together.ai/blog/llama-2-7b-32k.
  - Cited in 09_appendix-a-models.md as the Together-base model.

- **Together AI, 2023b** — Together AI. "Llama-2-7b-32k-instruct -- and fine-tuning for llama-2 models with together api." 2023b. URL https://www.together.ai/blog/llama-2-7b-32k-instruct.
  - Cited in 09_appendix-a-models.md as the Together (aligned) model.

- **Touvron et al., 2023** — Hugo Touvron et al. "Llama 2: Open foundation and fine-tuned chat models." *arXiv:2307.09288*, 2023.
  - Cited in 09_appendix-a-models.md as the Llama2 (base) and Llama2 (chat) models.

- **Tanzer et al., 2024** — Garrett Tanzer, Mirac Suzgun, Eline Visser, Dan Jurafsky, and Luke Melas-Kyriazi. "A benchmark for learning to translate a new language from one grammar book." In *ICLR*, 2024.
  - Cited in 02_related-work.md as leveraging extremely low-resource materials to isolate parametric knowledge.

- **Trivedi et al., 2022** — Harsh Trivedi, Niranjan Balasubramanian, Tushar Khot, and Ashish Sabharwal. "Musique: Multihop questions via single-hop question composition." *Transactions of the ACL*, 10: 539-554, 2022.
  - Cited in 03_ruler-benchmark.md as a short-context QA dataset.

- **Tworkowski et al., 2024** — Szymon Tworkowski et al. "Focused Transformer: Contrastive training for context scaling." *NeurIPS*, 36, 2024.
  - Cited in 02_related-work.md as a method for retrieving relevant information from context.

## V

- **van Dijk & Kintsch, 1983** — Teun A. van Dijk and Walter Kintsch. "Strategies of discourse comprehension." In *Academic Press*, 1983.
  - Cited in 03_ruler-benchmark.md for effective discourse comprehension requiring entity recognition and coreference chains.

- **Vaswani et al., 2017** — Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Lukasz Kaiser, and Illia Polosukhin. "Attention is all you need." In *NeurIPS*, 2017.
  - Cited in 02_related-work.md as the original Transformer architecture.

- **Wolf et al., 2019** — Thomas Wolf et al. "HuggingFace's Transformers: State-of-the-art natural language processing." *arXiv:1910.03771*, 2019.
  - Cited in 09_appendix-a-models.md in the Table 4 header for the HuggingFace model hub column.

## W

- **Wang et al., 2024** — Weizhi Wang, Li Dong, Hao Cheng, Xiaodong Liu, Xifeng Yan, Jianfeng Gao, and Furu Wei. "Augmenting language models with long-term memory." *NeurIPS*, 36, 2024.
  - Cited in 02_related-work.md as a method for retrieving relevant information from context.

- **Wu et al., 2022** — Qingyang Wu, Zhenzhong Lan, Kun Qian, Jing Gu, Alborz Geramifard, and Zhou Yu. "Memformer: A memory-augmented Transformer for sequence modeling." In *Findings of the ACL: AACL-IJCNLP*, 2022.
  - Cited in 02_related-work.md as a recurrence-based method for caching previous context.

## X

- **X.AI, 2024** — X.AI. "Announcing grok-1.5." 2024. URL https://x.ai/blog/grok-1.5.
  - Cited in 01_introduction.md as a prior work using synthetic tasks for evaluating long-context LMs.

- **Xiao et al., 2024a** — Chaojun Xiao et al. "InfLLM: Unveiling the intrinsic capacity of LLMs for understanding extremely long sequences with training-free memory." *arXiv:2402.04617*, 2024a.
  - Cited in 02_related-work.md as a method for retrieving relevant information from context.

- **Xiao et al., 2024b** — Guangxuan Xiao, Yuandong Tian, Beidi Chen, Song Han, and Mike Lewis. "Efficient streaming language models with attention sinks." In *ICLR*, 2024b.
  - Cited in 02_related-work.md as an attention sinks method; cited in 05_task-error-analysis.md (footnote 7) for explaining copy behavior due to attention sinks.

- **Xiong et al., 2023** — Wenhan Xiong et al. "Effective long-context scaling of foundation models." *arXiv:2309.16039*, 2023.
  - Cited in 01_introduction.md and 02_related-work.md as enabling scaling up context length via RoPE variants; cited in 04_experiments-results.md for larger base frequencies in RoPE used by top models.

- **Xu et al., 2024a** — Peng Xu, Wei Ping, Xianchao Wu, Lawrence McAfee, Chen Zhu, Zihan Liu, Sandeep Subramanian, Evelina Bakhturina, Mohammad Shoeybi, and Bryan Catanzaro. "Retrieval meets long context large language models." In *ICLR*, 2024a.
  - Cited in 02_related-work.md as a method for retrieving relevant information from context.

- **Xu et al., 2024b** — Xiaoyue Xu, Qinyuan Ye, and Xiang Ren. "Stress-testing long-context language models with lifelong icl and task haystack." *arXiv preprint arXiv:2407.16695*, 2024b.
  - Cited in 02_related-work.md as an example of many-shot in-context learning research.

## Y

- **Yang et al., 2018** — Zhilin Yang, Peng Qi, Saizheng Zhang, Yoshua Bengio, William Cohen, Ruslan Salakhutdinov, and Christopher D. Manning. "HotpotQA: A dataset for diverse, explainable multi-hop question answering." In *EMNLP*, 2018.
  - Cited in 03_ruler-benchmark.md as a short-context QA dataset.

- **Yang et al., 2024** — An Yang, Baosong Yang, Binyuan Hui, et al. "Qwen2 technical report." *arXiv preprint arXiv:2407.10671*, 2024.
  - Cited in 09_appendix-a-models.md as the Qwen2 model.

- **Young et al., 2024** — Alex Young et al. "Yi: Open foundation models by 01.AI." *arXiv:2403.04652*, 2024.
  - Cited in 01_introduction.md as enabling scaling up context length. Cited in 09_appendix-a-models.md as the Yi model.

- **Yuan et al., 2024** — Tao Yuan, Xuefei Ning, Dong Zhou, Zhijie Yang, Shiyao Li, Minghui Zhuang, Zheyue Tan, Zhuyu Yao, Dahua Lin, Boxun Li, et al. "Lv-eval: A balanced long-context benchmark with 5 length levels up to 256k." *arXiv preprint arXiv:2402.05136*, 2024.
  - Cited in 02_related-work.md and 08_limitations.md as LV-Eval, for question answering and depth-level evaluation.

## Z

- **Zhang et al., 2024a** — Peitian Zhang, Zheng Liu, Shitao Xiao, Ninglu Shao, Qiwei Ye, and Zhicheng Dou. "Soaring from 4k to 400k: Extending LLM's context with activation beacon." *arXiv:2401.03462*, 2024a.
  - Cited in 02_related-work.md as a recurrence-based method for caching previous context.

- **Zhang et al., 2024b** — Xinrong Zhang, Yingfa Chen, Shengding Hu, Zihang Xu, Junhao Chen, Moo Khai Hao, Xu Han, Zhen Leng Thai, Shuo Wang, Zhiyuan Liu, and Maosong Sun. "InfiniteBench: Extending long context evaluation beyond 100k tokens." *arXiv:2402.13718*, 2024b.
  - Cited in 02_related-work.md as the InfiniteBench benchmark with tasks >100K tokens.

- **Zhu et al., 2024** — Dawei Zhu, Nan Yang, Liang Wang, Yifan Song, Wenhao Wu, Furu Wei, and Sujian Li. "PoSE: Efficient context window extension of LLMs via positional skip-wise training." In *ICLR*, 2024.
  - Cited in 02_related-work.md as a RoPE variant for length extrapolation.
