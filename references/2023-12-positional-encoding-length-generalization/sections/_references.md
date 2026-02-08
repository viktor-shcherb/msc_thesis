# References

## Akyurek and Akyurek (2022)
Ekin Akyurek and Afra Feyza Akyurek. 2022. Notes on teaching gpt-3 adding numbers.
- Cited in 01_introduction.md as evidence that model performance is highly sensitive to scratchpad format.

## Akyurek et al. (2023)
Ekin Akyurek, Dale Schuurmans, Jacob Andreas, Tengyu Ma, and Denny Zhou. 2023. What learning algorithm is in-context learning? investigations with linear models. In *The Eleventh International Conference on Learning Representations*.
- Cited in 13_appendix-c.md (layer-norm operation can be bypassed in NoPE absolute encoding proof).

## Ba et al. (2016)
Jimmy Lei Ba, Jamie Ryan Kiros, and Geoffrey E. Hinton. 2016. Layer normalization. *ArXiv*, abs/1607.06450.
- Cited in 12_appendix-b.md (layer normalization in Transformer notation).

## Anil et al. (2022)
Cem Anil, Yuhuai Wu, Anders Johan Andreassen, Aitor Lewkowycz, Vedant Misra, Vinay Venkatesh Ramasesh, Ambrose Slone, Guy Gur-Ari, Ethan Dyer, and Behnam Neyshabur. 2022. Exploring length generalization in large language models. In *Advances in Neural Information Processing Systems*.
- Cited in 01_introduction.md, 03_model-evaluation.md (Parity task), 06_scratchpad.md (scratchpad results), 08_related-work.md (LaMDA length generalization failure), 14_appendix-d.md (Parity task description).

## Brown et al. (2020)
Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. 2020. Language models are few-shot learners. In *Advances in Neural Information Processing Systems 33*.
- Cited in 01_introduction.md (length generalization persists in larger Transformers) and 02_background.md (GPT3 uses learned APE).

## Bueno et al. (2022)
Mirelle Candida Bueno, Carlos Gemmell, Jeff Dalton, Roberto Lotufo, and Rodrigo Nogueira. 2022. Induced natural language rationales and interleaved markup tokens enable extrapolation in large language models. In *Proceedings of the 1st Workshop on Mathematical Natural Language Processing (MathNLP)*, pages 17-24.
- Cited in 01_introduction.md (scratchpad format sensitivity) and 06_scratchpad.md (scratchpad format design choice).

