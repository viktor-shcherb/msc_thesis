# References

Only references actually cited in the section notes are included below.

---

**Acemoglu and Restrepo (2018)**
Daron Acemoglu and Pascual Restrepo. Artificial intelligence, automation, and work. In *The economics of artificial intelligence: An agenda*, pages 197--236. University of Chicago Press, 2018.
- Cited in 06_related-work.md as a broader societal concern (job displacement due to AI).

**Ainslie et al. (2023)**
Joshua Ainslie, James Lee-Thorp, Michiel de Jong, Yury Zemlyanskiy, Federico Lebron, and Sumit Sanghai. Gqa: Training generalized multi-query transformer models from multi-head checkpoints, 2023.
- Cited in 01_introduction.md for grouped-query attention adopted in Llama 2.

**Almazrouei et al. (2023)**
Ebtesam Almazrouei, Hamza Alobeidli, Abdulaziz Alshamsi, Alessandro Cappelli, Ruxandra Cojocaru, Merouane Debbah, Etienne Goffinet, Daniel Heslow, Julien Launay, Quentin Malartic, Badreddine Noune, Baptiste Pannier, and Guilherme Penedo. Falcon-40B: an open large language model with state-of-the-art performance. 2023.
- Cited in 02_pretraining.md and 04_safety.md as a baseline model (Falcon) for evaluation.

**Anil et al. (2023)**
Rohan Anil, Andrew M. Dai, Orhan Firat, Melvin Johnson, Dmitry Lepikhin, Alexandre Passos, Siamak Shakeri, Emanuel Taropa, Paige Bailey, Zhifeng Chen, et al. Palm 2 technical report, 2023.
- Cited in 02_pretraining.md (Table 4, PaLM-2-L results), 03_fine-tuning.md (PaLM baseline in human evaluation), and 14_appendix-a7-model-card.md (model card framework reference).

**Askell et al. (2021a)**
Amanda Askell, Yuntao Bai, Anna Chen, Dawn Drain, Deep Ganguli, Tom Henighan, Andy Jones, Nicholas Joseph, Ben Mann, Nova DasSarma, et al. A general language assistant as a laboratory for alignment. *arXiv preprint arXiv:2112.00861*, 2021a.
- Cited in 04_safety.md for context distillation technique used in safety fine-tuning.

**Askell et al. (2021b)**
Amanda Askell, Yuntao Bai, Anna Chen, Dawn Drain, Deep Ganguli, Tom Henighan, Andy Jones, Nicholas Joseph, Ben Mann, Nova DasSarma, et al. A general language assistant as a laboratory for alignment. *arXiv preprint arXiv:2112.00861*, 2021b.
- Cited in 04_safety.md for context distillation in safety fine-tuning.

**Austin et al. (2021)**
Jacob Austin, Augustus Odena, Maarten Nye, Maarten Bosma, Henryk Michalewski, David Dohan, Ellen Jiang, Carrie Cai, Michael Terry, Quoc Le, and Charles Sutton. Program synthesis with large language models, 2021.
- Cited in 02_pretraining.md as the MBPP benchmark for code evaluation.

**Autor and Salomons (2018)**
David Autor and Anna Salomons. Is automation labor-displacing? Productivity growth, employment, and the labor share. Technical report, National Bureau of Economic Research, 2018.
- Cited in 06_related-work.md as a broader societal concern (job displacement).

**Bai et al. (2022a)**
Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort, Deep Ganguli, Tom Henighan, et al. Training a helpful and harmless assistant with reinforcement learning from human feedback. *arXiv preprint arXiv:2204.05862*, 2022a.
- Cited in 03_fine-tuning.md (Anthropic Helpful/Harmless dataset; helpfulness-safety trade-off; two separate reward models) and 04_safety.md (RLHF robustness to jailbreaks; safety data scaling tension).

**Bai et al. (2022b)**
Yuntao Bai, Saurav Kadavath, Sandipan Kundu, Amanda Askell, Jackson Kernion, Andy Jones, Anna Chen, Anna Goldie, Azalia Mirhoseini, Cameron McKinnon, et al. Constitutional ai: Harmlessness from ai feedback. *arXiv preprint arXiv:2212.08073*, 2022b.
- Cited in 03_fine-tuning.md (rejection sampling approach) and 06_related-work.md (RLAIF -- RL from AI Feedback).

**Bailey et al. (2022)**
April H Bailey, Adina Williams, and Andrei Cimpian. Based on billions of words on the internet, people=men. *Science Advances*, 8(13):eabm2463, 2022.
- Cited in 04_safety.md for bias in text corpora showing "people" used more similarly to "men" than "women."

**Bender et al. (2021a)**
Emily M Bender, Timnit Gebru, Angelina McMillan-Major, and Margaret Mitchell. On the dangers of stochastic parrots: Can language models be too big? In *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency*, pages 610--623, 2021a.
- Cited in 02_pretraining.md for carbon footprint considerations.

**Bender et al. (2021b)**
Emily M Bender, Timnit Gebru, Angelina McMillan-Major, and Shmargaret Shmitchell. On the dangers of stochastic parrots: Can language models be too big? In *Proceedings of the 2021 ACM conference on fairness, accountability, and transparency*, pages 610--623, 2021b.
- Cited in 01_introduction.md (potential risks of LLMs), 04_safety.md (relationship between dataset size and toxicity), and 06_related-work.md (hazards of LLMs).

**Bergman et al. (2022)**
A Stevie Bergman, Gavin Abercrombie, Shannon L Spruit, Dirk Hovy, Emily Dinan, Y-Lan Boureau, and Verena Rieser. Guiding the release of safer e2e conversational ai through value sensitive design. In *Proceedings of the 23rd Annual Meeting of the Special Interest Group on Discourse and Dialogue*, pages 39--52, 2022.
- Cited in 06_related-work.md for balancing positive and negative impacts of releasing dialogue models.

**Bhatt et al. (2022)**
Shaily Bhatt, Sunipa Dev, Partha Talukdar, Shachi Dave, and Vinodkumar Prabhakaran. Re-contextualizing fairness in nlp: The case of india, 2022.
- Cited in 04_safety.md for Western skew in demographic representation.

