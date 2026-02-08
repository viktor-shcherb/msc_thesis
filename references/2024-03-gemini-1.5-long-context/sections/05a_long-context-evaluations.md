# 5.2. Long-context Evaluations [p. 9–11]

[p. 9] For the past few years, LLM research has prioritized expanding the context window from which models can incorporate information (Anthropic, 2023a; OpenAI, 2023a). This emphasis stems from the recognition that a wider context window allows models to incorporate a larger amount of new, task-specific information not found in the training data at inference time, leading to improved performance in various natural language or multimodal tasks.

Recent approaches to improving the long-context capabilities of models fall into a few categories:
- **Novel architectural approaches:** Ainslie et al., 2023; Gu and Dao, 2023; Guo et al., 2021; Orvieto et al., 2023; Zaheer et al., 2020
- **Post-training modifications:** Bertsch et al., 2023; Chen et al., 2023b; Press et al., 2021; Xiong et al., 2023
- **Retrieval-augmented models:** Guu et al., 2020; Izacard et al., 2022; Jiang et al., 2022; Karpukhin et al., 2020; Santhanam et al., 2021
- **Memory-augmented models:** Bulatov et al., 2022, 2023; Martins et al., 2022; Mu et al., 2023; Wu et al., 2022a,b; Zhong et al., 2022
- **Techniques for building more coherent long-context datasets:** Shi et al., 2023b; Staniszewski et al., 2023

[p. 9–10] This activity has resulted in measurable improvements on long-context capabilities of LLMs over the past several months, with the recent concurrent work of Liu et al. (2024) exploring context window of 7B models up to 1M multimodal tokens. Notably, among the state-of-the-art LLMs, Anthropic has successfully extended the context of their text-only Claude 2 model to 100k tokens, while OpenAI has recently released GPT-4 Turbo reaching 128k tokens. Finally, the latest addition to the series was Claude 3 with a context window of up to 1M tokens.

[p. 10] Gemini 1.5 Pro significantly extends this context length frontier to multiple millions of tokens with almost no degradation in performance, making it possible to process significantly larger inputs. Key recall results:
- Compared to Claude 2.1 with a 200k token context window, Gemini 1.5 Pro achieves 100% recall at 200k tokens, surpassing Claude 2.1's 98%
- This 100% recall is maintained up to 530k tokens
- Recall is 99.7% at 1M tokens
- When increasing from 1M tokens to 10M tokens, the model retains 99.2% recall

Moreover, Gemini 1.5 Pro's native multimodal capabilities enable the model to ingest multiple hours of audio and video recordings alongside or interleaved with text. Such recall capabilities are summarized in Figure 1. Results on long-context evaluations are reported across all three modalities: text, vision, and audio. [p. 10]

Similarly, Gemini 1.5 Flash achieves almost perfect recall across all three modalities up to 2M tokens, yielding 100% recall on text, 99.8% on video, and 99.1% on audio. [p. 10]

The evaluation methodology consists of both diagnostic-focused probing of the long context capabilities (e.g., perplexity over long sequences, needle-in-a-haystack retrieval studies) and realistic evaluations specifically designed for multimodal long-context tasks (e.g., long-document QA, long-context automatic speech recognition, learning to translate a new language from only one book, and long-context video QA). Throughout this section, Gemini 1.5 models are compared with the leading model available externally for each task. With the evaluation harness developed for Gemini 1.5 models, they are able to quantify the quality of long-context understanding capabilities reliably all the way up to 10M tokens. [p. 10]

## 5.2.1. Diagnostic Long-Context Evaluations

### 5.2.1.1 Perplexity over Long Sequences

[p. 10–11] The authors start by reporting results on the text modality. To evaluate the ability of the models to make use of very long contexts to improve next-token prediction, they record the negative log-likelihood (NLL) of tokens at different positions in the input sequences from held-out text (i.e., not used in training). A lower value implies improved prediction.

Expected behavior: tokens at the beginning of a sequence have high NLL (little to no context for prediction), while tokens later in the sequence have lower NLL as more information becomes available. A downward trend signifies models making use of long-context to reduce uncertainty. An upward trend signifies that models are unable to effectively use information from previous context and may be deteriorating in prediction quality. [p. 11]

Two data sources are used:
- **(a)** A dataset of long documents with up to 1 million tokens
- **(b)** A dataset of code repositories constructed by first randomly shuffling all the files and then concatenating them. The code dataset contains sequences longer than 1 million tokens with some natural form of semantic association (e.g., a whole repository), allowing for further evaluation of sequences of up to 10M tokens.

A power law of the form $L(x) = \alpha x^{\beta} + \gamma$ is also fit to these data points (dashed line). [p. 11]

**Figure 7** (p. 10): "Cumulative average negative log-likelihood (NLL) as a function of token position in long documents and code data. A lower value demonstrates better prediction. Gemini 1.5 Pro shows improved predictions up to 1M tokens for long-documents and 10M tokens for code, whereas Gemini 1.0 Pro improves up to only 32K tokens. Gemini 1.5 Flash shows improvement up to 1M tokens for long-documents and 2M tokens in code. The NLL of Gemini 1.5 Pro follows a power-law trend up until 1M tokens (documents) and 2M tokens (code) with a deviating trend at 10M tokens."
- **Left panel:** "Cumulative Average NLL for Long Documents. R^2 = 0.997." X-axis: Sequence position (128 to 1M). Y-axis: Negative Log Likelihood. Three models plotted: Gemini 1.5 Flash, Gemini 1.0 Pro, Gemini 1.5 Pro, plus a power law fit (dashed). All three models show decreasing NLL with sequence position, but Gemini 1.5 Pro and 1.5 Flash continue decreasing far beyond Gemini 1.0 Pro.
- **Right panel:** "Cumulative Average NLL for Code. R^2 = 0.995." X-axis: Sequence position (128 to 10M). Y-axis: Negative Log Likelihood. Same three models plotted. Gemini 1.5 Pro continues improving up to 10M tokens; the power-law fit deviates around 10M.

