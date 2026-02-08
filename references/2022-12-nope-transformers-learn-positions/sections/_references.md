# References

Only references cited in the section notes are included below.

## Bahdanau et al., 2015
Dzmitry Bahdanau, Kyunghyun Cho, and Yoshua Bengio. 2015. Neural machine translation by jointly learning to align and translate. *CoRR*, abs/1409.0473.
- Cited in 01_introduction.md as the original attention mechanism.

## Vaswani et al., 2017
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Lukasz Kaiser, and Illia Polosukhin. 2017. Attention is all you need. In *Advances in Neural Information Processing Systems*, volume 30. Curran Associates, Inc.
- Cited in 01_introduction.md as the transformer paper; in 02_positional-encodings.md for sinusoidal embeddings.

## Radford et al., 2018
Alec Radford, Karthik Narasimhan, Tim Salimans, and Ilya Sutskever. 2018. Improving language understanding by generative pre-training.
- Cited in 01_introduction.md for absolute positional embeddings.

## Shaw et al., 2018
Peter Shaw, Jakob Uszkoreit, and Ashish Vaswani. 2018. Self-attention with relative position representations. In *Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 2 (Short Papers)*, pages 464–468, New Orleans, Louisiana. Association for Computational Linguistics.
- Cited in 01_introduction.md as a relative bias factor method.

## Raffel et al., 2020
Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, and Peter J. Liu. 2020. Exploring the limits of transfer learning with a unified text-to-text transformer. *Journal of Machine Learning Research*, 21(140):1–67.
- Cited in 01_introduction.md as a relative bias factor method.

## Press et al., 2022
Ofir Press, Noah Smith, and Mike Lewis. 2022. Train short, test long: Attention with linear biases enables input length extrapolation. In *International Conference on Learning Representations*.
- Cited in 01_introduction.md, 02_positional-encodings.md as ALiBi; in 03_experiment-setup.md for sequence length choice.

## Gehring et al., 2017
Jonas Gehring, Michael Auli, David Grangier, Denis Yarats, and Yann Dauphin. 2017. Convolutional sequence to sequence learning. In *ICML*.
- Cited in 01_introduction.md and 02_positional-encodings.md for learned positional embeddings.

## Devlin et al., 2019
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2019. BERT: Pre-training of deep bidirectional transformers for language understanding. In *Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers)*, pages 4171–4186, Minneapolis, Minnesota. Association for Computational Linguistics.
- Cited in 01_introduction.md for masked language models; in 02_positional-encodings.md for learned embeddings in MLMs; in 06_conjecture.md for bidirectional models and Table 4.

## Sukhbaatar et al., 2015
Sainbayar Sukhbaatar, Arthur Szlam, Jason Weston, and Rob Fergus. 2015. End-to-end memory networks. In *Proceedings of the 28th International Conference on Neural Information Processing Systems - Volume 2*, NIPS'15, page 2440–2448, Cambridge, MA, USA. MIT Press.
- Cited in 02_positional-encodings.md for learned positional embeddings.

## Liu et al., 2019
Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke Zettlemoyer, and Veselin Stoyanov. 2019. Roberta: A robustly optimized BERT pretraining approach. *CoRR*, abs/1907.11692.
- Cited in 02_positional-encodings.md for learned embeddings in MLMs; in 06_conjecture.md for RoBERTa large architecture.

## Brown et al., 2020
Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel Ziegler, Jeffrey Wu, Clemens Winter, Chris Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, and Dario Amodei. 2020. Language models are few-shot learners. In *Advances in Neural Information Processing Systems*, volume 33, pages 1877–1901. Curran Associates, Inc.
- Cited in 02_positional-encodings.md for GPT-3; in 03_experiment-setup.md for baseline architecture; in 04_results.md for Table 1 caption.

## Baevski and Auli, 2019
Alexei Baevski and Michael Auli. 2019. Adaptive input representations for neural language modeling. In *7th International Conference on Learning Representations, ICLR 2019, New Orleans, LA, USA, May 6-9, 2019*. OpenReview.net.
- Cited in 02_positional-encodings.md for sinusoidal embeddings in language modeling; in 03_experiment-setup.md for canonical WikiText-103 model; in 04_results.md for Table 1 caption.

