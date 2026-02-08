# References (cited in notes)

**[1]** Yoshua Bengio, Patrice Simard, and Paolo Frasconi. Learning long-term dependencies with gradient descent is difficult. *IEEE transactions on neural networks*, 5(2):157-166, 1994.
- Cited in 01_memory-modeling-and-prediction.md as a popular model for sequential prediction.
- Cited in 01e_related-work.md noting LSTMs forget the past exponentially quickly if "stable".

**[2]** S. Hochreiter and J. Schmidhuber. Long short-term memory. *Neural Computation*, 9(8):1735-1780, 1997.
- Cited in 01_memory-modeling-and-prediction.md as a specific class of RNNs.
- Cited in 01e_related-work.md as a model with explicit memory in the sequential prediction practice section.

**[3]** Felix A Gers, Jurgen Schmidhuber, and Fred Cummins. Learning to forget: Continual prediction with LSTM. *Neural computation*, 12(10):2451-2471, 2000.
- Cited in 01_memory-modeling-and-prediction.md as a specific class of RNNs.
- Cited in 01e_related-work.md as a model with explicit memory in the sequential prediction practice section.

**[4]** Alex Graves, Greg Wayne, and Ivo Danihelka. Neural turing machines. *arXiv preprint arXiv:1410.5401*, 2014.
- Cited in 01_memory-modeling-and-prediction.md as a model with explicit memory.
- Cited in 01e_related-work.md in the sequential prediction practice section.

**[5]** J. Weston, S. Chopra, and A. Bordes. Memory networks. In *International Conference on Learning Representations (ICLR)*, 2015.
- Cited in 01_memory-modeling-and-prediction.md as a model with explicit memory.
- Cited in 01e_related-work.md in the sequential prediction practice section.

**[6]** Alex Graves, Greg Wayne, Malcolm Reynolds, Tim Harley, Ivo Danihelka, Agnieszka Grabska-Barwinska, Sergio Gomez Colmenarejo, Edward Grefenstette, Tiago Ramalho, John Agapiou, et al. Hybrid computing using a neural network with dynamic external memory. *Nature*, 538(7626):471-476, 2016.
- Cited in 01_memory-modeling-and-prediction.md as a model with explicit memory.
- Cited in 01e_related-work.md in the sequential prediction practice section.

**[7]** D. Bahdanau, K. Cho, and Y. Bengio. Neural machine translation by jointly learning to align and translate. *arXiv preprint arXiv:1409.0473*, 2014.
- Cited in 01_memory-modeling-and-prediction.md as a model with explicit memory.
- Cited in 01e_related-work.md in the sequential prediction practice section.

**[8]** Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Lukasz Kaiser, and Illia Polosukhin. Attention is all you need. In *Advances in Neural Information Processing Systems*, pages 6000-6010, 2017.
- Cited in 01_memory-modeling-and-prediction.md as a model with explicit memory.
- Cited in 01e_related-work.md in the sequential prediction practice section.

**[9]** M. Luong, H. Pham, and C. D. Manning. Effective approaches to attention-based neural machine translation. In *Empirical Methods in Natural Language Processing (EMNLP)*, pages 1412-1421, 2015.
- Cited in 01_memory-modeling-and-prediction.md as evidence of model success; also cited in 01b_implications.md regarding empirical gains of RNNs.
- Cited in 01e_related-work.md as evidence of promising empirical performance.

**[10]** Y. Wu, M. Schuster, Z. Chen, Q. V. Le, M. Norouzi, W. Macherey, M. Krikun, Y. Cao, Q. Gao, K. Macherey, et al. Google's neural machine translation system: Bridging the gap between human and machine translation. *arXiv preprint arXiv:1609.08144*, 2016.
- Cited in 01_memory-modeling-and-prediction.md as evidence of model success; also cited in 01b_implications.md regarding empirical gains of RNNs.
- Cited in 01e_related-work.md as evidence of promising empirical performance.

**[11]** Zhe Chen and Matthew A Wilson. Deciphering neural codes of memory of sleep. *Trends in Neurosciences*, 2017.
- Cited in 01_memory-modeling-and-prediction.md regarding neuroscience efforts on memory.

