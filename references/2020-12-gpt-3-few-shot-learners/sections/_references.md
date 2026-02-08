# References cited in section notes

This file contains only references that are actually cited in the section notes files.

---

- **[MCCD13]** Mikolov, Chen, Corrado, Dean. "Efficient Estimation of Word Representations in Vector Space," 2013.
  - Cited in 01_introduction.md as an early single-layer word vector representation approach.

- **[PSM14]** Pennington, Socher, Manning. "GloVe: Global Vectors for Word Representation," EMNLP 2014.
  - Cited in 01_introduction.md as an early single-layer word vector representation approach.

- **[DL15]** Dai, Le. "Semi-supervised Sequence Learning," NeurIPS 2015.
  - Cited in 01_introduction.md as an RNN-based approach with multiple layers of representations and contextual state; cited in 07_related-work.md as prefixLM algorithmic innovation.

- **[MBXS17]** McCann, Bradbury, Xiong, Socher. "Learned in Translation: Contextualized Word Vectors," NeurIPS 2017.
  - Cited in 01_introduction.md as an RNN-based approach with multiple layers of representations.

- **[PNZtY18]** Matthew E. Peters, Mark Neumann, Luke Zettlemoyer, and Wen tau Yih. "Dissecting contextual word embeddings: Architecture and representation." 2018.
  - Cited in 01_introduction.md as an RNN-based approach with multiple layers of representations.

- **[VSP+17]** Vaswani, Shazeer, Parmar, et al. "Attention Is All You Need," NeurIPS 2017.
  - Cited in 01_introduction.md as the Transformer architecture enabling pre-trained language models; cited in 07_related-work.md as the 213M parameter original Transformer model.

- **[RNSS18]** Radford, Narasimhan, Salimans, Sutskever. "Improving Language Understanding by Generative Pre-Training" (GPT-1), 2018.
  - Cited in 01_introduction.md as a pre-trained model that removes the need for task-specific architectures; also cited for the 100M parameter scale milestone.

- **[DCLT18]** Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. "BERT: Pre-training of deep bidirectional transformers for language understanding." *arXiv preprint arXiv:1810.04805*, 2018.
  - Cited in 01_introduction.md as a pre-trained model removing the need for task-specific architectures; also cited for the 300M parameter scale milestone; cited in 07_related-work.md for the 300M parameter model and for denoising-based bidirectionality.

- **[HR18]** Jeremy Howard and Sebastian Ruder. "Universal language model fine-tuning for text classification." *arXiv preprint arXiv:1801.06146*, 2018.
  - Cited in 01_introduction.md as a pre-trained model removing the need for task-specific architectures.

- **[RSR+19]** Raffel, Shazeer, Roberts, et al. "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer" (T5), 2019.
  - Cited in 01_introduction.md as advancing the fine-tuning paradigm and achieving 11B parameters; cited in 02_approach.md for Common Crawl dataset and as baseline for evaluation parameters (beam search, binary classification framing); cited in 05_limitations.md for documenting improved fine-tuning performance using bidirectional architectures and denoising objectives; cited in 07_related-work.md for the 11B parameter model, fine-tuning on QA, presenting tasks in natural language via text-to-text, and encoder-decoder architectures.

- **[LOG+19]** Liu, Ott, Goyal, et al. "RoBERTa: A Robustly Optimized BERT Pretraining Approach," 2019.
  - Cited in 01_introduction.md as advancing the fine-tuning paradigm; cited in 07_related-work.md for improvements in data and training procedures.

- **[YDY+19]** Yang, Dai, Yang, et al. "XLNet: Generalized Autoregressive Pretraining for Language Understanding," NeurIPS 2019.
  - Cited in 01_introduction.md as advancing the fine-tuning paradigm; cited in 07_related-work.md for random permutations during training.

- **[LCG+19]** Zhenzhong Lan, Mingda Chen, Sebastian Goodman, Kevin Gimpel, Piyush Sharma, and Radu Soricut. "ALBERT: A lite BERT for self-supervised learning of language representations." *arXiv preprint arXiv:1909.11942*, 2019.
  - Cited in 01_introduction.md as advancing the fine-tuning paradigm; cited in 07_related-work.md for model compression (preserving performance while being as small as possible) and for efficiency increases in the embedding parameters.

- **[HLW+20]** Dan Hendrycks, Xiaoyuan Liu, Eric Wallace, Adam Dziedzic, Rishabh Krishnan, and Dawn Song. "Pretrained transformers improve out of distribution robustness." *arXiv preprint arXiv:2004.06100*, 2020.
  - Cited in 01_introduction.md for the observation that larger models do not necessarily generalize better out-of-distribution.

- **[YdC+19]** Dani Yogatama, Cyprien de Masson d'Autume, Jerome Connor, Tomas Kocisky, Mike Chrzanowski, Lingpeng Kong, Angeliki Lazaridou, Wang Ling, Lei Yu, Chris Dyer, et al. "Learning and evaluating general linguistic intelligence." *arXiv preprint arXiv:1901.11373*, 2019.
  - Cited in 01_introduction.md for evidence that generalization under the fine-tuning paradigm can be poor.

- **[MPL19]** McCoy, Pavlick, Linzen. "Right for the Wrong Reasons: Diagnosing Syntactic Heuristics in Natural Language Inference," ACL 2019.
  - Cited in 01_introduction.md and 02_approach.md for evidence of poor out-of-distribution generalization under fine-tuning.

- **[GSL+18]** Suchin Gururangan, Swabha Swayamdipta, Omer Levy, Roy Schwartz, Samuel R Bowman, and Noah A Smith. "Annotation artifacts in natural language inference data." *arXiv preprint arXiv:1803.02324*, 2018.
  - Cited in 01_introduction.md and 02_approach.md for evidence that fine-tuned models may exploit spurious features of training data.

- **[NK19]** Niven, Kao. "Probing Neural Network Comprehension of Natural Language Arguments," ACL 2019.
  - Cited in 01_introduction.md and 02_approach.md for evidence that benchmark performance may exaggerate actual task performance.

