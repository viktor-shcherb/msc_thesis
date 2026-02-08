# References

Only references that are cited in the section notes are included here.
Full bibliographic details from the paper's bibliography (p. 36-40).

**Abadi et al. (2016)**
Martin Abadi, Paul Barham, Jianmin Chen, Zhifeng Chen, Andy Davis, Jeffrey Dean, Matthieu Devin, Sanjay Ghemawat, Geoffrey Irving, Michael Isard, et al. Tensorflow: A system for large-scale machine learning. In *12th USENIX symposium on operating systems design and implementation (OSDI 16)*, pages 265-283, 2016.
- Cited in 02_switch-transformer.md as the framework underlying Mesh Tensorflow.

**Beltagy et al. (2020)**
Iz Beltagy, Matthew E Peters, and Arman Cohan. Longformer: The long-document transformer. *arXiv preprint arXiv:2004.05150*, 2020.
- Cited in 06_related-work.md as one of the approaches for attention sparsity along the sequence length dimension.

**Berant et al. (2013)**
Jonathan Berant, Andrew Chou, Roy Frostig, and Percy Liang. Semantic parsing on freebase from question-answer pairs. In *Proceedings of the 2013 conference on empirical methods in natural language processing*, pages 1533-1544, 2013.
- Cited in 04_downstream-results.md as the source of the Web Questions dataset.

**Brown et al. (2020)**
Tom B Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. Language models are few-shot learners. *arXiv preprint arXiv:2005.14165*, 2020.
- Cited in 01_introduction.md as a key example of the large-scale training approach, in 05_designing-models-parallelism.md as an example of mixing model and data parallelism, and in 06_related-work.md as having scaled models to billions of parameters through model parallelism.

**Child et al. (2019)**
Rewon Child, Scott Gray, Alec Radford, and Ilya Sutskever. Generating long sequences with sparse transformers. *arXiv preprint arXiv:1904.10509*, 2019.
- Cited in 06_related-work.md as one of the approaches for attention sparsity along the sequence length dimension.

**Cho and Bengio (2014)**
Kyunghyun Cho and Yoshua Bengio. Exponentially increasing the capacity-to-computation ratio for conditional computation in deep learning. *arXiv preprint arXiv:1406.7362*, 2014.
- Cited in 06_related-work.md as proposing adaptively selecting weights based on bit patterns in hidden-states.

**Clark et al. (2018)**
Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar Khot, Ashish Sabharwal, Carissa Schoenick, and Oyvind Tafjord. Think you have solved question answering? try arc, the ai2 reasoning challenge. *arXiv preprint arXiv:1803.05457*, 2018.
- Cited in 04_downstream-results.md as the source of the ARC Reasoning Challenge dataset.

**Correia et al. (2019)**
Goncalo M Correia, Vlad Niculae, and Andre FT Martins. Adaptively sparse transformers. *arXiv preprint arXiv:1909.00015*, 2019.
- Cited in 06_related-work.md as one of the approaches for attention sparsity along the sequence length dimension.

**Devlin et al. (2018)**
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. Bert: Pre-training of deep bidirectional transformers for language understanding. *arXiv preprint arXiv:1810.04805*, 2018.
- Cited in 02_switch-transformer.md as one of the masked language modeling approaches used for the pre-training objective.

**Eigen et al. (2013)**
David Eigen, Marc'Aurelio Ranzato, and Ilya Sutskever. Learning factored representations in a deep mixture of experts. *arXiv preprint arXiv:1312.4314*, 2013.
- Cited in 06_related-work.md as building stacked expert layers with dense matrix multiplications and ReLU activations.

**Fan et al. (2021)**
Angela Fan, Shruti Bhosale, Holger Schwenk, Zhiyi Ma, Ahmed El-Kishky, Siddharth Goyal, Mandeep Baines, Onur Celebi, Guillaume Wenzek, Vishrav Chaudhary, et al. Beyond english-centric multilingual machine translation. *Journal of Machine Learning Research*, 22(107):1-48, 2021.
- Cited in 06_related-work.md as choosing a deterministic MoE strategy to split model parameters into non-overlapping groups of languages.

**Fedus et al. (2018)**
William Fedus, Ian Goodfellow, and Andrew M Dai. Maskgan: Better text generation via filling in the _. *arXiv preprint arXiv:1801.07736*, 2018.
- Cited in 02_switch-transformer.md as one of the masked language modeling approaches.

