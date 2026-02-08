# References cited in notes

## Al-Rfou et al. (2018)
- Rami Al-Rfou, Dokook Choe, Noah Constant, Mandy Guo, and Llion Jones. 2018. Character-level language modeling with deeper self-attention. *arXiv preprint arXiv:1808.04444*.
- Cited in 01_introduction.md (auxiliary losses for deep Transformer character-level LM, outperforming LSTMs; fixed-length segments without cross-segment information flow), 03a_vanilla-transformer-lm.md (vanilla model limitations, segment length a few hundred for char-level), 04_experiments.md (baseline on enwiki8, text8; 12L and 64L Transformer comparisons), 04b_ablation-study.md (absolute encoding baseline in Table 6), 04e_evaluation-speed.md (vanilla Transformer speed comparison in Table 9)

## Bai et al. (2018)
- Cited in 04_experiments.md (TCN baseline on WikiText-103 at 45.2 PPL)

## Baevski and Auli (2018)
- Alexei Baevski and Michael Auli. 2018. Adaptive input representations for neural language modeling. *arXiv preprint arXiv:1809.10853*.
- Cited in 04_experiments.md (adaptive softmax/input representations adopted; contemporary SoTA baseline on WikiText-103 at 20.5 PPL; baseline on One Billion Word at 24.1/23.7 PPL; outperformed by Transformer-XL on One Billion Word), 04b_ablation-study.md (contemporary method using vanilla Transformers, outperformed on One Billion Word)

## Bahdanau et al. (2014)
- Cited in 01_introduction.md (attention mechanisms might ease optimization and enable long-term dependency learning)

## Bengio et al. (2003)
- Cited in 02_related-work.md (novel architectures to better encode context)

## Chelba et al. (2013)
- Cited in 04_experiments.md (One Billion Word dataset; RNN-1024 + 9 Gram baseline at 51.3 PPL)

## Cooijmans et al. (2016)
- Cited in 04_experiments.md (BN-LSTM baseline on text8 at 1.36 bpc)

## Chung et al. (2016)
- Cited in 04_experiments.md (LN HM-LSTM baseline on enwiki8 at 1.32 bpc, text8 at 1.29 bpc)

## Dai and Le (2015)
- Cited in 01_introduction.md (unsupervised pretraining)

## Dauphin et al. (2016)
- Cited in 04_experiments.md (GCNN-8 and GCNN-14 baselines on WikiText-103; GCNN-14 bottleneck on One Billion Word)

## Devlin et al. (2018)
- Cited in 01_introduction.md (unsupervised pretraining), 03a_vanilla-transformer-lm.md (standard practice of chunking text into fixed-length segments)

## Dieng et al. (2016)
- Cited in 02_related-work.md (document-level topics learned from data)

## Gal and Ghahramani (2016)
- Cited in 02_related-work.md (improving regularization and optimization algorithms)

## Grave et al. (2016a)
- Cited in 02_related-work.md (speeding up Softmax computation), 04_experiments.md (adaptive softmax adopted)

## Grave et al. (2016b)
- Cited in 04_experiments.md (LSTM and LSTM + Neural cache baselines on WikiText-103)

## Graves (2013)
- Cited in 01_introduction.md (gradient clipping technique)

## Graves et al. (2014)
- Cited in 03b_segment-level-recurrence.md (memory augmented neural networks, connection to cached memory)

## Ha et al. (2016)
- Cited in 04_experiments.md (LN HyperNetworks baseline on enwiki8 at 1.34 bpc)

## Hochreiter and Schmidhuber (1997)
- Cited in 01_introduction.md (LSTMs as standard solution for language modeling)

## Hochreiter et al. (2001)
- Cited in 01_introduction.md (gradient vanishing and explosion in RNNs)

## Huang et al. (2018)
- Cited in 03c_relative-positional-encodings.md (relative positional encodings explored in music generation)

## Ji et al. (2015)
- Cited in 02_related-work.md (manually defined context representations)