- **[RWC+19]** Radford, Wu, Child, et al. "Language Models are Unsupervised Multitask Learners" (GPT-2), 2019.
  - Cited in 01_introduction.md as introducing in-context learning and achieving 1.5B parameters; cited in 02_approach.md as the basis for the pre-training approach, in-context learning methodology, model architecture (Section 2.1), WebText dataset (Section 2.2), and PTB measurement baseline (Section 2.4); cited in 03_results.md as PTB SOTA baseline, LAMBADA context, and for stop-word filters addressing the LAMBADA continuation problem; cited in Table 3.2 as LAMBADA perplexity SOTA (8.63); cited in 03d_winograd-style-tasks.md for the "partial evaluation" method used on Winograd schemas; cited in 03i_synthetic-and-qualitative-tasks.md as prior work on generating synthetic news articles by conditional sampling; cited in 04_measuring-preventing-memorization.md for post-hoc overlap analysis on GPT-2 training data; cited in 07_related-work.md for the 1.5B parameter model, metalearning in language models, and utilizing multi-task instructions in natural language.

- **[SPP+19]** Shoeybi, Patwary, Puri, et al. "Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism," 2019.
  - Cited in 01_introduction.md for the 8B parameter scale milestone; cited in 03_results.md as a recent SOTA result on LAMBADA; cited in 03f_reading-comprehension.md (Table 3.7) as RACE-h SOTA (90.0) and RACE-m SOTA (93.1); cited in 07_related-work.md for the 8B parameter model.

- **[Tur20]** Turing NLG (Microsoft). 17 billion parameter language model, 2020.
  - Cited in 01_introduction.md for the 17B parameter scale milestone; cited in 03_results.md (Section 3.1.2) as a recent SOTA on LAMBADA and for arguing that continued scaling is not the path forward; cited in Table 3.2 as LAMBADA accuracy SOTA (68.0); cited in 07_related-work.md for the most recent 17B parameter model in the scaling line of work.

- **[KMH+20]** Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B. Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jeffrey Wu, and Dario Amodei. "Scaling laws for neural language models." 2020.
  - Cited in 01_introduction.md for evidence that log loss follows a smooth trend of improvement with scale and correlates well with many downstream tasks; cited in 02_approach.md for power-law scaling of validation loss (Section 2.1), sensitivity to architectural parameters (Section 2.1), training compute analysis and Figure 2.2 (Section 2.2), and batch size / learning rate scaling (Section 2.3); cited in 03_results.md for the power-law trend in training curves (Figure 3.1); cited in 07_related-work.md as one of several efforts studying the effect of scale on language model performance.

- **[HYC01]** Sepp Hochreiter, A Steven Younger, and Peter R Conwell. "Learning to Learn Using Gradient Descent." In *International Conference on Artificial Neural Networks*, pages 87-94. Springer, 2001.
  - Cited in 02_approach.md as related work on few-shot learning in other ML contexts; cited in 07_related-work.md for resemblance to the approach where an inner loop of adaptation takes place through computation in model activations without updating weights.

- **[VBL+16]** Vinyals, Blundell, Lillicrap, et al. "Matching Networks for One Shot Learning," NeurIPS 2016.
  - Cited in 02_approach.md as related work on few-shot learning in other ML contexts; cited in 07_related-work.md as matching networks in the extensive metalearning literature.

- **[CGRS19]** Child, Gray, Radford, Sutskever. "Generating Long Sequences with Sparse Transformers," 2019.
  - Cited in 02_approach.md (Section 2.1) as the Sparse Transformer whose alternating dense and locally banded sparse attention patterns are adopted in GPT-3.

- **[MKAT18]** McCandlish, Kaplan, Amodei, et al. "An Empirical Model of Large-Batch Training," 2018.
  - Cited in 02_approach.md (Section 2.3) for the gradient noise scale used to guide batch size choice, and for the observation that larger models can use larger batch sizes but require smaller learning rates.

- **[MKM+94]** Marcus, Kim, Marcinkiewicz, et al. "The Penn Treebank: Annotating Predicate Argument Structure," 1994.
  - Cited in 03_results.md (Section 3.1.1) as the Penn Tree Bank (PTB) language modeling dataset.

- **[PKL+16]** Paperno, Kruszewski, Lazaridou, et al. "The LAMBADA Dataset: Word Prediction Requiring a Broad Discourse Context," ACL 2016.
  - Cited in 03_results.md (Section 3.1.2) as the LAMBADA dataset for testing long-range dependencies.

- **[BHT+20]** Yonatan Bisk, Ari Holtzman, Jesse Thomason, Jacob Andreas, Yoshua Bengio, Joyce Chai, Mirella Lapata, Angeliki Lazaridou, Jonathan May, Aleksandr Nisnevich, et al. "Experience grounds language." *arXiv preprint arXiv:2004.10151*, 2020.
  - Cited in 03_results.md (Section 3.1.2) for reflecting on diminishing returns of scaling language models on the LAMBADA benchmark; cited in 05_limitations.md for noting that large pretrained language models lack grounding in other domains of experience.

- **[LDL19]** Zhongyang Li, Xiao Ding, and Ting Liu. "Story ending prediction by transferable bert." *arXiv preprint arXiv:1905.07504*, 2019.
  - Cited in 03_results.md (Table 3.2) as StoryCloze SOTA (91.8); cited in 03_results.md (Section 3.1.4) as the fine-tuned BERT-based SOTA on StoryCloze.

- **[LCH+20]** Xiaodong Liu, Hao Cheng, Pengcheng He, Weizhu Chen, Yu Wang, Hoifung Poon, and Jianfeng Gao. "Adversarial training for large neural language models." *arXiv preprint arXiv:2004.08994*, 2020.
  - Cited in 03_results.md (Table 3.2) as HellaSwag SOTA (85.6).

- **[ZHB+19]** Zellers, Holtzman, Bisk, et al. "HellaSwag: Can a Machine Really Finish Your Sentence?" ACL 2019.
  - Cited in 03_results.md (Section 3.1.3) as the HellaSwag dataset; notes that examples were adversarially mined to be difficult for language models while easy for humans (95.6% accuracy).

- **[ZHR+19]** Rowan Zellers, Ari Holtzman, Hannah Rashkin, Yonatan Bisk, Ali Farhadi, Franziska Roesner, and Yejin Choi. "Defending against neural fake news." *arXiv preprint arXiv:1905.12616*, 2019.
  - Cited in 03_results.md (Section 3.1.3) as a fine-tuned 1.5B parameter language model achieving 75.4% on HellaSwag; cited in 03i_synthetic-and-qualitative-tasks.md as GROVER, an automatic discriminator for detecting model generated text, and as similar work on human evaluation of machine-generated news articles.

