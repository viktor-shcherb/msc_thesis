# References cited in section notes

## Ainslie et al., 2020
- **Full citation:** Joshua Ainslie, Santiago Ontanon, Chris Alberti, Vaclav Cvicek, Zachary Fisher, Philip Pham, Anirudh Ravula, Sumit Sanghai, Qifan Wang, and Li Yang. ETC: Encoding Long and Structured Inputs in Transformers. EMNLP, 2020.
- **Cited in:** 02_related-work.md as a contemporaneous work using local + global attention (ETC); 06_tasks.md as contemporaneous leaderboard submission on HotpotQA (Table 9).

## Al-Rfou et al., 2018
- **Full citation:** Rami Al-Rfou, Dokook Choe, Noah Constant, Mandy Guo, and Llion Jones. Character-Level Language Modeling with Deeper Self-Attention. AAAI, 2018.
- **Cited in:** 04_autoregressive-language-modeling.md as baseline T12 model in Tables 2.

## Chen et al., 2016 (gradient checkpointing)
- **Full citation:** Tianqi Chen, Bing Xu, Chiyuan Zhang, and Carlos Guestrin. Training Deep Nets with Sublinear Memory Cost. arXiv preprint, abs/1604.06174, 2016.
- **Cited in:** 10_appendix-b-character-lm-hyperparameters.md as the gradient checkpointing method used to reduce memory usage during character LM training.

## Chen et al., 2017
- **Full citation:** Danqi Chen, Adam Fisch, Jason Weston, and Antoine Bordes. Reading Wikipedia to Answer Open-Domain Questions. ACL, 2017.
- **Cited in:** 02_related-work.md as a two-stage retrieval approach for QA.

## Chen et al., 2018
- **Full citation:** Tianqi Chen, Thierry Moreau, Ziheng Jiang, Lianmin Zheng, Eddie Yan, Haichen Shen, Meghan Cowan, Leyuan Wang, Yuwei Hu, Luis Ceze, et al. TVM: An Automated End-to-End Optimizing Compiler for Deep Learning. OSDI, 2018.
- **Cited in:** 03_longformer.md as the framework used to implement the custom CUDA kernel; 09_appendix-a-implementation-details.md as the TVM framework used to build the custom CUDA kernel.

## Chen et al., 2019
- **Full citation:** Jifan Chen, Shih-Ting Lin, and Greg Durrett. Multi-hop Question Answering via Reasoning Chains. arXiv preprint, abs/1910.02610, 2019.
- **Cited in:** 06_tasks.md as an example of complex task-specific architecture for HotpotQA.

## Child et al., 2019
- **Full citation:** Rewon Child, Scott Gray, Alec Radford, and Ilya Sutskever. Generating Long Sequences with Sparse Transformers. arXiv:1904.10509, 2019.
- **Cited in:** 02_related-work.md as the most similar attention pattern (Sparse Transformer); 04_autoregressive-language-modeling.md as baseline in Table 3; 10_appendix-b-character-lm-hyperparameters.md as architecture reference for the large model config (30 layers, 512 hidden size).

## Clark and Gardner, 2017
- **Full citation:** Christopher Clark and Matt Gardner. Simple and Effective Multi-Paragraph Reading Comprehension. ACL, 2017.
- **Cited in:** 02_related-work.md as a two-stage retrieval approach for multihop QA; 06_tasks.md as the loss function used for TriviaQA answer span prediction; 12_appendix-d-task-specific-model-details.md as the loss function used for TriviaQA distant supervision.

## Clark et al., 2019
- **Full citation:** Kevin Clark, Urvashi Khandelwal, Omer Levy, and Christopher D. Manning. What Does BERT Look At? An Analysis of BERT's Attention. arXiv preprint, abs/1906.04341, 2019.
- **Cited in:** 05_pretraining-and-finetuning.md as analysis showing BERT attention heads have strong bias to attending to local context, motivating position embedding copy initialization.

## Cohan et al., 2018
- **Full citation:** Arman Cohan, Franck Dernoncourt, Doo Soon Kim, Trung Bui, Seokhwan Kim, Walter Chang, and Nazli Goharian. A Discourse-Aware Attention Model for Abstractive Summarization of Long Documents. NAACL-HLT, 2018.
- **Cited in:** 01_introduction.md as the arXiv summarization dataset used to demonstrate LED effectiveness; 07_longformer-encoder-decoder.md as the arXiv summarization dataset used for LED evaluation.