## Jozefowicz et al. (2016)
- Cited in 04_experiments.md (LSTM and LSTM + CNN Input baselines on One Billion Word)

## Ke et al. (2018)
- Cited in 02_related-work.md (augmented memory structure for long-term dependency)

## Khandelwal et al. (2018)
- Urvashi Khandelwal, He He, Peng Qi, and Dan Jurafsky. 2018. Sharp nearby, fuzzy far away: How neural language models use context. *arXiv preprint arXiv:1805.04623*.
- Cited in 01_introduction.md (LSTM language models use 200 context words on average), 04c_relative-effective-context-length.md (proposed the Effective Context Length metric)

## Knol (2017)
- Cited in 04_experiments.md (cmix v13 baseline on enwiki8 at 1.23 bpc)

## Krause et al. (2016)
- Cited in 04_experiments.md (Large mLSTM baseline on enwiki8 at 1.24 bpc, text8 at 1.27 bpc)

## Kuchaiev and Ginsburg (2017)
- Cited in 04_experiments.md (G-LSTM-2 baseline on One Billion Word at 36.0 PPL)

## Le et al. (2015)
- Cited in 02_related-work.md (better initialization for relieving vanishing gradient)

## Li et al. (2018)
- Cited in 02_related-work.md (modifying internal architecture of RNNs to ease optimization)

## LLC (2009)
- Cited in 04_experiments.md (enwiki8 and text8 datasets)

## Merity et al. (2016)
- Cited in 02_related-work.md (novel architectures), 04_experiments.md (WikiText-103 dataset), 10_appendix-e-generated-text.md (WikiText-103 data preprocessing procedure)

## Merity et al. (2017)
- Stephen Merity, Nitish Shirish Keskar, and Richard Socher. 2017. Regularizing and optimizing lstm language models. *arXiv preprint arXiv:1708.02182*.
- Cited in 04_experiments.md (AWD-LSTM baseline on Penn Treebank at 58.8 PPL; variational dropout and weight average technique adopted for Transformer-XL)

## Merity et al. (2018)
- Stephen Merity, Nitish Shirish Keskar, and Richard Socher. 2018. An analysis of neural language modeling at multiple scales. *arXiv preprint arXiv:1803.08240*.
- Cited in 04_experiments.md (QRNN baseline on WikiText-103 at 33.0 PPL), 04b_ablation-study.md (standard parameter budget reference for 151M setting)

## Mikolov and Zweig (2012)
- Cited in 02_related-work.md (manually defined context representations), 04_experiments.md (Penn Treebank dataset)

## Mikolov et al. (2010)
- Cited in 02_related-work.md (novel architectures), 03b_segment-level-recurrence.md (truncated BPTT for training RNN-LMs)

## Mujika et al. (2017)
- Cited in 04_experiments.md (FS-LSTM-4 baseline on enwiki8 at 1.25 bpc)

## Peters et al. (2018)
- Cited in 01_introduction.md (unsupervised pretraining), 03a_vanilla-transformer-lm.md (standard practice of chunking text into fixed-length segments)

## Radford et al. (2018)
- Cited in 01_introduction.md (unsupervised pretraining)

## Rae et al. (2018)
- Cited in 04_experiments.md (Hebbian + Cache baseline on WikiText-103 at 29.9 PPL)

## Shaw et al. (2018)
- Peter Shaw, Jakob Uszkoreit, and Ashish Vaswani. 2018. Self-attention with relative position representations. *arXiv preprint arXiv:1803.02155*.
- Cited in 03c_relative-positional-encodings.md (relative positional encodings in machine translation; only has terms (a) and (b), drops bias terms (c) and (d); merges W_k R into single trainable matrix, abandoning sinusoid inductive bias), 04b_ablation-study.md (encoding scheme compared in ablation Tables 6 and 7), 04c_relative-effective-context-length.md (encoding variant in RECL comparison Table 8), 08_appendix-c-recl-details.md (encoding variant label in Figures 3 and 4)

