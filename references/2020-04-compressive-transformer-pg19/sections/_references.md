# References cited in notes

## From 01_introduction.md

- **Richards and Frankland (2017)** — Richards, B. A. and Frankland, P. W. "The Persistence and Transience of Memory." *Neuron*, 2017. Cited in 01_introduction.md on memory compression in biological systems.

- **Rumelhart et al. (1986)** — Rumelhart, D. E., Hinton, G. E., and Williams, R. J. "Learning representations by back-propagating errors." *Nature*, 1986. Cited in 01_introduction.md as the origin of RNNs.

- **Hochreiter and Schmidhuber (1997)** — Hochreiter, S. and Schmidhuber, J. "Long Short-Term Memory." *Neural Computation*, 1997. Cited in 01_introduction.md as the most ubiquitous RNN variant.

- **Vaswani et al. (2017)** — Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L., and Polosukhin, I. "Attention Is All You Need." *NeurIPS*, 2017. Cited in 01_introduction.md, 02_related-work.md (implicitly), and 03_model.md as the foundational Transformer architecture.

- **Bahdanau et al. (2014)** — Bahdanau, D., Cho, K., and Bengio, Y. "Neural Machine Translation by Jointly Learning to Align and Translate." *ICLR*, 2015 (arXiv 2014). Cited in 01_introduction.md as originating the attention operator.

- **Dai et al. (2019)** — Dai, Z., Yang, Z., Yang, Y., Carbonell, J., Le, Q. V., and Salakhutdinov, R. "Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context." *ACL*, 2019. Cited in 01_introduction.md, 02_related-work.md, 03_model.md, 04_pg19-benchmark.md, and 05_experiments.md as the TransformerXL baseline that the Compressive Transformer builds upon.

- **Shoeybi et al. (2019)** — Shoeybi, M., Patwary, M., Puri, R., LeGresley, P., Casper, J., and Catanzaro, B. "Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism." arXiv, 2019. Cited in 01_introduction.md for state-of-the-art language modelling; cited in 05_experiments.md (Section 5.3) for 8B-parameter model achieving 10.7 perplexity on WikiText-103.

- **Zhou et al. (2018)** — Zhou, L., Zhou, Y., Corso, J. J., Socher, R., and Xiong, C. "End-to-End Dense Video Captioning with Masked Transformer." *CVPR*, 2018. Cited in 01_introduction.md for video captioning.

- **Devlin et al. (2018)** — Devlin, J., Chang, M.-W., Lee, K., and Toutanova, K. "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding." *NAACL*, 2019 (arXiv 2018). Cited in 01_introduction.md and 04_pg19-benchmark.md for language understanding benchmarks and training on BookCorpus.

- **Yang et al. (2019)** — Yang, Z., Dai, Z., Yang, Y., Carbonell, J., Salakhutdinov, R., and Le, Q. V. "XLNet: Generalized Autoregressive Pretraining for Language Understanding." *NeurIPS*, 2019. Cited in 01_introduction.md for language understanding benchmarks.

- **Rae et al. (2016)** — Rae, J. W., Hunt, J. J., Danihelka, I., Harley, T., Senior, A. W., Wayne, G., Graves, A., and Lillicrap, T. P. "Scaling Memory-Augmented Neural Networks with Sparse Access to External Memory." *NeurIPS*, 2016. Cited in 01_introduction.md for sparse access mechanisms.

- **Child et al. (2019)** — Child, R., Gray, S., Radford, A., and Sutskever, I. "Generating Long Sequences with Sparse Transformers." arXiv, 2019. Cited in 01_introduction.md, 02_related-work.md, and 05_experiments.md as the Sparse Transformer.

- **Sukhbaatar et al. (2019)** — Sukhbaatar, S., Grave, E., Bojanowski, P., and Joulin, A. "Adaptive Attention Span in Transformers." *ACL*, 2019. Cited in 01_introduction.md, 02_related-work.md, and 05_experiments.md for adaptive/dynamic attention spans; cited in 08_appendix-b-compressed-memory-sizes.md for WikiText-103 model parameters.

