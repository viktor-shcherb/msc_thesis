# 6. Core Capability Evaluations [p. 28–31]

[p. 28] The final component of the evaluation harness for the Gemini 1.5 Pro and Gemini 1.5 Flash measures the quality of the models' core capabilities (i.e., performance on non long-context tasks). The evaluations in this section consist of benchmarks covering all three modalities: text, vision and audio. The authors rely on a combination of established benchmarks that are public and used by the community along with some internal benchmarks that are held-out and unleaked. The selection criteria primarily aim to measure the improvement of Gemini 1.5 series compared to its predecessor, Gemini 1.0 series of models: Gemini 1.0 Pro and Gemini 1.0 Ultra. The goal is to highlight the extent of the trade-off, if it exists, between the 1.5 generation of Gemini models that excel in long-context capabilities and their performance on non long-context tasks. In particular, as the authors develop the 1.5 series, they aim to enhance the models' proficiency in this new dimension of multimodal long-context without compromising their quality across all other capabilities. [p. 28]

[p. 28–29] All in all, a clear generational improvement is found between the 1.0 and 1.5 series, with Gemini 1.5 Pro uniformly outperforming 1.0 Pro and approaching (often even surpassing) 1.0 Ultra, a state-of-the-art model on most benchmarks, despite being significantly more efficient to train. An outlier to this picture is the situation on the audio capability. The post-training data of the model contains 5 head languages, resulting thus in slight regressions on multi-lingual datasets that are not head heavy (e.g., YouTube, FLEURS and Covost 2). [p. 29]

**Table 10** (p. 29): Detailed breakdown of the results presented in Table 1. * In speech recognition, it is generally accepted that any difference in Word Error Rate (WER) that falls within a 3% relative range is not statistically significant and can be considered as mere noise, and the authors grouped such instances as wins for the latest systems.

| Core Capability | | 1.5 Pro Relative to | | 1.5 Flash Relative to | |
|---|---|---|---|---|---|
| | **1.5 Pro (Feb)** | **1.0 Pro** | **1.0 Ultra** | **1.0 Pro** | **1.0 Ultra** |
| **Text** | | | | | |
| Math, Science & Reasoning | +5.9% | +49.6% | +18.1% | +30.8% | +4.1% |
| Multilinguality | -0.7% | +21.4% | +5.9% | +16.7% | +2.1% |
| Coding | +11.6% | +21.5% | +11.7% | +10.3% | +1.5% |
| Instruction following | — | +9.9% | -0.2% | +8.7% | -1.2% |
| Function calling | — | +72.8% | — | +54.6% | — |
| **Vision** | | | | | |
| Multimodal reasoning | +15.5% | +31.5% | +14.8% | +15.6% | +1.0% |
| Charts & Documents | +8.8% | +63.9% | +39.6% | +35.9% | +17.9% |
| Natural images | +8.3% | +21.7% | +8.1% | +18.9% | +5.6% |
| Video understanding | -0.3% | +18.7% | +2.1% | +7.5% | -8.1% |
| **Audio** | | | | | |
| Speech recognition* | +1.0% | +2.2% | -3.8% | -17.9% | -25.5% |
| Speech translation | -1.7% | -1.5% | -3.9% | -9.8% | -11.9% |

## 6.1. Core Text Evals

[p. 29] The authors start by evaluating Gemini models' performance on seven major core text capabilities: (1) Math and Science (Section 6.1.1); (2) General reasoning (Section 6.1.2), (3) Coding (Section 6.1.3); (4) Multilinguality (Section 6.1.4); (5) Function calling (Section 6.1.5); (6) Instruction Following (Section 6.1.6); and (7) Real-world and expert long-tail GenAI tasks (Section 6.1.7). See Table 11 for a summary of these results; see the Appendix for details on each, and an additional evaluation on QA for Web Search Topics. [p. 29]

[p. 29] With web-scale pretraining of language models, decontamination of public benchmarks is a persistent challenge (Brown et al., 2020; Gemini-Team et al., 2023; OpenAI, 2023a). Gemini 1.5 employed standard n-gram based decontamination procedures to help mitigate this issue, however these n-gram based procedures are imperfect. To move beyond the reliance on training set decontamination, the authors also report performance on internally developed non-public evals, such as PhysicsFinals, HiddenMath, and Natural2Code. [p. 29]