## Dai and Le, 2015
- **Full citation:** Andrew M. Dai and Quoc V. Le. Semi-supervised Sequence Learning. NeurIPS, 2015.
- **Cited in:** 01_introduction.md as prior work on transfer learning.

## Dai et al., 2019
- **Full citation:** Zihang Dai, Zhilin Yang, Yiming Yang, Jaime G. Carbonell, Quoc V. Le, and Ruslan Salakhutdinov. Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context. ACL, 2019.
- **Cited in:** 01_introduction.md as prior work on generative language modeling; 04_autoregressive-language-modeling.md as prior work on long-sequence transformers and baseline in Table 2 and Table 3; evaluation protocol reference; 10_appendix-b-character-lm-hyperparameters.md as the Transformer-XL codebase used and architecture reference for the small model config.

## Devlin et al., 2019
- **Full citation:** Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. NAACL-HLT, 2019.
- **Cited in:** 01_introduction.md as prior work on discriminative language understanding and transfer learning; 06_tasks.md as the simple QA model followed for WikiHop and TriviaQA; 12_appendix-d-task-specific-model-details.md as the BERT QA model used for HotpotQA answer span extraction.

## Fang et al., 2020
- **Full citation:** Yuwei Fang, Siqi Sun, Zhe Gan, Rohit Pillai, Shuohang Wang, and Jingjing Liu. Hierarchical Graph Network for Multi-hop Question Answering. EMNLP, 2020.
- **Cited in:** 06_tasks.md as the current SOTA on HotpotQA (HGN) that Longformer-large underperforms by a point; Table 9; 12_appendix-d-task-specific-model-details.md as SOTA method on HotpotQA whose importance of paragraph selection is confirmed.

## Fisch et al., 2019
- **Full citation:** Adam Fisch, Alon Talmor, Robin Jia, Minjoon Seo, Eunsol Choi, and Danqi Chen. MRQA 2019 Shared Task: Evaluating Generalization in Reading Comprehension. MRQA workshop at EMNLP, 2019.
- **Cited in:** 06_tasks.md (footnote 7) noting that the full versions of TriviaQA and HotpotQA are used, not the simplified MRQA versions.

## Glass et al., 2019
- **Full citation:** Michael Glass, Alfio Massimiliano Gliozzo, Rishav Chakravarti, Anthony Ferritto, Lin Pan, Gaudani Bhargav, Dinesh Garg, and Avirup Sil. Span Selection Pre-training for Question Answering. arXiv preprint, abs/1909.04120, 2019.
- **Cited in:** 06_tasks.md as a baseline model (TAP 2) on HotpotQA (Table 9); as a non-GNN method outperformed by Longformer.

## Gray et al., 2017
- **Full citation:** Scott Gray, Alec Radford, and Diederik P. Kingma. GPU Kernels for Block-Sparse Weights. 2017.
- **Cited in:** 02_related-work.md as the BlockSparse library used by Sparse Transformer.

## Groeneveld et al., 2020
- **Full citation:** Dirk Groeneveld, Tushar Khot, Mausam, and Ashish Sabhwaral. A Simple Yet Strong Pipeline for HotpotQA. arXiv preprint, abs/2004.06753, 2020.
- **Cited in:** 06_tasks.md as an example of complex task-specific architecture (Quark); Table 9; as a non-GNN method outperformed by Longformer; 12_appendix-d-task-specific-model-details.md as the constrained decoding strategy used for HotpotQA evidence extraction at inference.

## Gupta and Berant, 2020
- **Full citation:** Ankit Gupta and Jonathan Berant. GMAT: Global Memory Augmentation for Transformers. arXiv, 2020.
- **Cited in:** 02_related-work.md as a contemporaneous work using global locations as global memory.

## Howard and Ruder, 2018
- **Full citation:** Jeremy Howard and Sebastian Ruder. Universal Language Model Fine-tuning for Text Classification. ACL, 2018.
- **Cited in:** 01_introduction.md as prior work on transfer learning.

## Joshi et al., 2017
- **Full citation:** Mandar Joshi, Eunsol Choi, Daniel S. Weld, and Luke Zettlemoyer. TriviaQA: A Large Scale Distantly Supervised Challenge Dataset for Reading Comprehension. ACL, 2017.
- **Cited in:** 06_tasks.md as the TriviaQA dataset (Wikipedia setting).

