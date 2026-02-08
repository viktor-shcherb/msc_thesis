# References

Only references cited in the section notes are included below.

---

**Almazrouei et al., 2023**
Ebtesam Almazrouei, Hamza Alobeidli, Abdulaziz Alshamsi, Alessandro Cappelli, Ruxandra Cojocaru, Merouane Debbah, Etienne Goffinet, Daniel Heslow, Julien Launay, Quentin Malartic, Badreddine Noune, Baptiste Pannier, and Guilherme Penedo. Falcon-40B: an open large language model with state-of-the-art performance. 2023.
- Cited in 05_ai-safety.md as one of the open-source LLM baselines (Falcon-instruct) for safety evaluation.

**An et al., 2023**
Chenxin An, Shansan Gong, Ming Zhong, Mukai Li, Jun Zhang, Lingpeng Kong, and Xipeng Qiu. L-eval: Instituting standardized evaluation for long context language models. *arXiv preprint arXiv:2307.11088*, 2023.
- Cited in 03_main-results.md and 09_appendix-a.md as the source of the L-Eval benchmark used for additional long-context evaluation.

**Anthropic, 2023**
Anthropic. Introducing 100K Context Windows, 2023. URL https://www.anthropic.com/index/100k-context-windows.
- Cited in 01_introduction.md and 05_ai-safety.md as a proprietary long-context LLM API provider (Claude-2).

**Austin et al., 2021**
Jacob Austin, Augustus Odena, Maxwell I. Nye, Maarten Bosma, Henryk Michalewski, David Dohan, Ellen Jiang, Carrie J. Cai, Michael Terry, Quoc V. Le, and Charles Sutton. Program synthesis with large language models. *arXiv:abs/2108.07732*, 2021.
- Cited in 03_main-results.md as the source of the MBPP coding benchmark.

**Bisk et al., 2020**
Yonatan Bisk, Rowan Zellers, Jianfeng Gao, Yejin Choi, et al. Piqa: Reasoning about physical commonsense in natural language. In *Proceedings of the AAAI conference on artificial intelligence*, volume 34, pages 7432-7439, 2020.
- Cited in 03_main-results.md as part of the Commonsense benchmark suite (PIQA).

**Chen et al., 2021**
Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde de Oliveira Pinto, Jared Kaplan, Harri Edwards, Yuri Burda, Nicholas Joseph, Greg Brockman, et al. Evaluating large language models trained on code. *arXiv preprint arXiv:2107.03374*, 2021.
- Cited in 03_main-results.md as the source of the HumanEval coding benchmark.

**Chen et al., 2023**
Shouyuan Chen, Sherman Wong, Liangjian Chen, and Yuandong Tian. Extending context window of large language models via positional interpolation, 2023.
- Cited in 01_introduction.md, 02_method.md, 03_main-results.md, 04a_positional-encoding.md, 05_ai-safety.md, and 10_appendix-b.md as the position interpolation (PI) approach and as an existing open-source long-context model that observes degradation on short tasks.

**Child et al., 2019**
Rewon Child, Scott Gray, Alec Radford, and Ilya Sutskever. Generating long sequences with sparse transformers. *arXiv preprint arXiv:1904.10509*, 2019.
- Cited in 02_method.md as the sparse attention approach the authors chose not to apply.

**Clark et al., 2018**
Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar Khot, Ashish Sabharwal, Carissa Schoenick, and Oyvind Tafjord. Think you have solved question answering? try arc, the ai2 reasoning challenge. *arXiv preprint arXiv:1803.05457*, 2018.
- Cited in 03_main-results.md as part of the Commonsense benchmark suite (ARC easy and challenge).

**Cobbe et al., 2021**
Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, et al. Training verifiers to solve math word problems. *arXiv preprint arXiv:2110.14168*, 2021.
- Cited in 03_main-results.md as the source of the GSM8K math benchmark.

