# References

[1] Anthropic. Introducing claude, 2023. URL https://www.anthropic.com/index/introducing-claude.
- Cited in 01_introduction.md as example of LLM with expanded context (100K)

[2] Christian Bischof. *Parallel computing: Architectures, algorithms, and applications*, volume 15. IOS Press, 2008.
- Cited in 03_ring-attention.md and 06_related-work.md as prior work on ring communication in parallel computing scenarios

[3] Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. Language models are few-shot learners. *Advances in neural information processing systems*, 33:1877–1901, 2020.
- Cited in 12_appendix-d-training-flops-scaling.md as source for GPT-3 model configuration (hidden dimension 12288 for 175B)

[4] Lili Chen, Kevin Lu, Aravind Rajeswaran, Kimin Lee, Aditya Grover, Misha Laskin, Pieter Abbeel, Aravind Srinivas, and Igor Mordatch. Decision transformer: Reinforcement learning via sequence modeling. *Advances in neural information processing systems*, 34:15084–15097, 2021.
- Cited in 05_results.md as DT baseline in ExoRL experiments (Section 5.3)

[5] Tianqi Chen, Bing Xu, Chiyuan Zhang, and Carlos Guestrin. Training deep nets with sublinear memory cost. *arXiv preprint arXiv:1604.06174*, 2016.
- Cited in 04_setting.md and 10_appendix-b-experiment-details.md for full gradient checkpointing applied to attention and feedforward

[6] Wei-Lin Chiang, Zhuohan Li, Zi Lin, Ying Sheng, Zhanghao Wu, Hao Zhang, Lianmin Zheng, Siyuan Zhuang, Yonghao Zhuang, Joseph E Gonzalez, et al. Vicuna: An open-source chatbot impressing gpt-4 with 90%* chatgpt quality. See https://vicuna.lmsys.org, 2023.
- Cited in 05_results.md and 10_appendix-b-experiment-details.md as prior work methodology followed for LLaMA finetuning (Section 5.4)

[7] Anthony Danalis, Ki-Yong Kim, Lori Pollock, and Martin Swany. Transformations to parallel codes for communication-computation overlap. In *SC'05: Proceedings of the 2005 ACM/IEEE conference on Supercomputing*, pages 58–58. IEEE, 2005.
- Cited in 03_ring-attention.md and 06_related-work.md as HPC literature on overlapping communication with computation

[8] Anthony Danalis, Lori Pollock, Martin Swany, and John Cavazos. Mpi-aware compiler optimizations for improving communication-computation overlap. In *Proceedings of the 23rd international conference on Supercomputing*, pages 316–325, 2009.
- Cited in 03_ring-attention.md and 06_related-work.md as HPC literature on overlapping communication with computation

[9] Tri Dao, Dan Fu, Stefano Ermon, Atri Rudra, and Christopher Re. Flashattention: Fast and memory-efficient exact attention with io-awareness. *Advances in Neural Information Processing Systems*, 35:16344–16359, 2022.
- Cited in 01_introduction.md, 02_large-context-memory-constraint.md, 03_ring-attention.md, 04_setting.md, and 06_related-work.md as efficient CUDA implementation of memory efficient attention

[10] Jeffrey Dean, Greg Corrado, Rajat Monga, Kai Chen, Matthieu Devin, Mark Mao, Marc'aurelio Ranzato, Andrew Senior, Paul Tucker, Ke Yang, et al. Large scale distributed deep networks. *Advances in neural information processing systems*, 25, 2012.
- Cited in 06_related-work.md as prior work on data parallelism

[11] Facebook. Fully Sharded Data Parallel: faster AI training with fewer GPUs — engineering.fb.com. https://engineering.fb.com/2021/07/15/open-source/fsdp/, 2023.
- Cited in 05_results.md (Sections 5.1 and 5.2), 06_related-work.md, and 10_appendix-b-experiment-details.md for FSDP used in evaluation

[12] Xinyang Geng and Hao Liu. Openllama: An open reproduction of llama, may 2023. URL https://github.com/openlm-research/open_llama, 2023.
- Cited in 05_results.md (Sections 5.1 and 5.2) as prior end-to-end training work (OpenLLaMA)

[13] Xinyang Geng, Arnav Gudibande, Hao Liu, Eric Wallace, Pieter Abbeel, Sergey Levine, and Dawn Song. Koala: A dialogue model for academic research. *Blog post, April*, 1, 2023.
- Cited in 05_results.md and 10_appendix-b-experiment-details.md as prior work methodology followed for LLaMA finetuning (Section 5.4)

[14] Andrew Gibiansky. Bringing hpc techniques to deep learning. *Baidu Research, Tech. Rep.*, 2017.
- Cited in 03_ring-attention.md and 06_related-work.md as ring communication in parallel computing scenarios