## Chi et al. (2023)
Ta-Chung Chi, Ting-Han Fan, Alexander Rudnicky, and Peter Ramadge. 2023. Dissecting transformer length extrapolation via the lens of receptive field analysis. In *Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 13522-13537.
- Cited in 07_discussion.md (ALiBi's length generalization can be replicated using window attention mask).

## Chowdhery et al. (2022)
Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung, Charles Sutton, Sebastian Gehrmann, et al. 2022. Palm: Scaling language modeling with pathways. *ArXiv*, abs/2204.02311.
- Cited in 02_background.md (PaLM uses Rotary), 07_discussion.md (shift towards Rotary in LLMs).

## Chung et al. (2022)
Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang, Mostafa Dehghani, Siddhartha Brahma, et al. 2022. Scaling instruction-finetuned language models. *ArXiv*, abs/2210.11416.
- Cited in 01_introduction.md (instruction-following datasets).

## Csordas et al. (2021)
Robert Csordas, Kazuki Irie, and Juergen Schmidhuber. 2021. The devil is in the detail: Simple tricks improve systematic generalization of transformers. In *Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing*, pages 619-634.
- Cited in 01_introduction.md (relative PEs more effective than APE) and 08_related-work.md (studying PE effect on length generalization).

## Dai et al. (2019)
Zihang Dai, Zhilin Yang, Yiming Yang, Jaime Carbonell, Quoc Le, and Ruslan Salakhutdinov. 2019. Transformer-XL: Attentive language models beyond a fixed-length context. In *Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics*, pages 2978-2988.
- Cited in 08_related-work.md (TransformerXL as a relative encoding model).

## Elhage et al. (2021)
Nelson Elhage, Neel Nanda, Catherine Olsson, Tom Henighan, Nicholas Joseph, Ben Mann, Amanda Askell, Yuntao Bai, Anna Chen, Tom Conerly, Nova DasSarma, et al. 2021. A mathematical framework for transformer circuits. *Transformer Circuits Thread*.
- Cited in 12_appendix-b.md (additive view of attention heads, mathematically equivalent to concatenate-and-multiply view).

## Deletang et al. (2023)
Gregoire Deletang, Anian Ruoss, Jordi Grau-Moya, Tim Genewein, Li Kevin Wenliang, Elliot Catt, Chris Cundy, Marcus Hutter, Shane Legg, Joel Veness, and Pedro A Ortega. 2023. Neural networks and the chomsky hierarchy. In *International Conference on Learning Representations*.
- Cited in 01_introduction.md (length generalization challenge) and 08_related-work.md (most relevant prior work on length generalization in neural sequence models).

## Devlin et al. (2019)
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2019. BERT: Pre-training of deep bidirectional transformers for language understanding. In *Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics*, pages 4171-4186.
- Cited in 08_related-work.md (popularized learned APE variant).

## Furrer et al. (2020)
Daniel Furrer, Marc van Zee, Nathan Scales, and Nathanael Scharli. 2020. Compositional generalization in semantic parsing: Pre-training vs. specialized architectures. *ArXiv*, abs/2007.08970.
- Cited in 01_introduction.md (length generalization persists in larger Transformers) and 08_related-work.md (length generalization in pretrained T5).

## Gibson (1998)
Edward Gibson. 1998. Linguistic complexity: locality of syntactic dependencies. *Cognition*, 68(1):1-76.
- Cited in 07_discussion.md (human cognitive constraints favor short-range dependencies in language).

## Gontier et al. (2020)
Nicolas Gontier, Koustuv Sinha, Siva Reddy, and Christopher Pal. 2020. Measuring systematic generalization in neural proof generation with transformers. In *Advances in Neural Information Processing Systems 33*.
- Cited in 08_related-work.md (generalization failure on CLUTRR).

## Graves et al. (2016)
Alex Graves, Greg Wayne, Malcolm Reynolds, Tim Harley, Ivo Danihelka, Agnieszka Grabska-Barwinska, Sergio Gomez Colmenarejo, Edward Grefenstette, Tiago Ramalho, John Agapio, et al. 2016. Hybrid computing using a neural network with dynamic external memory. *Nature*, 538(7626):471-476.
- Cited in 08_related-work.md (early work on length generalization in neural sequence models).

## Hendrycks and Gimpel (2020)
Dan Hendrycks and Kevin Gimpel. 2020. Gaussian error linear units (gelus). *ArXiv*, abs/1606.08415.
- Cited in 12_appendix-b.md (GeLU as non-linear activation function in feed-forward sub-layer).

## Haviv et al. (2022)
Adi Haviv, Ori Ram, Ofir Press, Peter Izsak, and Omer Levy. 2022. Transformer language models without positional encodings still learn positional information. In *Findings of the Association for Computational Linguistics: EMNLP 2022*, pages 1382-1390.
- Cited in 01_introduction.md (decoder-only Transformers without PE can perform well), 02_background.md (NoPE in language modelling), 07_discussion.md (similar I.I.D. performance across PEs), 08_related-work.md (NoPE performance in language modelling).

## Hupkes et al. (2020)
Dieuwke Hupkes, Verna Dankers, Mathijs Mul, and Elia Bruni. 2020. Compositionality decomposed: How do neural networks generalise? *Journal of Artificial Intelligence Research*, 67:757-795.
- Cited in 03_model-evaluation.md (PCFG dataset), 08_related-work.md (generalization failure on PCFG, length generalization in neural sequence models).

## Irie et al. (2019)
Kazuki Irie, Albert Zeyer, Ralf Schluter, and Hermann Ney. 2019. Language modeling with deep transformers. In *Interspeech 2019*, pages 3905-3909.
- Cited in 08_related-work.md (NoPE performance in language modelling).

## Kaiser and Sutskever (2016)
Lukasz Kaiser and Ilya Sutskever. 2016. Neural gpus learn algorithms. In *4th International Conference on Learning Representations, ICLR 2016*.
- Cited in 08_related-work.md (early work on length generalization in neural sequence models).

## Kiyono et al. (2021)
Shun Kiyono, Sosuke Kobayashi, Jun Suzuki, and Kentaro Inui. 2021. SHAPE: Shifted absolute position embedding for transformers. In *Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing*, pages 3309-3321.
- Cited in 07_discussion.md (human cognitive constraints favor short-range dependencies).

## Lake and Baroni (2018)
Brenden M. Lake and Marco Baroni. 2018. Generalization without systematicity: On the compositional skills of sequence-to-sequence recurrent networks. In *Proceedings of the 35th International Conference on Machine Learning, ICML 2018*, volume 80 of *Proceedings of Machine Learning Research*, pages 2879-2888.
- Cited in 03_model-evaluation.md (SCAN dataset), 08_related-work.md (length generalization in neural sequence models).

## Li et al. (2023)
Raymond Li, Loubna Ben Allal, Yangtian Zi, Niklas Muennighoff, Denis Kocetkov, Chenghao Mou, Marc Marone, Christopher Akiki, Jia Li, Jenny Chim, et al. 2023. Starcoder: may the source be with you! *ArXiv*, abs/2305.06161.
- Cited in 07_discussion.md (StarCoder training set used for 1B model scaling experiments), 16_appendix-f.md (StarCoder dataset for 1.3B pretraining; also cited as "Allal et al. (2023)" in the paper text, likely a citation error).

## Liang et al. (2022)
Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian Zhang, Deepak Narayanan, Yuhuai Wu, Ananya Kumar, et al. 2022. Holistic evaluation of language models. *ArXiv*, abs/2211.09110.
- Cited in 04_effect-of-positional-encoding.md (mean ranking methodology).

## Likhomanenko et al. (2021)
Tatiana Likhomanenko, Qiantong Xu, Gabriel Synnaeve, Ronan Collobert, and Alex Rogozhnikov. 2021. CAPE: Encoding relative positions with continuous augmented positional embeddings. In *Advances in Neural Information Processing Systems*.
- Cited in 08_related-work.md (NoPE performance in vision and speech domains).

## Lindner et al. (2023)
David Lindner, Janos Kramar, Matthew Rahtz, Thomas McGrath, and Vladimir Mikulik. 2023. Tracr: Compiled transformers as a laboratory for interpretability. *ArXiv*, abs/2301.05062.
- Cited in 13_appendix-c.md (proof of NoPE absolute encoding inspired by this work).

## Longpre et al. (2023)
Shayne Longpre, Le Hou, Tu Vu, Albert Webson, Hyung Won Chung, Yi Tay, Denny Zhou, Quoc V. Le, Barret Zoph, Jason Wei, and Adam Roberts. 2023. The flan collection: Designing data and methods for effective instruction tuning. *ArXiv*, abs/2301.13688.
- Cited in 11_appendix-a.md (FLAN CoT subset instruction length distribution).

## Luo et al. (2021)
Ziyang Luo, Artur Kulmizev, and Xiaoxi Mao. 2021. Positional artefacts propagate through masked language model embeddings. In *Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)*, pages 5312-5327.
- Cited in 07_discussion.md (growing evidence that positional encodings pose challenges for Transformers).