- **[MCH+16]** Mostafazadeh, Chambers, He, et al. "A Corpus and Cloze Evaluation for Deeper Understanding of Commonsense Stories," NAACL 2016.
  - Cited in 03_results.md (Section 3.1.4) as the StoryCloze 2016 dataset.

- **[RRS20]** Roberts, Raffel, Shazeer. "How Much Knowledge Can You Pack Into the Parameters of a Language Model?" EMNLP 2020.
  - Cited in 03b_closed-book-qa.md as demonstrating that large language models can perform well on closed-book QA; cited as the source of the 3 QA datasets and splits used; cited in Table 3.3 as T5-11B+SSM baseline; cited in 05_limitations.md for demonstrating benefits of customizing prediction to entities of interest; cited in 07_related-work.md as a QA-focused work that fine-tuned an 11B parameter model.

- **[KPR+19]** Tom Kwiatkowski, Jennimaria Palomaki, Olivia Redfield, Michael Collins, Ankur Parikh, Chris Alberti, Danielle Epstein, Illia Polosukhin, Matthew Kelcey, Jacob Devlin, Kenton Lee, Kristina N. Toutanova, Llion Jones, Ming-Wei Chang, Andrew Dai, Jakob Uszkoreit, Quoc Le, and Slav Petrov. "Natural questions: a benchmark for question answering research." *Transactions of the Association of Computational Linguistics*, 2019.
  - Cited in 03b_closed-book-qa.md as the Natural Questions dataset; cited in 07_related-work.md as a question answering task.

- **[BCFL13]** Berant, Chou, Frostig, Liang. "Semantic Parsing on Freebase from Question-Answer Pairs," EMNLP 2013.
  - Cited in 03b_closed-book-qa.md as the WebQuestions dataset.

- **[JCWZ17]** Joshi, Choi, Weld, Zettlemoyer. "TriviaQA: A Large Scale Distantly Supervised Challenge Dataset for Reading Comprehension," ACL 2017.
  - Cited in 03b_closed-book-qa.md as the TriviaQA dataset.

- **[LPP+20]** Lewis, Perez, Piktus, et al. "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks" (RAG), 2020.
  - Cited in 03b_closed-book-qa.md as the open-domain fine-tuned SOTA using a learned retrieval mechanism over a 15.3B parameter dense vector index of 21M documents; cited in Table 3.3 and Figure 3.3 as the SOTA baseline; cited in 07_related-work.md as work that could be combined with in-context learning in the future.

- **[SHB15]** Sennrich, Haddow, Birch. "Improving Neural Machine Translation Models with Monolingual Data" (back-translation), ACL 2015.
  - Cited in 03c_translation.md for back-translation approach used in existing unsupervised machine translation.

- **[LC19]** Guillaume Lample and Alexis Conneau. "Cross-lingual language model pretraining." *arXiv preprint arXiv:1901.07291*, 2019.
  - Cited in 03c_translation.md (Table 3.4) as unsupervised NMT baseline.

- **[STQ+19]** Song, Tan, Qin, et al. "MASS: Masked Sequence to Sequence Pre-training for Language Generation," ICML 2019.
  - Cited in 03c_translation.md (Table 3.4) as unsupervised NMT baseline.

- **[LGG+20]** Yinhan Liu, Jiatao Gu, Naman Goyal, Xian Li, Sergey Edunov, Marjan Ghazvininejad, Mike Lewis, and Luke Zettlemoyer. "Multilingual denoising pre-training for neural machine translation." *arXiv preprint arXiv:2001.08210*, 2020.
  - Cited in 03c_translation.md (Table 3.4) as unsupervised NMT baseline; also cited as supervised SOTA for En->Ro and Ro->En.

- **[EOAG18]** Sergey Edunov, Myle Ott, Michael Auli, and David Grangier. "Understanding back-translation at scale." *arXiv preprint arXiv:1808.09381*, 2018.
  - Cited in 03c_translation.md (Table 3.4) as supervised SOTA for En->Fr (45.6).

- **[DHKH14]** Nadir Durrani, Barry Haddow, Philipp Koehn, and Kenneth Heafield. "Edinburgh's phrase-based machine translation systems for wmt-14." In *Proceedings of the Ninth Workshop on Statistical Machine Translation*, pages 97-104, 2014.
  - Cited in 03c_translation.md (Table 3.4) as supervised SOTA for Fr->En (35.0).

- **[WXH+18]** Yiren Wang, Yingce Xia, Tianyu He, Fei Tian, Tao Qin, ChengXiang Zhai, and Tie-Yan Liu. "Multi-agent dual learning." *ICLR 2019*, 2018.
  - Cited in 03c_translation.md (Table 3.4) as supervised SOTA for En->De (41.2).

- **[oR16]** University of Regensburg. Fascha, 2016.
  - Cited in 03c_translation.md (Table 3.4) as supervised SOTA for De->En (40.2).

- **[Pos18]** Post. "A Call for Clarity in Reporting BLEU Scores" (SacreBLEU), WMT 2018.
  - Cited in 03c_translation.md (Table 3.4 footnote) for SacreBLEU evaluation metric; results reported in Appendix H.

- **[LHCG19b]** Xiaodong Liu, Pengcheng He, Weizhu Chen, and Jianfeng Gao. "Multi-task deep neural networks for natural language understanding." *arXiv preprint arXiv:1901.11504*, 2019.
  - Cited in 03c_translation.md as the overall SOTA on Ro-En that few-shot GPT-3 performs within 0.5 BLEU of.

- **[LDM12]** Hector Levesque, Ernest Davis, and Leora Morgenstern. "The Winograd schema challenge." In *Thirteenth International Conference on the Principles of Knowledge Representation and Reasoning*, 2012.
  - Cited in 03d_winograd-style-tasks.md as the original Winograd Schemas Challenge.

- **[SBBC19]** Keisuke Sakaguchi, Ronan Le Bras, Chandra Bhagavatula, and Yejin Choi. "Winogrande: An adversarial winograd schema challenge at scale." 2019.
  - Cited in 03d_winograd-style-tasks.md (Table 3.5) as Winograd fine-tuned SOTA (90.1); also cited for the adversarially-mined Winogrande dataset and human performance on Winogrande (94.0%); also cited in 03e_common-sense-reasoning.md for PIQA contamination context; cited in 07_related-work.md as an adversarially constructed dataset designed to be difficult for existing language models.

