# 3.4 Tool Use, Code Interpreter, and Agent [p. 13–16]

[p. 13] The QWEN models, which are designed to be versatile, have the remarkable ability to assist with (semi-)automating daily tasks by leveraging their skills in tool-use and planning. As such, they can serve as agents or copilots to help streamline various tasks. QWEN's proficiency is explored in the following areas:

- Utilizing unseen tools through ReAct prompting (Yao et al., 2022) (see Table 6).
- Using a Python code interpreter to enhance math reasoning, data analysis, and more (see Table 7 and Table 8).
- Functioning as an agent that accesses Hugging Face's extensive collection of multimodal models while engaging with humans (see Table 9).

## SFT data for tool use and agent capabilities

[p. 15] To enhance QWEN's capabilities as an agent or copilot, the self-instruct (Wang et al., 2023c) strategy is employed for SFT. Specifically, the in-context learning capability of QWEN is utilized for self-instruction. By providing a few examples, QWEN is prompted to generate more relevant queries and generate outputs that follow a specific format, such as ReAct (Yao et al., 2022). Rules are then applied and human annotators are involved to filter out any noisy samples. Afterwards, the samples are incorporated into QWEN's training data, resulting in an updated version of QWEN that is more dependable for self-instruction. This process is iterated multiple times until an ample number of samples that possess both exceptional quality and a wide range of diversity are gathered. The final collection consists of around 2000 high-quality samples.

[p. 15] During the finetuning process, these high-quality samples are mixed with all the other general-purpose SFT samples, rather than introducing an additional training stage. By doing so, essential general-purpose capabilities that are also pertinent for constructing agent applications are retained.

## Using Tools via ReAct Prompting

[p. 15] A benchmark has been created and made publicly available for evaluating QWEN's ability to call plugins, tools, functions, or APIs using ReAct Prompting (see Qwen Team, Alibaba Group, 2023b). To ensure fair evaluation, any plugins that were included in QWEN's training set have been excluded. The benchmark assesses the model's accuracy in selecting the correct plugin from a pool of up to five candidates, as well as the plausibility of the parameters passed into the plugin and the frequency of false positives. A false positive occurs when the model incorrectly invokes a plugin in response to a query, despite not being required to do so.

**Table 6: Performance of QWEN on the in-house Chinese benchmark that evaluates its ability to use unseen tools via ReAct prompting.** [p. 13]

| Model | Params | Tool Selection (Acc.↑) | Tool Input (Rouge-L↑) | False Positive Error (%)↓ |
|---|---|---|---|---|
| GPT-4 | - | 95 | 90 | 15.0 |
| GPT-3.5 | - | 85 | 88 | 75.0 |
| QWEN-CHAT | 1.8B | 92 | 89 | 19.3 |
| | 7B | **98** | 91 | 7.3 |
| | 14B | **98** | **93** | **2.4** |

[p. 15] The results presented in Table 6 demonstrate that QWEN consistently achieves higher accuracy in identifying the relevance of a query to the available tools as the model size increases. However, the table also highlights that beyond a certain point, there is little improvement in performance when it comes to selecting the appropriate tool and providing relevant arguments. This suggests that the current preliminary benchmark may be relatively easy and may require further enhancement in future iterations.

[p. 15] GPT-3.5 stands out as an exception, displaying suboptimal performance on this particular benchmark. This could potentially be attributed to the fact that the benchmark primarily focuses on the Chinese language, which may not align well with GPT-3.5's capabilities. Additionally, GPT-3.5 tends to attempt to use at least one tool, even if the query cannot be effectively addressed by the provided tools.

## Using Code Interpreter for Math Reasoning and Data Analysis

[p. 15–16] The Python code interpreter is widely regarded as a powerful tool for augmenting the capabilities of an LLM agent. It is worth investigating whether QWEN can harness the full potential of this interpreter to enhance its performance in diverse domains, such as mathematical reasoning and data analysis. A benchmark has been developed and made publicly available for this purpose (see Qwen Team, Alibaba Group, 2023a).

[p. 16] The benchmark encompasses three primary categories of tasks: math problem-solving, data visualization, and other general-purpose tasks like file post-processing and web crawling. Within the visualization tasks, two levels of difficulty are differentiated. The easier level can be achieved by simply writing and executing a single code snippet without the need for advanced planning skills. However, the more challenging level requires strategic planning and executing multiple code snippets in a sequential manner. This is because the subsequent code must be written based on the output of the previous code. For example, an agent may need to examine the structure of a CSV file using one code snippet before proceeding to write and execute additional code to create a plot.

### Evaluation metrics for code interpreter

[p. 16] Regarding evaluation metrics, both the executability and the correctness of the generated code are considered. To elaborate on the correctness metrics, for math problems, accuracy is measured by verifying if the ground truth numerical answer is present in both the code execution result and the final response. When it comes to data visualization, accuracy is assessed by utilizing QWEN-VL (Bai et al., 2023), a powerful multimodal language model. QWEN-VL is capable of answering text questions paired with images, and is relied on to confirm whether the image generated by the code fulfills the user's request.

**Table 7: The proportion of code generated by QWEN that is executable on the in-house evaluation benchmark for Code Interpreter.** This benchmark examines QWEN's coding proficiency in math problem solving, data visualization, and general purposes. CODE LLAMA underperforms on visualization tasks because it hallucinates non-existent columns solely based on CSV file names (see Figure 5). [p. 14]

