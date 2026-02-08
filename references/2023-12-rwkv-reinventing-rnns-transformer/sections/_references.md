# References

Only references cited in the section notes are included.

---

**Albalak et al. (2022)**
Alon Albalak, Yi-Lin Tuan, Pegah Jandaghi, Connor Pryor, Luke Yoffe, Deepak Ramachandran, Lise Getoor, Jay Pujara, and William Yang Wang. 2022. FETA: A benchmark for few-sample task transfer in open-domain dialogue. In *Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing*, pages 10936-10953. Association for Computational Linguistics.
- Cited in 01_introduction.md as an example of sequential data processing tasks.

**Anand et al. (2023)**
Yuvanesh Anand, Zach Nussbaum, Brandon Duderstadt, Benjamin Schmidt, and Andriy Mulyar. 2023. Gpt4all: Training an assistant-style chatbot with large scale data distillation from gpt-3.5-turbo. https://github.com/nomic-ai/gpt4all.
- Cited in 10_ethics-statement.md as publicly available instructions used for fine-tuning.

**Anonymous (2023)**
Anonymous. 2023. Sharegpt_vicuna_unfiltered.
- Cited in 10_ethics-statement.md as publicly available instructions used for fine-tuning.

**Ba et al. (2016)**
Jimmy Lei Ba, Jamie Ryan Kiros, and Geoffrey E. Hinton. 2016. Layer normalization.
- Cited in 03_rwkv.md for layer normalization used in the architecture.

**Biderman et al. (2022)**
Stella Biderman, Kieran Bicheno, and Leo Gao. 2022. Datasheet for the pile. *arXiv preprint arXiv:2201.07311*.
- Cited in 01_introduction.md, 04_trained-models-and-computing-costs.md, and 10_ethics-statement.md for the Pile training dataset.

**Biderman et al. (2023a)**
Stella Biderman, USVSN Sai Prashanth, Lintang Sutawika, Hailey Schoelkopf, Quentin Anthony, Shivanshu Purohit, and Edward Raf. 2023a. Emergent and predictable memorization in large language models. *arXiv preprint arXiv:2304.11158*.
- Cited in 04_trained-models-and-computing-costs.md for contexts where scaling laws fail providing feedback.

**Biderman et al. (2023b)**
Stella Biderman, Hailey Schoelkopf, Quentin Anthony, Herbie Bradley, Kyle O'Brien, Eric Hallahan, Mohammad Aflah Khan, Shivanshu Purohit, USVSN Sai Prashanth, Edward Raff, et al. 2023b. Pythia: A suite for analyzing large language models across training and scaling. *arXiv preprint arXiv:2304.01373*.
- Cited in 05_evaluations.md as a baseline model family (Pythia) for NLP evaluations; in 22_appendix-k-inference-results.md for the Pythia inference benchmark family.

**Bisk et al. (2020)**
Yonatan Bisk, Rowan Zellers, Ronan Le Bras, Jianfeng Gao, and Yejin Choi. 2020. Piqa: Reasoning about physical commonsense in natural language. In *Thirty-Fourth AAAI Conference on Artificial Intelligence*.
- Cited in 05_evaluations.md and 21_appendix-j-additional-evaluations.md as the PIQA benchmark.

**Black et al. (2022)**
Sidney Black, Stella Biderman, Eric Hallahan, Quentin Anthony, Leo Gao, Laurence Golding, Horace He, Connor Leahy, Kyle McDonell, Jason Phang, et al. 2022. Gpt-neox-20b: An open-source autoregressive language model. In *Proceedings of BigScience Episode #5 -- Workshop on Challenges & Perspectives in Creating Large Language Models*, pages 95-136.
- Cited in 04_trained-models-and-computing-costs.md for scaling law interpolation and extrapolation.

**Bradbury et al. (2017)**
James Bradbury, Stephen Merity, Caiming Xiong, and Richard Socher. 2017. Quasi-recurrent neural networks. In *ICLR*.
- Cited in 02_background.md for noting that RNNs can be factored into two linear blocks; in 14_appendix-c-additional-related-work.md for the QRNN as most similar prior work to RWKV.

**Brown et al. (2020)**
Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. 2020. Language models are few-shot learners. *Advances in neural information processing systems*, 33:1877-1901.
- Cited in 01_introduction.md as GPT-3 and as an example of sequential data processing; in 21_appendix-j-additional-evaluations.md for the untokenized LAMBADA version.

**Chaudhary (2023)**
Sahil Chaudhary. 2023. Code alpaca: An instruction-following llama model for code generation. https://github.com/sahil280114/codealpaca.
- Cited in 10_ethics-statement.md as publicly available instructions used for fine-tuning.

