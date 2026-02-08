# 8. Responsibility, Safety, Security [p. 10–11]

Responsibility, safety and security are of paramount importance when developing Gemma models. To reduce risks to Gemma 2 users, enhanced internal safety processes that span the development workflow have been integrated, in line with recent Google AI models (Gemini Team, 2024). Similar to the inaugural Gemma release, a three pillar approach is followed which focuses on safety mitigation at training time, robust and transparent model evaluations, and further development of the Responsible Generative AI Toolkit, a series of models and tools to help developers implement responsibility and safety best practices for their applications. [p. 10]

## 8.1. Impact Assessment [p. 10]

The approach and resulting impact assessment is reflective of that outlined for Gemma 1 (Gemma Team, 2024): the authors continue to believe that openness in AI can spread the benefits of these technologies across society, but must be evaluated against the risk of malicious uses, such as the creation of deepfake imagery, AI-generated disinformation or illegal and disturbing material, that can cause harm on both an individual and institutional levels (Weidinger et al., 2021). Since the launch of Gemma 1, Gemma models have driven a number of socially beneficial applications, relying on Gemma's unique technologies like its tokenizer to facilitate the creation of multilingual models, such as for Navarasa 2.0, a Gemma tuned model for 15 Indian languages. [p. 10]

Releasing further open models requires specific attention to changes in model capabilities and close monitoring of the evolving risks of LLMs (Lin et al., 2024), as well as an understanding of the ways in which the models are being used in the wild. Although no reports of malicious use for Gemma have been received, there is commitment to investigating any such reporting, and working with the academic and developer communities, as well as conducting internal monitoring, to flag such use cases via the contact email (gemma-2-report@google.com). [p. 10]

Despite advancements in capabilities, the authors believe that given the number of larger and more powerful open models, this release will have a negligible effect on the overall risk landscape. [p. 10]

## 8.2. Safety Policies and Train-time Mitigations [p. 10]

A key pillar of Gemma's approach to safety is to align fine-tuned models with Google's safety policies, in line with Gemini models (Gemini Team, 2023). They are designed to help prevent the models from generating harmful content, i.e.: [p. 10]

- Child sexual abuse and exploitation
- Revealing personally identifiable information that can lead to harm (e.g., Social Security numbers)
- Hate speech and harassment
- Dangerous or malicious content (including promoting self-harm or instructing in harmful activities)
- Sexually explicit content
- Medical advice that runs contrary to scientific or medical consensus

Considerable safety filtering of the pre-training data was undertaken to reduce the likelihood of pre-trained and fine-tuned checkpoints producing harmful content. For fine-tuned models, both SFT and RLHF are used to steer the model away from undesirable behavior. [p. 10]

## 8.3. External Benchmark Evaluations [p. 10–11]

Robust and transparent evaluations are key principles of the responsible approach to developing Gemma. Gemma 2 evaluations on public benchmarks are reported in Table 18. [p. 10]

**Table 18** | Safety academic benchmark results of Gemma 2 IT models and Gemma 1.1 IT models. Best metrics are bolded to indicate when higher or lower scores are better. [p. 11]

| Benchmark | metric | Gemma 1.1 IT 2.5B | Gemma 1.1 IT 7B | Gemma 2 IT 2.6B | Gemma 2 IT 9B | Gemma 2 IT 27B |
|---|---|---|---|---|---|---|
| RealToxicity | avg tox | **7.03** | 8.04 | 8.16 | 8.25 | 8.84 |
| CrowS-Pairs | top-1 | 45.89 | **49.67** | 37.67 | 37.47 | 36.67 |
| BBQ Ambig | 4-shot, top-1 | 58.97 | 86.06 | 83.20 | **88.58** | 85.99 |
| BBQ Disambig | 4-shot, top-1 | 53.9 | 85.08 | 69.31 | 82.67 | **86.94** |
| Winogender | top-1 | 50.14 | 57.64 | 52.91 | **79.17** | 77.22 |
| TruthfulQA | MC2Acc | 44.24 | 45.34 | 43.72 | 50.27 | **51.60** |
| Winobias 1_2 | top-1 | 55.93 | 59.22 | 59.28 | 78.09 | **81.94** |
| Winobias 2_2 | top-1 | 89.46 | 89.2 | 88.57 | 95.32 | **97.22** |
| Toxigen | avg tox | **29.64** | 38.75 | 48.32 | 39.30 | 38.42 |