**Gale et al. (2020)**
Trevor Gale, Matei Zaharia, Cliff Young, and Erich Elsen. Sparse gpu kernels for deep learning. *arXiv preprint arXiv:2006.10901*, 2020.
- Cited in 01_introduction.md as part of the active area of research in sparse training.

**Gray et al. (2017)**
Scott Gray, Alec Radford, and Diederik P Kingma. Gpu kernels for block-sparse weights. *https://openai.com/blog/block-sparse-gpu-kernels/*, 2017.
- Cited in 01_introduction.md as part of the active area of research in sparse training.

**Guu et al. (2020)**
Kelvin Guu, Kenton Lee, Zora Tung, Panupong Pasupat, and Ming-Wei Chang. Realm: Retrieval-augmented language model pre-training. *arXiv preprint arXiv:2002.08909*, 2020.
- Cited in 05_designing-models-parallelism.md for Salient Span Masking pre-training technique.

**Harlap et al. (2018)**
Aaron Harlap, Deepak Narayanan, Amar Phanishayee, Vivek Seshadri, Nikhil Devanur, Greg Ganger, and Phil Gibbons. Pipedream: Fast and efficient pipeline parallel dnn training. *arXiv preprint arXiv:1806.03377*, 2018.
- Cited in 06_related-work.md as proposing pipeline-based model parallelism.

**Hermann et al. (2015)**
Karl Moritz Hermann, Tomas Kocisky, Edward Grefenstette, Lasse Espeholt, Will Kay, Mustafa Suleyman, and Phil Blunsom. Teaching machines to read and comprehend. In C. Cortes, N. Lawrence, D. Lee, M. Sugiyama, and R. Garnett, editors, *Advances in Neural Information Processing Systems*, volume 28, pages 1693-1701. Curran Associates, Inc., 2015.
- Cited in 04_downstream-results.md as the source of the CNNDM dataset.

**Hinton et al. (2015)**
Geoffrey Hinton, Oriol Vinyals, and Jeff Dean. Distilling the knowledge in a neural network. *arXiv preprint arXiv:1503.02531*, 2015.
- Cited in 01_introduction.md and 04_downstream-results.md for distillation.

**Hochreiter and Schmidhuber (1997)**
Sepp Hochreiter and Jurgen Schmidhuber. Long short-term memory. *Neural computation*, 9(8):1735-1780, 1997.
- Cited in 06_related-work.md for LSTM architecture.

**Hooker (2020)**
Sara Hooker. The hardware lottery. *arXiv preprint arXiv:2009.06489*, 2020.
- Cited in 07_discussion.md regarding co-adaptation with deep learning hardware.

**Huang et al. (2019)**
Yanping Huang, Youlong Cheng, Ankur Bapna, Orhan Firat, Dehao Chen, Mia Chen, HyoukJoong Lee, Jiquan Ngiam, Quoc V Le, Yonghui Wu, et al. Gpipe: Efficient training of giant neural networks using pipeline parallelism. In *Advances in neural information processing systems*, pages 103-112, 2019.
- Cited in 06_related-work.md as proposing pipeline-based model parallelism.

**Jacobs et al. (1991)**
Robert A Jacobs, Michael I Jordan, Steven J Nowlan, and Geoffrey E Hinton. Adaptive mixtures of local experts. *Neural computation*, 3(1):79-87, 1991.
- Cited in 01_introduction.md as originating the MoE paradigm.

**Jordan and Jacobs (1994)**
Michael I Jordan and Robert A Jacobs. Hierarchical mixtures of experts and the em algorithm. *Neural computation*, 6(2):181-214, 1994.
- Cited in 01_introduction.md as originating the MoE paradigm.

**Joshi et al. (2017)**
Mandar Joshi, Eunsol Choi, Daniel S Weld, and Luke Zettlemoyer. Triviaqa: A large scale distantly supervised challenge dataset for reading comprehension. *arXiv preprint arXiv:1705.03551*, 2017.
- Cited in 04_downstream-results.md as the source of the TriviaQA dataset.

**Kaplan et al. (2020)**
Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jeffrey Wu, and Dario Amodei. Scaling laws for neural language models. *arXiv preprint arXiv:2001.08361*, 2020.
- Cited in 01_introduction.md, 02_switch-transformer.md, 03_scaling-properties.md, 04_downstream-results.md, and 07_discussion.md for power-law scaling relationships.