**Cheung (2023)**
Joseph Cheung. 2023. Guanacodataset.
- Cited in 10_ethics-statement.md as publicly available instructions used for fine-tuning.

**Chowdhery et al. (2022)**
Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung, Charles Sutton, Sebastian Gehrmann, Parker Schuh, Kensen Shi, et al. 2022. Palm: Scaling language modeling with pathways. *CoRR*, abs/2204.02311.
- Cited in 04_trained-models-and-computing-costs.md for the auxiliary loss introduced by PaLM.

**Chung et al. (2014)**
Junyoung Chung, Caglar Gulcehre, KyungHyun Cho, and Yoshua Bengio. 2014. Empirical evaluation of gated recurrent neural networks on sequence modeling. In *NIPS 2014 Deep Learning and Representation Learning Workshop*.
- Cited in 02_background.md for GRU as a popular RNN architecture; in 14_appendix-c-additional-related-work.md for RNN-style recursive components.

**Clark et al. (2018)**
Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar Khot, Ashish Sabharwal, Carissa Schoenick, and Oyvind Tafjord. 2018. Think you have solved question answering? try arc, the ai2 reasoning challenge. In *arXiv:1803.05457*.
- Cited in 05_evaluations.md and 21_appendix-j-additional-evaluations.md as the ARC benchmark.

**Clark et al. (2019)**
Christopher Clark, Kenton Lee, Ming-Wei Chang, Tom Kwiatkowski, Michael Collins, and Kristina Toutanova. 2019. Boolq: Exploring the surprising difficulty of natural yes/no questions. *arXiv preprint arXiv:1905.10044*.
- Cited in 05_evaluations.md and 21_appendix-j-additional-evaluations.md as the BoolQ benchmark.

**Dao et al. (2022a)**
Tri Dao, Daniel Y Fu, Stefano Ermon, Atri Rudra, and Christopher Re. 2022a. FlashAttention: Fast and memory-efficient exact attention with IO-awareness. In *Advances in Neural Information Processing Systems*.
- Cited in 01_introduction.md for research to enhance Transformers' scalability; in 14_appendix-c-additional-related-work.md for FlashAttention sharing similarities with RWKV's chunked computation.

**Gao et al. (2020)**
Leo Gao, Stella Biderman, Sid Black, Laurence Golding, Travis Hoppe, Charles Foster, Jason Phang, Horace He, Anish Thite, Noa Nabeshima, et al. 2020. The pile: An 800gb dataset of diverse text for language modeling. *arXiv preprint arXiv:2101.00027*.
- Cited in 01_introduction.md, 04_trained-models-and-computing-costs.md, 05_evaluations.md (Figure 6), and 10_ethics-statement.md for the Pile training dataset.

**He et al. (2016)**
Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. 2016. Identity mappings in deep residual networks.
- Cited in 03_rwkv.md for custom initialization principles.

**Henighan et al. (2020)**
Tom Henighan, Jared Kaplan, Mor Katz, Mark Chen, Christopher Hesse, Jacob Jackson, Heewoo Jun, Tom B Brown, Prafulla Dhariwal, Scott Gray, et al. 2020. Scaling laws for autoregressive generative modeling. *arXiv preprint arXiv:2010.14701*.
- Cited in 04_trained-models-and-computing-costs.md for scaling laws.

**Hochreiter (1998)**
Sepp Hochreiter. 1998. The vanishing gradient problem during learning recurrent neural nets and problem solutions. *International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems*, 6(02):107-116.
- Cited in 01_introduction.md for the vanishing gradient problem in RNNs.

**Hochreiter and Schmidhuber (1997)**
Sepp Hochreiter and Jurgen Schmidhuber. 1997. Long short-term memory. *Neural Computation*, 9(8):1735-1780.
- Cited in 02_background.md for LSTM as a popular RNN architecture; in 14_appendix-c-additional-related-work.md for RNN-style recursive components.

**Hoffmann et al. (2022)**
Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, Tom Hennigan, Eric Noland, Katie Millican, George van den Driessche, Bogdan Damoc, Aurelia Guy, Simon Osindero, Karen Simonyan, Erich Elsen, Jack W. Rae, Oriol Vinyals, and Laurent Sifre. 2022. Training compute-optimal large language models.
- Cited in 01_introduction.md for Chinchilla, 04_trained-models-and-computing-costs.md for scaling laws, and 05_evaluations.md for the Chinchilla-optimal regime.

**Ismail Fawaz et al. (2019)**
Hassan Ismail Fawaz, Germain Forestier, Jonathan Weber, Lhassane Idoumghar, and Pierre-Alain Muller. 2019. Deep learning for time series classification: a review. *Data mining and knowledge discovery*, 33(4):917-963.
- Cited in 01_introduction.md for time-series analysis as a sequential data task.

