# References

This file contains bibliographic information for works cited in the section notes.

## An et al. (2024)
Shengnan An, Zexiong Ma, Zeqi Lin, Nanning Zheng, and Jian-Guang Lou. 2024. Make your llm fully utilize the context. arXiv preprint arXiv:2404.16811.
- Cited in: 01_introduction.md as a mitigation strategy for "Lost in the Middle" via extended training with long-context tasks

## Chen et al. (2023)
Yukang Chen, Shengju Qian, Haotian Tang, Xin Lai, Zhijian Liu, Song Han, and Jiaya Jia. 2023. Longlora: Efficient fine-tuning of long-context large language models. arXiv preprint arXiv:2309.12307.
- Cited in: 03_experiments.md as the basis for Llama-2-7b-longlora-8k-ft model

## Dao et al. (2023)
Tri Dao. 2023. Flashattention-2: Faster attention with better parallelism and work partitioning. arXiv preprint arXiv:2307.08691.
- Cited in: 01_introduction.md as advancement enabling larger context sizes

## Dao et al. (2022)
Tri Dao, Dan Fu, Stefano Ermon, Atri Rudra, and Christopher Ré. 2022. Flashattention: Fast and memory-efficient exact attention with io-awareness. Advances in Neural Information Processing Systems, 35:16344–16359.
- Related to Flash Attention mechanism mentioned in introduction

## Feng et al. (2023)
Shangbin Feng, Vidhisha Balachandran, Yuyang Bai, and Yulia Tsvetkov. 2023. FactKB: Generalizable factuality evaluation using language models enhanced with factual knowledge. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, pages 933–952, Singapore. Association for Computational Linguistics.
- Cited in: 02_related-work.md in context of multi-hop QA requiring parametric knowledge

## Guo et al. (2022)
Wangzhen Guo, Qinkang Gong, and Hanjiang Lai. 2022. Counterfactual multihop qa: A cause-effect approach for reducing disconnected reasoning.
- Cited in: 02_related-work.md discussing challenges in multi-hop QA performance and factual accuracy

## Hermann et al. (2015)
Karl Moritz Hermann, Tomas Kocisky, Edward Grefenstette, Lasse Espeholt, Will Kay, Mustafa Suleyman, and Phil Blunsom. 2015. Teaching machines to read and comprehend. Advances in neural information processing systems, 28.
- Cited in: 03_experiments.md as the CNN/DailyMail dataset used for BART fine-tuning

## Izacard and Grave (2020)
Gautier Izacard and Edouard Grave. 2020. Leveraging passage retrieval with generative models for open domain question answering. CoRR, abs/2007.01282.
- Cited in: 01_introduction.md describing earlier RAG systems that processed documents independently

## Kandpal et al. (2023)
Nikhil Kandpal, Haikang Deng, Adam Roberts, Eric Wallace, and Colin Raffel. 2023. Large language models struggle to learn long-tail knowledge. In International Conference on Machine Learning, pages 15696–15707. PMLR.
- Cited in: 03_experiments.md for best-subspan accuracy metric

## Kim et al. (2024)
Jaehyung Kim, Jaehyun Nam, Sangwoo Mo, Jongjin Park, Sang-Woo Lee, Minjoon Seo, Jung-Woo Ha, and Jinwoo Shin. 2024. Sure: Improving open-domain question answering of llms via summarized retrieval. In The Twelfth International Conference on Learning Representations.
- Cited in: 01_introduction.md as mitigation via document length reduction through summarization

## Kwiatkowski et al. (2019)
Tom Kwiatkowski, Jennimaria Palomaki, Olivia Redfield, Michael Collins, Ankur Parikh, Chris Alberti, Danielle Epstein, Illia Polosukhin, Jacob Devlin, Kenton Lee, Kristina Toutanova, Llion Jones, Matthew Kelcey, Ming-Wei Chang, Andrew M. Dai, Jakob Uszkoreit, Quoc Le, and Slav Petrov. 2019. Natural questions: A benchmark for question answering research. Transactions of the Association for Computational Linguistics, 7:452–466.
- Cited in: 02_related-work.md as the NaturalQuestions-Open dataset used by Liu et al. (2024)

## Lee et al. (2021)
Kyungjae Lee, Seung won Hwang, Sang eun Han, and Dohyeon Lee. 2021. Robustifying multi-hop qa through pseudo-evidentiality training.
- Cited in: 02_related-work.md in context of multi-hop QA requiring parametric knowledge

