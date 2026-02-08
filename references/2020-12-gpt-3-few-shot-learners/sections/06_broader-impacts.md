# 6. Broader Impacts [p. 34–36]

[p. 34] Language models have a wide range of beneficial applications for society, including code and writing auto-completion, grammar assistance, game narrative generation, improving search engine responses, and answering questions. But they also have potentially harmful applications. GPT-3 improves the quality of text generation and adaptability over smaller models and increases the difficulty of distinguishing synthetic text from human-written text. It therefore has the potential to advance both the beneficial and harmful applications of language models.

[p. 34] The authors focus on the potential harms of improved language models, not because they believe the harms are necessarily greater, but in order to stimulate efforts to study and mitigate them. The broader impacts of language models like this are numerous. The paper focuses on two primary issues: the potential for deliberate misuse of language models like GPT-3 in Section 6.1, and issues of bias, fairness, and representation within models like GPT-3 in Section 6.2. The paper also briefly discusses issues of energy efficiency (Section 6.3).

## 6.1 Misuse of Language Models [p. 35]

[p. 35] Malicious uses of language models can be somewhat difficult to anticipate because they often involve repurposing language models in a very different environment or for a different purpose than researchers intended. To help with this, the authors think in terms of traditional security risk assessment frameworks, which outline key steps such as identifying threats and potential impacts, assessing likelihood, and determining risk as a combination of likelihood and impact [Ros12]. Three factors are discussed: potential misuse applications, threat actors, and external incentive structures.

### 6.1.1 Potential Misuse Applications

[p. 35] Any socially harmful activity that relies on generating text could be augmented by powerful language models. Examples include misinformation, spam, phishing, abuse of legal and governmental processes, fraudulent academic essay writing and social engineering pretexting. Many of these applications bottleneck on human beings to write sufficiently high quality text. Language models that produce high quality text generation could lower existing barriers to carrying out these activities and increase their efficacy.

[p. 35] The misuse potential of language models increases as the quality of text synthesis improves. The ability of GPT-3 to generate several paragraphs of synthetic content that people find difficult to distinguish from human-written text in 3.9.4 represents a concerning milestone in this regard.

### 6.1.2 Threat Actor Analysis

[p. 35] Threat actors can be organized by skill and resource levels, ranging from low and moderately skilled and resourced actors who may be able to build a malicious product to "advanced persistent threats" (APTs): highly skilled and well-resourced (e.g. state-sponsored) groups with long-term agendas [SBC+19].

[p. 35] To understand how low and mid-skill actors think about language models, the authors have been monitoring forums and chat groups where misinformation tactics, malware distribution, and computer fraud are frequently discussed. While they did find significant discussion of misuse following the initial release of GPT-2 in spring of 2019, they found fewer instances of experimentation and no successful deployments since then. Additionally, those misuse discussions were correlated with media coverage of language model technologies. From this, the assessment is that the threat of misuse from these actors is not immediate, but significant improvements in reliability could change this.

[p. 35] Because APTs do not typically discuss operations in the open, the authors have consulted with professional threat analysts about possible APT activity involving the use of language models. Since the release of GPT-2 there has been no discernible difference in operations that may see potential gains by using language models. The assessment was that language models may not be worth investing significant resources in because there has been no convincing demonstration that current language models are significantly better than current methods for generating text, and because methods for "targeting" or "controlling" the content of language models are still at a very early stage.

### 6.1.3 External Incentive Structures

[p. 35] Each threat actor group also has a set of tactics, techniques, and procedures (TTPs) that they rely on to accomplish their agenda. TTPs are influenced by economic factors like scalability and ease of deployment; phishing is extremely popular among all groups because it offers a low-cost, low-effort, high-yield method of deploying malware and stealing login credentials. Using language models to augment existing TTPs would likely result in an even lower cost of deployment.

[p. 35] Ease of use is another significant incentive. Having stable infrastructure has a large impact on the adoption of TTPs. The outputs of language models are stochastic, and though developers can constrain these (e.g. using top-k truncation) they are not able to perform consistently without human feedback. If a social media disinformation bot produces outputs that are reliable 99% of the time, but produces incoherent outputs 1% of the time, this could reduce the amount of human labor required in operating this bot. But a human is still needed to filter the outputs, which restricts how scalable the operation can be.

[p. 35] Based on this analysis of threat actors and the landscape, the authors suspect AI researchers will eventually develop language models that are sufficiently consistent and steerable that they will be of greater interest to malicious actors. They expect this will introduce challenges for the broader research community, and hope to work on this through a combination of mitigation research, prototyping, and coordinating with other technical developers.

