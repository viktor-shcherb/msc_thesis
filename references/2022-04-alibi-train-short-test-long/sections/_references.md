# References

Only references actually cited in the section notes are included here.

## Baevski & Auli (2018)
Alexei Baevski and Michael Auli. Adaptive input representations for neural language modeling. *CoRR*, abs/1809.10853, 2018.
- Cited in 02_current-approaches.md as the baseline language model used for experiments, in 04_results.md as the baseline on WikiText-103, in 09_appendix-a2.md (Table 7 baseline and sliding window evaluation reference), in 10_appendix-a3.md for the adaptive word embedding and softmax replaced in the Toronto BookCorpus experiments and in Table 10 sliding window reference, and in 12_appendix-b.md as the source of sliding window evaluation.

## Beltagy et al. (2020)
Iz Beltagy, Matthew E. Peters, and Arman Cohan. Longformer: The long-document transformer. *arXiv:2004.05150*, 2020.
- Cited in 05_related-work.md as a model that adapts shorter-sequence models to document-level tasks but requires partial retraining on longer sequences.

## Brown et al. (2020)
Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, and Dario Amodei. Language models are few-shot learners, 2020.
- Cited in 01_introduction.md and 02_current-approaches.md as GPT-3, which uses learned position embeddings.

## Conneau et al. (2020)
Alexis Conneau, Kartikay Khandelwal, Naman Goyal, Vishrav Chaudhary, Guillaume Wenzek, Francisco Guzmán, Edouard Grave, Myle Ott, Luke Zettlemoyer, and Veselin Stoyanov. Unsupervised cross-lingual representation learning at scale. *Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics*, 2020.
- Cited in 04_results.md as the source of the English CC-100 corpus (300 GB).

## Dai et al. (2019)
Zihang Dai, Zhilin Yang, Yiming Yang, Jaime Carbonell, Quoc Le, and Ruslan Salakhutdinov. Transformer-XL: Attentive language models beyond a fixed-length context. In *Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics*, pp. 2978--2988, Florence, Italy, July 2019.
- Cited in 04_results.md as a baseline surpassed by ALiBi on WikiText-103, in 05_related-work.md as a cache-based language model with limited extrapolation, and in 09_appendix-a2.md (Table 7 as Transformer-XL baseline).

## Devlin et al. (2019)
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. BERT: Pre-training of deep bidirectional transformers for language understanding. In *Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics*, pp. 4171--4186, Minneapolis, Minnesota, June 2019.
- Cited in 04_results.md in context of the RoBERTa training corpus, and in 10_appendix-a3.md noting the Toronto BooksCorpus was used to train BERT.

## Gokaslan & Cohen (2019)
Aaron Gokaslan and Vanya Cohen. Openwebtext corpus. http://Skylion007.github.io/OpenWebTextCorpus, 2019.
- Cited in 04_results.md as part of the RoBERTa training corpus.

## Huang et al. (2019)
Cheng-Zhi Anna Huang, Ashish Vaswani, Jakob Uszkoreit, Ian Simon, Curtis Hawthorne, Noam M. Shazeer, Andrew M. Dai, M. Hoffman, M. Dinculescu, and D. Eck. Music transformer: Generating music with long-term structure. In *ICLR*, 2019.
- Cited in 02_current-approaches.md as a relative position method related to the T5 bias.

## Hupkes et al. (2020)
Dieuwke Hupkes, Verna Dankers, Mathijs Mul, and Elia Bruni. Compositionality decomposed: How do neural networks generalise? *Journal of Artificial Intelligence Research*, 67:757--795, April 2020.
- Cited in 05_related-work.md as work exploring extrapolation with seq2seq models on an artificial dataset.

## Inan et al. (2017)
Hakan Inan, Khashayar Khosravi, and Richard Socher. Tying word vectors and word classifiers: A loss framework for language modeling. In *ICLR*, 2017.
- Cited in 02_current-approaches.md for tying embedding and softmax matrices, and in 10_appendix-a3.md for the tied word embedding and softmax matrix used in Toronto BookCorpus experiments.

## Jumper et al. (2021)
J. Jumper, Richard Evans, A. Pritzel, Tim Green, Michael Figurnov, O. Ronneberger, et al. Highly accurate protein structure prediction with alphafold. *Nature*, 596:583--589, 2021.
- Cited in 05_related-work.md as work on extrapolation in protein structure prediction (Appendix 1.5).