**Ji et al. (2023a)**
Yunjie Ji, Yong Deng, Yan Gong, Yiping Peng, Qiang Niu, Baochang Ma, and Xiangang Li. 2023a. Belle: Be everyone's large language model engine. https://github.com/LianjiaTech/BELLE.
- Cited in 10_ethics-statement.md as publicly available instructions used for fine-tuning.

**Ji et al. (2023b)**
Yunjie Ji, Yong Deng, Yan Gong, Yiping Peng, Qiang Niu, Lei Zhang, Baochang Ma, and Xiangang Li. 2023b. Exploring the impact of instruction data scaling on large language models: An empirical study on real-world use cases. *arXiv preprint arXiv:2303.14742*.
- Cited in 10_ethics-statement.md as publicly available instructions used for fine-tuning.

**Johannes Welbl Nelson F. Liu (2017)**
Matt Gardner Johannes Welbl Nelson F. Liu. 2017. Crowdsourcing multiple choice science questions. In *DOI:10.18653/v1/W17-4413*.
- Cited in 05_evaluations.md and 21_appendix-j-additional-evaluations.md as the SciQ benchmark.

**Jumper et al. (2021)**
John Jumper, Richard Evans, Alexander Pritzel, Tim Green, Michael Figurnov, Olaf Ronneberger, Kathryn Tunyasuvunakool, Russ Bates, Augustin Zidek, Anna Potapenko, et al. 2021. Highly accurate protein structure prediction with alphafold. *Nature*, 596(7873):583-589.
- Cited in 03_rwkv.md for custom initialization principles.

**Kaplan et al. (2020)**
Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jeffrey Wu, and Dario Amodei. 2020. Scaling laws for neural language models. *arXiv preprint arXiv:2001.08361*.
- Cited in 04_trained-models-and-computing-costs.md for scaling laws and the FLOP calculation formula; also for the claim that LSTMs do not follow the same log-log linear scaling as transformers.

**Katharopoulos et al. (2020)**
Angelos Katharopoulos, Apoorv Vyas, Nikolaos Pappas, and Francois Fleuret. 2020. Transformers are rnns: Fast autoregressive transformers with linear attention. In *International Conference on Machine Learning*, pages 5156-5165. PMLR.
- Cited in 01_introduction.md for linear scaling / memory bottleneck alleviation; in 14_appendix-c-additional-related-work.md as an efficient attention method; in 21_appendix-j-additional-evaluations.md as a baseline for Enwik8 perplexity (J.3).

**Kocon et al. (2023)**
Jan Kocon, Igor Cichecki, Oliwier Kaszyca, Mateusz Kochanek, Dominika Szydlo, Joanna Baran, Julita Bielaniewicz, Marcin Gruza, Arkadiusz Janz, Kamil Kanclerz, Anna Kocon, Bartlomiej Koptyra, Wiktoria Mieleszczenko-Kowszewicz, Piotr Milkowski, Marcin Oleksy, Maciej Piasecki, Lukasz Radlinski, Konrad Wojtasik, Stanislaw Wozniak, and Przemyslaw Kazienko. 2023. Chatgpt: Jack of all trades, master of none. *Information Fusion*, page 101861.
- Cited in 01_introduction.md for ChatGPT; in 23_appendix-l-prompt-construction.md as inspiration for the prompt comparison experiments and as source of ChatGPT prompts used for RWKV evaluation (Tables 6 and 7), and for chain-of-thought experiments on MathQA.

**Le and Zuidema (2016)**
Phong Le and Willem Zuidema. 2016. Quantifying the vanishing gradient and long distance dependency problem in recursive neural networks and recursive lstms. In *Proceedings of the 1st Workshop on Representation Learning for NLP*, pages 87-93.
- Cited in 01_introduction.md for the vanishing gradient problem limiting RNN scalability.

**Le Scao et al. (2022)**
Teven Le Scao, Angela Fan, Christopher Akiki, Ellie Pavlick, Suzana Ilic, Daniel Hesslow, Roman Castagné, Alexandra Sasha Luccioni, Francois Yvon, Matthias Gallé, et al. 2022. Bloom: A 176b-parameter open-access multilingual language model. *arXiv preprint arXiv:2211.05100*.
- Cited in 04_trained-models-and-computing-costs.md for scaling law interpolation and extrapolation.

**Lei et al. (2018)**
Tao Lei, Yu Zhang, Sida I. Wang, Hui Dai, and Yoav Artzi. 2018. Simple recurrent units for highly parallelizable recurrence. In *Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing*, pages 4470-4481. Association for Computational Linguistics.
- Cited in 03_rwkv.md for parallelization of element-wise WKV computation.