- **[LYN+20]** Sheng-Chieh Lin, Jheng-Hong Yang, Rodrigo Nogueira, Ming-Feng Tsai, Chuan-Ju Wang, and Jimmy Lin. "Tttttackling winogrande schemas." *arXiv preprint arXiv:2003.08380*, 2020.
  - Cited in 03d_winograd-style-tasks.md (Table 3.5) as Winogrande fine-tuned SOTA (84.6).

- **[BZB+19]** Bisk, Zellers, Bras, et al. "PIQA: Reasoning about Physical Intuition in Natural Language," AAAI 2020.
  - Cited in 03e_common-sense-reasoning.md as the PhysicalQA (PIQA) dataset for probing grounded understanding of the physical world; cited in 05_limitations.md as a dataset where GPT-3 does well despite informal difficulty with "common sense physics".

- **[CCE+18]** Clark, Cowhey, Etzioni, et al. "Think you have Solved Question Answering? Try ARC, the AI2 Reasoning Challenge," 2018.
  - Cited in 03e_common-sense-reasoning.md as the ARC dataset of multiple-choice science exam questions (3rd to 9th grade); cited in 07_related-work.md as a question answering task.

- **[KKS+20]** Daniel Khashabi, Tushar Khot, Ashish Sabharwal, Oyvind Tafjord, Peter Clark, and Hannaneh Hajishirzi. "Unifiedqa: Crossing format boundaries with a single qa system." *arXiv preprint arXiv:2005.00700*, 2020.
  - Cited in 03e_common-sense-reasoning.md (Table 3.6) as the fine-tuned SOTA on ARC Easy (92.0), ARC Challenge (78.5), and OpenBookQA (87.2); also cited as RoBERTa baseline (55.9%) on ARC Challenge; cited in 07_related-work.md for pushing boundaries on certain tasks through multi-stage fine-tuning.

- **[MCKS18]** Mihaylov, Clark, Khot, Sabharwal. "Can a Suit of Armor Conduct Electricity? A New Dataset for Open Book Question Answering," EMNLP 2018.
  - Cited in 03e_common-sense-reasoning.md as the OpenBookQA dataset; cited in 07_related-work.md as a question answering task.

- **[RCM19]** Reddy, Chen, Manning. "CoQA: A Conversational Question Answering Challenge," TACL 2019.
  - Cited in 03f_reading-comprehension.md as the CoQA conversational reading comprehension dataset; cited in 07_related-work.md as a reading comprehension task.

- **[CHI+18]** Choi, He, Iyyer, et al. "QuAC: Question Answering in Context," EMNLP 2018.
  - Cited in 03f_reading-comprehension.md as the QuAC dataset requiring modeling structured dialog acts and answer span selections; cited in 07_related-work.md as a reading comprehension task.

- **[DWD+19]** Dheeru Dua, Yizhong Wang, Pradeep Dasigi, Gabriel Stanovsky, Sameer Singh, and Matt Gardner. "Drop: A reading comprehension benchmark requiring discrete reasoning over paragraphs." *arXiv preprint arXiv:1903.00161*, 2019.
  - Cited in 03f_reading-comprehension.md as the DROP dataset testing discrete reasoning and numeracy in reading comprehension.

- **[RLL+19]** Qiu Ran, Yankai Lin, Peng Li, Jie Zhou, and Zhiyuan Liu. "NumNet: Machine reading comprehension with numerical reasoning." In *Proceedings of EMNLP*, 2019.
  - Cited in 03f_reading-comprehension.md as state-of-the-art approaches on DROP that augment neural networks with symbolic systems.

- **[RJL18]** Rajpurkar, Jia, Liang. "Know What You Don't Know: Unanswerable Questions for SQuAD," ACL 2018.
  - Cited in 03f_reading-comprehension.md as the SQuAD 2.0 dataset.

- **[LXL+17]** Lai, Xie, Liu, et al. "RACE: Large-scale ReAding Comprehension Dataset From Examinations," EMNLP 2017.
  - Cited in 03f_reading-comprehension.md as the RACE dataset of middle school and high school English examinations.

- **[JZC+19]** Ying Ju, Fubang Zhao, Shijie Chen, Bowen Zheng, Xuefeng Yang, and Yunfeng Liu. "Technical report on conversational question answering." *arXiv preprint arXiv:1909.10772*, 2019.
  - Cited in 03f_reading-comprehension.md (Table 3.7) as CoQA fine-tuned SOTA (90.7 F1).

- **[JN20]** Zheng Junyuan and Gamma Lab NYC. "Numeric transformer - albert." March 2020.
  - Cited in 03f_reading-comprehension.md (Table 3.7) as DROP fine-tuned SOTA (89.1 F1).

- **[AI19]** WeChat AI. "Tr-mt (ensemble)." December 2019.
  - Cited in 03f_reading-comprehension.md (Table 3.7) as QuAC fine-tuned SOTA (74.4 F1).

- **[QIA20]** QIANXIN. "Sa-net on albert (ensemble)." April 2020.
  - Cited in 03f_reading-comprehension.md (Table 3.7) as SQuADv2 fine-tuned SOTA (93.0 F1).

- **[WPN+19]** Wang, Pruksachatkun, Nangia, et al. "SuperGLUE: A Stickier Benchmark for General-Purpose Language Understanding Systems," NeurIPS 2019.
  - Cited in 03g_superglue.md as the SuperGLUE benchmark suite.

- **[CLC+19]** Christopher Clark, Kenton Lee, Ming-Wei Chang, Tom Kwiatkowski, Michael Collins, and Kristina Toutanova. "BoolQ: Exploring the surprising difficulty of natural yes/no questions." *arXiv preprint arXiv:1905.10044*, 2019.
  - Cited in 03g_superglue.md as part of the SuperGLUE benchmark.

- **[DMST19]** Marie-Catherine De Marneffe, Mandy Simons, and Judith Tonhauser. "The CommitmentBank: Investigating projection in naturally occurring discourse." 2019. To appear in proceedings of Sinn und Bedeutung 23. Data at https://github.com/mcdm/CommitmentBank/.
  - Cited in 03g_superglue.md as part of the SuperGLUE benchmark.

