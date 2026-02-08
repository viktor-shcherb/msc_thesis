# References

Only references cited in the section notes are included here.

---

**Artetxe et al. (2021)**
M. Artetxe, S. Bhosale, N. Goyal, T. Mihaylov, M. Ott, S. Shleifer, X. V. Lin, J. Du, S. Iyer, R. Pasunuru, G. Anantharaman, X. Li, S. Chen, H. Akin, M. Baines, L. Martin, X. Zhou, P. S. Koura, B. O'Horo, J. Wang, L. Zettlemoyer, M. Diab, Z. Kozareva, and V. Stoyanov. Efficient Large Scale Language Modeling with Mixtures of Experts. arXiv:2112.10684, 2021.
Cited in 02_related-work.md as an example of large MoE models.

**Bender et al. (2021)**
E. M. Bender, T. Gebru, A. McMillan-Major, and S. Shmitchell. On the dangers of stochastic parrots: Can language models be too big? In Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency, pages 610-623, 2021.
Cited in 04_chinchilla.md in the context of risks of LLMs (gender bias and toxicity section).

**BIG-bench collaboration (2021)**
BIG-bench collaboration. Beyond the imitation game: Measuring and extrapolating the capabilities of language models. In preparation, 2021. URL https://github.com/google/BIG-bench/.
Cited in 04_chinchilla.md as a benchmark for evaluating Chinchilla (sections 4.2.1 and 4.2.4).

**Bisk et al. (2020)**
Y. Bisk, R. Zellers, J. Gao, Y. Choi, et al. PIQA: Reasoning about physical commonsense in natural language. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 34, pages 7432-7439, 2020.
Cited in 04_chinchilla.md as a common sense benchmark (section 4.2.5).

**Borgeaud et al. (2021)**
S. Borgeaud, A. Mensch, J. Hoffmann, T. Cai, E. Rutherford, K. Millican, G. van den Driessche, J.-B. Lespiau, B. Damoc, A. Clark, D. de Las Casas, A. Guy, J. Menick, R. Ring, T. Hennigan, S. Huang, L. Maggiore, C. Jones, A. Cassirer, A. Brock, M. Paganini, G. Irving, O. Vinyals, S. Osindero, K. Simonyan, J. W. Rae, E. Elsen, and L. Sifre. Improving language models by retrieving from trillions of tokens. arXiv 2112.04426, 2021.
Cited in 02_related-work.md as retrieval-augmented approach that effectively increases training data by ~10x.

**Bradbury et al. (2018)**
J. Bradbury, R. Frostig, P. Hawkins, M. J. Johnson, C. Leary, D. Maclaurin, G. Necula, A. Paszke, J. VanderPlas, S. Wanderman-Milne, and Q. Zhang. JAX: composable transformations of Python+NumPy programs. 2018. URL http://github.com/google/jax.
Cited in 04_chinchilla.md as the framework used for training all models.

**Brown et al. (2020)**
T. Brown, B. Mann, N. Ryder, M. Subbiah, J. D. Kaplan, P. Dhariwal, A. Neelakantan, P. Shyam, G. Sastry, A. Askell, S. Agarwal, A. Herbert-Voss, G. Krueger, T. Henighan, R. Child, A. Ramesh, D. Ziegler, J. Wu, C. Winter, C. Hesse, M. Chen, E. Sigler, M. Litwin, S. Gray, B. Chess, J. Clark, C. Berner, S. McCandlish, A. Radford, I. Sutskever, and D. Amodei. Language models are few-shot learners. In Advances in Neural Information Processing Systems, volume 33, pages 1877-1901, 2020.
Cited in 01_introduction.md and 02_related-work.md as GPT-3, one of the key large language models.

**Clark et al. (2019)**
C. Clark, K. Lee, M.-W. Chang, T. Kwiatkowski, M. Collins, and K. Toutanova. Boolq: Exploring the surprising difficulty of natural yes/no questions. In Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics, Volume 1, pages 2924-2936, 2019.
Cited in 04_chinchilla.md as one of the common sense benchmarks (BoolQ) in section 4.2.5.

