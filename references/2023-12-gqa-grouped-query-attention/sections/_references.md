# References

Only references cited in the section notes are included below.

## Bradbury et al., 2018
James Bradbury, Roy Frostig, Peter Hawkins, Matthew James Johnson, Chris Leary, Dougal Maclaurin, George Necula, Adam Paszke, Jake VanderPlas, Skye Wanderman-Milne, and Qiao Zhang. 2018. JAX: composable transformations of Python+NumPy programs.
- Cited in 03_experiments.md as the framework used for implementation.

## Chen et al., 2023
Charlie Chen, Sebastian Borgeaud, Geoffrey Irving, Jean-Baptiste Lespiau, Laurent Sifre, and John Jumper. 2023. Accelerating large language model decoding with speculative sampling. *CoRR*, abs/2302.01318.
- Cited in 04_related-work.md as a speculative sampling method that ameliorates the memory bandwidth bottleneck.

## Chowdhery et al., 2022
Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung, Charles Sutton, Sebastian Gehrmann, Parker Schuh, Kensen Shi, Sasha Tsvyashchenko, Joshua Maynez, Abhishek Rao, Parker Barnes, Yi Tay, Noam Shazeer, Vinodkumar Prabhakaran, Emily Reif, Nan Du, Ben Hutchinson, Reiner Pope, James Bradbury, Jacob Austin, Michael Isard, Guy Gur-Ari, Pengcheng Yin, Toju Duke, Anselm Levskaya, Sanjay Ghemawat, Sunipa Dev, Henryk Michalewski, Xavier Garcia, Vedant Misra, Kevin Robinson, Liam Fedus, Denny Zhou, Daphne Ippolito, David Luan, Hyeontaek Lim, Barret Zoph, Alexander Spiridonov, Ryan Sepassi, David Dohan, Shivani Agrawal, Mark Omernick, Andrew M. Dai, Thanumalayan Sankaranarayana Pillai, Marie Pellat, Aitor Lewkowycz, Erica Moreira, Rewon Child, Oleksandr Polozov, Katherine Lee, Zongwei Zhou, Xuezhi Wang, Brennan Saeta, Mark Diaz, Orhan Firat, Michele Catasta, Jason Wei, Kathy Meier-Hellstern, Douglas Eck, Jeff Dean, Slav Petrov, and Noah Fiedel. 2022. Palm: Scaling language modeling with pathways.
- Cited in 01_introduction.md as an example of a language model that already uses multi-query attention.

## Cohan et al., 2018
Arman Cohan, Franck Dernoncourt, Doo Soon Kim, Trung Bui, Seokhwan Kim, Walter Chang, and Nazli Goharian. 2018. A discourse-aware attention model for abstractive summarization of long documents. In *Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 2 (Short Papers)*, pages 615-621, New Orleans, Louisiana. Association for Computational Linguistics.
- Cited in 03_experiments.md as the source of the arXiv and PubMed summarization datasets.

## Dao et al., 2022
Tri Dao, Daniel Y. Fu, Stefano Ermon, Atri Rudra, and Christopher Re. 2022. Flashattention: Fast and memory-efficient exact attention with io-awareness. *CoRR*, abs/2205.14135.
- Cited in 04_related-work.md as a method that structures attention computation to avoid materializing quadratic attention scores.

## de Jong et al., 2022
Michiel de Jong, Yury Zemlyanskiy, Joshua Ainslie, Nicholas FitzGerald, Sumit Sanghai, Fei Sha, and William Cohen. 2022. FiDO: Fusion-in-decoder optimized for stronger performance and faster inference. *arXiv preprint arXiv:2212.08153*.
- Cited in 01_introduction.md and 04_related-work.md as follow-up work showing multi-query attention is helpful for long inputs, and as a layer-sparse cross-attention method.

## Dettmers et al., 2022
Tim Dettmers, Mike Lewis, Younes Belkada, and Luke Zettlemoyer. 2022. Llm.int8(): 8-bit matrix multiplication for transformers at scale. *CoRR*, abs/2208.07339.
- Cited in 04_related-work.md as a quantization method that reduces the size of weights and activations.