## Merity et al., 2017
Stephen Merity, Caiming Xiong, James Bradbury, and Richard Socher. 2017. Pointer sentinel mixture models. In *5th International Conference on Learning Representations, ICLR 2017, Toulon, France, April 24-26, 2017, Conference Track Proceedings*. OpenReview.net.
- Cited in 03_experiment-setup.md for WikiText-103 corpus; in 04_results.md for Table 1 caption.

## Gao et al., 2020
Leo Gao, Stella Biderman, Sid Black, Laurence Golding, Travis Hoppe, Charles Foster, Jason Phang, Horace He, Anish Thite, Noa Nabeshima, Shawn Presser, and Connor Leahy. 2020. The Pile: An 800gb dataset of diverse text for language modeling. *arXiv preprint arXiv:2101.00027*.
- Cited in 03_experiment-setup.md for The Pile dataset; in 04_results.md for Table 1 caption; in 06_conjecture.md for Table 4 caption.

## Ott et al., 2019
Myle Ott, Sergey Edunov, Alexei Baevski, Angela Fan, Sam Gross, Nathan Ng, David Grangier, and Michael Auli. 2019. fairseq: A fast, extensible toolkit for sequence modeling. In *Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics (Demonstrations)*, pages 48–53, Minneapolis, Minnesota. Association for Computational Linguistics.
- Cited in 03_experiment-setup.md for the fairseq implementation.

## Radford et al., 2019
Alec Radford, Jeff Wu, Rewon Child, David Luan, Dario Amodei, and Ilya Sutskever. 2019. Language models are unsupervised multitask learners.
- Cited in 03_experiment-setup.md for the GPT-2 tokenizer.

## Press et al., 2020
Ofir Press, Noah A. Smith, and Omer Levy. 2020. Improving transformer models by reordering their sublayers. In *Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics*, pages 2996–3005, Online. Association for Computational Linguistics.
- Cited in 04_results.md (footnote 2) for seed variance on WikiText-103.

## Scao et al., 2022
Teven Le Scao, Thomas Wang, Daniel Hesslow, Lucile Saulnier, Stas Bekman, M Saiful Bari, Stella Biderman, Hady Elsahar, Jason Phang, Ofir Press, Colin Raffel, Victor Sanh, Sheng Shen, Lintang Sutawika, Jaesung Tae, Zheng Xin Yong, Julien Launay, and Iz Beltagy. 2022. What language model to train if you have one million GPU hours? In *Challenges & Perspectives in Creating Large Language Models*.
- Cited in 04_results.md as concurrent work showing NoPos models gain competitive downstream task performance.

## Voita et al., 2019
Elena Voita, Rico Sennrich, and Ivan Titov. 2019. The bottom-up evolution of representations in the transformer: A study with machine translation and language modeling objectives. In *Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)*, pages 4396–4406, Hong Kong, China. Association for Computational Linguistics.
- Cited in 05_analysis.md for the finding that models shed positional information in final layers.

## Sinha et al., 2021
Koustuv Sinha, Robin Jia, Dieuwke Hupkes, Joelle Pineau, Adina Williams, and Douwe Kiela. 2021. Masked language modeling and the distributional hypothesis: Order word matters pre-training for little. In *Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing*, pages 2888–2913, Online and Punta Cana, Dominican Republic. Association for Computational Linguistics.
- Cited in 06_conjecture.md for the observation that MLMs without positional embeddings suffer significant performance degradation.

## Irie et al., 2019
Kazuki Irie, Albert Zeyer, Ralf Schluter, and Hermann Ney. 2019. Language modeling with deep transformers. In *INTERSPEECH*.
- Cited in 07_related-work.md for finding that transformers without positional encoding outperform those with sinusoidal embeddings in speech recognition.

## Nesterov, 1983
Yurii Nesterov. 1983. A method for unconstrained convex minimization problem with the rate of convergence o(1/k^2).
- Cited in 13_appendix-c.md (Table 5 caption) for the NAG optimizer.

## Kingma and Ba, 2015
Diederik P. Kingma and Jimmy Ba. 2015. Adam: A method for stochastic optimization. In *3rd International Conference on Learning Representations, ICLR 2015, San Diego, CA, USA, May 7-9, 2015, Conference Track Proceedings*.
- Cited in 13_appendix-c.md (Table 5 caption) for the Adam optimizer.