**Table 11** (p. 30): Evaluation results of Gemini 1.5 Pro, 1.5 Flash and Gemini 1.0 models on standard coding, multilingual as well as math, science and reasoning benchmarks. Unless explicitly specified, all tasks are evaluated in terms of answer accuracy. Note that in this table, PT for the 1.0 Ultra and Pro models denote tasks evaluated with model variants that have undergone a post-training (i.e. instruction-tuning) phase after pre-training. All numbers for the 1.5 Pro and 1.5 Flash are obtained after instruction-tuning except for the ones marked with * which come from pretrained models, as described in Section 4.

| Capability | Benchmark | 1.0 Pro | 1.0 Ultra | 1.5 Flash | 1.5 Pro |
|---|---|---|---|---|---|
| Math and Science | **GPQA:** Graduate-Level Google-Proof Q&A. (Rein et al., 2023) | 27.9% 4-shot | 35.7% 4-shot | 39.5% 0-shot | **46.2%** 0-shot |
| Math and Science | **MATH:** Math problems ranging across 5 levels of difficulty and 7 sub-disciplines. (Hendrycks et al., 2021b) | 32.6% 4-shot Minerva prompt | 53.2% 4-shot Minerva prompt | 54.9% 4-shot Minerva prompt | **67.7%** 4-shot Minerva prompt |
| Math and Science | | — | — | — | 77.9%* maj@64 |
| Math and Science | **PhysicsFinals:** 61 undergraduate physics problems that have not appeared on the internet. | 31.1% 0-shot | 41.0% 0-shot | 57.4% 0-shot | **63.9%** 0-shot |
| Math and Science | **HiddenMath:** 179 new math problems created from scratch. | 6.1% 0-shot | 11.2% 0-shot | 6.7% 0-shot | **20.1%** 0-shot |
| Math and Science | **Functional MATH:** Functional variant of 1745 MATH problems (December snapshot) | 39.9% 0-shot | 55.8% 0-shot | 53.6% 0-shot | **64.6%** 0-shot |
| Math and Science | **AMC 2022-23:** 250 latest problems including 100 AMC 12, 100 AMC 10, and 50 AMC 8 problems. | 22.8% 4-shot | 30% 4-shot | 34.8% 4-shot | **46.4%** 4-shot |
| Math and Science | **GSM8K:** Grade-school math problems. (Cobbe et al., 2021) | 77.9% 11-shot | 88.9% 11-shot | 86.2% 11-shot | **90.8%** 11-shot |
| Math and Science | **BigBench - Hard:** A subset of harder tasks from Big Bench. (Srivastava et al., 2022; Suzgun et al., 2022) | 75.0% 3-shot | 83.6% 3-shot | 85.5% 3-shot | **89.2%** 3-shot |
| General Reasoning | **DROP:** Reading comprehension & arithmetic. (Metric: F1-Score). (Dua et al., 2019) | 74.1 Variable shots | **82.4** Variable shots | 78.4 Variable shots | 74.9 Variable shots |
| General Reasoning | **MMLU:** Multiple-choice questions in 57 subjects (professional & academic). (Hendrycks et al., 2021a) | 71.8% 5-shot | 83.7% 5-shot | 78.9% 5-shot | **85.9%** 5-shot |
| General Reasoning | | — | 90.0%* maj@32 | — | 91.7%* maj@32 |
| General Reasoning | **Hellaswag** (Zellers et al., 2019) | 84.7% 10-shot | 87.8% 10-shot | 86.5% 10-shot | **93.3%** 10-shot |
| General Reasoning | **HumanEval** chat preamble* (Metric: pass rate). (Chen et al., 2021) | 67.7% 0-shot (PT) | 74.4% 0-shot (PT) | 74.3% 0-shot | **84.1%** 0-shot |
| Coding | **Natural2Code** chat preamble* (Metric: pass rate). | 69.6% 0-shot | 74.9% 0-shot | 77.2% 0-shot | **82.6%** 0-shot |
| Multilinguality | **WMT23:** sentence-level machine translation (Metric: BLEURT). (Tom et al., 2023) | 71.7 1-shot (PT) | 74.4 1-shot (PT) | 74.1 1-shot | **75.3** 1-shot |
| Multilinguality | **MGSM:** multilingual math reasoning. (Shi et al., 2023a) | 63.5% 8-shot (PT) | 79.0% 8-shot | 82.6% 8-shot | **87.5%** 8-shot |