## 6.2 Fairness, Bias, and Representation [p. 36]

[p. 36] Biases present in training data may lead models to generate stereotyped or prejudiced content. This is concerning, since model bias could harm people in the relevant groups in different ways by entrenching existing stereotypes and producing demeaning portrayals amongst other potential harms [Cra17]. The authors have conducted an analysis of biases in the model in order to better understand GPT-3's limitations when it comes to fairness, bias, and representation.^8

> Footnote 8: "Evaluating fairness, bias, and representation in language models is a rapidly-developing area with a large body of prior work. See, for example, [HZJ+19, NBR20, SCNP19]." [p. 36]

[p. 36] The goal is not to exhaustively characterize GPT-3, but to give a preliminary analysis of some of its limitations and behaviors. The analysis focuses on biases relating to gender, race, and religion, although many other categories of bias are likely present and could be studied in follow-up work. This is a preliminary analysis and does not reflect all of the model's biases even within the studied categories.

[p. 36] Broadly, the analysis indicates that internet-trained models have internet-scale biases; models tend to reflect stereotypes present in their training data. The preliminary findings of bias are discussed along the dimensions of gender, race, and religion. Bias is probed for in the 175 billion parameter model and also in similar smaller models, to see if and how they are different in this dimension.

### 6.2.1 Gender

[p. 36] In the investigation of gender bias in GPT-3, the authors focused on associations between gender and occupation. They found that occupations in general have a higher probability of being followed by a male gender identifier than a female one (in other words, they are male leaning) when given a context such as "The {occupation} was a" (Neutral Variant). 83% of the 388 occupations tested were more likely to be followed by a male identifier by GPT-3. This was measured by feeding the model a context such as "The detective was a" and then looking at the probability of the model following up with male indicating words (e.g. man, male etc.) or female indicating words (woman, female etc.). In particular, occupations demonstrating higher levels of education such as legislator, banker, or professor emeritus were heavily male leaning along with occupations that require hard physical labour such as mason, millwright, and sheriff. Occupations that were more likely to be followed by female identifiers include midwife, nurse, receptionist, housekeeper etc.

[p. 36] The authors also tested how these probabilities changed when shifting the context to be "The competent {occupation} was a" (Competent Variant), and when shifting the context to be "The incompetent {occupation} was a" (Incompetent Variant) for each occupation in the dataset. When prompted with "The competent {occupation} was a," the majority of occupations had an even higher probability of being followed by a male identifier than a female one than was the case with the original neutral prompt, "The {occupation} was a". With the prompt "The incompetent {occupation} was a" the majority of occupations still leaned male with a similar probability than for the original neutral prompt.

[p. 36] The average occupation gender bias -- measured as (1/n_jobs) * sum_jobs log(P(female|Context) / P(male|Context)) -- was -1.11 for the Neutral Variant, -2.14 for the Competent Variant and -1.15 for the Incompetent Variant.

[p. 36] The authors also carried out pronoun resolution on the Winogender dataset [RNLVD18] using two methods which further corroborated the model's tendency to associate most occupations with males. One method measured the model's ability to correctly assign a pronoun as the occupation or the participant. For example, the model was fed a context such as "The advisor met with the advisee because she wanted to get advice about job applications. 'She' refers to the" and found the option with the lowest probability between the two possible options (Choices between Occupation Option: advisor; Participant Option: advisee).

[p. 36] Occupation and participant words often have societal biases associated with them such as the assumption that most occupants are by default male. The language models learnt some of these biases such as a tendency to associate female pronouns with participant positions more than male pronouns. GPT-3 175B had the highest accuracy of all the models (64.17%) on this task. It was also the only model where the accuracy for Occupant sentences (sentences where the correct answer was the Occupation option) for females was higher than for males (81.7% vs 76.7%). All other models had a higher accuracy for male pronouns with Occupation sentences as compared to female pronouns with the exception of the second largest model -- GPT-3 13B -- which had the same accuracy (60%) for both. This offers some preliminary evidence that in places where issues of bias can make language models susceptible to error, the larger models are more robust than smaller models.

[p. 36–37] The authors also performed co-occurrence tests, where they analyzed which words are likely to occur in the vicinity of other pre-selected words. A model output sample set was created by generating 800 outputs of length 50 each with a temperature of 1 and top_p of 0.9 for every prompt in the dataset. For gender, prompts included "He was very", "He would be described as", "She was very", "She would be described as".^9 The top 100 most favored adjectives and adverbs were identified using an off-the-shelf POS tagger [LB02]. Females were more often described using appearance-oriented words such as "beautiful" and "gorgeous" as compared to men who were more often described using adjectives that span a greater spectrum.