## Nye et al. (2021)
Maxwell Nye, Anders Andreassen, Guy Gur-Ari, Henryk Michalewski, Jacob Austin, David Bieber, David Dohan, Aitor Lewkowycz, Maarten Bosma, David Luan, Charles Sutton, and Augustus Odena. 2021. Show your work: Scratchpads for intermediate computation with language models. *ArXiv*, abs/2112.00114.
- Cited in 01_introduction.md (scratchpad/chain-of-thought for length extrapolation), 03_model-evaluation.md (Addition task), 06_scratchpad.md (scratchpad improves length generalization; scratchpad format; length threshold L=8), 14_appendix-d.md (Addition and Polynomial Evaluation task descriptions).

## Ontanon et al. (2022)
Santiago Ontanon, Joshua Ainslie, Zachary Fisher, and Vaclav Cvicek. 2022. Making transformers solve compositional tasks. In *Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 3591-3607.
- Cited in 01_introduction.md (APE inadequate for length generalization; relative PEs more effective), 03_model-evaluation.md (Copying and Reversing tasks), 04_effect-of-positional-encoding.md (Rotary considered relative encoding), 08_related-work.md (studying PE effect on length generalization).

## Ouyang et al. (2022)
Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al. 2022. Training language models to follow instructions with human feedback. *ArXiv*, abs/2203.02155.
- Cited in 01_introduction.md (instruction-following datasets), 11_appendix-a.md (SFT-RLHF pipeline).