## 6.1.1. Math and Science

[p. 29–31] The authors find that 1.5 Pro consistently outperforms both 1.0 Ultra and 1.0 Pro on grade-school math (i.e., GSM8K) and even shows material improvement over the more demanding benchmarks where there is more headroom for improvement, i.e., +14.5% over 1.0 Ultra for middle- and high-school math problems (i.e., Hendrycks MATH), +13.2% for the American Mathematical Competitions (i.e., AMC 2022-23), and +5.8% on graduate-level science problems (i.e., GPQA (Rein et al., 2023)).^21 [p. 29, 31]

[p. 31] Gemini 1.5 Flash demonstrates significant improvements over the 1.0 Pro version, achieving an 11.6% increase on GPQA, a 22.3% increase on middle- and high-school math problems (Hendrycks MATH), a 26.3% increase on undergraduate physics problems (PhysicsFinals), a 0.6% increase on HiddenMath problems, an 8.4% increase on AMC problems, and an 8.3% increase on Grade School Math problems. [p. 31]

### Functional MATH

[p. 31] Functional MATH (Srivastava et al., 2024), a new benchmark derived from the MATH dataset, comprises 1,745 problems in both original and modified forms. The benchmark aims to evaluate a model's ability to solve modified problems compared to its performance on the original versions. The "Reasoning Gap", defined as the relative decrease in performance between original and modified problems, serves as a novel metric for assessing generalization capability. It quantifies a model's adaptability to modifications of problems previously published online, specifically those introduced after the training data cut-off date. As modifications often lead to problems of increased computational complexity, a performance gap is expected. The Functional MATH dataset provides a means to control and analyze the magnitude of this gap across different models. The authors specifically chose to utilize the December snapshot of Functional MATH. The evaluation prioritizes both overall performance on the modified problem set and minimization of the Reasoning Gap. The models are tested in a zero-shot setting without any accompanying context or instructions. [p. 31]

The automated evaluation process consisted of two steps. First, the Gemini 1.0 Pro model is used to extract the proposed final answer from the model's output, and then this answer is compared to the ground truth using the same programmatic heuristic as employed in evaluations of the MATH dataset. [p. 31]

- Gemini 1.0 Pro solved 55.8% of the original problems and 39.9% of the modified problems (reasoning gap = 28.5%).
- Gemini 1.5 Flash solved 69.7% of the original problems and 53.6% of the modified problems (reasoning gap = 23.1%).
- Gemini Ultra 1.0 solved 74.5% of the original problems, 55.8% of the modified problems (reasoning gap = 25.1%).
- Gemini 1.5 Pro solved 81.1% and 64.6% (reasoning gap = 20.3%). [p. 31]

### PhysicsFinals and HiddenMath

[p. 31] Gemini 1.5 Pro is also evaluated on two new, unreleased internal benchmarks: PhysicsFinals and HiddenMath.

**PhysicsFinals** comprises 61 undergraduate physics problems, curated by a group of physics professors for offline final exams, covering topics such as wave mechanics, quantum mechanics, special relativity, and introductory general relativity. Answers were graded by a physics professor. Gemini 1.5 Pro achieved a score of 39, significantly surpassing Gemini 1.0 Ultra (25) and Gemini 1.0 Pro (19). [p. 31]

**HiddenMath** comprises 179 competition-level math problems, crafted by experts and evaluated automatically. Gemini 1.0 Pro solved 11 problems, Gemini 1.5 Flash solved 12, Gemini 1.0 Ultra solved 20, and Gemini 1.5 Pro solved 36. [p. 31]

Section 7 presents additional results obtained with a Math-Specialized Gemini 1.5 Pro. [p. 31]

