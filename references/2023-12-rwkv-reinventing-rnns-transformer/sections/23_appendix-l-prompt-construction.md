# L Importance of Prompt Construction and Comparison to GPT Models [p. 25-26]

[p. 25-26]

Inspired by Kocon et al. (2023), the authors compared the zero-shot performance of RWKV-4-Raven-14B with ChatGPT (access in February 2023) and GPT-4 using several known NLP tasks: recognizing textual entailment (RTE), Winograd Natural Language Inference (WNLI), and recognizing emotions elicited in readers (GoEmotions and PolEmo2). Each model got the same prompts manually chosen to receive proper responses from the ChatGPT model. As shown in Table 6, RWKV performs significantly worse than ChatGPT and GPT-4 in several specific tasks. The authors suspect that this disparity is likely caused by the choice of prompts used to generate the answers since the prompts are written in natural language and do not take into account that RWKV, as an RNN, is unable to look back inside an instruction. [p. 25]

**Table 6:** ChatGPT, GPT-4 and RWKV-4-Raven-14B reasoning performance comparison in RTE (Wang et al., 2019), WNLI (Wang et al., 2018), GoEmotions (Demszky et al., 2020), and PolEmo2 (Kocon et al., 2019) benchmarks. RWKV GPT prompts were primarily used for ChatGPT in (Kocon et al., 2023). SOTA is provided as a supplementary reference.

| Task Name | Measure | ChatGPT | GPT-4 | RWKV-GPT | RWKV-adapted | SOTA |
|---|---|---|---|---|---|---|
| RTE | F1 Macro | 88.1 | **91.3** | 44.2 | 74.8 | 92.1 |
| WNLI | Accuracy | 81.7 | **91.6** | 47.9 | 49.3 | 97.9 |
| GoEmotions | F1 Macro | **25.6** | 23.1 | 7.9 | 7.9 | 52.8 |
| PolEmo2 | F1 Macro | **44.1** | 41.0 | 38.2 | 40.9 | 76.4 |

When the instruction style was adapted (re-ordered) to respect that RNNs are not capable of "retrospective processing", the quality may significantly change, e.g., for RTE (Wang et al., 2019) F1 Macro increased from 44.2% to 74.8%. The authors hypothesize that RWKV models are more sensitive to the position of the components in the context, as RNN-based architectures cannot look back and readjust the weight of previous information. For better performance, the desired information should be placed *after* the main question. [p. 25]

Example ChatGPT prompt for RTE:
> Having premise \<here is a premise\> judge if the following hypothesis \<here is a hypothesis\> is logically connected with the premise. Answer "entailment" if yes, or "not_entailment" if no.

Re-ordered RWKV prompt for RTE (taking into account the nature of the RNN):
> Can you tell me if the hypothesis is entailment or is not entailment to the premise?
> premise: \<here is a premise\>
> hypothesis: \<here is a hypothesis\>

[p. 26]

The authors also tested the approach of stating the input after the question on multiple other tasks: aggression and sarcasm detection, classification of unhealthy (offensive) texts, mathematical Q&A, and sentiment analysis, see Table 7. The results suggest that better prompts might reduce the disparity between models. Raven achieves comparable results to ChatGPT on unhealthy conversation detection and even surpasses it on the sarcasm detection dataset. While such an approach to prompting looks necessary, it is not enough in itself to replace the capability of having free access to the whole context. Therefore, prompt engineering seems to be significantly more important for the RNN models rather than for standard transformers. It is entirely possible that good prompts to RNN models do not mean additional restrictions, but should simply be constructed using completely different guidelines. [p. 26]

**Table 7:** ChatGPT and RWKV-4-Raven-14B performance comparison in Aggression (Wulczyn et al., 2017), Sarcasm (Siddiqui, 2019), Unhealthy (Price et al., 2020), MathQA (Cobbe et al., 2021), and TweetSent (Barbieri et al., 2020) benchmarks. SOTA is provided as a supplementary reference.

| Task Name | Measure | ChatGPT | RWKV-adapted | SOTA |
|---|---|---|---|---|
| Aggression | F1 Macro | **69.10** | 56.66 | 74.45 |
| MathQA | Accuracy | **71.40** | 5.43 | 83.20 |
| Sarcasm | F1 Macro | 49.88 | **50.96** | 53.57 |
| TweetSent | F1 Macro | **63.32** | 52.50 | 72.07 |
| Unhealthy | F1 Macro | **45.21** | 43.30 | 50.96 |

The authors of Kocon et al. (2023)^4 perform chain-of-thought to improve results on the MathQA dataset. Even including this approach, the Raven model achieved a very low accuracy of 5.43%. Without it, the model performed even worse, performing only very basic and simple calculations and achieving 4.13% accuracy. Raven struggled with questions that required intermediate results. It is likely that the order of information presented in the math questions inside the dataset poses a challenge for the RWKV model. It is yet to be seen if prompt engineering can address this issue. This further emphasizes the importance of the order of information the model receives. [p. 26]

^4 This is in line with the idea discussed in (Wei et al., 2022b).

Template used to prompt the Raven model in MathQA with chain-of-thought:
> Write the reasoning and highlight the answer to the question at the end in the format: "Answer: ". The question is: \<here is a question\>

Template used to prompt the Raven model in MathQA without chain-of-thought:
> Write the answer to the math question in the format: "Answer: ". The question is: \<here is a question\>
