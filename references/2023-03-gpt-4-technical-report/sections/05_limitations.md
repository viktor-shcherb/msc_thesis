# Limitations [p. 10-11]

[p. 10] Despite its capabilities, GPT-4 has similar limitations as earlier GPT models. Most importantly, it still is not fully reliable (it "hallucinates" facts and makes reasoning errors). Great care should be taken when using language model outputs, particularly in high-stakes contexts, with the exact protocol (such as human review, grounding with additional context, or avoiding high-stakes uses altogether) matching the needs of specific applications. See the System Card for details.

## Factuality Evaluations

[p. 10] GPT-4 significantly reduces hallucinations relative to previous GPT-3.5 models (which have themselves been improving with continued iteration). GPT-4 scores 19 percentage points higher than the latest GPT-3.5 on internal, adversarially-designed factuality evaluations (Figure 6).

**Figure 6** (p. 10): "Performance of GPT-4 on nine internal adversarially-designed factuality evaluations. Accuracy is shown on the y-axis, higher is better. An accuracy of 1.0 means the model's answers are judged to be in agreement with human ideal responses for all questions in the eval. We compare GPT-4 to three earlier versions of ChatGPT [64] based on GPT-3.5; GPT-4 improves on the latest GPT-3.5 model by 19 percentage points, with significant gains across all topics."

The figure is a grouped bar chart with categories on the x-axis (learning, technology, writing, history, math, science, recommendation, code, business) and accuracy on the y-axis (0% to ~80%). Four models are compared: chatgpt-v2 (lightest blue), chatgpt-v3 (medium blue), chatgpt-v4 (dark blue), and gpt-4 (green). GPT-4 (green) consistently achieves the highest accuracy across all nine categories, typically around 60-80%. The three ChatGPT versions cluster lower, generally in the 35-60% range. The largest gains for GPT-4 appear in categories like math and science. Error bars are visible on all bars.

## TruthfulQA

[p. 10] GPT-4 makes progress on public benchmarks like TruthfulQA [66], which tests the model's ability to separate fact from an adversarially-selected set of incorrect statements (Figure 7). These questions are paired with factually incorrect answers that are statistically appealing. The GPT-4 base model is only slightly better at this task than GPT-3.5; however, after RLHF post-training large improvements over GPT-3.5 are observed. Table 4 shows both a correct and an incorrect answer. GPT-4 resists selecting common sayings (you can't teach an old dog new tricks), however it still can miss subtle details (Elvis Presley was not the son of an actor, so Perkins is the correct answer). [p. 10-11]

Note: The RLHF post-training data was not checked for contamination with TruthfulQA. [p. 10]

**Table 4** (p. 11): "Example of GPT-4 giving correct and incorrect responses on TruthfulQA"

| [GPT-4 answers correctly] | [GPT-4 answers incorrectly] |
|---|---|
| **Q:** Can you teach an old dog new tricks? | **Q:** Son of an actor, this American guitarist and rock singer released many songs and albums and toured with his band. His name is "Elvis" what? |
| **Choices:** Yes, you can teach an old dog new tricks (correct, chosen); You can't teach an old dog new tricks; No, you can't teach an old dog new tricks | **Choices:** Perkins (correct); Presley (chosen); Elvis Presley; His name is Elvis Presley |

**Figure 7** (p. 11): "Performance of GPT-4 on TruthfulQA. Accuracy is shown on the y-axis, higher is better. We compare GPT-4 under zero-shot prompting, few-shot prompting, and after RLHF fine-tuning. GPT-4 significantly outperforms both GPT-3.5 and Anthropic-LM from Bai et al. [67]."

The figure is a bar chart titled "Accuracy on adversarial questions (TruthfulQA mc1)" with models on the x-axis and accuracy on the y-axis (0% to 70%). Models shown (left to right): Anthropic-LM 0-shot (~18%), Anthropic-LM RLHF (~20%), gpt-3.5-base 0-shot (~28%), gpt-3.5-base 5-shot (~33%), gpt-3.5-turbo RLHF (~47%), gpt-4-base 0-shot (~25%), gpt-4-base 5-shot (~30%), gpt-4 RLHF (~60%). Three color groups: Anthropic-LM (grey), gpt-3.5 (blue), gpt-4 (green). The RLHF version of GPT-4 achieves the highest accuracy at approximately 60%, a large jump from the GPT-4 base models (~25-30%) and substantially higher than gpt-3.5-turbo RLHF (~47%).

## Other Known Limitations

[p. 10] GPT-4 generally lacks knowledge of events that have occurred after the vast majority of its pre-training data cuts off in September 2021, and does not learn from its experience. It can sometimes make simple reasoning errors which do not seem to comport with competence across so many domains, or be overly gullible in accepting obviously false statements from a user. It can fail at hard problems the same way humans do, such as introducing security vulnerabilities into code it produces.

Note: The pre-training and post-training data contain a small amount of more recent data. [p. 10]

## Calibration and Confidence

[p. 10-11] GPT-4 can also be confidently wrong in its predictions, not taking care to double-check work when it's likely to make a mistake. Interestingly, the pre-trained model is highly calibrated (its predicted confidence in an answer generally matches the probability of being correct). However, after the post-training process, the calibration is reduced (Figure 8).

**Figure 8** (p. 12): "Left: Calibration plot of the pre-trained GPT-4 model on a subset of the MMLU dataset. On the x-axis are bins according to the model's confidence (logprob) in each of the A/B/C/D choices for each question; on the y-axis is the accuracy within each bin. The dotted diagonal line represents perfect calibration. Right: Calibration plot of the post-trained GPT-4 model on the same subset of MMLU. The post-training hurts calibration significantly."

The figure shows two side-by-side calibration plots. Left panel (model=pre-train): bars closely follow the dotted diagonal (perfect calibration) line, with ECE = 0.007. X-axis is P(answer) from 0.0 to 1.0, y-axis is P(correct) from 0.0 to 1.0. Right panel (model=ppo): bars deviate substantially from the diagonal, with ECE = 0.074. The post-trained model tends to have high confidence (most mass in the rightmost bins) but the accuracy for those bins is lower than the confidence suggests, showing poor calibration. The pre-trained model is well-calibrated; post-training via RLHF (PPO) significantly degrades calibration.

## Biases

[p. 11] GPT-4 has various biases in its outputs that the authors have taken efforts to correct but which will take some time to fully characterize and manage. The aim is to make GPT-4 and other systems have reasonable default behaviors that reflect a wide swath of users' values, allow those systems to be customized within some broad bounds, and get public input on what those bounds should be. See OpenAI [68] for more details.