> ^21 In Appendix 12.6, the authors analyze the impact of long-context prompting on the performance of Gemini 1.5 Pro on a selection of 528 challenging problems from Hendrycks MATH (Level 4 and 5 Intermediate Algebra problems). [p. 31]

## 6.1.2. General Reasoning

[p. 31–32] BigBench-Hard, DROP, MMLU, and Hellaswag are benchmarks designed to assess a model's ability to handle complex relationships within text, perform multi-step reasoning, and apply common sense knowledge to novel situations. BigBench-Hard, a curated subset of challenging tasks from the broader BigBench suite, requires models to engage in intricate reasoning processes. Gemini 1.5 Pro achieves a state-of-the-art score of 89.2% on this benchmark. MMLU, encompassing a diverse range of 57 subjects across professional and academic domains, sees Gemini 1.0 Ultra, 1.5 Pro, and 1.5 Flash all exceeding 80%. Hellaswag, a benchmark designed to test common sense reasoning and the ability to distinguish plausible scenarios, sees Gemini 1.5 Pro achieving 93.3%. A similar strong performance is observed for Gemini 1.5 Flash, with the model outperforming Gemini 1.0 Pro. [p. 31–32]

## 6.1.3. Code

[p. 32] Gemini 1.5 Pro is the best performing model in code to date, surpassing Gemini 1.0 Ultra on HumanEval and Natural2Code, the internal held-out code generation test set made to prevent web-leakage. The same gains are transferred to Gemini 1.5 Flash with the model outperforming Gemini Ultra 1.0. [p. 32]

### HumanEval leakage

[p. 32] HumanEval is an industry standard open-source evaluation benchmark (Chen et al., 2021), but the authors found controlling for accidental leakage on webpages and open-source code repositories to be a non-trivial task, even with conservative filtering heuristics. An analysis of the test data leakage of Gemini 1.0 Ultra showed that continued pre-training on a dataset containing even a single epoch of the test split for HumanEval boosted scores from 74.4% to 89.0%, highlighting the danger of data contamination. This sharp increase persisted even when examples were embedded in extraneous formats (e.g. JSON, HTML). The authors invite researchers assessing coding abilities of these models head-to-head to always maintain a small set of truly held-out test functions that are written in-house, thereby minimizing the risk of leakage. The Natural2Code benchmark, which was announced and used in the evaluation of Gemini 1.0 series of models, was created to fill this gap. It follows the exact same format of HumanEval but with a different set of prompts and tests. [p. 32]

## 6.1.4. Multilinguality

[p. 32] For multilingual evaluations the authors use a multilingual math reasoning (MGSM; Shi et al., 2023a) benchmark and a machine translation benchmark (WMT23; Kocmi et al., 2023) which was constructed after the model's training data cut-off hence minimizing test set leakage risks. Both of these cover diverse languages from different language families and resource groups, with MGSM covering 11 languages and WMT23 eight languages for a total of 14 language pairs. [p. 32]

[p. 32] Gemini 1.5 Pro improves over Gemini 1.0 Ultra on both tasks, particularly showing a substantial improvement of almost +9% on the MGSM dataset, in line with the English-only math improvements reported above. These improvements are not limited to a particular resource group; rather, 1.5 Pro improves performance equally among differently-resourced languages. Particularly, on medium and low resource languages the gap between 1.0 Ultra and 1.5 Pro increases to > 9% and > 7%, respectively.^22 In addition, Gemini 1.5 Flash achieves comparable performance to Gemini 1.0 Ultra on WMT23, and surpasses it by > 3 on MGSM, despite its much smaller size. [p. 32]

> ^22 See Appendix 12.4 for a complete performance breakdown. [p. 32]

## 6.1.5. Function Calling

[p. 32–33] There is an increasing interest in LLMs as the core building block of AI systems (often called agents) that operate in environments to achieve complex goals. Environments may include anything from general web search, private documents or calendars of users, internal enterprise APIs to general programming interpreters and robot sensors. Due to their general-purpose nature, LLMs are expected--and have the promise--to operate in many such environments without having seen them at training time. The authors focus on evaluating this capability via Function Calling (FC), or zero-shot tool use: given the descriptions and type signatures of a set of functions or APIs, and a user prompt, the model has to infer what function calls have to be made to service the prompt, if any. Specifically, they use the Berkeley Function Calling Leaderboard (Yan et al., 2024, BFCL) and focus on a subset of BCFL splits.^23 [p. 32–33]