## Fabbri et al., 2019
Alexander R. Fabbri, Irene Li, Tianwei She, Suyi Li, and Dragomir R. Radev. 2019. Multi-news: A large-scale multi-document summarization dataset and abstractive hierarchical model. In *Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics, ACL 2019, Florence, Italy, July 28- August 2, 2019, Volume 1: Long Papers*, pages 1074-1084. Association for Computational Linguistics.
- Cited in 03_experiments.md as the source of the Multi-News summarization dataset.

## Frantar et al., 2022
Elias Frantar, Saleh Ashkboos, Torsten Hoefler, and Dan Alistarh. 2022. GPTQ: accurate post-training quantization for generative pre-trained transformers. *CoRR*, abs/2210.17323.
- Cited in 04_related-work.md as a quantization method.

## Google, 2020
Google. 2020. Profile your model with cloud tpu tools. https://cloud.google.com/tpu/docs/cloud-tpu-tools. Accessed: 2022-11-11.
- Cited in 03_experiments.md as the timing measurement tool (xprof).

## Gou et al., 2021
Jianping Gou, Baosheng Yu, Stephen J. Maybank, and Dacheng Tao. 2021. Knowledge distillation: A survey. *Int. J. Comput. Vis.*, 129(6):1789-1819.
- Cited in 04_related-work.md as a knowledge distillation survey.

## Heek et al., 2020
Jonathan Heek, Anselm Levskaya, Avital Oliver, Marvin Ritter, Bertrand Rondepierre, Andreas Steiner, and Marc van Zee. 2020. Flax: A neural network library and ecosystem for JAX.
- Cited in 03_experiments.md as the neural network library used for implementation.

## Hinton et al., 2015
Geoffrey E. Hinton, Oriol Vinyals, and Jeffrey Dean. 2015. Distilling the knowledge in a neural network. *CoRR*, abs/1503.02531.
- Cited in 04_related-work.md as a foundational model distillation method.

## Joshi et al., 2017
Mandar Joshi, Eunsol Choi, Daniel S. Weld, and Luke Zettlemoyer. 2017. Triviaqa: A large scale distantly supervised challenge dataset for reading comprehension. In *Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics*, Vancouver, Canada. Association for Computational Linguistics.
- Cited in 03_experiments.md as the source of the TriviaQA dataset.

## Komatsuzaki et al., 2022
Aran Komatsuzaki, Joan Puigcerver, James Lee-Thorp, Carlos Riquelme Ruiz, Basil Mustafa, Joshua Ainslie, Yi Tay, Mostafa Dehghani, and Neil Houlsby. 2022. Sparse upcycling: Training mixture-of-experts from dense checkpoints.
- Cited in 01_introduction.md as the inspiration for the uptraining procedure, and in 04_related-work.md as the method that uptrains standard T5 checkpoints into sparsely activated Mixture-of-Experts models.

## Leviathan et al., 2022
Yaniv Leviathan, Matan Kalman, and Yossi Matias. 2022. Fast inference from transformers via speculative decoding. *CoRR*, abs/2211.17192.
- Cited in 04_related-work.md as a speculative decoding method.

## Luo et al., 2022
Gen Luo, Yiyi Zhou, Xiaoshuai Sun, Yan Wang, Liujuan Cao, Yongjian Wu, Feiyue Huang, and Rongrong Ji. 2022. Towards lightweight transformer via groupwise transformation for vision-and-language tasks. *IEEE Trans. Image Process.*, 31:3386-3398.
- Cited in 04_related-work.md as work exploring grouping attention heads for computational efficiency.

## Nallapati et al., 2016
Ramesh Nallapati, Bowen Zhou, Cicero Nogueira dos Santos, Caglar Gulcehre, and Bing Xiang. 2016. Abstractive text summarization using sequence-to-sequence rnns and beyond. In *Proceedings of the 20th SIGNLL Conference on Computational Natural Language Learning, CoNLL 2016, Berlin, Germany, August 11-12, 2016*, pages 280-290. ACL.
- Cited in 03_experiments.md as the source of the CNN/Daily Mail summarization dataset.

