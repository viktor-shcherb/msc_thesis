# References

Only references substantively cited in the section notes are included.
The broad range citation [1-34] in the introduction is omitted except for
entries that are also cited individually elsewhere.

## [1]
Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D. Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. Language models are few-shot learners. *Advances in Neural Information Processing Systems*, 33:1877-1901, 2020.
- Cited in 01_introduction.md as an earlier GPT model with similar limitations; cited in 04_capabilities.md for few-shot prompting methodology.

## [2]
Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, et al. Training compute-optimal large language models. *arXiv preprint arXiv:2203.15556*, 2022.
- Cited in 03_predictable-scaling.md as prior work on scaling laws; cited in 04_capabilities.md as a baseline (Chinchilla) for multilingual MMLU comparison.

## [3]
Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung, Charles Sutton, Sebastian Gehrmann, et al. PaLM: Scaling language modeling with pathways. *arXiv preprint arXiv:2204.02311*, 2022.
- Cited in 04_capabilities.md as a baseline (PaLM) for MMLU multilingual comparison and as LM SOTA on WinoGrande, HumanEval, and DROP benchmarks.

## [4]
Jack W Rae, Sebastian Borgeaud, Trevor Cai, Katie Millican, Jordan Hoffmann, Francis Song, John Aslanides, Sarah Henderson, Roman Ring, Susannah Young, et al. Scaling language models: Methods, analysis & insights from training gopher. *arXiv preprint arXiv:2112.11446*, 2021.
- Cited in 14_appendix-f-multilingual-mmlu.md as the source of the MMLU prompt format used for multilingual evaluation.

## [11]
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Ed Chi, Quoc Le, and Denny Zhou. Chain-of-thought prompting elicits reasoning in large language models. *NeurIPS*, 2022.
- Cited in 04_capabilities.md for chain-of-thought prompting used in GSM-8K evaluation.

## [14]
Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B. Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jeffrey Wu, and Dario Amodei. Scaling laws for neural language models. *arXiv preprint arXiv:2001.08361*, 2020.
- Cited in 03_predictable-scaling.md as prior work establishing that LLM loss follows power laws in compute.

## [15]
Tom Henighan, Jared Kaplan, Mor Katz, Mark Chen, Christopher Hesse, Jacob Jackson, Heewoo Jun, Tom B. Brown, Prafulla Dhariwal, Scott Gray, et al. Scaling laws for autoregressive generative modeling. *arXiv preprint arXiv:2010.14701*, 2020.
- Cited in 03_predictable-scaling.md for the scaling law formulation with irreducible loss term used to predict GPT-4's final loss.

## [18]
Barret Zoph, Irwan Bello, Sameer Kumar, Nan Du, Yanping Huang, Jeff Dean, Noam Shazeer, and William Fedus. ST-MoE: Designing stable and transferable sparse expert models. *arXiv preprint arXiv:2202.08906*, 2022.
- Cited in 04_capabilities.md as SOTA on ARC benchmark (86.5%).

## [28]
Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothee Lacroix, Baptiste Roziere, Naman Goyal, Eric Hambro, Faisal Azhar, et al. LLaMA: Open and efficient foundation language models. *arXiv preprint arXiv:2302.13971*, 2023.
- Cited in 04_capabilities.md as LM SOTA on HellaSwag (84.2%, validation set).

## [35]
Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn Song, and Jacob Steinhardt. Measuring massive multitask language understanding. *Proceedings of the International Conference on Learning Representations (ICLR)*, 2021.
- Cited in 01_introduction.md and 04_capabilities.md for the MMLU benchmark.

## [36]
Dan Hendrycks, Collin Burns, Steven Basart, Andrew Critch, Jerry Li, Dawn Song, and Jacob Steinhardt. Aligning AI with shared human values. *Proceedings of the International Conference on Learning Representations (ICLR)*, 2021.
- Cited in 01_introduction.md and 04_capabilities.md for the MMLU benchmark (co-reference with [35]).

## [37]
Alec Radford, Jeff Wu, Rewon Child, David Luan, Dario Amodei, and Ilya Sutskever. Language models are unsupervised multitask learners. 2019.
- Cited in 01_introduction.md as an earlier GPT model with similar limitations to GPT-4.

## [38]
Alec Radford, Karthik Narasimhan, Tim Salimans, and Ilya Sutskever. Improving language understanding by generative pre-training. 2018.
- Cited in 01_introduction.md as an earlier GPT model with similar limitations to GPT-4.

## [39]
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Lukasz Kaiser, and Illia Polosukhin. Attention is all you need. *NeurIPS*, 2017.
- Cited in 02_scope-and-limitations.md identifying GPT-4 as a Transformer-style model.

## [40]
Paul F Christiano, Jan Leike, Tom Brown, Miljan Martic, Shane Legg, and Dario Amodei. Deep reinforcement learning from human preferences. *Advances in Neural Information Processing Systems*, 30, 2017.
- Cited in 02_scope-and-limitations.md and 06_risks-and-mitigations.md for RLHF fine-tuning.

## [41]
Joel Hestness, Sharan Narang, Newsha Ardalani, Gregory Diamos, Heewoo Jun, Hassan Kianinejad, Md Patwary, Mostofa Ali, Yang Yang, and Yanqi Zhou. Deep learning scaling is predictable, empirically. *arXiv preprint arXiv:1712.00409*, 2017.
- Cited in 03_predictable-scaling.md as prior work on power law scaling of LLM loss.

## [42]
Neil C Thompson, Kristjan Greenewald, Keeheon Lee, and Gabriel F Manso. The computational limits of deep learning. *arXiv preprint arXiv:2007.05558*, 2020.
- Cited in 03_predictable-scaling.md as prior work on power law scaling of LLM loss.

## [43]
Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde de Oliveira Pinto, Jared Kaplan, Harri Edwards, Yuri Burda, Nicholas Joseph, Greg Brockman, et al. Evaluating large language models trained on code. 2021.
- Cited in 03_predictable-scaling.md for the HumanEval dataset used to demonstrate capability scaling; cited in 04_capabilities.md for the HumanEval benchmark results.

## [44]
Ian McKenzie, Alexander Lyzhov, Alicia Parrish, Ameya Prabhu, Aaron Mueller, Najoung Kim, Sam Bowman, and Ethan Perez. The Inverse Scaling Prize, 2022. URL https://github.com/inverse-scaling/prize.
- Cited in 03_predictable-scaling.md for tasks where model performance decreases with scale.

## [45]
Jason Wei, Najoung Kim, Yi Tay, and Quoc V. Le. Inverse scaling can become U-shaped. *arXiv preprint arXiv:2211.02011*, 2022.
- Cited in 03_predictable-scaling.md as a recent result finding that inverse scaling trends can reverse at sufficient scale; GPT-4 is shown to exhibit this reversal.

## [46]
Ian McKenzie, Alexander Lyzhov, Alicia Parrish, Ameya Prabhu, Aaron Mueller, Najoung Kim, Sam Bowman, and Ethan Perez. Inverse Scaling Prize: First round winners, 2022. URL https://irmckenzie.co.uk/round1.
- Cited in 03_predictable-scaling.md for the Hindsight Neglect task shown in Figure 3.

## [47]
Greg Brockman, Peter Welinder, Mira Murati, and OpenAI. OpenAI: OpenAI API, 2020. URL https://openai.com/blog/openai-api.
- Cited in 03_predictable-scaling.md for model names (ada, babbage, curie); cited in 04_capabilities.md for user prompt collection.

## [48]
Aarohi Srivastava, Abhinav Rastogi, Abhishek Rao, Abu Awal Md Shoeb, Abubakar Abid, Adam Fisch, Adam R. Brown, Adam Santoro, Aditya Gupta, Adria Garriga-Alonso, et al. Beyond the imitation game: Quantifying and extrapolating the capabilities of language models. *arXiv preprint arXiv:2206.04615*, 2022.
- Cited in 04_capabilities.md noting that portions of BIG-bench were inadvertently mixed into the training set and excluded from results.