**Mihaylov et al. (2018)**
Todor Mihaylov, Peter Clark, Tushar Khot, and Ashish Sabharwal. 2018. Can a suit of armor conduct electricity? a new dataset for open book question answering. In *EMNLP*.
- Cited in 05_evaluations.md and 21_appendix-j-additional-evaluations.md as the OpenBookQA benchmark.

**Muennighoff et al. (2023)**
Niklas Muennighoff, Alexander M Rush, Boaz Barak, Teven Le Scao, Aleksandra Piktus, Nouamane Tazi, Sampo Pyysalo, Thomas Wolf, and Colin Raffel. 2023. Scaling data-constrained language models. *arXiv preprint arXiv:2305.16264*.
- Cited in 04_trained-models-and-computing-costs.md for scaling laws.

**OpenAI (2022)**
OpenAI. 2022. Introducing chatgpt. https://openai.com/blog/chatgpt.
- Cited in 01_introduction.md for ChatGPT.

**Paperno et al. (2016)**
Denis Paperno, German Kruszewski, Angeliki Lazaridou, Ngoc Quan Pham, Raffaella Bernardi, Sandro Pezzelle, Marco Baroni, Gemma Boleda, and Raquel Fernandez. 2016. The LAMBADA dataset: Word prediction requiring a broad discourse context. In *Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 1525-1534. Association for Computational Linguistics.
- Cited in 05_evaluations.md and 21_appendix-j-additional-evaluations.md as the LAMBADA benchmark.

**Paszke et al. (2019)**
Adam Paszke, Sam Gross, Francisco Massa, Adam Lerer, James Bradbury, Gregory Chanan, Trevor Killeen, Zeming Lin, Natalia Gimelshein, Luca Antiga, Alban Desmaison, Andreas Kopf, Edward Yang, Zach DeVito, Martin Raison, Alykhan Tejani, Sasank Chilamkurthy, Benoit Steiner, Lu Fang, Junjie Bai, and Soumith Chintala. 2019. Pytorch: An imperative style, high-performance deep learning library.
- Cited in 03_rwkv.md for PyTorch implementation of token shift and overall implementation.

**Rasley et al. (2020)**
Jeff Rasley, Samyam Rajbhandari, Olatunji Ruwase, and Yuxiong He. 2020. Deepspeed: System optimizations enable training deep learning models with over 100 billion parameters. In *Proceedings of the 26th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining*, KDD '20, page 3505-3506. Association for Computing Machinery.
- Cited in 03_rwkv.md for DeepSpeed optimization strategies.

**Roemmele et al. (2018)**
Melissa Roemmele, Cosmin Adrian Bejan, and Andrew S. Gordon. 2018. Choice of plausible alternatives: An evaluation of commonsense causal reasoning. In *AAAI*.
- Cited in 05_evaluations.md and 21_appendix-j-additional-evaluations.md as the COPA benchmark.

**Scao et al. (2022)**
Teven Le Scao, Angela Fan, Christopher Akiki, Ellie Pavlick, Suzana Ilic, Daniel Hesslow, Roman Castagné, Alexandra Sasha Luccioni, Francois Yvon, Matthias Gallé, et al. 2022. Bloom: A 176b-parameter open-access multilingual language model. *arXiv preprint arXiv:2211.05100*.
- Cited in 05_evaluations.md as the BLOOM baseline model family for NLP evaluations. (Same reference as Le Scao et al., 2022.) Also cited in 22_appendix-k-inference-results.md for the Bloom inference benchmark family.

**So et al. (2021)**
David R. So, Wojciech Manke, Hanxiao Liu, Zihang Dai, Noam Shazeer, and Quoc V. Le. 2021. Primer: Searching for efficient transformers for language modeling. *CoRR*, abs/2109.08668.
- Cited in 03_rwkv.md for the squared ReLU activation function.

**Taori et al. (2023)**
Rohan Taori, Ishaan Gulrajani, Tianyi Zhang, Yann Dubois, Xuechen Li, Carlos Guestrin, Percy Liang, and Tatsunori B. Hashimoto. 2023. Stanford alpaca: An instruction-following llama model. https://github.com/tatsu-lab/stanford_alpaca.
- Cited in 10_ethics-statement.md as publicly available instructions used for fine-tuning.

**Tay et al. (2021)**
Yi Tay, Mostafa Dehghani, Samira Abnar, Yikang Shen, Dara Bahri, Philip Pham, Jinfeng Rao, Liu Yang, Sebastian Ruder, and Donald Metzler. 2021. Long range arena: A benchmark for efficient transformers. In *International Conference on Learning Representations*.
- Cited in 05_evaluations.md for the Long-Range Arena (LRA) benchmark; in 21_appendix-j-additional-evaluations.md for the LRA benchmark description in J.2.