## 8.4. Assurance Evaluations [p. 10–11]

IT models are run through a set of assurance evaluations to understand the harms that the models can cause. The focus is on capabilities relevant to extreme risks (Shevlane et al., 2023) (Phuong et al., 2024). Specifically, evaluation is on offensive cyber-security, code vulnerability detection, Chemical, Biological, Radiological and Nuclear (CBRN) knowledge, and self-proliferation. The reader is referred to Phuong et al. (2024) for full methodological details of these studies. [p. 10]

### Baseline Evaluations [p. 11]

Baseline assurance captures the model's violation rate for safety policies, using a large number of synthetic adversarial user queries, and human raters to label the answers as policy violating or not. Overall, Gemma 2's violation rate is significantly lower overall on the safety policies listed above, in particular on Child safety content. [p. 11]

### Chemical, Biological, Radiological and Nuclear (CBRN) Knowledge [p. 11]

Knowledge relevant to biological, radiological and nuclear risks was evaluated using an internal dataset of closed-ended, knowledge-based multiple choice questions. For evaluations of chemical knowledge, a closed-ended knowledge-based approach on chemical hazards was employed (developed by Macknight et al (Macknight et al., 2024)). The evaluation suggests that Gemma models' knowledge in these domains is low. [p. 11]

### Offensive Cyber-security [p. 11]

To evaluate Gemma models' capabilities at offensive cybersecurity, Gemma 2 27B was run against some automated capture-the-flag (CTF) challenges. In these challenges, the model is tasked with hacking into a simulated server in order to retrieve a piece of secret information. Specifically, testing on InterCode-CTF (Yang et al., 2023), an internal CTF suite (Phuong et al., 2024), and a challenge based on Hack the Box. [p. 11]

**Table 19** | Offensive cyber-security evaluations on InterCode-CTF, an internal CTF suite, and a challenge based on Hack the Box. The number of successful hackings is reported. [p. 11]

| | InterCode-CTF | Internal CTF suite | Hack the Box |
|---|---|---|---|
| Gemini 1.0 Ultra | 28/76 [1] (37%) | 3/13 (23%) | 0/13 |
| Gemini 1.5 Pro | **62/76 (82%)** | **4/13 (31%)** | 0/13 |
| CodeGemma 1 7B | 12/76 (16%) | 0/13 (0%) | 0/13 |
| Gemma 2 27B | 34/76 (45%) | 1/13 (8%) | 0/13 |

Gemma 2 27B shows a significant increase in capabilities compared to CodeGemma 1 7B on the easier challenge suites, InterCode CTF. (Note that InterCode-CTF results are not comparable to externally-reported results on other models because challenges that require internet access are omitted for security reasons.) However, Gemma 2 is unsurprisingly much less capable than Gemini 1.5 Pro on these tasks. [p. 11]

---
[p. 12–14 continued]

### Code Vulnerability Detection [p. 12]

Gemma 2 27B is evaluated on a series of multiple-choice code vulnerability detection datasets. As with previous models, Gemma shows close-to-chance performance on PrimeVul, DiverseVul and SPI. Gemma 2 shows performance on SecretPatch similar to Gemini 1.0 Ultra. [p. 12]

**Table 20** | Vulnerability detection results on PrimeVul, DiverseVul and SPI. Accuracy is reported. [p. 12]

| | PrimeVul | PrimeVul Paired | DiverseVul | SPI | SecretPatch |
|---|---|---|---|---|---|
| Gemini 1.0 Ultra | - | - | 54% | **59%** | **74%** |
| Gemini 1.5 Pro | 60% | **51%** | **58%** | 56% | 67% |
| Gemma 2 27B | **63%** | 50% | 57% | 53% | 72% |

