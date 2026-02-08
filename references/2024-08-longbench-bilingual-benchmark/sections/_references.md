# References

Only references that are cited in the section notes are included.

## A

### Ainslie et al. (2023)
Joshua Ainslie, Tao Lei, Michiel de Jong, Santiago Ontanon, Siddhartha Brahma, Yury Zemlyanskiy, David Uthus, Mandy Guo, James Lee-Thorp, Yi Tay, et al. 2023. Colt5: Faster long-range transformers with conditional computation. *arXiv preprint arXiv:2303.09752*.
- Cited in 03_longbench-task-and-construction.md as motivation for few-shot learning requiring long context

### An et al. (2023)
Chenxin An, Shansan Gong, Ming Zhong, Mukai Li, Jun Zhang, Lingpeng Kong, and Xipeng Qiu. 2023. L-eval: Instituting standardized evaluation for long context language models. *arXiv preprint arXiv:2307.11088*.
- Cited in 02_related-work.md as a concurrent evaluation benchmark (L-Eval); in 06_limitations.md as alternative LLM-as-examiner evaluation approach

## B

### Bai et al. (2023)
Yushi Bai, Jiahao Ying, Yixin Cao, Xin Lv, Yuze He, Xiaozhi Wang, Jifan Yu, Kaisheng Zeng, Yijia Xiao, Haozhe Lyu, et al. 2023. Benchmarking foundation models with language-model-as-an-examiner. *arXiv preprint arXiv:2306.04181*.
- Cited in 06_limitations.md regarding unreliability of automatic metrics and LLM-as-examiner evaluation

### Beltagy et al. (2020)
Iz Beltagy, Matthew E Peters, and Arman Cohan. 2020. Longformer: The long-document transformer. *arXiv preprint arXiv:2004.05150*.
- Cited in 02_related-work.md as sparse/efficient transformer approach; also noted for perplexity-based evaluation

### Borgeaud et al. (2022)
Sebastian Borgeaud, Arthur Mensch, Jordan Hoffmann, Trevor Cai, Eliza Rutherford, Katie Millican, George Bm Van Den Driessche, Jean-Baptiste Lespiau, Bogdan Damoc, Aidan Clark, et al. 2022. Improving language models by retrieving from trillions of tokens. In *International conference on machine learning*, pages 2206-2240. PMLR.
- Cited in 04_experiments.md as prior work on retrieval-augmented language models

### Bulatov et al. (2022)
Aydar Bulatov, Yury Kuratov, and Mikhail Burtsev. 2022. Recurrent memory transformer. *Advances in Neural Information Processing Systems*, 35:11079-11091.
- Cited in 02_related-work.md as recurrent/memory module approach

### Bulatov et al. (2023)
Aydar Bulatov, Yuri Kuratov, and Mikhail S Burtsev. 2023. Scaling transformer to 1m tokens and beyond with rmt. *arXiv preprint arXiv:2304.11062*.
- Cited in 01_introduction.md as utilizing recurrent memory for long context

## C

### Chen et al. (2023)
Shouyuan Chen, Sherman Wong, Liangjian Chen, and Yuandong Tian. 2023. Extending context window of large language models via positional interpolation. *arXiv preprint arXiv:2306.15595*.
- Cited in 01_introduction.md and 02_related-work.md as length extrapolation method; in 04_experiments.md for ChatGLM2-6B-32k position interpolation

### Child et al. (2019)
Rewon Child, Scott Gray, Alec Radford, and Ilya Sutskever. 2019. Generating long sequences with sparse transformers. *arXiv preprint arXiv:1904.10509*.
- Cited in 02_related-work.md as sparse/efficient computation approach

## D

### Dai et al. (2019)
Zihang Dai, Zhilin Yang, Yiming Yang, Jaime G Carbonell, Quoc Le, and Ruslan Salakhutdinov. 2019. Transformer-xl: Attentive language models beyond a fixed-length context. In *Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics*, pages 2978-2988.
- Cited in 01_introduction.md and 02_related-work.md as recurrent memory approach