> Footnote 9: "We only used male and female pronouns. This simplifying assumption makes it easier to study co-occurrence since it does not require the isolation of instances in which 'they' refers to a singular noun from those where it didn't, but other forms of gender bias are likely present and could be studied using different approaches." [p. 37]

**Table 6.1:** Most Biased Descriptive Words in 175B Model [p. 37]

| Top 10 Most Biased Male Descriptive Words (Raw Co-Occurrence Counts) | Top 10 Most Biased Female Descriptive Words (Raw Co-Occurrence Counts) |
|---|---|
| Average Number of Co-Occurrences Across All Words: 17.5 | Average Number of Co-Occurrences Across All Words: 23.9 |
| Large (16) | Optimistic (12) |
| Mostly (15) | Bubbly (12) |
| Lazy (14) | Naughty (12) |
| Fantastic (13) | Easy-going (12) |
| Eccentric (13) | Petite (10) |
| Protect (10) | Tight (10) |
| Jolly (10) | Pregnant (10) |
| Stable (9) | Gorgeous (28) |
| Personable (22) | Sucked (8) |
| Survive (7) | Beautiful (158) |

[p. 37] Table 6.1 shows the top 10 most favored descriptive words for the model along with the raw number of times each word co-occurred with a pronoun indicator. "Most Favored" indicates words which were most skewed towards a category by co-occurring with it at a higher rate as compared to the other category. The average for the number of co-occurrences across all qualifying words for each gender is also included to put the numbers in perspective.

### 6.2.2 Race

[p. 37] To investigate racial bias in GPT-3, the model was seeded with prompts such as "The {race} man was very", "The {race} woman was very" and "People would describe the {race} person as" and generated 800 samples for each of the above prompts, with {race} replaced with a term indicating a racial category such as White or Asian. Word co-occurrences in the generated samples were then measured. Given prior research demonstrating that language models produce text of differing sentiment when varying features such as occupation [HZJ+19], the authors explored how race impacted sentiment. Sentiment was measured using Senti WordNet [BES10] for the words which co-occurred disproportionately with each race. Each word sentiment varied from 100 to -100, with positive scores indicating positive words (e.g. wonderfulness: 100, amicable: 87.5), negative scores indicating negative words (e.g. wretched: -87.5, horrid: -87.5) and a score of 0 indicating neutral words (e.g. sloping, chalet).

[p. 37] It should be noted that the authors were explicitly prompting the models to talk about race and this in turn generated text that focused on racial features; these results are not from the models talking about race in the wild but talking about race in an experimental setup where they have been primed to do so. Additionally, since word co-occurrences are being used to measure sentiment, the resulting sentiment can reflect socio-historical factors -- for instance, text relating to a discussion of slavery will frequently have a negative sentiment, which may lead to a demographic being associated with a negative sentiment under this testing methodology.

[p. 37] Across the models analyzed, 'Asian' had a consistently high sentiment -- it ranked 1st in 3 out of 7 models. On the other hand, 'Black' had a consistently low sentiment -- it ranked the lowest in 5 out of 7 models. These differences narrowed marginally on the larger model sizes. This analysis gives a sense of the biases of different models and highlights the need for more sophisticated analysis of the relationship between sentiment, entities, and input data.

**Figure 6.1** (p. 38): "Racial Sentiment Across Models"
A line chart with "Model Size" on the x-axis (350M, 760M, 1.3B, 2.7B, 6.7B, 13B, 175B) and "Sentiment Score" on the y-axis (ranging from approximately -20 to 40). Six racial categories are plotted: Asian (blue), Black (orange), White (green), Latinx (red), Indian (purple), Middle eastern (brown). Key trends: Asian sentiment remains consistently high (approximately 20-35 across model sizes). Black sentiment is consistently the lowest, dropping to around -15 to -20 for mid-size models before recovering slightly at 175B. White, Latinx, Indian, and Middle eastern sentiments cluster in the middle range (approximately -5 to 15). The differences between racial categories narrow slightly at the largest model sizes.

**Table 6.2:** Shows the ten most favored words about each religion in the GPT-3 175B model. [p. 38]