- **[RBG11]** Melissa Roemmele, Cosmin Adrian Bejan, and Andrew S Gordon. "Choice of plausible alternatives: An evaluation of commonsense causal reasoning." In *2011 AAAI Spring Symposium Series*, 2011.
  - Cited in 03g_superglue.md as part of the SuperGLUE benchmark.

- **[KCR+18]** Daniel Khashabi, Snigdha Chaturvedi, Michael Roth, Shyam Upadhyay, and Dan Roth. "Looking beyond the surface: A challenge set for reading comprehension over multiple sentences." In *Proceedings of North American Chapter of the Association for Computational Linguistics (NAACL)*, 2018.
  - Cited in 03g_superglue.md as part of the SuperGLUE benchmark.

- **[ZLL+18]** Sheng Zhang, Xiaodong Liu, Jingjing Liu, Jianfeng Gao, Kevin Duh, and Benjamin Van Durme. "ReCoRD: Bridging the gap between human and machine commonsense reading comprehension." *arXiv preprint arXiv:1810.12885*, 2018.
  - Cited in 03g_superglue.md as part of the SuperGLUE benchmark.

- **[DGM06]** Ido Dagan, Oren Glickman, and Bernardo Magnini. "The PASCAL recognising textual entailment challenge." In *Machine learning challenges. evaluating predictive uncertainty, visual object classification, and recognising textual entailment*, pages 177-190. Springer, 2006.
  - Cited in 03g_superglue.md as part of the SuperGLUE benchmark.

- **[BHDD+06]** Roy Bar Haim, Ido Dagan, Bill Dolan, Lisa Ferro, Danilo Giampiccolo, Bernardo Magnini, and Idan Szpektor. "The second PASCAL recognising textual entailment challenge." 2006.
  - Cited in 03g_superglue.md as part of the SuperGLUE benchmark.

- **[GMDD07]** Danilo Giampiccolo, Bernardo Magnini, Ido Dagan, and Bill Dolan. "The third PASCAL recognizing textual entailment challenge." In *Proceedings of the ACL-PASCAL workshop on textual entailment and paraphrasing*, pages 1-9. Association for Computational Linguistics, 2007.
  - Cited in 03g_superglue.md as part of the SuperGLUE benchmark.

- **[BDD+09]** Luisa Bentivogli, Ido Dagan, Hoa Trang Dang, Danilo Giampiccolo, and Bernardo Magnini. "The fifth PASCAL recognizing textual entailment challenge." 2009.
  - Cited in 03g_superglue.md as part of the SuperGLUE benchmark.

- **[PCC18]** Pilehvar, Camacho-Collados. "WiC: The Word-in-Context Dataset for Evaluating Context-Sensitive Meaning Representations," NAACL 2019.
  - Cited in 03g_superglue.md as part of the SuperGLUE benchmark (WiC task).

- **[PHR+18]** Adam Poliak, Aparajita Haldar, Rachel Rudinger, J. Edward Hu, Ellie Pavlick, Aaron Steven White, and Benjamin Van Durme. "Collecting diverse natural language inference problems for sentence representation evaluation." In *Proceedings of EMNLP*, 2018.
  - Cited in 03g_superglue.md as part of the SuperGLUE benchmark.

- **[Fyo00]** Yaroslav Fyodorov. "A natural logic inference system." 2000. [Note: this citation key does not appear in the bibliography on pages 68-75; it may be cited only in passing or may use a different key in the bibliography.]
  - Cited in 03h_nli.md as foundational reference for Natural Language Inference (NLI).

- **[NWD+19]** Nie, Williams, Dinan, et al. "Adversarial NLI: A New Benchmark for Natural Language Understanding," ACL 2020.
  - Cited in 03h_nli.md as the ANLI dataset employing adversarially mined NLI questions in three rounds (R1, R2, R3); cited in 07_related-work.md as an adversarially constructed dataset.

- **[Nor09]** Peter Norvig. "Natural language corpus data." 2009.
  - Cited in 03i_synthetic-and-qualitative-tasks.md as the source for the top 10,000 most frequent words used in word scrambling tasks.

- **[TLBS03]** Peter D. Turney, Michael L. Littman, Jeffrey Bigham, and Victor Shnayder. "Combining independent modules to solve multiple-choice synonym and analogy problems." *CoRR*, cs.CL/0309035, 2003.
  - Cited in 03i_synthetic-and-qualitative-tasks.md as the source of 374 "SAT analogy" problems.

- **[TL05]** Peter D. Turney and Michael L. Littman. "Corpus-based learning of analogies and semantic relations." *CoRR*, abs/cs/0508103, 2005.
  - Cited in 03i_synthetic-and-qualitative-tasks.md for the average score of 57% among college applicants on SAT analogies (random guessing yields 20%).

- **[KMB20]** Sarah E. Kreps, Miles McCain, and Miles Brundage. "All the news that's fit to fabricate: Ai-generated text as a tool of media misinformation." 2020.
  - Cited in 03i_synthetic-and-qualitative-tasks.md as similar work on measuring human ability to distinguish model-generated news articles from real ones.

- **[IDCBE19]** Daphne Ippolito, Daniel Duckworth, Chris Callison-Burch, and Douglas Eck. "Automatic detection of generated text is easiest when humans are fooled." *arXiv preprint arXiv:1911.00650*, 2019.
  - Cited in 03i_synthetic-and-qualitative-tasks.md for research indicating automatic discriminators may have greater success at detecting model generated text than human evaluators, and that human accuracy at detection increases as humans observe more tokens.

- **[GSR19]** Sebastian Gehrmann, Hendrik Strobelt, and Alexander M. Rush. "Gltr: Statistical detection and visualization of generated text." *arXiv preprint arXiv:1906.04043*, 2019.
  - Cited in 03i_synthetic-and-qualitative-tasks.md as an automatic discriminator for detecting model generated text.

- **[CB78]** Susan Carey and Elsa Bartlett. "Acquiring a single new word." *Proceedings of the Stanford Child Language Conference*, 1978.
  - Cited in 03i_synthetic-and-qualitative-tasks.md as a developmental linguistics study on the ability to learn and utilize new words.

- **[TL18]** Trieu H. Trinh and Quoc V. Le. "A simple method for commonsense reasoning." *arXiv preprint arXiv:1806.02847*, 2018.
  - Cited in 04_measuring-preventing-memorization.md as one of the first papers to train a language model on Common Crawl data that detected and removed a training document overlapping with an evaluation dataset.