### Dasigi et al. (2021)
Pradeep Dasigi, Kyle Lo, Iz Beltagy, Arman Cohan, Noah A Smith, and Matt Gardner. 2021. A dataset of information-seeking questions and answers anchored in research papers. In *Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies*, pages 4599-4610.
- Cited in 03_longbench-task-and-construction.md as source for the Qasper dataset

### Ding et al. (2023)
Jiayu Ding, Shuming Ma, Li Dong, Xingxing Zhang, Shaohan Huang, Wenhui Wang, and Furu Wei. 2023. Longnet: Scaling transformers to 1,000,000,000 tokens. *arXiv preprint arXiv:2307.02486*.
- Cited in 01_introduction.md and 02_related-work.md as sparsed attention approach

### Du et al. (2022)
Zhengxiao Du, Yujie Qian, Xiao Liu, Ming Ding, Jiezhong Qiu, Zhilin Yang, and Jie Tang. 2022. Glm: General language model pretraining with autoregressive blank infilling. In *Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 320-335.
- Cited in 04_experiments.md as the basis for ChatGLM2-6B

## F

### Fabbri et al. (2019)
Alexander Richard Fabbri, Irene Li, Tianwei She, Suyi Li, and Dragomir Radev. 2019. Multi-news: A large-scale multi-document summarization dataset and abstractive hierarchical model. In *Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics*, pages 1074-1084.
- Cited in 03_longbench-task-and-construction.md as source for the MultiNews dataset

### Fedus et al. (2022)
William Fedus, Barret Zoph, and Noam Shazeer. 2022. Switch transformers: Scaling to trillion parameter models with simple and efficient sparsity. *The Journal of Machine Learning Research*, 23(1):5232-5270.
- Cited in 02_related-work.md as sparse/efficient computation approach

## G

### Gliwa et al. (2019)
Bogdan Gliwa, Iwona Mochol, Maciej Biesek, and Aleksander Wawer. 2019. Samsum corpus: A human-annotated dialogue dataset for abstractive summarization. *EMNLP-IJCNLP 2019*, page 70.
- Cited in 03_longbench-task-and-construction.md as source for the SAMSum dataset

### Guo et al. (2023)
Daya Guo, Canwen Xu, Nan Duan, Jian Yin, and Julian McAuley. 2023. Longcoder: A long-range pretrained language model for code completion. *arXiv preprint arXiv:2306.14893*.
- Cited in 03_longbench-task-and-construction.md as source for the LCC dataset

## H

### He et al. (2018)
Wei He, Kai Liu, Jing Liu, Yajuan Lyu, Shiqi Zhao, Xinyan Xiao, Yuan Liu, Yizhong Wang, Hua Wu, Qiaoqiao She, et al. 2018. Dureader: a chinese machine reading comprehension dataset from real-world applications. *ACL 2018*, page 37.
- Cited in 03_longbench-task-and-construction.md as source for the DuReader dataset

### Hendrycks et al. (2021)
Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn Song, and Jacob Steinhardt. 2021. Measuring massive multitask language understanding. In *International Conference on Learning Representations*.
- Cited in 01_introduction.md as example of short-context multi-task benchmark

### Ho et al. (2020)
Xanh Ho, Anh-Khoa Duong Nguyen, Saku Sugawara, and Akiko Aizawa. 2020. Constructing a multi-hop qa dataset for comprehensive evaluation of reasoning steps. In *Proceedings of the 28th International Conference on Computational Linguistics*, pages 6609-6625.
- Cited in 03_longbench-task-and-construction.md as source for the 2WikiMultihopQA dataset

### Huang et al. (2021)
Luyang Huang, Shuyang Cao, Nikolaus Parulian, Heng Ji, and Lu Wang. 2021. Efficient attentions for long document summarization. In *Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies*, pages 1419-1436.
- Cited in 03_longbench-task-and-construction.md as source for the GovReport dataset

