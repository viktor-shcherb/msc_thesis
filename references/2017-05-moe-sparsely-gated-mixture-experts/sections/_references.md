# References

Only references actually cited in the section notes are included here.

---

**Abadi et al. (2016)**
Martin Abadi, Ashish Agarwal, Paul Barham, Eugene Brevdo, Zhifeng Chen, Craig Citro, Gregory S. Corrado, Andy Davis, Jeffrey Dean, Matthieu Devin, Sanjay Ghemawat, Ian J. Goodfellow, Andrew Harp, Geoffrey Irving, Michael Isard, Yangqing Jia, Rafal Jozefowicz, Lukasz Kaiser, Manjunath Kudlur, Josh Levenberg, Dan Mane, Rajat Monga, Sherry Moore, Derek Gordon Murray, Chris Olah, Mike Schuster, Jonathon Shlens, Benoit Steiner, Ilya Sutskever, Kunal Talwar, Paul A. Tucker, Vincent Vanhoucke, Vijay Vasudevan, Fernanda B. Viegas, Oriol Vinyals, Pete Warden, Martin Wattenberg, Martin Wicke, Yuan Yu, and Xiaoqiang Zheng. Tensorflow: Large-scale machine learning on heterogeneous distributed systems. *CoRR*, abs/1603.04467, 2016.
Cited in 05_experiments.md as the framework used for training (TensorFlow).

**Aljundi et al. (2016)**
Rahaf Aljundi, Punarjay Chakravarty, and Tinne Tuytelaars. Expert gate: Lifelong learning with a network of experts. *CoRR*, abs/1611.06194, 2016.
Cited in 01_introduction-and-related-work.md as an example of adding experts sequentially.

**Almahairi et al. (2015)**
A. Almahairi, N. Ballas, T. Cooijmans, Y. Zheng, H. Larochelle, and A. Courville. Dynamic Capacity Networks. *ArXiv e-prints*, November 2015.
Cited in 01_introduction-and-related-work.md as a prior conditional computation method.

**Amodei et al. (2015)**
Dario Amodei, Rishita Anubhai, Eric Battenberg, et al. Deep speech 2: End-to-end speech recognition in english and mandarin. *arXiv preprint arXiv:1512.02595*, 2015.
Cited in 01_introduction-and-related-work.md as evidence that scale improves accuracy in audio.

**Bahdanau et al. (2014)**
Dzmitry Bahdanau, Kyunghyun Cho, and Yoshua Bengio. Neural machine translation by jointly learning to align and translate. *arXiv preprint arXiv:1409.0473*, 2014.
Cited in 01_introduction-and-related-work.md as evidence that scale improves accuracy in text.

**Bengio et al. (2013)**
Yoshua Bengio, Nicholas Leonard, and Aaron Courville. Estimating or propagating gradients through stochastic neurons for conditional computation. *arXiv preprint arXiv:1308.3432*, 2013.
Cited in 01_introduction-and-related-work.md as a prior conditional computation method; in 02_structure-of-moe-layer.md regarding occasionally-sensitive behavior with noisy rectifiers.

**Bengio et al. (2015)**
Emmanuel Bengio, Pierre-Luc Bacon, Joelle Pineau, and Doina Precup. Conditional computation in neural networks for faster models. *arXiv preprint arXiv:1511.06297*, 2015.
Cited in 01_introduction-and-related-work.md as a prior conditional computation method using three loss terms; in 02_structure-of-moe-layer.md as related to block-wise dropout and as using boolean gates with REINFORCE; in 04_balancing-expert-utilization.md regarding soft constraint on batch-wise average of each gate and additional losses.

**Chelba et al. (2013)**
Ciprian Chelba, Tomas Mikolov, Mike Schuster, Qi Ge, Thorsten Brants, Phillipp Koehn, and Tony Robinson. One billion word benchmark for measuring progress in statistical language modeling. *arXiv preprint arXiv:1312.3005*, 2013.
Cited in 05_experiments.md as the source of the 1 Billion Word Language Modeling Benchmark dataset; in 09_appendix-c-1b-word-details.md for the holdout dataset evaluation procedure.

