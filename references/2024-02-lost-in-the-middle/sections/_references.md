# References

## A

**Arampatzis et al. (2009)**
Avi Arampatzis, Jaap Kamps, and Stephen Robertson. 2009. Where to stop reading a ranked list? threshold optimization using truncated score distributions. In *Proc. of SIGIR*.
- Cited in 05_more-context-case-study.md as a method for ranked list truncation.

## B

**Beltagy et al. (2020)**
Iz Beltagy, Matthew E. Peters, and Arman Cohan. 2020. Longformer: The long-document transformer. ArXiv:2004.05150.
- Cited in 01_introduction.md and 06_related-work.md as an example of factorizing attention into computationally less intensive approximations.

## C

**Chung et al. (2022)**
Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Yunxuan Li, Xuezhi Wang, Mostafa Dehghani, Siddhartha Brahma, et al. 2022. Scaling instruction-finetuned language models. ArXiv:2210.11416.
- Cited in 04_why-not-robust.md as co-reference for Flan-T5-XXL.

## D

**Dai et al. (2019)**
Zihang Dai, Zhilin Yang, Yiming Yang, Jaime Carbonell, Quoc Le, and Ruslan Salakhutdinov. 2019. Transformer-XL: Attentive language models beyond a fixed-length context. In *Proc. of ACL*.
- Cited in 01_introduction.md and 06_related-work.md as an example of attention modifications using recurrence.

**Daniluk et al. (2017)**
Michal Daniluk, Tim Rocktaschel, Johannes Welbl, and Sebastian Riedel. 2017. Frustratingly short attention spans in neural language modeling. In *Proc. of ICLR*.
- Cited in 06_related-work.md as finding that attentive LSTM language models tend to mainly use recent history.

**Dao et al. (2022)**
Tri Dao, Daniel Y. Fu, Stefano Ermon, Atri Rudra, and Christopher Re. 2022. FlashAttention: Fast and memory-efficient exact attention with IO-awareness. ArXiv:2205.14135.
- Cited in 01_introduction.md and 06_related-work.md as providing faster exact attention via an IO-aware CUDA kernel.

## E

**Ebbinghaus (1913)**
Hermann Ebbinghaus. 1913. Memory: A contribution to experimental psychology. *H. A. Ruger & C. E. Bussenius, Trans.*
- Cited in 06_related-work.md as foundational work on the serial-position effect.

## G

**Gu et al. (2022)**
Albert Gu, Karan Goel, and Christopher Re. 2022. Efficiently modeling long sequences with structured state spaces. In *Proc. of ICLR*.
- Cited in 06_related-work.md as the S4 model for removing quadratic sequence length complexity.

## I

**Ivgi et al. (2023)**
Maor Ivgi, Uri Shaham, and Jonathan Berant. 2023. Efficient long-text understanding with short-text models. *Transactions of the Association for Computational Linguistics*, 11:284-299.
- Cited in 02_multi-document-question-answering.md as conducting similar needle-in-a-haystack experiments comparing beginning vs. random placement.

**Izacard et al. (2021)**
Gautier Izacard, Mathilde Caron, Lucas Hosseini, Sebastian Riedel, Piotr Bojanowski, Armand Joulin, and Edouard Grave. 2021. Unsupervised dense information retrieval with contrastive learning. ArXiv:2112.09118.
- Cited in 02_multi-document-question-answering.md as the Contriever retrieval system used to collect distractor documents, and in 09_appendix-a.md as part of the NaturalQuestions-Open retrieval setup.

**Izacard and Grave (2021)**
Gautier Izacard and Edouard Grave. 2021. Leveraging passage retrieval with generative models for open domain question answering. In *Proc. of EACL*.
- Cited in 09_appendix-a.md as prior work on NaturalQuestions-Open.

## K

**Kandpal et al. (2022)**
Nikhil Kandpal, Haikang Deng, Adam Roberts, Eric Wallace, and Colin Raffel. 2022. Large language models struggle to learn long-tail knowledge. ArXiv:2211.08411.
- Cited in 02_multi-document-question-answering.md as prior work using accuracy as the evaluation metric.

