# References

Only references that are cited in the section notes are included below.

---

**Almazrouei et al., 2023**
Ebtesam Almazrouei, Hamza Alobeidli, Abdulaziz Alshamsi, Alessandro Cappelli, Ruxandra Cojocaru, Merouane Debbah, Etienne Goffinet, Daniel Heslow, Julien Launay, Quentin Malartic, Badreddine Noune, Baptiste Pannier, and Guilherme Penedo. Falcon-40B: an open large language model with state-of-the-art performance. 2023.
- Cited in 04_experiments.md as one of the four evaluated model families (Falcon).

**Anagnostidis et al., 2023**
Sotiris Anagnostidis, Dario Pavllo, Luca Biggio, Lorenzo Noci, Aurelien Lucchi, and Thomas Hofmann. Dynamic context pruning for efficient and interpretable autoregressive transformers, 2023.
- Cited in 01_introduction.md as work on improving inference efficiency for lengthy inputs.

**Ainslie et al., 2020**
Joshua Ainslie, Santiago Ontanon, Chris Alberti, Vaclav Cvicek, Zachary Fisher, Philip Pham, Anirudh Ravula, Sumit Sanghai, Qifan Wang, and Li Yang. ETC: Encoding long and structured inputs in transformers. In *EMNLP*, 2020.
- Cited in 10_appendix-b-additional-related-works.md as the Extended Transformer Construction (ETC) with global-local attention mechanism.

**Beltagy et al., 2020**
Iz Beltagy, Matthew E. Peters, and Arman Cohan. Longformer: The long-document transformer, 2020. arXiv:2004.05150.
- Cited in 01_introduction.md as window attention reference; cited in 02_related-work.md as an approximate attention method; cited in 10_appendix-b-additional-related-works.md as combining dilated local windowed attention with global attention.

**Biderman et al., 2023**
Stella Biderman, Hailey Schoelkopf, Quentin Anthony, Herbie Bradley, Kyle O'Brien, Eric Hallahan, Mohammad Aflah Khan, Shivanshu Purohit, USVSN Sai Prashanth, Edward Raff, Aviya Skowron, Lintang Sutawika, and Oskar van der Wal. Pythia: A suite for analyzing large language models across training and scaling, 2023.
- Cited in 04_experiments.md as one of the four evaluated model families (Pythia) and as the codebase for sink token pre-training experiments in Section 4.2.

**Bisk et al., 2020**
Yonatan Bisk, Rowan Zellers, Ronan Le Bras, Jianfeng Gao, and Yejin Choi. Piqa: Reasoning about physical commonsense in natural language. In *Thirty-Fourth AAAI Conference on Artificial Intelligence*, 2020.
- Cited in 04_experiments.md as one of the seven NLP benchmarks (PIQA) for evaluating sink token pre-training.

**bloc97, 2023**
bloc97. NTK-Aware Scaled RoPE allows LLaMA models to have extended (8k+) context size without any fine-tuning and minimal perplexity degradation., 2023.
- Cited in 02_related-work.md as a method for extending pre-trained LLMs with RoPE.

**Bondarenko et al., 2023**
Yelysei Bondarenko, Markus Nagel, and Tijmen Blankevoort. Quantizable transformers: Removing outliers by helping attention heads do nothing, 2023.
- Cited in 03a_failure-of-window-attention-and-attention-sinks.md as related work on quantization outliers linked to the attention sink phenomenon.

**Brown et al., 2020**
Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. Language models are few-shot learners. *Advances in neural information processing systems*, 33:1877-1901, 2020.
- Cited in 01_introduction.md as a foundational LLM reference.

**Child et al., 2019**
Rewon Child, Scott Gray, Alec Radford, and Ilya Sutskever. Generating long sequences with sparse transformers. 2019.
- Cited in 10_appendix-b-additional-related-works.md as Sparse Transformer introducing sparse factorizations of the attention matrix with $O(n\sqrt{n})$ complexity.