**Cho & Bengio (2014)**
K. Cho and Y. Bengio. Exponentially Increasing the Capacity-to-Computation Ratio for Conditional Computation in Deep Learning. *ArXiv e-prints*, June 2014.
Cited in 01_introduction-and-related-work.md as a prior conditional computation method; in 02_structure-of-moe-layer.md as related via parameterized weight matrix.

**Collobert et al. (2002)**
Ronan Collobert, Samy Bengio, and Yoshua Bengio. A parallel mixture of SVMs for very large scale problems. *Neural Computing*, 2002.
Cited in 01_introduction-and-related-work.md as an example of SVM-based expert architectures.

**Davis & Arel (2013)**
Andrew Davis and Itamar Arel. Low-rank approximations for conditional feedforward computation in deep neural networks. *arXiv preprint arXiv:1312.4461*, 2013.
Cited in 01_introduction-and-related-work.md as a prior conditional computation method.

**Durrani et al. (2014)**
Nadir Durrani, Barry Haddow, Philipp Koehn, and Kenneth Heafield. Edinburgh's phrase-based machine translation systems for wmt-14. In *Proceedings of the Ninth Workshop on Statistical Machine Translation*, 2014.
Cited in 05_experiments.md in Tables 2 and 3 as a PBMT baseline for WMT'14 En->Fr and En->De.

**Deisenroth & Ng (2015)**
Marc Peter Deisenroth and Jun Wei Ng. Distributed Gaussian processes. In *ICML*, 2015.
Cited in 01_introduction-and-related-work.md as an example of Gaussian Process expert architectures.

**Duchi et al. (2010)**
John Duchi, Elad Hazan, and Yoram Singer. Adaptive subgradient methods for online learning and stochastic optimization. *Journal of Machine Learning Research*, 2010.
Cited in 10_appendix-d-100b-word-details.md as an alternative optimizer to which the factored second-moment approximation could be applied.

**Eigen et al. (2013)**
David Eigen, Marc'Aurelio Ranzato, and Ilya Sutskever. Learning factored representations in a deep mixture of experts. *arXiv preprint arXiv:1312.4314*, 2013.
Cited in 01_introduction-and-related-work.md as introducing the idea of using multiple MoEs with their own gating networks as parts of a deep model and as the key prior work this paper builds on; in 04_balancing-expert-utilization.md regarding the self-reinforcing imbalance phenomenon and using a hard constraint.

**Garmash & Monz (2016)**
Ekaterina Garmash and Christof Monz. Ensemble learning for multi-source neural machine translation. In *staff.science.uva.nl/c.monz*, 2016.
Cited in 01_introduction-and-related-work.md as suggesting an ensemble model in the format of MoE for machine translation.

**Gers et al. (2000)**
Felix A. Gers, Jurgen A. Schmidhuber, and Fred A. Cummins. Learning to forget: Continual prediction with lstm. *Neural Computation*, 2000.
Cited in 05_experiments.md regarding LSTM baseline models; in 09_appendix-c-1b-word-details.md for the LSTM architecture in the 5-layer model.

**Gruslys et al. (2016)**
Audrunas Gruslys, Remi Munos, Ivo Danihelka, Marc Lanctot, and Alex Graves. Memory-efficient backpropagation through time. *CoRR*, abs/1606.03401, 2016.
Cited in 03_addressing-performance-challenges.md as describing a technique for reducing stored activations in an unrolled RNN.

**He et al. (2015)**
Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Deep residual learning for image recognition. *IEEE Conference on Computer Vision and Pattern Recognition*, 2015.
Cited in 09_appendix-c-1b-word-details.md for the residual connection encouraging gradient flow; in 11_appendix-e-mt-details.md for residual connections around LSTM and MoE layers.

**Hinton et al. (2012)**
Geoffrey Hinton, Li Deng, Dong Yu, George E. Dahl, Abdel-rahman Mohamed, Navdeep Jaitly, Andrew Senior, Vincent Vanhoucke, Patrick Nguyen, Tara N. Sainath, et al. Deep neural networks for acoustic modeling in speech recognition: The shared views of four research groups. *IEEE Signal Processing Magazine*, 2012.
Cited in 01_introduction-and-related-work.md as evidence that scale improves accuracy in audio.

