# Appendix I: Tokenizer Selection [p. 92–93]

[p. 92] This section details the evaluation metrics used in the tokenizer selection process. Four metrics are considered: **fertility rate**, **compression ratio**, **vocabulary utilization**, and the **Gini coefficient**. These metrics are adapted from Foroutan et al. (2025a).

Let *T* be a tokenizer with tokenization function *tau*, applied to a parallel corpus *D*. For a sequence **b** in *D*, let |**b**|_u denote its length with respect to a given *normalization unit* u (e.g., characters, words, lines, or bytes).

## Compression Rate

[p. 92] The *compression rate* measures how efficiently a tokenizer represents text by quantifying the average number of tokens produced per normalization unit across a corpus. Using lines (documents) as units, it is defined as:

$$CR(D; \tau) \stackrel{\text{def}}{=} \frac{1}{|D|} \sum_{\mathbf{b} \in D} \frac{|\mathbf{b}|_u}{|\tau(\mathbf{b})|} \qquad (1)$$

Higher compression rates are generally desirable, as they imply fewer tokens must be processed by an autoregressive LM per unit of raw text.

## Fertility

[p. 92–93] The *fertility* of a tokenizer captures the average number of tokens produced per unit (commonly a word). It indicates how much a tokenizer fragments input text, with higher fertility implying longer token sequences. Using words as the normalization unit (as determined by the HuggingFace Whitespace Pretokenizer), fertility is defined as:

$$\text{Fertility}(T) = \frac{\sum_{\mathbf{b} \in D} |\tau(\mathbf{b})|}{\sum_{\mathbf{b} \in D} |\mathbf{b}|_u} \qquad (2)$$

This metric provides insight into both computational efficiency and expected sequence lengths for downstream tasks.

## Vocabulary Utilization

[p. 93] *Vocabulary utilization* measures how much of a tokenizer's vocabulary is actively used when encoding a corpus:

$$\text{VocabUtil}(T) = \frac{|\{v : v \in \tau(\mathbf{b}), \mathbf{b} \in D\}|}{|V|} \qquad (3)$$

The numerator counts distinct tokens observed across the entire corpus. High vocabulary utilization suggests efficient use of the learned vocabulary. Conversely, low utilization in a specific language may indicate bias, as only a small portion of the vocabulary is relevant for that language.

## Tokenizer Fairness Gini Coefficient

[p. 93] The Gini coefficient (commonly used to measure inequality in economics) is adapted to quantify fairness across languages (Meister, 2025). Let *L* = *l*_1, *l*_2, ..., *l*_n be the set of languages, and let *c*_1 <= *c*_2 <= ... <= *c*_n denote their tokenization costs under *T*. Here, cost is defined as the average number of tokens required to encode one normalization unit (e.g., a byte, word, or line);^57 for parallel corpora, cost per line is often used to control for differences in character byte lengths across scripts. The Gini coefficient is given by:

$$\text{Gini}(T) = \frac{1}{n} \left( n + 1 - 2 \frac{\sum_{i=1}^{n} (n + 1 - i) c_i}{\sum_{i=1}^{n} c_i} \right) \qquad (4)$$

Values range from 0 (perfect equality) to 1 (maximum inequality). Lower values indicate more equitable compression across languages, while higher values reveal systematic bias that favors certain languages.

This evaluation covers a wide range of languages, including Afrikaans, Albanian, Arabic, North Azerbaijani, Basque, Belarusian, Bengali, Bulgarian, Catalan, Chinese, Czech, Danish, Dutch, English, Estonian, Finnish, French, Galician, Georgian, German, Greek, Gujarati, Hebrew, Hindi, Hungarian, Indonesian, Italian, Japanese, Korean, Latvian, Malay, Malayalam, Marathi, Macedonian, Norwegian Bokmal, Persian (Farsi), Polish, Portuguese, Romanian, Russian, Slovak, Southern Sotho, Spanish, Swahili, Swedish, Tamil, Tajik, Telugu, Thai, Turkish, Ukrainian, Urdu, Vietnamese, Welsh, and Yoruba.

^57 This is equivalent to fertility, or the inverse of the compression rate.