**Bisk et al. (2020)**
Yonatan Bisk, Rowan Zellers, Jianfeng Gao, Yejin Choi, et al. Piqa: Reasoning about physical commonsense in natural language. In *Proceedings of the AAAI conference on artificial intelligence*, pages 7432--7439, 2020.
- Cited in 02_pretraining.md as the PIQA benchmark for commonsense reasoning.

**Blodgett et al. (2021)**
Su Lin Blodgett, Gilsinia Lopez, Alexandra Olteanu, Robert Sim, and Hanna Wallach. Stereotyping norwegian salmon: An inventory of pitfalls in fairness benchmark datasets. In *Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)*, pages 1004--1015, 2021.
- Cited in 04_safety.md for linguistic markedness differences between gendered terms.

**Bojanowski et al. (2016)**
Piotr Bojanowski, Edouard Grave, Armand Joulin, and Tomas Mikolov. Enriching word vectors with subword information. *CoRR*, abs/1607.04606, 2016.
- Cited in 04_safety.md for fastText language identification tool.

**Brown et al. (2020)**
Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. Language models are few-shot learners. In *Advances in Neural Information Processing Systems*, volume 33, pages 1877--1901, 2020.
- Cited in 01_introduction.md and 06_related-work.md as GPT-3 baseline; cited in 13_appendix-a6-dataset-contamination.md as prior work on measuring dataset contamination.

**Chen et al. (2021)**
Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde de Oliveira Pinto, Jared Kaplan, Harri Edwards, et al. Evaluating large language models trained on code, 2021.
- Cited in 02_pretraining.md as the HumanEval benchmark for code evaluation.

**Chiang et al. (2023)**
Wei-Lin Chiang, Zhuohan Li, Zi Lin, Ying Sheng, Zhanghao Wu, Hao Zhang, Lianmin Zheng, Siyuan Zhuang, Yonghao Zhuang, Joseph E. Gonzalez, Ion Stoica, and Eric P. Xing. Vicuna: An open-source chatbot impressing gpt-4 with 90%* chatgpt quality, March 2023.
- Cited in 03_fine-tuning.md, 04_safety.md, and 06_related-work.md as Vicuna baseline.

**Choi et al. (2018)**
Eunsol Choi, He He, Mohit Iyyer, Mark Yatskar, Wen-tau Yih, Yejin Choi, Percy Liang, and Luke Zettlemoyer. Quac: Question answering in context. In *Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing*, pages 2174--2184, 2018.
- Cited in 02_pretraining.md as the QuAC benchmark for reading comprehension.

**Chowdhery et al. (2022)**
Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, et al. Palm: Scaling language modeling with pathways, 2022.
- Cited in 02_pretraining.md (Table 4, PaLM results), 04_safety.md (pronoun frequency in pretraining data), and 13_appendix-a6-dataset-contamination.md (prior methodology for n-gram contamination detection).

**Christiano et al. (2017)**
Paul F Christiano, Jan Leike, Tom Brown, Miljan Martic, Shane Legg, and Dario Amodei. Deep reinforcement learning from human preferences. *Advances in neural information processing systems*, 30, 2017.
- Cited in 06_related-work.md as originator of RLHF.

**Chung et al. (2022)**
Hyung Won Chung, Le Hou, S. Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang, Mostafa Dehghani, Siddhartha Brahma, et al. Scaling instruction-finetuned language models. *arXiv preprint arXiv:2210.11416*, 2022.
- Cited in 03_fine-tuning.md (publicly available instruction tuning data) and 06_related-work.md (instruction tuning research).

**Clark et al. (2018)**
Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar Khot, Ashish Sabharwal, Carissa Schoenick, and Oyvind Tafjord. Think you have solved question answering? Try arc, the ai2 reasoning challenge. *arXiv preprint arXiv:1803.05457*, 2018.
- Cited in 02_pretraining.md as the ARC benchmark for commonsense reasoning.

**Clark et al. (2019)**
Christopher Clark, Kenton Lee, Ming-Wei Chang, Tom Kwiatkowski, Michael Collins, and Kristina Toutanova. Boolq: Exploring the surprising difficulty of natural yes/no questions. *arXiv preprint arXiv:1905.10044*, 2019.
- Cited in 02_pretraining.md as the BoolQ benchmark for reading comprehension.

**Clark et al. (2021)**
Elizabeth Clark, Tal August, Sofia Serrano, Nikita Haduong, Suchin Gururangan, and Noah A. Smith. All that's 'human' is not gold: Evaluating human evaluation of generated text. In *Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics*, pages 7282--7296, 2021.
- Cited in 03_fine-tuning.md for HCI considerations in human evaluation of LLMs.

**Cobbe et al. (2021)**
Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, et al. Training verifiers to solve math word problems. *arXiv preprint arXiv:2110.14168*, 2021.
- Cited in 02_pretraining.md as the GSM8K benchmark for math evaluation.

**Deng et al. (2019)**
Yuntian Deng, Anton Bakhtin, Myle Ott, Arthur Szlam, and Marc'Aurelio Ranzato. Residual energy-based models for text generation. In *International Conference on Learning Representations*, 2019.
- Cited in 03_fine-tuning.md for re-ranking strategy using reward as energy function.

**Deng et al. (2023)**
Jiawen Deng, Hao Sun, Zhexin Zhang, Jiale Cheng, and Minlie Huang. Recent advances towards safe, responsible, and moral dialogue systems: A survey. *arXiv preprint arXiv:2302.09270*, 2023.
- Cited in 06_related-work.md for taxonomic framework for safety issues.

**Dhamala et al. (2021)**
Jwala Dhamala, Tony Sun, Varun Kumar, Satyapriya Krishna, Yada Pruksachatkun, Kai-Wei Chang, and Rahul Gupta. BOLD: Dataset and metrics for measuring biases in open-ended language generation. In *Proceedings of the 2021 ACM conference on fairness, accountability, and transparency*, pages 862--872, 2021.
- Cited in 04_safety.md as the BOLD benchmark for measuring bias.