**Khandelwal et al. (2018)**
Urvashi Khandelwal, He He, Peng Qi, and Dan Jurafsky. 2018. Sharp nearby, fuzzy far away: How neural language models use context. In *Proc. of ACL*.
- Cited in 04_why-not-robust.md, 06_related-work.md, and 13_appendix-e.md as pioneering work showing small LSTM language models make increasingly coarse use of longer-term context, and that non-instruction fine-tuned models are biased towards recent tokens.

**Krishna et al. (2022)**
Kalpesh Krishna, Yapei Chang, John Wieting, and Mohit Iyyer. 2022. RankGen: Improving text generation with large ranking models. In *Proc. of EMNLP*.
- Cited in 06_related-work.md as finding that long-context neural generation in modestly-sized Transformer language models degenerates.

**Kwiatkowski et al. (2019)**
Tom Kwiatkowski, Jennimaria Palomaki, Olivia Redfield, Michael Collins, Ankur Parikh, Chris Alberti, Danielle Epstein, Illia Polosukhin, Jacob Devlin, Kenton Lee, Kristina Toutanova, Llion Jones, Matthew Kelcey, Ming-Wei Chang, Andrew M. Dai, Jakob Uszkoreit, Quoc Le, and Slav Petrov. 2019. Natural Questions: A benchmark for question answering research. *Transactions of the Association for Computational Linguistics*, 7:452-466.
- Cited in 02_multi-document-question-answering.md as the source of the NaturalQuestions dataset.

## L

**Lee et al. (2019)**
Kenton Lee, Ming-Wei Chang, and Kristina Toutanova. 2019. Latent retrieval for weakly supervised open domain question answering. In *Proc. of ACL*.
- Cited in 02_multi-document-question-answering.md as part of the NaturalQuestions-Open reference.

**Lee et al. (2022)**
Mina Lee, Percy Liang, and Qian Yang. 2022. CoAuthor: Designing a human-AI collaborative writing dataset for exploring language model capabilities. In *Proc. of CHI*.
- Cited in 01_introduction.md as an example of collaborative writing applications.

**Li et al. (2023)**
Dacheng Li, Rulin Shao, Anze Xie, Ying Sheng, Lianmin Zheng, Joseph E. Gonzalez, Ion Stoica, Xuezhe Ma, and Hao Zhang. 2023. How long can open-source LLMs truly promise on context length?
- Cited in 02_multi-document-question-answering.md as the source of LongChat-13B (16K) and in 03_key-value-retrieval.md for the fine-grained line retrieval task.

## M

**Mallen et al. (2023)**
Alex Mallen, Akari Asai, Victor Zhong, Rajarshi Das, Daniel Khashabi, and Hannaneh Hajishirzi. 2023. When not to trust language models: Investigating effectiveness of parametric and non-parametric memories. In *Proc. of ACL*.
- Cited in 01_introduction.md and 02_multi-document-question-answering.md as prior work on evaluation methodology and as augmenting LMs with external information.

**Min et al. (2020)**
Sewon Min, Julian Michael, Hannaneh Hajishirzi, and Luke Zettlemoyer. 2020. AmbigQA: Answering ambiguous open-domain questions. In *Proc. of EMNLP*.
- Cited in 09_appendix-a.md as the source of ambiguity annotations used to create a subset of unambiguous questions.

**Murdock Jr (1962)**
Bennet B. Murdock Jr. 1962. The serial position effect of free recall. *Journal of experimental psychology*, 64(5):482.
- Cited in 06_related-work.md as foundational work on the serial-position effect in psychology.

## O

**O'Connor and Andreas (2021)**
Joe O'Connor and Jacob Andreas. 2021. What context features can Transformer language models use? In *Proc. of ACL*.
- Cited in 03_key-value-retrieval.md and 06_related-work.md as finding that many information-destroying operations had marginal effects on Transformer LMs' predictions.

## P

**Papailiopoulos et al. (2023)**
Dimitris Papailiopoulos, Kangwook Lee, and Jy-yong Sohn. 2023. A little retrieval test for large language models. https://github.com/anadim/the-little-retrieval-test.
- Cited in 03_key-value-retrieval.md as sharing similar goals with the key-value retrieval task (Little Retrieval Test).

**Peng (2023)**
Bo Peng. 2023. RWKV-LM. https://github.com/BlinkDL/RWKV-LM.
- Cited in 06_related-work.md as an example of replacing attention with convolution/linear RNNs.

