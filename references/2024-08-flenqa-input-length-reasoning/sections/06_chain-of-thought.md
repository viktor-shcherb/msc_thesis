# 6 Does Chain of Thought Help? [p. 7-8]

[p. 7] Chain of Thought (CoT) prompting, introduced by Kojima et al. (2022); Wei et al. (2022), is a technique by which the LLM is pushed to produce a text comprising of reasoning steps before concluding the correct answer for a question. Zhou et al. (2022) found that a more specific and optimised instruction ("Let's work this out in a step by step way to be sure we have the right answer.") improves performance.

The CoT technique was shown to significantly improve the accuracy on many reasoning-based question-answering setups. The authors investigate whether using it will change the trend and allow the LLMs to perform effectively on longer inputs. They experiment with CoT using the elicitation string of Zhou et al. (2022).

The results show (Figure 1) that CoT has different effects on different LLMs, and overall does not mitigate the drop in performance due to length. In most cases (GPT4, Mixtral 8x7B, Mistral Medium and GPT3.5) it improves performance, but only in GPT4 it has an increased effect as length increases, making it a limited mitigation technique. In the case of Gemini-Pro, CoT decreases performance as input length is increased, even though it increases performance on short length.

The full results of the CoT prompting over all tasks and setups can be found in Appendix C.