## Levy et al. (2024)
Mosh Levy, Alon Jacoby, and Yoav Goldberg. 2024. Same task, more tokens: the impact of input length on the reasoning performance of large language models. arXiv preprint arXiv:2402.14848.
- Cited in: 02_related-work.md as concurrent work examining LLM performance degradation with input length

## Lewis et al. (2019)
Mike Lewis, Yinhan Liu, Naman Goyal, Marjan Ghazvininejad, Abdelrahman Mohamed, Omer Levy, Veselin Stoyanov, and Luke Zettlemoyer. 2019. BART: Denoising sequence-to-sequence pre-training for natural language generation, translation, and comprehension. CoRR, abs/1910.13461.
- Cited in: 03_experiments.md as BART-large-CNN model used for summarization

## Liu et al. (2024)
Nelson F Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, and Percy Liang. 2024. Lost in the middle: How language models use long contexts. Transactions of the Association for Computational Linguistics, 12:157–173.
- Cited extensively throughout: 01_introduction.md, 02_related-work.md, 03_experiments.md, 04_methodology.md as the foundational work identifying the "Lost in the Middle" problem

## Mavi et al. (2024)
Vaibhav Mavi, Anubhav Jangra, and Adam Jatowt. 2024. Multi-hop question answering.
- Cited in: 02_related-work.md discussing multi-hop QA tasks

## Mallen et al. (2022)
Alex Mallen, Akari Asai, Victor Zhong, Rajarshi Das, Daniel Khashabi, and Hannaneh Hajishirzi. 2022. When not to trust language models: Investigating effectiveness of parametric and non-parametric memories. arXiv preprint arXiv:2212.10511.
- Cited in: 03_experiments.md for best-subspan accuracy metric

## Peysakhovich and Lerer (2023)
Alexander Peysakhovich and Adam Lerer. 2023. Attention sorting combats recency bias in long context language models.
- Cited in: 01_introduction.md and 02_related-work.md as mitigation strategy via document re-ranking based on attention scores

## Pezeshkpour (2023)
Pouya Pezeshkpour. 2023. Measuring and modifying factual knowledge in large language models.
- Cited in: 02_related-work.md discussing challenges in multi-hop QA accuracy

## Press et al. (2022)
Ofir Press, Noah Smith, and Mike Lewis. 2022. Train short, test long: Attention with linear biases enables input length extrapolation. In International Conference on Learning Representations.
- Cited in: 01_introduction.md and 03_experiments.md regarding ALiBi attention mechanism used in MPT-7b-8k-instruct

## Saxena et al. (2020)
Apoorv Saxena, Aditay Tripathi, and Partha Talukdar. 2020. Improving multi-hop question answering over knowledge graphs using knowledge base embeddings. In Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, pages 4498–4507, Online. Association for Computational Linguistics.
- Cited in: 02_related-work.md discussing multi-hop QA tasks

## Shaier et al. (2023a)
Sagi Shaier, Kevin Bennett, Lawrence Hunter, and Katharina von der Wense. 2023a. Emerging practices for demographic reporting in personalized medicine: Assessing demographic effects to biomedical question answering systems. In Proceedings of the 13th International Joint Conference on Natural Language Processing and the 3rd Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics (Volume 1: Long Papers), pages 540–550, Nusa Dua, Bali. Association for Computational Linguistics.
- Cited in: 02_related-work.md in context of combining parametric knowledge with external context

## Shaier et al. (2023b)
Sagi Shaier, Lawrence Hunter, and Katharina Kann. 2023b. Who are all the stochastic parrots imitating? they should tell us! In Proceedings of the 17th Conference of the European Chapter of the Association for Computational Linguistics (Volume 2: Short Papers), pages 105–120, Nusa Dua, Bali. Association for Computational Linguistics.
- Cited in: 02_related-work.md discussing reduction in accuracy in multi-hop reasoning

## Shaier et al. (2024a)
Sagi Shaier, Kevin Bennett, Lawrence Hunter, and Katharina von der Wense. 2024a. Comparing template-based and template-free language model probing. In Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1: Long Papers), pages 766–776, St. Julian's, Malta. Association for Computational Linguistics.
- Cited in: 02_related-work.md in context of combining parametric knowledge with external context