**Chen et al., 2021**
Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde de Oliveira Pinto, Jared Kaplan, Harri Edwards, Yuri Burda, Nicholas Joseph, Greg Brockman, Alex Ray, Raul Puri, Gretchen Krueger, Michael Petrov, Heidy Khlaaf, Girish Sastry, Pamela Mishkin, Brooke Chan, Scott Gray, Nick Ryder, Mikhail Pavlov, Alethea Power, Lukasz Kaiser, Mohammad Bavarian, Clemens Winter, Philippe Tillet, Felipe Petroski Such, Dave Cummings, Matthias Plappert, Fotios Chantzis, Elizabeth Barnes, Ariel Herbert-Voss, William Hebgen Guss, Alex Nichol, Alex Paino, Nikolas Tezak, Jie Tang, Igor Babuschkin, Suchir Balaji, Shantanu Jain, William Saunders, Christopher Hesse, Andrew N. Carr, Jan Leike, Josh Achiam, Vedant Misra, Evan Morikawa, Alec Radford, Matthew Knight, Miles Brundage, Mira Murati, Katie Mayer, Peter Welinder, Bob McGrew, Dario Amodei, Sam McCandlish, Ilya Sutskever, and Wojciech Zaremba. Evaluating large language models trained on code, 2021.
- Cited in 01_introduction.md as an example of code completion powered by LLMs.

**Chen et al., 2023**
Shouyuan Chen, Sherman Wong, Liangjian Chen, and Yuandong Tian. Extending context window of large language models via positional interpolation, 2023. arXiv: 2306.15595.
- Cited in 01_introduction.md and 02_related-work.md as a context window extension method using position interpolation with RoPE.

**Chiang et al., 2023**
Wei-Lin Chiang, Zhuohan Li, Zi Lin, Ying Sheng, Zhanghao Wu, Hao Zhang, Lianmin Zheng, Siyuan Zhuang, Yonghao Zhuang, Joseph E. Gonzalez, Ion Stoica, and Eric P. Xing. Vicuna: An open-source chatbot impressing gpt-4 with 90%* chatgpt quality, March 2023.
- Cited in 01_introduction.md as an example of dialog systems powered by LLMs.

**Clark et al., 2018**
Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar Khot, Ashish Sabharwal, Carissa Schoenick, and Oyvind Tafjord. Think you have solved question answering? try arc, the ai2 reasoning challenge. *arXiv:1803.05457v1*, 2018.
- Cited in 04_experiments.md as the source of the ARC-[Challenge, Easy] benchmarks.

**Darcet et al., 2023**
Timothee Darcet, Maxime Oquab, Julien Mairal, and Piotr Bojanowski. Vision transformers need registers, 2023.
- Cited in 10_appendix-b-additional-related-works.md as concurrent work observing similar attention concentration on random background patch tokens in Vision Transformers, termed "registers"; cited in 16_appendix-h-encoder-transformers.md as identifying attention spikes in ViTs attributed to background patch tokens acting as "registers"; cited in 17_appendix-i-more-sink-tokens.md as contrasting finding where multiple "registers" are beneficial in ViTs.

**Dao, 2023**
Tri Dao. FlashAttention-2: Faster attention with better parallelism and work partitioning. 2023.
- Cited in 01_introduction.md and 02_related-work.md as a system optimization for training efficiency.

**Dao et al., 2022**
Tri Dao, Daniel Y. Fu, Stefano Ermon, Atri Rudra, and Christopher Re. FlashAttention: Fast and memory-efficient exact attention with IO-awareness, 2022. arXiv:2205.14135.
- Cited in 01_introduction.md and 02_related-work.md as a system optimization for training efficiency.

**Han et al., 2023**
Chi Han, Qifan Wang, Wenhan Xiong, Yu Chen, Heng Ji, and Sinong Wang. LM-Infinite: Simple on-the-fly length generalization for large language models, 2023.
- Cited in 10_appendix-b-additional-related-works.md as concurrent work conducting a theoretical study on length generalization failure, employing a "Lambda"-shaped attention pattern.

**Gao et al., 2020**
Leo Gao, Stella Biderman, Sid Black, Laurence Golding, Travis Hoppe, Charles Foster, Jason Phang, Horace He, Anish Thite, Noa Nabeshima, Shawn Presser, and Connor Leahy. The Pile: An 800gb dataset of diverse text for language modeling. *arXiv preprint arXiv:2101.00027*, 2020.
- Cited in 04_experiments.md as the training dataset (deduplicated Pile) for sink token pre-training experiments.