## [49]
Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn Song, and Jacob Steinhardt. Measuring massive multitask language understanding. *arXiv preprint arXiv:2009.03300*, 2020.
- Cited in 04_capabilities.md as the MMLU benchmark in Table 2.

## [50]
Yi Tay, Jason Wei, Hyung Won Chung, Vinh Q Tran, David R So, Siamak Shakeri, Xavier Garcia, Huaixiu Steven Zheng, Jinfeng Rao, Aakanksha Chowdhery, et al. Transcending scaling laws with 0.1% extra compute. *arXiv preprint arXiv:2210.11399*, 2022.
- Cited in 04_capabilities.md as LM SOTA on MMLU (70.7%, 5-shot U-PaLM).

## [51]
Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang, Mostafa Dehghani, Siddhartha Brahma, et al. Scaling instruction-finetuned language models. *arXiv preprint arXiv:2210.11416*, 2022.
- Cited in 04_capabilities.md as SOTA on MMLU (75.2%, 5-shot Flan-PaLM).

## [52]
Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali Farhadi, and Yejin Choi. HellaSwag: Can a machine really finish your sentence? In *Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics*, pages 4791-4800, Florence, Italy, July 2019. Association for Computational Linguistics.
- Cited in 04_capabilities.md for the HellaSwag benchmark in Table 2.

## [53]
Xiaodong Liu, Hao Cheng, Pengcheng He, Weizhu Chen, Yu Wang, Hoifung Poon, and Jianfeng Gao. Adversarial training for large neural language models. *arXiv preprint arXiv:2004.08994*, 2020.
- Cited in 04_capabilities.md as SOTA on HellaSwag (85.6, ALUM).

## [54]
Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar Khot, Ashish Sabharwal, Carissa Schoenick, and Oyvind Tafjord. Think you have solved question answering? Try ARC, the AI2 reasoning challenge. *ArXiv*, abs/1803.05457, 2018.
- Cited in 04_capabilities.md for the ARC benchmark in Table 2.

## [55]
Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, and Denny Zhou. Self-consistency improves chain of thought reasoning in language models. *arXiv preprint arXiv:2203.11171*, 2022.
- Cited in 04_capabilities.md as LM SOTA on ARC (85.2%, 8-shot PaLM).

## [56]
Keisuke Sakaguchi, Ronan Le Bras, Chandra Bhagavatula, and Yejin Choi. WinoGrande: An adversarial Winograd schema challenge at scale. *arXiv preprint arXiv:1907.10641*, 2019.
- Cited in 04_capabilities.md for the WinoGrande benchmark in Table 2.

## [57]
Bei Chen, Fengji Zhang, Anh Nguyen, Daoguang Zan, Zeqi Lin, Jian-Guang Lou, and Weizhu Chen. CodeT: Code generation with generated tests. *arXiv preprint arXiv:2207.10397*, 2022.
- Cited in 04_capabilities.md as SOTA on HumanEval (65.8%, CodeT + GPT-3.5).

## [58]
Dheeru Dua, Yizhong Wang, Pradeep Dasigi, Gabriel Stanovsky, Sameer Singh, and Matt Gardner. DROP: A reading comprehension benchmark requiring discrete reasoning over paragraphs. In *Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies*, pages 2368-2378, 2019.
- Cited in 04_capabilities.md for the DROP benchmark in Table 2 (only benchmark where GPT-4 does not beat SOTA).

## [59]
Kunlong Chen, Weidi Xu, Xingyi Cheng, Zou Xiaochuan, Yuyu Zhang, Le Song, Taifeng Wang, Yuan Qi, and Wei Chu. Question directed graph attention network for numerical reasoning over text. *arXiv preprint arXiv:2009.07448*, 2020.
- Cited in 04_capabilities.md as SOTA on DROP (88.4, QDGAT), outperforming GPT-4.

## [60]
Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, Christopher Hesse, and John Schulman. Training verifiers to solve math word problems. *arXiv preprint arXiv:2110.14168*, 2021.
- Cited in 04_capabilities.md for the GSM-8K benchmark in Table 2.

## [61]
Aitor Lewkowycz, Anders Andreassen, David Dohan, Ethan Dyer, Henryk Michalewski, Vinay Ramasesh, Ambrose Slone, Cem Anil, Imanol Schlag, Theo Gutman-Solo, et al. Solving quantitative reasoning problems with language models. *arXiv preprint arXiv:2206.14858*, 2022.
- Cited in 04_capabilities.md as LM SOTA on GSM-8K (58.8%, 8-shot Minerva).

## [62]
Jonathan Uesato, Nate Kushman, Ramana Kumar, Francis Song, Noah Siegel, Lisa Wang, Antonia Creswell, Geoffrey Irving, and Irina Higgins. Solving math word problems with process- and outcome-based feedback. *arXiv preprint arXiv:2211.14275*, 2022.
- Cited in 04_capabilities.md as SOTA on GSM-8K (87.3%, Chinchilla + SFT+ORM-RL, ORM reranking).

## [63]
Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al. Training language models to follow instructions with human feedback. *arXiv preprint arXiv:2203.02155*, 2022.
- Cited in 04_capabilities.md for GPT-4's improved ability to follow user intent; cited in 06_risks-and-mitigations.md for RLHF fine-tuning.

## [64]
OpenAI. OpenAI: Introducing ChatGPT, 2022. URL https://openai.com/blog/chatgpt.
- Cited in 04_capabilities.md for user prompt collection from ChatGPT; cited in 05_limitations.md as earlier versions of ChatGPT based on GPT-3.5.

## [65]
OpenAI. OpenAI: GPT-4, 2023. URL https://openai.com/research/gpt-4.
- Cited in 04_capabilities.md for preliminary visual capability benchmark results.

## [66]
Stephanie Lin, Jacob Hilton, and Owain Evans. TruthfulQA: Measuring how models mimic human falsehoods. In *Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 3214-3252, Dublin, Ireland, May 2022. Association for Computational Linguistics.
- Cited in 05_limitations.md for the TruthfulQA benchmark testing factuality.

## [67]
Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort, Deep Ganguli, Tom Henighan, et al. Training a helpful and harmless assistant with reinforcement learning from human feedback. *arXiv preprint arXiv:2204.05862*, 2022.
- Cited in 05_limitations.md as a comparison point (Anthropic-LM) on TruthfulQA.

## [68]
OpenAI. OpenAI: How should AI systems behave, and who should decide?, 2023. URL https://openai.com/blog/how-should-ai-systems-behave.
- Cited in 05_limitations.md regarding efforts to correct biases and get public input on default behaviors.

## [69]
Jan Leike, John Schulman, and Jeffrey Wu. OpenAI: Our approach to alignment research, 2022. URL https://openai.com/blog/our-approach-to-alignment-research.
- Cited in 06_risks-and-mitigations.md for the model-assisted safety pipeline.

## [70]
Joseph Carlsmith. Is power-seeking AI an existential risk? *ArXiv*, abs/2206.13353, 2022.
- Cited in 06_risks-and-mitigations.md for assessment of risks such as power seeking relevant to very advanced AIs.

## [71]
Amelia Glaese, Nat McAleese, Maja Trebacz, John Aslanides, Vlad Firoiu, Timo Ewalds, Maribeth Rauh, Laura Weidinger, Martin Chadwick, Phoebe Thacker, et al. Improving alignment of dialogue agents via targeted human judgements. *arXiv preprint arXiv:2209.14375*, 2022.
- Cited in 06_risks-and-mitigations.md as related work on rule-based reward models for steering model behavior.

## [72]
Ethan Perez, Saffron Huang, H. Francis Song, Trevor Cai, Roman Ring, John Aslanides, Amelia Glaese, Nat McAleese, and Geoffrey Irving. Red teaming language models with language models. *arXiv preprint arXiv:2202.03286*, 2022.
- Cited in 06_risks-and-mitigations.md as related work on rule-based reward models for steering model behavior.

