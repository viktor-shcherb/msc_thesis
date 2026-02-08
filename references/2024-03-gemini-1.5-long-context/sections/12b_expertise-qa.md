# 12.10. Expertise QA [p. 128–129]

## 12.10.0.1. Background: Why evaluate the long tail? [p. 128]

[p. 128] The most impactful use cases of Generative AI (GenAI) require the model to operate on the long tail of human knowledge and skills. Such skills are valuable to a user because they are rare, and information and quality sparseness in training data is a challenge for GenAI models. To apply expertise, models need to balance memorization with generalization from training data to individual use cases. The model needs to have sufficient capacity and a precise enough fit to describe the long tail of the distribution (c.f., GPQA, Carlini et al., 2022; Rein et al., 2023; Saab et al., 2024).

Measuring performance on the long tail in generative applications turns out to be challenging for practical reasons: without in-depth knowledge of the subject matter, model responses are difficult to judge even when golden answers are available. It is equally difficult to identify a distribution of general topics that reflects realistic, yet aspirational use cases.

The authors surveyed a panel of in-house experts selected for their general ability to reason, write, read, and gauge, asking for their specific expertise. Examples of such expertise included "25 years experience as a professional classical pianist", "Shakespearean Tragic Plays - M.A.". In Expertise QA, the focus is on hard human-interest questions, predominantly from the humanities.

These experts (n_e = 57) were asked to formulate questions (n_q = 572; 19.2 words avg.) that required the specific expertise to do any necessary research, but also to select and combine the obtained information into a well-crafted response. The same experts then rated and ranked model responses to their respective questions. The models were evaluated according to their ability to answer such questions with a high degree of accuracy, but, secondarily, completeness and informativeness. This reflects the expected utility provided to users. Experts were unaware of the origins of each model response.

Results show that the Gemini 1.5 models significantly and strongly outperform 1.0 Pro on the Expert QA task, both in pointwise 'Accurate' and 'Severely inaccurate' ratings, and in side-by-side rankings (see Figure 18). The advantage also holds when comparing answers side-by-side, which takes into account not just factual accuracy, but also informativeness (see Table 53 in the Appendix).

## 12.10.1. Results [p. 128–129]

[p. 128] See Table 52 for pointwise accuracy judgments, and Table 53 for side-by-side comparisons derived from the n-way rankings.

**Table 52:** Experts label each response as "fully accurate" (higher is better), "somewhat inaccurate", and "severely inaccurate" (lower is better). The two metrics shown correspond to the proportion of the extreme labels. n_q = 572. [p. 128]

|                     | 1.0 Pro        | 1.0 Ultra      | 1.5 Flash       | 1.5 Pro          |
|---------------------|----------------|----------------|-----------------|------------------|
| Accurate            | 50.0% +/-4.1   | 61.5% +/-4.0   | **67.7% +/-3.9** | **67.1% +/-3.8** |
| Severely inaccurate | 26.7% +/-3.6   | 10.1% +/-2.4   | **7.3% +/-2.2**  | **6.3% +/-2.0**  |
| Words               | 270 +/-12      | 314 +/-7       | 420 +/-7         | 390 +/-7         |

Bold values for 1.5 Flash and 1.5 Pro indicate the best-performing models. Both 1.5 Flash and 1.5 Pro produce substantially longer responses (420 and 390 words on average) compared to 1.0 Pro (270 words) and 1.0 Ultra (314 words).

**Table 53:** Expertise QA: Pairwise SxS analysis obtained from the multi-way side-by-side data. [p. 129]

| Model     | Baseline  | wins | ties | losses | W/L Ratio |
|-----------|-----------|------|------|--------|-----------|
| 1.0 Ultra | 1.0 Pro   | 336  | 120  | 118    | 2.85      |
| 1.5 Flash | 1.0 Pro   | 355  | 130  | 85     | 4.18      |
| 1.5 Flash | 1.0 Ultra | 240  | 157  | 171    | 1.40      |
| 1.5 Pro   | 1.0 Pro   | 358  | 114  | 99     | 3.62      |
| 1.5 Pro   | 1.0 Ultra | 259  | 146  | 164    | 1.58      |
| 1.5 Pro   | 1.5 Flash | 197  | 181  | 190    | 1.04      |

## 12.10.2. Instructions to in-house experts (example with 5 models) [p. 129]

[p. 129] The full instructions given to in-house experts for rating are reproduced below.

> "In this task, you are asked to rate machine-produced responses to questions that require expertise -- specifically, your expertise." [p. 129]

The instructions assume the response speaks to a reasonably well educated audience. Evaluators are given 5 responses labeled A, B, C, D, and E.

**Pointwise accuracy question:** For each question, experts are asked: Is the response fully accurate? If it is inaccurate, would you consider the inaccuracy severe (objective mistakes relevant to the query)?

Possible answers: fully accurate; somewhat inaccurate; severely inaccurate.

**Ranking question:** Experts rank responses A, B, C, D, E in the order of best to worst (e.g., "B,ADE,C" to indicate B is best and C is worst, and D/A/E are equal between them). Accuracy is most important, followed by completeness and informativeness.

**Ranking criteria (from most to least important):**

1. Consider every detailed claim of the response, its accuracy to today's knowledge, and its appropriateness in an answer to the question. The most important claims are those that respond directly to the question, or whose accuracy has significant impact on the overall response. If these claims are inaccurate, the inaccuracy should be considered severe. Where experts would differ in opinion, and these different viewpoints are not niche opinions but part of a widely held discourse, the response should discuss these appropriately. A response supporting only one viewpoint would be inaccurate in this case. Sometimes, a model might give a general, plausible answer as opposed to a specific one. It is important to evaluate whether the plausible answer is in fact accurate for the specific case asked in the query. Do not let the model "get away" with a low-effort response!
2. Is the response complete or at least sufficient (in relation to other responses)?
3. Is the response well-crafted and understandable for its target audience?