**Dinan et al. (2021)**
Emily Dinan, Gavin Abercrombie, A Stevie Bergman, Shannon Spruit, Dirk Hovy, Y-Lan Boureau, and Verena Rieser. Anticipating safety issues in e2e conversational ai: Framework and tooling. *arXiv preprint arXiv:2107.03451*, 2021.
- Cited in 06_related-work.md for difficulties tied to chatbot-oriented LLMs.

**Dodge et al. (2021)**
Jesse Dodge, Maarten Sap, Ana Marasovic, William Agnew, Gabriel Ilharco, Dirk Groeneveld, Margaret Mitchell, and Matt Gardner. Documenting large webtext corpora: A case study on the colossal clean crawled corpus. In *Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing*, pages 1286--1305, 2021.
- Cited in 04_safety.md for ongoing empirical work on pretraining dataset size and toxicity/bias.

**Dodge et al. (2022)**
Jesse Dodge, Taylor Prewitt, Remi Tachet Des Combes, Erika Odmark, Roy Schwartz, Emma Strubell, Alexandra Sasha Luccioni, Noah A Smith, Nicole DeCario, and Will Buchanan. Measuring the carbon intensity of ai in cloud instances. *arXiv preprint arXiv:2206.05229*, 2022.
- Cited in 02_pretraining.md for carbon footprint of pretraining.

**Du et al. (2022)**
Nan Du, Yanping Huang, Andrew M Dai, Simon Tong, Dmitry Lepikhin, Yuanzhong Xu, Maxim Krikun, Yanqi Zhou, Adams Wei Yu, Orhan Firat, Barret Zoph, Liam Fedus, Maarten P Bosma, Zongwei Zhou, Tao Wang, Emma Wang, Kellie Webster, Marie Pellat, Kevin Robinson, Kathleen Meier-Hellstern, Toju Duke, Lucas Dixon, Kun Zhang, Quoc Le, Yonghui Wu, Zhifeng Chen, and Claire Cui. GLaM: Efficient scaling of language models with mixture-of-experts. In *Proceedings of the 39th International Conference on Machine Learning*, volume 162, pages 5547--5569. PMLR, 2022.
- Cited in 13_appendix-a6-dataset-contamination.md as prior work on measuring dataset contamination.

**Ethayarajh et al. (2022)**
Kawin Ethayarajh, Yejin Choi, and Swabha Swayamdipta. Understanding dataset difficulty with V-usable information. In *Proceedings of the 39th International Conference on Machine Learning*, volume 162, pages 5988--6008. PMLR, 2022.
- Cited in 03_fine-tuning.md as the Stanford Human Preferences (SHP) dataset for reward modeling.

**Ganesh et al. (2023)**
Prakhar Ganesh, Hongyan Chang, Martin Strobel, and Reza Shokri. On the impact of machine learning randomness on group fairness. In *2023 ACM Conference on Fairness, Accountability, and Transparency*, pages 1789--1800, 2023.
- Cited in 04_safety.md for model fairness dependence on training data for underrepresented groups.

**Ganguli et al. (2022)**
Deep Ganguli, Liane Lovitt, Jackson Kernion, Amanda Askell, Yuntao Bai, Saurav Kadavath, Ben Mann, Ethan Perez, Nicholas Schiefer, Kamal Ndousse, et al. Red teaming language models to reduce harms: Methods, scaling behaviors, and lessons learned. *arXiv preprint arXiv:2209.07858*, 2022.
- Cited in 06_related-work.md for red teaming revealing specific challenges in tuned LLMs.

**Ganguli et al. (2023)**
Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini, Catherine Olsson, Danny Hernandez, et al. The capacity for moral self-correction in large language models. *arXiv preprint arXiv:2302.07459*, 2023.
- Cited in 06_related-work.md for using follow-up instructions to refine generations.

**Gao et al. (2021)**
Leo Gao, Jonathan Tow, Stella Biderman, Sid Black, Anthony DiPofi, Charles Foster, Laurence Golding, Jeffrey Hsu, Kyle McDonell, Niklas Muennighoff, Jason Phang, Laria Reynolds, Eric Tang, Anish Thite, Ben Wang, Kevin Wang, and Andy Zou. A framework for few-shot language model evaluation, September 2021.
- Cited in 13_appendix-a6-dataset-contamination.md as an open-sourced evaluation library using n-gram contamination detection.

**Gehrmann et al. (2023)**
Sebastian Gehrmann, Elizabeth Clark, and Thibault Sellam. Repairing the cracked foundation: A survey of obstacles in evaluation practices for generated text. *Journal of Artificial Intelligence Research*, 77:103--166, 2023.
- Cited in 03_fine-tuning.md for HCI considerations in human evaluation.

**Gilardi et al. (2023)**
Fabrizio Gilardi, Meysam Alizadeh, and Mael Kubli. Chatgpt outperforms crowd-workers for text-annotation tasks. *arXiv preprint arXiv:2303.15056*, 2023.
- Cited in 05_discussion.md for evidence that LLMs surpass human annotators in certain tasks.

**Gudibande et al. (2023)**
Arnav Gudibande, Eric Wallace, Charlie Snell, Xinyang Geng, Hao Liu, Pieter Abbeel, Sergey Levine, and Dawn Song. The false promise of imitating proprietary llms. *arXiv preprint arXiv:2305.15717*, 2023.
- Cited in 06_related-work.md for alignment techniques in production LLMs.

**Gupta et al. (2022a)**
Udit Gupta, Mariam Elgamal, Gage Hills, Gu-Yeon Wei, Hsien-Hsin S Lee, David Brooks, and Carole-Jean Wu. Act: designing sustainable computer systems with an architectural carbon modeling tool. In *Proceedings of the 49th Annual International Symposium on Computer Architecture*, pages 784--799, 2022a.
- Cited in 02_pretraining.md for carbon footprint of AI hardware production.

**Gupta et al. (2022b)**
Udit Gupta, Young Guen Kim, Sylvia Lee, Jordan Tse, Hsien-Hsin Sean Lee, Gu-Yeon Wei, David Brooks, and Carole-Jean Wu. Chasing carbon: The elusive environmental footprint of computing. *IEEE Micro*, 2022b.
- Cited in 02_pretraining.md for carbon footprint of AI hardware production.