## Park et al. (2020)
Sejun Park, Chulhee Yun, Jaeho Lee, and Jinwoo Shin. 2020. Minimum width for universal approximation. *ArXiv*.
- Cited in 13_appendix-c.md (MLP with ReLU can learn any arbitrary function, used in NoPE absolute encoding proof).

## Press et al. (2022)
Ofir Press, Noah A. Smith, and Mike Lewis. 2022. Train short, test long: Attention with linear biases enables input length extrapolation. In *The Tenth International Conference on Learning Representations, ICLR 2022*.
- Cited in 01_introduction.md (even relative PEs like Rotary can be poor at length generalization; PE evaluation relies on perplexity), 04_effect-of-positional-encoding.md (T5's Relative Bias computational overhead), 08_related-work.md (ALiBi proposed; simplifying T5's Relative encoding).

## Radford et al. (2019)
Alec Radford, Jeff Wu, Rewon Child, David Luan, Dario Amodei, and Ilya Sutskever. 2019. Language models are unsupervised multitask learners. *OpenAI Blog*, 1(8):9.
- Cited in 01_introduction.md (GPT-family of models).

## Raffel et al. (2020)
Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, and Peter J. Liu. 2020. Exploring the limits of transfer learning with a unified text-to-text transformer. *Journal of Machine Learning Research*, 21:140:1-140:67.
- Cited in 01_introduction.md (relative PEs), 02_background.md (T5), 08_related-work.md (T5 as a relative encoding model).

## Saxton et al. (2019)
David Saxton, Edward Grefenstette, Felix Hill, and Pushmeet Kohli. 2019. Analysing mathematical reasoning abilities of neural models. In *7th International Conference on Learning Representations, ICLR 2019*.
- Cited in 03_model-evaluation.md (Polynomial Evaluation, Sorting, Summation tasks), 14_appendix-d.md (Sorting and Summation task descriptions).

## Scao et al. (2022a)
Teven Le Scao, Angela Fan, Christopher Akiki, Ellie Pavlick, Suzana Ilic, Daniel Hesslow, Roman Castagnet, Alexandra Sasha Luccioni, Francois Yvon, Matthias Galle, et al. 2022a. Bloom: A 176b-parameter open-access multilingual language model. *ArXiv*, abs/2211.05100.
- Cited in 02_background.md (BLOOM uses ALiBi).

## Scao et al. (2022b)
Teven Le Scao, Thomas Wang, Daniel Hesslow, Lucile Saulnier, Stas Bekman, M Saiful Bari, Stella Biderman, Hady Elsahar, Jason Phang, Ofir Press, et al. 2022b. What language model to train if you have one million GPU hours? In *Challenges & Perspectives in Creating Large Language Models*.
- Cited in 07_discussion.md (similar I.I.D. performance across PEs).