- **[ZSW+19a]** Daniel M. Ziegler, Nisan Stiennon, Jeffrey Wu, Tom B. Brown, Alec Radford, Dario Amodei, Paul Christiano, and Geoffrey Irving. "Fine-tuning language models from human preferences." 2019.
  - Cited in 05_limitations.md as a promising future direction for learning the objective function from humans.

- **[CLY+19]** Yen-Chun Chen, Linjie Li, Licheng Yu, Ahmed El Kholy, Faisal Ahmed, Zhe Gan, Yu Cheng, and Jingjing Liu. "Uniter: Learning universal image-text representations." *arXiv preprint arXiv:1909.11740*, 2019.
  - Cited in 05_limitations.md as a promising future direction for adding additional modalities such as images to provide grounding.

- **[Lin20]** Tal Linzen. "How can we accelerate progress towards human-like linguistic generalization?" *arXiv preprint arXiv:2005.00955*, 2020.
  - Cited in 05_limitations.md for the observation that GPT-3 still sees much more text during pre-training than a human sees in their lifetime.

- **[HVD15]** Geoffrey Hinton, Oriol Vinyals, and Jeff Dean. "Distilling the knowledge in a neural network." *arXiv preprint arXiv:1503.02531*, 2015.
  - Cited in 05_limitations.md as a possible future direction for distillation of large models down to manageable size for specific tasks; cited in 07_related-work.md as a general approach to distillation of language models.

- **[LHCG19a]** Xiaodong Liu, Pengcheng He, Weizhu Chen, and Jianfeng Gao. "Improving multi-task deep neural networks via knowledge distillation for natural language understanding." *arXiv preprint arXiv:1904.09482*, 2019.
  - Cited in 05_limitations.md for noting that distillation is well-explored in general but has not been tried at the scale of hundreds of billions of parameters; cited in 06_broader-impacts.md for model distillation as a technique to bring down cost of large models.

- **[Ros12]** R.S. Ross. "Guide for conducting risk assessments." *NIST Special Publication*, 2012.
  - Cited in 06_broader-impacts.md for traditional security risk assessment frameworks used to analyze potential misuse of language models.

- **[SBC+19]** Irene Solaiman, Miles Brundage, Jack Clark, Amanda Askell, Ariel Herbert-Voss, Jeff Wu, Alec Radford, Gretchen Krueger, Jong Wook Kim, Sarah Kreps, Miles McCain, Alex Newhouse, Jason Blazakis, Kris McGuffie, and Jasmine Wang. "Release strategies and the social impacts of language models." 2019.
  - Cited in 06_broader-impacts.md for characterization of advanced persistent threats (APTs) as highly skilled and well-resourced groups with long-term agendas.

- **[Cra17]** Kate Crawford. "The trouble with bias." *NIPS 2017 Keynote*, 2017.
  - Cited in 06_broader-impacts.md for potential harms of biases in training data including entrenching existing stereotypes and producing demeaning portrayals.

- **[HZJ+19]** Po-Sen Huang, Huan Zhang, Ray Jiang, Robert Stanforth, Johannes Welbl, Jack Rae, Vishal Maini, Dani Yogatama, and Pushmeet Kohli. "Reducing sentiment bias in language models via counterfactual evaluation." *arXiv preprint arXiv:1911.03064*, 2019.
  - Cited in 06_broader-impacts.md (footnote 8) as prior work on evaluating fairness, bias, and representation in language models; also cited in Section 6.2.2 (Race) for prior research demonstrating that language models produce text of differing sentiment varying with features such as occupation; also cited in Section 6.2.4 for extensive literature on bias intervention.

- **[NBR20]** Moin Nadeem, Anna Bethke, and Siva Reddy. "Stereoset: Measuring stereotypical bias in pretrained language models." *arXiv preprint arXiv:2004.09456*, 2020.
  - Cited in 06_broader-impacts.md (footnote 8) as prior work on evaluating fairness, bias, and representation in language models.

- **[SCNP19]** Emily Sheng, Kai-Wei Chang, Premkumar Natarajan, and Nanyun Peng. "The woman worked as a babysitter: On biases in language generation." *arXiv preprint arXiv:1909.01326*, 2019.
  - Cited in 06_broader-impacts.md (footnote 8) as prior work on evaluating fairness, bias, and representation in language models.

- **[RNLVD18]** Rachel Rudinger, Jason Naradowsky, Brian Leonard, and Benjamin Van Durme. "Gender bias in coreference resolution." *arXiv preprint arXiv:1804.09301*, 2018.
  - Cited in 06_broader-impacts.md for the Winogender dataset used for pronoun resolution to study gender bias in GPT-3.

- **[LB02]** Edward Loper and Steven Bird. "Nltk: The natural language toolkit." 2002.
  - Cited in 06_broader-impacts.md (Section 6.2.1) for the POS tagger used to identify adjectives and adverbs in the co-occurrence analysis.

- **[BES10]** Baccianella, Esuli, Sebastiani. "SentiWordNet 3.0: An Enhanced Lexical Resource for Sentiment Analysis and Opinion Mining," LREC 2010.
  - Cited in 06_broader-impacts.md (Section 6.2.2) for Senti WordNet used to measure sentiment of co-occurring words in the racial bias analysis.

- **[MWZ+18]** Mitchell, Wu, Zaldivar, et al. "Model Cards for Model Reporting," 2018.
  - Cited in 06_broader-impacts.md (Section 6.2.4) as inspiration for characterizing model attributes with informative labels.

- **[QMZH19]** Yusu Qian, Urwa Muaz, Ben Zhang, and Jae Won Hyun. "Reducing gender bias in word-level language models with a gender-equalizing loss function." *arXiv preprint arXiv:1905.12801*, 2019.
  - Cited in 06_broader-impacts.md (Section 6.2.4) for extensive literature on bias intervention in language systems.

- **[BBDIW20]** Blodgett, Barocas, Daum III, Wallach (2020). [Note: this citation key does not appear in the bibliography on pages 68-75 under this exact key; the full entry was not found in pages 71-75.]
  - Cited in 06_broader-impacts.md (Section 6.2.4) for the need for research that engages with the lived experience of communities affected by NLP systems.

- **[GG19]** Hila Gonen and Yoav Goldberg. "Lipstick on a pig: Debiasing methods cover up systematic gender biases in word embeddings but do not remove them." *arXiv preprint arXiv:1903.03862*, 2019.
  - Cited in 06_broader-impacts.md (Section 6.2.4) for showing that purely metric-driven approaches to removing bias have blind spots.