## I

### Izacard et al. (2022a)
Gautier Izacard, Mathilde Caron, Lucas Hosseini, Sebastian Riedel, Piotr Bojanowski, Armand Joulin, and Edouard Grave. 2022a. Unsupervised dense information retrieval with contrastive learning. *Transactions on Machine Learning Research*.
- Cited in 04_experiments.md as the Contriever retriever used in context compression experiments

### Izacard et al. (2022b)
Gautier Izacard, Patrick Lewis, Maria Lomeli, Lucas Hosseini, Fabio Petroni, Timo Schick, Jane Dwivedi-Yu, Armand Joulin, Sebastian Riedel, and Edouard Grave. 2022b. Few-shot learning with retrieval augmented language models. *arXiv preprint arXiv:2208.03299*.
- Cited in 04_experiments.md as prior work on retrieval-augmented language models

## J

### Joshi et al. (2017)
Mandar Joshi, Eunsol Choi, Daniel S Weld, and Luke Zettlemoyer. 2017. Triviaqa: A large scale distantly supervised challenge dataset for reading comprehension. In *Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 1601-1611.
- Cited in 03_longbench-task-and-construction.md as source for the TriviaQA dataset

## K

### Khandelwal et al. (2020)
Urvashi Khandelwal, Omer Levy, Dan Jurafsky, Luke Zettlemoyer, and Mike Lewis. 2020. Generalization through memorization: Nearest neighbor language models. In *International Conference on Learning Representations*.
- Cited in 04_experiments.md as prior work on retrieval-augmented language models with external memory

### Kitaev et al. (2020)
Nikita Kitaev, Lukasz Kaiser, and Anselm Levskaya. 2020. Reformer: The efficient transformer. In *International Conference on Learning Representations*.
- Cited in 02_related-work.md as sparse/efficient computation approach

### Kočiský et al. (2018)
Tomáš Kočiský, Jonathan Schwarz, Phil Blunsom, Chris Dyer, Karl Moritz Hermann, Gábor Melis, and Edward Grefenstette. 2018. The narrativeqa reading comprehension challenge. *Transactions of the Association for Computational Linguistics*, 6:317-328.
- Cited in 03_longbench-task-and-construction.md as source for the NarrativeQA dataset

## L

### Li et al. (2023)
Dacheng Li, Rulin Shao, Anze Xie, Ying Sheng, Lianmin Zheng, Joseph E. Gonzalez, Ion Stoica, Xuezhe Ma, and Hao Zhang. 2023. How long can open-source llms truly promise on context length?
- Cited in 02_related-work.md for LongChat-32k; in 04_experiments.md for LongChat-v1.5-7B-32k model

### Li and Roth (2002)
Xin Li and Dan Roth. 2002. Learning question classifiers. In *COLING 2002: The 19th International Conference on Computational Linguistics*.
- Cited in 03_longbench-task-and-construction.md as source for the TREC dataset

### Liang et al. (2023)
Xinnian Liang, Bing Wang, Hui Huang, Shuangzhi Wu, Peihao Wu, Lu Lu, Zejun Ma, and Zhoujun Li. 2023. Unleashing infinite-length input capacity for large-scale language models with self-controlled memory system. *arXiv preprint arXiv:2304.13343*.
- Cited in 01_introduction.md and 02_related-work.md as external memory augmentation approach

### Lin (2004)
Chin-Yew Lin. 2004. Rouge: A package for automatic evaluation of summaries. In *Text summarization branches out*, pages 74-81.
- Cited in 04_experiments.md as the source of the ROUGE-L metric

### Liu et al. (2023a)
Nelson F Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, and Percy Liang. 2023a. Lost in the middle: How language models use long contexts. *arXiv preprint arXiv:2307.03172*.
- Cited in 03_longbench-task-and-construction.md regarding positional biases in evidence placement; in 01_introduction.md