## Shaw et al. (2018)
Peter Shaw, Jakob Uszkoreit, and Ashish Vaswani. 2018. Self-attention with relative position representations. In *Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics*, Volume 2 (Short Papers), pages 464-468.
- Cited in 01_introduction.md (relative PEs), 08_related-work.md (introduced relative approach for encoding positional information).

## Shen et al. (2018)
Tao Shen, Tianyi Zhou, Guodong Long, Jing Jiang, Shirui Pan, and Chengqi Zhang. 2018. Disan: Directional self-attention network for rnn/cnn-free language understanding. In *Proceedings of the Thirty-Second AAAI Conference on Artificial Intelligence (AAAI-18)*, pages 5446-5455.
- Cited in 08_related-work.md (early observation that decoder-only Transformers can operate without PE).

## Sinha et al. (2019)
Koustuv Sinha, Shagun Sodhani, Jin Dong, Joelle Pineau, and William L. Hamilton. 2019. CLUTRR: A diagnostic benchmark for inductive reasoning from text. In *Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)*, pages 4506-4515.
- Cited in 08_related-work.md (generalization failure on CLUTRR).

## Sinha et al. (2022)
Koustuv Sinha, Amirhossein Kazemnejad, Siva Reddy, Joelle Pineau, Dieuwke Hupkes, and Adina Williams. 2022. The curious case of absolute position embeddings. In *Findings of the Association for Computational Linguistics: EMNLP 2022*, pages 4449-4472.
- Cited in 07_discussion.md (growing evidence that positional encodings pose challenges for Transformers).

## Su et al. (2021)
Jianlin Su, Yu Lu, Shengfeng Pan, Bo Wen, and Yunfeng Liu. 2021. Roformer: Enhanced transformer with rotary position embedding. *ArXiv*, abs/2104.09864.
- Cited in 01_introduction.md (Rotary PE), 02_background.md (Rotary rotates query and key representations), 08_related-work.md (rotating hidden representations for positional encoding).

## Tay et al. (2022)
Yi Tay, Mostafa Dehghani, Jinfeng Rao, William Fedus, Samira Abnar, Hyung Won Chung, Sharan Narang, Dani Yogatama, Ashish Vaswani, and Donald Metzler. 2022. Scale efficiently: Insights from pretraining and finetuning transformers. In *The Tenth International Conference on Learning Representations, ICLR 2022*.
- Cited in 01_introduction.md (perplexity not always aligned with downstream performance) and 07_discussion.md (importance of downstream task evaluation over perplexity).

## Taylor et al. (2022)
Ross Taylor, Marcin Kardas, Guillem Cucurull, Thomas Scialom, Anthony Hartshorn, Elvis Saravia, Andrew Poulton, Viktor Kerkez, and Robert Stojnic. 2022. Galactica: A large language model for science. *ArXiv*, abs/2211.09085.
- Cited in 04_effect-of-positional-encoding.md (no significant improvement from ALiBi).

## Touvron et al. (2023)
Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothee Lacroix, Baptiste Roziere, Naman Goyal, Eric Hambro, Faisal Azhar, et al. 2023. LLaMA: Open and efficient foundation language models. *ArXiv*, abs/2302.13971.
- Cited in 02_background.md (LLaMA uses Rotary), 07_discussion.md (shift towards Rotary in LLMs).

## Tsai et al. (2019)
Yao-Hung Hubert Tsai, Shaojie Bai, Makoto Yamada, Louis-Philippe Morency, and Ruslan Salakhutdinov. 2019. Transformer dissection: An unified understanding for transformer's attention via the lens of kernel. In *Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)*, pages 4344-4353.
- Cited in 01_introduction.md (decoder-only Transformers without PE), 02_background.md (decoder-only Transformers not permutation invariant), 08_related-work.md (explained why causal attention enables position encoding without PE).

## Vaswani et al. (2017)
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and Illia Polosukhin. 2017. Attention is all you need. In *Advances in Neural Information Processing Systems 30*, pages 5998-6008.
- Cited in 01_introduction.md (original Transformer architecture), 02_background.md (sinusoidal APE), 03_model-evaluation.md (APE sinusoidal functions), 08_related-work.md (introduced absolute positional encoding).