## Khandelwal et al. (2020)
Urvashi Khandelwal, Omer Levy, Dan Jurafsky, Luke Zettlemoyer, and Mike Lewis. Generalization through Memorization: Nearest Neighbor Language Models. In *International Conference on Learning Representations (ICLR)*, 2020.
- Cited in 02_current-approaches.md as a development building on the Baevski & Auli model, in 04_results.md as a method (kNN-LM) whose results ALiBi falls short of on WikiText-103, in 09_appendix-a2.md (Table 7 as kNN-LM baseline and sliding window evaluation reference), and in 10_appendix-a3.md for the train/validation/test split and tokenization used in Toronto BookCorpus experiments and in Table 10 as kNN-LM baseline.

## Kiyono et al. (2021)
Shun Kiyono, Sosuke Kobayashi, Jun Suzuki, and Kentaro Inui. Shape: Shifted absolute position embedding for transformers. *ArXiv*, abs/2109.05644, 2021.
- Cited in 05_related-work.md as work on extrapolation in machine translation.

## Lampinen et al. (2021)
Andrew Kyle Lampinen, Stephanie C. Y. Chan, Andrea Banino, and Felix Hill. Towards mental time travel: a hierarchical memory for reinforcement learning agents. *CoRR*, abs/2105.14039, 2021.
- Cited in 05_related-work.md as work on extrapolation with reinforcement learning.

## Lewis et al. (2021)
Mike Lewis, Shruti Bhosale, Tim Dettmers, Naman Goyal, and Luke Zettlemoyer. Base layers: Simplifying training of large, sparse models, 2021.
- Cited in 02_current-approaches.md as an example of a model using sinusoidal position embeddings.

## Lieber et al. (2021)
Opher Lieber, Or Sharir, Barak Lenz, and Yoav Shoham. Jurassic-1: Technical details and evaluation. Technical report, AI21 Labs, August 2021.
- Cited in 04_results.md as Jurassic-1, which uses learned position embeddings.

## Likhomanenko et al. (2021)
Tatiana Likhomanenko, Qiantong Xu, Ronan Collobert, Gabriel Synnaeve, and Alex Rogozhnikov. CAPE: encoding relative positions with continuous augmented positional embeddings. *CoRR*, abs/2106.03143, 2021.
- Cited in 05_related-work.md as work on extrapolation in image, speech recognition, and machine translation.

## Liu et al. (2019)
Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke Zettlemoyer, and Veselin Stoyanov. Roberta: A robustly optimized bert pretraining approach, 2019.
- Cited in 04_results.md as the source of the RoBERTa training corpus.

## Merity et al. (2016)
Stephen Merity, Caiming Xiong, James Bradbury, and Richard Socher. Pointer sentinel mixture models, 2016.
- Cited in 02_current-approaches.md and 04_results.md as the source of the WikiText-103 corpus.

## Mikolov et al. (2010)
Tomas Mikolov, M. Karafiát, L. Burget, J. Cernocký, and S. Khudanpur. Recurrent neural network based language model. In *INTERSPEECH*, 2010.
- Cited in 01_introduction.md as an example of RNN LMs trained on shorter sequences that generalize to longer contexts.

## Mikolov & Zweig (2012)
Tomas Mikolov and G. Zweig. Context dependent recurrent neural network language model. *2012 IEEE Spoken Language Technology Workshop (SLT)*, pp. 234--239, 2012.
- Cited in 01_introduction.md as an example of RNN LMs trained on shorter sequences.

## Nagel (2016)
Sebastian Nagel. Cc-news. https://commoncrawl.org/2016/10/news-dataset-available/, 2016.
- Cited in 04_results.md as part of the RoBERTa training corpus.

## Narang et al. (2021)
Sharan Narang, Hyung Won Chung, Yi Tay, William Fedus, Thibault Fevry, Michael Matena, Karishma Malkan, Noah Fiedel, Noam Shazeer, Zhenzhong Lan, Yanqi Zhou, Wei Li, Nan Ding, Jake Marcus, Adam Roberts, and Colin Raffel. Do transformer modifications transfer across implementations and applications?, 2021.
- Cited in 02_current-approaches.md (footnote 8) for benchmarking the T5 bias as 8.7% slower than sinusoidal on different hardware.