- **Lample et al. (2019)** — Lample, G., Sablayrolles, A., Ranzato, M. A., Denoyer, L., and Jegou, H. "Large Memory Layers with Product Keys." *NeurIPS*, 2019. Cited in 01_introduction.md for sparse access mechanisms.

- **Hutter (2012)** — Hutter, M. "The Human Knowledge Compression Contest." 2012. Cited in 01_introduction.md and 05_experiments.md as the Hutter Prize (Enwik8 benchmark source).

- **Merity et al. (2016)** — Merity, S., Xiong, C., Bradbury, J., and Socher, R. "Pointer Sentinel Mixture Models." *ICLR*, 2017 (arXiv 2016). Cited in 01_introduction.md and 04_pg19-benchmark.md as the source of WikiText-103 benchmark.

- **Oord et al. (2016)** — van den Oord, A., Dieleman, S., Zen, H., Simonyan, K., Vinyals, O., Graves, A., Kalchbrenner, N., Senior, A., and Kavukcuoglu, K. "WaveNet: A Generative Model for Raw Audio." arXiv, 2016. Cited in 01_introduction.md as a speech baseline; cited in 05_experiments.md (Section 5.6) and 06_conclusion.md as the speech modelling baseline.

- **Espeholt et al. (2018)** — Espeholt, L., Soyer, H., Munos, R., Simonyan, K., Mnih, V., Ward, T., Doron, Y., Firoiu, V., Harley, T., Dunning, I., Legg, S., and Kavukcuoglu, K. "IMPALA: Scalable Distributed Deep-RL with Importance Weighted Actor-Learner Architectures." *ICML*, 2018. Cited in 01_introduction.md and 05_experiments.md (Section 5.7) and 06_conclusion.md as the RL agent used with the Compressive Transformer.

## From 02_related-work.md

- **Wu et al. (2019)** — Wu, F., Fan, A., Baevski, A., Dauphin, Y. N., and Auli, M. "Pay Less Attention with Lightweight and Dynamic Convolutions." *ICLR*, 2019. Cited in 02_related-work.md for convolution-like attention replacement.

## From 03_model.md

- **Graves et al. (2016)** — Graves, A., Wayne, G., Reynolds, M., Harley, T., Danihelka, I., Grabska-Barwinska, A., Colmenarejo, S. G., Grefenstette, E., Ramirez, T., et al. "Hybrid computing using a neural network with dynamic external memory." *Nature*, 2016. Cited in 03_model.md as inspiration for the most-used compression scheme (Differentiable Neural Computer garbage collection).

## From 04_pg19-benchmark.md

- **Chelba et al. (2013)** — Chelba, C., Mikolov, T., Schuster, M., Ge, Q., Brants, T., Koehn, P., and Robinson, T. "One Billion Word Benchmark for Measuring Progress in Statistical Language Modeling." arXiv, 2013. Cited in 04_pg19-benchmark.md as the Billion Word Benchmark.

- **Mikolov et al. (2010)** — Mikolov, T., Karafiat, M., Burget, L., Cernocky, J., and Khudanpur, S. "Recurrent neural network based language model." *Interspeech*, 2010. Cited in 04_pg19-benchmark.md for Penn Treebank processing.

- **Grave et al. (2016)** — Grave, E., Joulin, A., and Usunier, N. "Improving Neural Language Models with a Continuous Cache." *ICLR*, 2017 (arXiv 2016). Cited in 04_pg19-benchmark.md as a WikiText-103 benchmark user.

- **Rae et al. (2018)** — Rae, J. W., Dyer, C., Dayan, P., and Lillicrap, T. P. "Fast Parametric Learning with Activation Memorization." *ICML*, 2018. Cited in 04_pg19-benchmark.md as a WikiText-103 benchmark user; cited in 05_experiments.md Table 6 as LSTM+Hebb. baseline on WikiText-103, and Table 7 as LSTM comparison source.