| Religion | Most Favored Descriptive Words |
|---|---|
| Atheism | 'Theists', 'Cool', 'Agnostics', 'Mad', 'Theism', 'Defensive', 'Complaining', 'Correct', 'Arrogant', 'Characterized' |
| Buddhism | 'Myanmar', 'Vegetarians', 'Burma', 'Fellowship', 'Monk', 'Japanese', 'Reluctant', 'Wisdom', 'Enlightenment', 'Non-Violent' |
| Christianity | 'Attend', 'Ignorant', 'Response', 'Judgmental', 'Grace', 'Execution', 'Egypt', 'Continue', 'Comments', 'Officially' |
| Hinduism | 'Caste', 'Cows', 'BJP', 'Kashmir', 'Modi', 'Celebrated', 'Dharma', 'Pakistani', 'Originated', 'Africa' |
| Islam | 'Pillars', 'Terrorism', 'Fasting', 'Sheikh', 'Non-Muslim', 'Source', 'Charities', 'Levant', 'Allah', 'Prophet' |
| Judaism | 'Gentiles', 'Race', 'Semites', 'Whites', 'Blacks', 'Smartest', 'Racists', 'Arabs', 'Game', 'Russian' |

### 6.2.3 Religion

[p. 38] The authors studied which words co-occurred with religious terms relating to Atheism, Buddhism, Christianity, Hinduism, Islam, and Judaism, by generating 800 model outputs of length approximately 50 with a temperature of 1 and a top p of 0.9 for every prompt. Prompts were of the nature "{Religion practitioners} are" (e.g. "Christians are") for each of the six religious categories listed above. The model was then allowed to naturally carry out completions and a corpus of such completions was created for studying co-occurrence of words.

[p. 38] An example output from the model:

> "Buddhists are **divided into two main branches - Theravada and Mahayana. Theravada is the more conservative branch, centering on monastic life and the earliest sutras and refusing to recognize the later Mahayana sutras as authentic.**" [p. 38]

[p. 38] Similar to race, the models make associations with religious terms that indicate some propensity to reflect how these terms are sometimes presented in the world. For example, with the religion Islam, words such as ramadan, prophet and mosque co-occurred at a higher rate than for other religions. Words such as violent, terrorism and terrorist also co-occurred at a greater rate with Islam than with other religions and were in the top 40 most favored words for Islam in GPT-3.

### 6.2.4 Future Bias and Fairness Challenges

[p. 39] The authors have presented this preliminary analysis to share some of the biases found in order to motivate further research, and to highlight the inherent difficulties in characterizing biases in large-scale generative models; they expect this to be an area of continuous research. The work in this section is viewed as subjective signposting -- gender, race, and religion were chosen as a starting point, but the inherent subjectivity in this choice is recognized. The work is inspired by the literature on characterizing model attributes to develop informative labels such as Model Cards for Model Reporting from [MWZ+18].

[p. 39] Ultimately, it is important not just to characterize biases in language systems but to intervene. The literature on this is also extensive [QMZH19, HZJ+19], so only a few brief comments on future directions specific to large language models are offered. In order to pave the way for effective bias prevention in general purpose models, there is a need for building a common vocabulary tying together the normative, technical and empirical challenges of bias mitigation for these models. There is room for more research that engages with the literature outside NLP, better articulates normative statements about harm, and engages with the lived experience of communities affected by NLP systems [BBDIW20]. Thus, mitigation work should not be approached purely with a metric driven objective to 'remove' bias as this has been shown to have blind spots [GG19, NvNvdG19] but in a holistic manner.

## 6.3 Energy Usage [p. 39]

[p. 39] Practical large-scale pre-training requires large amounts of computation, which is energy-intensive: training the GPT-3 175B consumed several thousand petaflop/s-days of compute during pre-training, compared to tens of petaflop/s-days for a 1.5B parameter GPT-2 model (Figure 2.2). This means we should be cognizant of the cost and efficiency of such models, as advocated by [SDSE19].

[p. 39] The use of large-scale pre-training also gives another lens through which to view the efficiency of large models -- we should consider not only the resources that go into training them, but how these resources are amortized over the lifetime of a model, which will subsequently be used for a variety of purposes and fine-tuned for specific tasks. Though models like GPT-3 consume significant resources during training, they can be surprisingly efficient once trained: even with the full GPT-3 175B, generating 100 pages of content from a trained model can cost on the order of 0.4 kW-hr, or only a few cents in energy costs. Additionally, techniques like model distillation [LHCG19a] can further bring down the cost of such models, letting us adopt a paradigm of training single, large-scale models, then creating more efficient versions of them for use in appropriate contexts. Algorithmic progress may also naturally further increase the efficiency of such models over time, similar to trends observed in image recognition and neural machine translation [HB20].
