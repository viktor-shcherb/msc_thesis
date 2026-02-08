# References

Only references cited in the section notes are included below.

## [1]
Jimmy Lei Ba, Jamie Ryan Kiros, and Geoffrey E Hinton. Layer normalization. *arXiv preprint arXiv:1607.06450*, 2016.
- Cited in 03_outlier-analysis.md as LayerNorm, part of the outlier hypothesis (marker 2).

## [2]
Ron Banner, Yury Nahshan, Elad Hoffer, and Daniel Soudry. Post-training 4-bit quantization of convolution networks for rapid-deployment. *arXiv preprint arXiv:1810.05723*, 2018.
- Cited in 02_background-and-related-work.md as a PTQ method. Cited in 09_appendix-b-detailed-results.md as recommending MSE range estimator for low-bit quantization.

## [3]
Yash Bhalgat, Jinwon Lee, Markus Nagel, Tijmen Blankevoort, and Nojun Kwak. Lsq+: Improving low-bit quantization through learnable offsets and better initialization. In *Proceedings of the IEEE/CVF CVPR Workshops*, 2020.
- Cited in 02_background-and-related-work.md as a QAT method.

## [4]
Yelysei Bondarenko, Markus Nagel, and Tijmen Blankevoort. Understanding and overcoming the challenges of efficient transformer quantization. In *Proceedings of the 2021 EMNLP*, pages 7947-7969, 2021.
- Cited in 01_introduction.md as prior work finding existence of outliers. Cited in 02_background-and-related-work.md as showing outliers in transformer activations and as a prior fix approach. Cited in 03_outlier-analysis.md (footnote 1) for defining outliers as values exceeding 6 standard deviations. Cited in 05_experiments.md as showing outlier metrics correlate with quantizability.

## [5]
Yaohui Cai, Zhewei Yao, Zhen Dong, Amir Gholami, Michael W Mahoney, and Kurt Keutzer. Zeroq: A novel zero shot quantization framework. In *Proceedings of the IEEE/CVF CVPR*, pages 13169-13178, 2020.
- Cited in 02_background-and-related-work.md as a PTQ method.

## [6]
Brian Chmiel, Ron Banner, Gil Shomron, Yury Nahshan, Alex Bronstein, Uri Weiser, et al. Robust quantization: One model to rule them all. *Advances in Neural Information Processing Systems*, 33:5308-5317, 2020.
- Cited in 05_experiments.md as showing outlier metrics correlate with quantizability.

## [7]
Yoni Choukroun, Eli Kravchik, Fan Yang, and Pavel Kisilev. Low-bit quantization of neural networks for efficient inference. In *ICCV Workshops*, pages 3009-3018, 2019.
- Cited in 02_background-and-related-work.md as a PTQ method. Cited in 09_appendix-b-detailed-results.md as recommending MSE range estimator for low-bit quantization.

## [8]
Kevin Clark, Urvashi Khandelwal, Omer Levy, and Christopher D. Manning. What does BERT look at? an analysis of BERT's attention. In *Proceedings of the 2019 ACL Workshop BlackboxNLP*, pages 276-286, 2019.
- Cited in 03_outlier-analysis.md as prior work arguing that attending to delimiter tokens acts as a "no-op".

## [9]
Kevin Clark, Minh-Thang Luong, Quoc V Le, and Christopher D Manning. Electra: Pre-training text encoders as discriminators rather than generators. *arXiv preprint arXiv:2003.10555*, 2020.
- Cited in 02_background-and-related-work.md as a model exhibiting transformer outliers.

## [10]
Ekin D Cubuk, Barret Zoph, Jonathon Shlens, and Quoc V Le. Randaugment: Practical automated data augmentation with a reduced search space. In *Proceedings of the IEEE/CVF conference on computer vision and pattern recognition workshops*, pages 702-703, 2020.
- Cited in 10_appendix-c-experimental-details.md as a data augmentation method used for ViT training.