| Model | Params | Math (%) | Visualization (%) | General (%) | All (%) |
|---|---|---|---|---|---|
| GPT-4 | - | 91.9 | 85.9 | 82.8 | 86.8 |
| GPT-3.5 | - | 89.2 | 65.0 | 74.1 | 72.9 |
| LLAMA 2-CHAT | 7B | 41.9 | 33.1 | 24.1 | 33.6 |
| | 13B | 50.0 | 40.5 | 48.3 | 44.4 |
| CODE LLAMA-INSTRUCT | 7B | 85.1 | 54.0 | 70.7 | 65.1 |
| | 13B | 93.2 | 55.8 | 74.1 | 68.8 |
| InternLM-Chat | 7B v1.1 | 78.4 | 44.2 | 62.1 | 56.3 |
| | 20B | 70.3 | 44.2 | 65.5 | 54.9 |
| QWEN-CHAT | 1.8B | 33.8 | 30.1 | 8.6 | 26.8 |
| | 7B | 82.4 | 64.4 | 67.2 | 70.2 |
| | 14B | 89.2 | 84.1 | 65.5 | 81.7 |

**Table 8: Correctness of the final response on the in-house evaluation benchmark for Code Interpreter.** Visualization-Hard tasks involve planning multiple steps, while Visualization-Easy tasks do not. Visualization-All measures both types of tasks. CODE LLAMA excels in performing Visualization-Easy tasks but tends to underperform in Visualization-Hard tasks, due to its inclination to hallucinate non-existent columns based on the name of a CSV file (see Figure 5). [p. 14]

| Model | Params | Math (%) | Vis.-Hard (%) | Vis.-Easy (%) | Vis.-All (%) |
|---|---|---|---|---|---|
| GPT-4 | - | 82.8 | 66.7 | 60.8 | 63.8 |
| GPT-3.5 | - | 47.3 | 33.3 | 55.7 | 44.2 |
| LLAMA 2-CHAT | 7B | 3.9 | 14.3 | 39.2 | 26.4 |
| | 13B | 8.3 | 8.3 | 40.5 | 23.9 |
| CODE LLAMA-INSTRUCT | 7B | 14.3 | 26.2 | 60.8 | 42.9 |
| | 13B | 28.2 | 27.4 | 62.0 | 44.2 |
| InternLM-Chat | 7B v1.1 | 28.5 | 4.8 | 40.5 | 22.1 |
| | 20B | 34.6 | 21.4 | 45.6 | 33.1 |
| QWEN-CHAT | 1.8B | 14.7 | 3.6 | 20.3 | 11.7 |
| | 7B | 41.9 | 40.5 | 54.4 | 47.2 |
| | 14B | 58.4 | 53.6 | 59.5 | 56.4 |

[p. 16] The results regarding executability and correctness are presented in Table 7 and Table 8, respectively. It is evident that CODE LLAMA generally outperforms LLAMA 2, its generalist counterpart, which is not surprising since this benchmark specifically requires coding skills. However, it is worth noting that specialist models that are optimized for code synthesis do not necessarily outperform generalist models. This is due to the fact that this benchmark encompasses various skills beyond coding, such as abstracting math problems into equations, understanding language-specified constraints, and responding in the specified format such as ReAct. Notably, QWEN-7B-CHAT and QWEN-14B-CHAT surpass all other open-source alternatives of similar scale significantly, despite being generalist models.

## Serving as a Hugging Face Agent

[p. 16] Hugging Face provides a framework called the Hugging Face Agent or Transformers Agent (Hugging Face, 2023), which empowers LLM agents with a curated set of multimodal tools, including speech recognition and image synthesis. This framework allows an LLM agent to interact with humans, interpret natural language commands, and employ the provided tools as needed.

[p. 16] To evaluate QWEN's effectiveness as a Hugging Face agent, the evaluation benchmarks offered by Hugging Face are utilized. The results are presented in Table 9.

**Table 9: Results of QWEN-Chat on the Hugging Face Agent benchmark.** [p. 15]

| Task | Model | Params | Tool Selection ↑ | Tool Used ↑ | Code Correctness ↑ |
|---|---|---|---|---|---|
| Run Mode | GPT-4 | - | 100 | 100 | 97.4 |
| | GPT-3.5 | - | 95.4 | 96.3 | 87.0 |
| | Starcoder-Base | 15B | 86.1 | 87.0 | 68.9 |
| | Starcoder | 15B | 87.0 | 88.0 | 68.9 |
| | QWEN-CHAT | 1.8B | 85.2 | 84.3 | 61.1 |
| | | 7B | 87.0 | 87.0 | 71.5 |
| | | 14B | 93.5 | 94.4 | 87.0 |
| Chat Mode | GPT-4 | - | 97.9 | 97.9 | 98.5 |
| | GPT-3.5 | - | 97.3 | 96.8 | 89.6 |
| | Starcoder-Base | 15B | 97.9 | 97.9 | 91.1 |
| | Starcoder | 15B | 97.9 | 97.9 | 89.6 |
| | QWEN-CHAT | 1.8B | 93.6 | 93.6 | 73.2 |
| | | 7B | 94.7 | 94.7 | 85.1 |
| | | 14B | 97.9 | 97.9 | 95.5 |

[p. 16] The evaluation results reveal that QWEN performs quite well in comparison to other open-source alternatives, only slightly behind the proprietary GPT-4, demonstrating QWEN's competitive capabilities.