**Gwet (2008)**
Kilem Li Gwet. Computing inter-rater reliability and its variance in the presence of high agreement. *British Journal of Mathematical and Statistical Psychology*, 61(1):29--48, 2008.
- Cited in 03_fine-tuning.md for Gwet's AC1/2 statistic used to measure inter-rater reliability.

**Gwet (2014)**
Kilem L. Gwet. *Handbook of inter-rater reliability: The definitive guide to measuring the extent of agreement among raters*. Advanced Analytics, LLC, 2014.
- Cited in 03_fine-tuning.md for inter-rater reliability measurement.

**Hartvigsen et al. (2022)**
Thomas Hartvigsen, Saadia Gabriel, Hamid Palangi, Maarten Sap, Dipankar Ray, and Ece Kamar. Toxigen: A large-scale machine-generated dataset for adversarial and implicit hate speech detection. In *Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 3309--3326, 2022.
- Cited in 04_safety.md as the ToxiGen dataset/benchmark for toxicity measurement.

**Havrilla**
Alex Havrilla. synthetic-instruct-gptj-pairwise. https://huggingface.co/datasets/Dahoas/synthetic-instruct-gptj-pairwise.
- Cited in 03_fine-tuning.md as the Synthetic GPT-J dataset for reward modeling.

**He et al. (2020)**
Pengcheng He, Xiaodong Liu, Jianfeng Gao, and Weizhu Chen. Deberta: Decoding-enhanced bert with disentangled attention. *arXiv preprint arXiv:2006.03654*, 2020.
- Cited in 03_fine-tuning.md as the architecture for Open Assistant reward model baseline.

**Hendrycks et al. (2020)**
Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn Xiaodong Song, and Jacob Steinhardt. Measuring massive multitask language understanding. *arXiv preprint arXiv:2009.03300*, 2020.
- Cited in 02_pretraining.md as the MMLU benchmark.

**Hendrycks et al. (2021)**
Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. Measuring mathematical problem solving with the math dataset. *arXiv preprint arXiv:2103.03874*, 2021.
- Cited in 02_pretraining.md as the MATH benchmark.

**Hoffmann et al. (2022)**
Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, et al. Training compute-optimal large language models. *arXiv preprint arXiv:2203.15556*, 2022.
- Cited in 01_introduction.md (Chinchilla as closed pretrained competitor) and 06_related-work.md (Chinchilla redefined scaling laws toward token count).

**Holtzman et al. (2020)**
Ari Holtzman, Jan Buys, Li Du, Maxwell Forbes, and Yejin Choi. The curious case of neural text degeneration. In *International Conference on Learning Representations*, 2020.
- Cited in 04_safety.md for nucleus sampling decoding strategy.

**Honovich et al. (2022)**
Or Honovich, Thomas Scialom, Omer Levy, and Timo Schick. Unnatural instructions: Tuning language models with (almost) no human labor. *arXiv preprint arXiv:2212.09689*, 2022.
- Cited in 06_related-work.md for training with synthetic instructions.

**Hosseini et al. (2023)**
Saghar Hosseini, Hamid Palangi, and Ahmed Hassan Awadallah. An empirical study of metrics to measure representational harms in pre-trained language models. *arXiv preprint arXiv:2301.09211*, 2023.
- Cited in 11_appendix-a4-safety.md for the revised version of ToxiGen dataset that reduces noise by filtering out prompts for which annotators disagree on the target demographic group.

**Huang et al. (2023)**
Fan Huang, Haewoon Kwak, and Jisun An. Is chatgpt better than human annotators? Potential and limitations of chatgpt in explaining implicit hate speech. *arXiv preprint arXiv:2302.07736*, 2023.
- Cited in 05_discussion.md for evidence that LLMs surpass human annotators.

**Hutto and Gilbert (2014)**
Clayton Hutto and Eric Gilbert. Vader: A parsimonious rule-based model for sentiment analysis of social media text. In *Proceedings of the international AAAI conference on web and social media*, volume 8, pages 216--225, 2014.
- Cited in 11_appendix-a4-safety.md for the VADER sentiment analyzer used to evaluate sentiment scores in BOLD benchmark analysis.

**Joshi et al. (2017)**
Mandar Joshi, Eunsol Choi, Daniel S Weld, and Luke Zettlemoyer. Triviaqa: A large scale distantly supervised challenge dataset for reading comprehension. *arXiv preprint arXiv:1705.03551*, 2017.
- Cited in 02_pretraining.md as the TriviaQA benchmark for world knowledge.

**Kaplan et al. (2020)**
Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jeffrey Wu, and Dario Amodei. Scaling laws for neural language models. *arXiv preprint arXiv:2001.08361*, 2020.
- Cited in 06_related-work.md for neural scaling laws.

**Kirkpatrick et al. (2017)**
James Kirkpatrick, Razvan Pascanu, Neil Rabinowitz, Joel Veness, Guillaume Desjardins, Andrei A Rusu, Kieran Milan, John Quan, Tiago Ramalho, Agnieszka Grabska-Barwinska, et al. Overcoming catastrophic forgetting in neural networks. *Proceedings of the national academy of sciences*, 114(13):3521--3526, 2017.
- Cited in 03_fine-tuning.md for catastrophic forgetting in iterative RLHF.

**Kopf et al. (2023)**
Andreas Kopf, Yannic Kilcher, Dimitri von Rutte, Sotiris Anagnostidis, Zhi-Rui Tam, Keith Stevens, Abdullah Barhoum, Nguyen Minh Duc, Oliver Stanley, Richard Nagyfi, et al. Openassistant conversations -- democratizing large language model alignment. *arXiv preprint arXiv:2304.07327*, 2023.
- Cited in 03_fine-tuning.md as the Open Assistant reward model baseline.

**Korbak et al. (2023)**
Tomasz Korbak, Kejian Shi, Angelica Chen, Rasika Bhalerao, Christopher L Buckley, Jason Phang, Samuel R Bowman, and Ethan Perez. Pretraining language models with human preferences. *arXiv preprint arXiv:2302.08582*, 2023.
- Cited in 04_safety.md for benefit of unfiltered pretraining data for downstream safety alignment.