**Tay et al. (2022)**
Yi Tay, Mostafa Dehghani, Dara Bahri, and Donald Metzler. 2022. Efficient transformers: A survey. *ACM Computing Surveys*, 55(6):1-28.
- Cited in 01_introduction.md for Transformers being adept at managing dependencies and supporting parallelized training; in 14_appendix-c-additional-related-work.md for the survey of x-former variants.

**Touvron et al. (2023)**
Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothee Lacroix, Baptiste Roziere, Naman Goyal, Eric Hambro, Faisal Azhar, Aurelien Rodriguez, Armand Joulin, Edouard Grave, and Guillaume Lample. 2023. Llama: Open and efficient foundation language models.
- Cited in 01_introduction.md for LLaMA and in 05_evaluations.md for the overtrained regime.

**Vaswani et al. (2017)**
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Lukasz Kaiser, and Illia Polosukhin. 2017. Attention is all you need. In *Advances in Neural Information Processing Systems*, volume 30. Curran Associates, Inc.
- Cited in 01_introduction.md and 02_background.md for the Transformer architecture, and in 03_rwkv.md for the Small Init Embedding discussion.

**Vilares and Gomez-Rodriguez (2019)**
David Vilares and Carlos Gomez-Rodriguez. 2019. Head-qa: A healthcare dataset for complex reasoning. In *ACL*.
- Cited in 05_evaluations.md and 21_appendix-j-additional-evaluations.md as the HeadQA benchmark.

**Wang et al. (2020)**
Sinong Wang, Belinda Z. Li, Madian Khabsa, Han Fang, and Hao Ma. 2020. Linformer: Self-attention with linear complexity.
- Cited in 01_introduction.md for research to enhance Transformers' scalability; in 14_appendix-c-additional-related-work.md for Linformer approximating the full attention matrix.

**Wei et al. (2022a)**
Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama, Maarten Bosma, Denny Zhou, Donald Metzler, Ed Chi, Tatsunori Hashimoto, Oriol Vinyals, Percy Liang, Jeff Dean, and William Fedus. 2022a. Emergent abilities of large language models. *ArXiv*, abs/2206.07682.
- Cited in 04_trained-models-and-computing-costs.md for contexts where scaling laws provide feedback on future research.

**Wolf et al. (2020)**
Thomas Wolf, Lysandre Debut, Victor Sanh, Julien Chaumond, Clement Delangue, Anthony Moi, Perric Cistac, Clara Ma, Yacine Jernite, Julien Plu, Canwen Xu, Teven Le Scao, Sylvain Gugger, Mariama Drame, Quentin Lhoest, and Alexander M. Rush. 2020. Transformers: State-of-the-Art Natural Language Processing. pages 38-45. Association for Computational Linguistics.
- Cited in 06_inference-experiments.md for HuggingFace Transformers used in inference experiments.

**Wu et al. (2020)**
Zonghan Wu, Shirui Pan, Fengwen Chen, Guodong Long, Chengqi Zhang, and S Yu Philip. 2020. A comprehensive survey on graph neural networks. *IEEE transactions on neural networks and learning systems*, 32(1):4-24.
- Cited in 01_introduction.md for graph-based sequential data processing.

**Yang (2023)**
Jianxin Yang. 2023. Firefly. https://github.com/yangjianxin1/Firefly.
- Cited in 10_ethics-statement.md as publicly available instructions used for fine-tuning.

**Zaheer et al. (2020)**
Manzil Zaheer, Guru Guruganesh, Kumar Avinava Dubey, Joshua Ainslie, Chris Alberti, Santiago Ontanon, Philip Pham, Anirudh Ravula, Qifan Wang, Li Yang, et al. 2020. Big bird: Transformers for longer sequences. *Advances in Neural Information Processing Systems*, 33.
- Cited in 01_introduction.md for research to enhance Transformers' scalability.

**Zellers et al. (2019)**
Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali Farhadi, and Yejin Choi. 2019. Hellaswag: Can a machine really finish your sentence? In *ACL*.
- Cited in 05_evaluations.md and 21_appendix-j-additional-evaluations.md as the HellaSwag benchmark.

**Zellers et al. (2020)**
Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali Farhadi, and Yejin Choi. 2020. Winogrande: An adversarial winograd schema challenge at scale. In *ACL*.
- Cited in 05_evaluations.md and 21_appendix-j-additional-evaluations.md as the Winogrande benchmark.

**Zhai et al. (2021)**
Shuangfei Zhai, Walter Talbott, Nitish Srivastava, Chen Huang, Hanlin Goh, Ruixiang Zhang, and Josh Susskind. 2021. An attention free transformer.
- Cited in 02_background.md and 03_rwkv.md for the Attention Free Transformer (AFT) that inspired RWKV's approach; in 14_appendix-c-additional-related-work.md as an attention-free model.