> ^23 The authors are excluding execution-based evaluations as they were sensitive to 3rd party API availability and Java/JavaScript questions due to concerns around the annotations and metrics. In addition, they corrected various other annotations and metrics of core splits. [p. 33]

**Table 12** (p. 33): Function calling performance on Berkeley Function Calling Leaderboard splits (excluding Java and Javascript, and with various fixes).

| Task | 1.0 Pro | 1.5 Flash | 1.5 Pro |
|---|---|---|---|
| Simple Functions | 92.0% | 88.0% | **92.8%** |
| Multiple Functions | 90.0% | **92.0%** | 90.5% |
| Parallel Functions | 38.5% | 73.5% | **88.5%** |
| Parallel Multiple | 27.0% | 73.5% | **83.5%** |
| Relevance | 67.5% | 75.4% | **83.3%** |
| Weighted Average | 67.8% | 81.8% | **88.4%** |

[p. 33] In Table 12 there is a substantial improvement from Gemini 1.0 Pro to 1.5 Pro in terms of overall weighted accuracy. This can be attributed in large part to the new support for parallel function calling (where one prompt triggers several independent functions) but also to the improved ability of Gemini to determine when not to call functions (cf. "Relevance" column). The 1.5 Flash FC endpoint is found to be extremely close to 1.5 Pro. The authors believe that while this benchmark is useful to test the models' ability to perform simple one-step function calling, it is likely close to saturation and robust metrics and data for multi-step and multi-turn action taking in more complex environments are needed. [p. 33]

## 6.1.6. Instruction Following

[p. 33–34] The authors also evaluate Gemini 1.5 models on instruction following capability, employing a fine-grained evaluation methodology that measures how well models can follow instructions in complex prompts. [p. 33]

[p. 33] Two evaluation sets are used:
1. An internal evaluation set with 1326 prompts constructed by human raters, inspired by real-world use cases. These prompts represent complex user needs e.g., generating formal and creative content, providing recommendations, summarizing, rewriting text, and solving coding and logical problems. They also capture enterprise tasks such as information extraction, data/table understanding, and multi-document summarization. These prompts are long, 307 words on average, with between one to tens of instructions with a mean of about 8.
2. Another set of 406 prompts from human raters that covers varied topics and instruction types, different from the Gemini 1.0 Technical Report (Gemini-Team et al., 2023). These prompts are shorter, 66 words on average, with one to more than a dozen instructions (average count is five). [p. 33]

[p. 33] For evaluation, human annotators were asked to rate whether a response follows (or not) each of the instructions present in the prompt. Two metrics are aggregated from these human judgements: per-instruction accuracy (the percentage of instructions over the full evaluation set that are followed) and full-response accuracy (percentage of prompts where every instruction was followed). [p. 33]

**Table 13** (p. 34): Instruction tuning performance on a) the set of 1326 prompts covering diverse tasks and enterprise domains; longer prompts and larger number of instructions per prompt, and b) set of 406 shorter prompts with fewer instructions.

| | 1.0 Pro | 1.0 Ultra | 1.5 Flash | 1.5 Pro |
|---|---|---|---|---|
| **1326 long prompts** | | | | |
| Per-instruction accuracy | 82.6 ± 0.8 | 88.2 ± 0.6 | 87.9 ± 0.6 | **90.2 ± 0.6** |
| Full-response accuracy | 44.4 ± 2.7 | 53.9 ± 2.7 | 55.0 ± 2.7 | **58.6 ± 2.7** |
| **406 shorter prompts** | | | | |
| Per-instruction accuracy | 87.8 ± 1.5 | **90.7 ± 1.3** | 87.1 ± 1.5 | 85.9 ± 1.6 |
| Full-response accuracy | 63.4 ± 4.7 | **68.4 ± 4.6** | 66.8 ± 4.6 | 64.0 ± 4.7 |