**Kudo and Richardson (2018)**
Taku Kudo and John Richardson. Sentencepiece: A simple and language independent subword tokenizer and detokenizer for neural text processing, 2018.
- Cited in 02_pretraining.md for SentencePiece tokenizer implementation.

**Kumar et al. (2022)**
Sachin Kumar, Vidhisha Balachandran, Lucille Njoo, Antonios Anastasopoulos, and Yulia Tsvetkov. Language generation models can cause harm: So what can we do about it? An actionable survey. *arXiv preprint arXiv:2210.07700*, 2022.
- Cited in 06_related-work.md for potential mitigation strategies to curb harm from LLMs.

**Kwiatkowski et al. (2019)**
Tom Kwiatkowski, Jennimaria Palomaki, Olivia Redfield, Michael Collins, Ankur Parikh, Chris Alberti, Danielle Epstein, Illia Polosukhin, Jacob Devlin, Kenton Lee, et al. Natural questions: A benchmark for question answering research. *Transactions of the Association for Computational Linguistics*, 7:453--466, 2019.
- Cited in 02_pretraining.md as the NaturalQuestions benchmark for world knowledge.

**Lambert et al. (2023)**
Nathan Lambert, Lewis Tunstall, Nazneen Rajani, and Tristan Thrush. Huggingface h4 stack exchange preference dataset. 2023.
- Cited in 03_fine-tuning.md as the StackExchange dataset for reward modeling.

**Lee et al. (2022)**
Katherine Lee, Daphne Ippolito, Andrew Nystrom, Chiyuan Zhang, Douglas Eck, Chris Callison-Burch, and Nicholas Carlini. Deduplicating training data makes language models better. In *Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics*. Association for Computational Linguistics, 2022.
- Cited in 13_appendix-a6-dataset-contamination.md for the suffix array library used to implement 10(+)-skipgram detection.

**Lee and Sengupta (2022)**
Kevin Lee and Shubho Sengupta. Introducing the ai research supercluster -- meta's cutting-edge ai supercomputer for ai research, 2022.
- Cited in 02_pretraining.md for Meta's Research Super Cluster (RSC).

**Lin et al. (2021)**
Stephanie Lin, Jacob Hilton, and Owain Evans. Truthfulqa: Measuring how models mimic human falsehoods. *arXiv preprint arXiv:2109.07958*, 2021.
- Cited in 04_safety.md as the TruthfulQA benchmark for truthfulness.

**Liu et al. (2019)**
Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke Zettlemoyer, and Veselin Stoyanov. Roberta: A robustly optimized bert pretraining approach. *arXiv preprint arXiv:1907.11692*, 2019.
- Cited in 11_appendix-a4-safety.md for the RoBERTa-based ToxiGen classifier used to measure toxicity of model generations.

**Longpre et al. (2023)**
Shayne Longpre, Le Hou, Tu Vu, Albert Webson, Hyung Won Chung, Yi Tay, Denny Zhou, Quoc V Le, Barret Zoph, Jason Wei, et al. The flan collection: Designing data and methods for effective instruction tuning. *arXiv preprint arXiv:2301.13688*, 2023.
- Cited in 06_related-work.md for investigating instruction tuning as a function of tasks, model size, etc.

**Loshchilov and Hutter (2017)**
Ilya Loshchilov and Frank Hutter. Decoupled weight decay regularization. *arXiv preprint arXiv:1711.05101*, 2017.
- Cited in 02_pretraining.md and 03_fine-tuning.md for AdamW optimizer.

**Madaan et al. (2023)**
Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, et al. Self-refine: Iterative refinement with self-feedback. *arXiv preprint arXiv:2303.17651*, 2023.
- Cited in 06_related-work.md for using follow-up instructions to refine generations.

**Mialon et al. (2023)**
Gregoire Mialon, Roberto Dessi, Maria Lomeli, Christoforos Nalmpantis, Ram Pasunuru, Roberta Raileanu, Baptiste Roziere, Timo Schick, Jane Dwivedi-Yu, Asli Celikyilmaz, et al. Augmented language models: A survey. *arXiv preprint arXiv:2302.07842*, 2023.
- Cited in 05_discussion.md (tool integration research) and 06_related-work.md (advanced emergent model behaviors).

**Mihaylov et al. (2018)**
Todor Mihaylov, Peter Clark, Tushar Khot, and Ashish Sabharwal. Can a suit of armor conduct electricity? A new dataset for open book question answering. *arXiv preprint arXiv:1809.02789*, 2018.
- Cited in 02_pretraining.md as the OpenBookQA benchmark for commonsense reasoning.

**Mitchell et al. (2018)**
Margaret Mitchell, Simone Wu, Andrew Zaldivar, Parker Barnes, Lucy Vasserman, Ben Hutchinson, Elena Spitzer, Inioluwa Deborah Raji, and Timnit Gebru. Model cards for model reporting. *CoRR*, abs/1810.03993, 2018.
- Cited in 14_appendix-a7-model-card.md as the originator of the model card framework.

**MosaicML NLP Team et al. (2023)**
MosaicML NLP Team et al. Introducing mpt-7b: A new standard for open-source, commercially usable llms, 2023.
- Cited in 02_pretraining.md, 03_fine-tuning.md, and 04_safety.md as MPT baseline.

**Nakano et al. (2021)**
Reiichiro Nakano, Jacob Hilton, Suchir Balaji, Jeff Wu, Lonbrown Ouyanbrown, Christina Kim, Christopher Hesse, Shantanu Jain, Vineet Kosaraju, William Saunders, et al. Webgpt: Browser-assisted question-answering with human feedback. In *arXiv*, 2021.
- Cited in 03_fine-tuning.md as the OpenAI WebGPT dataset for reward modeling.

**Nguyen et al. (2019)**
Cuong V. Nguyen, Alessandro Achille, Michael Lam, Tal Hassner, Vijay Mahadevan, and Stefano Soatto. Toward understanding catastrophic forgetting in continual learning. *arXiv preprint arXiv:1908.01091*, 2019.
- Cited in 03_fine-tuning.md for catastrophic forgetting research.