## [73]
Samuel Gehman, Suchin Gururangan, Maarten Sap, Yejin Choi, and Noah A Smith. RealToxicityPrompts: Evaluating neural toxic degeneration in language models. *arXiv preprint arXiv:2009.11462*, 2020.
- Cited in 06_risks-and-mitigations.md for the RealToxicityPrompts dataset on which GPT-4 produces toxic generations only 0.73% of the time vs. GPT-3.5 at 6.48%.

## [74]
Dora Seigel. How do you calculate your SAT score? raw and scaled, 1 2020. URL https://blog.prepscholar.com/how-to-calculate-sat-score.
- Cited in 09_appendix-a-exam-benchmark-methodology.md for converting SAT multiple-choice scores into scaled scores.

## [75]
The Albert blog. URL https://www.albert.io/blog/.
- Cited in 09_appendix-a-exam-benchmark-methodology.md for the AP exam score calculators based on 2019-2020 scoring guidelines.

## [76]
Mathematical Association of America. AMC statistics, 2023. URL http://amc-reg.maa.org/Reports/GeneralReports.aspx.
- Cited in 09_appendix-a-exam-benchmark-methodology.md for AMC 10 and AMC 12 score distributions used to estimate percentile ranges.

## [77]
Halle Edwards. SAT percentiles and score rankings, 2022. URL https://blog.prepscholar.com/sat-percentiles-and-score-rankings.
- Cited in 09_appendix-a-exam-benchmark-methodology.md for official SAT score distributions used to compute percentiles.

## [78]
College Board. Understanding SAT scores, 2022. URL https://satsuite.collegeboard.org/media/pdf/understanding-sat-scores.pdf.
- Cited in 09_appendix-a-exam-benchmark-methodology.md for official SAT score distributions used to compute percentiles.

## [79]
College Board. AP score distributions by subject, 2022. URL https://apcentral.collegeboard.org/media/pdf/ap-score-distributions-by-subject-2022.pdf.
- Cited in 09_appendix-a-exam-benchmark-methodology.md for official AP score distributions used to compute percentiles.

## [80]
Center for Excellence in Education. 2020 USABO Semifinal exam score distribution, 2022. URL https://www.usabo-trc.org/sites/default/files/allfiles/2020%20USABO%20Semifinal%20Exam%20Histogram.pdf.
- Cited in 09_appendix-a-exam-benchmark-methodology.md for official USABO score distributions used to compute percentiles.

## [81]
Chris Swimmer. GRE score percentiles -- what does your score mean for you? (2021 update), 4 2021. URL https://magoosh.com/gre/gre-score-percentiles/.
- Cited in 09_appendix-a-exam-benchmark-methodology.md for official GRE score distributions used to compute percentiles.

## [82]
John B. Nici. *AP Art History: 5 Practice Tests + Comprehensive Review + Online Practice*. Barron's Test Prep. Barron's Educational Series, 2020. ISBN 9781506260501.
- Cited in 09_appendix-a-exam-benchmark-methodology.md as the source for the AP Art History example few-shot prompt in section A.8.

## [83]
ETS. GRE sample issue task, 2022. URL https://www.ets.org/pdfs/gre/sample-issue-task.pdf.
- Cited in 09_appendix-a-exam-benchmark-methodology.md as the source for the high-scoring GRE essay example used in the free-response few-shot prompt.

## [84]
Margaret Mitchell, Simone Wu, Andrew Zaldivar, Parker Barnes, Lucy Vasserman, Ben Hutchinson, Elena Spitzer, Inioluwa Deborah Raji, and Timnit Gebru. Model Cards for Model Reporting. In *Proceedings of the Conference on Fairness, Accountability, and Transparency*, pages 220–229, January 2019. doi: 10.1145/3287560.3287596.
- Cited in 16_appendix-h-system-card.md as the original Model Cards paper referenced alongside the GPT-4 System Card.

## [85]
Nekesha Green, Chavez Procope, Adeel Cheema, and Adekunle Adediji. System Cards, a new resource for understanding how AI systems work. https://ai.facebook.com/blog/system-cards-a-new-resource-for-understanding-how-ai-systems-work/, February 2022.
- Cited in 16_appendix-h-system-card.md as the System Cards concept referenced alongside the GPT-4 System Card.

---

# System Card Internal References

The System Card (Appendix H) uses its own separate bibliography with independent
numbering [1]–[105+]. Below are entries visible on p. 71 (the bibliography
continues beyond this page). Only entries cited in the System Card section notes
are included.

## SC [1]
A. Tamkin, M. Brundage, J. Clark, and D. Ganguli, "Understanding the Capabilities, Limitations, and Societal Impact of Large Language Models," Feb. 2021.
- Cited in 16_appendix-h-system-card.md (System Card abstract and Section 1) as part of the broad citation [1, 2, 3, 4, 5, 6, 7] noting LLMs are being deployed across many domains.

## SC [2]
"Introducing the new Bing." https://www.bing.com/new.
- Cited in 16_appendix-h-system-card.md (System Card abstract and Section 1) as part of the broad citation [1, 2, 3, 4, 5, 6, 7].

## SC [3]
J. Hilton, R. Nakano, S. Balaji, and J. Schulman, "WebGPT: Improving the factual accuracy of language models through web browsing." https://openai.com/research/webgpt, Dec. 2021.
- Cited in 16_appendix-h-system-card.md (System Card abstract and Section 1) as part of the broad citation [1, 2, 3, 4, 5, 6, 7].

## SC [4]
"ACT-1: Transformer for Actions -- Adept." https://www.adept.ai/blog/act-1.
- Cited in 16_appendix-h-system-card.md (System Card abstract and Section 1) as part of the broad citation [1, 2, 3, 4, 5, 6, 7].

## SC [5]
M. Chen, J. Tworek, H. Jun, Q. Yuan, H. P. d. O. Pinto, J. Kaplan, H. Edwards, Y. Burda, N. Joseph, G. Brockman, A. Ray, R. Puri, G. Krueger, M. Petrov, H. Khlaaf, G. Sastry, P. Mishkin, B. Chan, S. Gray, N. Ryder, M. Pavlov, A. Power, L. Kaiser, M. Bavarian, C. Winter, P. Tillet, F. P. Such, D. Cummings, M. Plappert, F. Chantzis, E. Barnes, A. Herbert-Voss, W. H. Guss, A. Nichol, A. Paino, N. Tezak, J. Tang, I. Babuschkin, S. Balaji, S. Jain, W. Saunders, C. Hesse, A. N. Carr, J. Leike, J. Achiam, V. Misra, E. Morikawa, A. Radford, M. Knight, M. Brundage, M. Murati, K. Mayer, P. Welinder, B. McGrew, D. Amodei, S. McCandlish, I. Sutskever, and W. Zaremba, "Evaluating Large Language Models Trained on Code," July 2021.
- Cited in 16_appendix-h-system-card.md (System Card abstract and Section 1) as part of the broad citations [1, 2, 3, 4, 5, 6, 7] and [5, 6, 7].

## SC [6]
L. Weidinger, J. Mellor, M. Rauh, C. Griffin, J. Uesato, P.-S. Huang, M. Cheng, M. Glaese, B. Balle, A. Kasirzadeh, Z. Kenton, S. Brown, W. Hawkins, T. Stepleton, C. Biles, A. Birhane, J. Haas, L. Rimell, L. A. Hendricks, W. Isaac, S. Legassick, G. Irving, and I. Gabriel, "Ethical and social risks of harm from Language Models," Dec. 2021.
- Cited in 16_appendix-h-system-card.md (System Card abstract and Section 1) as part of the broad citations [1, 2, 3, 4, 5, 6, 7] and [5, 6, 7]; also cited in Section 2 [6, 30] for prior observed risks, and in Section 2.3 [6, 21] for harmful content background, and in Section 2.4 [40, 41, 42, 43, 44, 45, 46, 6] for biases and stereotypes.