[p. 34] On the set of 1326 long and enterprise prompts: the 1.5 Pro model has 32% improvement in response accuracy from the 1.0 Pro model, by fully following 59% of all the long prompts. Even the smaller 1.5 Flash model has a 24% increase here. At instruction-level, the 1.5 Pro model reaches 90% accuracy. [p. 34]

[p. 34] For the set of 406 shorter prompts, the Gemini 1.5 models follow 86-87% of the diverse instructions. 65% of the prompts were fully followed, performing similar to Gemini 1.0 Pro^24. Note that the 1.0 models compared with here are different from the Gemini Apps models in the 1.0 Technical Report which were specifically post-trained for conversational AI tasks. [p. 34]

> ^24 Refer to the Gemini 1.0 Technical Report for more evaluations of 1.0 models that were post-trained for conversational AI. [p. 34]

## 6.1.7. Real-world and long-tail expert GenAI tasks

[p. 34] The authors note that the most impactful use cases of Generative AI (GenAI) require models to operate on specialized knowledge and skills. Such expertise is challenging for models to learn due to sparse training data. Models must balance memorization and generalization, ensuring sufficient capacity and precision to capture the long tail of knowledge distribution (c.f., GPQA, (Carlini et al., 2022; Rein et al., 2023; Saab et al., 2024)). [p. 34]

[p. 34] The authors perform evaluations to study various such tasks on the long tail of capability and knowledge distribution. In structuring this space, they consider different types of expertise (knowledge vs. skills) which might be encoded in training data or provided as part of the context when it is dynamic or proprietary. Also, provenance of eval sets can vary: they may be constructed according to aspirational distributions, sampled from publicly proposed hard use cases, or sampled on-distribution. [p. 34]

[p. 34] The authors believe that this shift from traditional benchmark datasets provides a more accurate picture of how these models perform in actual data points driven by user needs, giving rise to open-ended questions, creative writing prompts and even opinion-seeking queries.^25 [p. 34]

> ^25 In addition, the authors also evaluated their models on everyday information seeking topics (see Appendix 12.12). [p. 34]

### Expertise QA