**Goyal & Durrett, 2020**
Tanya Goyal and Greg Durrett. Evaluating factuality in generation with dependency-level entailment. In *Findings of the Association for Computational Linguistics: EMNLP 2020*, Online, 2020.
- Cited in 01_introduction.md as an example of document summarization powered by LLMs.

**kaiokendev, 2023**
kaiokendev. Things I'm learning while training superhot., 2023.
- Cited in 01_introduction.md and 02_related-work.md as work on expanding the attention window size.

**Kamalloo et al., 2023**
Ehsan Kamalloo, Nouha Dziri, Charles L. A. Clarke, and Davood Rafiei. Evaluating open-domain question answering in the era of large language models, 2023.
- Cited in 01_introduction.md as an example of question answering powered by LLMs.

**Kitaev et al., 2020**
Nikita Kitaev, Lukasz Kaiser, and Anselm Levskaya. Reformer: The efficient transformer. In *8th International Conference on Learning Representations, ICLR 2020*. OpenReview.net, April 2020.
- Cited in 02_related-work.md as an approximate attention method.

**Li et al., 2023**
Dacheng Li, Rulin Shao, Anze Xie, Ying Sheng, Lianmin Zheng, Joseph E. Gonzalez, Ion Stoica, Xuezhe Ma, and Hao Zhang. How long can open-source llms truly promise on context length?, June 2023.
- Cited in 02_related-work.md as evidence that context extension does not guarantee effective utilization of long contexts; cited in 04_experiments.md as the inspiration for the StreamEval benchmark (LongEval) and as the source of LongChat-7b-v1.5-32k.

**Liu et al., 2023**
Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, and Percy Liang. Lost in the middle: How language models use long contexts, 2023.
- Cited in 02_related-work.md as evidence that success in length extrapolation or context extension does not necessarily translate to effective utilization of lengthy contexts; cited in 11_appendix-c-streameval-accuracy.md as supporting evidence that LLMs cannot fully utilize context information within the cache; cited in 12_appendix-d-long-range-benchmark.md as aligned observation on inability to fully utilize context information.

**Mihaylov et al., 2018**
Todor Mihaylov, Peter Clark, Tushar Khot, and Ashish Sabharwal. Can a suit of armor conduct electricity? a new dataset for open book question answering. In *EMNLP*, 2018.
- Cited in 04_experiments.md as the source of the OpenbookQA benchmark.

**Miller, 2023**
Evan Miller. Attention is off by one, 2023. URL https://www.evanmiller.org/attention-is-off-by-one.html.
- Cited in 03a_failure-of-window-attention-and-attention-sinks.md and 03c_pre-training-llms-with-attention-sinks.md as the proposal for SoftMax-Off-by-One (SoftMax$_1$), used as "Zero Sink" variant.

**OpenAI, 2023**
OpenAI. Gpt-4 technical report, 2023.
- Cited in 01_introduction.md as a foundational LLM reference.

**Paperno et al., 2016**
Denis Paperno, German Kruszewski, Angeliki Lazaridou, Ngoc Quan Pham, Raffaella Bernardi, Sandro Pezzelle, Marco Baroni, Gemma Boleda, and Raquel Fernandez. The LAMBADA dataset: Word prediction requiring a broad discourse context. In *Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pp. 1525-1534, Berlin, Germany, August 2016.
- Cited in 04_experiments.md as the source of the LAMBADA benchmark.

**Peng et al., 2023**
Bowen Peng, Jeffrey Quesnelle, Honglu Fan, and Enrico Shippole. Yarn: Efficient context window extension of large language models, 2023.
- Cited in 01_introduction.md and 02_related-work.md as work on expanding the attention window / context extension with RoPE.

**Pope et al., 2022**
Reiner Pope, Sholto Douglas, Aakanksha Chowdhery, Jacob Devlin, James Bradbury, Anselm Levskaya, Jonathan Heek, Kefan Xiao, Shivani Agrawal, and Jeff Dean. Efficiently scaling transformer inference. *arXiv preprint arXiv:2211.05102*, 2022.
- Cited in 01_introduction.md as work on improving inference efficiency and as motivation for KV caching memory concerns.