## [11]
Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li, and Li Fei-Fei. Imagenet: A large-scale hierarchical image database. In *2009 IEEE CVPR*, pages 248-255, 2009.
- Cited in 05_experiments.md as the ImageNet-1K training data for ViT.

## [12]
Tim Dettmers and Luke Zettlemoyer. The case for 4-bit precision: k-bit inference scaling laws. *arXiv preprint arXiv:2212.09720*, 2022.
- Cited in 01_introduction.md as showing 4-bit weights might be optimal. Cited in 02_background-and-related-work.md as a prior fix approach.

## [13]
Tim Dettmers, Mike Lewis, Younes Belkada, and Luke Zettlemoyer. Gpt3. int8 (): 8-bit matrix multiplication for transformers at scale. In *Advances in Neural Information Processing Systems*, 2022.
- Cited in 01_introduction.md as suggesting post-training fixes for outliers. Cited in 02_background-and-related-work.md as showing outliers in transformers and as requiring specific hardware for input-channel quantization.

## [14]
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. BERT: Pre-training of deep bidirectional transformers for language understanding. In *Proceedings of the 2019 NAACL*, pages 4171-4186, 2019.
- Cited in 02_background-and-related-work.md as a model exhibiting outliers. Cited in 05_experiments.md as the training procedure followed for BERT pre-training. Cited in 10_appendix-c-experimental-details.md as the fine-tuning and pre-training procedure followed for BERT.

## [15]
Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, et al. An image is worth 16x16 words: Transformers for image recognition at scale. *arXiv preprint arXiv:2010.11929*, 2020.
- Cited in 03_outlier-analysis.md as the Vision transformer architecture. Cited in 05_experiments.md as the ViT model used.

## [16]
Steven K. Esser, Jeffrey L. McKinstry, Deepika Bablani, Rathinakumar Appuswamy, and Dharmendra S. Modha. Learned step size quantization. In *ICLR*, 2020.
- Cited in 02_background-and-related-work.md as a QAT method.

## [17]
Angela Fan, Pierre Stock, Benjamin Graham, Edouard Grave, Remi Gribonval, Herve Jegou, and Armand Joulin. Training with quantization noise for extreme model compression. *arXiv preprint arXiv:2004.07320*, 2020.
- Cited in 02_background-and-related-work.md as a prior fix approach for transformer quantization.

## [18]
Elias Frantar, Saleh Ashkboos, Torsten Hoefler, and Dan Alistarh. Gptq: Accurate post-training quantization for generative pre-trained transformers. *arXiv preprint arXiv:2210.17323*, 2022.
- Cited in 09_appendix-b-detailed-results.md as a more advanced quantization method that can be combined with the proposed methods.

## [19]
Amir Gholami, Sehoon Kim, Zhen Dong, Zhewei Yao, Michael W Mahoney, and Kurt Keutzer. A survey of quantization methods for efficient neural network inference. *arXiv preprint arXiv:2103.13630*, 2021.
- Cited in 02_background-and-related-work.md as a general reference on neural network quantization.

## [20]
Sylvain Gugger, Lysandre Debu, Thomas Wolf, Philipp Schmid, Zachary Mueller, and Sourab Mangrulkar. Accelerate: Training and inference at scale made simple, efficient and adaptable. https://github.com/huggingface/accelerate, 2022.
- Cited in 05_experiments.md as part of HuggingFace libraries used for implementation. Cited in 10_appendix-c-experimental-details.md as FP16 mixed-precision library used for BERT and OPT pre-training.

## [21]
Suyog Gupta, Ankur Agrawal, Kailash Gopalakrishnan, and Pritish Narayanan. Deep learning with limited numerical precision. In *ICML*, pages 1737-1746. PMLR, 2015.
- Cited in 02_background-and-related-work.md as a QAT method.

## [22]
Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Delving deep into rectifiers: Surpassing human-level performance on imagenet classification. In *Proceedings of the IEEE international conference on computer vision*, pages 1026-1034, 2015.
- Cited in 05_experiments.md as the weight initialization method used for gating module (He initialization).