[p. 35] In Expertise QA, in-house experts with formal training and experience in various domains (e.g., history, literature, psychology) produced hard, sometimes complex questions (e.g., *As films began using sound for dialogue, how did the changing use of visual metaphor affect the ways audiences expected narratives to develop in movies?* or *How does Vygotsky's theory of internal speech apply across multilingual language acquisition?*). [p. 35]

[p. 35] The same experts then rated and ranked model responses to their respective questions. Models were evaluated according to their ability to answer such questions with a high degree of accuracy, but also, secondarily, completeness and informativeness. The Gemini 1.5 models significantly and strongly outperform 1.0 Pro on this task (see Appendix 12.10.0.1 for ranking results that corroborate these gains). [p. 35]

**Figure 18** (p. 35): "Performance of different models on Expertise QA. 95% confidence intervals via bootstrapping. See the Appendix, Table 52 for the numerical measurements, and Table 53 for side-by-side comparisons."

Bar chart showing "Rate [%]" on y-axis (0–60+) for two groups: "Accurate" and "Severely Inaccurate". For Accurate: 1.0 Pro ~50.0%, 1.0 Ultra ~61.5%, 1.5 Flash ~67.7%, 1.5 Pro ~67.1%. For Severely Inaccurate: 1.0 Pro ~26.7%, 1.0 Ultra ~10.1%, 1.5 Flash ~7.3%, 1.5 Pro ~6.3%. Shows 95% confidence interval error bars on all bars. Supports the claim that Gemini 1.5 models are substantially more accurate and less severely inaccurate than 1.0 Pro. [p. 35]

### Domain-Specific Long-Form Methodical Tasks

[p. 35] The recently introduced DOLOMITES benchmark (Malaviya et al., 2024) captures methodological planning, organizing and writing tasks performed routinely by experts (e.g., a teacher writing a lesson plan for students, a biologist developing a protocol for a toxicity assay). The models are prompted in a zero-shot manner with the task description, the input sections corresponding to an example, and instructed to generate the output sections (see Appendix 12.16.16 for details). An LM-based Automated Evaluation with Claude 3 Opus is used as the judge, an approach that has been shown to have a high correlation with human preferences ((Malaviya et al., 2024), Figure 7). Specifically, they compare side-by-side Gemini responses to GPT-4 Turbo Preview to provide preferences. [p. 35]

**Table 14** (p. 36): Evaluation results of Gemini 1.5 Pro, 1.5 Flash and Gemini 1.0 models on Domain-specific methodical tasks from DOLOMITES benchmark. (Metric: LM-judge win rate).

| 1.0 Pro | 1.0 Ultra | 1.5 Flash | 1.5 Pro |
|---|---|---|---|
| 20.9% | 18.4% | 34.5% | **55.3%** |

[p. 35] Table 14 shows that Gemini 1.5 Pro achieves the highest win-rate of 55.3%. Moreover, both 1.5 Pro and 1.5 Flash significantly improve upon Gemini 1.0 models. [p. 35]

### STEM QA with Context

[p. 35–36] Here the authors evaluate how good their models are on STEM topics, specifically studying how well they can generate accurate text responses that are well-grounded based on a context such as an article. Questions and contexts (i.e., research papers) are drawn from the Qasper dataset (Dasigi et al., 2021). Models are provided with the whole content of an article as context in addition to a question. Human expert STEM then assesses the accuracy of models' responses using the same context provided to the models (i.e., question and research paper). Experiment details are reported in Section 12.11. [p. 35–36]

**Table 15** (p. 36): STEM QA with Context: proportions [%] of accurate and inaccurate sentences in Gemini 1.0 and 1.5 model responses on the Qasper dataset (Dasigi et al., 2021). 95% C.I. obtained by bootstrap.

| | 1.0 Pro | 1.0 Ultra | 1.5 Flash | 1.5 Pro |
|---|---|---|---|---|
| Accurate | 86.9 ± 0.9 | 86.1 ± 1.5 | **91.6 ± 0.6** | 91.1 ± 0.5 |
| Inaccurate | 8.2 ± 0.7 | 9.5 ± 1.1 | 2.2 ± 0.3 | **2.2 ± 0.2** |
| Severely Inaccurate | 7.5 ± 0.7 | 9.0 ± 1.1 | 1.6 ± 0.2 | **1.6 ± 0.2** |

[p. 36] Tables 15 shows that the Gemini 1.5 models all significantly outperform the Gemini 1.0 Pro and Ultra models in this evaluation with 4-5% more accurate and 6-7% fewer inaccurate response sentences (including severe cases). In addition, no significant differences are observed between Gemini 1.5 Flash and Pro on this task, showing that the Gemini 1.5 models are consistently accurate regardless of the model size. [p. 36]

### Hard, externally proposed real-world GenAI use cases

[p. 36] This test presents a novel methodology for evaluating the models by leveraging hundreds of real-world challenging, long-tail, and complex prompt shared on the Internet and various social media. The results in Table 16 show the relative human rater preference for each of the new Gemini 1.5 Flash and Pro models compared to the baseline Gemini 1.0 Pro and Ultra models. The Gemini 1.5 models demonstrate superior performance compared to the 1.0 Pro model, with Gemini 1.5 Pro outperforming even 1.0 Ultra and 1.5 Flash being on par with 1.0 Ultra. [p. 36]

**Table 16** (p. 36): The preference results are presented as win/tie/loss percentages, relative preference of each new Gemini model against Gemini 1.0 Pro and Ultra. There were multiple ratings per prompt by different raters and the order of model responses was randomized on the interface.

| | 1.0 Pro | 1.0 Ultra |
|---|---|---|
| Gemini 1.5 Pro | **59.9%** / 11.4% / 28.7% | **45.7%** / 16.7% / 37.6% |
| Gemini 1.5 Flash | **51.5%** / 13.9% / 34.5% | 38.3% / 22.0% / **39.7%** |

### Productivity Impact of LLMs Across Jobs

[p. 36–38] There is huge potential for LLMs to aid and augment people on routine, time-consuming, or repetitive tasks in the course of their jobs, leading thus to improved productivity. The authors specifically study and measure the productivity improvement that Gemini models bring to tasks from various professions. [p. 36]

**Table 17** (p. 37): Example task from a pre-school teacher (abridged). The prompt describes creating a weekly activities calendar for a preschool class, including choosing a theme, color of the week, animal of the week, snack theme, and designing daily activities and a weekly calendar with a 3-column supply table. Attached documents include a web page with pre-school themes and an image with an example of a weekly pre-school planner. [p. 37]

[p. 37] In previous work, productivity or economic impact was measured in studies that classified jobs based on what current LLMs are able to do with human annotators or classifiers categorizing the tasks in each job as impacted by AI advances (Eloundou et al., 2023; Felten et al., 2018; World Economic Forum, 2023). Here, the authors conduct a practical exercise to evaluate how their models can help people from various industries in their jobs. Specifically, they ask participants to consider typical and complex tasks they do in the course of their jobs. This task description is then given as input to the models together with any other attached material required to complete these tasks (e.g., documents, web pages, spreadsheets, or images). [p. 37]

[p. 37] The 325 prompts collected are rich depictions of user needs in practical settings. Prompts are on average 277 words long, and 78% of them have at least one attachment. Additionally, participants indicate the difficulty of the task in terms of time and effort, and also the job expertise-level needed to complete it. Both these indicators were skewed towards higher complexity.^26 Interestingly, participants estimated that without any AI support, the average time to complete the task was 2.5 hours, indicating that these tasks typically involve significant effort. [p. 37]

> ^26 The average difficulty was 3.4 on a 5 point scale, and expertise was 1.8 average on a 3 point scale. [p. 37]

[p. 37] Raters from the same profession were then presented with model responses and asked to estimate how much time they would save using them as support for their tasks compared to having no AI support. Overall, raters estimated a 56.4% time saving for the prompt set with the 1.5 Pro model, and 27.7% for the 1.0 Pro model. [p. 37]

[p. 37–38] Time savings by job categories are presented in Figure 19. Model responses were rated as saving time across all these jobs, with the 1.5 Pro model emerging stronger than the 1.0 Pro model. The 1.5 Pro model saves 26% time in the architecture domain, and has bigger gains in photography (73%) and programming (75%). As a qualitative measure, raters were also asked to judge the usefulness of the response on a scale from 1 to 5. The average usefulness of 1.5 Pro model responses was 4.0, and 2.7 for the 1.0 Pro model. [p. 37–38]

**Figure 19** (p. 38): "Time saving per industry of completing the tasks with an LLM response compared to without, weighted by the estimated frequency of the task over a year, with 95% confidence intervals."

Bar chart with x-axis listing 10 job categories (Architecture, Childcare, Data Science, Health, Law, Media, Photography, Public Relations, Programming, Teaching) and y-axis showing "Percent time saved (weighted by task frequency)" from 0.0 to 0.8. Two bars per category: blue = Gemini 1.0 Pro, green = Gemini 1.5 Pro. Key data points:
- Architecture: 1.0 Pro 0.11, 1.5 Pro 0.26
- Childcare: 1.0 Pro 0.14, 1.5 Pro 0.44
- Data Science: 1.0 Pro 0.43, 1.5 Pro 0.63
- Health: 1.0 Pro 0.31, 1.5 Pro 0.46
- Law: 1.0 Pro 0.07, 1.5 Pro 0.44
- Media: 1.0 Pro 0.08, 1.5 Pro 0.46
- Photography: 1.0 Pro 0.33, 1.5 Pro 0.73
- Public Relations: 1.0 Pro 0.50, 1.5 Pro 0.53
- Programming: 1.0 Pro 0.31, 1.5 Pro 0.75
- Teaching: 1.0 Pro 0.33, 1.5 Pro 0.69
All bars have 95% confidence interval error bars. Supports the claim that Gemini 1.5 Pro consistently saves more time than 1.0 Pro across all job categories. [p. 38]

[p. 38] To the best of the authors' knowledge, this is the first study to elicit real-world occupation oriented prompts, and examine the usefulness of LLMs to collaborate on these tasks. Overall, the 1.5 Gemini models significantly improve job productivity in multiple domains. The authors envision that these collaborative settings could be further improved using more suitable tools, additional model capabilities, and explanatory behavior. [p. 38]