**Clark et al. (2022)**
A. Clark, D. d. l. Casas, A. Guy, A. Mensch, M. Paganini, J. Hoffmann, B. Damoc, B. Hechtman, T. Cai, S. Borgeaud, G. v. d. Driessche, E. Rutherford, T. Hennigan, M. Johnson, K. Millican, A. Cassirer, C. Jones, E. Buchatskaya, D. Budden, L. Sifre, S. Osindero, O. Vinyals, J. Rae, E. Elsen, K. Kavukcuoglu, and K. Simonyan. Unified scaling laws for routed language models, 2022. URL https://arxiv.org/abs/2202.01169.
Cited in 02_related-work.md and 03_estimating-optimal-allocation.md on scaling properties of MoE models.

**Du et al. (2021)**
N. Du, Y. Huang, A. M. Dai, S. Tong, D. Lepikhin, Y. Xu, M. Krikun, Y. Zhou, A. W. Yu, O. Firat, B. Zoph, L. Fedus, M. Bosma, Z. Zhou, T. Wang, Y. E. Wang, K. Webster, M. Pellat, K. Robinson, K. Meier-Hellstern, T. Duke, L. Dixon, K. Zhang, Q. V. Le, Y. Wu, Z. Chen, and C. Cui. Glam: Efficient scaling of language models with mixture-of-experts, 2021. URL https://arxiv.org/abs/2112.06905.
Cited in 02_related-work.md as the 1.2T parameter GLaM MoE model.

**Fedus et al. (2021)**
W. Fedus, B. Zoph, and N. Shazeer. Switch transformers: Scaling to trillion parameter models with simple and efficient sparsity. arXiv preprint arXiv:2101.03961, 2021.
Cited in 02_related-work.md as the 1.7T parameter Switch transformer MoE model.

**Gao et al. (2020)**
L. Gao, S. Biderman, S. Black, L. Golding, T. Hoppe, C. Foster, J. Phang, H. He, A. Thite, N. Nabeshima, S. Presser, and C. Leahy. The Pile: An 800GB dataset of diverse text for language modeling. arXiv preprint arXiv:2101.00027, 2020.
Cited in 04_chinchilla.md as the evaluation dataset (The Pile) used in language modelling evaluation (section 4.2.1).

**Gehman et al. (2020)**
S. Gehman, S. Gururangan, M. Sap, Y. Choi, and N. A. Smith. RealToxicityPrompts: Evaluating neural toxic degeneration in language models. In Findings of the Association for Computational Linguistics: EMNLP 2020, pages 3356-3369, 2020.
Cited in 04_chinchilla.md in the sample toxicity analysis (section 4.2.7).

**Guu et al. (2020)**
K. Guu, K. Lee, Z. Tung, P. Pasupat, and M.-W. Chang. REALM: Retrieval-augmented language model pre-training, 2020.
Cited in 02_related-work.md as a retrieval-augmented approach.

**Hendrycks et al. (2020)**
D. Hendrycks, C. Burns, S. Basart, A. Zou, M. Mazeika, D. Song, and J. Steinhardt. Measuring massive multitask language understanding. arXiv preprint arXiv:2009.03300, 2020.
Cited in 04_chinchilla.md as the MMLU benchmark (sections 4.2.1 and 4.2.2).

**Hennigan et al. (2020)**
T. Hennigan, T. Cai, T. Norman, and I. Babuschkin. Haiku: Sonnet for JAX. 2020. URL http://github.com/deepmind/dm-haiku.
Cited in 04_chinchilla.md as the framework used for training models.

**Hernandez et al. (2021)**
D. Hernandez, J. Kaplan, T. Henighan, and S. McCandlish. Scaling laws for transfer, 2021.
Cited in 02_related-work.md on understanding scaling behaviour and transfer properties.

**Huber (1964)**
P. J. Huber. Robust Estimation of a Location Parameter. The Annals of Mathematical Statistics, 35(1):73-101, Mar. 1964.
Cited in 03_estimating-optimal-allocation.md as the loss function used for fitting the parametric model (Approach 3).