[15] Yanping Huang, Youlong Cheng, Ankur Bapna, Orhan Firat, Dehao Chen, Mia Chen, HyoukJoong Lee, Jiquan Ngiam, Quoc V Le, Yonghui Wu, et al. Gpipe: Efficient training of giant neural networks using pipeline parallelism. *Advances in neural information processing systems*, 32, 2019.
- Cited in 06_related-work.md as prior work on pipeline parallelism

[16] Joshua Hursey and Richard L Graham. Building a fault tolerant mpi application: A ring communication example. In *2011 IEEE International Symposium on Parallel and Distributed Processing Workshops and Phd Forum*, pages 1549–1556. IEEE, 2011.
- Cited in 03_ring-attention.md and 06_related-work.md as ring communication in parallel computing scenarios

[17] Sam Ade Jacobs, Masahiro Tanaka, Chengming Zhang, Minjia Zhang, Leon Song, Samyam Rajbhandari, and Yuxiong He. Deepspeed ulysses: System optimizations for enabling training of extreme long sequence transformer models. *arXiv preprint arXiv:2309.14509*, 2023.
- Cited in 06_related-work.md as prior work on sequence parallelism; method restricted by number of attention heads, requires gathering full sequence on each device

[18] Vijay Korthikanti, Jared Casper, Sangkug Lym, Lawrence McAfee, Michael Andersch, Mohammad Shoeybi, and Bryan Catanzaro. Reducing activation recomputation in large transformer models. *arXiv preprint arXiv:2205.05198*, 2022.
- Cited in 06_related-work.md as prior work on sequence parallelism

[19] Michael Laskin, Denis Yarats, Hao Liu, Kimin Lee, Albert Zhan, Kevin Lu, Catherine Cang, Lerrel Pinto, and Pieter Abbeel. Urlb: Unsupervised reinforcement learning benchmark. *arXiv preprint arXiv:2110.15191*, 2021.
- Cited in 05_results.md as unsupervised RL used to collect ExoRL data

[20] Dacheng Li, Rulin Shao, Anze Xie, Ying Sheng, Lianmin Zheng, Joseph E. Gonzalez, Ion Stoica, Xuezhe Ma, and Hao Zhang. How long can open-source llms truly promise on context length?, June 2023. URL https://lmsys.org/blog/2023-06-29-longchat.
- Cited in 05_results.md as line retrieval test used to evaluate finetuned model (Section 5.4)

[21] Shenggui Li, Fuzhao Xue, Chaitanya Baranwal, Yongbin Li, and Yang You. Sequence parallelism: Long sequence training from system perspective. In *Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 2391–2404, Toronto, Canada, July 2023. Association for Computational Linguistics.
- Cited in 01_introduction.md, 03_ring-attention.md, and 06_related-work.md as prior work on ring topology for self-attention / sequence parallelism with non-overlapped communication overheads

[22] Hao Liu and Pieter Abbeel. Emergent agentic transformer from chain of hindsight experience. *International Conference on Machine Learning*, 2023.
- Cited in 05_results.md as AT (Algorithm Transformer) baseline in ExoRL experiments (Section 5.3)

[23] Hao Liu and Pieter Abbeel. Blockwise parallel transformer for large context models. *Advances in neural information processing systems*, 2023.
- Cited throughout (01_introduction.md, 02_large-context-memory-constraint.md, 03_ring-attention.md, 04_setting.md, 05_results.md, 06_related-work.md) as blockwise parallel transformer (BPT) — the foundational framework Ring Attention builds upon

[24] Maxim Milakov and Natalia Gimelshein. Online normalizer calculation for softmax. *arXiv preprint arXiv:1805.02867*, 2018.
- Cited in 01_introduction.md and 06_related-work.md as tiling technique enabling blockwise computation of self-attention without full materialization

[25] MosaicML. Introducing mpt-7b: A new standard for open-source, commercially usable llms, 2023. URL https://www.mosaicml.com/blog/mpt-7b.
- Cited in 01_introduction.md as example of LLM with expanded context (65K)

[26] Sharan Narang, Hyung Won Chung, Yi Tay, William Fedus, Thibault Fevry, Michael Matena, Karishma Malkan, Noah Fiedel, Noam Shazeer, Zhenzhong Lan, et al. Do transformer modifications transfer across implementations and applications? *arXiv preprint arXiv:2102.11972*, 2021.
- Cited in 06_related-work.md as survey on attention mechanism approximation techniques

[27] Deepak Narayanan, Aaron Harlap, Amar Phanishayee, Vivek Seshadri, Nikhil R Devanur, Gregory R Ganger, Phillip B Gibbons, and Matei Zaharia. Pipedream: Generalized pipeline parallelism for dnn training. In *Proceedings of the 27th ACM Symposium on Operating Systems Principles*, pages 1–15, 2019.
- Cited in 06_related-work.md as prior work on pipeline parallelism

