# 2 Detecting Retrieval Head [p. 3]

To detect which head is implementing the retrieval algorithm, the authors introduce a *retrieval score* to measure the frequency of a head's copy-paste behavior during autoregressive decoding. An attention head with high retrieval score suggests that across various contexts, this head is frequently copying the input tokens from the input to the output.

## Needle-in-a-Haystack [p. 3]

The retrieval head detection algorithm roots from the needle-in-a-Haystack test, which asks the model to copy-paste input tokens to the output. Given a question q and its corresponding answer k (the needle), the authors insert k in a given context x (the haystack) at a random position index range i_x. The language model is then tasked to answering q based on the haystack with the inserted needle. The authors set q and k unique and irrelevant with the given long context, ensuring that if an answer is correctly generated, it is indeed copied from the context, not from the model's internal knowledge.

## Retrieval Score for Attention Heads [p. 3]

The authors define the retrieval score as the frequency of a head's copy-paste operations. Specifically, during auto-regressive decoding (greedy decoding by default), denote the current token being generated as w and the attention scores of a head as a ∈ ℝ^|x|. As demonstrated in Fig. 2, the authors say an attention head h copies and pastes a token from the needle to the output sentence if it follows two criteria: (1) i.e., w is a token within the needle sentence. (2) x_j = w, j = arg max(a), j ∈ i_x, i.e., the input token that receives the most attention probability mass by this head is a token within the needle and is the same token as the currently generated token. Let g_h be the set containing all tokens copy and pasted by a given head h, the authors define:

$$\text{Retrieval score for head } h = \frac{|g_h \cap k|}{|k|}$$ (1)

Intuitively, retrieval score represents a token-level recall rate of the most attended tokens by an attention head. For example, when retrieving a needle of 10 tokens, a retrieval score of 0.9 indicates that the attention head has copies and pastes 9 out of the 10-token target answer.

**Figure 2** (p. 3): "An attention head that performs a copy-paste operation if the token that the head attend to is the same the token being generated. The retrieval score of a head is defined as the frequency of this head's copy-paste behavior when answering questions that asks for raw information from the input."

Description: Line diagram showing attention distribution of a retrieval head across a context.
- Key elements: Horizontal timeline showing "Once upon a time", "The best thing to do in San Francisco...", "Needle sentence", "100K context", and "live happily ever after"; vertical spike showing high attention to "The best thing to do in San Francisco"; question shown as "Q: What is the best thing to do in San Francisco?" with answer "A: to eat ..."
- Notable patterns: Single prominent attention spike at the needle location within long context (100K tokens)
- Supports claim: Retrieval heads attend strongly to specific tokens in the input that match the information being generated

## Retrieval Head Detection Algorithm [p. 3]

The authors calculate the retrieval score for all attention heads under a diverse set of input contexts. For each language model considered, they compile three sets of Needle-in-a-Haystack samples, each consisting of a unique tuple (q, k, x). For each sample, the authors make sure (q, k) is semantically irrelevant with x and that q cannot be answered using the model's existing knowledge by manually inspecting the model output. Then for each (q, k, x) sample, the authors