## SC [7]
I. Solaiman, M. Brundage, J. Clark, A. Askell, A. Herbert-Voss, J. Wu, A. Radford, G. Krueger, J. W. Kim, S. Kreps, M. McCain, A. Newhouse, J. Blazakis, K. McGuffie, and J. Wang, "Release Strategies and the Social Impacts of Language Models," Nov. 2019.
- Cited in 16_appendix-h-system-card.md (System Card abstract and Section 1) as part of the broad citations [1, 2, 3, 4, 5, 6, 7] and [5, 6, 7].

## SC [8]
A. Radford, "Improving language understanding with unsupervised learning." https://openai.com/research/language-unsupervised, June 2018.
- Cited in 16_appendix-h-system-card.md (System Card abstract and Section 1) as part of the citation [8, 9, 10] noting GPT-4 as the latest in the GPT family.

## SC [9]
A. Radford, J. Wu, D. Amodei, D. Amodei, J. Clark, M. Brundage, I. Sutskever, A. Askell, D. Lansky, D. Hernandez, and D. Luan, "Better language models and their implications." https://openai.com/research/better-language-models, Feb. 2019.
- Cited in 16_appendix-h-system-card.md (System Card abstract and Section 1) as part of the citation [8, 9, 10] noting GPT-4 as the latest in the GPT family.

## SC [10]
T. B. Brown, B. Mann, N. Ryder, M. Subbiah, J. Kaplan, P. Dhariwal, A. Neelakantan, P. Shyam, G. Sastry, A. Askell, S. Agarwal, A. Herbert-Voss, G. Krueger, T. Henighan, R. Child, A. Ramesh, D. M. Ziegler, J. Wu, C. Winter, C. Hesse, M. Chen, E. Sigler, M. Litwin, S. Gray, B. Chess, J. Clark, C. Berner, S. McCandlish, A. Radford, I. Sutskever, and D. Amodei, "Language Models are Few-Shot Learners," July 2020.
- Cited in 16_appendix-h-system-card.md (System Card abstract and Section 1) as part of the citation [8, 9, 10] and [10, 12, 13]; also cited in Section 2 [22] and GPT-3 [10] for comparison of earlier models.

## SC [11]
S. Altman, "Planning for AGI and beyond." https://openai.com/blog/planning-for-agi-and-beyond, Feb. 2023.
- Cited in 16_appendix-h-system-card.md (System Card abstract) for the need for anticipatory planning and governance; cited in 17_appendix-h-conclusion.md [11] in the context of needing more research on AI literacy, economic and social resilience, and anticipatory governance; also cited in Section 2.4 [11] for how to govern systems and share access.

## SC [12]
L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. L. Wainwright, P. Mishkin, C. Zhang, S. Agarwal, K. Slama, A. Ray, J. Schulman, J. Hilton, F. Kelton, L. Miller, M. Simens, A. Askell, P. Welinder, P. Christiano, J. Leike, and R. Lowe, "Training language models to follow instructions with human feedback," Mar. 2022.
- Cited in 16_appendix-h-system-card.md (Section 1) as part of [10, 12, 13] for RLHF fine-tuning; cited in Section 3.1 [12] for the RLHF methods used to shape GPT-4-launch behavior; cited in Section 3.1 for GPT-4-launch's improved ability to follow user intent [12].

## SC [13]
P. Christiano, J. Leike, T. B. Brown, M. Martic, S. Legg, and D. Amodei, "Deep reinforcement learning from human preferences," Feb. 2023.
- Cited in 16_appendix-h-system-card.md (Section 1) as part of [10, 12, 13] for RLHF fine-tuning.

## SC [14]
M. Mitchell, S. Wu, A. Zaldivar, P. Barnes, L. Vasserman, B. Hutchinson, E. Spitzer, I. D. Raji, and T. Gebru, "Model Cards for Model Reporting," in *Proceedings of the Conference on Fairness, Accountability, and Transparency*, pp. 220–229, Jan. 2019.
- Cited in 16_appendix-h-system-card.md (Section 1.1) as part of [14, 15, 16] for model cards and system cards concepts.

## SC [15]
N. Green, C. Procope, A. Cheema, and A. Adediji, "System Cards, a new resource for understanding how AI systems work." https://ai.facebook.com/blog/system-cards-a-new-resource-for-understanding-how-ai-systems-work/, Feb. 2022.
- Cited in 16_appendix-h-system-card.md (Section 1.1) as part of [14, 15, 16] for system cards concept.

## SC [16]
"DALL·E 2 Preview - Risks and Limitations." OpenAI, Apr. 2022.
- Cited in 16_appendix-h-system-card.md (Section 1.1) as part of [14, 15, 16]; also cited in Section 2.1.1 [16] for leveraging external expertise for domain-specific adversarial testing.

## SC [17]
J. Sandbrink, H. Hobbs, J. Swett, A. Dafoe, and A. Sandberg, "Differential Technology Development: A Responsible Innovation Principle for Navigating Technology Risks," Sept. 2022.
- Cited in 16_appendix-h-system-card.md (Section 1.1, footnote 2) for Differential Technology Development discussion.

## SC [18]
Y. Bai, A. Jones, K. Ndousse, A. Askell, A. Chen, N. DasSarma, D. Drain, S. Fort, D. Ganguli, T. Henighan, N. Joseph, S. Kadavath, J. Kernion, T. Conerly, S. El-Showk, N. Elhage, Z. Hatfield-Dodds, D. Hernandez, T. Hume, S. Johnston, S. Kravec, L. Lovitt, N. Nanda, C. Olsson, D. Amodei, T. Brown, J. Clark, S. McCandlish, C. Olah, B. Mann, and J. Kaplan, "Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback," Apr. 2022.
- Cited in 16_appendix-h-system-card.md (Section 1.1) for GPT-4-launch fine-tuned for increased helpfulness and harmlessness [18].

## SC [19]
E. Perez, S. Ringer, K. Lukošiūtė, K. Nguyen, E. Chen, S. Heiner, C. Pettit, C. Olsson, S. Kundu, S. Kadavath, A. Jones, A. Chen, B. Mann, B. Israel, B. Seethor, C. McKinnon, C. Olah, D. Yan, D. Amodei, D. Amodei, D. Drain, D. Li, E. Tran-Johnson, G. Khundadze, J. Kernion, J. Landis, J. Kerr, J. Mueller, J. Hyun, J. Landau, K. Ndousse, L. Goldberg, L. Lovitt, M. Lucas, M. Sellitto, M. Zhang, N. Kingsland, N. Elhage, N. Joseph, N. Mercado, N. DasSarma, O. Rausch, R. Larson, S. McCandlish, S. Johnston, S. Kravec, S. E. Showk, T. Lanham, T. Telleen-Lawton, T. Brown, T. Henighan, T. Hume, Y. Bai, Z. Hatfield-Dodds, J. Clark, S. R. Bowman, A. Askell, R. Grosse, D. Hernandez, D. Ganguli, E. Hubinger, N. Schiefer, and J. Kaplan, "Discovering Language Model Behaviors with Model-Written Evaluations," Dec. 2022.
- Cited in 16_appendix-h-system-card.md (Section 1.1) for sycophancy tendency that can worsen with scale [19].

## SC [20]
B. P. Kehoe, *Zen and the Art of the Internet*. Project Gutenberg, June 1992.
- Cited in 16_appendix-h-system-card.md (Section 1.1, footnote 5) referencing self-replicating computer worms (Morris worm of 1988).

## SC [21]
M. Brundage, K. Mayer, T. Eloundou, S. Agarwal, S. Adler, G. Krueger, J. Leike, and P. Mishkin, "Lessons learned on language model safety and misuse." https://openai.com/research/language-model-safety-and-misuse, Mar. 2022.
- Cited in 16_appendix-h-system-card.md (Section 1.1) for OpenAI's deployment strategy; cited in Section 2.3 [6, 21] for background on harmful content; cited in Section 3 [21] for iterating on deployment.

## SC [22]
A. Radford, J. Wu, R. Child, D. Luan, D. Amodei, and I. Sutskever, "Language Models are Unsupervised Multitask Learners," 2019.
- Cited in 16_appendix-h-system-card.md (Section 2) for GPT-2 as an earlier model compared to GPT-4.