## Joshi et al., 2019
- **Full citation:** Mandar Joshi, Omer Levy, Luke Zettlemoyer, and Daniel Weld. BERT for Coreference Resolution: Baselines and Analysis. EMNLP-IJCNLP, 2019.
- **Cited in:** 02_related-work.md as a chunking approach that processes chunks separately and combines activations; 06_tasks.md as the coreference resolution model adapted for Longformer; 12_appendix-d-task-specific-model-details.md as the coarse-to-fine BERT coreference model adapted for Longformer.

## Kiesel et al., 2019
- **Full citation:** Johannes Kiesel, Maria Mestre, Rishabh Shukla, Emmanuel Vincent, Payam Adineh, David Corney, Benno Stein, and Martin Potthast. SemEval-2019 Task 4: Hyperpartisan News Detection. Proceedings of the 13th International Workshop on Semantic Evaluation, 2019.
- **Cited in:** 06_tasks.md as the Hyperpartisan news detection dataset.

## Kipf and Welling, 2017
- **Full citation:** Thomas N. Kipf and Max Welling. Semi-supervised Classification with Graph Convolutional Networks. ICLR, 2017.
- **Cited in:** 06_tasks.md noting that top-performing HotpotQA models use GNNs.

## Kitaev et al., 2020
- **Full citation:** Nikita Kitaev, Lukasz Kaiser, and Anselm Levskaya. Reformer: The Efficient Transformer. ICLR, 2020.
- **Cited in:** 04_autoregressive-language-modeling.md as baseline in Table 2 (enwik8) and as recent work justifying evaluation choices.

## Kovaleva et al., 2019
- **Full citation:** Olga Kovaleva, Alexey Romanov, Anna Rogers, and Anna Rumshisky. Revealing the Dark Secrets of BERT. EMNLP, 2019.
- **Cited in:** 03_longformer.md as motivation for the importance of local context in the sliding window design.

## Lee et al., 2018
- **Full citation:** Kenton Lee, Luheng He, and Luke Zettlemoyer. Higher-order Coreference Resolution with Coarse-to-fine Inference. NAACL, 2018.
- **Cited in:** 06_tasks.md as the original coreference system that was adapted (replacing ELMo with BERT) and then further adapted with Longformer; 12_appendix-d-task-specific-model-details.md as the original highly optimized custom GPU kernel used in the coreference TensorFlow implementation.

## Lewis et al., 2020
- **Full citation:** Mike Lewis, Yinhan Liu, Naman Goyal, Marjan Ghazvininejad, Abdelrahman Mohamed, Omer Levy, Veselin Stoyanov, and Luke Zettlemoyer. BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension. ACL, 2020.
- **Cited in:** 07_longformer-encoder-decoder.md as the pre-trained encoder-decoder model from which LED is initialized.

## Liu et al., 2019
- **Full citation:** Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke Zettlemoyer, and Veselin Stoyanov. RoBERTa: A Robustly Optimized BERT Pretraining Approach. arXiv:1907.11692, 2019.
- **Cited in:** 01_introduction.md and 05_pretraining-and-finetuning.md as the RoBERTa checkpoint used for continued pretraining.

## Maas et al., 2011
- **Full citation:** Andrew L. Maas, Raymond E. Daly, Peter T. Pham, Dan Huang, Andrew Y. Ng, and Christopher Potts. Learning Word Vectors for Sentiment Analysis. ACL, 2011.
- **Cited in:** 06_tasks.md as the IMDB sentiment classification dataset.

## Mahoney, 2009
- **Full citation:** Matt Mahoney. Large Text Compression Benchmark. 2009.
- **Cited in:** 04_autoregressive-language-modeling.md as the source of text8 and enwik8 benchmarks.

## Ott et al., 2019
- **Full citation:** Myle Ott, Sergey Edunov, Alexei Baevski, Angela Fan, Sam Gross, Nathan Ng, David Grangier, and Michael Auli. fairseq: A Fast, Extensible Toolkit for Sequence Modeling. NAACL System Demonstrations, 2019.
- **Cited in:** 05_pretraining-and-finetuning.md as the training framework used for pretraining.

## Peters et al., 2018
- **Full citation:** Matthew E. Peters, Mark Neumann, Mohit Iyyer, Matt Gardner, Christopher Clark, Kenton Lee, and Luke Zettlemoyer. Deep Contextualized Word Representations. NAACL, 2018.
- **Cited in:** 01_introduction.md as prior work on transfer learning.