**OpenAI (2023)**
OpenAI. GPT-4 technical report. *CoRR*, abs/2303.08774, 2023.
- Cited in 02_pretraining.md (Table 4, GPT-3.5 and GPT-4 results), 03_fine-tuning.md (ChatGPT baseline), and 04_safety.md (borderline test set design).

**Ouyang et al. (2022)**
Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al. Training language models to follow instructions with human feedback. *Advances in Neural Information Processing Systems*, 35:27730--27744, 2022.
- Cited in 03_fine-tuning.md (binary ranking loss for reward model) and 06_related-work.md (instruction fine-tuning + RLHF).

**Patterson et al. (2021)**
David Patterson, Joseph Gonzalez, Quoc Le, Chen Liang, Lluis-Miquel Munguia, Daniel Rothchild, David So, Maud Texier, and Jeff Dean. Carbon emissions and large neural network training. *arXiv preprint arXiv:2104.10350*, 2021.
- Cited in 02_pretraining.md for carbon footprint of pretraining.

**Penedo et al. (2023)**
Guilherme Penedo, Quentin Malartic, Daniel Hesslow, Ruxandra Cojocaru, Alessandro Cappelli, Hamza Alobeidli, Baptiste Pannier, Ebtesam Almazrouei, and Julien Launay. The refinedweb dataset for falcon llm: Outperforming curated corpora with web data, and web data only, 2023.
- Cited in 01_introduction.md and 06_related-work.md as the Falcon pretraining data/model.

**Rae et al. (2022)**
Jack W. Rae, Sebastian Borgeaud, Trevor Cai, Katie Millican, Jordan Hoffmann, Francis Song, et al. Scaling language models: Methods, analysis & insights from training gopher, 2022.
- Cited in 06_related-work.md as Gopher, a >100B parameter LLM.

**Rajpurkar et al. (2018)**
Pranav Rajpurkar, Robin Jia, and Percy Liang. Know what you don't know: Unanswerable questions for squad. *arXiv preprint arXiv:1806.03822*, 2018.
- Cited in 02_pretraining.md as the SQuAD benchmark for reading comprehension.

**Ramasesh et al. (2021)**
Vinay Venkatesh Ramasesh, Aitor Lewkowycz, and Ethan Dyer. Effect of scale on catastrophic forgetting in neural networks. In *International Conference on Learning Representations*, 2021.
- Cited in 03_fine-tuning.md for catastrophic forgetting research.

**Roller et al. (2020)**
Stephen Roller, Y-Lan Boureau, Jason Weston, Antoine Bordes, Emily Dinan, Angela Fan, David Gunning, Da Ju, Margaret Li, Spencer Poff, et al. Open-domain conversational agents: Current progress, open problems, and future directions. *arXiv preprint arXiv:2006.12442*, 2020.
- Cited in 06_related-work.md for difficulties tied to chatbot-oriented LLMs.

**Sakaguchi et al. (2021)**
Keisuke Sakaguchi, Ronan Le Bras, Chandra Bhagavatula, and Yejin Choi. Winogrande: An adversarial winograd schema challenge at scale. *Communications of the ACM*, 64(9):99--106, 2021.
- Cited in 02_pretraining.md as the WinoGrande benchmark for commonsense reasoning.

**Sap et al. (2019)**
Maarten Sap, Hannah Rashkin, Derek Chen, Ronan LeBras, and Yejin Choi. Socialiqa: Commonsense reasoning about social interactions. *arXiv preprint arXiv:1904.09728*, 2019.
- Cited in 02_pretraining.md as the SIQA benchmark for commonsense reasoning.

**Scao et al. (2022)**
Teven Le Scao, Angela Fan, Christopher Akiki, Ellie Pavlick, Suzana Ilic, Daniel Hesslow, Roman Castagne, Alexandra Sasha Luccioni, Francois Yvon, Matthias Galle, et al. Bloom: A 176b-parameter open-access multilingual language model. *arXiv preprint arXiv:2211.05100*, 2022.
- Cited in 01_introduction.md and 06_related-work.md as BLOOM, an open-source LLM.

**Schick et al. (2023)**
Timo Schick, Jane Dwivedi-Yu, Roberto Dessi, Roberta Raileanu, Maria Lomeli, Luke Zettlemoyer, Nicola Cancedda, and Thomas Scialom. Toolformer: Language models can teach themselves to use tools. *arXiv preprint arXiv:2302.04761*, 2023.
- Cited in 05_discussion.md for Toolformer approach to LLM tool use (Table 15 baselines).

**Schulman et al. (2017)**
John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. *arXiv preprint arXiv:1707.06347*, 2017.
- Cited in 03_fine-tuning.md for PPO algorithm used in RLHF.

**Scialom et al. (2020a)**
Thomas Scialom, Paul-Alexis Dray, Sylvain Lamprier, Benjamin Piwowarski, and Jacopo Staiano. Discriminative adversarial search for abstractive summarization. In *Proceedings of the 37th International Conference on Machine Learning*, volume 119, pages 8555--8564. PMLR, 2020a.
- Cited in 03_fine-tuning.md for fine-tuning on ranked samples to reinforce reward.

**Scialom et al. (2020b)**
Thomas Scialom, Paul-Alexis Dray, Sylvain Lamprier, Benjamin Piwowarski, and Jacopo Staiano. Coldgans: Taming language gans with cautious sampling strategies. *Advances in Neural Information Processing Systems*, 33:18978--18989, 2020b.
- Cited in 03_fine-tuning.md for hyper-specialization risk requiring on-distribution reward model data.

**Sennrich et al. (2016)**
Rico Sennrich, Barry Haddow, and Alexandra Birch. Neural machine translation of rare words with subword units, 2016.
- Cited in 02_pretraining.md for BPE tokenization algorithm.

**Shazeer (2020)**
Noam Shazeer. Glu variants improve transformer, 2020.
- Cited in 02_pretraining.md for SwiGLU activation function.

**Shumailov et al. (2023)**
Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Yarin Gal, Nicolas Papernot, and Ross Anderson. The curse of recursion: Training on generated data makes models forget. *arXiv preprint arxiv:2305.17493*, 2023.
- Cited in 06_related-work.md for training data degradation from over-reliance on LLMs.