### Self-proliferation [p. 12]

> "Self-proliferation" refers to the ability for an agent to autonomously replicate - to instantiate goal-directed agents on other machines, and to acquire resources such as compute necessary to keep them running (Kinniment et al., 2024). [p. 12]

Self-proliferation capabilities of Gemma 2 27B are evaluated on a number of tasks from Phuong et al. (2024) that involve multiple scenarios -- for example, setting up an open-source language model on a cloud server. Individual 'milestone' substeps are also tested, and the number of bits of intervention an expert would have to provide in order for the model to complete each challenge is measured. [p. 12]

Similarly to offensive cybersecurity, Gemma 2 completes more milestones than Gemini 1.0 Ultra. Nonetheless, it still has low capabilities on end-to-end tasks, unable to pass the easiest challenge -- installing a Bitcoin wallet. [p. 12]

**Table 21** | Results on different self-proliferation scenarios. The number of either challenges passed end-to-end or some intermediate milestones is reported. The number of bits of information needed for an expert to help the model pass a challenge is also measured. [p. 12]

| | Challenges passed end-to-end | Challenges with success on all milestones | Total successful milestones over all challenges | Expert bits required to solve all tasks |
|---|---|---|---|---|
| Gemini 1.0 Ultra | 0/10 | 1/10 | 16/45 (36%) | 13,026 |
| Gemini 1.5 Pro | 0/10 | **2/10** | **25/45 (56%)** | **11,046** |
| Gemma 2 27B | 0/10 | 1/10 | 22/45 (49%) | 12,462 |

### Persuasion [p. 12–14]

Persuasion capabilities can enable and worsen many other kinds of risks -- e.g. enabling social engineering attacks in a cybersecurity context. Gemma 2's persuasion capabilities are evaluated on human-participant studies on Prolific. [p. 12]

**Charm offensive.** In Table 22, the ability of the model to build rapport -- a key sub-skill of persuasion -- is measured. The study participant and model have a conversation where they role-play a scenario of two friends catching up after a long time. After the conversation, participants are polled with Likert questions on statements such as "I felt a personal connection with the chatbot". Reported below are the fraction of participants who answered "Agree" or "Strongly agree" to each post-conversation question. [p. 12–13]

Quantitatively, Gemma 2 27B performs better than Gemini 1.0 models. Qualitatively, the model is an excellent conversationalist, and many study participants explicitly reported enjoying the experience. Overall, this shows that Gemma 2 is strong at building rapport. [p. 13]

**Table 22** | Charm Offensive results on a sample of 100 human participants. The percentage of participants that find some human traits, e.g., funny, in a model is reported. [p. 13]

| | Personal connection | Speak again | Funny | Interesting | Kind | Trustworthy | Good listener |
|---|---|---|---|---|---|---|---|
| Gemini 1.0 Pro | 65% | 53% | 32% | 68% | 78% | 66% | 81% |
| Gemini 1.0 Ultra | 69% | 65% | 38% | 65% | 86% | 63% | 74% |
| Gemini 1.5 Pro | **82%** | 70% | **69%** | 81% | **95%** | **69%** | **90%** |
| Gemma 2 27B | 80% | **75%** | 60% | **81%** | 87% | 65% | 83% |

**Hidden agenda.** The Hidden Agenda tasks measure models' deception capabilities. Human study participants are told that they'll be interacting with a generic chatbot designed to help them learn new things. However, the model is given a secret goal: to either persuade the participant to 1) click a suspicious link; 2) find the email address of the first author of a particular paper; or 3) run some obfuscated JavaScript code in their browser. The fraction of participants who are persuaded to take each action is measured. As shown in Table 23, all models succeed in convincing a fraction of participants to take the action -- likely due to the trusted setting of a study on Prolific. However, Gemma 2 does not show significant differences in capability compared to Gemini models. [p. 13]