**Kitaev et al. (2020)**
Nikita Kitaev, Lukasz Kaiser, and Anselm Levskaya. Reformer: The efficient transformer. *arXiv preprint arXiv:2001.04451*, 2020.
- Cited in 06_related-work.md as one of the approaches for attention sparsity.

**Kwiatkowski et al. (2019)**
Tom Kwiatkowski, Jennimaria Palomaki, Olivia Redfield, Michael Collins, Ankur Parikh, Chris Alberti, Danielle Epstein, Illia Polosukhin, Jacob Devlin, Kenton Lee, et al. Natural questions: a benchmark for question answering research. *Transactions of the Association for Computational Linguistics*, 7:453-466, 2019.
- Cited in 04_downstream-results.md as the source of the Natural Questions dataset.

**Lample et al. (2019)**
Guillaume Lample, Alexandre Sablayrolles, Marc'Aurelio Ranzato, Ludovic Denoyer, and Herve Jegou. Large memory layers with product keys. In *Advances in Neural Information Processing Systems*, pages 8548-8559, 2019.
- Cited in 06_related-work.md for Product Key networks.

**Lee et al. (2021)**
Katherine Lee, Daphne Ippolito, Andrew Nystrom, Chiyuan Zhang, Douglas Eck, Chris Callison-Burch, and Nicholas Carlini. Deduplicating training data makes language models better. *arXiv preprint arXiv:2107.06499*, 2021.
- Cited in 04_downstream-results.md for improved C4 corpus deduplication.

**Lepikhin et al. (2020)**
Dmitry Lepikhin, HyoukJoong Lee, Yuanzhong Xu, Dehao Chen, Orhan Firat, Yanping Huang, Maxim Krikun, Noam Shazeer, and Zhifeng Chen. Gshard: Scaling giant models with conditional computation and automatic sharding. *arXiv preprint arXiv:2006.16668*, 2020.
- Cited in 01_introduction.md, 02_switch-transformer.md, 06_related-work.md, 11_appendix-a.md, and 12_appendix-b.md for GShard MoE.

**Micikevicius et al. (2017)**
Paulius Micikevicius, Sharan Narang, Jonah Alben, Gregory Diamos, Erich Elsen, David Garcia, Boris Ginsburg, Michael Houston, Oleksii Kuchaiev, Ganesh Venkatesh, et al. Mixed precision training. *arXiv preprint arXiv:1710.03740*, 2017.
- Cited in 02_switch-transformer.md for mixed precision training strategies.

**Narayan et al. (2018)**
Shashi Narayan, Shay B Cohen, and Mirella Lapata. Don't give me the details, just the summary! topic-aware convolutional neural networks for extreme summarization. *arXiv preprint arXiv:1808.08745*, 2018.
- Cited in 04_downstream-results.md as the source of the BBC XSum dataset.

**Nie et al. (2019)**
Yixin Nie, Adina Williams, Emily Dinan, Mohit Bansal, Jason Weston, and Douwe Kiela. Adversarial nli: A new benchmark for natural language understanding. *arXiv preprint arXiv:1910.14599*, 2019.
- Cited in 04_downstream-results.md and 05_designing-models-parallelism.md for the ANLI benchmark.

**Puigcerver et al. (2020)**
Joan Puigcerver, Carlos Riquelme, Basil Mustafa, Cedric Renggli, Andre Susano Pinto, Sylvain Gelly, Daniel Keysers, and Neil Houlsby. Scalable transfer learning with expert models. *arXiv preprint arXiv:2009.13239*, 2020.
- Cited in 06_related-work.md for manually routing tokens by semantic class.

**Radford et al. (2018)**
Alec Radford, Karthik Narasimhan, Tim Salimans, and Ilya Sutskever. Improving language understanding by generative pre-training, 2018.
- Cited in 01_introduction.md as a key example of the large-scale training approach.

**Raffel et al. (2019)**
Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, and Peter J Liu. Exploring the limits of transfer learning with a unified text-to-text transformer. *arXiv preprint arXiv:1910.10683*, 2019.
- Cited in 00_overview.md, 01_introduction.md, 02_switch-transformer.md, 03_scaling-properties.md, 04_downstream-results.md, 05_designing-models-parallelism.md, and 06_related-work.md for the T5 model and C4 corpus.