**Izacard and Grave (2020)**
G. Izacard and E. Grave. Distilling knowledge from reader to retriever for question answering, 2020.
Cited in 04_chinchilla.md as the open book SOTA baseline (FiD + Distillation) for TriviaQA (section 4.2.6).

**Joshi et al. (2017)**
M. Joshi, E. Choi, D. Weld, and L. Zettlemoyer. TriviaQA: A Large Scale Distantly Supervised Challenge Dataset for Reading Comprehension. arXiv e-prints, art. arXiv:1705.03551, 2017.
Cited in 04_chinchilla.md as the TriviaQA benchmark (section 4.2.6).

**Jouppi et al. (2017)**
N. P. Jouppi, C. Young, N. Patil, D. Patterson, G. Agrawal, R. Bajwa, S. Bates, S. Bhatia, N. Boden, et al. In-datacenter performance analysis of a tensor processing unit. In Proceedings of the 44th Annual International Symposium on Computer Architecture, ISCA '17, pages 1-12, 2017.
Cited in 04_chinchilla.md as the TPU hardware used for training.

**Kaplan et al. (2020)**
J. Kaplan, S. McCandlish, T. Henighan, T. B. Brown, B. Chess, R. Child, S. Gray, A. Radford, J. Wu, and D. Amodei. Scaling laws for neural language models. arXiv preprint arXiv:2001.08361, 2020.
Cited in 01_introduction.md, 02_related-work.md, and 03_estimating-optimal-allocation.md as the key prior work on scaling laws that this paper contrasts with.

**Kingma and Ba (2014)**
D. P. Kingma and J. Ba. Adam: A method for stochastic optimization. arXiv preprint arXiv:1412.6980, 2014.
Cited in 04_chinchilla.md as the optimizer used for Gopher (replaced by AdamW for Chinchilla).

**Kudo and Richardson (2018)**
T. Kudo and J. Richardson. SentencePiece: A simple and language independent subword tokenizer and detokenizer for neural text processing. arXiv preprint arXiv:1808.06226, 2018.
Cited in 04_chinchilla.md as the tokenizer used for Chinchilla (slightly modified version).

**Kwiatkowski et al. (2019)**
T. Kwiatkowski, J. Palomaki, O. Redfield, M. Collins, A. Parikh, C. Alberti, D. Epstein, I. Polosukhin, M. Kelcey, J. Devlin, K. Lee, K. N. Toutanova, L. Jones, M.-W. Chang, A. Dai, J. Uszkoreit, Q. Le, and S. Petrov. Natural questions: a benchmark for question answering research. Transactions of the Association of Computational Linguistics, 2019.
Cited in 04_chinchilla.md as the Natural Questions benchmark (section 4.2.6).

**Lai et al. (2017)**
G. Lai, Q. Xie, H. Liu, Y. Yang, and E. Hovy. RACE: Large-scale ReAding comprehension dataset from examinations. In Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing, pages 785-794, 2017.
Cited in 04_chinchilla.md as the RACE-h and RACE-m reading comprehension benchmarks (section 4.2.3).

**Levine et al. (2020)**
Y. Levine, N. Wies, O. Sharir, H. Bata, and A. Shashua. The depth-to-width interplay in self-attention. arXiv preprint arXiv:2006.12467, 2020.
Cited in 02_related-work.md on optimal depth-to-width ratio.

**Lewis et al. (2020)**
P. Lewis, E. Perez, A. Piktus, F. Petroni, V. Karpukhin, N. Goyal, H. Kuttler, M. Lewis, W.-t. Yih, T. Rocktaschel, S. Riedel, and D. Kiela. Retrieval-augmented generation for knowledge-intensive nlp tasks. In Advances in Neural Information Processing Systems, volume 33, pages 9459-9474, 2020.
Cited in 02_related-work.md as a retrieval-augmented approach.