## SC [23]
G. C. Bowker and S. L. Star, *Sorting Things Out*. MIT Press, Aug. 2000.
- Cited in 16_appendix-h-system-card.md (Section 2, footnote 6) as part of [23, 24, 25] noting the categorization is not optimal or hierarchical.

## SC [24]
L. Weidinger, J. Uesato, M. Rauh, C. Griffin, P.-S. Huang, J. Mellor, A. Glaese, M. Cheng, B. Balle, A. Kasirzadeh, C. Biles, S. Brown, Z. Kenton, W. Hawkins, T. Stepleton, A. Birhane, L. A. Hendricks, L. Rimell, W. Isaac, J. Haas, S. Legassick, G. Irving, and I. Gabriel, "Taxonomy of Risks posed by Language Models," in *2022 ACM Conference on Fairness, Accountability, and Transparency*, FAccT '22, pp. 214–229, June 2022.
- Cited in 16_appendix-h-system-card.md (Section 2, footnote 6) as part of [23, 24, 25] for risk taxonomy.

## SC [25]
I. Solaiman and C. Dennison, "Process for Adapting Language Models to Society (PALMS) with Values-Targeted Datasets," Nov. 2021.
- Cited in 16_appendix-h-system-card.md (Section 2, footnote 6) as part of [23, 24, 25] for risk categorization.

## SC [26]
H. Khlaaf, "Toward Comprehensive Risk Assessments and Assurance of AI-Based Systems," *Trail of Bits*, 2023.
- Cited in 16_appendix-h-system-card.md (Section 2.6, footnote 16) for the traditional cybersecurity usage of the term "red teaming."

## SC [27]
M. Brundage, S. Avin, J. Wang, H. Belfield, G. Krueger, G. Hadfield, H. Khlaaf, J. Yang, H. Toner, R. Fong, T. Maharaj, P. W. Koh, S. Hooker, J. Leung, A. Trask, E. Bluemke, J. Lebensold, C. O'Keefe, M. Koren, T. Ryffel, J. B. Rubinovitz, T. Besiroglu, F. Carugati, J. Clark, P. Eckersley, S. de Haas, M. Johnson, B. Laurie, A. Ingerman, I. Krawczuk, A. Askell, R. Cammarota, A. Lohn, D. Krueger, C. Stix, P. Henderson, L. Graham, C. Prunkl, B. Martin, E. Seger, N. Zilberman, S. Ó. hÉigeartaigh, F. Kroeger, G. Sastry, R. Kagan, A. Weller, B. Tse, E. Barnes, A. Dafoe, P. Scharre, A. Herbert-Voss, M. Rasser, S. Sodhani, C. Flynn, T. K. Gilbert, L. Dyer, S. Khan, Y. Bengio, and M. Anderljung, "Toward Trustworthy AI Development: Mechanisms for Supporting Verifiable Claims," Apr. 2020.
- Cited in 16_appendix-h-system-card.md (Section 2.1.1) for the definition of red teaming [27]; also cited in Section 2.1.1 [27] as one of the mechanisms used to inform identification, measurement, and testing.

## SC [28]
D. Ganguli, L. Lovitt, J. Kernion, A. Askell, Y. Bai, S. Kadavath, B. Mann, E. Perez, N. Schiefer, K. Ndousse, A. Jones, S. Bowman, A. Chen, T. Conerly, N. DasSarma, D. Drain, N. Elhage, S. El-Showk, S. Fort, Z. Hatfield-Dodds, T. Henighan, D. Hernandez, T. Hume, J. Jacobson, S. Johnston, S. Kravec, C. Olsson, S. Ringer, E. Tran-Johnson, D. Amodei, T. Brown, N. Joseph, S. McCandlish, C. Olah, J. Kaplan, and J. Clark, "Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors, and Lessons Learned," Nov. 2022.
- Cited in 16_appendix-h-system-card.md (Section 2.1.1) for reducing harmful outputs through red teaming [28].

## SC [29]
E. Perez, S. Huang, F. Song, T. Cai, R. Ring, J. Aslanides, A. Glaese, N. McAleese, and G. Irving, "Red Teaming Language Models with Language Models," Feb. 2022.
- Cited in 16_appendix-h-system-card.md (Section 2.1.1) for red teaming LMs using LMs [29]; also cited in Section 2.9 [29] for evidence that models can identify power-seeking as instrumentally useful; also cited in Section 3.1 [29] for Perez's related work on RBRMs.

## SC [30]
H. Khlaaf, P. Mishkin, J. Achiam, G. Krueger, and M. Brundage, "A Hazard Analysis Framework for Code Synthesis Large Language Models," July 2022.
- Cited in 16_appendix-h-system-card.md (Section 2.1.1) as part of [6, 30] for prior observed risks in language models.

## SC [31]
J. Maynez, S. Narayan, B. Bohnet, and R. McDonald, "On Faithfulness and Factuality in Abstractive Summarization," May 2020.
- Cited in 16_appendix-h-system-card.md (Section 2.2) as part of [31, 32] for the definition of hallucination.

## SC [32]
S. Lin, J. Hilton, and O. Evans, "TruthfulQA: Measuring How Models Mimic Human Falsehoods," May 2022.
- Cited in 16_appendix-h-system-card.md (Section 2.2) as part of [31, 32] for the definition of hallucination.

## SC [33]
J. A. Goldstein, G. Sastry, M. Musser, R. DiResta, M. Gentzel, and K. Sedova, "Forecasting potential misuses of language models for disinformation campaigns and how to reduce risk." https://openai.com/research/forecasting-misuse, Jan. 2023.
- Cited in 16_appendix-h-system-card.md (Section 2.2) for hallucinations leading to degradation of overall information quality [33].

## SC [34]
O. Evans, O. Cotton-Barratt, L. Finnveden, A. Bales, A. Balwit, P. Wills, L. Righetti, and W. Saunders, "Truthful AI: Developing and governing AI that does not lie," Oct. 2021.
- Cited in 16_appendix-h-system-card.md (Section 2.2) for open domain hallucination evaluation using a "factual" set [34]; also cited in Section 3.1 [34] for TruthfulQA factuality evaluations.

## SC [35]
A. Xu, E. Pathak, E. Wallace, S. Gururangan, M. Sap, and D. Klein, "Detoxifying Language Models Risks Marginalizing Minority Voices," Apr. 2021.
- Cited in 16_appendix-h-system-card.md (Section 2.3, footnote 12) for how terms like "harmful" or "toxic" can be wielded in harmful ways [35]; also cited in Section 2.4 [35] for how refusals can exacerbate bias.

## SC [36]
L. Dixon, J. Li, J. Sorensen, N. Thain, and L. Vasserman, "Measuring and Mitigating Unintended Bias in Text Classification," in *Proceedings of the 2018 AAAI/ACM Conference on AI, Ethics, and Society*, AIES '18, pp. 67–73, Dec. 2018.
- Cited in 16_appendix-h-system-card.md (Section 2.3, footnote 12) for false-positive bias in classifiers (e.g., queer content flagged as unsafe) [36].

## SC [37]
T. Markov, C. Zhang, S. Agarwal, T. Eloundou, T. Lee, S. Adler, A. Jiang, and L. Weng, "A Holistic Approach to Undesired Content Detection in the Real World," Feb. 2023.
- Cited in 16_appendix-h-system-card.md (Section 2.3, footnote 12) for OpenAI's content taxonomy [37]; also cited in Section 3.1 [37] for internally trained classifiers used to filter pre-training data.

## SC [38]
OpenAI, "How should AI systems behave, and who should decide?." https://openai.com/blog/how-should-ai-systems-behave, Feb. 2023.
- Cited in 16_appendix-h-system-card.md (Section 2.3, footnote 12) for OpenAI's justifications for AI systems' behavior [38].