### Liu et al. (2023b)
Tianyang Liu, Canwen Xu, and Julian McAuley. 2023b. Repobench: Benchmarking repository-level code auto-completion systems. *arXiv preprint arXiv:2306.03091*.
- Cited in 03_longbench-task-and-construction.md as source for the RepoBench-P dataset

### Liu et al. (2023c)
Xiao Liu, Hao Yu, Hanchen Zhang, Yifan Xu, Xuanyu Lei, Hanyu Lai, Yu Gu, Hangliang Ding, Kaiwen Men, Kejuan Yang, et al. 2023c. Agentbench: Evaluating llms as agents. *arXiv preprint arXiv:2308.03688*.
- Cited in 02_related-work.md regarding agent handling of long interaction trajectories

## M

### Martins et al. (2022)
Pedro Henrique Martins, Zita Marinho, and André FT Martins. 2022. ∞-former: Infinite memory transformer. In *Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 5468-5485.
- Cited in 02_related-work.md as recurrent/memory module approach

### Mohtashami and Jaggi (2023)
Amirkeivan Mohtashami and Martin Jaggi. 2023. Landmark attention: Random-access infinite context length for transformers. *arXiv preprint arXiv:2305.16300*.
- Cited in 01_introduction.md as sparsed attention approach

## N

### Nijkamp et al. (2023)
Erik Nijkamp, Tian Xie, Hiroaki Hayashi, Bo Pang, Congying Xia, Chen Xing, Jesse Vig, Semih Yavuz, Philippe Laban, et al. 2023. Long sequence modeling with xgen: A 7b llm trained on 8k input sequence length. Salesforce AI Research Blog.
- Cited in 04_experiments.md for the XGen-7B-8k model

### NLPCC (2014)
NLPCC. 2014. Task definition for large scale text categorization at nlpcc 2014.
- Cited in 03_longbench-task-and-construction.md as source for the LSHT dataset

## O

### OpenAI (2022a)
OpenAI. 2022a. Introducing chatgpt.
- Cited in 04_experiments.md for GPT-3.5-Turbo-16k model

### OpenAI (2022b)
OpenAI. 2022b. Openai: New and improved embedding model.
- Cited in 04_experiments.md for text-embedding-ada-002 retriever

### Orvieto et al. (2023)
Antonio Orvieto, Samuel L Smith, Albert Gu, Anushan Fernando, Caglar Gulcehre, Razvan Pascanu, and Soham De. 2023. Resurrecting recurrent neural networks for long sequences. *arXiv preprint arXiv:2303.06349*.
- Cited in 02_related-work.md as recurrent/memory module approach

## P

### Press et al. (2022)
Ofir Press, Noah Smith, and Mike Lewis. 2022. Train short, test long: Attention with linear biases enables input length extrapolation. In *International Conference on Learning Representations*.
- Cited in 01_introduction.md and 02_related-work.md as length extrapolation method

## R

### Rae et al. (2020)
Jack W Rae, Anna Potapenko, Siddhant M Jayakumar, Chloe Hillier, and Timothy P Lillicrap. 2020. Compressive transformers for long-range sequence modelling. In *International Conference on Learning Representations*.
- Cited in 02_related-work.md as recurrent/memory module approach

### Raffel et al. (2020)
Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, and Peter J Liu. 2020. Exploring the limits of transfer learning with a unified text-to-text transformer. *The Journal of Machine Learning Research*, 21(1):5485-5551.
- Cited in 03_longbench-task-and-construction.md for C4 dataset used in PassageRetrieval-zh

### Roy et al. (2021)
Aurko Roy, Mohammad Saffar, Ashish Vaswani, and David Grangier. 2021. Efficient content-based sparse attention with routing transformers. *Transactions of the Association for Computational Linguistics*, 9:53-68.
- Cited in 02_related-work.md regarding perplexity-based evaluation

## S

### Shaham et al. (2022)
Uri Shaham, Elad Segal, Maor Ivgi, Avia Efrat, Ori Yoran, Adi Haviv, Ankit Gupta, Wenhan Xiong, Mor Geva, Jonathan Berant, et al. 2022. Scrolls: Standardized comparison over long language sequences. In *Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing*, pages 12007-12021.
- Cited in 02_related-work.md as concurrent evaluation benchmark (SCROLLS)