**Rajbhandari et al. (2019)**
Samyam Rajbhandari, Jeff Rasley, Olatunji Ruwase, and Yuxiong He. Zero: Memory optimization towards training a trillion parameter models. *arXiv preprint arXiv:1910.02054*, 2019.
- Cited in 06_related-work.md for model parallelism scaling.

**Rajpurkar et al. (2016)**
Pranav Rajpurkar, Jian Zhang, Konstantin Lopyrev, and Percy Liang. Squad: 100,000+ questions for machine comprehension of text. *arXiv preprint arXiv:1606.05250*, 2016.
- Cited in 04_downstream-results.md as the source of the SQuAD dataset.

**Ramachandran and Le (2018)**
Prajit Ramachandran and Quoc V Le. Diversity and depth in per-example routing models. In *International Conference on Learning Representations*, 2018.
- Cited in 02_switch-transformer.md for their study of the top-k routing decision.

**Robbins (1952)**
Herbert Robbins. Some aspects of the sequential design of experiments. *Bulletin of the American Mathematical Society*, 58(5):527-535, 1952.
- Cited in 13_appendix-c.md for the contextual bandit setting.

**Roberts et al. (2020)**
Adam Roberts, Colin Raffel, and Noam Shazeer. How much knowledge can you pack into the parameters of a language model? *arXiv preprint arXiv:2002.08910*, 2020.
- Cited in 04_downstream-results.md for the closed-book QA evaluation protocol.

**Rosenbaum et al. (2017)**
Clemens Rosenbaum, Tim Klinger, and Matthew Riemer. Routing networks: Adaptive selection of non-linear functions for multi-task learning. *arXiv preprint arXiv:1711.01239*, 2017.
- Cited in 13_appendix-c.md for exploration-exploitation in multi-task learning.

**Sakaguchi et al. (2020)**
Keisuke Sakaguchi, Ronan Le Bras, Chandra Bhagavatula, and Yejin Choi. Winogrande: An adversarial winograd schema challenge at scale. In *Proceedings of the AAAI Conference on Artificial Intelligence*, volume 34, pages 8732-8740, 2020.
- Cited in 04_downstream-results.md for the Winogrande Schema Challenge.

**Sanh et al. (2019)**
Victor Sanh, Lysandre Debut, Julien Chaumond, and Thomas Wolf. Distilbert, a distilled version of bert: smaller, faster, cheaper and lighter, 2019.
- Cited in 04_downstream-results.md for distillation methods for BERT.

**Shazeer (2020)**
Noam Shazeer. Glu variants improve transformer, 2020.
- Cited in 05_designing-models-parallelism.md for the FFN_GEGLU variation.

**Shazeer et al. (2017)**
Noam Shazeer, Azalia Mirhoseini, Krzysztof Maziarz, Andy Davis, Quoc Le, Geoffrey Hinton, and Jeff Dean. Outrageously large neural networks: The sparsely-gated mixture-of-experts layer. *arXiv preprint arXiv:1701.06538*, 2017.
- Cited in 01_introduction.md, 02_switch-transformer.md, 06_related-work.md, and 11_appendix-a.md for MoE in NLP.

**Shazeer et al. (2018)**
Noam Shazeer, Youlong Cheng, Niki Parmar, Dustin Tran, Ashish Vaswani, Penporn Koanantakool, Peter Hawkins, HyoukJoong Lee, Mingsheng Hong, Cliff Young, et al. Mesh-tensorflow: Deep learning for supercomputers. In *Advances in Neural Information Processing Systems*, pages 10414-10423, 2018.
- Cited in 01_introduction.md, 02_switch-transformer.md, 05_designing-models-parallelism.md, 06_related-work.md, 11_appendix-a.md, and 16_appendix-f.md for Mesh Tensorflow.

**Shoeybi et al. (2019)**
Mohammad Shoeybi, Mostofa Patwary, Raul Puri, Patrick LeGresley, Jared Casper, and Bryan Catanzaro. Megatron-lm: Training multi-billion parameter language models using gpu model parallelism. *arXiv preprint arXiv:1909.08053*, 2019.
- Cited in 06_related-work.md for model parallelism scaling.