**Press et al., 2022**
Ofir Press, Noah Smith, and Mike Lewis. Train short, test long: Attention with linear biases enables input length extrapolation. In *International Conference on Learning Representations*, 2022.
- Cited in 01_introduction.md, 02_related-work.md, 03b_rolling-kv-cache-with-attention-sinks.md, and 04_experiments.md as the ALiBi positional encoding method and as evidence of limited length extrapolation.

**Radford et al., 2018**
Alec Radford, Karthik Narasimhan, Tim Salimans, Ilya Sutskever, et al. Improving language understanding by generative pre-training. 2018.
- Cited in 01_introduction.md as a foundational LLM reference.

**Rae et al., 2020**
Jack W. Rae, Anna Potapenko, Siddhant M. Jayakumar, Chloe Hillier, and Timothy P. Lillicrap. Compressive transformers for long-range sequence modelling. In *International Conference on Learning Representations*, 2020.
- Cited in 04_experiments.md as the source of the PG19 dataset used for language modeling evaluation.

**Roziere et al., 2023**
Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, Sten Sootla, Itai Gat, Xiaoqing Ellen Tan, Yossi Adi, Jingyu Liu, Tal Remez, Jeremy Rapin, Artyom Kozhevnikov, Ivan Evtimov, Joanna Bitton, Manish Bhatt, Cristian Canton Ferrer, Aaron Grattafiori, Wenhan Xiong, Alexandre Defossez, Jade Copet, Faisal Azhar, Hugo Touvron, Louis Martin, Nicolas Usunier, Thomas Scialom, and Gabriel Synnaeve. Code Llama: Open foundation models for code, 2023.
- Cited in 01_introduction.md as an example of code completion powered by LLMs.

**Sakaguchi et al., 2019**
Keisuke Sakaguchi, Ronan Le Bras, Chandra Bhagavatula, and Yejin Choi. Winogrande: An adversarial winograd schema challenge at scale. *arXiv preprint arXiv:1907.10641*, 2019.
- Cited in 04_experiments.md as the source of the Winogrande benchmark.

**Schulman et al., 2022**
John Schulman, Barret Zoph, Christina Kim, Jacob Hilton, Jacob Menick, Jiayi Weng, Juan Felipe Ceron Uribe, Liam Fedus, Luke Metz, Michael Pokorny, et al. Chatgpt: Optimizing language models for dialogue. *OpenAI blog*, 2022.
- Cited in 01_introduction.md as an example of dialog systems powered by LLMs.

**Su et al., 2021**
Jianlin Su, Yu Lu, Shengfeng Pan, Ahmed Murtadha, Bo Wen, and Yunfeng Liu. Roformer: Enhanced transformer with rotary position embedding. *arXiv preprint arXiv:2104.09864*, 2021.
- Cited in 02_related-work.md, 03b_rolling-kv-cache-with-attention-sinks.md, and 04_experiments.md as the RoPE positional encoding method used by Llama-2, Falcon, and Pythia.

**Tay et al., 2022**
Yi Tay, Mostafa Dehghani, Dara Bahri, and Donald Metzler. Efficient transformers: A survey. *ACM Computing Surveys*, 55(6), dec 2022. ISSN 0360-0300.
- Cited in 10_appendix-b-additional-related-works.md as a survey on efficient Transformer models and sparsifying attention with fixed patterns.

**Taori et al., 2023**
Rohan Taori, Ishaan Gulrajani, Tianyi Zhang, Yann Dubois, Xuechen Li, Carlos Guestrin, Percy Liang, and Tatsunori B. Hashimoto. Stanford alpaca: An instruction-following llama model. https://github.com/tatsu-lab/stanford_alpaca, 2023.
- Cited in 01_introduction.md as an example of dialog systems powered by LLMs.

**Team, 2023**
MosaicML NLP Team. Introducing mpt-7b: A new standard for open-source, commercially usable llms, 2023. URL www.mosaicml.com/blog/mpt-7b.
- Cited in 04_experiments.md as one of the four evaluated model families (MPT).

**Together, 2023**
Together. Llama-2-7b-32k-instruct -- and fine-tuning for llama-2 models with together api, June 2023. URL https://together.ai/blog/llama-2-7b-32k-instruct.
- Cited in 04_experiments.md as the source of Llama-2-7B-32K-Instruct, a context-extended model.