**Hochreiter & Schmidhuber (1997)**
Sepp Hochreiter and Jurgen Schmidhuber. Long short-term memory. *Neural Computation*, 1997.
Cited in 01_introduction-and-related-work.md as the LSTM architecture used between MoE layers; in 05_experiments.md regarding LSTM baseline models; in 09_appendix-c-1b-word-details.md for the LSTM architecture in the 5-layer model.

**Ioffe & Szegedy (2015)**
Sergey Ioffe and Christian Szegedy. Batch normalization: Accelerating deep network training by reducing internal covariate shift. *arXiv preprint arXiv:1502.03167*, 2015.
Cited in 12_appendix-f-strictly-balanced-gating.md regarding the need to modify inference when using batchwise functions during training.

**Jacobs et al. (1991)**
Robert A. Jacobs, Michael I. Jordan, Steven J. Nowlan, and Geoffrey E. Hinton. Adaptive mixtures of local experts. *Neural Computing*, 1991.
Cited in 01_introduction-and-related-work.md as the original introduction of the mixture-of-experts approach.

**Jordan & Jacobs (1994)**
Michael I. Jordan and Robert A. Jacobs. Hierarchical mixtures of experts and the EM algorithm. *Neural Computing*, 1994.
Cited in 01_introduction-and-related-work.md as an early MoE reference; in 02_structure-of-moe-layer.md as the source of the Softmax gating function.

**Johnson et al. (2016)**
Melvin Johnson, Mike Schuster, Quoc V. Le, Maxim Krikun, Yonghui Wu, Zhifeng Chen, Nikhil Thorat, Fernanda B. Viegas, Martin Wattenberg, Greg Corrado, Macduff Hughes, and Jeffrey Dean. Google's multilingual neural machine translation system: Enabling zero-shot translation. *CoRR*, abs/1611.04558, 2016.
Cited in 05_experiments.md as the source of the multilingual translation dataset and single multilingual GNMT baseline (Section 5.4).

**Jozefowicz et al. (2016)**
Rafal Jozefowicz, Oriol Vinyals, Mike Schuster, Noam Shazeer, and Yonghui Wu. Exploring the limits of language modeling. *arXiv preprint arXiv:1602.02410*, 2016.
Cited in 01_introduction-and-related-work.md as evidence that scale improves accuracy in text; in 05_experiments.md as the previous state-of-the-art on the 1 Billion Word benchmark and in Table 1 caption; in 09_appendix-c-1b-word-details.md for baseline models marked with * in Table 7, importance sampling training of the softmax layer, and LSTM-2048-512 baseline.

**Kingma & Ba (2015)**
Diederik Kingma and Jimmy Ba. Adam: A method for stochastic optimization. In *ICLR*, 2015.
Cited in 09_appendix-c-1b-word-details.md, 10_appendix-d-100b-word-details.md, and 11_appendix-e-mt-details.md as the optimizer used for training.

**Kneser & Ney (1995)**
Reinhard Kneser and Hermann Ney. Improved backingoff for m-gram language modeling., 1995.
Cited in 10_appendix-d-100b-word-details.md for the Kneser-Ney smoothing baseline 5-gram model.

**Krizhevsky et al. (2012)**
Alex Krizhevsky, Ilya Sutskever, and Geoffrey E. Hinton. Imagenet classification with deep convolutional neural networks. In *NIPS*, 2012.
Cited in 01_introduction-and-related-work.md as evidence that scale improves accuracy in images.

**Le et al. (2012)**
Quoc V. Le, Marc'Aurelio Ranzato, Rajat Monga, Matthieu Devin, Kai Chen, Greg S. Corrado, Jeffrey Dean, and Andrew Y. Ng. Building high-level features using large scale unsupervised learning. In *ICML*, 2012.
Cited in 01_introduction-and-related-work.md as evidence that scale improves accuracy in images.

**Luong et al. (2015a)**
Minh-Thang Luong, Hieu Pham, and Christopher D. Manning. Effective approaches to attention-based neural machine translation. *EMNLP*, 2015a.
Cited in 05_experiments.md as previous work compared against in the WMT'14 benchmarks (Section 5.3); in 11_appendix-e-mt-details.md for the BLEU evaluation script.

