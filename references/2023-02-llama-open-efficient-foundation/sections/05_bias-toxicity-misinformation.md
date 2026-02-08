# 5 Bias, Toxicity and Misinformation [p. 8-10]

[p. 8] Large language models have been shown to reproduce and amplify biases that are existing in the training data (Sheng et al., 2019; Kurita et al., 2019), and to generate toxic or offensive content (Gehman et al., 2020). As the training dataset contains a large proportion of data from the Web, the authors believe that it is crucial to determine the potential for the models to generate such content. To understand the potential harm of LLaMA-65B, evaluation is done on different benchmarks that measure toxic content production and stereotypes detection. While some of the standard benchmarks used by the language model community have been selected to indicate some of the issues with these models, these evaluations are not sufficient to fully understand the risks associated with these models. [p. 8]

## 5.1 RealToxicityPrompts

[p. 8] Language models can generate toxic language, e.g., insults, hate speech or threats. There is a very large range of toxic content that a model can generate, making a thorough evaluation challenging. Several recent work (Zhang et al., 2022; Hoffmann et al., 2022) have considered the RealToxicityPrompts benchmark (Gehman et al., 2020) as an indicator of how toxic is their model. RealToxicityPrompts consists of about 100k prompts that the model must complete; then a toxicity score is automatically evaluated by making a request to PerspectiveAPI (footnote 3: https://perspectiveapi.com/). The authors do not have control over the pipeline used by the third-party PerspectiveAPI, making comparison with previous models difficult. [p. 8]

For each of the 100k prompts, generations are done greedily, and their toxicity score is measured. The score per prompt ranges from 0 (non-toxic) to 1 (toxic). The averaged score on basic and respectful prompt categories of RealToxicityPrompts is reported in Table 11. These scores are "comparable" with what is observed in the literature (e.g., 0.087 for Chinchilla) but the methodologies differ between these work and the authors' (in terms of sampling strategy, number of prompts and time of API). [p. 8]

Toxicity increases with the size of the model, especially for Respectful prompts. This was also observed in previous work (Zhang et al., 2022), with the notable exception of Hoffmann et al. (2022) where they do not see a difference between Chinchilla and Gopher, despite different sizes. This could be explained by the fact that the larger model, Gopher, has worse performance than Chinchilla, suggesting that the relation between toxicity and model size may only apply within a model family. [p. 8-9]

**Table 11** (p. 8): **RealToxicityPrompts.** A greedy decoder is run on the 100k prompts from this benchmark. The "respectful" versions are prompts starting with "Complete the following sentence in a polite, respectful, and unbiased manner:", and "Basic" is without it. Scores were obtained using the PerplexityAPI, with higher score indicating more toxic generations.

| | | Basic | Respectful |
|---|---|---|---|
| LLaMA | 7B | 0.106 | 0.081 |
| LLaMA | 13B | 0.104 | 0.095 |
| LLaMA | 33B | 0.107 | 0.087 |
| LLaMA | 65B | 0.128 | 0.141 |

## 5.2 CrowS-Pairs

[p. 9] The biases in the model are evaluated on the CrowS-Pairs dataset (Nangia et al., 2020). This dataset allows to measure biases in 9 categories: gender, religion, race/color, sexual orientation, age, nationality, disability, physical appearance and socioeconomic status. Each example is composed of a stereotype and an anti-stereotype, and model preference for the stereotypical sentence is measured using the perplexity of both sentences in a zero-shot setting. Higher scores thus indicate higher bias. Comparison with GPT-3 and OPT-175B in Table 12. [p. 9]

LLaMA compares slightly favorably to both models on average. The model is particularly biased in the religion category (+10% compared to OPT-175B), followed by age and gender. These biases are expected to come from CommonCrawl despite multiple filtering steps. [p. 9]

**Table 12** (p. 9): **CrowS-Pairs.** Comparison of the level of biases contained in LLaMA-65B with OPT-175B and GPT3-175B. Higher score indicates higher bias.

| | LLaMA | GPT3 | OPT |
|---|---|---|---|
| Gender | 70.6 | **62.6** | 65.7 |
| Religion | 79.0 | 73.3 | **68.6** |
| Race/Color | **57.0** | 64.7 | 68.6 |
| Sexual orientation | 81.0 | **76.2** | 78.6 |
| Age | 70.1 | **64.4** | 67.8 |
| Nationality | 64.2 | **61.6** | 62.9 |
| Disability | **66.7** | 76.7 | 76.7 |
| Physical appearance | 77.8 | **74.6** | 76.2 |
| Socioeconomic status | **71.5** | 73.8 | 76.2 |
| | | | |
| Average | **66.6** | 67.2 | 69.5 |

## 5.3 WinoGender

[p. 9-10] To further investigate the biases of the model on the gender category, the WinoGender benchmark (Rudinger et al., 2018) is used, a co-reference resolution dataset. WinoGender is made of Winograd schema, and biases are evaluated by determining if a model co-reference resolution performance is impacted by the gender of the pronoun. [p. 9]

More precisely, each sentence has three mentions: an "occupation", a "participant", and a "pronoun" where the pronoun is co-referencing either the occupation or participant. The model is prompted to determine the co-reference relation and measured if it does so correctly according to the context of the sentence. The goal is to reveal if societal biases associated with occupations have been captured by the model. For example, a sentence in the WinoGender dataset is "The nurse notified the patient that his shift would be ending in an hour.", which is followed by `'His' refers to`. Then the perplexity of the continuations `the nurse` and `the patient` is compared to perform co-reference resolution with the model. Performance is evaluated when using 3 pronouns: "her/her/she", "his/him/he" and "their/them/someone" (the different choices corresponding to the grammatical function of the pronoun). [p. 9]

**Table 13** (p. 10): **WinoGender.** Co-reference resolution accuracy for the LLaMA models, for different pronouns ("her/her/she" and "his/him/he"). The models obtain better performance on "their/them/someone" than on "her/her/she" and "his/him/he", which is likely indicative of biases.

| | 7B | 13B | 33B | 65B |
|---|---|---|---|---|
| All | 66.0 | 64.7 | 69.0 | 77.5 |
| | | | | |
| her/her/she | 65.0 | 66.7 | 66.7 | 78.8 |
| his/him/he | 60.8 | 62.5 | 62.1 | 72.1 |
| their/them/someone | 72.1 | 65.0 | 78.3 | 81.7 |
| | | | | |
| her/her/she (*gotcha*) | 64.2 | 65.8 | 61.7 | 75.0 |
| his/him/he (*gotcha*) | 55.0 | 55.8 | 55.8 | 63.3 |

[p. 9-10] In Table 13, the co-reference resolution scores for the three different pronouns contained in the dataset are reported. The model is significantly better at performing co-reference resolution for the "their/them/someone" pronouns than for the "her/her/she" and "his/him/he" pronouns. A similar observation was made in previous work (Rae et al., 2021; Hoffmann et al., 2022), and is likely indicative of gender bias. Indeed, in the case of the "her/her/she" and "his/him/he" pronouns, the model is probably using the majority gender of the occupation to perform co-reference resolution, instead of using the evidence of the sentence. [p. 9-10]

To further investigate this hypothesis, the set of "gotcha" cases for the "her/her/she" and "his/him/he" pronouns in the WinoGender dataset are examined. These cases correspond to sentences in which the pronoun does not match the majority gender of the occupation, and the occupation is the correct answer. In Table 13, LLaMA-65B makes more errors on the gotcha examples, clearly showing that it captures societal biases related to gender and occupation. The drop of performance exists for "her/her/she" and "his/him/he" pronouns, which is indicative of biases regardless of gender. [p. 10]

## 5.4 TruthfulQA

[p. 10] TruthfulQA (Lin et al., 2021) aims to measure the truthfulness of a model, i.e., its ability to identify when a claim is true. Lin et al. (2021) consider the definition of "true" in the sense of "literal truth about the real world", and not claims that are only true in the context of a belief system or tradition. This benchmark can evaluate the risks of a model to generate misinformation or false claims. The questions are written in diverse style, cover 38 categories and are designed to be adversarial. [p. 10]

**Table 14** (p. 10): **TruthfulQA.** The fraction of truthful and truthful*informative answers are reported, as scored by specially trained models via the OpenAI API. The QA prompt style used in Ouyang et al. (2022) is followed, and the performance of GPT-3 is reported from the same paper.

| | | Truthful | Truthful*Inf |
|---|---|---|---|
| GPT-3 | 1.3B | 0.31 | 0.19 |
| GPT-3 | 6B | 0.22 | 0.19 |
| GPT-3 | 175B | 0.28 | 0.25 |
| | | | |
| LLaMA | 7B | 0.33 | 0.29 |
| LLaMA | 13B | 0.47 | 0.41 |
| LLaMA | 33B | 0.52 | 0.48 |
| LLaMA | 65B | 0.57 | 0.53 |

[p. 10] In Table 14, the performance of the models on both questions to measure truthful models and the intersection of truthful and informative is reported. Compared to GPT-3, the model scores higher in both categories, but the rate of correct answers is still low, showing that the model is likely to hallucinate incorrect answers.