**Touvron et al., 2023a**
Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothee Lacroix, Baptiste Roziere, Naman Goyal, Eric Hambro, Faisal Azhar, et al. Llama: Open and efficient foundation language models. *arXiv preprint arXiv:2302.13971*, 2023a.
- Cited in 01_introduction.md as a foundational LLM reference.

**Touvron et al., 2023b**
Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, et al. Llama 2: Open foundation and fine-tuned chat models. *arXiv preprint arXiv:2307.09288*, 2023b.
- Cited in 01_introduction.md and 04_experiments.md as the primary evaluated model family (Llama-2) and defining the 4K pre-training window.

**Wang et al., 2020**
Sinong Wang, Belinda Z Li, Madian Khabsa, Han Fang, and Hao Ma. Linformer: Self-attention with linear complexity. 2020.
- Cited in 02_related-work.md as an approximate attention method.

**Wang et al., 2021**
Hanrui Wang, Zhekai Zhang, and Song Han. Spatten: Efficient sparse attention architecture with cascade token and head pruning. *HPCA*, 2021.
- Cited in 01_introduction.md as work on improving inference efficiency for lengthy inputs.

**Wolf et al., 2020**
Thomas Wolf, Lysandre Debut, Victor Sanh, Julien Chaumond, Clement Delangue, Anthony Moi, Pierric Cistac, Tim Rault, Remi Louf, Morgan Funtowicz, Joe Davison, Sam Shleifer, Patrick von Platen, Clara Ma, Yacine Jernite, Julien Plu, Canwen Xu, Teven Le Scao, Sylvain Gugger, Mariama Drame, Quentin Lhoest, and Alexander M. Rush. Huggingface's transformers: State-of-the-art natural language processing, 2020.
- Cited in 04e_efficiency-results.md as the implementation library for efficiency benchmarks.

**Xiao et al., 2023**
Guangxuan Xiao, Ji Lin, Mickael Seznec, Hao Wu, Julien Demouth, and Song Han. SmoothQuant: Accurate and efficient post-training quantization for large language models. In *Proceedings of the 40th International Conference on Machine Learning*, 2023.
- Cited in 01_introduction.md as work on inference efficiency and in 03a_failure-of-window-attention-and-attention-sinks.md as related work on quantization outliers.

**Zaheer et al., 2020a**
Manzil Zaheer, Guru Guruganesh, Kumar Avinava Dubey, Joshua Ainslie, Chris Alberti, Santiago Ontanon, Philip Pham, Anirudh Ravula, Qifan Wang, Li Yang, and Amr Ahmed. Big Bird: Transformers for longer sequences. In *Proc. of NeurIPS*, volume 33, 2020a.
- Cited in 10_appendix-b-additional-related-works.md as BigBird proposing linear complexity attention with global tokens, local sliding window attentions, and random attention.

**Zaheer et al., 2020b**
Manzil Zaheer, Guru Guruganesh, Kumar Avinava Dubey, Joshua Ainslie, Chris Alberti, Santiago Ontanon, Philip Pham, Anirudh Ravula, Qifan Wang, Li Yang, and Amr Ahmed. Big bird: Transformers for longer sequences. In *Advances in Neural Information Processing Systems 33: NeurIPS 2020*. Curran Associates, Inc., 2020b.
- Cited in 02_related-work.md as an approximate attention method.

**Zellers et al., 2019**
Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali Farhadi, and Yejin Choi. Hellaswag: Can a machine really finish your sentence? *CoRR*, abs/1905.07830, 2019.
- Cited in 04_experiments.md as the source of the HellaSwag benchmark.

**Zhang et al., 2022**
Susan Zhang, Stephen Roller, Naman Goyal, Mikel Artetxe, Moya Chen, Shuohui Chen, Christopher Dewan, Mona Diab, Xian Li, Xi Victoria Lin, Todor Mihaylov, Myle Ott, Sam Shleifer, Kurt Shuster, Daniel Simig, Punit Singh Koura, Anjali Sridhar, Tianlu Wang, and Luke Zettlemoyer. Opt: Open pre-trained transformer language models, 2022.
- Cited in 01_introduction.md as a foundational LLM reference.