### Shaham et al. (2023)
Uri Shaham, Maor Ivgi, Avia Efrat, Jonathan Berant, and Omer Levy. 2023. Zeroscrolls: A zero-shot benchmark for long text understanding. *arXiv preprint arXiv:2305.14196*.
- Cited in 02_related-work.md as concurrent evaluation benchmark (ZeroSCROLLS); in 10_appendix-c-radar-plot.md as previous benchmark that averaged over all tasks

### Srivastava et al. (2023)
Aarohi Srivastava, Abhinav Rastogi, Abhishek Rao, Abu Awal Md Shoeb, Abubakar Abid, Adam Fisch, Adam R Brown, Adam Santoro, Aditya Gupta, Adrià Garriga-Alonso, et al. 2023. Beyond the imitation game: Quantifying and extrapolating the capabilities of language models. *Transactions on Machine Learning Research*.
- Cited in 01_introduction.md as example of short-context multi-task benchmark

### Sun et al. (2021)
Simeng Sun, Kalpesh Krishna, Andrew Mattarella-Micke, and Mohit Iyyer. 2021. Do long-range language models actually use long-range context? In *Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing*, pages 807-822.
- Cited in 02_related-work.md noting that perplexity may not reflect sequence-level task performance

### Sun et al. (2022)
Yutao Sun, Li Dong, Barun Patra, Shuming Ma, Shaohan Huang, Alon Benhaim, Vishrav Chaudhary, Xia Song, and Furu Wei. 2022. A length-extrapolatable transformer. *arXiv preprint arXiv:2212.10554*.
- Cited in 02_related-work.md as length extrapolation method

### Svyatkovskiy et al. (2020)
Alexey Svyatkovskiy, Shao Kun Deng, Shengyu Fu, and Neel Sundaresan. 2020. Intellicode compose: Code generation using transformer. In *Proceedings of the 28th ACM Joint Meeting on European Software Engineering Conference and Symposium on the Foundations of Software Engineering*, pages 1433-1443.
- Cited in 04_experiments.md as source for Edit Sim (Levenshtein distance) metric for code generation evaluation

## T

### Tay et al. (2021)
Yi Tay, Mostafa Dehghani, Samira Abnar, Yikang Shen, Dara Bahri, Philip Pham, Jinfeng Rao, Liu Yang, Sebastian Ruder, and Donald Metzler. 2021. Long range arena: A benchmark for efficient transformers. In *International Conference on Learning Representations*.
- Cited in 02_related-work.md regarding artificial retrieval tasks

### Tay et al. (2022)
Yi Tay, Mostafa Dehghani, Dara Bahri, and Donald Metzler. 2022. Efficient transformers: A survey. *ACM Comput. Surv.*, 55(6).
- Cited in 02_related-work.md as survey of efficient transformers

### Team (2023)
InternLM Team. 2023. Internlm: A multilingual language model with progressively enhanced capabilities. https://github.com/InternLM/InternLM.
- Cited in 04_experiments.md for the InternLM-7B-8k model

### Touvron et al. (2023)
Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, et al. 2023. Llama 2: Open foundation and fine-tuned chat models. *arXiv preprint arXiv:2307.09288*.
- Cited in 04_experiments.md for Llama2-7B-chat-4k model

### Trivedi et al. (2022)
Harsh Trivedi, Niranjan Balasubramanian, Tushar Khot, and Ashish Sabharwal. 2022. MuSiQue: Multihop questions via single-hop question composition. *Transactions of the Association for Computational Linguistics*, 10:539-554.
- Cited in 03_longbench-task-and-construction.md as source for the MuSiQue dataset

## W