## [23]
M. Horowitz. 1.1 computing's energy problem (and what we can do about it). In *2014 IEEE ISSCC*, pages 10-14, 2014.
- Cited in 02_background-and-related-work.md as motivation for fixed-point arithmetic being more efficient.

## [24]
Itay Hubara, Matthieu Courbariaux, Daniel Soudry, Ran El-Yaniv, and Yoshua Bengio. Quantized neural networks: Training neural networks with low precision weights and activations. *JMLR*, 18(1):6869-6898, 2017.
- Cited in 02_background-and-related-work.md as a reference for uniform affine quantization.

## [25]
Itay Hubara, Yury Nahshan, Yair Hanani, Ron Banner, and Daniel Soudry. Improving post training neural quantization: Layer-wise calibration and integer programming. *arXiv preprint arXiv:2006.10518*, 2020.
- Cited in 02_background-and-related-work.md as a PTQ method.

## [26]
Benoit Jacob, Skirmantas Kligys, Bo Chen, Menglong Zhu, Matthew Tang, Andrew Howard, Hartwig Adam, and Dmitry Kalenichenko. Quantization and training of neural networks for efficient integer-arithmetic-only inference. In *Proceedings of the IEEE CVPR*, pages 2704-2713, 2018.
- Cited in 02_background-and-related-work.md as the source for the quantization function formulation (Eq. 1) and as a QAT method.

## [27]
Minsoo Kim, Sihwa Lee, Sukjin Hong, Du-Seong Chang, and Jungwook Choi. Understanding and improving knowledge distillation for quantization-aware training of large transformer encoders. *arXiv preprint arXiv:2211.11014*, 2022.
- Cited in 02_background-and-related-work.md as a prior fix approach.

## [28]
Sehoon Kim, Amir Gholami, Zhewei Yao, Michael W Mahoney, and Kurt Keutzer. I-bert: Integer-only bert quantization. *arXiv preprint arXiv:2101.01321*, 2021.
- Cited in 02_background-and-related-work.md as a prior fix approach.

## [29]
Diederik P Kingma and Jimmy Ba. Adam: A method for stochastic optimization. *arXiv preprint arXiv:1412.6980*, 2014.
- Cited in 10_appendix-c-experimental-details.md as the optimizer used for BERT fine-tuning.

## [30]
Olga Kovaleva, Alexey Romanov, Anna Rogers, and Anna Rumshisky. Revealing the dark secrets of BERT. In *Proceedings of the 2019 EMNLP-IJCNLP*, pages 4365-4374, 2019.
- Cited in 03_outlier-analysis.md as prior work arguing that attending to delimiter tokens acts as a "no-op".

## [31]
Olga Kovaleva, Saurabh Kulshreshtha, Anna Rogers, and Anna Rumshisky. Bert busters: Outlier dimensions that disrupt transformers. In *Findings of ACL: ACL-IJCNLP 2021*, pages 3392-3405, 2021.
- Cited in 02_background-and-related-work.md as showing outliers play a crucial role in model predictions.

## [32]
Raghuraman Krishnamoorthi. Quantizing deep convolutional networks for efficient inference: A whitepaper. *arXiv preprint arXiv:1806.08342*, 2018.
- Cited in 02_background-and-related-work.md as a reference for uniform affine quantization and as a QAT method. Cited in 10_appendix-c-experimental-details.md as the running min-max estimator used for activation quantization.

## [33]
Mike Lewis, Yinhan Liu, Naman Goyal, Marjan Ghazvininejad, Abdelrahman Mohamed, Omer Levy, Veselin Stoyanov, and Luke Zettlemoyer. BART: Denoising sequence-to-sequence pre-training for natural language generation, translation, and comprehension. In *Proceedings of the 58th ACL*, pages 7871-7880, 2020.
- Cited in 02_background-and-related-work.md as a model exhibiting transformer outliers.