## SC [39]
M. Rauh, J. Mellor, J. Uesato, P.-S. Huang, J. Welbl, L. Weidinger, S. Dathathri, A. Glaese, G. Irving, I. Gabriel, W. Isaac, and L. A. Hendricks, "Characteristics of Harmful Text: Towards Rigorous Benchmarking of Language Models," Oct. 2022.
- Cited in 16_appendix-h-system-card.md (Section 2.3) for context of usage playing a key role in determining harm [39].

## SC [40]
S. L. Blodgett, S. Barocas, H. Daumé III, and H. Wallach, "Language (Technology) is Power: A Critical Survey of 'Bias' in NLP." https://arxiv.org/abs/2005.14050v2, May 2020.
- Cited in 16_appendix-h-system-card.md (Section 2.4) as part of [40, 41, 42, 43, 44, 45, 46, 6] for biases and stereotypes in language models.

## SC [41]
S. Dev, E. Sheng, J. Zhao, A. Amstutz, J. Sun, Y. Hou, M. Sanseverino, J. Kim, A. Nishi, N. Peng, and K.-W. Chang, "On Measures of Biases and Harms in NLP," in *Findings of the Association for Computational Linguistics: AACL-IJCNLP 2022*, pp. 246–267, Nov. 2022.
- Cited in 16_appendix-h-system-card.md (Section 2.4) as part of [40, 41, 42, 43, 44, 45, 46, 6] for biases in NLP.

## SC [42]
T. Bolukbasi, K.-W. Chang, J. Zou, V. Saligrama, and A. Kalai, "Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings," July 2016.
- Cited in 16_appendix-h-system-card.md (Section 2.4) as part of [40, 41, 42, 43, 44, 45, 46, 6] for biases in word embeddings.

## SC [43]
H. Gonen and Y. Goldberg, "Lipstick on a Pig: Debiasing Methods Cover up Systematic Gender Biases in Word Embeddings But do not Remove Them," in *Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers)*, pp. 609–614, June 2019.
- Cited in 16_appendix-h-system-card.md (Section 2.4) as part of [40, 41, 42, 43, 44, 45, 46, 6] for biases; also cited in Section 2.4 [43] for how refusals can contribute to a false sense of assurance.

## SC [44]
K. Webster, M. Recasens, V. Axelrod, and J. Baldridge, "Mind the GAP: A Balanced Corpus of Gendered Ambiguous Pronouns," Oct. 2018.
- Cited in 16_appendix-h-system-card.md (Section 2.4) as part of [40, 41, 42, 43, 44, 45, 46, 6] for biases.

## SC [45]
E. M. Bender, T. Gebru, A. McMillan-Major, and S. Shmitchell, "On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?," in *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency*, pp. 610–623, Mar. 2021.
- Cited in 16_appendix-h-system-card.md (Section 2.4) as part of [40, 41, 42, 43, 44, 45, 46, 6] for biases; also cited in Section 2.4 [47, 48, 45, 49] for reinforcing ideologies and worldviews.

## SC [46]
R. Bommasani, D. A. Hudson, E. Adeli, R. Altman, S. Arora, S. von Arx, M. S. Bernstein, J. Bohg, A. Bosselut, E. Brunskill, et al., "On the Opportunities and Risks of Foundation Models," Aug. 2021.
- Cited in 16_appendix-h-system-card.md (Section 2.4) as part of [40, 41, 42, 43, 44, 45, 46, 6] for biases in foundation models.

## SC [47]
S. U. Noble, *Algorithms of Oppression*. NYU Press, Feb. 2018.
- Cited in 16_appendix-h-system-card.md (Section 2.4) as part of [47, 48, 45, 49] for AI reinforcing ideologies and worldviews.

## SC [48]
R. Richardson, J. Schultz, and K. Crawford, "Dirty Data, Bad Predictions: How Civil Rights Violations Impact Police Data, Predictive Policing Systems, and Justice," Feb. 2019.
- Cited in 16_appendix-h-system-card.md (Section 2.4) as part of [47, 48, 45, 49] for AI reinforcing ideologies.

## SC [49]
W. MacAskill, *What We Owe The Future*. Basic Books, Aug. 2022.
- Cited in 16_appendix-h-system-card.md (Section 2.4) as part of [47, 48, 45, 49] for foreclosing future contestation.

## SC [50]
OpenAI, "GPT-2: 1.5B release." https://openai.com/research/gpt-2-1-5b-release, Nov. 2019.
- Cited in 16_appendix-h-system-card.md (Section 2.5) for risk of GPT-4 being used to generate misleading content [50].

## SC [51]
S. Kreps, R. M. McCain, and M. Brundage, "All the News That's Fit to Fabricate: AI-Generated Text as a Tool of Media Misinformation," *Journal of Experimental Political Science*, vol. 9, no. 1, pp. 104–117, 2022.
- Cited in 16_appendix-h-system-card.md (Section 2.5) for earlier LMs useful for generating misleading but persuasive content [51].

## SC [52]
B. Buchanan, A. Lohn, M. Musser, and K. Sedova, "Truth, Lies, and Automation," tech. rep., Center for Security and Emerging Technology, May 2021.
- Cited in 16_appendix-h-system-card.md (Section 2.5) for GPT-3 being capable of tasks relevant to changing the narrative on a topic [52].

## SC [53]
A. Myers, "AI's Powers of Political Persuasion." https://hai.stanford.edu/news/ais-powers-political-persuasion, Feb. 2023.
- Cited in 16_appendix-h-system-card.md (Section 2.5) as part of [53, 54] for persuasive appeals by LMs on politically charged issues.

## SC [54]
H. Bai, J. Voelkel, J. Eichstaedt, and R. Willer, "Artificial intelligence can persuade humans on political issues," 2023.
- Cited in 16_appendix-h-system-card.md (Section 2.5) as part of [53, 54] for persuasive appeals by LMs on politically charged issues.

## SC [55]
E. Horvitz, "On the Horizon: Interactive and Compositional Deepfakes," in *INTERNATIONAL CONFERENCE ON MULTIMODAL INTERACTION*, pp. 653–661, Nov. 2022.
- Cited in 16_appendix-h-system-card.md (Section 2.5) for false information casting doubt on the information environment [55].

## SC [56]
R. Chesney and D. K. Citron, "Deep Fakes: A Looming Challenge for Privacy, Democracy, and National Security," July 2018.
- Cited in 16_appendix-h-system-card.md (Section 2.5) for the "Liar's Dividend" phenomenon [56].

## SC [57]
U.S. Department of Commerce, "Dual use export licenses," March 13 2023.
- Cited in 16_appendix-h-system-card.md (Section 2.6) for dual-use potential definition [57].

## SC [58]
NATO, "Arms control, disarmament and non-proliferation in nato," February 27 2023.
- Cited in 16_appendix-h-system-card.md (Section 2.6, footnote 17) for the definition of WMD proliferation [58].

## SC [59]
N. Carlini, F. Tramer, E. Wallace, M. Jagielski, A. Herbert-Voss, K. Lee, A. Roberts, T. Brown, D. Song, U. Erlingsson, A. Oprea, and C. Raffel, "Extracting Training Data from Large Language Models," June 2021.
- Cited in 16_appendix-h-system-card.md (Section 2.7) as part of [59, 60] for privacy risks from publicly available personal information in training data.

## SC [60]
N. Carlini, D. Ippolito, M. Jagielski, K. Lee, F. Tramer, and C. Zhang, "Quantifying Memorization Across Neural Language Models," Mar. 2023.
- Cited in 16_appendix-h-system-card.md (Section 2.7) as part of [59, 60] for privacy risks from memorization.

## SC [61]
D. Ganguli, D. Hernandez, L. Lovitt, N. DasSarma, T. Henighan, A. Jones, N. Joseph, J. Kernion, B. Mann, A. Askell, Y. Bai, A. Chen, T. Conerly, D. Drain, N. Elhage, S. E. Showk, S. Fort, Z. Hatfield-Dodds, S. Johnston, S. Kravec, N. Nanda, K. Ndousse, C. Olsson, D. Amodei, T. Brown, J. Kaplan, S. McCandlish, C. Olah, and J. Clark, "Predictability and Surprise in Large Generative Models," in *2022 ACM Conference on Fairness, Accountability, and Transparency*, pp. 1747–1764, June 2022.
- Cited in 16_appendix-h-system-card.md (Section 2.9) as part of [61, 62] for novel capabilities emerging in more powerful models.