## Pradhan et al., 2012
- **Full citation:** Sameer Pradhan, Alessandro Moschitti, Nianwen Xue, Olga Uryupina, and Yuchen Zhang. CoNLL-2012 Shared Task: Modeling Multilingual Unrestricted Coreference in OntoNotes. CoNLL, 2012.
- **Cited in:** 06_tasks.md as the OntoNotes coreference resolution dataset.

## Qiu et al., 2019
- **Full citation:** Jiezhong Qiu, Hao Ma, Omer Levy, Scott Wen-tau Yih, Sinong Wang, and Jie Tang. Blockwise Self-Attention for Long Document Understanding. EMNLP Findings, 2019.
- **Cited in:** 02_related-work.md as blockwise attention model that pretrained and evaluated on QA.

## Radford et al., 2019
- **Full citation:** Alec Radford, Jeff Wu, Rewon Child, David Luan, Dario Amodei, and Ilya Sutskever. Language Models are Unsupervised Multitask Learners. OpenAI, 2019.
- **Cited in:** 01_introduction.md as prior work on generative language modeling.

## Rae et al., 2020
- **Full citation:** Jack W. Rae, Anna Potapenko, Siddhant M. Jayakumar, Chloe Hillier, and Timothy P. Lillicrap. Compressive Transformers for Long-Range Sequence Modelling. ICLR, 2020.
- **Cited in:** 04_autoregressive-language-modeling.md as prior work on long-sequence transformers and baseline in Table 3 (Compressive Transformer).

## Raffel et al., 2020
- **Full citation:** Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, and Peter J. Liu. Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer. JMLR, 2020.
- **Cited in:** 07_longformer-encoder-decoder.md as T5, a pre-trained encoder-decoder model achieving strong summarization results.

## Roy et al., 2020
- **Full citation:** Aurko Roy, Mohammad Saffar, Ashish Vaswani, and David Grangier. Efficient Content-Based Sparse Attention with Routing Transformers. TACL, 2020.
- **Cited in:** 04_autoregressive-language-modeling.md as baseline in Table 3 (Routing).

## Shao et al., 2020
- **Full citation:** Nan Shao et al. C2F Reader. 2020.
- **Cited in:** 06_tasks.md as a top-performing GNN-based model on HotpotQA (Table 9).

## Sukhbaatar et al., 2019
- **Full citation:** Sainbayar Sukhbaatar, Edouard Grave, Piotr Bojanowski, and Armand Joulin. Adaptive Attention Span in Transformers. ACL, 2019.
- **Cited in:** 04_autoregressive-language-modeling.md as prior work on long-sequence transformers, baseline in Tables 2 and 3, and as model not suitable for pretrain-finetune paradigm; attention pattern design followed in section 4.1.

## Sutskever et al., 2014
- **Full citation:** Ilya Sutskever, Oriol Vinyals, and Quoc V. Le. Sequence to Sequence Learning with Neural Networks. NeurIPS, 2014.
- **Cited in:** 01_introduction.md as the foundational work on seq2seq learning motivating the LED variant; 07_longformer-encoder-decoder.md as the foundational seq2seq work.

## Trinh and Le, 2018
- **Full citation:** Trieu H. Trinh and Quoc V. Le. A Simple Method for Commonsense Reasoning. arXiv preprint, abs/1806.02847, 2018.
- **Cited in:** 11_appendix-c-pretraining-data.md as the Stories corpus used in pretraining data (Table 13).

## Tu et al., 2019
- **Full citation:** Ming Tu, Kevin Huang, Guangtao Wang, Jing Huang, Xiaodong He, and Bowen Zhou. Select, Answer and Explain: Interpretable Multi-hop Reading Comprehension over Multiple Documents. 2019.
- **Cited in:** 06_tasks.md as an example of complex task-specific architecture for HotpotQA; baseline SAE in Table 9.

## Tu et al., 2020
- **Full citation:** Ming Tu et al. 2020.
- **Cited in:** 06_tasks.md as an example of complex task-specific architecture for HotpotQA.

## van den Oord et al., 2016
- **Full citation:** Aaron van den Oord, Sander Dieleman, Heiga Zen, Karen Simonyan, Oriol Vinyals, Alex Graves, Nal Kalchbrenner, Andrew Senior, and Koray Kavukcuoglu. WaveNet: A Generative Model for Raw Audio. arXiv:1609.03499, 2016.
- **Cited in:** 03_longformer.md as the analogy for dilated sliding window (dilated CNNs).