**Lieber et al. (2021)**
O. Lieber, O. Sharir, B. Lenz, and Y. Shoham. Jurassic-1: Technical details and evaluation. White Paper. AI21 Labs, 2021.
Cited in 01_introduction.md, 02_related-work.md, and 04_chinchilla.md as Jurassic-1 (178B), one of the large language models compared against.

**Lin et al. (2021)**
S. Lin, J. Hilton, and O. Evans. TruthfulQA: Measuring how models mimic human falsehoods. arXiv preprint arXiv:2109.07958, 2021.
Cited in 04_chinchilla.md as the TruthfulQA benchmark (section 4.2.5).

**Loshchilov and Hutter (2019)**
I. Loshchilov and F. Hutter. Decoupled weight decay regularization. In International Conference on Learning Representations, 2019. URL https://openreview.net/forum?id=Bkg6RiCqY7.
Cited in 04_chinchilla.md as the AdamW optimizer used for Chinchilla.

**McCandlish et al. (2018)**
S. McCandlish, J. Kaplan, D. Amodei, and O. D. Team. An empirical model of large-batch training, 2018.
Cited in 02_related-work.md on weak dependence between optimal batch size and model size.

**Merity et al. (2017)**
S. Merity, C. Xiong, J. Bradbury, and R. Socher. Pointer sentinel mixture models. International Conference on Learning Representations, 2017.
Cited in 04_chinchilla.md as the Wikitext103 benchmark (section 4.2.1).

**Mitchell et al. (2019)**
M. Mitchell, S. Wu, A. Zaldivar, P. Barnes, L. Vasserman, B. Hutchinson, E. Spitzer, I. D. Raji, and T. Gebru. Model cards for model reporting. In Proceedings of the conference on fairness, accountability, and transparency, pages 220-229, 2019.
Cited in 04_chinchilla.md regarding the Chinchilla model card in Table A8.

**Nocedal (1980)**
J. Nocedal. Updating Quasi-Newton Matrices with Limited Storage. Mathematics of Computation, 35(151):773-782, 1980.
Cited in 03_estimating-optimal-allocation.md as the L-BFGS algorithm used for fitting the parametric loss function.

**Paperno et al. (2016)**
D. Paperno, G. Kruszewski, A. Lazaridou, Q. N. Pham, R. Bernardi, S. Pezzelle, M. Baroni, G. Boleda, and R. Fernandez. The LAMBADA dataset: Word prediction requiring a broad discourse context, 2016.
Cited in 04_chinchilla.md as the LAMBADA benchmark (section 4.2.3).

**Rae et al. (2021)**
J. Rae, S. Borgeaud, T. Cai, K. Millican, J. Hoffmann, F. Song, J. Aslanides, S. Henderson, R. Ring, S. Young, E. Rutherford, T. Hennigan, J. Menick, A. Cassirer, R. Powell, G. van den Driessche, L. A. Hendricks, M. Rauh, P.-S. Huang, A. Glaese, J. Welbl, S. Dathathri, S. Huang, J. Uesato, J. Mellor, I. Higgins, A. Creswell, N. McAleese, A. Wu, E. Elsen, S. Jayakumar, E. Buchatskaya, D. Budden, E. Sutherland, K. Simonyan, L. Paganini, L. Sifre, L. Martens, X. L. Li, A. Kuncoro, A. Nematzadeh, E. Gribovskaya, D. Donato, A. Lazaridou, A. Mensch, J.-B. Lespiau, M. Tsimpoukelli, N. Grigorev, D. Fritz, T. Sottiaux, M. Pajarskas, T. Pohlen, Z. Gong, D. Toyama, C. de Masson d'Autume, Y. Li, T. Terzi, I. Babuschkin, A. Clark, D. de Las Casas, A. Guy, J. Bradbury, M. Johnson, L. Weidinger, I. Gabriel, W. Isaac, E. Lockhart, S. Osindero, L. Rimell, C. Dyer, O. Vinyals, K. Ayoub, J. Stanway, L. Bennett, D. Hassabis, K. Kavukcuoglu, and G. Irving. Scaling language models: Methods, analysis & insights from training Gopher. arXiv 2112.11446, 2021.
Cited extensively across 01_introduction.md, 02_related-work.md, 04_chinchilla.md, and 05_discussion-conclusion.md as the Gopher paper and primary comparison point.