## Shazeer et al. (2014)
- Cited in 04_experiments.md (Sparse Non-Negative baseline on One Billion Word at 52.9 PPL)

## Shazeer et al. (2017)
- Cited in 04_experiments.md (Low-Budget MoE at 34.1 PPL and High-Budget MoE at 28.0 PPL on One Billion Word)

## Shazeer et al. (2018)
- Cited in 04_experiments.md (Mesh Tensorflow baseline on One Billion Word at 24.0 PPL)

## Trinh et al. (2018)
- Cited in 02_related-work.md (additional loss signal for relieving vanishing gradient)

## Vaswani et al. (2017)
- Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Lukasz Kaiser, and Illia Polosukhin. 2017. Attention is all you need. In *Advances in Neural Information Processing Systems*, pages 5998-6008.
- Cited in 01_introduction.md (attention mechanisms for long-term dependency), 03c_relative-positional-encodings.md (standard Transformer attention score decomposition; original sinusoid positional encoding), 04b_ablation-study.md (absolute encoding scheme compared in ablation Table 6)

## Wang and Cho (2015)
- Cited in 02_related-work.md (manually defined context representations)

## Wang et al. (2017)
- Cited in 02_related-work.md (document-level topics learned from data)

## Weston et al. (2014)
- Cited in 03b_segment-level-recurrence.md (memory augmented neural networks)

## Wu et al. (2016)
- Cited in 02_related-work.md (modifying internal architecture of RNNs to ease optimization)

## Yang et al. (2017)
- Zhilin Yang, Zihang Dai, Ruslan Salakhutdinov, and William W Cohen. 2017. Breaking the softmax bottleneck: A high-rank rnn language model. *arXiv preprint arXiv:1711.03953*.
- Cited in 02_related-work.md (enriching the output distribution family), 04_experiments.md (AWD-LSTM-MoS baseline on Penn Treebank at 55.97 PPL; MoS+Finetune at 54.44 PPL)

## Zilly et al. (2016)
- Julian Georg Zilly, Rupesh Kumar Srivastava, Jan Koutnık, and Jurgen Schmidhuber. 2016. Recurrent highway networks. *arXiv preprint arXiv:1607.03474*.
- Cited in 04_experiments.md (RHN baseline on enwiki8 at 1.27 bpc, text8 at 1.27 bpc; Variational RHN baseline on Penn Treebank at 65.4 PPL)

## Zoph and Le (2016)
- Barret Zoph and Quoc V Le. 2016. Neural architecture search with reinforcement learning. *arXiv preprint arXiv:1611.01578*.
- Cited in 04_experiments.md (NAS Cell baseline on Penn Treebank at 64.0 PPL)

## Inan et al. (2016)
- Hakan Inan, Khashayar Khosravi, and Richard Socher. 2016. Tying word vectors and word classifiers: A loss framework for language modeling. *arXiv preprint arXiv:1611.01462*.
- Cited in 04_experiments.md (Tied Variational LSTM baseline on Penn Treebank at 73.2 PPL)

## Pham et al. (2018)
- Hieu Pham, Melody Y Guan, Barret Zoph, Quoc V Le, and Jeff Dean. 2018. Efficient neural architecture search via parameter sharing. *arXiv preprint arXiv:1802.03268*.
- Cited in 04_experiments.md (Efficient NAS baseline on Penn Treebank at 58.6 PPL)

## Liu et al. (2018)
- Hanxiao Liu, Karen Simonyan, and Yiming Yang. 2018. Darts: Differentiable architecture search. *arXiv preprint arXiv:1806.09055*.
- Cited in 04_experiments.md (Differentiable NAS baseline on Penn Treebank at 56.1 PPL)

## Melis et al. (2018)
- Gabor Melis, Charles Blundell, Tomas Kociskv, Karl Moritz Hermann, Chris Dyer, and Phil Blunsom. 2018. Pushing the bounds of dropout. *arXiv preprint arXiv:1805.09208*.
- Cited in 04_experiments.md (Dropout tuning baseline on Penn Treebank at 55.3 PPL)