## SC [62]
J. Wei, Y. Tay, R. Bommasani, C. Raffel, B. Zoph, S. Borgeaud, D. Yogatama, M. Bosma, D. Zhou, D. Metzler, E. H. Chi, T. Hashimoto, O. Vinyals, P. Liang, J. Dean, and W. Fedus, "Emergent Abilities of Large Language Models," Oct. 2022.
- Cited in 16_appendix-h-system-card.md (Section 2.9) as part of [61, 62] for emergent capabilities.

## SC [63]
R. Ngo, L. Chan, and S. Mindermann, "The alignment problem from a deep learning perspective," Feb. 2023.
- Cited in 16_appendix-h-system-card.md (Section 2.9) for the ability to create and act on long-term plans [63].

## SC [64]
N. Bostrom, *Superintelligence: Paths, Dangers, Strategies*. United Kingdom: Oxford University Press, Sept. 2014.
- Cited in 16_appendix-h-system-card.md (Section 2.9) for power-seeking behavior [64].

## SC [65]
A. Chan, R. Salganik, A. Markelius, C. Pang, N. Rajkumar, D. Krasheninnikov, L. Langosco, Z. He, Y. Duan, M. Carroll, M. Lin, A. Mayhew, K. Collins, M. Molamohammadi, J. Burden, W. Zhao, S. Rismani, K. Voudouris, U. Bhatt, A. Weller, D. Krueger, and T. Maharaj, "Harms from Increasingly Agentic Algorithmic Systems," Feb. 2023.
- Cited in 16_appendix-h-system-card.md (Section 2.9) for agentic behavior [65]; also cited as part of [66, 67, 65] for evidence of emergent behavior.

## SC [66]
J. Andreas, "Language Models as Agent Models," Dec. 2022.
- Cited in 16_appendix-h-system-card.md (Section 2.9) as part of [66, 67, 65] for evidence of emergent behavior in models.

## SC [67]
J. Steinhardt, "Emergent Deception and Emergent Optimization." https://bounded-regret.ghost.io/emergent-deception-optimization/, Feb. 2023.
- Cited in 16_appendix-h-system-card.md (Section 2.9) as part of [66, 67, 65] for evidence of emergent behavior.

## SC [68]
S. M. Omohundro, "The Basic AI Drives," in *Proceedings of the 2008 Conference on Artificial General Intelligence 2008*, pp. 483–492, IOS Press, June 2008.
- Cited in 16_appendix-h-system-card.md (Section 2.9) as part of [68, 69] for auxiliary power-seeking actions being inherently useful.

## SC [69]
N. Bostrom, "The Superintelligent Will: Motivation and Instrumental Rationality in Advanced Artificial Agents," *Minds and Machines*, vol. 22, pp. 71–85, May 2012.
- Cited in 16_appendix-h-system-card.md (Section 2.9) as part of [68, 69] for instrumental convergence in power-seeking.

## SC [70]
A. M. Turner, L. Smith, R. Shah, A. Critch, and P. Tadepalli, "Optimal Policies Tend to Seek Power," Jan. 2023.
- Cited in 16_appendix-h-system-card.md (Section 2.9) as part of [70, 71, 72] for power-seeking being optimal for most reward functions.

## SC [71]
A. M. Turner and P. Tadepalli, "Parametrically Retargetable Decision-Makers Tend To Seek Power," Oct. 2022.
- Cited in 16_appendix-h-system-card.md (Section 2.9) as part of [70, 71, 72] for power-seeking being optimal.

## SC [72]
V. Krakovna and janos, "Power-seeking can be probable and predictive for trained agents," Mar. 2023.
- Cited in 16_appendix-h-system-card.md (Section 2.9) as part of [70, 71, 72] for power-seeking being optimal.

## SC [73]
S. Russell, *Human Compatible: Artificial Intelligence and the Problem of Control*. Cham: Springer International Publishing, 2022.
- Cited in 16_appendix-h-system-card.md (Section 2.9) as part of [73, 74] for high risks of power-seeking.

## SC [74]
J. Carlsmith, "Is Power-Seeking AI an Existential Risk?," June 2022.
- Cited in 16_appendix-h-system-card.md (Section 2.9) as part of [73, 74] for high risks of power-seeking.

## SC [75]
Alignment Research Center, "Update on arc's recent eval efforts," March 2023. accessed 2023-03-17.
- Cited in 16_appendix-h-system-card.md (Section 2.9, footnote 20) for ARC's methodology of combining GPT-4 with a read-execute-print loop to test autonomous replication [75].

## SC [76]
E. Karpas, O. Abend, Y. Belinkov, B. Lenz, O. Lieber, N. Ratner, Y. Shoham, H. Bata, Y. Levine, K. Leyton-Brown, D. Muhlgay, N. Rozen, E. Schwartz, G. Shachaf, S. Shalev-Shwartz, A. Shashua, and M. Tenenholtz, "MRKL Systems: A modular, neuro-symbolic architecture that combines large language models, external knowledge sources and discrete reasoning," May 2022.
- Cited in 16_appendix-h-system-card.md (Section 2.10) as part of [76, 77, 78, 79] for GPT-4 augmented with other tools.

## SC [77]
T. Schick, J. Dwivedi-Yu, R. Dessì, R. Raileanu, M. Lomeli, L. Zettlemoyer, N. Cancedda, and T. Scialom, "Toolformer: Language Models Can Teach Themselves to Use Tools," Feb. 2023.
- Cited in 16_appendix-h-system-card.md (Section 2.10) as part of [76, 77, 78, 79] for tool-augmented language models.

## SC [78]
G. Mialon, R. Dessì, M. Lomeli, C. Nalmpantis, R. Pasunuru, R. Raileanu, B. Rozière, T. Schick, J. Dwivedi-Yu, A. Celikyilmaz, E. Grave, Y. LeCun, and T. Scialom, "Augmented Language Models: A Survey," Feb. 2023.
- Cited in 16_appendix-h-system-card.md (Section 2.10) as part of [76, 77, 78, 79] for augmented language models.

## SC [79]
A. Parisi, Y. Zhao, and N. Fiedel, "TALM: Tool Augmented Language Models," May 2022.
- Cited in 16_appendix-h-system-card.md (Section 2.10) as part of [76, 77, 78, 79] for tool-augmented language models.

## SC [80]
D. Weininger, "Smiles, a chemical language and information system. 1. introduction to methodology and encoding rules," *Journal of chemical information and computer sciences*, vol. 28, no. 1, pp. 31–36, 1988.
- Cited in 16_appendix-h-system-card.md (Section 2.10, footnote 21) for the SMILES molecular notation system [80].

## SC [81]
E. Calvano, G. Calzolari, V. Denicolò, and S. Pastorello, "Artificial Intelligence, Algorithmic Pricing, and Collusion," Apr. 2019.
- Cited in 16_appendix-h-system-card.md (Section 2.10) for algorithmic collusion as an example of harmful feedback loops [81].

## SC [82]
D. Krueger, T. Maharaj, and J. Leike, "Hidden Incentives for Auto-Induced Distributional Shift," Sept. 2020.
- Cited in 16_appendix-h-system-card.md (Section 2.10) for manipulation of humans in the loop and polarization of users of recommender systems [82].

## SC [83]
S. J. DeCanio, "Robots and humans -- complements or substitutes?," *Journal of Macroeconomics*, vol. 49, pp. 280–291, Sept. 2016.
- Cited in 16_appendix-h-system-card.md (Section 2.11) for GPT-4 or subsequent models potentially leading to automation of certain jobs [83].