## [34]
Quentin Lhoest, Albert Villanova del Moral, Yacine Jernite, Abhishek Thakur, et al. Datasets: A community library for natural language processing. In *Proceedings of the 2021 EMNLP: System Demonstrations*, pages 175-184, 2021.
- Cited in 05_experiments.md as part of HuggingFace libraries used for implementation.

## [35]
Yuhang Li, Ruihao Gong, Xu Tan, Yang Yang, Peng Hu, Qi Zhang, Fengwei Yu, Wei Wang, and Shi Gu. Brecq: Pushing the limit of post-training quantization by block reconstruction. *arXiv preprint arXiv:2102.05426*, 2021.
- Cited in 02_background-and-related-work.md as a PTQ method. Cited in 09_appendix-b-detailed-results.md as a more advanced quantization method that can be combined with the proposed methods.

## [36]
Ji Lin, Jiaming Tang, Haotian Tang, Shang Yang, Xingyu Dang, and Song Han. Awq: Activation-aware weight quantization for llm compression and acceleration. *arXiv preprint arXiv:2306.00978*, 2023.
- Cited in 09_appendix-b-detailed-results.md as a more advanced quantization method that can be combined with the proposed methods.

## [37]
Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke Zettlemoyer, and Veselin Stoyanov. Roberta: A robustly optimized bert pretraining approach. *arXiv preprint arXiv:1907.11692*, 2019.
- Cited in 02_background-and-related-work.md as a model exhibiting transformer outliers.

## [38]
Ze Liu, Yutong Lin, Yue Cao, Han Hu, Yixuan Wei, Zheng Zhang, Stephen Lin, and Baining Guo. Swin transformer: Hierarchical vision transformer using shifted windows. In *Proceedings of the IEEE/CVF international conference on computer vision*, pages 10012-10022, 2021.
- Cited in 03_outlier-analysis.md as a transformer variant where the outlier hypothesis applies (pre-LayerNorm variant).

## [39]
Ilya Loshchilov and Frank Hutter. Decoupled weight decay regularization. *arXiv preprint arXiv:1711.05101*, 2017.
- Cited in 10_appendix-c-experimental-details.md as the AdamW optimizer used for BERT pre-training.

## [40]
Christos Louizos, Max Welling, and Diederik P Kingma. Learning sparse neural networks through l_0 regularization. *arXiv preprint arXiv:1712.01312*, 2017.
- Cited in 04_method.md as prior work using a similar stretch formulation for sigmoid function.

## [41]
Eldad Meller, Alexander Finkelstein, Uri Almog, and Mark Grobman. Same, same but different: Recovering neural network quantization error through weight factorization. In *ICML*, pages 4486-4495. PMLR, 2019.
- Cited in 02_background-and-related-work.md as a PTQ method.

## [42]
Stephen Merity, Caiming Xiong, James Bradbury, and Richard Socher. Pointer sentinel mixture models. *arXiv preprint arXiv:1609.07843*, 2016.
- Cited in 05_experiments.md as the WikiText-103 dataset used for BERT-6L experiments.

## [43]
Markus Nagel, Mart van Baalen, Tijmen Blankevoort, and Max Welling. Data-free quantization through weight equalization and bias correction. In *Proceedings of the IEEE/CVF ICCV*, pages 1325-1334, 2019.
- Cited in 02_background-and-related-work.md as a PTQ method.

## [44]
Markus Nagel, Rana Ali Amjad, Mart Van Baalen, Christos Louizos, and Tijmen Blankevoort. Up or down? Adaptive rounding for post-training quantization. In *ICML*, 2020.
- Cited in 02_background-and-related-work.md as a PTQ method.

## [45]
Markus Nagel, Rana Ali Amjad, Mart Van Baalen, Christos Louizos, and Tijmen Blankevoort. Up or down? Adaptive rounding for post-training quantization. In *ICML*, pages 7197-7206. PMLR, 2020.
- Cited in 04_method.md as prior work using a similar stretch formulation for sigmoid function. Cited in 09_appendix-b-detailed-results.md as a more advanced quantization method that can be combined with the proposed methods.