## Neishi & Yoshinaga (2019)
Masato Neishi and Naoki Yoshinaga. On the relation between position information and sentence length in neural machine translation. In *Proceedings of the 23rd Conference on Computational Natural Language Learning (CoNLL)*, pp. 328--338, Hong Kong, China, November 2019.
- Cited in 05_related-work.md as work on extrapolation in machine translation.

## Newman et al. (2020)
Benjamin Newman, John Hewitt, Percy Liang, and Christopher D. Manning. The eos decision and length extrapolation. In *BlackBoxNLP@EMNLP*, 2020.
- Cited in 05_related-work.md as work on extrapolation in machine translation.

## Nogueira et al. (2021)
Rodrigo Nogueira, Zhiying Jiang, and Jimmy J. Li. Investigating the limitations of the transformers with simple arithmetic tasks. *ArXiv*, abs/2102.13019, 2021.
- Cited in 05_related-work.md as work on extrapolation with pretrained seq2seq models on arithmetic tasks.

## Ott et al. (2018)
Myle Ott, Sergey Edunov, David Grangier, and Michael Auli. Scaling neural machine translation. In *Proceedings of the Third Conference on Machine Translation (WMT)*, 2018.
- Cited in 02_current-approaches.md as an example of a model using sinusoidal position embeddings.

## Parikh et al. (2016)
Ankur Parikh, Oscar Täckström, Dipanjan Das, and Jakob Uszkoreit. A decomposable attention model for natural language inference. In *Proceedings of the 2016 Conference on Empirical Methods in Natural Language Processing*, pp. 2249--2255, Austin, Texas, November 2016.
- Cited in 02_current-approaches.md (footnote 6) as having a method similar to the T5 bias.

## Press & Wolf (2017)
Ofir Press and Lior Wolf. Using the output embedding to improve language models. In *Proceedings of the 15th Conference of the European Chapter of the Association for Computational Linguistics: Volume 2, Short Papers*, pp. 157--163, Valencia, Spain, April 2017.
- Cited in 02_current-approaches.md for tying embedding and softmax matrices, and in 10_appendix-a3.md for the tied word embedding and softmax matrix used in Toronto BookCorpus experiments.

## Press et al. (2020)
Ofir Press, Noah A. Smith, and Omer Levy. Improving transformer models by reordering their sublayers. In *Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics*, pp. 2996--3005, Online, July 2020.
- Cited in 04_results.md as the Sandwich model surpassed by ALiBi on WikiText-103, in 09_appendix-a2.md (Table 7 as Sandwich Transformer baseline), and in 10_appendix-a3.md (Table 10 as Sandwich baseline and sliding window evaluation reference).

## Press et al. (2021)
Ofir Press, Noah A. Smith, and Mike Lewis. Shortformer: Better language modeling using shorter inputs. In *Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)*, pp. 5493--5505, Online, August 2021.
- Cited in 02_current-approaches.md (as Shortformer, for experiment setup context), 04_results.md (as Shortformer and staged training baseline), 05_related-work.md (noting slow relative position method of Transformer-XL), 09_appendix-a2.md (Table 7 as Shortformer and Staged Training baselines, and sliding window evaluation reference), 10_appendix-a3.md (Table 10 as Shortformer and Staged Training baselines), and 12_appendix-b.md (as the source of the early token curse concept and noting sliding window inference is prohibitively slow).

## Raffel et al. (2020)
Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, and Peter J. Liu. Exploring the limits of transfer learning with a unified text-to-text transformer. *Journal of Machine Learning Research*, 21(140):1--67, 2020.
- Cited in 01_introduction.md and 02_current-approaches.md as the source of the T5 bias relative position method.

## Rosendahl et al. (2019)
Jan Rosendahl, Viet Anh Khoa Tran, Weiyue Wang, and Hermann Ney. Analysis of positional encodings for neural machine translation. In *International Workshop on Spoken Language Translation*, Hong Kong, China, November 2019.
- Cited in 05_related-work.md as work on extrapolation in machine translation.

