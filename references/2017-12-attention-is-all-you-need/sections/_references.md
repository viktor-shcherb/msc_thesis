# References (cited in notes)

[1] Jimmy Lei Ba, Jamie Ryan Kiros, and Geoffrey E Hinton. Layer normalization. *arXiv preprint arXiv:1607.06450*, 2016.
- Cited in 03a_encoder-and-decoder-stacks.md: layer normalization applied after residual connections.

[2] Dzmitry Bahdanau, Kyunghyun Cho, and Yoshua Bengio. Neural machine translation by jointly learning to align and translate. *CoRR*, abs/1409.0473, 2014.
- Cited in 01_introduction.md as state-of-the-art encoder-decoder architecture; in 02_background.md; in 03a_encoder-and-decoder-stacks.md; in 03b_attention.md as originating additive attention and as a baseline encoder-decoder attention mechanism.

[3] Denny Britz, Anna Goldie, Minh-Thang Luong, and Quoc V. Le. Massive exploration of neural machine translation architectures. *CoRR*, abs/1703.03906, 2017.
- Cited in 05_training.md: byte-pair encoding used for tokenization; in 03b_attention.md: comparison of attention mechanisms.

[4] Jianpeng Cheng, Li Dong, and Mirella Lapata. Long short-term memory-networks for machine reading. *arXiv preprint arXiv:1601.06733*, 2016.
- Cited in 02_background.md: self-attention used in reading comprehension.

[5] Kyunghyun Cho, Bart van Merrienboer, Caglar Gulcehre, Fethi Bougares, Holger Schwenk, and Yoshua Bengio. Learning phrase representations using rnn encoder-decoder for statistical machine translation. *CoRR*, abs/1406.1078, 2014.
- Cited in 01_introduction.md and 03a_encoder-and-decoder-stacks.md as foundational encoder-decoder work.

[6] Francois Chollet. Xception: Deep learning with depthwise separable convolutions. *arXiv preprint arXiv:1610.02357*, 2016.
- Cited in 04_why-self-attention.md: separable convolutions reduce complexity.

[7] Junyoung Chung, Caglar Gulcehre, Kyunghyun Cho, and Yoshua Bengio. Empirical evaluation of gated recurrent neural networks on sequence modeling. *CoRR*, abs/1412.3555, 2014.
- Cited in 01_introduction.md: gated recurrent networks as state of the art.

[8] Chris Dyer, Adhiguna Kuncoro, Miguel Ballesteros, and Noah A. Smith. Recurrent neural network grammars. In *Proc. of NAACL*, 2016.
- Cited in 06_results.md: constituency parsing baseline (Recurrent Neural Network Grammar), the only model outperforming the Transformer in Table 4.

[9] Jonas Gehring, Michael Auli, David Grangier, Denis Yarats, and Yann N. Dauphin. Convolutional sequence to sequence learning. *arXiv preprint arXiv:1705.03122v2*, 2017.
- Cited in 02_background.md as ConvS2S baseline; in 03b_attention.md; in 03c_ffn-embeddings-positional-encoding.md for positional encodings; in 06_results.md as baseline in Tables 2 and 3.

[10] Alex Graves. Generating sequences with recurrent neural networks. *arXiv preprint arXiv:1308.0850*, 2013.
- Cited in 03a_encoder-and-decoder-stacks.md: auto-regressive models.

[11] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Deep residual learning for image recognition. In *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition*, pages 770-778, 2016.
- Cited in 03a_encoder-and-decoder-stacks.md: residual connections.

[12] Sepp Hochreiter, Yoshua Bengio, Paolo Frasconi, and Jurgen Schmidhuber. Gradient flow in recurrent nets: the difficulty of learning long-term dependencies, 2001.
- Cited in 02_background.md: difficulty of learning dependencies between distant positions; in 04_why-self-attention.md: difficulty of learning long-range dependencies related to path length.

[13] Sepp Hochreiter and Jurgen Schmidhuber. Long short-term memory. *Neural computation*, 9(8):1735-1780, 1997.
- Cited in 01_introduction.md: LSTMs as state of the art.

[14] Zhongqiang Huang and Mary Harper. Self-training PCFG grammars with latent annotations across languages. In *Proceedings of the 2009 Conference on Empirical Methods in Natural Language Processing*, pages 832-841. ACL, August 2009.
- Cited in 06_results.md Table 4: semi-supervised constituency parsing baseline.