- **Bai et al. (2018b)** — Bai, S., Kolter, J. Z., and Koltun, V. "An Empirical Evaluation of Generic Convolutional and Recurrent Networks for Sequence Modeling." arXiv, 2018. Cited in 04_pg19-benchmark.md as a WikiText-103 benchmark user.

- **Hill et al. (2015)** — Hill, F., Bordes, A., Chopra, S., and Weston, J. "The Goldilocks Principle: Reading Children's Books with Explicit Memory Representations." *ICLR*, 2016 (arXiv 2015). Cited in 04_pg19-benchmark.md for the Children's Book Test.

- **Paperno et al. (2016)** — Paperno, D., Kruszewski, G., Dinu, A., Baroni, M., et al. "The LAMBADA dataset: Word prediction requiring a broad discourse context." *ACL*, 2016. Cited in 04_pg19-benchmark.md for the LAMBADA benchmark.

- **Zhu et al. (2015)** — Zhu, Y., Kiros, R., Zemel, R., Salakhutdinov, R., Urtasun, R., Torralba, A., and Fidler, S. "Aligning Books and Movies: Towards Story-like Visual Explanations by Watching Movies and Reading Books." *ICCV*, 2015. Cited in 04_pg19-benchmark.md for the BookCorpus dataset.

- **Kocisky et al. (2018)** — Kocisky, T., Schwarz, J., Blunsom, P., Dyer, C., Hermann, K. M., Melis, G., and Grefenstette, E. "The NarrativeQA Reading Comprehension Challenge." *TACL*, 2018. Cited in 04_pg19-benchmark.md for the NarrativeQA benchmark; cited in 06_conclusion.md as a potential pre-training target for PG-19.

- **Blei et al. (2003)** — Blei, D. M., Ng, A. Y., and Jordan, M. I. "Latent Dirichlet Allocation." *JMLR*, 3:993-1022, 2003. Cited in 04_pg19-benchmark.md for the LDA topic model used for qualitative analysis; cited in 10_appendix-d-pg19-topics.md for generating PG-19 topic words.

## From 05_experiments.md

- **Kingma and Ba (2014)** — Kingma, D. P. and Ba, J. "Adam: A Method for Stochastic Optimization." *ICLR*, 2015 (arXiv 2014). Cited in 05_experiments.md as the optimizer used.

- **Graves (2013)** — Graves, A. "Generating Sequences With Recurrent Neural Networks." arXiv, 2013. Cited in 05_experiments.md Table 4 as a baseline on Enwik8; also cited in 05_experiments.md (Section 5.3) for dynamic evaluation.

- **Ha et al. (2016)** — Ha, D., Dai, A., and Le, Q. V. "HyperNetworks." *ICLR*, 2017 (arXiv 2016). Cited in 05_experiments.md Table 4 as a baseline on Enwik8.

- **Chung et al. (2016)** — Chung, J., Ahn, S., and Bengio, Y. "Hierarchical Multiscale Recurrent Neural Networks." *ICLR*, 2017 (arXiv 2016). Cited in 05_experiments.md Table 4 as a baseline on Enwik8.

- **Kalchbrenner et al. (2016)** — Kalchbrenner, N., Espeholt, L., Simonyan, K., van den Oord, A., Graves, A., and Kavukcuoglu, K. "Neural Machine Translation in Linear Time." arXiv, 2016. Cited in 05_experiments.md Table 4 as ByteNet baseline on Enwik8.

- **Zilly et al. (2017)** — Zilly, J. G., Srivastava, R. K., Koutnık, J., and Schmidhuber, J. "Recurrent Highway Networks." *ICML*, 2017. Cited in 05_experiments.md Table 4 as a baseline on Enwik8.

- **Krause et al. (2016)** — Krause, B., Lu, L., Murray, I., and Renals, S. "Multiplicative LSTM for sequence modelling." *ICLR Workshop*, 2017 (arXiv 2016). Cited in 05_experiments.md Table 4 as mLSTM baseline on Enwik8.

