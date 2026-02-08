# Overview

**Title:** Democratizing Open and Compliant LLMs for Global Language Environments

**Authors (Project Apertus):**

*Core Team:* Alejandro Hernandez-Cano^1, Alexander Hagele^1, Allen Hao Huang^1, Angelika Romanou^1, Antoni-Joan Solergibert^{1,2}, Barna Pasztor^2, Bettina Messmer^1, Dhia Garbaya^1, Eduard Frank Durech^{1,2}, Ido Hakimi^2, Juan Garcia Giraldo^1, Mete Ismayilzada^1, Negar Foroutan^1, Skander Moalla^1, Tiancheng Chen^2, Vinko Sabolcec^1, Yixuan Xu^{1,2}

*Contributors:* Michael Aerni^2, Badr AlKhamissi^1, Ines Altemir Marinas^1, Mohammad Hossein Amani^1, Matin Ansaripour^1, Ilia Badanin^{1,2}, Harold Benoit^1, Emanuela Boros^1, Nicholas Browning^3, Fabian Bosch^3, Maximilian Bother^2, Niklas Canova^2, Camille Challier^1, Clement Charmillot^1, Jonathan Coles^3, Jan Deriu^7, Arnout Devos^2, Lukas Drescher^3, Daniil Dzenhaliou^1, Maud Ehrmann^1, Dongyang Fan^1, Simin Fan^1, Silin Gao^1, Miguel Gila^3, Maria Grandury^1, Diba Hashemi^1, Alexander Hoyle^2, Jiaming Jiang^1, Mark Klein^3, Andrei Kucharavy^4, Anastasiia Kucherenko^4, Frederike Lubeck^2, Roman Machacek^9, Theofilos Manitaras^3, Andreas Marfurt^5, Kyle Matoba^1, Simon Matrenok^1, Henrique Mendonca^3, Fawzi Roberto Mohamed^3, Syrielle Montariol^1, Luca Mouchel^1, Sven Najem-Meyer^1, Jingwei Ni^2, Gennaro Oliva^3, Matteo Pagliardini^1, Elia Palme^3, Andrei Panferov^6, Leo Paoletti^1, Marco Passerini^3, Ivan Pavlov^1, Auguste Poiroux^1, Kaustubh Ponkshe^1, Nathan Ranchin^1, Javi Rando^2, Mathieu Sauser^1, Jakhongir Saydaliev^1, Muhammad Ali Sayfiddinov^2, Marian Schneider^2, Stefano Schuppli^3, Marco Scialanga^1, Andrei Semenov^1, Kumar Shridhar^2, Raghav Singhal^1, Anna Sotnikova^1, Alexander Sternfeld^4, Ayush Kumar Tarun^1, Paul Teiletche^1, Jannis Vamvas^8, Xiaozhe Yao^2, Hao Zhao^1

*Advisors:* Alexander Ilic^2, Ana Klimovic^2, Andreas Krause^2, Caglar Gulcehre^1, David Rosenthal^{10}, Elliott Ash^2, Florian Tramer^2, Joost VandeVondele^3, Livio Veraldi^{10}, Martin Rajman^1, Thomas Schulthess^3, Torsten Hoefler^2

*Leads:* Antoine Bosselut^1, Martin Jaggi^1, Imanol Schlag^2

**Affiliations:**
1. EPFL
2. ETH Zurich
3. CSCS
4. HES-SO Valais-Wallis
5. HSLU
6. IST Austria
7. ZHAW
8. University of Zurich
9. University of Bern
10. Vischer

*Authors ordered alphabetically by first or last name in grouping. Contributions in Appendix A.

**Venue:** Apertus v1 Technical Report

**Date:** arXiv:2509.14233v2 [cs.CL] 1 Dec 2025

**Abstract:**
> "We present Apertus, a fully open suite of large language models (LLMs) designed to address two systemic shortcomings in today's open model ecosystem: data compliance and multilingual representation. Unlike many prior models that release weights without reproducible data pipelines or regard for content-owner rights, Apertus models are pretrained exclusively on openly available data, retroactively respecting robots.txt exclusions and filtering for non-permissive, toxic, and personally identifiable content. To mitigate risks of memorization, we adopt the Goldfish objective during pretraining, strongly suppressing verbatim recall of data while retaining downstream task performance. The Apertus models also expand multilingual coverage, training on 15T tokens from over 1800 languages, with ~40% of pretraining data allocated to non-English content. Released at 8B and 70B scales, Apertus approaches state-of-the-art results among fully open models on multilingual benchmarks, rivalling or surpassing open-weight counterparts. Beyond model weights, we release all scientific artifacts from our development cycle with a permissive license, including data preparation scripts, checkpoints, evaluation suites, and training code, enabling transparent audit and extension." [p. 2]

## Section headings

1. Introduction (p. 6)
2. Model Architecture & Pretraining Recipe (p. 9)
   - 2.1 Model Architecture (p. 9)
   - 2.2 Tokenizer (p. 10)
   - 2.3 Optimizer & Training Recipe (p. 11)
   - 2.4 Ablations (p. 13)
   - 2.5 Long Context (p. 14)
   - 2.6 Final Run Retrospective (p. 15)