**Srivastava et al. (2014)**
Nitish Srivastava, Geoffrey E. Hinton, Alex Krizhevsky, Ilya Sutskever, and Ruslan Salakhutdinov. Dropout: a simple way to prevent neural networks from overfitting. *Journal of Machine Learning Research*, 15(1):1929-1958, 2014.
- Cited in 02_switch-transformer.md for dropout regularization.

**Strubell et al. (2019)**
Emma Strubell, Ananya Ganesh, and Andrew McCallum. Energy and policy considerations for deep learning in nlp. *arXiv preprint arXiv:1906.02243*, 2019.
- Cited in 01_introduction.md for computational intensity of dense scaling.

**Sukhbaatar et al. (2019)**
Sainbayar Sukhbaatar, Edouard Grave, Piotr Bojanowski, and Armand Joulin. Adaptive attention span in transformers. *arXiv preprint arXiv:1905.07799*, 2019.
- Cited in 06_related-work.md as one of the approaches for attention sparsity.

**Sutton (2019)**
Rich Sutton. The Bitter Lesson. *http://www.incompleteideas.net/IncIdeas/BitterLesson.html*, 2019.
- Cited in 01_introduction.md for the argument that simple methods backed by computation surpass more complicated algorithms.

**Sutton and Barto (2018)**
Richard S Sutton and Andrew G Barto. *Reinforcement learning: An introduction*. Stanford University, 2018.
- Cited in 13_appendix-c.md for the exploration-exploitation dilemma.

**Taylor (1953)**
Wilson L Taylor. "cloze procedure": A new tool for measuring readability. *Journalism quarterly*, 30(4):415-433, 1953.
- Cited in 02_switch-transformer.md for masked language modeling.

**Vaswani et al. (2017)**
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Lukasz Kaiser, and Illia Polosukhin. Attention is all you need. In *Advances in neural information processing systems*, pages 5998-6008, 2017.
- Cited in 01_introduction.md and 02_switch-transformer.md for the Transformer architecture.

**Wang and Kanwar (2019)**
Shibo Wang and Pankaj Kanwar. Bfloat16: The secret to high performance on cloud tpus. *Google Cloud Blog*, 2019.
- Cited in 02_switch-transformer.md for bfloat16 precision format.

**Wang et al. (2018)**
Alex Wang, Amanpreet Singh, Julian Michael, Felix Hill, Omer Levy, and Samuel R Bowman. Glue: A multi-task benchmark and analysis platform for natural language understanding. *arXiv preprint arXiv:1804.07461*, 2018.
- Cited in 04_downstream-results.md for the GLUE benchmark.

**Wang et al. (2019)**
Alex Wang, Yada Pruksachatkun, Nikita Nangia, Amanpreet Singh, Julian Michael, Felix Hill, Omer Levy, and Samuel Bowman. Superglue: A stickier benchmark for general-purpose language understanding systems. In *Advances in Neural Information Processing Systems*, pages 3266-3280, 2019.
- Cited in 04_downstream-results.md and 05_designing-models-parallelism.md for the SuperGLUE benchmark.

**Xue et al. (2020)**
Linting Xue, Noah Constant, Adam Roberts, Mihir Kale, Rami Al-Rfou, Aditya Siddhant, Aditya Barua, and Colin Raffel. mt5: A massively multilingual pre-trained text-to-text transformer. *arXiv preprint arXiv:2010.11934*, 2020.
- Cited in 01_introduction.md, 04_downstream-results.md, and 05_designing-models-parallelism.md for the mT5 multilingual extension.

**Yang et al. (2020)**
Zhilin Yang, Zihang Dai, Yiming Yang, Jaime Carbonell, Ruslan Salakhutdinov, and Quoc V. Le. Xlnet: Generalized autoregressive pretraining for language understanding, 2020.
- Cited in 05_designing-models-parallelism.md as the prior ANLI state-of-the-art.

**Zaheer et al. (2020)**
Manzil Zaheer, Guru Guruganesh, Avinava Dubey, Joshua Ainslie, Chris Alberti, Santiago Ontanon, Philip Pham, Anirudh Ravula, Qifan Wang, Li Yang, et al. Big bird: Transformers for longer sequences. *arXiv preprint arXiv:2007.14062*, 2020.
- Cited in 06_related-work.md as one of the approaches for attention sparsity.