## Ni et al., 2023
Jinjie Ni, Rui Mao, Zonglin Yang, Han Lei, and Erik Cambria. 2023. Finding the pillars of strength for multi-head attention. In *Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), ACL 2023, Toronto, Canada, July 9-14, 2023*, pages 14526-14540. Association for Computational Linguistics.
- Cited in 04_related-work.md as work exploring grouping attention heads for computational efficiency.

## Park et al., 2020
Sungrae Park, Geewook Kim, Junyeop Lee, Junbum Cha, Ji-Hoon Kim, and Hwalsuk Lee. 2020. Scale down transformer by grouping features for a lightweight character-level language model. In *Proceedings of the 28th International Conference on Computational Linguistics, COLING 2020, Barcelona, Spain (Online), December 8-13, 2020*, pages 6883-6893. International Committee on Computational Linguistics.
- Cited in 04_related-work.md as work exploring grouping attention heads for computational efficiency.

## Pope et al., 2022
Reiner Pope, Sholto Douglas, Aakanksha Chowdhery, Jacob Devlin, James Bradbury, Anselm Levskaya, Jonathan Heek, Kefan Xiao, Shivani Agrawal, and Jeff Dean. 2022. Efficiently scaling transformer inference. *arXiv preprint arXiv:2211.05102*.
- Cited in 01_introduction.md as work identifying memory bandwidth overhead in decoder inference, in 02_method.md regarding standard sharding replicating key/value heads, and in 04_related-work.md as follow-up work showing multi-query attention is helpful for long inputs.

## Rabe, 2023
Markus Rabe. 2023. Memory-efficient attention. https://github.com/google/flaxformer/blob/main/flaxformer/components/attention/memory_efficient_attention.py. Accessed: 2023-05-23.
- Cited in 04_related-work.md as an independent development of GQA with public implementation.

## Raffel et al., 2020
Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, and Peter J. Liu. 2020. Exploring the limits of transfer learning with a unified text-to-text transformer. *J. Mach. Learn. Res.*, 21:140:1-140:67.
- Cited in 01_introduction.md as T5, a publicly available model that does not use multi-query attention. Cited in 03_experiments.md as the base architecture (T5.1.1) and the pre-training setup/dataset used for uptraining.

## Shazeer, 2019
Noam Shazeer. 2019. Fast transformer decoding: One write-head is all you need. *arXiv preprint arXiv:1911.02150*.
- Cited in 01_introduction.md as the original proposer of multi-query attention, in 03_experiments.md regarding KV cache constraints for larger models, and in 04_related-work.md as the foundational work on multi-query attention.

## Touvron et al., 2023
Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothee Lacroix, Baptiste Roziere, Naman Goyal, Eric Hambro, Faisal Azhar, Aurelien Rodriguez, Armand Joulin, Edouard Grave, and Guillaume Lample. 2023. Llama: Open and efficient foundation language models.
- Cited in 01_introduction.md as a publicly available model (LLaMA) that does not use multi-query attention.

## Wang et al., 2019
Alex Wang, Amanpreet Singh, Julian Michael, Felix Hill, Omer Levy, and Samuel R. Bowman. 2019. GLUE: A multi-task benchmark and analysis platform for natural language understanding. In *7th International Conference on Learning Representations, ICLR 2019, New Orleans, LA, USA, May 6-9, 2019*. OpenReview.net.
- Cited in 03_experiments.md as a classification benchmark not evaluated in this paper because autoregressive inference is less applicable.

## Williams et al., 2009
Samuel Williams, Andrew Waterman, and David A. Patterson. 2009. Roofline: an insightful visual performance model for multicore architectures. *Commun. ACM*, 52(4):65-76.
- Cited in 04_related-work.md as the source for memory bandwidth overhead concept.

## Zhu et al., 2021
Chenguang Zhu, Yang Liu, Jie Mei, and Michael Zeng. 2021. Mediasum: A large-scale media interview dataset for dialogue summarization. In *Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, NAACL-HLT 2021, Online, June 6-11, 2021*, pages 5927-5934. Association for Computational Linguistics.
- Cited in 03_experiments.md as the source of the MediaSum dataset.
