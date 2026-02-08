# The RULER Benchmark [p. 3-6]

[p. 3] RULER comprises tasks across four categories: *retrieval*, *multi-hop tracing*, *aggregation*, and *question answering*. Evaluation examples in RULER are automatically generated based on input configurations (see Table 2) that define the length and complexity of each input. Within a constrained domain as in RULER, the task complexity can be thought of as a function of the number of target output tokens and the signal-to-noise ratio in the context. The authors point readers to Goldman et al. (2024) for more comprehensive discussion on evaluation task design for long-context language models.

**Table 2** (p. 4): Task examples with flexible configurations in RULER. Different colors highlight queries, keys, values, and distractors in the examples.

| Task | Configuration | Example |
|------|--------------|---------|
| Single NIAH (S-NIAH) | type_key = word, type_value = number, type_haystack = essay, size_haystack proportional to context length | (essays)... One of the special magic numbers for long-context is: 12345. ... What is the special magic number for long-context mentioned in the provided text? Answer: 12345 |
| Multi-keys NIAH (MK-NIAH) | num_keys = 2, type_key = word, type_value = number, type_haystack = essay, size_haystack proportional to context length | (essays)... One of the special magic numbers for long-context is: 12345. One of the special magic numbers for large-model is: 54321. ... What is the special magic number for long-context mentioned in the provided text? Answer: 12345 |
| Multi-values NIAH (MV-NIAH) | num_values = 2, type_key = word, type_value = number, type_haystack = essay, size_haystack proportional to context length | (essays)... One of the special magic numbers for long-context is: 12345. One of the special magic numbers for long-context is: 54321. ... What are all the special magic numbers for long-context mentioned in the provided text? Answer: 12345 54321 |
| Multi-queries NIAH (MQ-NIAH) | num_queries = 2, type_key = word, type_value = number, type_haystack = essay, size_haystack proportional to context length | (essays)... One of the special magic numbers for long-context is: 12345. One of the special magic numbers for large-model is: 54321. ... What are all the special magic numbers for long-context and large-model mentioned in the provided text? Answer: 12345 54321 |
| Variable Tracking (VT) | num_chains = 2, num_hops = 2, size_noises proportional to context length | ... VAR X1 = 12345 ... VAR Y1 = 54321 ... VAR X2 = X1 ... VAR Y2 = Y1 ... VAR X3 = X2 ... VAR Y3 = Y2 ... Find all variables that are assigned the value 12345. Answer: X1 X2 X3 |
| Common Words Extraction (CWE) | freq_cw = 2, freq_ucw = 1, num_cw = 10, num_ucw proportional to context length | aaa bbb ccc aaa ddd ccc ccc fff ggg bbb iii iii ... What are the 10 most common words in the above list? Answer: aaa ccc iii ... |
| Frequent Words Extraction (FWE) | a = 2, num_word proportional to context length | aaa bbb ccc aaa ddd ccc ccc fff ggg aaa bbb aaa ccc iii iii ... What are the 3 most frequently appeared words in the above coded text? Answer: aaa ccc iii |
| Question Answering (QA) | dataset = SQuAD, num_document proportional to context length | Document 1: ... aaa ... Document 2: ... bbb ... Document 3: ... ccc ... Question: question Answer: bbb |

## 3.1 Retrieval: Needle-in-a-haystack (NIAH)

[p. 3-4] Recent works (Reid et al., 2024; Anthropic, 2023) commonly employ the needle-in-a-haystack (Kamradt, 2023; NIAH) test to evaluate long-context modeling capability. The NIAH test is reminiscent of the extensively studied (Hopfield, 1982; Graves et al., 2014; Olsson et al., 2022; Arora et al., 2024) *associative recall* tasks, in which relevant information needs to be retrieved from context given a sufficient query.

In RULER, the authors include multiple retrieval-based tasks, extending the vanilla NIAH test to evaluate models based on three criteria. Concretely, the retrieval capability should be (1) agnostic to the type of the "needle" and the "haystack", (2) strong enough to disregard hard distractors, and (3) of high recall when multiple items need to be retrieved. Based on these criteria, four NIAH tasks are developed:

[p. 4] The "needle" in each of these tasks is a *key-value* pair inserted into the "haystack" (long distractor texts). The *query* is located at the end of the sequence and serves as a cue for matching the *keys* in the context and subsequently retrieving the associated *values*.

- **Single NIAH (S-NIAH):** The vanilla NIAH test where a single "needle" needs to be retrieved from the "haystack". The query/key/value can take the form of words, numbers (7 digits), or UUIDs (32 digits). The "haystack" can be repeated noise sentences or Paul Graham essays (Kamradt, 2023).

