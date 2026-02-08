# 4 Experiments [p. 4, 6–7]

## Table 3

**Table 3** (p. 4): "Main results. The performance of the baselines on InfiniteBench. For multiple-choice questions, if the model does not output one of the options, we regard it as an empty prediction, and thus give it a score of 0."

| Task              | GPT-4      | YaRN-Mistral | Kimi-Chat | Claude 2  |
|-------------------|------------|--------------|-----------|-----------|
| Retrieve.PassKey  | **100.00** | 92.71        | 98.14     | 97.80     |
| Retrieve.Number   | **100.00** | 56.61        | 95.42     | 98.14     |
| Retrieve.KV       | **89.00**  | 0.00         | 53.60     | 65.40     |
| En.Sum            | 14.73      | 9.09         | **17.93** | 14.45     |
| En.QA             | **22.22**  | 9.55         | 16.52     | 11.97     |
| En.MC             | 67.25      | 27.95        | **72.49** | 62.88     |
| En.Dia            | 8.50       | 7.50         | 11.50     | **46.50** |
| Zh.QA             | **23.06**  | 16.98        | 18.62     | 10.53     |
| Code.Debug        | **39.59**  | 0.76         | 18.02     | 2.28      |
| Code.Run          | **23.25**  | 1.25         | 2.00      | 2.50      |
| Math.Calc         | **0.01**   | 0.00         | 0.00      | 0.00      |
| Math.Find         | **60.00**  | 17.14        | 12.57     | 32.29     |
| Average           | **45.63**  | 19.96        | 34.73     | 37.06     |

---

[p. 6] The authors conduct a thorough set of experiments on InfiniteBench, covering baselines, experimental setup, and main results.

## 4.1 Baselines

[p. 7] InfiniteBench generally requires the ability to handle input contexts longer than 100K. There is a handful of LLMs that claim to be capable of handling contexts over 100K. Four baselines are included: the first three are proprietary LLMs (no access to the model), while the last baseline is open-sourced. Details on evaluation are in Appendix D.

**GPT-4** GPT by OpenAI is one of the most widely used and capable LLMs in the market, and a recent version of GPT-4 (OpenAI, 2023b) can support 128K contexts.

**Claude 2** Claude 2 (Anthropic, 2023) is a proprietary chat-based LLM released by Anthropic AI and has shown impressive capabilities. The second version of the Claude series supports 200K contexts. The authors manually enter each example through the webpage because they have no access to their API.

**Kimi-Chat** Kimi-Chat, a proprietary chat-oriented LLM developed by Moonshot AI (AI, 2023), is designed to process contexts up to 200K. Due to the lack of API access, the authors manually input the test data using their web interface.

**YaRN-Mistral** YaRN-Mistral is a derivative of Mistral-7B (Jiang et al., 2023) introduced by Peng et al. (2023b). The original Mistral-7B was trained on input lengths up to 8K and shows a reduced performance in longer contexts. Peng et al. (2023b) adapted it to 128K contexts by modifying the position encoding and continued training.

## 4.2 Experimental Setup

[p. 7] **Prompt Templates** For each model-task combination, the authors craft prompts to optimize model performance on short dummy examples. Detailed prompt templates for each model and task can be found in Appendix B.

**Input Truncation** All API-based baselines are subject to a maximum input length limit and will reject inputs exceeding this threshold. While YaRN-Mistral is theoretically capable of handling longer contexts, the authors only claim abilities up to 128K. Therefore, inputs are truncated by removing the center and joining both ends. This approach is predicated on the assumption that key information, such as instructions and book titles, is typically located at either the start or the end of a prompt.

## 4.3 Main Result

[p. 7] Table 3 and Figure 1 display the performances of various baselines on InfiniteBench. Notably, GPT-4 outperforms other baselines in the retrieval, code, and math domains, with a considerably higher average score. However, in the novel-based tasks, no distinct winner emerges among the proprietary LLMs. On the other hand, the open-source YaRN-Mistral lags behind the proprietary models in most tasks, exhibiting almost random performance in multiple areas. This aligns with its relatively inferior performance in shorter contexts compared to these models. Additionally, it is observed that the baselines generally excel more in retrieval tasks than in other areas, echoing the relative simplicity of these tasks for human participants.