## Vaswani et al., 2017
- **Full citation:** Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and Illia Polosukhin. Attention Is All You Need. NeurIPS, 2017.
- **Cited in:** 01_introduction.md as the original Transformer work; 03_longformer.md for the attention score formula (Eq. 1); 07_longformer-encoder-decoder.md as the original encoder-decoder Transformer architecture.

## Welbl et al., 2018
- **Full citation:** Johannes Welbl, Pontus Stenetorp, and Sebastian Riedel. Constructing Datasets for Multi-hop Reading Comprehension Across Documents. TACL, 2018.
- **Cited in:** 06_tasks.md as the WikiHop dataset.

## Wu et al., 2019
- **Full citation:** Felix Wu, Angela Fan, Alexei Baevski, Yann N. Dauphin, and Michael Auli. Pay Less Attention with Lightweight and Dynamic Convolutions. ICLR, 2019.
- **Cited in:** 03_longformer.md as analogy for how stacked windowed attention builds representations similar to CNNs.

## Xie et al., 2019
- **Full citation:** Qizhe Xie, Zihang Dai, Eduard Hovy, Minh-Thang Luong, and Quoc V. Le. Unsupervised Data Augmentation for Consistency Training. arXiv, 2019.
- **Cited in:** 02_related-work.md as an example of the truncation approach for classification.

## Yang et al., 2018
- **Full citation:** Zhilin Yang, Peng Qi, Saizheng Zhang, Yoshua Bengio, William W. Cohen, Ruslan Salakhutdinov, and Christopher D. Manning. HotpotQA: A Dataset for Diverse, Explainable Multi-hop Question Answering. EMNLP, 2018.
- **Cited in:** 06_tasks.md as the HotpotQA dataset (distractor setting).

## Ye et al., 2019
- **Full citation:** Zihao Ye, Qipeng Guo, Quan Gan, Xipeng Qiu, and Zheng Zhang. BP-Transformer: Modelling Long-Range Context via Binary Partitioning. arXiv:1911.04070, 2019.
- **Cited in:** 02_related-work.md as a model evaluated on MT but not pretrain-finetune; 04_autoregressive-language-modeling.md as baseline in Table 2.

## Xiong et al., 2020
- **Full citation:** Ruibin Xiong, Yunchang Yang, Di He, Kai Zheng, Shuxin Zheng, Chen Xing, Huishuai Zhang, Yanyan Lan, Li-Wei Wang, and Tie-Yan Liu. On Layer Normalization in the Transformer Architecture. arXiv preprint, abs/2002.04745, 2020.
- **Cited in:** 10_appendix-b-character-lm-hyperparameters.md as the pre-layernorm variant used in character LM experiments (Table 12).

## Zaheer et al., 2020
- **Full citation:** Manzil Zaheer, Guru Guruganesh, Avinava Dubey, Joshua Ainslie, Chris Alberti, Santiago Ontanon, Philip Pham, Anirudh Ravula, Qifan Wang, Li Yang, and Amr Ahmed. Big Bird: Transformers for Longer Sequences. NeurIPS, 2020.
- **Cited in:** 02_related-work.md as a contemporaneous work (BigBird) extending ETC, showing sparse Transformers are universal approximators; 06_tasks.md (footnote 9) as later improving leaderboard results; 07_longformer-encoder-decoder.md as comparison on arXiv summarization (Table 11).

## Zellers et al., 2019
- **Full citation:** Rowan Zellers, Ari Holtzman, Hannah Rashkin, Yonatan Bisk, Ali Farhadi, Franziska Roesner, and Yejin Choi. Defending Against Neural Fake News. NeurIPS, 2019.
- **Cited in:** 11_appendix-c-pretraining-data.md as the Realnews dataset used in pretraining data (Table 13).

## Zhang et al., 2020
- **Full citation:** Jingqing Zhang, Yao Zhao, Mohammad Saleh, and Peter J. Liu. PEGASUS: Pre-training with Extracted Gap-sentences for Abstractive Summarization. ICML, 2020.
- **Cited in:** 07_longformer-encoder-decoder.md as a model specifically designed and pre-trained for summarization, from which BigBird continues pre-training.

## Zhu et al., 2015
- **Full citation:** Yukun Zhu, Ryan Kiros, Richard S. Zemel, Ruslan Salakhutdinov, Raquel Urtasun, Antonio Torralba, and Sanja Fidler. Aligning Books and Movies: Towards Story-like Visual Explanations by Watching Movies and Reading Books. ICCV, 2015, pages 19-27.
- **Cited in:** 11_appendix-c-pretraining-data.md as the Books corpus used in pretraining data (Table 13).