- **Multi-keys NIAH (MK-NIAH):** Multiple "needles" are inserted into the "haystack", and only one of them needs to be retrieved. The additional "needles" are hard distractors. The most challenging setting is a version where the "haystack" is filled with distractor needles.

[p. 5]
- **Multi-values NIAH (MV-NIAH):** Multiple "needles" sharing the same *key* are inserted into the "haystack". All *values* associated with the same *key* need to be retrieved.

- **Multi-queries NIAH (MQ-NIAH):** Multiple "needles" with distinct keys need to be retrieved. All "needles" with distinct keys need to be retrieved from the "haystack". This is the same *multi-query associative recall* task setup used by Arora et al. (2024). Together with MV-NIAH, these two tasks evaluate the retrieval capability without missing any critical information.

Footnotes:
- Similar to Liu et al. (2024a), the authors use *"the special magic number for XXX is: YYY"* as the needle due to its extendability instead of the sentence about San Francisco proposed by Kamradt (2023). [p. 4, footnote 2]
- Following Mohtashami & Jaggi (2023), the authors use *"The grass is green. The sky is blue. The sun is yellow. Here we go. There and back again."* as noise sentences. [p. 4, footnote 3]

## 3.2 Multi-hop Tracing: Variable Tracking (VT)

[p. 5] Effective discourse comprehension (van Dijk & Kintsch, 1983) is contingent upon successful recognition of newly mentioned entities and establishing the chain of references co-referring to the same entity (Karttunen, 1969) throughout the long context. The authors develop a new task *variable tracking* to emulate a minimal coreference chain resolution (Ng, 2010) task. This task checks the behavior of tracking relevant co-occurrence patterns and drawing skipped connections within long input.

Specifically, a variable X1 is initialized with a value V, followed by a linear *chain* of variable name binding statements (e.g., X2 = X1, X3 = X2, ...), which are inserted at various positions of the input. The objective is to return *all* variable names pointing to the same value V. The task complexity can be increased by adding more hops (i.e., the times of name binding) or more chains, similar to adding hard distractors in MK-NIAH.

## 3.3 Aggregation: Common Words (CWE) and Frequent Words Extraction (FWE)

[p. 5] The authors introduce a new category as a proxy for summarization tasks where relevant information constitutes much larger portion of the context, and the target output depends on accurate aggregation of the relevant input.

**Common Words Extraction (CWE):** An input sequence is constructed by sampling words from a pre-defined (synthetic) word list. Words are sampled from discrete uniform distributions, with the number of common words fixed while the number of uncommon words increases with the sequence length. A model needs to return the top-*K* frequent words in the context. In CWE, *K* equals to the number of common words.

**Frequent Words Extraction (FWE):** Words are sampled from Zeta distribution. The authors set *K* to 3, as increasing *K* leads to poor performance even at small context sizes for most models.

The task complexity can be adjusted by varying the number of common words or the parameter of the Zeta distribution.

**Figure 1** (p. 5): "In aggregation tasks, we sample words from a vocabulary following the two distributions above. The common words extraction (CWE) samples from uniform distributions. In the frequent words extraction (FWE), the frequency of each word is determined by its rank in the vocabulary and the parameter alpha of Zeta distribution."

The figure contains two subplots:
- **Left (CWE):** Bar chart with "Word types" on x-axis and "Word Freq." on y-axis (0-30). Shows two distributions: "Common words" (higher frequency, ~30) and "Uncommon words" (lower frequency, ~5). Uniform distributions for both groups.
- **Right (FWE):** Line plot with "log (Word rank)" on x-axis and "log (Word Freq.)" on y-axis (0-8). Shows curves for four values of alpha: 1.5, 2.0, 2.5, 3.0. Higher alpha values produce steeper slopes, indicating more concentrated frequency at top-ranked words.

Footnote 4 [p. 5]: The authors draw inspiration from Zipf's Law (Kingsley Zipf, 1932). Let *N* be the total number of words, which is determined by the context size, the frequency of the *k*-th ranked word (the *k*-th most frequently appeared word) is k^{-a} * N / zeta(a), where zeta(a) is the Zeta function. The top-ranked word is set to noise.

## 3.4 Question Answering (QA)

[p. 5-6] The majority of existing QA datasets (Rajpurkar et al., 2018; Yang et al., 2018; Trivedi et al., 2022) are designed to answer questions based on short passages. These datasets can be extended to simulate long-context input by adding distracting information. In this task category, the authors insert the golden paragraphs (i.e., the paragraphs that contain answers) into paragraphs randomly sampled from the same dataset. This category is a real-world adaptation (Ivgi et al., 2023) of NIAH, where the question serves as the query, the golden paragraphs are the "needles", and the distracting paragraphs form the "haystack".