## Rae et al. (2020)
Jack W. Rae, Anna Potapenko, Siddhant M. Jayakumar, Chloe Hillier, and Timothy P. Lillicrap. Compressive transformers for long-range sequence modelling. In *International Conference on Learning Representations*, 2020.
- Cited in 09_appendix-a2.md (Table 7 as the Compressive Transformer baseline on WikiText-103).

## Roy et al. (2020)
Aurko Roy, Mohammad Saffar, Ashish Vaswani, and David Grangier. Efficient content-based sparse attention with routing transformers, 2020.
- Cited in 04_results.md as the Routing Transformer whose results ALiBi falls short of on WikiText-103, and in 09_appendix-a2.md (Table 7 as Routing Transformer baseline).

## Shaw et al. (2018)
Peter Shaw, Jakob Uszkoreit, and Ashish Vaswani. Self-attention with relative position representations. In *Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 2 (Short Papers)*, pp. 464--468, New Orleans, Louisiana, June 2018.
- Cited in 02_current-approaches.md as a relative position method related to the T5 bias.

## Su et al. (2021)
Jianlin Su, Yu Lu, Shengfeng Pan, Bo Wen, and Yunfeng Liu. Roformer: Enhanced transformer with rotary position embedding, 2021.
- Cited in 01_introduction.md and 02_current-approaches.md as the source of the rotary position embedding method.

## Trinh & Le (2018)
Trieu H. Trinh and Quoc V. Le. A simple method for commonsense reasoning, 2018.
- Cited in 04_results.md as the source of the Stories dataset in the RoBERTa training corpus.

## Vaswani et al. (2017)
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Lukasz Kaiser, and Illia Polosukhin. Attention is all you need. In *Advances in Neural Information Processing Systems*, volume 30. Curran Associates, Inc., 2017.
- Cited throughout (01_introduction.md, 02_current-approaches.md, 03_alibi.md, 04_results.md) as the original transformer paper introducing sinusoidal position embeddings.

## Wang & Komatsuzaki (2021)
Ben Wang and Aran Komatsuzaki. GPT-J-6B: A 6 Billion Parameter Autoregressive Language Model. https://github.com/kingoflolz/mesh-transformer-jax, May 2021.
- Cited in 02_current-approaches.md as the open source GPT-3 implementation using the rotary method.

## Wennberg & Henter (2021)
Ulme Wennberg and Gustav Eje Henter. The case for translation-invariant self-attention in transformer-based language models, 2021.
- Cited in 05_related-work.md as a concurrent work adding a radial-basis function bias to attention scores.

## Wolf et al. (2020)
Thomas Wolf, Lysandre Debut, Victor Sanh, Julien Chaumond, Clement Delangue, Anthony Moi, Pierric Cistac, Tim Rault, Rémi Louf, Morgan Funtowicz, Joe Davison, Sam Shleifer, Patrick von Platen, Clara Ma, Yacine Jernite, Julien Plu, Canwen Xu, Teven Le Scao, Sylvain Gugger, Marianna Drame, Quentin Lhoest, and Alexander M. Rush. Transformers: State-of-the-art natural language processing. In *Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing: System Demonstrations*, pp. 38--45, Online, October 2020.
- Cited in 02_current-approaches.md (footnote 7) as the source of the T5 bias implementation.

## Wu et al. (2021)
Chuhan Wu, Fangzhao Wu, and Yongfeng Huang. DA-transformer: Distance-aware transformer. In *Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies*, pp. 2059--2068, Online, June 2021.
- Cited in 05_related-work.md as the Distance Aware Transformer that multiplies (rather than adds) attention scores by a distance bias.

## Zaremba et al. (2014)
Wojciech Zaremba, Ilya Sutskever, and Oriol Vinyals. Recurrent neural network regularization, 2014.
- Cited in 01_introduction.md as an example of RNN LMs trained on shorter sequences.

## Zhu et al. (2015)
Yukun Zhu, Ryan Kiros, Rich Zemel, Ruslan Salakhutdinov, Raquel Urtasun, Antonio Torralba, and Sanja Fidler. Aligning books and movies: Towards story-like visual explanations by watching movies and reading books. In *Proceedings of the IEEE international conference on computer vision*, pp. 19--27, 2015.
- Cited in 04_results.md as the source of the Toronto Book Corpus, and in 10_appendix-a3.md as the source of the Toronto BooksCorpus used in the domain transfer experiments.