[15] Rafal Jozefowicz, Oriol Vinyals, Mike Schuster, Noam Shazeer, and Yonghui Wu. Exploring the limits of language modeling. *arXiv preprint arXiv:1602.02410*, 2016.
- Cited in 01_introduction.md: pushing boundaries of recurrent language models.

[16] Lukasz Kaiser and Samy Bengio. Can active memory replace attention? In *Advances in Neural Information Processing Systems, (NIPS)*, 2016.
- Cited in 02_background.md: Extended Neural GPU as a model reducing sequential computation.

[17] Lukasz Kaiser and Ilya Sutskever. Neural GPUs learn algorithms. In *International Conference on Learning Representations (ICLR)*, 2016.
- Cited in 02_background.md: listed alongside [18] and [9] as a model the authors compare against.

[18] Nal Kalchbrenner, Lasse Espeholt, Karen Simonyan, Aaron van den Oord, Alex Graves, and Koray Kavukcuoglu. Neural machine translation in linear time. *arXiv preprint arXiv:1610.10099v2*, 2017.
- Cited in 02_background.md as ByteNet; in 04_why-self-attention.md for dilated convolutions; in 06_results.md Table 2 as baseline.

[19] Yoon Kim, Carl Denton, Luong Hoang, and Alexander M. Rush. Structured attention networks. In *International Conference on Learning Representations*, 2017.
- Cited in 01_introduction.md: attention mechanisms for sequence modeling.

[20] Diederik Kingma and Jimmy Ba. Adam: A method for stochastic optimization. In *ICLR*, 2015.
- Cited in 05_training.md: Adam optimizer used for training.

[21] Oleksii Kuchaiev and Boris Ginsburg. Factorization tricks for LSTM networks. *arXiv preprint arXiv:1703.10722*, 2017.
- Cited in 01_introduction.md: factorization tricks to improve efficiency of recurrent models.

[22] Zhouhan Lin, Minwei Feng, Cicero Nogueira dos Santos, Mo Yu, Bing Xiang, Bowen Zhou, and Yoshua Bengio. A structured self-attentive sentence embedding. *arXiv preprint arXiv:1703.03130*, 2017.
- Cited in 02_background.md: self-attention for sentence representations.

[23] Minh-Thang Luong, Quoc V. Le, Ilya Sutskever, Oriol Vinyals, and Lukasz Kaiser. Multi-task sequence to sequence learning. *arXiv preprint arXiv:1511.06114*, 2015.
- Cited in 06_results.md Table 4: multi-task constituency parsing result (93.0 F1).

[24] Minh-Thang Luong, Hieu Pham, and Christopher D Manning. Effective approaches to attention-based neural machine translation. *arXiv preprint arXiv:1508.04025*, 2015.
- Cited in 01_introduction.md: encoder-decoder architecture work.

[25] Mitchell P Marcus, Mary Ann Marcinkiewicz, and Beatrice Santorini. Building a large annotated corpus of english: The penn treebank. *Computational linguistics*, 19(2):313-330, 1993.
- Cited in 06_results.md: Penn Treebank used for constituency parsing experiments.

[26] David McClosky, Eugene Charniak, and Mark Johnson. Effective self-training for parsing. In *Proceedings of the Human Language Technology Conference of the NAACL, Main Conference*, pages 152-159. ACL, June 2006.
- Cited in 06_results.md Table 4: semi-supervised constituency parsing baseline.

[27] Ankur Parikh, Oscar Tackstrom, Dipanjan Das, and Jakob Uszkoreit. A decomposable attention model. In *Empirical Methods in Natural Language Processing*, 2016.
- Cited in 01_introduction.md: one of the few cases of attention without recurrence; in 02_background.md: self-attention for textual entailment.

[28] Romain Paulus, Caiming Xiong, and Richard Socher. A deep reinforced model for abstractive summarization. *arXiv preprint arXiv:1705.04304*, 2017.
- Cited in 02_background.md: self-attention for abstractive summarization.