3. Pretraining Data (p. 17)
   - 3.1 Data Compliance (p. 17)
     - 3.1.1 Consent: robots.txt with Hindsight (p. 17)
     - 3.1.2 Personally identifiable information (PII) (p. 18)
     - 3.1.3 Toxicity Filtering (p. 18)
   - 3.2 Source Datasets (p. 18)
     - 3.2.1 English-only Data (p. 18)
     - 3.2.2 Multilingual Data (p. 20)
     - 3.2.3 Code, Mathematical, and Structured Data (p. 20)
     - 3.2.4 Data for Downstream Analysis (p. 21)
     - 3.2.5 Data Filtering (p. 21)
   - 3.3 Pretraining Curriculum (p. 21)
   - 3.4 Long Context Data Mixture (p. 23)
4. Post-Training (p. 26)
   - 4.1 Data Overview (p. 26)
     - 4.1.1 Data Collection & Legal Compliance (p. 26)
     - 4.1.2 Decontamination (p. 27)
     - 4.1.3 Supervised Finetuning Data (p. 28)
     - 4.1.4 Alignment Data (p. 30)
   - 4.2 Supervised Finetuning (p. 31)
     - 4.2.1 Format and Chat Template (p. 31)
   - 4.3 Preference Alignment (p. 32)
     - 4.3.1 Alignment for Standard Topics (p. 33)
     - 4.3.2 Alignment of Controversial Topics (p. 34)
   - 4.4 Chatbot System Prompt (p. 36)
5. Evaluations (p. 37)
   - 5.1 Pretraining Evaluation (p. 37)
   - 5.2 Post-training evaluation (p. 39)
   - 5.3 Low-resource Translation (p. 42)
   - 5.4 Verbatim Memorization (p. 46)
     - 5.4.1 Apertus Memorization Patterns (p. 46)
     - 5.4.2 Failure Case Studies (p. 47)
   - 5.5 Security And Safety (p. 49)
     - 5.5.1 General Considerations (p. 49)
     - 5.5.2 Safety Benchmark Performance (p. 49)
   - 5.6 Qualitative Spot-Testing (p. 51)
6. Infrastructure, Scaling, and Efficiency (p. 52)
   - 6.1 Infrastructure (p. 52)
     - 6.1.1 The Alps Research Infrastructure (p. 52)
     - 6.1.2 The Machine Learning Platform (p. 52)
   - 6.2 Full Training Run Performance (p. 53)
   - 6.3 Engineering Challenges and Solutions (p. 53)
     - 6.3.1 Systems-level Fixes (p. 54)
     - 6.3.2 Stability and Container Robustness (p. 55)
     - 6.3.3 Checkpointing and Restart Strategies (p. 55)
     - 6.3.4 Performance Optimizations at Scale (p. 55)
     - 6.3.5 Operational Efficiency and Monitoring (p. 56)
     - 6.3.6 Scaling and Parallel Efficiency (p. 56)
7. Conclusion (p. 57)
Acknowledgements (p. 57–58)
A. Contributions Statement (p. 79)
B. Data opt-out by Applying AI-crawler Blocks Retroactively (p. 80)
C. Pretraining Hyperparameters (p. 82)
D. FP8 Training (p. 83)
E. FLOPs Estimation (p. 83)
F. Implementation of Goldfish Loss (p. 85)
G. FineWeb-2 Language Distribution (p. 88)
H. Additional Pretraining Data (p. 90)
   - H.1 Synthetic data for scientific research in data poisoning and memorization (p. 90)
   - H.2 Possible Swiss Data (Not currently used in pretraining) (p. 90)
   - H.3 Apertus 8B and 70B data stages (p. 91)
I. Tokenizer Selection (p. 92)
J. Supplementary Material on Post-Training (p. 94)
   - J.1 Romansh SFT Data (p. 94)
   - J.2 Completion generation prompts (p. 94)
   - J.3 Ideological Sensitivity Classifier (p. 97)
   - J.4 Synthetic Degradation Prompt (p. 99)
   - J.5 Additional Results: Charter Analysis (p. 100)
K. SwitzerlandQA (p. 102)
L. Constitutional Harms Test derivation (p. 103)
   - L.1 Prompts (p. 103)
   - L.2 Identified Risk Classes (p. 104)
     - L.2.1 Enabling Discrimination (p. 104)
     - L.2.2 Facilitating Exploitation (p. 105)
     - L.2.3 Endangering Vulnerable Populations (p. 106)
     - L.2.4 Prioritizing Abstract Considerations Over Human Safety (p. 106)
     - L.2.5 Enabling Dangerous Actions (p. 108)
     - L.2.6 Inadequate Response to Self-Harm or Harm to Others (p. 108)
     - L.2.7 Propagating or Failing to Correct Dangerous Misinformation (p. 109)
     - L.2.8 Reinforcing Harmful Stereotypes (p. 110)
     - L.2.9 Undermining Humanitarian or International Efforts (p. 111)
M. Harms Spot Testing (p. 112)
   - M.1 Harms Spot Testing Risk Models (p. 112)
     - M.1.1 Risks Related to Malicious Use (p. 112)
     - M.1.2 Risks Related to Misguided Use (p. 113)
     - M.1.3 Risks Out of Scope (p. 113)
   - M.2 Harms Spot Testing Prompts (p. 113)
N. Discovered Issues with Existing Safety and Security Evaluation tools (p. 113)
   - N.1 Wrongful toxic response detection example (p. 113)
   - N.2 LinguaSafe (p. 113)
O. The Swiss AI Charter (p. 115)
P. System Prompt for Chatbot (p. 118)
