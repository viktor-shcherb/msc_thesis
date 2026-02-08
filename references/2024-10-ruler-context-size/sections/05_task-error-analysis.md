# Task Error Analysis [p. 7-9]

[p. 7] The authors evaluate Yi-34B-200K with increased input lengths (up to 256K) on more complex tasks to understand the effect of task configurations and failure modes on RULER.

## Non-robustness to "needle" types

[p. 7] Figure 2 (left) shows that while Yi achieves almost perfect performance when using needle of word-number pair in the standard passkey retrieval and vanilla NIAH, performance degrades when the needle takes other forms. The largest degradation is observed in the task of retrieving UUIDs (32 digits), for which Yi sometimes fails to return the complete 32 digits given long (>128K) input context.

## Failure to ignore distractors

[p. 7] Figure 2 (middle-left) shows that increasing the number of distracting needles steadily lowers performance, with Yi dropping by ~40 points at 256K in the extreme version, where the context is full of irrelevant needles (#K=FULL). Error analysis reveals that Yi fails to effectively ignore the hard distractors given long input context, thus incorrectly retrieving values associated with the distractor keys. In the extreme version, Yi often returns values from the vicinity of the target, suggesting coarse match of the range but the lack of precision to locate the key when the target is in-distribution of the noises.

## Return incomplete information

[p. 7-8] Consistent with previous works (Liu et al., 2024a; Reid et al., 2024), the authors notice significant degradation in performance when the model needs to retrieve multiple items from a long input. For instance, increasing the number of queries from 1 to 8 drops the performance by ~15 points (Figure 2 right). When the model needs to retrieve multiple values associated with the same key (Figure 2 middle-right), Yi often outputs duplicated answers without returning the complete set of values, implying uneven associations between the key and each of its values.

## Tendency to copy from context

[p. 8] Yi has a strong tendency to copy from context verbatim when scaling the input length. This tendency is most notable in *variable tracking* (VT) and *common words extraction* (CWE) where one in-context demonstration is included at the beginning of the sequence. Over 80% of Yi's output in the CWE task at 128K is simply a string copied from the one-shot example, whereas the copying is nonexistent for short sequences. This copying behavior is also present in the LWM model and LongAlpaca, however it is less prevalent in other models, such as Mixtral. This finding further reinforces the need to test behaviors other than retrieval given long input context.

Footnote 7 [p. 8]: The authors also experimented with removing the one-shot example. The model will simply copy the string of the beginning of the input, likely due to the attention sinks (Xiao et al., 2024b).

## Unreliable tracking within context

[p. 8] For the *variable tracking* task, both adding more chains and more hops contribute to large degradation in Yi's performance. Yi consistently degrades in the more-hops setting as context size increases (Figure 3 left), whereas the degradation in the more-chains setting is most significant for lengths greater than 128K (Figure 3 middle-left). Besides the copying issue, Yi makes errors due to incorrectly returning empty strings or variables from other chains, implying a lack of ability to reliably trace the same entity within long context. These errors are also frequently observed in models that do not exhibit the copying behavior.

## Failure to accurately aggregate

[p. 9] Two common failure modes in aggregation tasks are observed: incorrect use of parametric knowledge and inaccurate aggregation. Models that do not exhibit the copying issue in the CWE task sometimes ignore the contextual information and instead use parametric knowledge to answer the query, especially at large context sizes. For instance, Mistral (7b-instruct-v0.2) returns high frequency words, such as "the", "an", "a", as output without counting the words in context. For the FWE task which demonstrates less the copying issue, Yi fails to correctly output the top frequent words as the authors decrease the *a* in Zeta distribution (Figure 3 middle-right). Decreasing *a* leads to smaller difference in frequency among words, increasing the difficulty to distinguish the top-frequent words.

## Frequent hallucination in long-context QA

[p. 9] For the QA tasks, Yi's performance approaches its no-context baseline as the authors extend the context with distracting paragraphs (Figure 3 right). The degradation stems primarily from hallucination and reduced reliance on contextual information. At large context sizes, model predictions sometimes are irrelevant to the question and can coincide with the answers of its no-context baseline. The overall worse performance in QA tasks confirms that the fuzzy matching between a query and a relevant paragraph in long context is a more challenging setting than the simplistic NIAH tests, where keys can be exactly located in context.

## Figures

**Figure 2** (p. 8): "Performance of Yi-34B in the needle-in-a-haystack (NIAH) tasks. By default, we use word-number as the key-value pair and Paul Graham essays as the haystack. Yi is not robust to the change of needle types and degrades with the increasing amount of distractors. (W: words; N: numbers; U: UUIDs; Full: entire haystack)."

The figure contains four subplots, all with x-axis "Sequence Length" (4K to 256K) and y-axis "Accuracy" (30-100):

- **Yi34B - Single NIAH (left):** Lines for Passkey retrieval, Vanilla NIAH, K=W V=U (key=words, value=UUIDs), K=W V=W (key=words, value=words), K=U V=U (key=UUIDs, value=UUIDs). Passkey retrieval stays near 100; vanilla NIAH stays near 100; K=W V=W stays near 90-100; K=W V=U degrades from ~90 to ~70 by 256K; K=U V=U degrades most, from ~80 to ~40 by 256K.
- **Yi34B - MK-NIAH (middle-left):** Lines for #K=1, #K=4, #K=8, #K=FULL, #K=FULL K=1 V=U. #K=1 stays near 100; #K=4 and #K=8 degrade moderately; #K=FULL drops from ~80 to ~50 by 256K; #K=FULL K=1 V=U drops most severely.
- **Yi34B - MV-NIAH (middle-right):** Lines for #V=1, #V=2, #V=4, #V=8. #V=1 stays near 100; performance degrades with more values; #V=8 drops from ~80 to ~40 by 256K.
- **Yi34B - MQ-NIAH (right):** Lines for #Q=1, #Q=2, #Q=4, #Q=8. #Q=1 stays near 100; performance degrades with more queries; #Q=8 drops from ~80 to ~60 by 256K.

**Figure 3** (p. 8): "Performance of Yi-34B in variable tracking (VT), frequent words extraction (FWE), and QA tasks across different task complexities. Yi shows large degradation and distinct trends with scaled context size in these non-retrieval tasks, demonstrating the need to evaluate behavior beyond retrieval from context."

The figure contains four subplots, all with x-axis "Sequence Length" (4K to 256K) and y-axis "Accuracy":

- **Yi34B - VT (left):** Lines for chain=1 hop=4, chain=1 hop=6, chain=1 hop=10. All degrade with sequence length. chain=1 hop=10 drops most severely, from ~70 to ~30 by 256K.
- **Yi34B - VT (middle-left):** Lines for chain=2 hop=2, chain=4 hop=2, chain=8 hop=2. chain=2 hop=2 stays relatively stable until 128K then drops; chain=4 and chain=8 degrade more, especially beyond 128K.
- **Yi34B - FWE (middle-right):** Lines for a=3.5, a=1.5, a=1.3, a=1.2. a=3.5 performs best (~80-90, degrading to ~50 by 256K); lower values of *a* perform worse, with a=1.2 dropping to ~30 by 256K.
- **Yi34B - QA (right):** Lines for SQuAD, HotpotQA, SQuAD w/o context, HotpotQA w/o context. With context, both start at ~80-100 at 4K and degrade; SQuAD with context drops to ~25 by 256K; performance approaches no-context baselines (~25 for SQuAD, ~0 for HotpotQA) at long context.