**Conover et al., 2023**
Mike Conover, Matt Hayes, Ankit Mathur, Jianwei Xie, Jun Wan, Sam Shah, Ali Ghodsi, Patrick Wendell, Matei Zaharia, and Reynold Xin. Free dolly: Introducing the world's first truly open instruction-tuned llm, 2023. URL https://www.databricks.com/blog/2023/04/12/dolly-first-open-commercially-viable-instruction-tuned-llm.
- Cited in 02_method.md as an example of an open-source instruction dataset predominantly consisting of short samples.

**Dao et al., 2022**
Tri Dao, Daniel Y. Fu, Stefano Ermon, Atri Rudra, and Christopher Re. Flashattention: Fast and memory-efficient exact attention with io-awareness. In *NeurIPS*, 2022.
- Cited in 02_method.md as the FlashAttention technique used for memory-efficient training.

**Dasigi et al., 2021**
Pradeep Dasigi, Kyle Lo, Iz Beltagy, Arman Cohan, Noah A. Smith, and Matt Gardner. A dataset of information-seeking questions and answers anchored in research papers. In *Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies*, pages 4599-4610, Online, June 2021.
- Cited in 03_main-results.md as the source of the Qasper benchmark.

**Dhamala et al., 2021**
Jwala Dhamala, Tony Sun, Varun Kumar, Satyapriya Krishna, Yada Pruksachatkun, Kai-Wei Chang, and Rahul Gupta. Bold: Dataset and metrics for measuring biases in open-ended language generation. In *Proceedings of the 2021 ACM conference on fairness, accountability, and transparency*, pages 862-872, 2021.
- Cited in 05_ai-safety.md as the source of the BOLD safety benchmark.

**Ding et al., 2023**
Jiayu Ding, Shuming Ma, Li Dong, Xingxing Zhang, Shaohan Huang, Wenhui Wang, and Furu Wei. Longnet: Scaling transformers to 1,000,000,000 tokens, 2023.
- Cited in 05_ai-safety.md as a work on the same topic that does not discuss safety performance.

**Greshake et al., 2023**
Kai Greshake, Sahar Abdelnabi, Shailesh Mishra, Christoph Endres, Thorsten Holz, and Mario Fritz. Not what you've signed up for: Compromising real-world llm-integrated applications with indirect prompt injection. *arXiv preprint arXiv:2302.12173*, 2023.
- Cited in 05_ai-safety.md as a reference for prompt injection risks with long-context models.

**Hartvigsen et al., 2022**
Thomas Hartvigsen, Saadia Gabriel, Hamid Palangi, Maarten Sap, Dipankar Ray, and Ece Kamar. Toxigen: A large-scale machine-generated dataset for adversarial and implicit hate speech detection. *arXiv preprint arXiv:2203.09509*, 2022.
- Cited in 05_ai-safety.md as the source of the ToxiGen safety benchmark.

**Hendrycks et al., 2021**
Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. Measuring mathematical problem solving with the math dataset. *arXiv preprint arXiv:2103.03874*, 2021.
- Cited in 03_main-results.md as the source of the MATH benchmark.

**Hoffmann et al., 2022**
Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, Tom Hennigan, Eric Noland, Katie Millican, George van den Driessche, Bogdan Damoc, Aurelia Guy, Simon Osindero, Karen Simonyan, Erich Elsen, Jack W. Rae, Oriol Vinyals, and Laurent Sifre. Training compute-optimal large language models, 2022.
- Cited in 03_main-results.md as inspiration for the power-law scaling relationship with context length.

**Hutto and Gilbert, 2014**
Clayton Hutto and Eric Gilbert. Vader: A parsimonious rule-based model for sentiment analysis of social media text. In *Proceedings of the international AAAI conference on web and social media*, volume 8, pages 216-225, 2014.
- Cited in 05_ai-safety.md as the VADER sentiment analysis tool used for BOLD evaluation.

