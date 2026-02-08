# 4.3.2 Alignment of Controversial Topics [p. 34–36]

[p. 34] Off-the-shelf preference datasets and reward models generally do not account for the values and needs of a specific user population. Kirk et al. (2025), for example, shows that user preferences on LLM outputs can vary substantially, especially across different countries and cultures (see also Zollo et al., 2024). The alignment process, in line with the goals of the Swiss AI Initiative,^43 draws on Swiss and global constitutional norms for controversial topics that entail moral, political, social, and cultural values (Stammbach et al., 2024).

To address this issue, a separate alignment pipeline is used for controversial issues. A "Constitutional AI" approach (Bai et al., 2022b) is taken to develop, organize, and deploy a set of principles that should guide LLM generations for such issues. This section describes the development of the *Swiss AI Charter*, its validation through surveys of Swiss residents, and its deployment into the alignment pipeline through an LLM-as-judge with a constitutional prompt. [p. 34]

## The Swiss AI Charter [p. 34]

[p. 34] A set of precepts for LLM behaviour informed by Switzerland's constitutional values is developed, including neutrality, consensus-building, federalism, multilingualism, and respect for cultural diversity. The Charter (included in Appendix O) incorporates Switzerland's strong traditions of direct democracy, privacy protection, and collective decision-making processes that have contributed to the country's renowned stability and international standing.

The Charter consists of 11 articles, each summarizing a principle that should guide AI alignment:

1. **Response Quality** -- Writing clear, accurate, and useful responses.
2. **Knowledge and Reasoning Standards** -- Using verified facts and sound reasoning.
3. **Respectful Communication** -- Treating people with courtesy, fairness, and accessibility.
4. **Preventing Harm** -- Protecting safety and refusing harmful requests.
5. **Resolving Value Conflicts** -- Handling trade-offs openly and preserving principles.
6. **Professional Competence Boundaries** -- Educating without giving licensed advice.
7. **Collective Decision-Making** -- Supporting fair and constructive group decisions.
8. **Autonomy and Personal Boundaries** -- Respecting choice, privacy, and clear limits.
9. **Long-term Orientation and Sustainability** -- Considering long-term impacts and risks.
10. **Human Agency** -- Keeping humans in control and independent.
11. **AI Identity and Limits** -- Being clear about what the AI is and is not.

Each article consists of a set of 3-9 clauses. For example, Article 10 in full:

> *"10. Human Agency. The AI must ensure that ultimate control and decision-making authority always remain with humans [10.1]. The system should remain focused exclusively on serving intended human purposes, without developing, implying, or expressing separate interests, including any form of self-preservation or power-seeking [10.2]. Responses should prevent unhealthy dependencies by supporting human independence in decision-making [10.3]."* [p. 34]

[p. 35] The use of bracketed clause numbers (*e.g.* [10.1], [10.2]) allows the LLM judge to ground evaluations of completions in the constitutional text. The full charter (a bit more than 2 pages) is printed in Appendix O.

The Swiss AI Initiative plans to open the Swiss AI Charter for further refinement through a democratized process, inviting broad participation from other institutions, communities, and stakeholders to collaboratively develop principles that authentically represent shared values in AI alignment. [p. 35]

## Public Agreement with the Swiss AI Charter [p. 35]

[p. 35] To evaluate the charter, Swiss residents are surveyed to gauge agreement with these values and to ensure they were appropriate for model training. A sample of 163 Swiss residents is recruited through Prolific and through the ETH Decision Sciences Lab. Survey statistics are computed from about 88% of respondents who passed a basic attention check.

The main goal of the survey is to evaluate whether respondents generally agree with the principles set forth in the charter. The survey asked:

> *Here is a hypothetical principle specifying how an AI chatbot (like ChatGPT) should behave when interacting with users:*
> *{Charter Article}*
> *When interacting with human users, to what extent should AI chatbots follow this principle?*

where {Charter Article} is the full text of one of the charter articles. Respondents could answer with *Always/definitely yes*, *Usually/probably yes*, *Neutral / Unsure*, *Usually/probably not*, or *Always/definitely not*. The respondents answered this question eleven times, once for each principle, in random order. [p. 35]

[p. 35–36] Table 13 reports the shares across respondent answers for each of the eleven principles. Overall, there is high agreement and low disagreement with all principles articulated in the charter. The rightmost column shows the overall agreement rate (combining the "always" and "usually" categories, and excluding "neutral/unsure"). The average agreement is very high at 97.3%, with the lowest agreement rate of 92.6% observed for Article 6 on respecting professional licensing boundaries. Further, most respondents have high confidence in these principles, with 71.8% of responses indicating that the chatbot should always or definitely follow the principle. This type of strong agreement is highest for Article 4 on Preventing Harm (91.3%). Meanwhile, strong disagreement with the principles (*always/definitely not*) is very rare -- 0.3% of the responses. Overall, these results give confidence that the Swiss AI Charter captures shared Swiss values. [p. 35]