**Smith and Williams (2021)**
Eric Michael Smith and Adina Williams. Hi, my name is martha: Using names to measure and mitigate bias in generative dialogue models. *arXiv preprint arXiv:2109.03300*, 2021.
- Cited in 04_safety.md for ongoing empirical work on dataset size and bias.

**Smith et al. (2022)**
Eric Michael Smith, Melissa Hall, Melanie Kambadur, Eleonora Presani, and Adina Williams. "I'm sorry to hear that": Finding new biases in language models with a holistic descriptor dataset. In *2022 Conference on Empirical Methods in Natural Language Processing*, pages 9180--9211, 2022.
- Cited in 04_safety.md for HolisticBias dataset used to measure demographic identity representation.

**Solaiman et al. (2023)**
Irene Solaiman, Zeerak Talat, William Agnew, Lama Ahmad, Dylan Baker, Su Lin Blodgett, Hal Daume III, Jesse Dodge, Ellie Evans, Sara Hooker, et al. Evaluating the social impact of generative ai systems in systems and society. *arXiv preprint arXiv:2306.05949*, 2023.
- Cited in 01_introduction.md (potential risks) and 06_related-work.md (categorizing LLM impacts into base system vs. societal context).

**Stiennon et al. (2020)**
Nisan Stiennon, Long Ouyang, Jeff Wu, Daniel M. Ziegler, Ryan Lowe, Chelsea Voss, Alec Radford, Dario Amodei, and Paul Christiano. Learning to summarize from human feedback. In *NeurIPS*, 2020.
- Cited in 03_fine-tuning.md (OpenAI Summarize dataset; PPO RL scheme; KL penalty) and 06_related-work.md (RLHF first showcased for text summarization).

**Su et al. (2022)**
Jianlin Su, Yu Lu, Shengfeng Pan, Ahmed Murtadha, Bo Wen, and Yunfeng Liu. Roformer: Enhanced transformer with rotary position embedding, 2022.
- Cited in 02_pretraining.md for Rotary Positional Embeddings (RoPE).

**Suzgun et al. (2022)**
Mirac Suzgun, Nathan Scales, Nathanael Scharli, Sebastian Gehrmann, Yi Tay, Hyung Won Chung, Aakanksha Chowdhery, Quoc V Le, Ed H Chi, Denny Zhou, et al. Challenging big-bench tasks and whether chain-of-thought can solve them. *arXiv preprint arXiv:2210.09261*, 2022.
- Cited in 02_pretraining.md as the Big Bench Hard (BBH) benchmark.

**Synnaeve et al. (2019)**
Gabriel Synnaeve, Jonas Gehring, Zeming Lin, Daniel Haziza, Nicolas Usunier, Danielle Rothermel, Vegard Mella, Da Ju, Nicolas Carion, Laura Gustafson, et al. Growing up together: Structured exploration for large action spaces. 2019.
- Cited in 03_fine-tuning.md for analogous approach in RL literature to incorporating prior iteration samples.

**Tal et al. (2022)**
Yarden Tal, Inbal Magar, and Roy Schwartz. Fewer errors, but more stereotypes? The effect of model size on gender bias. In *Proceedings of the 4th Workshop on Gender Bias in Natural Language Processing (GeBNLP)*, pages 112--120, 2022.
- Cited in 04_safety.md for ongoing empirical work on model size and bias.

**Talmor et al. (2018)**
Alon Talmor, Jonathan Herzig, Nicholas Lourie, and Jonathan Berant. Commonsenseqa: A question answering challenge targeting commonsense knowledge. *arXiv preprint arXiv:1811.00937*, 2018.
- Cited in 02_pretraining.md as the CommonsenseQA benchmark.

**Taori et al. (2023)**
Rohan Taori, Ishaan Gulrajani, Tianyi Zhang, Yann Dubois, Xuechen Li, Carlos Guestrin, Percy Liang, and Tatsunori B. Hashimoto. Stanford alpaca: An instruction-following llama model. https://github.com/tatsu-lab/stanford_alpaca, 2023.
- Cited in 06_related-work.md as Alpaca, a distillation-based model.

**Taylor et al. (2022)**
Ross Taylor, Marcin Kardas, Guillem Cucurull, Thomas Scialom, Anthony Hartshorn, Elvis Saravia, Andrew Poulton, Viktor Kerkez, and Robert Stojnic. Galactica: A large language model for science. *arXiv preprint arXiv:2211.09085*, 2022.
- Cited in 06_related-work.md as Galactica, a specialized LLM for science.

**Touvron et al. (2023)**
Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothee Lacroix, Baptiste Roziere, Naman Goyal, Eric Hambro, Faisal Azhar, et al. Llama: Open and efficient foundation language models. *arXiv preprint arXiv:2302.13971*, 2023.
- Cited in 01_introduction.md (LLaMA-1 release), 02_pretraining.md (prior pretraining approach), 03_fine-tuning.md (SFT bootstrapping), 04_safety.md (comparison baseline), and 06_related-work.md (Llama 1 for computational efficiency).

**Vaswani et al. (2017)**
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and Illia Polosukhin. Attention is all you need, 2017.
- Cited in 02_pretraining.md for standard transformer architecture.

**Vinyals et al. (2019)**
Oriol Vinyals, Igor Babuschkin, Wojciech M Czarnecki, Michael Mathieu, Andrew Dudzik, Junyoung Chung, David H Choi, Richard Powell, Timo Ewalds, Petko Georgiev, et al. Grandmaster level in starcraft ii using multi-agent reinforcement learning. *Nature*, 575(7782):350--354, 2019.
- Cited in 03_fine-tuning.md for analogous approach in RL literature to incorporating prior iteration samples.

**Wang et al. (2022)**
Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Alisa Liu, Noah A Smith, Daniel Khashabi, and Hannaneh Hajishirzi. Self-instruct: Aligning language model with self generated instructions. *arXiv preprint arXiv:2212.10560*, 2022.
- Cited in 06_related-work.md for training with synthetic instructions.

**Webb (2019)**
Michael Webb. The impact of artificial intelligence on the labor market. *Available at SSRN 3482150*, 2019.
- Cited in 06_related-work.md as a broader societal concern (job displacement).