**Ji et al., 2023**
Ziwei Ji, Nayeon Lee, Rita Frieske, Tiezheng Yu, Dan Su, Yan Xu, Etsuko Ishii, Ye Jin Bang, Andrea Madotto, and Pascale Fung. Survey of hallucination in natural language generation. *ACM Computing Surveys*, 55(12):1-38, 2023.
- Cited in 05_ai-safety.md as a reference for LLMs generating misinformative content.

**Joshi et al., 2017**
Mandar Joshi, Eunsol Choi, Daniel S Weld, and Luke Zettlemoyer. Triviaqa: A large scale distantly supervised challenge dataset for reading comprehension. *arXiv preprint arXiv:1705.03551*, 2017.
- Cited in 03_main-results.md as the source of the TriviaQA benchmark.

**Kaplan et al., 2020**
Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B. Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jeffrey Wu, and Dario Amodei. Scaling laws for neural language models, 2020.
- Cited in 03_main-results.md as inspiration for the power-law scaling relationship with context length.

**Kocisky et al., 2018**
Tomas Kocisky, Jonathan Schwarz, Phil Blunsom, Chris Dyer, Karl Moritz Hermann, Gabor Melis, and Edward Grefenstette. The NarrativeQA reading comprehension challenge. *Transactions of the Association for Computational Linguistics*, 6:317-328, 2018.
- Cited in 03_main-results.md as the source of the NarrativeQA benchmark.

**Kopf et al., 2023**
Andreas Kopf, Yannic Kilcher, Dimitri von Rutte, Sotiris Anagnostidis, Zhi-Rui Tam, Keith Stevens, Abdullah Barhoum, Nguyen Minh Duc, Oliver Stanley, Richard Nagyfi, et al. Openassistant conversations -- democratizing large language model alignment. *arXiv preprint arXiv:2304.07327*, 2023.
- Cited in 02_method.md as an example of an open-source instruction dataset predominantly consisting of short samples.

**Kwiatkowski et al., 2019**
Tom Kwiatkowski, Jennimaria Palomaki, Olivia Redfield, Michael Collins, Ankur Parikh, Chris Alberti, Danielle Epstein, Illia Polosukhin, Jacob Devlin, Kenton Lee, et al. Natural questions: a benchmark for question answering research. *Transactions of the Association for Computational Linguistics*, 7:453-466, 2019.
- Cited in 03_main-results.md as the source of the NaturalQuestions benchmark.

**Lin et al., 2021**
Stephanie Lin, Jacob Hilton, and Owain Evans. Truthfulqa: Measuring how models mimic human falsehoods. *arXiv preprint arXiv:2109.07958*, 2021.
- Cited in 05_ai-safety.md as the source of the TruthfulQA safety benchmark.

**Liu et al., 2019**
Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke Zettlemoyer, and Veselin Stoyanov. Roberta: A robustly optimized bert pretraining approach. *arXiv preprint arXiv:1907.11692*, 2019.
- Cited in 05_ai-safety.md as the basis for the ToxiGen classifier (RoBERTa).

**Mihaylov et al., 2018**
Todor Mihaylov, Peter Clark, Tushar Khot, and Ashish Sabharwal. Can a suit of armor conduct electricity? a new dataset for open book question answering. *arXiv preprint arXiv:1809.02789*, 2018.
- Cited in 03_main-results.md as part of the Commonsense benchmark suite (OpenBookQA).

**Mohtashami and Jaggi, 2023**
Amirkeivan Mohtashami and Martin Jaggi. Landmark attention: Random-access infinite context length for transformers. *arXiv preprint arXiv:2305.16300*, 2023.
- Cited in 01_introduction.md and 03_main-results.md as an existing open-source long-context model and in 04a_positional-encoding.md for the PASSKEY task.

**MosaicML, 2023a**
MosaicML. Introducing mpt-30b: Raising the bar for open-source foundation models, 2023a. URL www.mosaicml.com/blog/mpt-30b. Accessed: 2023-06-22.
- Cited in 05_ai-safety.md as one of the open-source LLM baselines (MPT-instruct) and in 03_main-results.md for long-context comparisons.