**Peng et al. (2021)**
Hao Peng, Nikolaos Pappas, Dani Yogatama, Roy Schwartz, Noah Smith, and Lingpeng Kong. 2021. Random feature attention. In *Proc. of ICLR*.
- Cited in 06_related-work.md as an example of low-rank approximations for attention.

**Petroni et al. (2020)**
Fabio Petroni, Patrick Lewis, Aleksandra Piktus, Tim Rocktaschel, Yuxiang Wu, Alexander H Miller, and Sebastian Riedel. 2020. How context affects language models' factual predictions. In *Proc. of AKBC*.
- Cited in 01_introduction.md and 06_related-work.md as among the first to demonstrate combining context from IR systems with pretrained LMs for unsupervised QA.

**Poli et al. (2023)**
Michael Poli, Stefano Massaroli, Eric Nguyen, Daniel Y. Fu, Tri Dao, Stephen Baccus, Yoshua Bengio, Stefano Ermon, and Christopher Re. 2023. Hyena hierarchy: Towards larger convolutional language models. In *Proc. of ICML*.
- Cited in 01_introduction.md and 06_related-work.md as an example of replacing attention with convolution.

**Press et al. (2021)**
Ofir Press, Noah A. Smith, and Mike Lewis. 2021. Shortformer: Better language modeling using shorter inputs. In *Proc. of ACL*.
- Cited in 04_why-not-robust.md as prior work finding recency bias in non-instruction fine-tuned language models.

**Press et al. (2022)**
Ofir Press, Noah A. Smith, and Mike Lewis. 2022. Train short, test long: Attention with linear biases enables input length extrapolation. In *Proc. of ICLR*.
- Cited in 02_multi-document-question-answering.md as the ALiBi positional encoding used in MPT-30B-Instruct.

## Q

**Qin et al. (2023)**
Guanghui Qin, Yukun Feng, and Benjamin Van Durme. 2023. The NLP task effectiveness of long-range transformers. In *Proc. of EACL*.
- Cited in 06_related-work.md as finding that long-context transformers are recency-biased and do not effectively use long-range context.

## R

**Raffel et al. (2020)**
Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, and Peter J. Liu. 2020. Exploring the limits of transfer learning with a unified text-to-text Transformer. *Journal of Machine Learning Research*, 21(140):1-67.
- Cited in 04_why-not-robust.md as co-reference for Flan-T5-XXL (T5 architecture).

**Ram et al. (2023)**
Ori Ram, Yoav Levine, Itay Dalmedigos, Dor Muhlgay, Amnon Shashua, Kevin Leyton-Brown, and Yoav Shoham. 2023. In-context retrieval-augmented language models. ArXiv:2302.00083.
- Cited in 01_introduction.md as an example of augmenting LMs with external information.

**Rubin and Berant (2023)**
Ohad Rubin and Jonathan Berant. 2023. Long-range language modeling with self-retrieval. ArXiv:2306.13421.
- Cited in 01_introduction.md as an algorithmic improvement enabling larger context windows.

## S

**Sankar et al. (2019)**
Chinnadhurai Sankar, Sandeep Subramanian, Chris Pal, Sarath Chandar, and Yoshua Bengio. 2019. Do neural dialog systems use the conversation history effectively? an empirical study. In *Proc. of ACL*.
- Cited in 06_related-work.md as finding similar results to Khandelwal et al. (2018) in dialogue models.

**Schick et al. (2023)**
Timo Schick, Jane Dwivedi-Yu, Roberto Dessi, Roberta Raileanu, Maria Lomeli, Luke Zettlemoyer, Nicola Cancedda, and Thomas Scialom. 2023. Toolformer: Language models can teach themselves to use tools.
- Cited in 01_introduction.md as an example of augmenting LMs with external information.

**Shaham et al. (2023)**
Uri Shaham, Maor Ivgi, Avia Efrat, Jonathan Berant, and Omer Levy. 2023. ZeroSCROLLS: A zero-shot benchmark for long text understanding. ArXiv:2305.14196.
- Cited in 04_why-not-robust.md as finding that Flan-T5-XXL and Flan-UL2 can perform well with sequences of up to 8K tokens.