[p. 11] Key findings from Figure 7:
- NLL decreases monotonically with sequence length, and thus prediction accuracy improves up to the tested sequence lengths (1M for long documents and 10M for code)
- This indicates that Gemini 1.5 models are able to make use of the whole input even at very long-context lengths
- This suggests that Gemini 1.5 models can improve their predictions by finding useful patterns in tokens, even if they occurred millions of tokens in the past (as in the case of code)

The improved prediction follows a regular power-law structure. While it is well known that language models follow a power-law in terms of training compute to model performance (NLL) (Kaplan et al., 2020) up to a very large scale, the authors demonstrate that a power law can hold between log-loss and context length up to extremely long context lengths. The power-law fit is quite accurate up to 1M tokens for long-documents and about 2M tokens for code for Gemini 1.5 Pro. From inspecting longer code token predictions closer to 10M, there is a phenomenon of the increased context occasionally providing outsized benefit (e.g. due to repetition of code blocks) which may explain the power-law deviation. The authors note this deserves further study and may be dependent on the exact dataset used. [p. 11]

### 5.2.1.2 Text Haystack

[p. 11] Long-context recall is tested using the needle-in-a-haystack evaluation (Kamradt, 2023), which tests a model's ability to retrieve a text (i.e., "needle") inserted at various positions into a sequence (i.e., "haystack"). Following prior work (Dhinakaran, 2024), a set of concatenated and repeated essays written by Paul Graham^8 is used to fill the desired context length.

A needle is inserted at linearly spaced intervals from the beginning to the end of the context. The needle format is:

> "The special magic {city} number is: {number}" [p. 11]

where the city and number are varied for each query. The model is queried to return the magic number for a specific city. Recall of the magic number is reported as correct at various context lengths (x axis -- the haystack) as a function of its position in the input sequence expressed in terms of depth percentage (y axis), where depth at 100% indicates a needle inserted at the very end of the input and 0% at the very beginning.

[p. 11–12] As can be seen in Figure 8, Gemini 1.5 Pro achieves 100% recall up to 530k tokens and >99.7% recall up to 1M tokens. This task, while simple, provides a clear demonstration that Gemini 1.5 Pro is able to reliably retrieve information from long documents up to 1M tokens. For reference, results for GPT-4 Turbo up to the 128K sequence length supported by their API are also reported.

In order to test whether the capabilities demonstrated in the perplexity plots in Figure 7 transfer to sampling tasks, Gemini 1.5 Pro is further evaluated on the needle-in-a-haystack task beyond 1M tokens. The results in Figure 8 show that the model is still able to find and extract information with 99.2% accuracy up to 10M tokens. On the same task, Gemini 1.5 Flash was also evaluated up to 2M tokens and attained a flawless recall of 100%, suggesting its best in class long-context text retrieval performance, which is exclusive in its tier of models. [p. 12]

In Section 9.4.1, the authors also showcase an "adversarial" version of this needle-in-the-haystack task for long context safety evaluations. [p. 12]

**Figure 8** (p. 12): "Text Haystack. This figure compares Gemini 1.5 Pro with GPT-4 Turbo for the text needle-in-a-haystack task. Green cells indicate the model successfully retrieved the secret number, gray cells indicate API errors, and red cells indicate that the model response did not contain the secret number. The top row shows results for Gemini 1.5 Pro, from 1k to 1M tokens (top left), and from 1M to 10M tokens (top right). The bottom row shows results on GPT-4 Turbo up to the maximum supported context length of 128k."
- **Top left panel (Gemini 1.5 Pro: From 1k to 1M tokens):** A heatmap grid with x-axis "Tokens" (32k to 1M) and y-axis "Depth (%)" (0 to 100). Almost entirely green cells, with a small number of red cells appearing around 512k tokens at various depths (approximately depth 29, 57, 71, and 86). Demonstrates near-perfect recall across all positions and context lengths up to 1M tokens.
- **Top right panel (Up to 10M tokens):** A smaller heatmap with x-axis "Tokens" (2M, 5M, 10M). Almost entirely green with one red cell visible around 5M at depth ~14. Demonstrates that recall extends to 10M tokens with 99.2% accuracy.
- **Bottom panel (GPT-4 Turbo: From 1k to 128k tokens):** A heatmap grid with x-axis "Tokens" (32k to 512k) and y-axis "Depth (%)" (0 to 100). Green cells from 32k to about 64k, then increasingly gray cells (API errors) and red cells (failures) at larger context lengths. GPT-4 Turbo is limited to 128K context. Shows notably more failures and API errors compared to Gemini 1.5 Pro.

> ^7 "We note that we are unable to obtain logits for other commercially available LLMs for comparison." [p. 11]

> ^8 https://paulgraham.com/articles.html [p. 11]