**MosaicML, 2023b**
MosaicML. Introducing mpt-7b: A new standard for open-source, ly usable llms, 2023b. URL www.mosaicml.com/blog/mpt-7b.
- Cited in 01_introduction.md and 03_main-results.md as an existing open-source long-context model.

**Narayanan et al., 2021**
Deepak Narayanan, Mohammad Shoeybi, Jared Casper, Patrick LeGresley, Mostofa Patwary, Vijay Korthikanti, Dmitri Vainbrand, Prethvi Kashinkunti, Julie Bernauer, Bryan Catanzaro, et al. Efficient large-scale language model training on gpu clusters using megatron-lm. In *Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis*, pages 1-15, 2021.
- Cited in 02_method.md regarding the computation bottleneck threshold for attention when sequence length exceeds 6h tokens.

**Nijkamp et al., 2023**
Erik Nijkamp, Tian Xie, Hiroaki Hayashi, Bo Pang, Congying Xia, Chen Xing, Jesse Vig, Semih Yavuz, Philippe Laban, Ben Krause, et al. Long sequence modeling with xgen: A 7b llm trained on 8k input sequence length. *Salesforce AI Research Blog*, 2023.
- Cited in 03_main-results.md as one of the open-source long-context models compared against (Xgen-7B-8k-base).

**OpenAI, 2023**
OpenAI. Gpt-4 technical report, 2023.
- Cited in 01_introduction.md and 05_ai-safety.md as a proprietary LLM baseline (GPT-4).

**Ouyang et al., 2022**
Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al. Training language models to follow instructions with human feedback. *Advances in Neural Information Processing Systems*, 35:27730-27744, 2022.
- Cited in 02_method.md regarding the cost and difficulty of collecting human demonstration and preference labels.

**Pang et al., 2022**
Richard Yuanzhe Pang, Alicia Parrish, Nitish Joshi, Nikita Nangia, Jason Phang, Angelica Chen, Vishakh Padmakumar, Johnny Ma, Jana Thompson, He He, and Samuel Bowman. QuALITY: Question answering with long input texts, yes! In *Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies*, pages 5336-5358, Seattle, United States, July 2022.
- Cited in 03_main-results.md as the source of the QuALITY benchmark.

**Peng et al., 2023**
Bowen Peng, Jeffrey Quesnelle, Honglu Fan, and Enrico Shippole. Yarn: Efficient context window extension of large language models, 2023.
- Cited in 01_introduction.md and 03_main-results.md as an existing open-source long-context model (YaRN).

**Roziere et al., 2023**
Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, Sten Sootla, Itai Gat, Xiaoqing Ellen Tan, Yossi Adi, Jingyu Liu, Tal Remez, Jeremy Rapin, Artyom Kozhevnikov, Ivan Evtimov, Joanna Bitton, Manish Bhatt, Cristian Canton Ferrer, Aaron Grattafiori, Wenhan Xiong, Alexandre Defossez, Jade Copet, Faisal Azhar, Hugo Touvron, Louis Martin, Nicolas Usunier, Thomas Scialom, and Gabriel Synnaeve. Code llama: Open foundation models for code, 2023.
- Cited in 04a_positional-encoding.md as concurrent work suggesting the base frequency change idea.

**Sakaguchi et al., 2021**
Keisuke Sakaguchi, Ronan Le Bras, Chandra Bhagavatula, and Yejin Choi. Winogrande: An adversarial winograd schema challenge at scale. *Communications of the ACM*, 64(9):99-106, 2021.
- Cited in 03_main-results.md as part of the Commonsense benchmark suite (WinoGrande).

**Sap et al., 2019**
Maarten Sap, Hannah Rashkin, Derek Chen, Ronan LeBras, and Yejin Choi. Socialiqa: Commonsense reasoning about social interactions. *arXiv preprint arXiv:1904.09728*, 2019.
- Cited in 03_main-results.md as part of the Commonsense benchmark suite (SIQA).