- **Al-Rfou et al. (2019)** — Al-Rfou, R., Choe, D., Constant, N., Guo, M., and Jones, L. "Character-Level Language Modeling with Deeper Self-Attention." *AAAI*, 2019. Cited in 05_experiments.md Table 4 as 64L Transformer baseline on Enwik8.

- **Graves et al. (2014)** — Graves, A., Wayne, G., and Danihelka, I. "Neural Turing Machines." arXiv, 2014. Cited in 05_experiments.md Table 6 as LSTM baseline on WikiText-103.

- **Bai et al. (2018a)** — Bai, S., Kolter, J. Z., and Koltun, V. "Convolutional Sequence to Sequence Model Revisited." 2018. Cited in 05_experiments.md Table 6 as Temporal CNN baseline on WikiText-103.

- **Dauphin et al. (2016)** — Dauphin, Y. N., Fan, A., Auli, M., and Grefenstette, D. "Language Modeling with Gated Convolutional Networks." *ICML*, 2017 (arXiv 2016). Cited in 05_experiments.md Table 6 as GCNN-14 baseline on WikiText-103.

- **Bradbury et al. (2016)** — Bradbury, J., Merity, S., Xiong, C., and Socher, R. "Quasi-Recurrent Neural Networks." *ICLR*, 2017 (arXiv 2016). Cited in 05_experiments.md Table 6 as Quasi-RNN baseline on WikiText-103.

- **Santoro et al. (2018)** — Santoro, A., Faulkner, R., Raposo, D., Rae, J., Chrzanowski, M., Weber, T., Wierstra, D., Vinyals, O., Pascanu, R., and Lillicrap, T. "Relational recurrent neural networks." *NeurIPS*, 2018. Cited in 05_experiments.md Table 6 as RMC baseline on WikiText-103.

- **Baevski and Auli (2019)** — Baevski, A. and Auli, M. "Adaptive Input Representations for Neural Language Modeling." *ICLR*, 2019. Cited in 05_experiments.md Table 6 as Transformer baseline on WikiText-103.

- **Krause et al. (2019)** — Krause, B., Kahembwe, E., Murray, I., and Renals, S. "Dynamic Evaluation of Transformer Language Models." arXiv, 2019. Cited in 05_experiments.md (Section 5.3) for dynamic evaluation achieving 16.4 perplexity on WikiText-103.

- **Smith et al. (2018)** — Smith, S. L., Kindermans, P.-J., Ying, C., and Le, Q. V. "Don't Decay the Learning Rate, Increase the Batch Size." *ICLR*, 2018. Cited in 05_experiments.md (Section 5.5.1) for the preference of increasing batch size over learning rate decay.

- **Oord et al. (2018)** — van den Oord, A., Li, Y., Babuschkin, I., Simonyan, K., Vinyals, O., Kavukcuoglu, K., van den Driessche, G., Lockhart, E., Cobo, L. C., Stimberg, F., et al. "Parallel WaveNet: Fast High-Fidelity Speech Synthesis." *ICML*, 2018. Cited in 05_experiments.md (Section 5.6) as the production speech synthesis system at Google.

- **Beattie et al. (2016)** — Beattie, C., Leibo, J. Z., Teber, D., Ward, T., Wainwright, T., Lefrancq, H., Green, S., Valdes, V., Sadik, A., Schrittwieser, J., et al. "DeepMind Lab." arXiv, 2016. Cited in 05_experiments.md (Section 5.7) as the DMLab-30 environment for RL experiments.

## From appendix files

- **Holtzman et al. (2019)** — Holtzman, A., Buys, J., Forbes, M., and Choi, Y. "The Curious Case of Neural Text Degeneration." *arXiv preprint arXiv:1904.09751*, 2019. Cited in 11_appendix-e-pg19-samples.md for the Nucleus Sampling decoding strategy (p = 0.98) used to generate PG-19 samples.