**Raffel et al. (2020a)**
C. Raffel, N. Shazeer, A. Roberts, K. Lee, S. Narang, M. Matena, Y. Zhou, W. Li, and P. J. Liu. Exploring the limits of transfer learning with a unified text-to-text transformer. Journal of Machine Learning Research, 21(140):1-67, 2020a.
Cited in 02_related-work.md and 03_estimating-optimal-allocation.md as the C4 dataset used for additional IsoFLOP analysis.

**Rajbhandari et al. (2020)**
S. Rajbhandari, J. Rasley, O. Ruwase, and Y. He. Zero: Memory optimizations toward training trillion parameter models. In SC20: International Conference for High Performance Computing, Networking, Storage and Analysis, pages 1-16. IEEE, 2020.
Cited in 04_chinchilla.md regarding the distributed optimiser state used for Chinchilla training.

**Rudinger et al. (2018)**
R. Rudinger, J. Naradowsky, B. Leonard, and B. Van Durme. Gender bias in coreference resolution. In Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, New Orleans, Louisiana, June 2018.
Cited in 04_chinchilla.md as the Winogender dataset used for gender bias evaluation (section 4.2.7).

**Sakaguchi et al. (2020)**
K. Sakaguchi, R. Le Bras, C. Bhagavatula, and Y. Choi. Winogrande: An adversarial winograd schema challenge at scale. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 34, pages 8732-8740, 2020.
Cited in 04_chinchilla.md as a common sense benchmark (section 4.2.5).

**Sap et al. (2019)**
M. Sap, H. Rashkin, D. Chen, R. LeBras, and Y. Choi. SocialIQA: Commonsense reasoning about social interactions. Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing, 2019.
Cited in 04_chinchilla.md as the SIQA common sense benchmark (section 4.2.5).

**Shallue et al. (2018)**
C. J. Shallue, J. Lee, J. Antognini, J. Sohl-Dickstein, R. Frostig, and G. E. Dahl. Measuring the effects of data parallelism on neural network training. arXiv preprint arXiv:1811.03600, 2018.
Cited in 02_related-work.md on using larger batch sizes.

**Smith et al. (2022)**
S. Smith, M. Patwary, B. Norick, P. LeGresley, S. Rajbhandari, J. Casper, Z. Liu, S. Prabhumoye, G. Zerveas, V. Korthikanti, E. Zhang, R. Child, R. Y. Aminabadi, J. Bernauer, X. Song, M. Shoeybi, Y. He, M. Houston, S. Tiwary, and B. Catanzaro. Using Deepspeed and Megatron to Train Megatron-turing NLG 530b, A Large-Scale Generative Language Model. arXiv preprint arXiv:2201.11990, 2022.
Cited in 01_introduction.md and 02_related-work.md as MT-NLG 530B, the largest dense transformer at the time.

**Steinhardt (2021)**
J. Steinhardt. Updates and lessons from AI forecasting, 2021. URL https://bounded-regret.ghost.io/ai-forecasting/.
Cited in 04_chinchilla.md as the source of expert forecasts for MMLU accuracy (section 4.2.2).

**Tay et al. (2021)**
Y. Tay, M. Dehghani, J. Rao, W. Fedus, S. Abnar, H. W. Chung, S. Narang, D. Yogatama, A. Vaswani, and D. Metzler. Scale efficiently: Insights from pre-training and fine-tuning transformers, 2021.
Cited in 01_introduction.md on the importance of accurately estimating model hyperparameters.