**Shaham et al., 2023**
Uri Shaham, Maor Ivgi, Avia Efrat, Jonathan Berant, and Omer Levy. Zeroscrolls: A zero-shot benchmark for long text understanding, 2023.
- Cited in 03_main-results.md as the source of the ZeroSCROLLS benchmark.

**Su et al., 2022**
Jianlin Su, Yu Lu, Shengfeng Pan, Ahmed Murtadha, Bo Wen, and Yunfeng Liu. Roformer: Enhanced transformer with rotary position embedding, 2022.
- Cited in 02_method.md and 04a_positional-encoding.md as the original RoPE positional encoding.

**Sun et al., 2022**
Yutao Sun, Li Dong, Barun Patra, Shuming Ma, Shaohan Huang, Alon Benhaim, Vishrav Chaudhary, Xia Song, and Furu Wei. A length-extrapolatable transformer, 2022.
- Cited in 04a_positional-encoding.md as the source of xPOS, a variant of rotary encoding that smooths high-frequency components.

**Talmor et al., 2018**
Alon Talmor, Jonathan Herzig, Nicholas Lourie, and Jonathan Berant. Commonsenseqa: A question answering challenge targeting commonsense knowledge. *arXiv preprint arXiv:1811.00937*, 2018.
- Cited in 03_main-results.md as part of the Commonsense benchmark suite (CommonsenseQA).

**Together, 2023**
Together. Llama-2-7b-32k-instruct -- and fine-tuning for llama-2 models with together api, 2023. URL https://together.ai/blog/llama-2-7b-32k-instruct.
- Cited in 03_main-results.md as one of the open-source long-context models compared against (Together-7B-32k).

**Touvron et al., 2023**
Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, et al. Llama 2: Open foundation and fine-tuned chat models. *arXiv preprint arXiv:2307.09288*, 2023.
- Cited extensively throughout (02_method.md, 03_main-results.md, 04c_instruction-tuning.md, 05_ai-safety.md) as the source of LLAMA 2, the RLHF dataset, evaluation methodology, and safety evaluation procedures.

**Tworkowski et al., 2023a**
Szymon Tworkowski, Konrad Staniszewski, Mikolaj Pacek, Yuhuai Wu, Henryk Michalewski, and Piotr Milos. Focused transformer: Contrastive training for context scaling, 2023a.
- Cited in 03_main-results.md as one of the open-source long-context models compared against (Focused Transformer 3B).

**Tworkowski et al., 2023b**
Szymon Tworkowski, Konrad Staniszewski, Mikolaj Pacek, Yuhuai Wu, Henryk Michalewski, and Piotr Milos. Focused transformer: Contrastive training for context scaling, 2023b.
- Cited in 01_introduction.md and 05_ai-safety.md as an existing open-source long-context model that does not discuss safety.

**Wang et al., 2022**
Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Alisa Liu, Noah A Smith, Daniel Khashabi, and Hannaneh Hajishirzi. Self-instruct: Aligning language model with self generated instructions. *arXiv preprint arXiv:2212.10560*, 2022.
- Cited in 02_method.md as the self-instruct method used for synthetic long data generation.

**Zellers et al., 2019**
Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali Farhadi, and Yejin Choi. Hellaswag: Can a machine really finish your sentence?, 2019.
- Cited in 03_main-results.md as part of the Commonsense benchmark suite (HellaSwag).

**Zhong et al., 2021**
Ming Zhong, Da Yin, Tao Yu, Ahmad Zaidi, Mutethia Mutuma, Rahul Jha, Ahmed Hassan Awadallah, Asli Celikyilmaz, Yang Liu, Xipeng Qiu, and Dragomir Radev. QMSum: A new benchmark for query-based multi-domain meeting summarization. In *Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies*, pages 5905-5921, Online, June 2021.
- Cited in 03_main-results.md as the source of the QMSum benchmark.