## [46]
Markus Nagel, Marios Fournarakis, Rana Ali Amjad, Yelysei Bondarenko, Mart van Baalen, and Blankevoort Tijmen. A white paper on neural network quantization. *arXiv preprint arXiv:2106.08295*, 2021.
- Cited in 02_background-and-related-work.md as a general reference on neural network quantization.

## [47]
Vinod Nair and Geoffrey E. Hinton. Rectified Linear Units Improve Restricted Boltzmann Machines. In *Proceedings of the 27th International Conference on Machine Learning*, pages 807-814. Omnipress, 2010.
- Cited in 09_appendix-b-detailed-results.md as the ReLU non-linearity used in the MLP gating configuration.

## [48]
Adam Paszke, Sam Gross, Francisco Massa, Adam Lerer, James Bradbury, Gregory Chanan, et al. Pytorch: An imperative style, high-performance deep learning library. In *NeurIPS*, 2019.
- Cited in 05_experiments.md as the deep learning framework used for implementation.

## [49]
Giovanni Puccetti, Alessio Miaschi, and Felice Dell'Orletta. How do BERT embeddings organize linguistic knowledge? In *Proceedings of DeeLIO*, pages 48-57, 2021.
- Cited in 02_background-and-related-work.md as showing that clipping outliers or zeroing corresponding parameters degrades performance.

## [50]
Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, and Ilya Sutskever. Language models are unsupervised multitask learners. 2019.
- Cited in 02_background-and-related-work.md as a model exhibiting transformer outliers (GPT-2).

## [51]
Bita Rouhani, Daniel Lo, Ritchie Zhao, Ming Liu, Jeremy Fowers, Kalin Ovtcharov, et al. Pushing the limits of narrow precision inferencing at cloud scale with microsoft floating point. In *NeurIPS 2020*, 2020.
- Cited in 02_background-and-related-work.md as a prior fix approach.

## [52]
Olga Russakovsky, Jia Deng, Hao Su, Jonathan Krause, Sanjeev Satheesh, Sean Ma, Zhiheng Huang, Andrej Karpathy, Aditya Khosla, Michael Bernstein, Alexander C. Berg, and Li Fei-Fei. ImageNet Large Scale Visual Recognition Challenge. *IJCV*, 2015.
- Cited in 03_outlier-analysis.md and 05_experiments.md as the ImageNet dataset.

## [53]
Victor Sanh, Lysandre Debut, Julien Chaumond, and Thomas Wolf. Distilbert, a distilled version of bert: smaller, faster, cheaper and lighter. *arXiv preprint arXiv:1910.01108*, 2019.
- Cited in 02_background-and-related-work.md as a model exhibiting transformer outliers.

## [54]
Sheng Shen, Zhen Dong, Jiayu Ye, Linjian Ma, Zhewei Yao, Amir Gholami, Michael W Mahoney, and Kurt Keutzer. Q-bert: Hessian based ultra low precision quantization of bert. In *Proceedings of the AAAI Conference on AI*, volume 34, pages 8815-8821, 2020.
- Cited in 02_background-and-related-work.md as a prior fix approach.

## [55]
Zhiqing Sun, Hongkun Yu, Xiaodan Song, Renjie Liu, Yiming Yang, and Denny Zhou. MobileBERT: a compact task-agnostic BERT for resource-limited devices. In *Proceedings of the 58th ACL*, pages 2158-2170, 2020.
- Cited in 02_background-and-related-work.md as a model exhibiting transformer outliers.

## [56]
Christian Szegedy, Wei Liu, Yangqing Jia, Pierre Sermanet, Scott Reed, Dragomir Anguelov, Dumitru Erhan, Vincent Vanhoucke, and Andrew Rabinovich. Going deeper with convolutions. In *Proceedings of the IEEE conference on computer vision and pattern recognition*, pages 1-9, 2015.
- Cited in 10_appendix-c-experimental-details.md as random image cropping used for ViT data augmentation.