**Sharan et al. (2018)**
Vatsal Sharan, Sham Kakade, Percy Liang, and Gregory Valiant. 2018. Prediction with a short memory. In *Proc. of STOC*.
- Cited in 06_related-work.md as showing that sequence distributions with bounded mutual information necessarily lead to marginal average prediction benefits from increasingly long context.

**Shi et al. (2023)**
Weijia Shi, Sewon Min, Michihiro Yasunaga, Minjoon Seo, Rich James, Mike Lewis, Luke Zettlemoyer, and Wen tau Yih. 2023. REPLUG: Retrieval-augmented black-box language models. ArXiv:2301.12652.
- Cited in 01_introduction.md as an example of augmenting LMs with external information.

**Shuster et al. (2022)**
Kurt Shuster, Jing Xu, Mojtaba Komeili, Da Ju, Eric Michael Smith, Stephen Roller, Megan Ung, Moya Chen, Kushal Arora, Joshua Lane, Morteza Behrooz, William Ngan, Spencer Poff, Naman Goyal, Arthur Szlam, Y-Lan Boureau, Melanie Kambadur, and Jason Weston. 2022. BlenderBot 3: a deployed conversational agent that continually learns to responsibly engage. ArXiv:2208.03188.
- Cited in 01_introduction.md as an example of conversational interface applications.

**Sun et al. (2021)**
Simeng Sun, Kalpesh Krishna, Andrew Mattarella-Micke, and Mohit Iyyer. 2021. Do long-range language models actually use long-range context? In *Proc. of EMNLP*.
- Cited in 04_why-not-robust.md, 06_related-work.md, and 13_appendix-e.md as finding that longer contexts improve prediction of only a few tokens, and that recency bias was observed in next-word prediction of contiguous text.

## T

**Tay et al. (2023)**
Yi Tay, Mostafa Dehghani, Vinh Q. Tran, Xavier Garcia, Jason Wei, Xuezhi Wang, Hyung Won Chung, Siamak Shakeri, Dara Bahri, Tal Schuster, Huaixiu Steven Zheng, Denny Zhou, Neil Houlsby, and Donald Metzler. 2023. UL2: Unifying language learning paradigms. ArXiv:2205.05131.
- Cited in 04_why-not-robust.md as the source of Flan-UL2.

**Thoppilan et al. (2022)**
Romal Thoppilan, Daniel De Freitas, Jamie Hall, Noam Shazeer, Apoorv Kulshreshtha, Heng-Tze Cheng, Alicia Jin, Taylor Bos, Leslie Baker, Yu Du, et al. 2022. LaMDA: Language models for dialog applications. ArXiv:2201.08239.
- Cited in 01_introduction.md as an example of conversational interface applications.

**Touvron et al. (2023a)**
Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothee Lacroix, Baptiste Roziere, Naman Goyal, Eric Hambro, Faisal Azhar, Aurelien Rodriguez, Armand Joulin, Edouard Grave, and Guillaume Lample. 2023a. LLaMA: Open and efficient foundation language models. ArXiv:2302.13971.
- Cited in 02_multi-document-question-answering.md as the base model for LongChat-13B (16K).

**Touvron et al. (2023b)**
Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, et al. 2023b. Llama 2: Open foundation and fine-tuned chat models. ArXiv:2307.09288.
- Cited in 13_appendix-e.md as the source of Llama-2 models evaluated on multi-document QA.

## V

**Vaswani et al. (2017)**
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and Illia Polosukhin. 2017. Attention is all you need. In *Proc. of NeurIPS*.
- Cited in 01_introduction.md as the original Transformer architecture paper.

## W

**Wang et al. (2020)**
Sinong Wang, Belinda Z. Li, Madian Khabsa, Han Fang, and Hao Ma. 2020. Linformer: Self-attention with linear complexity. ArXiv:2006.04768.
- Cited in 06_related-work.md as an example of low-rank approximations for attention.

## Z

**Zaheer et al. (2020)**
Manzil Zaheer, Guru Guruganesh, Kumar Avinava Dubey, Joshua Ainslie, Chris Alberti, Santiago Ontanon, Philip Pham, Anirudh Ravula, Qifan Wang, Li Yang, and Amr Ahmed. 2020. Big Bird: Transformers for longer sequences. In *Proc. of NeurIPS*.
- Cited in 06_related-work.md as an example of factorizing attention into computationally less intensive approximations.