**Zhang et al. (2018)**
Sheng Zhang, Xiaodong Liu, Jingjing Liu, Jianfeng Gao, Kevin Duh, and Benjamin Van Durme. 2018. Record: Bridging the gap between human and machine commonsense reading comprehension. In *arXiv:1810.12885*.
- Cited in 05_evaluations.md and 21_appendix-j-additional-evaluations.md as the ReCoRD benchmark.

**Zhang et al. (2022)**
Susan Zhang, Stephen Roller, Naman Goyal, Mikel Artetxe, Moya Chen, Shuohui Chen, Christopher Dewan, Mona Diab, Xian Li, Xi Victoria Lin, et al. 2022. Opt: Open pre-trained transformer language models. *arXiv preprint arXiv:2205.01068*.
- Cited in 05_evaluations.md as the OPT baseline model family for NLP evaluations; in 22_appendix-k-inference-results.md for the OPT inference benchmark family.

**Alam et al. (2023)**
Mohammad Mahmudul Alam, Edward Raff, Stella Biderman, Tim Oates, and James Holt. 2023. Recasting self-attention with holographic reduced representations. *arXiv preprint arXiv:2305.19534*.
- Cited in 14_appendix-c-additional-related-work.md for HrrFormer as an attention-free model; in 21_appendix-j-additional-evaluations.md as source for other models' LRA performances in Table 4.

**Beltagy et al. (2020)**
Iz Beltagy, Matthew E. Peters, and Arman Cohan. 2020. Longformer: The long-document transformer. *arXiv:2004.05150*.
- Cited in 14_appendix-c-additional-related-work.md for sparse attention to reduce transformer complexity.

**Black et al. (2021)**
Sid Black, Leo Gao, Phil Wang, Connor Leahy, and Stella Biderman. 2021. Gpt-neo: Large scale autoregressive language modeling with mesh-tensorflow. *URL: https://doi.org/10.5281/zenodo*, 5297715.
- Cited in 14_appendix-c-additional-related-work.md for a transformer using a mix of local and global attention, compared against SSM-based models; in 22_appendix-k-inference-results.md for the GPT-Neo inference benchmark family.

**Bulatov et al. (2022)**
Aydar Bulatov, Yury Kuratov, and Mikhail Burtsev. 2022. Recurrent memory transformer. *Advances in Neural Information Processing Systems*, 35:11079-11091.
- Cited in 14_appendix-c-additional-related-work.md for modifications to RNN-style components to increase context length.

**Bulatov et al. (2023)**
Aydar Bulatov, Yuri Kuratov, and Mikhail S. Burtsev. 2023. Scaling transformer to 1m tokens and beyond with rmt.
- Cited in 14_appendix-c-additional-related-work.md for modifications to RNN-style components to increase context length.

**Choromanski et al. (2020)**
Krzysztof Choromanski, Valerii Likhosherstov, David Dohan, Xingyou Song, Andreea Gane, Tamas Sarlos, Peter Hawkins, Jared Davis, Afroz Mohiuddin, Lukasz Kaiser, David Belanger, Lucy Colwell, and Adrian Weller. 2020. Rethinking attention with performers. In *ICLR*.
- Cited in 14_appendix-c-additional-related-work.md for approximating the full attention matrix; in 21_appendix-j-additional-evaluations.md as a baseline for Enwik8 perplexity (J.3).

**Dao et al. (2022b)**
Tri Dao, Daniel Y Fu, Khaled K Saab, Armin W Thomas, Atri Rudra, and Christopher Re. 2022b. Hungry hungry hippos: Towards language modeling with state space models. *arXiv preprint arXiv:2212.14052*.
- Cited in 14_appendix-c-additional-related-work.md as a variant of state space models.

**Gu et al. (2021)**
Albert Gu, Karan Goel, and Christopher Re. 2021. Efficiently modeling long sequences with structured state spaces. *arXiv preprint arXiv:2111.00396*.
- Cited in 14_appendix-c-additional-related-work.md for the original structured state space model (S4/SSM).

**Guo et al. (2022)**
Mandy Guo, Joshua Ainslie, David C Uthus, Santiago Ontanon, Jianmo Ni, Yun-Hsuan Sung, and Yinfei Yang. 2022. LongT5: Efficient text-to-text transformer for long sequences. In *Findings of the Association for Computational Linguistics: NAACL 2022*, pages 724-736.
- Cited in 14_appendix-c-additional-related-work.md for sparse attention to reduce transformer complexity.

**Gupta et al. (2022)**
Ankit Gupta, Albert Gu, and Jonathan Berant. 2022. Diagonal state spaces are as effective as structured state spaces. *Advances in Neural Information Processing Systems*, 35:22982-22994.
- Cited in 14_appendix-c-additional-related-work.md as a variant of state space models.