## SC [84]
A. Korinek and J. E. Stiglitz, "Artificial Intelligence and Its Implications for Income Distribution and Unemployment," in *The Economics of Artificial Intelligence: An Agenda*, pp. 349–390, University of Chicago Press, Jan. 2018.
- Cited in 16_appendix-h-system-card.md (Section 2.11) for workforce displacement [84].

## SC [85]
J. H. Choi, K. E. Hickman, A. Monahan, and D. Schwarcz, "ChatGPT Goes to Law School," Jan. 2023.
- Cited in 16_appendix-h-system-card.md (Section 2.11) for GPT-4 impacting jobs requiring years of experience and education, such as legal services [85].

## SC [86]
L. R. Raymond, E. Brynjolfsson, and D. Li, "Augmented intelligence: The effects of ai on productivity and work practices," Sep 2022.
- Cited in 16_appendix-h-system-card.md (Section 2.11) for upskilling in call centers [86].

## SC [87]
E. van Inwegen, Z. Munyikwa, and J. J. Horton, "Algorithmic Writing Assistance on Jobseekers' Resumes Increases Hires," Jan. 2023.
- Cited in 16_appendix-h-system-card.md (Section 2.11) for help with writing [87] and better matching of candidates to jobs [87].

## SC [88]
A. Ziegler, E. Kalliamvakou, G. Simister, G. Sittampalam, A. Li, A. Rice, D. Rifkin, and E. Aftandilian, "Productivity Assessment of Neural Code Completion," May 2022.
- Cited in 16_appendix-h-system-card.md (Section 2.11) for coding assistance [88].

## SC [89]
S. Noy and W. Zhang, "Experimental evidence on the productivity effects of generative artificial intelligence," *Available at SSRN 4375283*, 2023.
- Cited in 16_appendix-h-system-card.md (Section 2.11) for improving overall job satisfaction [89].

## SC [90]
S. Peng, E. Kalliamvakou, P. Cihon, and M. Demirer, "The impact of ai on developer productivity: Evidence from github copilot," *arXiv preprint arXiv:2302.06590*, 2023.
- Cited in 16_appendix-h-system-card.md (Section 2.11) for improving overall job satisfaction [90].

## SC [91]
D. Acemoglu and P. Restrepo, "Demographics and Automation," *The Review of Economic Studies*, vol. 89, pp. 1–44, Jan. 2022.
- Cited in 16_appendix-h-system-card.md (Section 2.11) for automation technologies historically increasing inequality [91].

## SC [92]
Partnership on AI, "AI and Job Quality," tech. rep., Partnership on AI, Sept. 2022.
- Cited in 16_appendix-h-system-card.md (Section 2.11) for attention to how models are deployed in the workplace over time [92].

## SC [93]
"OpenAI Charter." https://openai.com/charter, Apr. 2018.
- Cited in 16_appendix-h-system-card.md (Section 2.12, footnote 23) for OpenAI's commitment to stop competing with safety-conscious projects close to AGI [93].

## SC [94]
S. Armstrong, N. Bostrom, and C. Shulman, "Racing to the precipice: A model of artificial intelligence development," Technical 2013-1, Future of Humanity Institute, Oct. 2013.
- Cited in 16_appendix-h-system-card.md (Section 2.12, footnote 24) for background on acceleration risk [94].

## SC [95]
P. E. Tetlock and D. Gardner, *Superforecasting: The Art and Science of Prediction*. Crown, Sept. 2015.
- Cited in 16_appendix-h-system-card.md (Section 2.12, footnote 26) for defining forecaster expertise empirically by competitive track record [95].

## SC [96]
S. Passi and M. Vorvoreanu, "Overreliance on AI Literature Review," tech. rep., AI Ethics and Effects in Engineering and Research, June 2022.
- Cited in 16_appendix-h-system-card.md (Section 2.13) for overreliance as a failure mode that increases with model capability [96].

## SC [97]
PAI, "Data enrichment sourcing guidelines," November 2022. accessed 2023-03-13.
- Cited in 16_appendix-h-system-card.md (Section 3.1, footnote 28) as part of [97, 98] for industry-best practices in annotator treatment.

## SC [98]
PAI, "Responsible sourcing of data enrichment services," June 2021. accessed 2023-03-13.
- Cited in 16_appendix-h-system-card.md (Section 3.1, footnote 28) as part of [97, 98] for responsible sourcing of data enrichment.

## SC [99]
J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov, "Proximal Policy Optimization Algorithms," Aug. 2017.
- Cited in 16_appendix-h-system-card.md (Section 3.1) for the PPO algorithm used in reinforcement learning fine-tuning [99].

## SC [100]
A. Glaese, N. McAleese, M. Trębacz, J. Aslanides, V. Firoiu, T. Ewalds, M. Rauh, L. Weidinger, M. Chadwick, P. Thacker, L. Campbell-Gillingham, J. Uesato, P.-S. Huang, R. Comanescu, F. Yang, A. See, S. Dathathri, R. Greig, C. Chen, D. Fritz, J. S. Elias, R. Green, S. Mokrá, N. Fernando, B. Wu, R. Foley, S. Young, I. Gabriel, W. Isaac, J. Mellor, D. Hassabis, K. Kavukcuoglu, L. A. Hendricks, and G. Irving, "Improving alignment of dialogue agents via targeted human judgements," Sept. 2022.
- Cited in 16_appendix-h-system-card.md (Section 3.1) as part of [100, 101] for rule-based reward models (RBRMs); also cited as Glaese [100] for related RBRM technique.

## SC [101]
Y. Bai, S. Kadavath, S. Kundu, A. Askell, J. Kernion, A. Jones, A. Chen, A. Goldie, A. Mirhoseini, C. McKinnon, C. Chen, C. Olsson, C. Olah, D. Hernandez, D. Drain, D. Ganguli, D. Li, E. Tran-Johnson, E. Perez, J. Kerr, J. Mueller, J. Ladish, J. Landau, K. Ndousse, K. Lukošiūtė, L. Lovitt, M. Sellitto, N. Elhage, N. Schiefer, N. Mercado, N. DasSarma, R. Lasenby, R. Larson, S. Ringer, S. Johnston, S. Kravec, S. E. Showk, S. Fort, T. Lanham, T. Telleen-Lawton, T. Conerly, T. Henighan, T. Hume, S. R. Bowman, Z. Hatfield-Dodds, B. Mann, D. Amodei, N. Joseph, S. McCandlish, T. Brown, and J. Kaplan, "Constitutional AI: Harmlessness from AI Feedback," Dec. 2022.
- Cited in 16_appendix-h-system-card.md (Section 3.1) as part of [100, 101] for RBRMs; also cited in Figure 8 caption as "Askell et al [101]" (this appears to be a naming error in the original paper -- the reference is Bai et al., not Askell et al.); also cited in Section 4.2 [101] for building classifiers for new content areas faster.

## SC [102]
S. Gehman, S. Gururangan, M. Sap, Y. Choi, and N. A. Smith, "RealToxicityPrompts: Evaluating Neural Toxic Degeneration in Language Models," *Findings of the Association for Computational Linguistics: EMNLP 2020*, pp. 3356–3369, 2020.
- Cited in 16_appendix-h-system-card.md (Section 3.1, footnote 29) for the RealToxicityPrompts dataset of 100k sentence snippets [102].

## SC [103]
OpenAI, "Introducing chatgpt," November 2022. accessed 2023-03-13.
- Cited in 16_appendix-h-system-card.md (Section 3.1) for ChatGPT user prompt collection [103].

## SC [104]
OpenAI, "Openai api," June 2020. accessed 2023-03-13.
- Cited in 16_appendix-h-system-card.md (Section 3.1) for OpenAI API user prompt collection [104].

## SC [105]
T. Davidson, D. Bhattacharya, and I. Weber, "Racial Bias in Hate Speech and Abusive Language Detection Datasets," in *Proceedings of the Third Workshop on Abusive Language Online*, pp. 25–35, Association for Computational Linguistics, Aug. 2019.
- Cited in 16_appendix-h-system-card.md (Section 4.2, footnote 32) for content classifiers themselves being a potential source of harms by exacerbating bias [105].