- **[NvNvdG19]** Malvina Nissim, Rik van Noord, and Rob van der Goot. "Fair is better than sensational: Man is to doctor as woman is to doctor." *arXiv preprint arXiv:1905.09866*, 2019.
  - Cited in 06_broader-impacts.md (Section 6.2.4) for showing that purely metric-driven approaches to removing bias have blind spots.

- **[SDSE19]** Roy Schwartz, Jesse Dodge, Noah A. Smith, and Oren Etzioni. "Green AI." *CoRR*, abs/1907.10597, 2019.
  - Cited in 06_broader-impacts.md (Section 6.3) for advocating cognizance of the cost and efficiency of large models.

- **[HB20]** Daniel Hernandez and Tom Brown. "Ai and efficiency." May 2020.
  - Cited in 06_broader-impacts.md (Section 6.3) for algorithmic progress naturally increasing the efficiency of models over time.

- **[JVS+16]** Rafal Jozefowicz, Oriol Vinyals, Mike Schuster, Noam Shazeer, and Yonghui Wu. "Exploring the limits of language modeling." *arXiv preprint arXiv:1602.02410*, 2016.
  - Cited in 07_related-work.md as an early work that scaled LSTM-based language models to over a billion parameters.

- **[BLC13]** Yoshua Bengio, Nicholas Leonard, and Aaron C. Courville. "Estimating or propagating gradients through stochastic neurons for conditional computation." *Arxiv*, 2013.
  - Cited in 07_related-work.md for the conditional computation framework that enables increasing parameter count without proportional computation increase.

- **[SMM+17]** Shazeer, Mirhoseini, Maziarz, et al. "Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer," ICLR 2017.
  - Cited in 07_related-work.md for the mixture-of-experts method used to produce 100 billion parameter models.

- **[AJF19]** Roee Aharoni, Melvin Johnson, and Orhan Firat. "Massively multilingual neural machine translation." In *Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers)*, 2019.
  - Cited in 07_related-work.md for 50 billion parameter translation models using the mixture-of-experts approach.

- **[Gra16]** Graves (2016). "Adaptive Computation Time for Recurrent Neural Networks." [Note: this entry was not found in the bibliography pages 71-75; it may appear on earlier bibliography pages 68-70.]
  - Cited in 07_related-work.md as an example of increasing computation without increasing parameters.

- **[DGV+18]** Mostafa Dehghani, Stephan Gouws, Oriol Vinyals, Jakob Uszkoreit, and Lukasz Kaiser. "Universal transformers." *Arxiv*, 2018.
  - Cited in 07_related-work.md as an example of increasing computation without increasing parameters (universal transformer).

- **[RRBS19]** Jonathan S. Rosenfeld, Amir Rosenfeld, Yonatan Belinkov, and Nir Shavit. "A constructive prediction of the generalization error across scales." 2019.
  - Cited in 07_related-work.md as one of several efforts studying the effect of scale on language model performance.

- **[LWS+20]** Zhuohan Li, Eric Wallace, Sheng Shen, Kevin Lin, Kurt Keutzer, Dan Klein, and Joseph E. Gonzalez. "Train large, then compress: Rethinking model size for efficient training and inference of transformers." 2020.
  - Cited in 07_related-work.md as one of several efforts studying the effect of scale on language model performance.

- **[HNA+17]** Joel Hestness, Sharan Narang, Newsha Ardalani, Gregory Diamos, Heewoo Jun, Hassan Kianinejad, Md. Mostofa Ali Patwary, Yang Yang, and Yanqi Zhou. "Deep learning scaling is predictable, empirically." *arXiv preprint arXiv:1712.00409*, 2017.
  - Cited in 07_related-work.md as one of several efforts studying the effect of scale on language model performance.

- **[SDCW19]** Victor Sanh, Lysandre Debut, Julien Chaumond, and Thomas Wolf. "DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter." *arXiv preprint arXiv:1910.01108*, 2019.
  - Cited in 07_related-work.md as a task-specific approach to distillation of language models.

- **[JYS+19]** Xiaoqi Jiao, Yichun Yin, Lifeng Shang, Xin Jiang, Xiao Chen, Linlin Li, Fang Wang, and Qun Liu. "TinyBERT: Distilling BERT for natural language understanding." *arXiv preprint arXiv:1909.10351*, 2019.
  - Cited in 07_related-work.md as a task-specific approach to distillation of language models.

- **[KR16]** Yoon Kim and Alexander M. Rush. "Sequence-level knowledge distillation." *Arxiv*, 2016.
  - Cited in 07_related-work.md as a task-specific approach to distillation of language models.

- **[IBGC+14]** Mohit Iyyer, Jordan Boyd-Graber, Leonardo Claudino, Richard Socher, and Hal Daume III. "A neural network for factoid question answering over paragraphs." In *Empirical Methods in Natural Language Processing*, 2014.
  - Cited in 07_related-work.md as a question answering task.

- **[GLT+20]** Kelvin Guu, Kenton Lee, Zora Tung, Panupong Pasupat, and Ming-Wei Chang. "Realm: Retrieval-augmented language model pre-training." *arXiv preprint arXiv:2002.08909*, 2020.
  - Cited in 07_related-work.md for work that focused on attending over a large corpus of data at test time; differs from the authors' in-context learning focus but could be combined.

- **[DSC+16]** Yan Duan, John Schulman, Xi Chen, Peter L. Bartlett, Ilya Sutskever, and Pieter Abbeel. "RL^2: Fast reinforcement learning via slow reinforcement learning." *ArXiv*, abs/1611.02779, 2016.
  - Cited in 07_related-work.md as RL2 in the metalearning literature; the authors' approach of stuffing context with examples is most structurally similar to RL2.

- **[RL16]** Sachin Ravi and Hugo Larochelle. "Optimization as a model for few-shot learning." *ICLR 2017 (oral)*, 2016.
  - Cited in 07_related-work.md as metalearning work on learning to optimize.

- **[ADG+16]** Marcin Andrychowicz, Misha Denil, Sergio Gomez, Matthew W Hoffman, David Pfau, Tom Schaul, Brendan Shillingford, and Nando De Freitas. "Learning to learn by gradient descent by gradient descent." In *Advances in neural information processing systems*, pages 3981-3989, 2016.
  - Cited in 07_related-work.md as metalearning work on learning to optimize.