**Jaegle et al. (2021)**
Andrew Jaegle, Felix Gimeno, Andy Brock, Oriol Vinyals, Andrew Zisserman, and Joao Carreira. 2021. Perceiver: General perception with iterative attention. In *International conference on machine learning*, pages 4651-4664. PMLR.
- Cited in 14_appendix-c-additional-related-work.md as an efficient attention method.

**Jang et al. (2019)**
Hanhwi Jang, Joonsung Kim, Jae-Eon Jo, Jaewon Lee, and Jangwoo Kim. 2019. Mnnfast: A fast and scalable system architecture for memory-augmented neural networks. In *Proceedings of the 46th International Symposium on Computer Architecture*, pages 250-263.
- Cited in 14_appendix-c-additional-related-work.md for sharing similarities with RWKV's chunked computation scheme.

**Kitaev et al. (2020)**
Nikita Kitaev, L. Kaiser, and Anselm Levskaya. 2020. Reformer: The efficient transformer. *ArXiv*, abs/2001.04451.
- Cited in 14_appendix-c-additional-related-work.md for sparse attention to reduce transformer complexity; in 21_appendix-j-additional-evaluations.md as a baseline for Enwik8 perplexity (J.3).

**Liu et al. (2021)**
Hanxiao Liu, Zihang Dai, David R. So, and Quoc V. Le. 2021. Pay attention to mlps.
- Cited in 14_appendix-c-additional-related-work.md for replacing attention by MLPs.

**Ma et al. (2021)**
Xuezhe Ma, Xiang Kong, Sinong Wang, Chunting Zhou, Jonathan May, Hao Ma, and Luke Zettlemoyer. 2021. Luna: Linear unified nested attention. *Advances in Neural Information Processing Systems*, 34:2441-2453.
- Cited in 14_appendix-c-additional-related-work.md for approximating the full attention matrix.

**Ma et al. (2023)**
Xuezhe Ma, Chunting Zhou, Xiang Kong, Junxian He, Liangke Gui, Graham Neubig, Jonathan May, and Luke Zettlemoyer. 2023. Mega: Moving average equipped gated attention. In *ICLR*.
- Cited in 14_appendix-c-additional-related-work.md for combining chunked attention with gating.

**Orvieto et al. (2023)**
Antonio Orvieto, Samuel L Smith, Albert Gu, Anushan Fernando, Caglar Gulcehre, Razvan Pascanu, and Soham De. 2023. Resurrecting recurrent neural networks for long sequences. *arXiv preprint arXiv:2303.06349*.
- Cited in 14_appendix-c-additional-related-work.md for Linear Recurrent Units as advances in RNNs.

**Poli et al. (2023)**
Michael Poli, Stefano Massaroli, Eric Nguyen, Daniel Y Fu, Tri Dao, Stephen Baccus, Yoshua Bengio, Stefano Ermon, and Christopher Re. 2023. Hyena hierarchy: Towards larger convolutional language models. *arXiv preprint arXiv:2302.10866*.
- Cited in 14_appendix-c-additional-related-work.md for SSM-based models with 125M and 355M parameters showing on-par performance with transformers.

**Rabe and Staats (2022)**
Markus N. Rabe and Charles Staats. 2022. Self-attention does not need $o(n^2)$ memory.
- Cited in 14_appendix-c-additional-related-work.md for sharing similarities with RWKV's chunked computation scheme.

**Tolstikhin et al. (2021)**
Ilya O. Tolstikhin, Neil Houlsby, Alexander Kolesnikov, Lucas Beyer, Xiaohua Zhai, Thomas Unterthiner, Jessica Yung, Andreas Steiner, Daniel Keysers, Jakob Uszkoreit, Mario Lucic, and Alexey Dosovitskiy. 2021. Mlp-mixer: An all-mlp architecture for vision. *CoRR*, abs/2105.01601.
- Cited in 14_appendix-c-additional-related-work.md for MLP-Mixer replacing attention by MLPs in computer vision.

**Meng et al. (2022)**
Kevin Meng, David Bau, Alex Andonian, and Yonatan Belinkov. 2022. Locating and editing factual associations in GPT. *Advances in Neural Information Processing Systems*, 36.
- Cited in 20_appendix-i-model-behavior-visualization.md for the causal trace method used to analyze information retrieval and propagation in RWKV.

**Gu et al. (2022)**
Albert Gu, Karan Goel, and Christopher Re. 2022. Efficiently modeling long sequences with structured state spaces. In *The International Conference on Learning Representations (ICLR)*.
- Cited in 21_appendix-j-additional-evaluations.md as source for other models' LRA performances in Table 4.