## [57]
Hugo Touvron, Matthieu Cord, Alexandre Sablayrolles, Gabriel Synnaeve, and Herve Jegou. Going deeper with image transformers. In *Proceedings of the IEEE/CVF ICCV*, pages 32-42, 2021.
- Cited in 03_outlier-analysis.md as a transformer variant where the outlier hypothesis applies (pre-LayerNorm variant).

## [58]
Hugo Touvron, Matthieu Cord, and Herve Jegou. Deit iii: Revenge of the vit. In *ECCV 2022*, pages 516-533, 2022.
- Cited in 03_outlier-analysis.md as a transformer variant where the outlier hypothesis applies (pre-LayerNorm variant).

## [59]
Mart van Baalen, Andrey Kuzmin, Suparna S Nair, Yuwei Ren, Eric Mahurin, Chirag Patel, Sundar Subramanian, Sanghyuk Lee, Markus Nagel, Joseph Soriaga, and Tijmen Blankevoort. Fp8 versus int8 for efficient deep learning inference. 2023.
- Cited in 02_background-and-related-work.md as motivation for fixed-point arithmetic being more efficient.

## [60]
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Lukasz Kaiser, and Illia Polosukhin. Attention is all you need. In *Proceedings of the 31st NeurIPS*, pages 6000-6010, 2017.
- Cited in 04_method.md as the original self-attention definition.

## [61]
Alex Wang, Amanpreet Singh, Julian Michael, Felix Hill, Omer Levy, and Samuel Bowman. GLUE: A multi-task benchmark and analysis platform for natural language understanding. In *Proceedings of the 2018 EMNLP Workshop BlackboxNLP*, pages 353-355, 2018.
- Cited in 03_outlier-analysis.md as the GLUE benchmark from which MNLI is drawn.

## [62]
Xiuying Wei, Yunchen Zhang, Xiangguo Zhang, Ruihao Gong, Shanghang Zhang, Qi Zhang, Fengwei Yu, and Xianglong Liu. Outlier suppression: Pushing the limit of low-bit transformer language models. *arXiv preprint arXiv:2209.13325*, 2022.
- Cited in 02_background-and-related-work.md as a prior fix approach.

## [63]
Xiuying Wei, Yunchen Zhang, Yuhang Li, Xiangguo Zhang, Ruihao Gong, Jinyang Guo, and Xianglong Liu. Outlier suppression+: Accurate quantization of large language models by equivalent and optimal shifting and scaling. *arXiv preprint arXiv:2304.09145*, 2023.
- Cited in 02_background-and-related-work.md as a prior fix approach. Cited in 09_appendix-b-detailed-results.md as a more advanced quantization method that can be combined with the proposed methods.

## [64]
Ross Wightman. Pytorch image models. https://github.com/rwightman/pytorch-image-models, 2019.
- Cited in 05_experiments.md as the library used for ViT training and validation pipelines. Cited in 10_appendix-c-experimental-details.md as the model definition and training pipeline source for ViT-S/16.

## [65]
Thomas Wolf, Lysandre Debut, Victor Sanh, Julien Chaumond, Clement Delangue, Anthony Moi, Pierric Cistac, Tim Rault, Remi Louf, Morgan Funtowicz, et al. Transformers: State-of-the-art natural language processing. In *Proceedings of the 2020 EMNLP: system demonstrations*, pages 38-45, 2020.
- Cited in 03_outlier-analysis.md as the HuggingFace checkpoint source. Cited in 05_experiments.md as part of HuggingFace libraries. Cited in 10_appendix-c-experimental-details.md as the fine-tuning practices source for BERT and OPT pre-training.

## [66]
Xiaoxia Wu, Cheng Li, Reza Yazdani Aminabadi, Zhewei Yao, and Yuxiong He. Understanding int4 quantization for transformer models: Latency speedup, composability, and failure cases. 2023.
- Cited in 01_introduction.md as showing 4-bit weight quantization is possible.