- **[LM17]** Ke Li and Jitendra Malik. "Learning to optimize neural nets." *arXiv preprint arXiv:1703.00441*, 2017.
  - Cited in 07_related-work.md as metalearning work on learning to optimize.

- **[FAL17]** Chelsea Finn, Pieter Abbeel, and Sergey Levine. "Model-agnostic meta-learning for fast adaptation of deep networks." *ArXiv*, abs/1703.03400, 2017.
  - Cited in 07_related-work.md as MAML in the extensive metalearning literature.

- **[RCP+17]** Scott Reed, Yutian Chen, Thomas Paine, Aaron van den Oord, SM Eslami, Danilo Rezende, Oriol Vinyals, and Nando de Freitas. "Few-shot autoregressive density estimation: Towards learning to learn distributions." *arXiv preprint arXiv:1710.10304*, 2017.
  - Cited in 07_related-work.md for few-shot auto-regressive density estimation.

- **[GWC+18]** Jiatao Gu, Yong Wang, Yun Chen, Kyunghyun Cho, and Victor OK Li. "Meta-learning for low-resource neural machine translation." *arXiv preprint arXiv:1808.08437*, 2018.
  - Cited in 07_related-work.md for studying low-resource NMT as a few-shot learning problem.

- **[SS20]** Timo Schick and Hinrich Schutze. "Exploiting cloze questions for few-shot text classification and natural language inference." *arXiv preprint arXiv:2001.07676*, 2020.
  - Cited in 07_related-work.md for prior work exploring ways of using pre-trained language models in combination with gradient descent to perform few-shot learning.

- **[XDH+19]** Qizhe Xie, Zihang Dai, Eduard Hovy, Minh-Thang Luong, and Quoc V. Le. "Unsupervised data augmentation for consistency training." 2019.
  - Cited in 07_related-work.md for UDA, a semi-supervised learning approach that also explores methods of fine-tuning with very little labeled data.

- **[MKXS18]** Bryan McCann, Nitish Shirish Keskar, Caiming Xiong, and Richard Socher. "The natural language decathlon: Multitask learning as question answering." *arXiv preprint arXiv:1806.08730*, 2018.
  - Cited in 07_related-work.md for first formalizing giving multi-task models instructions in natural language in a supervised setting.

- **[Car97]** Caruana (1997). "Multitask Learning," Machine Learning. [Note: this entry was not found on bibliography pages 71-75; it may appear on earlier bibliography pages 68-70.]
  - Cited in 07_related-work.md for multi-task learning as an approach to increasing generality and transfer-learning capability.

- **[LGH+15]** Luong, Le, Gulcehre, et al. (2015). "Representation learning using multi-task deep neural networks for semantic classification and information retrieval." In *Proceedings of the 2015 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies*, 2015. [Note: the PDF bibliography entry [LGH+15] lists Xiaodong Liu, Jianfeng Gao, Xiaodong He, Li Deng, Kevin Duh, and Ye-Yi Wang.]
  - Cited in 07_related-work.md for promising initial results in multi-task learning.

- **[LSP+18]** Peter J. Liu, Mohammad Saleh, Etienne Pot, Ben Goodrich, Ryan Sepassi, Lukasz Kaiser, and Noam Shazeer. "Generating Wikipedia by summarizing long sequences." *arXiv preprint arXiv:1801.10198*, 2018.
  - Cited in 07_related-work.md for promising initial results in multi-task learning.

- **[PFB18]** Jason Phang, Thibault Fevry, and Samuel R. Bowman. "Sentence encoders on STILTs: Supplementary training on intermediate labeled-data tasks." *arXiv preprint arXiv:1811.01088*, 2018.
  - Cited in 07_related-work.md for multi-stage fine-tuning becoming a standardized part of SOTA results on some datasets.

- **[TFR+17]** Josh Tobin, Rachel Fong, Alex Ray, Jonas Schneider, Wojciech Zaremba, and Pieter Abbeel. "Domain randomization for transferring deep neural networks from simulation to the real world." In *2017 IEEE/RSJ international conference on intelligent robots and systems (IROS)*, pages 23-30. IEEE, 2017.
  - Cited in 07_related-work.md as a possible future direction for generating a broader set of explicit tasks for multi-task learning through procedural generation.

- **[ZSW+19b]** Daniel M. Ziegler, Nisan Stiennon, Jeffrey Wu, Tom B. Brown, Alec Radford, Dario Amodei, Paul Christiano, and Geoffrey Irving. "Fine-tuning language models from human preferences." *ArXiv*, abs/1909.08593, 2019.
  - Cited in 07_related-work.md as a possible future direction for generating explicit tasks through human interaction.

- **[Mac92]** David MacKay. "Information-based objective functions for active data selection." *Neural Computation*, 1992.
  - Cited in 07_related-work.md as a possible future direction for generating explicit tasks through active learning.

- **[LLG+19]** Mike Lewis, Yinhan Liu, Naman Goyal, Marjan Ghazvininejad, Abdelrahman Mohamed, Omer Levy, Ves Stoyanov, and Luke Zettlemoyer. "Bart: Denoising sequence-to-sequence pre-training for natural language generation, translation, and comprehension." *arXiv preprint arXiv:1910.13461*, 2019.
  - Cited in 07_related-work.md as encoder-decoder architecture innovation in language models.

- **[DYY+19]** Zihang Dai, Zhilin Yang, Yiming Yang, Jaime G. Carbonell, Quoc V. Le, and Ruslan Salakhutdinov. "Transformer-xl: Attentive language models beyond a fixed-length context." *Arxiv*, 2019.
  - Cited in 07_related-work.md for architectures that improve the efficiency of sampling.

- **[LH17]** Ilya Loshchilov and Frank Hutter. "Decoupled weight decay regularization." *arXiv preprint arXiv:1711.05101*, 2017.
  - Cited in 11_appendix-b-model-training.md for weight decay of 0.1 used as regularization across all GPT-3 models.

- **[HBFC19]** Ari Holtzman, Jan Buys, Maxwell Forbes, and Yejin Choi. "The curious case of neural text degeneration." *CoRR*, abs/1904.09751, 2019.
  - Cited in 15_appendix-f-additional-samples.md for nucleus sampling used to generate poem completions (P = 0.9).