[29] Slav Petrov, Leon Barrett, Romain Thibaux, and Dan Klein. Learning accurate, compact, and interpretable tree annotation. In *Proceedings of the 21st International Conference on Computational Linguistics and 44th Annual Meeting of the ACL*, pages 433-440. ACL, July 2006.
- Cited in 06_results.md Table 4: BerkeleyParser constituency parsing baseline, outperformed by the Transformer even with only 40K WSJ sentences.

[30] Ofir Press and Lior Wolf. Using the output embedding to improve language models. *arXiv preprint arXiv:1608.05859*, 2016.
- Cited in 03c_ffn-embeddings-positional-encoding.md: weight sharing between embedding layers and pre-softmax linear transformation.

[31] Rico Sennrich, Barry Haddow, and Alexandra Birch. Neural machine translation of rare words with subword units. *arXiv preprint arXiv:1508.07909*, 2015.
- Cited in 04_why-self-attention.md: byte-pair representations.

[32] Noam Shazeer, Azalia Mirhoseini, Krzysztof Maziarz, Andy Davis, Quoc Le, Geoffrey Hinton, and Jeff Dean. Outrageously large neural networks: The sparsely-gated mixture-of-experts layer. *arXiv preprint arXiv:1701.06538*, 2017.
- Cited in 01_introduction.md: conditional computation; in 06_results.md Table 2 as MoE baseline.

[33] Nitish Srivastava, Geoffrey E Hinton, Alex Krizhevsky, Ilya Sutskever, and Ruslan Salakhutdinov. Dropout: a simple way to prevent neural networks from overfitting. *Journal of Machine Learning Research*, 15(1):1929-1958, 2014.
- Cited in 05_training.md: dropout regularization technique.

[34] Sainbayar Sukhbaatar, Arthur Szlam, Jason Weston, and Rob Fergus. End-to-end memory networks. In C. Cortes, N. D. Lawrence, D. D. Lee, M. Sugiyama, and R. Garnett, editors, *Advances in Neural Information Processing Systems 28*, pages 2440-2448. Curran Associates, Inc., 2015.
- Cited in 02_background.md: end-to-end memory networks with recurrent attention.

[35] Ilya Sutskever, Oriol Vinyals, and Quoc VV Le. Sequence to sequence learning with neural networks. In *Advances in Neural Information Processing Systems*, pages 3104-3112, 2014.
- Cited in 01_introduction.md and 03a_encoder-and-decoder-stacks.md: foundational sequence-to-sequence model.

[36] Christian Szegedy, Vincent Vanhoucke, Sergey Ioffe, Jonathon Shlens, and Zbigniew Wojna. Rethinking the inception architecture for computer vision. *CoRR*, abs/1512.00567, 2015.
- Cited in 05_training.md: label smoothing regularization technique.

[37] Vinyals & Kaiser, Koo, Petrov, Sutskever, and Hinton. Grammar as a foreign language. In *Advances in Neural Information Processing Systems*, 2015.
- Cited in 06_results.md: RNN seq2seq models for constituency parsing; baseline in Table 4; noted inability to attain SOTA in small-data regimes.

[38] Yonghui Wu, Mike Schuster, Zhifeng Chen, Quoc V Le, Mohammad Norouzi, Wolfgang Macherey, Maxim Krikun, Yuan Cao, Qin Gao, Klaus Macherey, et al. Google's neural machine translation system: Bridging the gap between human and machine translation. *arXiv preprint arXiv:1609.08144*, 2016.
- Cited in 01_introduction.md: encoder-decoder architecture; in 03b_attention.md: baseline attention mechanism; in 04_why-self-attention.md: word-piece representations; in 05_training.md: word-piece vocabulary; in 06_results.md: GNMT+RL baseline in Table 2, beam search and length penalty hyperparameters.

[39] Jie Zhou, Ying Cao, Xuguang Wang, Peng Li, and Wei Xu. Deep recurrent models with fast-forward connections for neural machine translation. *CoRR*, abs/1606.04199, 2016.
- Cited in 06_results.md Table 2: Deep-Att + PosUnk baseline.

[40] Muhua Zhu, Yue Zhang, Wenliang Chen, Min Zhang, and Jingbo Zhu. Fast and accurate shift-reduce constituent parsing. In *Proceedings of the 51st Annual Meeting of the ACL (Volume 1: Long Papers)*, pages 434-443. ACL, August 2013.
- Cited in 06_results.md Table 4: constituency parsing baseline.