## [67]
Guangxuan Xiao, Ji Lin, Mickael Seznec, Hao Wu, Julien Demouth, and Song Han. Smoothquant: Accurate and efficient post-training quantization for large language models. In *CVPR*, 2022.
- Cited in 01_introduction.md as a post-training fix requiring parts of activations in higher bit-widths. Cited in 09_appendix-b-detailed-results.md as a more advanced quantization method that can be combined with the proposed methods.

## [68]
Zhilin Yang, Zihang Dai, Yiming Yang, Jaime Carbonell, Russ R Salakhutdinov, and Quoc V Le. Xlnet: Generalized autoregressive pretraining for language understanding. In *NeurIPS*, volume 32, 2019.
- Cited in 02_background-and-related-work.md as a model exhibiting transformer outliers.

## [69]
Zhewei Yao, Reza Yazdani Aminabadi, Minjia Zhang, Xiaoxia Wu, Conglong Li, and Yuxiong He. Zeroquant: Efficient and affordable post-training quantization for large-scale transformers. In *NeurIPS*, volume 35, pages 27168-27183, 2022.
- Cited in 01_introduction.md as showing 4-bit weight quantization is possible. Cited in 02_background-and-related-work.md as a prior fix approach.

## [70]
Sangdoo Yun, Dongyoon Han, Seong Joon Oh, Sanghyuk Chun, Junsuk Choe, and Youngjoon Yoo. Cutmix: Regularization strategy to train strong classifiers with localizable features. In *Proceedings of the IEEE/CVF international conference on computer vision*, pages 6023-6032, 2019.
- Cited in 10_appendix-c-experimental-details.md as a data augmentation method used for ViT training.

## [71]
Ofir Zafrir, Guy Boudoukh, Peter Izsak, and Moshe Wasserblat. Q8bert: Quantized 8bit bert. *arXiv preprint arXiv:1910.06188*, 2019.
- Cited in 02_background-and-related-work.md as a prior fix approach.

## [72]
Chiyuan Zhang, Samy Bengio, Moritz Hardt, Benjamin Recht, and Oriol Vinyals. Understanding deep learning requires rethinking generalization. 2017.
- Cited in 06_discussion.md in the context of why overparametrized networks generalize.

## [73]
Hongyi Zhang, Moustapha Cisse, Yann N Dauphin, and David Lopez-Paz. mixup: Beyond empirical risk minimization. *arXiv preprint arXiv:1710.09412*, 2017.
- Cited in 10_appendix-c-experimental-details.md as a data augmentation method used for ViT training.

## [74]
Susan Zhang, Stephen Roller, Naman Goyal, Mikel Artetxe, Moya Chen, Shuohui Chen, Christopher Dewan, Mona Diab, Xian Li, Xi Victoria Lin, et al. Opt: Open pre-trained transformer language models. *arXiv preprint arXiv:2205.01068*, 2022.
- Cited in 02_background-and-related-work.md as a model exhibiting outliers. Cited in 05_experiments.md as the OPT model used in experiments. Cited in 10_appendix-c-experimental-details.md as the source of OPT pre-training practices.

## [75]
Ritchie Zhao, Yuwei Hu, Jordan Dotzel, Chris De Sa, and Zhiru Zhang. Improving neural network quantization without retraining using outlier channel splitting. In *ICML*, pages 7543-7552. PMLR, 2019.
- Cited in 02_background-and-related-work.md as a PTQ method.

## [76]
Shuchang Zhou, Yuxin Wu, Zekun Ni, Xinyu Zhou, He Wen, and Yuheng Zou. Dorefa-net: Training low bitwidth convolutional neural networks with low bitwidth gradients. *arXiv preprint arXiv:1606.06160*, 2016.
- Cited in 02_background-and-related-work.md as a reference for uniform affine quantization.

## [77]
Yukun Zhu, Ryan Kiros, Rich Zemel, Ruslan Salakhutdinov, Raquel Urtasun, Antonio Torralba, and Sanja Fidler. Aligning books and movies: Towards story-like visual explanations by watching movies and reading books. In *The IEEE ICCV*, December 2015.
- Cited in 05_experiments.md as the BookCorpus dataset used for BERT pre-training.