[28] Deepak Narayanan, Amar Phanishayee, Kaiyu Shi, Xie Chen, and Matei Zaharia. Memory-efficient pipeline-parallel dnn training. In *International Conference on Machine Learning*, pages 7937–7947. PMLR, 2021.
- Cited in 06_related-work.md as prior work on pipeline parallelism

[29] OpenAI. Gpt-4 technical report, 2023.
- Cited in 01_introduction.md as context length scaling challenge and GPT-4 with 32K context

[30] Markus N Rabe and Charles Staats. Self-attention does not need o(n2) memory. *arXiv preprint arXiv:2112.05682*, 2021.
- Cited throughout (01_introduction.md, 02_large-context-memory-constraint.md, 03_ring-attention.md, 04_setting.md, 05_results.md, 06_related-work.md) as memory efficient attention baseline

[31] Samyam Rajbhandari, Jeff Rasley, Olatunji Ruwase, and Yuxiong He. Zero: Memory optimizations toward training trillion parameter models. In *SC20: International Conference for High Performance Computing, Networking, Storage and Analysis*, pages 1–16. IEEE, 2020.
- Cited in 06_related-work.md as prior work on FSDP/Zero

[32] J. Schulman, B. Zoph, C. Kim, J. Hilton, J. Menick, J. Weng, J. F. C. Uribe, L. Fedus, L. Metz, M. Pokorny, R. G. Lopes, S. Zhao, A. Vijayvergiya, E. Sigler, A. Perelman, C. Voss, M. Heaton, J. Parish, D. Cummings, R. Nayak, V. Balcom, D. Schnurr, T. Kaftan, C. Hallacy, N. Turley, N. Deutsch, and V. Goel. Chatgpt: Optimizing language models for dialogue. *OpenAI Blog*, 2022. URL https://openai.com/blog/chatgpt.
- Cited in 01_introduction.md as GPT-3.5 with 16K context

[33] Alexander Sergeev and Mike Del Balso. Horovod: fast and easy distributed deep learning in tensorflow. *arXiv preprint arXiv:1802.05799*, 2018.
- Cited in 03_ring-attention.md and 06_related-work.md as ring communication in parallel computing scenarios

[34] Mohammad Shoeybi, Mostofa Patwary, Raul Puri, Patrick LeGresley, Jared Casper, and Bryan Catanzaro. Megatron-lm: Training multi-billion parameter language models using model parallelism. *arXiv preprint arXiv:1909.08053*, 2019.
- Cited in 06_related-work.md as prior work on tensor parallelism

[35] Yi Tay, Mostafa Dehghani, Samira Abnar, Hyung Won Chung, William Fedus, Jinfeng Rao, Sharan Narang, Vinh Q Tran, Dani Yogatama, and Donald Metzler. Scaling laws vs model architectures: How does inductive bias influence scaling? *arXiv preprint arXiv:2207.10551*, 2022.
- Cited in 06_related-work.md as survey on attention mechanism approximation techniques

[36] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothee Lacroix, Baptiste Roziere, Naman Goyal, Eric Hambro, Faisal Azhar, et al. Llama: Open and efficient foundation language models. *arXiv preprint arXiv:2302.13971*, 2023.
- Cited in 05_results.md (Sections 5.1 and 5.2), 10_appendix-b-experiment-details.md, and 12_appendix-d-training-flops-scaling.md as LLaMA model followed for training setup

[37] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Lukasz Kaiser, and Illia Polosukhin. Attention is all you need. *Advances in neural information processing systems*, 30, 2017.
- Cited throughout (01_introduction.md, 03_ring-attention.md, 04_setting.md, 05_results.md) as the original Transformer / vanilla transformer baseline

[38] Shibo Wang, Jinliang Wei, Amit Sabne, Andy Davis, Berkin Ilbeyi, Blake Hechtman, Dehao Chen, Karthik Srinivasa Murthy, Marcello Maggioni, Qiao Zhang, et al. Overlap communication with dependent computation via decomposition in large deep learning models. In *Proceedings of the 28th ACM International Conference on Architectural Support for Programming Languages and Operating Systems, Volume 1*, pages 93–106, 2022.
- Cited in 03_ring-attention.md and 06_related-work.md as HPC literature on overlapping communication with computation

[39] Denis Yarats, David Brandfonbrener, Hao Liu, Michael Laskin, Pieter Abbeel, Alessandro Lazaric, and Lerrel Pinto. Don't change the algorithm, change the data: Exploratory data for offline reinforcement learning. *arXiv preprint arXiv:2201.13425*, 2022.
- Cited in 05_results.md as ExoRL benchmark and finding that TD learning performs best while behavior cloning struggles (Section 5.3)