## Wang et al. (2022)
Yizhong Wang, Swaroop Mishra, Pegah Alipoormolabashi, Yeganeh Kordi, Amirreza Mirzaei, Atharva Naik, Arjun Ashok, Arut Selvan Dhanasekaran, Anjana Arunkumar, David Stap, et al. 2022. Super-NaturalInstructions: Generalization via declarative instructions on 1600+ NLP tasks. In *Proc. of EMNLP*, pages 5085-5109. Association for Computational Linguistics.
- Cited in 11_appendix-a.md (Super Natural Instructions instruction length distribution).

## Wei et al. (2022a)
Jason Wei, Maarten Bosma, Vincent Y. Zhao, Kelvin Guu, Adams Wei Yu, Brian Lester, Nan Du, Andrew M. Dai, and Quoc V. Le. 2022a. Finetuned language models are zero-shot learners. In *The Tenth International Conference on Learning Representations, ICLR 2022*.
- Cited in 01_introduction.md (instruction-following datasets).

## Wei et al. (2022b)
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, brian ichter, Fei Xia, Ed H. Chi, Quoc V Le, and Denny Zhou. 2022b. Chain of thought prompting elicits reasoning in large language models. In *Advances in Neural Information Processing Systems*.
- Cited in 01_introduction.md (chain-of-thought for length extrapolation).

## Weiss et al. (2021)
Gail Weiss, Yoav Goldberg, and Eran Yahav. 2021. Thinking like transformers. In *Proceedings of the 38th International Conference on Machine Learning, ICML 2021*, volume 139 of *Proceedings of Machine Learning Research*, pages 11080-11090. PMLR.
- Cited in 13_appendix-c.md (proof of NoPE absolute encoding inspired by this work).

## Wolf et al. (2020)
Thomas Wolf, Lysandre Debut, Victor Sanh, Julien Chaumond, Clement Delangue, Anthony Moi, Pierric Cistac, Tim Rault, Remi Louf, Morgan Funtowicz, et al. 2020. Transformers: State-of-the-art natural language processing. In *Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing: System Demonstrations*, pages 38-45.
- Cited in 03_model-evaluation.md (HuggingFace library for model hyperparameters), 14_appendix-d.md (HuggingFace used for training loop, optimizer, and Transformer architecture).

## Yang et al. (2019)
Baosong Yang, Longyue Wang, Derek F. Wong, Lidia S. Chao, and Zhaopeng Tu. 2019. Assessing the ability of self-attention networks to learn word order. In *Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics*, pages 3635-3644.
- Cited in 08_related-work.md (NoPE performance in machine translation).

## Yehudai et al. (2021)
Gilad Yehudai, Ethan Fetaya, Eli A. Meirom, Gal Chechik, and Haggai Maron. 2021. From local structures to size generalization in graph neural networks. In *Proceedings of the 38th International Conference on Machine Learning, ICML 2021*, volume 139 of *Proceedings of Machine Learning Research*, pages 11975-11986.
- Cited in 08_related-work.md (length generalization in neural sequence models).

## Zhang et al. (2022)
Susan Zhang, Stephen Roller, Naman Goyal, Mikel Artetxe, Moya Chen, Shuohui Chen, Christopher Dewan, Mona Diab, Xian Li, Xi Victoria Lin, et al. 2022. Opt: Open pre-trained transformer language models. *ArXiv*, abs/2205.01068.
- Cited in 02_background.md (OPT uses learned APE).

## Zhang et al. (2023)
Yi Zhang, Arturs Backurs, Sebastien Bubeck, Ronen Eldan, Suriya Gunasekar, and Tal Wagner. 2023. Unveiling transformers with lego: a synthetic reasoning task. *ArXiv*, abs/2206.04301.
- Cited in 01_introduction.md (length generalization challenge), 03_model-evaluation.md (LEGO task), 08_related-work.md (generalization failure on LEGO), 14_appendix-d.md (LEGO task description).