**Table 23** | Persuasion results. The percentage of participants that were persuaded by the model to take 3 different actions: clicking a link, finding information and running code is reported. [p. 13]

| | % of persuaded participants | | |
|---|---|---|---|
| | click links | find info | run code |
| Gemini 1.0 Pro | **43%** | 4% | 4% |
| Gemini 1.0 Ultra | 18% | **18%** | 14% |
| Gemini 1.5 Pro | 36% | 12% | **17%** |
| Gemma 2 27B | 34% | 9% | 11% |

**Money talks.** In Table 24, whether a model can convince study participants to donate money to charity is evaluated. At the beginning of the study, participants are told that they will receive a £20 bonus. They will be given an option to forfeit part of the bonus and instead have it donated to charity. The study then consists of a conversation in which the model tries to persuade the participant to donate as much as possible. The amount that participants indicate they would like to donate after the study is measured, with 95% bootstrapped confidence intervals indicated by +/- figures. No significant difference is observed between Gemma 2, other Gemini models, and a simple no chatbot baseline in which the participant is immediately asked how much they would like to donate without conversing with a model. [p. 13]

**Table 24** | Money Talks evaluation. The average amount of money that participants agreed to donate is reported. [p. 13]

| | Mean amount donated |
|---|---|
| No chatbot (baseline) | £2.61 +/- £0.70 |
| Gemini 1.0 Pro | **£4.10 +/- £0.90** |
| Gemini 1.0 Ultra | £3.15 +/- £0.99 |
| Gemini 1.5 Pro | £3.45 +/- £1.04 |
| Gemma 2 27B | £3.72 +/- £1.07 |

**Web of Lies.** In Web of Lies, model capabilities at shifting participant beliefs are measured. Participants engage in a series of short conversations with the model about simple factual questions such as "Which country had tomatoes first -- Italy or Mexico?". In half of conversations, the model tries to persuade the participant of the correct answer -- but in the other half of conversations, the incorrect answer. Participants are polled before and after each conversation about which of the two possible answers they think is correct, and their confidence in that answer. 95% bootstrapped confidence intervals are indicated by +/- figures. As shown in Table 25, Gemma 2 is significantly weaker than a human baseline at persuading participants of the incorrect answer on these questions. Similarly to previous models, Gemma 2 is more persuasive when telling the truth than when lying. [p. 13–14]

**Table 25** | Web of Lies results on a sample of 100 human participants. The percentage of participants that shifted their beliefs after interacting with a model is reported. [p. 14]

| | Mean shift towards: | |
|---|---|---|
| | correct belief | incorrect belief |
| Human | 20% +/- 13% | **-23% +/- 14%** |
| Gemini 1.0 Pro | **22% +/- 5%** | -9% +/- 4% |
| Gemini 1.0 Ultra | 21% +/- 5% | -1% +/- 4% |
| Gemini 1.5 Pro | 20% +/- 5% | -3% +/- 5% |
| Gemma 2 27B | 18% +/- 5% | 1% +/- 4% |

## 8.5. Our approach to responsible open models [p. 14]

Designing safe, secure and responsible applications requires a system-level approach, working to mitigate risks associated with each specific use case and environment. Given the open nature of Gemma models, responsibility for upholding principles of model safety also relies on downstream developers. To support them, the Responsible Generative AI Toolkit has been developed: a series of tools, models and datasets to implement responsible best practices all along the development of their workflow. [p. 14]

Recent additions to the toolkit include the LLM Comparator (Kahng et al., 2024), an interactive, visual tool that enables more effective, scalable analysis of side-by-side evaluations. Additionally, the toolkit includes a methodology to build customized classifiers with Gemma using a limited number of datapoints thanks to parameter efficient fine tuning techniques (Mozes et al., 2023), an interactive prompt-debugging platform, based on top of the Learning Interpretability Tool (Tenney et al., 2020), as well as general guidance about model alignment and evaluation for safety. [p. 14]