## Shaier et al. (2024b)
Sagi Shaier, Lawrence Hunter, and Katharina Wense. 2024b. Desiderata for the context use of question answering systems. In Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1: Long Papers), pages 777–792, St. Julian's, Malta. Association for Computational Linguistics.
- Cited in: 02_related-work.md discussing inconsistent utilization of relevant information

## Shaier et al. (2024c)
Sagi Shaier, Lawrence Hunter, and Katharina Wense. 2024c. It is not about what you say, it is about how you say it: A surprisingly simple approach for improving reading comprehension. In Findings of the Association for Computational Linguistics: ACL 2024, pages 8292–8305, Bangkok, Thailand. Association for Computational Linguistics.
- Cited in: 02_related-work.md discussing models' inability to utilize information consistently

## Shaier et al. (2024d)
Sagi Shaier, Ari Kobren, and Philip V. Ogren. 2024d. Adaptive question answering: Enhancing language model proficiency for addressing knowledge conflicts in QA. In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, pages 17226–17239, Miami, Florida, USA. Association for Computational Linguistics.
- Cited in: 01_introduction.md discussing likelihood of overlooking critical information as input volume increases

## Su et al. (2024)
Xin Su, Tiep Le, Steven Bethard, and Phillip Howard. 2024. Semi-structured thought: Integrating multiple sources of knowledge for improved language model reasoning. In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, pages 19519–19529, Miami, Florida, USA. Association for Computational Linguistics.
- Cited in: 02_related-work.md discussing multi-hop QA requiring parametric knowledge and challenges with information utilization

## Tang et al. (2023)
Raphael Tang, Xinyu Zhang, Xueguang Ma, Jimmy Lin, and Ferhan Ture. 2023. Found in the middle: Permutation self-consistency improves listwise ranking in large language models.
- Cited in: 01_introduction.md and 02_related-work.md as mitigation strategy via document re-ranking with permutation self-consistency

## Touvron et al. (2023)
Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, et al. 2023. Llama 2: Open foundation and fine-tuned chat models. arXiv preprint arXiv:2307.09288.
- Cited in: 03_experiments.md as base model for Llama-2-7b-longlora-8k-ft and for knowledge graph extraction

## Trivedi et al. (2020)
Harsh Trivedi, Niranjan Balasubramanian, Tushar Khot, and Ashish Sabharwal. 2020. Is multihop QA in DiRe condition? measuring and reducing disconnected reasoning. In Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP), pages 8846–8863, Online. Association for Computational Linguistics.
- Cited in: 02_related-work.md discussing multi-hop QA requiring parametric knowledge and challenges with information utilization

## Wang et al. (2023)
Cunxiang Wang, Xiaoze Liu, Yuanhao Yue, Xiangru Tang, Tianhang Zhang, Chengqiang Jia, Yue Zhang, Guangliang Cheng, Wentao Yao, Weiqi Wang, Linyi Yang, Jindong Wang, Xing Xie, Zheng Zhang, and Yue Zhang. 2023. Survey on factuality in large language models: Knowledge, retrieval, and domain-specificity.
- Cited in: 02_related-work.md discussing factual accuracy challenges in multi-hop reasoning

## Wang et al. (2024)
Yuxia Wang, Minghan Wang, Muhammad Arslan Manzoor, Fei Liu, Georgi Nenkov Georgiev, Rocktim Jyoti Das, Preslav Nakov, and Preslav Nakov. 2024. Factuality of large language models: A survey. In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, pages 19519–19529, Miami, Florida, USA. Association for Computational Linguistics.
- Cited in: 02_related-work.md discussing factual accuracy challenges in multi-hop reasoning

## Yang et al. (2018)
Zhilin Yang, Peng Qi, Saizheng Zhang, Yoshua Bengio, William Cohen, Ruslan Salakhutdinov, and Christopher D. Manning. 2018. HotpotQA: A dataset for diverse, explainable multi-hop question answering. In Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing, pages 2369–2380, Brussels, Belgium. Association for Computational Linguistics.
- Cited in: 02_related-work.md as foundational work on multi-hop QA tasks; also as HotpotQA dataset in 03_experiments.md

## Zhou et al. (2023)
Denny Zhou, Nathanael Schärli, Le Hou, Jason Wei, Nathan Scales, Xuezhi Wang, Dale Schuurmans, Claire Cui, Olivier Bousquet, Quoc Le, and Ed Chi. 2023. Least-to-most prompting enables complex reasoning in large language models.
- Cited in: 01_introduction.md as chain-of-thought (CoT) prompting technique used to tackle the problem
