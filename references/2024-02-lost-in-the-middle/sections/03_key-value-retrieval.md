# 3 How Well Can Language Models Retrieve From Input Contexts? [p. 6]

Given that language models struggle to retrieve and use information from the middle of their input contexts in the multi-document question answering task, to what extent can they simply *retrieve* from input contexts? This is studied with a synthetic key-value retrieval task, which is designed to provide a minimal testbed for the basic ability to retrieve matching tokens from an input context. [p. 6]

## 3.1 Experimental Setup [p. 6]

In the synthetic key-value retrieval task, the inputs are (i) a string-serialized JSON object with *k* key-value pairs, where each of the keys and values are unique, randomly-generated UUIDs and (ii) a key within the aforementioned JSON object. The goal is to return the value associated with the specified key. Thus, each JSON object contains one relevant key-value pair (where the value is to be returned), and *k - 1* irrelevant "distractor" key-value pairs. Figure 6 provides an example input context and its corresponding desired output. Accuracy is again measured by evaluating whether the correct value appears in the predicted output. [p. 6]

The synthetic key-value retrieval task shares similar goals with the Little Retrieval Test of Papailiopoulos et al. (2023) and the fine-grained line retrieval task of Li et al. (2023), but explicitly seeks to distill and simplify the task by removing as much natural language semantics as possible (using random UUIDs instead), since language features may present potential confounders. For example, Transformer language models may have varying sensitivity to different linguistic features in their input (O'Connor and Andreas, 2021). [p. 6]

To modulate the position of relevant information within the input context, the position of the key to retrieve within the serialized JSON object is changed. To modulate the input context length, the number of input JSON key-value pairs *k* is changed by adding or removing random keys, changing the number of distractor key-value pairs. [p. 6]

**Figure 6** (p. 6): "Example of the key-value retrieval task, with an input context and the desired model output. Given a key, the goal is to return the associated value. All keys and values are 128-bit UUIDs. The relevant key-value pair for answering the query is bolded here within the input context for clarity."

The figure shows an input context with a prompt: "Extract the value corresponding to the specified key in the JSON object below." A JSON object with 6 key-value pairs of UUID format is shown, with one pair bolded ("9f4a92b9-5f69-4725-bale-403f08dea695": "703a7ce5-f17f-4e6d-b895-5836ba5ec71c"). The key to extract is specified below the JSON, and the desired output is "703a7ce5-f17f-4e6d-b895-5836ba5ec71c".

## 3.2 Results and Discussion [p. 6]

Experiments use input contexts containing 75, 140, and 300 key-value pairs (500 examples each). The same set of models as the multi-document question answering experiments are used (see section 2.2 for more details). [p. 6]

Figure 7 presents key-value retrieval performance. Claude-1.3 and Claude-1.3 (100K) do nearly perfectly on all evaluated input context lengths, but other models struggle, especially when contexts have 140 or 300 key-value pairs -- although the synthetic key-value retrieval task only requires identifying exact match within the input context, not all models achieve high performance. [p. 6]

Similar to the multi-document QA results, GPT-3.5-Turbo, GPT-3.5-Turbo (16K), and MPT-30B-Instruct have the lowest performance when they must access key-value pairs in the middle of their input context. LongChat-13B (16K) exhibits a different trend in the 140 key-value setting; the authors qualitatively observe that when relevant information is placed at the start of the input context, LongChat-13B (16K) tends to generate code to retrieve the key, rather than outputting the value directly. [p. 6-7]

**Figure 7** (p. 7): "The effect of changing the input context length and the position of relevant information on key-value retrieval performance. Lower positions are closer to the start of the input context. Although some models show perfect accuracy on this synthetic task (e.g., Claude-1.3 and Claude-1.3 (100K)), we see again that performance is often highest when relevant information is occurs at the very start or end of the context, and rapidly degrades when models must retrieve from the middle of the input context."

Three panels showing results for 75 (approximately 4K tokens), 140 (approximately 8K tokens), and 300 (approximately 16K tokens) key-value pairs. Each panel plots accuracy (y-axis, 40-100%) vs. position of key to retrieve (x-axis). Six models are shown: claude-1.3, claude-1.3-100k, gpt-3.5-turbo-0613, gpt-3.5-turbo-16k-0613, mpt-30b-instruct, and longchat-13b-16k. Claude-1.3 and Claude-1.3 (100K) achieve near-perfect accuracy across all settings. GPT-3.5-Turbo, GPT-3.5-Turbo (16K), and MPT-30B-Instruct show U-shaped curves with lowest performance in the middle. In the 75 key-value pair setting, most models perform above 80%. In the 300 key-value pair setting, non-Claude models drop to 40-60% accuracy in the middle positions.