**[12]** Zhe Chen, Andres D Grosmark, Hector Penagos, and Matthew A Wilson. Uncovering representations of sleep-associated hippocampal ensemble spike activity. *Scientific reports*, 6:32193, 2016.
- Cited in 01_memory-modeling-and-prediction.md regarding neuroscience efforts on memory.

**[13]** Matthew A Wilson, Bruce L McNaughton, et al. Reactivation of hippocampal ensemble memories during sleep. *Science*, 265(5172):676-679, 1994.
- Cited in 01_memory-modeling-and-prediction.md regarding neuroscience efforts on memory.

**[14]** Prahladh Harsha, Rahul Jain, David McAllester, and Jaikumar Radhakrishnan. The communication complexity of correlation. In *Twenty-Second Annual IEEE Conference on Computational Complexity (CCC'07)*, pages 10-23. IEEE, 2007.
- Cited in 01a_mutual-information-interpretation.md as evidence that mutual information is not a bound on required memory.

**[15]** R. Kneser and H. Ney. Improved backing-off for m-gram language modeling. In *International Conference on Acoustics, Speech, and Signal Processing (ICASSP)*, volume 1, pages 181-184, 1995.
- Cited in 01b_implications.md as an example of practically successful simple Markov models.

**[16]** S. F. Chen and J. Goodman. An empirical study of smoothing techniques for language modeling. In *Association for Computational Linguistics (ACL)*, 1996.
- Cited in 01b_implications.md as an example of practically successful simple Markov models.

**[17]** E. Mossel and S. Roch. Learning nonsingular phylogenies and hidden Markov models. In *Theory of computing*, pages 366-375, 2005.
- Cited in 01c_lower-bounds.md regarding the computational hardness of learning HMMs.

**[18]** Vitaly Feldman, Will Perkins, and Santosh Vempala. On the complexity of random satisfiability problems with planted solutions. In *Proceedings of the Forty-Seventh Annual ACM Symposium on Theory of Computing*, pages 77-86. ACM, 2015.
- Cited in 01c_lower-bounds.md as the source of the hardness conjecture underlying Theorem 2.
- Cited in 05_lower-bound-large-alphabets.md as the source of the CSP complexity definition, Conjecture 1, and proof for the class of statistical algorithms.
- Cited in 10_appendix-b-lower-bound-large-alphabets.md for the notation and setup of the CSP formulation (B.1) and the hardness setting with/without repetition (B.3).

**[19]** Sarah R Allen, Ryan O'Donnell, and David Witmer. How to refute a random CSP. In *Foundations of Computer Science (FOCS), 2015 IEEE 56th Annual Symposium on*, pages 689-708. IEEE, 2015.
- Cited in 01c_lower-bounds.md alongside [18] and [20].
- Cited in 05_lower-bound-large-alphabets.md as providing a SOS algorithm for refuting random CSPs beyond the $\tilde{\Omega}(n^{r/2})$ regime (showing tightness).

**[20]** Pravesh K Kothari, Ryuhei Mori, Ryan O'Donnell, and David Witmer. Sum of squares lower bounds for refuting any CSP. *arXiv preprint arXiv:1701.04521*, 2017.
- Cited in 01c_lower-bounds.md alongside [18] and [19].
- Cited in 05_lower-bound-large-alphabets.md as showing the SOS approach requires $\tilde{\Omega}(n^{r/2})$ clauses for refutation.

**[21]** Y. Kim, Y. Jernite, D. Sontag, and A. M. Rush. Character-aware neural language models. *arXiv preprint arXiv:1508.06615*, 2015.
- Cited in 01c_lower-bounds.md regarding the regime where $d$ is small compared to dependencies.

**[22]** Avrim Blum, Adam Kalai, and Hal Wasserman. Noise-tolerant learning, the parity problem, and the statistical query model. *Journal of the ACM (JACM)*, 50(4):506-519, 2003.
- Cited in 01c_lower-bounds.md regarding the parity-based lower bound and the superconstant factor lost in the exponent.
- Cited in 06_lower-bound-small-alphabets.md as the fastest algorithm for parity with noise, running in time and samples $2^{n / \log n}$.

**[23]** Ryan O'Donnell. *Analysis of boolean functions*. Cambridge University Press, 2014.
- Cited in 01d_future-directions.md regarding noise stability over product distributions.

**[24]** Eric Blais, Ryan ODonnell, and Karl Wimmer. Polynomial regression under arbitrary product distributions. *Machine learning*, 80(2-3):273-294, 2010.
- Cited in 01d_future-directions.md regarding noise stability over product distributions.

**[25]** Adam Tauman Kalai, Adam R Klivans, Yishay Mansour, and Rocco A Servedio. Agnostically learning halfspaces. *SIAM Journal on Computing*, 37(6):1777-1805, 2008.
- Cited in 01d_future-directions.md as a potential avenue for improved sample complexity.

**[26]** D. Hsu, S. M. Kakade, and T. Zhang. A spectral algorithm for learning hidden Markov models. In *Conference on Learning Theory (COLT)*, 2009.
- Cited in 01e_related-work.md in the parameter estimation section.

**[27]** A. Anandkumar, D. Hsu, and S. M. Kakade. A method of moments for mixture models and hidden Markov models. In *Conference on Learning Theory (COLT)*, 2012.
- Cited in 01e_related-work.md in the parameter estimation section.

**[28]** H. Sedghi and A. Anandkumar. Training input-output recurrent neural networks through spectral methods. *arXiv preprint arXiv:1603.00954*, 2016.
- Cited in 01e_related-work.md in the parameter estimation section.

**[29]** M. Janzamin, H. Sedghi, and A. Anandkumar. Beating the perils of non-convexity: Guaranteed training of neural networks using tensor methods. *arXiv preprint arXiv:1506.08473*, 2015.
- Cited in 01e_related-work.md in the parameter estimation section.

**[30]** S. Arora, A. Bhaskara, R. Ge, and T. Ma. Provable bounds for learning some deep representations. In *International Conference on Machine Learning (ICML)*, pages 584-592, 2014.
- Cited in 01e_related-work.md in the parameter estimation section.

**[31]** N. Cesa-Bianchi and G. Lugosi. *Prediction, learning, and games*. Cambridge University Press, 2006.
- Cited in 01e_related-work.md in the universal prediction and information theory section.

**[32]** Daniel Russo and Benjamin Van Roy. An information-theoretic analysis of thompson sampling. *The Journal of Machine Learning Research*, 17(1):2442-2471, 2016.
- Cited in 01e_related-work.md as an analogous use of information-theoretic tools.

**[33]** A. Barron, J. Rissanen, and B. Yu. The minimum description length principle in coding and modeling. *IEEE Trans. Information Theory*, 44, 1998.
- Cited in 01e_related-work.md in the universal prediction and information theory section.

**[34]** P.D. Grunwald. A tutorial introduction to the minimum description length principle. *Advances in MDL: Theory and Applications*, 2005.
- Cited in 01e_related-work.md in the universal prediction and information theory section.

**[35]** A. Dawid. Statistical theory: The prequential approach. *J. Royal Statistical Society*, 1984.
- Cited in 01e_related-work.md in the universal prediction and information theory section; also cited as part of a list of works on regret in information-theoretic and statistical settings.

**[36]** Y. Shtarkov. Universal sequential coding of single messages. *Problems of Information Transmission*, 23, 1987.
- Cited in 01e_related-work.md regarding minimax rates; applicability limited to settings where number of strategies is relatively small.

**[37]** K. S. Azoury and M. Warmuth. Relative loss bounds for on-line density estimation with the exponential family of distributions. *Machine Learning*, 43(3), 2001.
- Cited in 01e_related-work.md as part of a list [35, 37, 38, 39, 40, 41, 42, 43].

**[38]** D. P. Foster. Prediction in the worst case. *Annals of Statistics*, 19, 1991.
- Cited in 01e_related-work.md as part of a list [35, 37, 38, 39, 40, 41, 42, 43].

**[39]** M. Opper and D. Haussler. Worst case prediction over sequences under log loss. *The Mathematics of Information Coding, Extraction and Distribution*, 1998.
- Cited in 01e_related-work.md as part of a list [35, 37, 38, 39, 40, 41, 42, 43].

**[40]** Nicolo Cesa-Bianchi and Gabor Lugosi. Worst-case bounds for the logarithmic loss of predictors. *Machine Learning*, 43, 2001.
- Cited in 01e_related-work.md as part of a list [35, 37, 38, 39, 40, 41, 42, 43].

**[41]** V. Vovk. Competitive on-line statistics. *International Statistical Review*, 69, 2001.
- Cited in 01e_related-work.md as part of a list [35, 37, 38, 39, 40, 41, 42, 43].

**[42]** S. M. Kakade and A. Y. Ng. Online bounds for bayesian algorithms. *Proceedings of Neural Information Processing Systems*, 2004.
- Cited in 01e_related-work.md as part of a list [35, 37, 38, 39, 40, 41, 42, 43].

**[43]** M. W. Seeger, S. M. Kakade, and D. P. Foster. Worst-case bounds for some non-parametric bayesian methods, 2005.
- Cited in 01e_related-work.md as part of a list [35, 37, 38, 39, 40, 41, 42, 43].

**[44]** B. S. Clarke and A. R. Barron. Information-theoretic asymptotics of Bayes methods. *IEEE Transactions on Information Theory*, 36(3):453-471, 1990.
- Cited in 01e_related-work.md regarding log-loss and statistical estimation.

**[45]** David Haussler and Manfred Opper. Mutual information, metric entropy and cumulative relative entropy risk. *Annals Of Statistics*, 25(6):2451-2492, 1997.
- Cited in 01e_related-work.md regarding log-loss and statistical estimation; specifically noted for mutual information characterizations of minimax risk in parametric i.i.d. settings.

**[46]** A. Barron. Information-theoretic characterization of Bayes performance and the choice of priors in parametric and nonparametric problems. In Bernardo, Berger, Dawid, and Smith, editors, *Bayesian Statistics 6*, pages 27-52, 1998.
- Cited in 01e_related-work.md regarding log-loss and statistical estimation.

**[47]** A. Barron, M. Schervish, and L. Wasserman. The consistency of posterior distributions in nonparametric problems. *Annals of Statistics*, 2(27):536-561, 1999.
- Cited in 01e_related-work.md regarding log-loss and statistical estimation.

**[48]** P. Diaconis and D. Freedman. On the consistency of Bayes estimates. *Annals of Statistics*, 14:1-26, 1986.
- Cited in 01e_related-work.md regarding log-loss and statistical estimation.

**[49]** T. Zhang. Learning bounds for a generalized family of Bayesian posterior distributions. *Proceedings of Neural Information Processing Systems*, 2006.
- Cited in 01e_related-work.md regarding log-loss and statistical estimation.

**[50]** J. Ziv and A. Lempel. Compression of individual sequences via variable-rate coding. *IEEE Transactions on Information Theory*, 1978.
- Cited in 01e_related-work.md as a different setting (block coding rather than prediction loss).

**[51]** D. Rumelhart, G. Hinton, and R. Williams. Learning representations by back-propagating errors. *Nature*, 323(6088):533-538, 1986.
- Cited in 01e_related-work.md in the sequential prediction practice section.

**[52]** Vitaly Feldman, Elena Grigorescu, Lev Reyzin, Santosh Vempala, and Ying Xiao. Statistical algorithms and a lower bound for detecting planted cliques. In *Proceedings of the forty-fifth annual ACM symposium on Theory of computing*, pages 655-664. ACM, 2013.
- Cited in 05_lower-bound-large-alphabets.md in footnote 4 regarding the statistical query model and statistical algorithms.

**[53]** Amit Daniely and Shai Shalev-Shwartz. Complexity theoretic limitations on learning DNF's. In *29th Annual Conference on Learning Theory*, pages 815-830, 2016.
- Cited in 05_lower-bound-large-alphabets.md as related work on using CSP hardness for learning lower bounds.

**[54]** Amit Daniely. Complexity theoretic limitations on learning halfspaces. In *Proceedings of the 48th Annual ACM SIGACT Symposium on Theory of Computing*, pages 105-117. ACM, 2016.
- Cited in 05_lower-bound-large-alphabets.md as related work on using CSP hardness for learning lower bounds.