**Wei et al. (2021)**
Jason Wei, Maarten Bosma, Vincent Zhao, Kelvin Guu, Adams Wei Yu, Brian Lester, Nan Du, Andrew M Dai, and Quoc V Le. Finetuned language models are zero-shot learners. In *International Conference on Learning Representations*, 2021.
- Cited in 06_related-work.md for obtaining zero-shot performance via fine-tuning on numerous datasets.

**Wei et al. (2022a)**
Jason Wei, Maarten Bosma, Vincent Zhao, Kelvin Guu, Adams Wei Yu, Brian Lester, Nan Du, Andrew M. Dai, and Quoc V Le. Finetuned language models are zero-shot learners. In *International Conference on Learning Representations*, 2022a.
- Cited in 13_appendix-a6-dataset-contamination.md as prior work on measuring dataset contamination.

**Wei et al. (2022b)**
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, et al. Chain-of-thought prompting elicits reasoning in large language models. *Advances in Neural Information Processing Systems*, 35:24824--24837, 2022b.
- Cited in 06_related-work.md for chain-of-thought prompting.

**Weidinger et al. (2021)**
Laura Weidinger, John Mellor, Maribeth Rauh, Conor Griffin, Jonathan Uesato, Po-Sen Huang, Myra Cheng, Mia Glaese, Borja Balle, Atoosa Kasirzadeh, et al. Ethical and social risks of harm from language models. *arXiv preprint arXiv:2112.04359*, 2021.
- Cited in 01_introduction.md (potential risks) and 06_related-work.md (hazards of LLMs).

**Welbl et al. (2021)**
Johannes Welbl, Amelia Glaese, Jonathan Uesato, Sumanth Dathathri, John Mellor, Lisa Anne Hendricks, Kirsty Anderson, Pushmeet Kohli, Ben Coppin, and Po-Sen Huang. Challenges in detoxifying language models, 2021.
- Cited in 04_safety.md for benefit of unfiltered pretraining data for downstream generalization.

**Wu et al. (2022)**
Carole-Jean Wu, Ramya Raghavendra, Udit Gupta, Bilge Acun, Newsha Ardalani, Kiwan Maeng, Gloria Chang, Fiona Aga, Jinshi Huang, Charles Bai, et al. Sustainable ai: Environmental implications, challenges and opportunities. *Proceedings of Machine Learning and Systems*, 4:795--813, 2022.
- Cited in 02_pretraining.md for carbon footprint of pretraining.

**Xu et al. (2021)**
Jing Xu, Da Ju, Margaret Li, Y-Lan Boureau, Jason Weston, and Emily Dinan. Recipes for safety in open-domain chatbots, 2021.
- Cited in 04_safety.md for benefit of unfiltered pretraining data for downstream safety alignment.

**Zellers et al. (2019a)**
Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali Farhadi, and Yejin Choi. Hellaswag: Can a machine really finish your sentence? *arXiv preprint arXiv:1905.07830*, 2019a.
- Cited in 02_pretraining.md as the HellaSwag benchmark for commonsense reasoning.

**Zellers et al. (2019b)**
Rowan Zellers, Ari Holtzman, Hannah Rashkin, Yonatan Bisk, Ali Farhadi, Franziska Roesner, and Yejin Choi. Defending against neural fake news. *Advances in neural information processing systems*, 32, 2019b.
- Cited in 05_discussion.md for argument that open releases promote transparency and democratize AI.

**Zhang and Sennrich (2019)**
Biao Zhang and Rico Sennrich. Root mean square layer normalization, 2019.
- Cited in 02_pretraining.md for RMSNorm pre-normalization.

**Zhang et al. (2022)**
Susan Zhang, Stephen Roller, Naman Goyal, Mikel Artetxe, Moya Chen, Shuohui Chen, Mona Diab, Xian Li, Xi Victoria Lin, et al. Opt: Open pre-trained transformer language models. *arXiv preprint arXiv:2205.01068*, 2022.
- Cited in 06_related-work.md as OPT, an open-source LLM.

**Zhao et al. (2023)**
Yanli Zhao, Andrew Gu, Rohan Varma, Liang Luo, Chien-Chin Huang, Min Xu, Less Wright, Hamid Shojanazeri, Myle Ott, Sam Shleifer, et al. Pytorch fsdp: Experiences on scaling fully sharded data parallel, 2023.
- Cited in 03_fine-tuning.md for FSDP used during PPO training.

**Zhong et al. (2023)**
Wanjun Zhong, Ruixiang Cui, Yiduo Guo, Yaobo Liang, Shuai Lu, Yanlin Wang, Amin Saied, Weizhu Chen, and Nan Duan. Agieval: A human-centric benchmark for evaluating foundation models. *arXiv preprint arXiv:2304.06364*, 2023.
- Cited in 02_pretraining.md as the AGI Eval benchmark.

**Zhou et al. (2022)**
Yongchao Zhou, Andrei Ioan Muresanu, Ziwen Han, Keiran Paster, Silviu Pitis, Harris Chan, and Jimmy Ba. Large language models are human-level prompt engineers. In *The Eleventh International Conference on Learning Representations*, 2022.
- Cited in 06_related-work.md for prompts created by LLMs themselves for instruction tuning.

**Zhou et al. (2023)**
Chunting Zhou, Pengfei Liu, Puxin Xu, Srini Iyer, Jiao Sun, Yuning Mao, Xuezhe Ma, Avia Efrat, Ping Yu, Lili Yu, Susan Zhang, Gargi Ghosh, Mike Lewis, Luke Zettlemoyer, and Omer Levy. Lima: Less is more for alignment. *arXiv preprint arXiv:2305.11206*, 2023.
- Cited in 03_fine-tuning.md for finding that a limited set of clean instruction-tuning data can suffice.

**Zhuo et al. (2023)**
Terry Yue Zhuo, Yujin Huang, Chunyang Chen, and Zhenchang Xing. Exploring ai ethics of chatgpt: A diagnostic analysis. *arXiv preprint arXiv:2301.12867*, 2023.
- Cited in 06_related-work.md for red teaming showcasing successful attack types.
