# 4 Representational Collapse [p. 6]

We start our theoretical analysis by showcasing a type of loss of information which we call representational collapse. More precisely, we show that under certain conditions, we can find distinct sequences such that their final representations of the last token at the last layer become arbitrarily close as the sequence length increases. As Transformer models operate over finite machine precision, this points to a fundamental representational incapacity of Transformers to distinguish certain prompts if the sequence is long enough.

The key intuition is that if two sequences are similar everywhere except at the last token, as the sequences get larger, their final representations will become closer and closer until they
 reach a critical point which is below floating point precision. In other words, solving certain tasks would require infinite floating point precision. We will later show how this phenomenon is not only theoretical, but also occurs in practice on sequences of reasonable length. In the Appendix (Section 4), we relate representational collapse to the L1 distance – or total variation – between the softmax distributions of the two sequences. We start by presenting a result that shows that the L1 difference tends to 0 as the sequence length grows, under some assumption on the sequences. We point to the Appendix (Lemma B.2) for the complete statement.

---
[p. 6–8 continued]

## Lemma 4.1 (Informal)

Consider two sequences x, x* ∈ R^n such that lim_{n→∞} |x_n - x*_n| = 0. Then, the L1 difference of their softmax tends to 0.

We now show, using Lemma 4.1, that we can find distinct sequences that will have arbitrarily close final representations. In particular, as language models often operate in low floating regimes, i.e. bf16, this can practically become catastrophic. The result is summarised in Theorem 4.2, which describes what we call representational collapse in this work. The complete statement is reported in the Appendix (Theorem B.3).

## Theorem 4.2 (Representational Collapse – informal)

Let v^(0) ∈ R^{n×d} be a sequence and v*^(0) ∈ R^{(n+1)×d} be another sequence equal to v^(0) with the last token of v^(0) repeated. Assume that the positional encoding information decays to 0 with the distance. Then, their representations become arbitrarily close as n increases.

Theorem 4.2 shows that it becomes increasingly challenging for a Transformer to distinguish two sequences that only differ via a repeated last token. We note that the repetition of the last token is a technical consideration to show this direct representational collapse. As we will later show in Section 5.1, it is particularly problematic in general to depend on the last token due to a type of topological 'squashing' present in decoder-only Transformers.

## Measuring representational collapse

We report experiments showcasing representational collapse by measuring the internal representations of Gemma 7B [27]. For two sequences v^(0) and v*^(0) we report their difference in representation at the last layer ||v^(L) - v*^(L)||_∞ averaged out over each head, alongside the minimum and maximum over each head.

**Figure 5** (p. 8): "Representational collapse for counting (a, b) and copying (c, d) tasks."

Description: Four line plots showing L∞ distance vs sequence length
- (a) "How many ones are in the following sequences?" Followed by a sequence of ones
- (b) "How many ones are in the following sequences?" Followed by sampled digits
- (c) "Can you copy the following number?" Followed by a sequence of ones
- (d) "Can you copy the following number?" Followed by a sequence of ones with commas
- Shows collapse occuring on (a) prompting the model to count the number of ones in a sequence of ones, with one having an additional one, and (b) prompting the model to count the number of ones for a sequences with digits sampled uniformly ending with either a single one or two ones
- The repeated digits seem to make the collapse occur much sooner with a sequence length of around 50 being near machine precision, while varying the digits seems to delay such a collapse, but a downward trend is maintained with respect to the sequence length

## Quantisation and Tokenisation

A common technique used to speedup the inference of an LLM is that of quantisation, a process that constructs an approximate version of an LLM that operates over lower precision datatypes. This helps drastically improve the inference speed of LLMs as modern accelerators produce significantly more FLOPs over lower precision datatypes. Of course quantisation usually comes at a cost. Our theoretical analysis points towards a potentially catastrophic loss in representation due to quantisation. In particular, a lower machine precision will mean that the convergence of representations in Theorem 4.2 will occur much sooner, and consequently the LLM will not be able to distinguish even shorter sequences.

In practice, the direct application of theoretical results is made more complicated due to tokenisation. In particular, a sequence of repeated tokens '11111' for instance may not be necessarily tokenised into 5 distinct '1' tokens. In principle, this should help alleviate the direct collapse of the representations. Tokenisation in general makes it more of a challenge to study such phenomena as it adds an additional layer of complexity to the experimental analysis. In our experiments, we took tokenisation into consideration and attempted to mitigate its effects.

## A simple solution to representational collapse

An important consequence of Theorem 4.2 is that it is challenging for a Transformer to deal with a long sequence of repeated tokens. A practical solution is to this issue is to introduce additional tokens throughout the sequence to help keep the representations distant. We provide direct evidence of this in Figure 5 (c,d), where we prompt the model on a simple copying task of a long string of ones. While the representations collapse for the sequence of ones (c), adding commas every third digit (d) helps to keep the representations well-separated.