**Zhang et al., 2023a**
Tianyi Zhang, Faisal Ladhak, Esin Durmus, Percy Liang, Kathleen McKeown, and Tatsunori B. Hashimoto. Benchmarking large language models for news summarization, 2023a.
- Cited in 01_introduction.md as an example of document summarization powered by LLMs.

**Zhang et al., 2023b**
Zhenyu Zhang, Ying Sheng, Tianyi Zhou, Tianlong Chen, Lianmin Zheng, Ruisi Cai, Zhao Song, Yuandong Tian, Christopher Re, Clark Barrett, Zhangyang Wang, and Beidi Chen. H2o: Heavy-hitter oracle for efficient generative inference of large language models, 2023b.
- Cited in 01_introduction.md as work on improving inference efficiency for lengthy inputs.

**Bai et al., 2023**
Yushi Bai, Xin Lv, Jiajie Zhang, Hongchang Lyu, Jiankai Tang, Zhidian Huang, Zhengxiao Du, Xiao Liu, Aohan Zeng, Lei Hou, Yuxiao Dong, Jie Tang, and Juanzi Li. Longbench: A bilingual, multitask benchmark for long context understanding. *arXiv preprint arXiv:2308.14508*, 2023.
- Cited in 12_appendix-d-long-range-benchmark.md as the LongBench benchmark used for long-range evaluation of StreamingLLM.

**Dasigi et al., 2021**
Pradeep Dasigi, Kyle Lo, Iz Beltagy, Arman Cohan, Noah A. Smith, and Matt Gardner. A dataset of information-seeking questions and answers anchored in research papers, 2021.
- Cited in 12_appendix-d-long-range-benchmark.md as the source of the Qasper single-document QA dataset.

**Devlin et al., 2019**
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. Bert: Pre-training of deep bidirectional transformers for language understanding. In *North American Chapter of the Association for Computational Linguistics*, 2019.
- Cited in 16_appendix-h-encoder-transformers.md as the BERT encoder model used to demonstrate attention sinks in encoder Transformers.

**Dosovitskiy et al., 2021**
Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, Jakob Uszkoreit, and Neil Houlsby. An image is worth 16x16 words: Transformers for image recognition at scale, 2021.
- Cited in 16_appendix-h-encoder-transformers.md as the Vision Transformer (ViT) architecture proposed to also exhibit attention sink behavior.

**Fabbri et al., 2019**
Alexander Fabbri, Irene Li, Tianwei She, Suyi Li, and Dragomir Radev. Multi-news: A large-scale multi-document summarization dataset and abstractive hierarchical model. In *Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics*, 2019.
- Cited in 12_appendix-d-long-range-benchmark.md as the source of the MultiNews summarization dataset in LongBench.

**Ho et al., 2020**
Xanh Ho, Anh-Khoa Duong Nguyen, Saku Sugawara, and Akiko Aizawa. Constructing a multi-hop QA dataset for comprehensive evaluation of reasoning steps. In *Proceedings of the 28th International Conference on Computational Linguistics*, December 2020.
- Cited in 12_appendix-d-long-range-benchmark.md as the source of the 2WikiMQA multi-document QA dataset in LongBench.

**Huang et al., 2021**
Luyang Huang, Shuyang Cao, Nikolaus Parulian, Heng Ji, and Lu Wang. Efficient attentions for long document summarization, 2021.
- Cited in 12_appendix-d-long-range-benchmark.md as the source of the GovReport summarization dataset in LongBench.

**Kocisk\'y et al., 2017**
Tomas Kocisk\'y, Jonathan Schwarz, Phil Blunsom, Chris Dyer, Karl Moritz Hermann, Gabor Melis, and Edward Grefenstette. The narrativeqa reading comprehension challenge, 2017.
- Cited in 12_appendix-d-long-range-benchmark.md as the source of the NarrativeQA single-document QA dataset in LongBench.

**Yang et al., 2018**
Zhilin Yang, Peng Qi, Saizheng Zhang, Yoshua Bengio, William W. Cohen, Ruslan Salakhutdinov, and Christopher D. Manning. HotpotQA: A dataset for diverse, explainable multi-hop question answering. In *Conference on Empirical Methods in Natural Language Processing (EMNLP)*, 2018.
- Cited in 12_appendix-d-long-range-benchmark.md as the source of the HotpotQA multi-document QA dataset in LongBench.
