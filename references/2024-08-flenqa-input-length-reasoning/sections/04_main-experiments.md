# 4 Main Experiments [p. 5-6]

[p. 5] Average accuracies over all three tasks are reported, and the same setup (prompt, temperature, etc.) is maintained over all input lengths. Five recent capable LLMs are evaluated: GPT4, GPT3.5, Gemini-Pro, Mistral Medium and Mixtral 8x7B. An output where no answer was mentioned (e.g "I don't know") is considered as incorrect. See Appendix C for a detailed breakdown of setup parameters.

## 4.1 Impact of Length and Location [p. 5-6]

The authors start by validating the impact of input length on LLM reasoning performance (Figure 1) in various experimental settings.

**No irrelevant paragraphs** [p. 5-6]: The extreme case where only relevant tokens are added ("duplicate padding") is examined first. Shi et al. (2023) demonstrate that appending irrelevant texts to the input of a reasoning task (GSM-8K (Cobbe et al., 2021)) reduces model performance substantially. The authors isolate the effect of relevance by testing a setting in which the padding is duplications of the exact text of the key paragraphs. In this setup, the LLMs are not required to "search" the input to find the key paragraphs, so any bias towards any position becomes irrelevant (Liu et al., 2023b). Also, any difficulty that might be imposed by the distance between the key paragraphs also becomes irrelevant. The expectation was that there will be no degradation in performance. The results shown in Figure 3 reveal that even in this setup length does play a factor, *and accuracy decreases with length for all models*. The authors consider these results surprising: duplicated texts are an artificial setup which is arguably the best case scenario of long inputs, as the information is constantly repeated and there is no distracting text. In more natural cases, most of the input is irrelevant to the question asked.

**Figure 3** (p. 6): "The relevance of padding is a factor, but it is distinct from the effect of length itself. Some models degrade in reasoning performance. Note, both GPT3.5 and GPT4 are less affected by length when the added tokens are relevant. Each point reflects 300 samples."
- Title: "Accuracy with duplicated key paragraphs"
- X-axis: Input length (# tokens), values: 250, 500, 1000, 1500, 2000, 2500, 3000
- Y-axis: Accuracy, range 0.80 to 1.00
- Lines for GPT3.5, GPT4, Gemini Pro, Mistral Medium, Mixtral 8x7B
- GPT3.5 and GPT4 remain relatively flat (less affected). Gemini Pro, Mistral Medium, and Mixtral 8x7B show more degradation, with Mixtral 8x7B dropping most sharply (to approximately 0.80 at 3000 tokens).

[p. 6] **Adjacent paragraphs surrounded by irrelevant ones:** The more realistic case where the prompt includes the key paragraphs as well as additional irrelevant ones is examined. In the first set of experiments, the key paragraphs are kept adjacent to each other: the LLM just needs to focus and operate on a single area of the input, ignoring the rest. Liu et al. (2023b) found that in the task of extractive QA, the position of the answer in the text affects the ability of models to answer correctly. They thus experiment with the three scenarios: positioning both key paragraphs at the start, end or middle of the text. In all cases they average over both types of irrelevant padding.

**Figure 4** (p. 6): "Accuracy decreases as input length grows regardless of where the key paragraphs are placed within the input. Each point reflects 300 samples. Results for all models appear in Appendix C"
- Title: "Mistral Medium accuracy on different key paragraph locations"
- X-axis: Input length (# tokens), values: 250, 500, 1000, 1500, 2000, 2500, 3000
- Y-axis: Accuracy, range approximately 0.7 to 1.0
- Lines for First, Last, Middle, Random placement
- All lines show declining accuracy with length. "Last" placement tends to yield highest accuracy (suggesting recency bias). "Random" placement shows the steepest decline. All positions converge toward lower accuracy at 3000 tokens.

The results in Figure 4 show a significant drop in accuracy as length increases beyond 500 tokens. For most models, adjacency of key paragraphs produces higher accuracy, and when the key paragraphs appear last, accuracy is often highest (suggesting recency bias). Some models perform worse when the key paragraphs are in the middle, similarly to what was found in the extraction task studied recently (Liu et al., 2023b).

**Non-adjacent relevant paragraphs:** Finally, the scenario in which the relevant facts need to be collected from two non-adjacent locations within the text is tested. The results in Figure 1 show a very large drop in performance as length increases, indicating that reasoning tasks becomes significantly harder for LLMs when they need to collect evidence from two distinct locations in a large-ish context length.

## 4.2 Kind of irrelevant material [p. 6]

The focus is now only on the non-adjacent key-paragraphs case. Two scenarios are explored: when the irrelevant paragraphs are *similar* to the relevant ones (taken from the same task), and when they are *different* (taken from the books corpus).

**Figure 5** (p. 6): "Performance degrade in both types of padding. Books padding impact is much greater in most models. Each point reflects the performance across 300 samples."
- Title: "Accuracy on different padding types"
- X-axis: Input length (# tokens), values: 250, 500, 1000, 1500, 2000, 2500, 3000
- Y-axis: Accuracy, range 0.6 to 1.0
- Lines for GPT3.5, GPT4, Gemini Pro, Mistral Medium, Mixtral 8x7B
- Dashed lines for Books Corpus, solid lines for Resampling
- Performance degrades in both types of padding. The Books Corpus (different) padding impact is much greater in most models, contrary to the initial expectation that different text would be easier to discard.

The initial expectation was that the setup in which the irrelevant paragraphs are *different* from the relevant ones will be easier for the model, as the irrelevant paragraphs will be easier to discard, aiding focusing on the relevant ones. However, the results (Figure 5) show that is not the case: the drop for the *different* setup is mostly larger than for the *similar* one.