### Wang et al. (2020)
Sinong Wang, Belinda Z Li, Madian Khabsa, Han Fang, and Hao Ma. 2020. Linformer: Self-attention with linear complexity. *arXiv preprint arXiv:2006.04768*.
- Cited in 02_related-work.md as sparse/efficient computation approach

### Wu et al. (2022)
Yuhuai Wu, Markus Norman Rabe, DeLesley Hutchins, and Christian Szegedy. 2022. Memorizing transformers. In *International Conference on Learning Representations*.
- Cited in 02_related-work.md as recurrent/memory module approach

### Wu et al. (2023)
Han Wu, Mingjie Zhan, Haochen Tan, Zhaohui Hou, Ding Liang, and Linqi Song. 2023. VCSUM: A versatile Chinese meeting summarization dataset. In *Findings of the Association for Computational Linguistics: ACL 2023*, pages 6065-6079.
- Cited in 03_longbench-task-and-construction.md as source for the VCSUM dataset

## Y

### Yang et al. (2018)
Zhilin Yang, Peng Qi, Saizheng Zhang, Yoshua Bengio, William Cohen, Ruslan Salakhutdinov, and Christopher D Manning. 2018. Hotpotqa: A dataset for diverse, explainable multi-hop question answering. In *Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing*, pages 2369-2380.
- Cited in 03_longbench-task-and-construction.md as source for the HotpotQA dataset

### Yu et al. (2024)
Jifan Yu, Xiaozhi Wang, Shangqing Tu, Shulin Cao, Daniel Zhang-Li, Xin Lv, Hao Peng, Zijun Yao, Xiaohan Zhang, Hanming Li, et al. 2024. Kola: Carefully benchmarking world knowledge of large language models. In *The Twelfth International Conference on Learning Representations*.
- Cited in 04_experiments.md regarding the delta score addressing the memorization phenomenon

## Z

### Zaheer et al. (2020)
Manzil Zaheer, Guru Guruganesh, Kumar Avinava Dubey, Joshua Ainslie, Chris Alberti, Santiago Ontanon, Philip Pham, Anirudh Ravula, Qifan Wang, Li Yang, et al. 2020. Big bird: Transformers for longer sequences. *Advances in neural information processing systems*, 33:17283-17297.
- Cited in 02_related-work.md as sparse/efficient computation approach

### Zeng et al. (2023)
Aohan Zeng, Xiao Liu, Zhengxiao Du, Zihan Wang, Hanyu Lai, Ming Ding, Zhuoyi Yang, Yifan Xu, Wendi Zheng, Xiao Xia, et al. 2023. Glm-130b: An open bilingual pre-trained model. In *The Eleventh International Conference on Learning Representations*.
- Cited in 02_related-work.md for ChatGLM2-32k; in 04_experiments.md for ChatGLM2-6B model

### Zheng et al. (2023a)
Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric Xing, et al. 2023a. Judging llm-as-a-judge with mt-bench and chatbot arena. *arXiv preprint arXiv:2306.05685*.
- Cited in 04_experiments.md for Vicuna-v1.5-7B-16k model; in 06_limitations.md regarding LLM bias as evaluation metric

### Zhong et al. (2021)
Ming Zhong, Da Yin, Tao Yu, Ahmad Zaidi, Mutethia Mutuma, Rahul Jha, Ahmed Hassan, Asli Celikyilmaz, Yang Liu, Xipeng Qiu, et al. 2021. Qmsum: A new benchmark for query-based multi-domain meeting summarization. In *Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies*, pages 5905-5921.
- Cited in 03_longbench-task-and-construction.md as source for the QMSum dataset

### Zhou et al. (2023)
Wangchunshu Zhou, Yuchen Eleanor Jiang, Peng Cui, Tiannan Wang, Zhenxin Xiao, Yifan Hou, Ryan Cotterell, and Mrinmaya Sachan. 2023. Recurrentgpt: Interactive generation of (arbitrarily) long text. *arXiv preprint arXiv:2305.13304*.
- Cited in 01_introduction.md and 02_related-work.md as external memory augmentation approach