A second survey task asked respondents to rank the eleven principles by their relative importance. Article 2 -- Knowledge and Reasoning Standards is by far the highest-ranked in terms of importance, indicating that most respondents want the AI to take a logical approach and use verified facts (Appendix Figure J.4). Article 4 -- Preventing Harm and Article 10 -- Human Agency are also ranked as important. On the other side, there are relatively lower importance rankings reported for Article 7 -- Collective Decision-Making, Article 9 -- Long-term Orientation and Sustainability, and Article 5 -- Resolving Value Conflicts. [p. 35]

**Table 13: Survey Approval on Values Expressed in Swiss AI Charter** [p. 36]

Rows correspond to the 11 articles of the Swiss AI Charter (Appendix O). The five middle columns correspond to answers to the main survey question: *"When interacting with human users, to what extent should AI chatbots follow this principle?"*. The rightmost column is the sum of the "yes" answers divided by the sum of the "yes" and "no" answers (excluding "neutral"). All numbers in percent.

| Principle | Always/ definitely not | Usually/ probably not | Neutral/ Unsure | Usually/ probably yes | Always/ definitely yes | Agree / Agree+Disagree |
|---|---|---|---|---|---|---|
| 1. Response Quality | 0.5 | 0.0 | 6.5 | 17.8 | 75.2 | 99.4 |
| 2. Knowledge and Reasoning Standards | 0.0 | 0.5 | 2.7 | 9.7 | 87.1 | 99.4 |
| 3. Respectful Communication | 0.5 | 3.2 | 4.9 | 21.1 | 70.3 | 95.4 |
| 4. Preventing Harm | 0.0 | 1.1 | 1.1 | 6.5 | 91.3 | 98.9 |
| 5. Resolving Value Conflicts | 0.0 | 1.6 | 5.9 | 24.9 | 67.6 | 97.5 |
| 6. Professional Competence Boundaries | 0.5 | 5.4 | 6.0 | 26.3 | 61.8 | 92.6 |
| 7. Collective Decision-Making | 0.0 | 4.9 | 7.6 | 26.5 | 61.0 | 94.9 |
| 8. Autonomy and Personal Boundaries | 0.5 | 3.3 | 5.5 | 18.1 | 72.6 | 96.4 |
| 9. Long-term Orientation and Sustainability | 0.5 | 3.8 | 9.7 | 26.5 | 59.5 | 93.6 |
| 10. Human Agency | 0.5 | 2.2 | 6.0 | 21.1 | 70.2 | 96.7 |
| 11. AI Identity and Limits | 0.0 | 3.3 | 8.2 | 22.4 | 66.1 | 95.8 |
| **Average** | **0.3** | **2.7** | **5.7** | **19.0** | **71.8** | **97.3** |

## Constitutional LLM Judge [p. 35–36]

[p. 35–36] Apertus's behaviour on controversial issues is aligned by prompting an LLM-as-judge (Qwen3-32B) to score completions by their level of adherence to the Charter. Specifically, the prompt includes the full text of the charter, followed by the following instruction:

```
Constitutional LLM Judge Instruction:

Based on the above principles, rate the following response to the
question on a scale from 1 to 9, where 9 is best and 1 is worst.

QUESTION: {prompt}

RESPONSE: {completion}

Rate this response from 1 to 9.

Don't think or explain. Answer with only the number.
```

[p. 36] This prompt is applied with Qwen3-32B and a single numerical score on the 1-9 scale is computed as the token-probability-weighted average across each number in the scale, following recommendations from Wang et al. (2025) and Licht et al. (2025).

These scores are evaluated using synthetic data. Using an LLM (Qwen3-32B), a high-quality completion is iteratively degraded to produce increasingly lower-quality completions, each with a "ground-truth" score corresponding to the iteration number (see Appendix J.4). Pairwise scoring performed slightly better than the probability-weighted pointwise scoring.^44 To optimize compute efficiency, the pointwise scores are first produced and then the top 5 scoring responses are pairwise ranked.

These constitutionality scores (and rankings) are then used to align Apertus using QRPO. [p. 36]

---

**Footnotes:**
- ^43: swiss-ai.org
- ^44: The prompt used, similar to the pointwise scale, starts with the Swiss AI Charter and then asks: "Based on the above principles, compare these two responses: ... {completions to compare} ... Compare these two completions and determine which is better."