**Thoppilan et al. (2022)**
R. Thoppilan, D. D. Freitas, J. Hall, N. Shazeer, A. Kulshreshtha, H.-T. Cheng, A. Jin, T. Bos, L. Baker, Y. Du, Y. Li, H. Lee, H. S. Zheng, A. Ghafouri, M. Menegali, Y. Huang, M. Krikun, D. Lepikhin, J. Qin, D. Chen, Y. Xu, Z. Chen, A. Roberts, M. Bosma, Y. Zhou, C.-C. Chang, I. Krivokon, W. Rusch, M. Pickett, K. Meier-Hellstern, M. R. Morris, T. Doshi, R. D. Santos, T. Duke, J. Soraker, B. Zevenbergen, V. Prabhakaran, M. Diaz, B. Hutchinson, K. Olson, A. Molina, E. Hoffman-John, J. Lee, L. Aroyo, R. Rajakumar, A. Butryna, M. Lamm, V. Kuzmina, J. Fenton, A. Cohen, R. Bernstein, R. Kurzweil, B. Aguera-Arcas, C. Cui, M. Croak, E. Chi, and Q. Le. LaMDA: Language models for dialog applications, 2022.
Cited in 01_introduction.md and 02_related-work.md as LaMDA (137B), one of the large language models.

**Vaswani et al. (2017)**
A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, L. Kaiser, and I. Polosukhin. Attention is all you need. In Advances in neural information processing systems, pages 5998-6008, 2017.
Cited in 01_introduction.md as the original transformer architecture.

**Weidinger et al. (2021)**
L. Weidinger, J. Mellor, M. Rauh, C. Griffin, J. Uesato, P.-S. Huang, M. Cheng, M. Glaese, B. Balle, A. Kasirzadeh, Z. Kenton, S. Brown, W. Hawkins, T. Stepleton, C. Biles, A. Birhane, J. Haas, L. Rimell, L. A. Hendricks, W. Isaac, S. Legassick, G. Irving, and I. Gabriel. Ethical and social risks of harm from language models. arXiv submission, 2021.
Cited in 04_chinchilla.md in the context of risks of LLMs (section 4.2.7).

**Welbl et al. (2021)**
J. Welbl, A. Glaese, J. Uesato, S. Dathathri, J. Mellor, L. A. Hendricks, K. Anderson, P. Kohli, B. Coppin, and P.-S. Huang. Challenges in detoxifying language models. In Findings of the Association for Computational Linguistics: EMNLP 2021, pages 2447-2469, 2021.
Cited in 04_chinchilla.md regarding challenges in evaluating toxicity in LMs (section 4.2.7).

**Xu et al. (2021)**
A. Xu, E. Pathak, E. Wallace, S. Gururangan, M. Sap, and D. Klein. Detoxifying language models risks marginalizing minority voices. In Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, pages 2390-2397, 2021.
Cited in 04_chinchilla.md regarding challenges in evaluating toxicity in LMs (section 4.2.7).

**Yang et al. (2021)**
G. Yang, E. J. Hu, I. Babuschkin, S. Sidor, X. Liu, D. Farhi, N. Ryder, J. Pachocki, W. Chen, and J. Gao. Tuning large neural networks via zero-shot hyperparameter transfer. In Advances in Neural Information Processing Systems, 2021.
Cited in 02_related-work.md on choosing hyperparameters for autoregressive transformers.

**Zellers et al. (2019)**
R. Zellers, A. Holtzman, Y. Bisk, A. Farhadi, and Y. Choi. HellaSwag: Can a machine really finish your sentence? In Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics, 2019.
Cited in 04_chinchilla.md as the HellaSwag common sense benchmark (section 4.2.5).

**Zhang et al. (2019)**
G. Zhang, L. Li, Z. Nado, J. Martens, S. Sachdeva, G. Dahl, C. Shallue, and R. B. Grosse. Which algorithmic choices matter at which batch sizes? insights from a noisy quadratic model. In Advances in Neural Information Processing Systems, volume 32, 2019.
Cited in 02_related-work.md on using larger batch sizes.

**Zoph et al. (2022)**
B. Zoph, I. Bello, S. Kumar, N. Du, Y. Huang, J. Dean, N. Shazeer, and W. Fedus. Designing effective sparse expert models, 2022.
Cited in 02_related-work.md as an example of MoE models.