**Tay et al. (2020)**
Yi Tay, Dara Bahri, Donald Metzler, Da-Cheng Juan, Zhe Zhao, and Che Zheng. 2020. Synthesizer: Rethinking self-attention in transformer models.
- Cited in 21_appendix-j-additional-evaluations.md as baseline (best performing dense version) for Enwik8 perplexity comparison in J.3.

**Wang et al. (2019)**
Alex Wang, Yada Pruksachatkun, Nikita Nangia, Amanpreet Singh, Julian Michael, Felix Hill, Omer Levy, and Samuel Bowman. 2019. Superglue: A stickier benchmark for general-purpose language understanding systems. In *Advances in Neural Information Processing Systems*, volume 32. Curran Associates, Inc.
- Cited in 23_appendix-l-prompt-construction.md for the RTE benchmark used in prompt comparison (Table 6).

**Wang et al. (2018)**
Alex Wang, Amanpreet Singh, Julian Michael, Felix Hill, Omer Levy, and Samuel Bowman. 2018. GLUE: A multi-task benchmark and analysis platform for natural language understanding. In *Proceedings of the 2018 EMNLP Workshop BlackboxNLP: Analyzing and Interpreting Neural Networks for NLP*, pages 353-355. Association for Computational Linguistics.
- Cited in 23_appendix-l-prompt-construction.md for the WNLI benchmark used in prompt comparison (Table 6).

**Demszky et al. (2020)**
Dorottya Demszky, Dana Movshovitz-Attias, Jeongwoo Ko, Alan S. Cowen, Gaurav Nemade, and Sujith Ravi. 2020. Goemotions: A dataset of fine-grained emotions. In *Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, ACL 2020, Online, July 5-10, 2020*, pages 4040-4054. Association for Computational Linguistics.
- Cited in 23_appendix-l-prompt-construction.md for the GoEmotions benchmark used in prompt comparison (Table 6).

**Kocon et al. (2019)**
Jan Kocon, Piotr Milkowski, and Monika Zasko-Zielinska. 2019. Multi-level sentiment analysis of polemo 2.0: Extended corpus of multi-domain consumer reviews. In *Proceedings of the 23rd Conference on Computational Natural Language Learning (CoNLL)*, pages 980-991.
- Cited in 23_appendix-l-prompt-construction.md for the PolEmo2 benchmark used in prompt comparison (Table 6).

**Wulczyn et al. (2017)**
Ellery Wulczyn, Nithum Thain, and Lucas Dixon. 2017. Ex machina: Personal attacks seen at scale. In *Proceedings of the 26th International Conference on World Wide Web, WWW 2017, Perth, Australia, April 3-7, 2017*, pages 1391-1399. ACM.
- Cited in 23_appendix-l-prompt-construction.md for the Aggression benchmark used in prompt comparison (Table 7).

**Siddiqui (2019)**
Ramsha Siddiqui. 2019. SARCASMANIA: Sarcasm Exposed! http://www.kaggle.com/rmsharks4/sarcasmania-dataset. [Online; accessed 02-February-2023].
- Cited in 23_appendix-l-prompt-construction.md for the Sarcasm benchmark used in prompt comparison (Table 7).

**Price et al. (2020)**
Ilan Price, Jordan Gifford-Moore, Jory Flemming, Saul Musker, Maayan Roichman, Guillaume Sylvain, Nithum Thain, Lucas Dixon, and Jeffrey Sorensen. 2020. Six attributes of unhealthy conversations. In *Proceedings of the Fourth Workshop on Online Abuse and Harms*, pages 114-124, Online. Association for Computational Linguistics.
- Cited in 23_appendix-l-prompt-construction.md for the Unhealthy benchmark used in prompt comparison (Table 7).

**Cobbe et al. (2021)**
Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Jacob Hilton, Reiichiro Nakano, Christopher Hesse, and John Schulman. 2021. Training verifiers to solve math word problems. In *arXiv*, volume abs/2110.14168.
- Cited in 23_appendix-l-prompt-construction.md for the MathQA benchmark used in prompt comparison (Table 7).

**Barbieri et al. (2020)**
Francesco Barbieri, Jose Camacho-Collados, Luis Espinosa Anke, and Leonardo Neves. 2020. TweetEval: Unified benchmark and comparative evaluation for tweet classification. In *Findings of the Association for Computational Linguistics: EMNLP 2020*, pages 1644-1650, Online. Association for Computational Linguistics.
- Cited in 23_appendix-l-prompt-construction.md for the TweetSent benchmark used in prompt comparison (Table 7).

**Wei et al. (2022b)**
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Ed Chi, Quoc Le, and Denny Zhou. 2022b. Chain of thought prompting elicits reasoning in large language models. *arXiv preprint arXiv:2201.11903*.
- Cited in 23_appendix-l-prompt-construction.md (footnote 4) for chain-of-thought prompting idea applied to MathQA.