**Luong et al. (2015b)**
Minh-Thang Luong, Ilya Sutskever, Quoc V. Le, Oriol Vinyals, and Wojciech Zaremba. Addressing the rare word problem in neural machine translation. *ACL*, 2015b.
Cited in 05_experiments.md in Table 2 as LSTM baselines (6-layer and 6-layer+PosUnk) for WMT'14 En->Fr.

**Ludovic Denoyer (2014)**
Patrick Gallinari Ludovic Denoyer. Deep sequential neural network. *arXiv preprint arXiv:1410.0510*, 2014.
Cited in 01_introduction-and-related-work.md as a prior conditional computation method.

**Rasmussen & Ghahramani (2002)**
Carl Edward Rasmussen and Zoubin Ghahramani. Infinite mixtures of Gaussian process experts. *NIPS*, 2002.
Cited in 01_introduction-and-related-work.md as work on infinite numbers of experts.

**Sak et al. (2014)**
Hasim Sak, Andrew W Senior, and Francoise Beaufays. Long short-term memory recurrent neural network architectures for large scale acoustic modeling. In *INTERSPEECH*, pp. 338-342, 2014.
Cited in 09_appendix-c-1b-word-details.md for the LSTM output projection technique used in the LSTM-2048-512 baseline and MoE-143M model.

**Schuster & Nakajima (2012)**
Mike Schuster and Kaisuke Nakajima. Japanese and Korean voice search. *ICASSP*, 2012.
Cited in 11_appendix-e-mt-details.md for the sub-word units (wordpieces) used for inputs and outputs.

**Shahbaba & Neal (2009)**
Babak Shahbaba and Radford Neal. Nonlinear models using dirichlet process mixtures. *JMLR*, 2009.
Cited in 01_introduction-and-related-work.md as an example of Dirichlet Process expert architectures.

**Sutskever et al. (2014)**
Ilya Sutskever, Oriol Vinyals, and Quoc V. Le. Sequence to sequence learning with neural networks. In *NIPS*, 2014.
Cited in 01_introduction-and-related-work.md as evidence that scale improves accuracy in text.

**Theis & Bethge (2015)**
Lucas Theis and Matthias Bethge. Generative image modeling using spatial LSTMs. In *NIPS*, 2015.
Cited in 01_introduction-and-related-work.md as an example of Gaussian Process expert architectures.

**Tresp (2001)**
Volker Tresp. Mixtures of Gaussian Processes. In *NIPS*, 2001.
Cited in 01_introduction-and-related-work.md as an example of Gaussian Process expert architectures.

**Wu et al. (2016)**
Yonghui Wu, Mike Schuster, Zhifeng Chen, Quoc V. Le, Mohammad Norouzi, et al. Google's neural machine translation system: Bridging the gap between human and machine translation. *arXiv preprint arXiv:1609.08144*, 2016.
Cited in 01_introduction-and-related-work.md as evidence that scale improves accuracy in text; in 05_experiments.md as the GNMT baseline model for machine translation experiments (Sections 5.3, 5.4), as the source of experimental protocols, and in Tables 2, 3, 4, and 5; in 11_appendix-e-mt-details.md as the base GNMT model, beam search source, and dropout procedure; in 13_appendix-g-attention-function.md for the GNMT attention function.

**Zhou et al. (2016)**
Jie Zhou, Ying Cao, Xuguang Wang, Peng Li, and Wei Xu. Deep recurrent models with fast-forward connections for neural machine translation. *arXiv preprint arXiv:1606.04199*, 2016.
Cited in 05_experiments.md in Tables 2 and 3 as DeepAtt and DeepAtt+PosUnk baselines for WMT'14 En->Fr and En->De.

**Yao et al. (2009)**
Bangpeng Yao, Dirk Walther, Diane Beck, and Li Fei-fei. Hierarchical mixture of classification experts uncovers interactions between brain regions. In *NIPS*, 2009.
Cited in 01_introduction-and-related-work.md as work on hierarchical expert structures.

**Zaremba et al. (2014)**
Wojciech Zaremba, Ilya Sutskever, and Oriol Vinyals. Recurrent neural network regularization. *arXiv preprint arXiv:1409.2329*, 2014.
Cited in 09_appendix-c-1b-word-details.md for the dropout technique applied to layer outputs; in 11_appendix-e-mt-details.md for dropout on embedding, LSTM and MoE layers.
