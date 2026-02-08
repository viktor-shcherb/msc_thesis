# 3 Experiments [p. 4-6]

[p. 4] In this section, the authors attempt to determine what information in transformer LM contexts is usable by measuring ablated information (Eq. (9)). Sections 3.1 and 3.2 describe the main results, with Section 3.1 focused on ordering and Section 3.2 focused on lexical information. Section 3.3 compares these results to ablations applied at evaluation time. Section 3.4 explores whether contexts can be further manipulated to improve model predictions.

## Model, data and training details

[p. 4] For all experiments, the LM uses the **GPT-2 model architecture** (Radford et al., 2019) in the implementation of Wolf et al. (2020) with default hyperparameters. All models are trained from scratch on the **WikiText-103 dataset** (Merity et al., 2016), an English language modeling benchmark. Aside from ablations, no preprocessing is applied. A special separator token is inserted between ablated and unablated context. The training set contains **103,221,021 words**, while the evaluation set contains **217,646 words**.

[p. 4] Because of the large number of experiments in this paper, all training and evaluation use Eq. (10).

**Training setup:** A **no information** model is trained to minimize L(theta, 0 ~ 512) and a **full information** model to minimize L(theta, 512 ~ 1024). For each context ablation f, a model is trained to minimize L(theta, f, 512 : 0 ~ 512). Each ablation has access to more information than the no information model (because it conditions on extra tokens) and less information than the full information model (because an ablation has been applied to those tokens).

The LM operates on BPE-derived subword tokens for consistency with the way GPT-2 is typically used, but all ablations are defined at the word level, meaning, e.g., that words are shuffled rather than tokens.

**Evaluation conditions:** The authors stratify evaluation of the ablated information into two conditions:
- A **mid-range** condition in which likelihoods in Eq. (9) are of the form L(., f, 512 : 0 ~ 256)
- A **long-range** condition with likelihoods L(., f, 512 : 256 ~ 512)

> "We call the former 'mid-range' rather than 'short-range' because most tokens are still predicted with significant unablated context; our experiments do not characterize sentence-internal modeling of syntactic well-formedness." [p. 4]

Results are shown in Figure 2 and discussed below.

## A note on evaluation

[p. 4] As in past work on evaluating language models (Brown et al., 1992), the evaluation of relative predictive information ultimately bottoms out in a conditional entropy (log-perplexity). Recent work has shown that other metrics, such as diversity of outputs, are important for evaluating the quality of LMs as models for language generation (Hashimoto et al., 2019; Caccia et al., 2020). Generation also depends on a number of other factors, such as choice of decoding procedure (Caglayan et al., 2020). The authors focus on LMs as predictive models, measuring their ability to place an accurate distribution over future words and sentences, rather than their ability to generate useful or coherent text (see Appendix C). They emphasize that these results apply to language models specifically, and not transformers applied to NLP tasks in general -- the same analysis might give very different conclusions if applied to, e.g., question answering or summarization.

## 3.1 Does order matter? [p. 4-6]

[p. 4] This section examines the effects of different augmentations to the order within long-range context.

### Overall word order

**shuffle all:** f shuffles words uniformly at random, forcing the model to treat ablated context as a bag of words.

**shuf. trigrams globally:** the context is divided into non-overlapping trigrams, the order of which is then permuted uniformly at random.

[p. 4-5] Key results:
- Shuffling all words removes **41%** of usable information in the mid-range condition and **84%** in the long-range condition: *ordering information is important even very far from the target*.
- Shuffling all trigrams removes **31%** in the mid-range condition and **50%** in the long-range condition: *local co-occurrence statistics carry a significant amount of usable information*.

### Word order within sentences

Three procedures for shuffling within sentences: [p. 5]
1. **shuf. within sent.** -- a uniform random permutation of all the words in the sentence
2. **shuf. within trigrams** -- a uniform random permutation of the words within each non-overlapping trigram in the sentence
3. **shuf. trigrams within sent.** -- a uniform random permutation of the order of the trigrams within the sentence

Procedures (1) and (2) were also recently explored by Pham et al. (2020) in models for entailment, and more complex shuffling procedures have been explored in neuroscience contexts (Mollica et al., 2020). Procedures (2) and (3) are chosen because they preserve local co-occurrence statistics ((3) more than (2)), while (2) also preserves the general linear information flow of the sentence.

[p. 5] The shuf. within trigrams (**14%** and **41%**) and the shuf. trigrams within sent. (**16%** and **35%**) ablations both remove relatively little usable information in both mid- and long-range conditions.

> "*Usable information is decreased only slightly by ablations that preserve local co-occurrence statistics and/or linear information flow.*" [p. 5]

This includes transformations like *man bites dog* -> *dog bites man* with significant effects on semantics. In the long-range condition, uniform shuffling within sentences produces a larger effect, removing **55%** of usable information.

### Sentence order

**shuf. sent.:** *sentences* are shuffled within the context while their internal word order is unchanged. [p. 5]

- Mid-range condition: removes **17%** of usable information, comparable to the trigram shuffling experiments above.
- Long-range condition: has an even smaller effect (**14%**).

> Together with the previous experiment these results suggest that "*prediction accuracy depends on information about local word co-occurrence, but not fine-grained word order or global position.*" [p. 5]

### Order of entire sections

**replace w/ old:** The ablation replaces the entire input with the 512 tokens that immediately precede it in the source document (which in general will be topically similar). [p. 5]

This transformation removes significant information in both mid- and long-range conditions (**55%** and **69%**).

> "*Long-range context is not simply a source of topic information: earlier text on the same theme is in some cases nearly as uninformative as no text at all.*" [p. 5-6]

**Figure 2** (p. 5): "Effect of **word order** on usable information. Bar labels show 'change in ablated likelihood (ablated information)'. The x axis shows ablated likelihood. Error bars represent 95% confidence intervals. Word-order changes that preserve local ordering remove only a small amount of information, while shuffling or replacement with thematically similar text remove more."

Figure 2 has two sub-figures:

**(a) Mid-range condition (first 256 tokens after context):**
| Ablation | Ablated likelihood (bits) | Change (ablated information) |
|---|---|---|
| full information | 4.19 (0%) | -- |
| shuf. within trigrams | ~4.23 | +0.04 (14%) |
| shuf. trigrams within sent. | ~4.23 | +0.04 (16%) |
| sent. shuf. | ~4.23 | +0.04 (17%) |
| shuf. within sent. | ~4.25 | +0.07 (26%) |
| shuf. trigrams globally | ~4.27 | +0.08 (31%) |
| shuffle all | ~4.29 | +0.10 (41%) |
| replace w/ old | ~4.33 | +0.14 (55%) |
| no information | 4.45 (100%) | -- |

**(b) Long-range condition (tokens 256-512 after ablation):**
| Ablation | Ablated likelihood (bits) | Change (ablated information) |
|---|---|---|
| full information | 4.17 (0%) | -- |
| sent. shuf. | ~4.18 | +0.01 (14%) |
| shuf. trigrams within sent. | ~4.19 | +0.02 (35%) |
| shuf. within trigrams | ~4.19 | +0.02 (41%) |
| shuf. within sent. | ~4.20 | +0.03 (55%) |
| shuf. trigrams globally | ~4.20 | +0.02 (50%) |
| replace w/ old | ~4.20 | +0.03 (69%) |
| shuffle all | ~4.21 | +0.04 (84%) |
| no information | 4.22 (100%) | -- |

Note: The bar chart labels in Figure 2(b) are difficult to read precisely for some rows because the differences are very small (the entire range spans only ~0.05 bits). The percentages in parentheses are the ablated information values.

## 3.2 Do all words matter? [p. 6]

[p. 6] These experiments focus on lexical rather than structural information, using ablations that delete selected words from the context. Training and evaluation setups are exactly as in Section 3.1. Unlike the previous section, ablations will generally cause the number of tokens in a given context to decrease; ablations also insert padding tokens to the *beginning* of the context window to preserve the original number of tokens. Results are shown in Fig. 3.

### Parts of speech

[p. 6] The authors retain only words whose part of speech tag is in a given set, using the spaCy model (Honnibal et al., 2020) for part-of-speech tagging. Five sets are examined:
1. **nouns only** (N)
2. **nouns and verbs** (N & VB)
3. **nouns, verbs, and adjectives** (N & VB & ADJ)
4. **content words** -- nouns, verbs, adjectives, and adverbs (cont. words / N & VB & ADJ & ADV)
5. **function words** -- all words *except* nouns, verbs, adjectives, and adverbs (func. words)

Example ablations shown for the Pierre Vinken sentence:
- **N:** *Pierre Vinken years board director Nov. Mr. Vinken chairman Elsevier N.V. publishing group*
- **N & VB:** *Pierre Vinken years will join board director Nov. Mr. Vinken chairman Elsevier N.V. publishing group*
- **N & VB & ADJ:** *Pierre Vinken years old will join board nonexecutive director Nov. Mr. Vinken chairman Elsevier N.V. Dutch publishing group*
- **cont. words (N & VB & ADJ & ADV):** *Pierre Vinken years old will join board nonexecutive director Nov. Mr. Vinken chairman Elsevier N.V. Dutch publishing group*
- **func. words:** *, 61 , the as a 29 . is of , the .*

[p. 6] **Mid-range condition results:**
- Deleting all words but nouns removes only **20%** of usable information.
- Deleting all but nouns and verbs removes only **13%**.

> "*Most usable information, even in mid-range context, appears to be captured by nouns and verbs.*" [p. 6]

Retaining only function words causes a considerably greater loss of information.

[p. 6] **Long-range condition results** are even more striking:

> "*retaining only content words improves predictions over the 'full information' experiment.*" [p. 6]

Like Shannon information, V-information is defined to be non-negative (Xu et al., 2020), and the result in Fig. 3 is a consequence of the finite-sample approximation based on held-out likelihood. The effect is robust across multiple training runs from random initializations. There is a significant gap between the training and validation perplexity of the model (roughly 11%), and the authors hypothesize that the ablation preserves semantic content while reducing the original model's ability to overfit.

### Named entities

[p. 6] Example: **named entities** ablation retains: *Pierre Vinken 61 years old Nov. 29 Vinken Elsevier N.V. Dutch*

**Figure 3** (p. 6): "Effect of **word identity** on usable information. Labels are as in Fig. 2. Several ablations, including deletion of all words except nouns, preserve most usable information in the mid-range condition, and *improve* model accuracy in the in the long range."

Figure 3 has two sub-figures:

**(a) Mid-range condition (first 256 tokens after context):**
| Ablation | Ablated likelihood (bits) | Change (ablated information) |
|---|---|---|
| full information | 4.19 (0%) | -- |
| cont. words | ~4.20 | +0.02 (9%) |
| N&VB&ADJ | ~4.21 | +0.03 (11%) |
| N&VB | ~4.21 | +0.03 (13%) |
| N | ~4.24 | +0.05 (20%) |
| common | ~4.29 | +0.10 (38%) |
| named entities | ~4.29 | +0.10 (39%) |
| rare | ~4.34 | +0.15 (58%) |
| func. words | ~4.37 | +0.18 (69%) |
| no information | 4.45 (100%) | -- |

**(b) Long-range condition (tokens 256-512 after context):**
| Ablation | Ablated likelihood (bits) | Change (ablated information) |
|---|---|---|
| cont. words | ~4.17 | +-0.01 (-31%) |
| N&VB&ADJ | ~4.17 | +-0.01 (-25%) |
| N&VB | ~4.17 | +-0.01 (-22%) |
| N | ~4.17 | +0.00 (-9%) |
| full information | 4.17 (0%) | -- |
| named entities | ~4.18 | +0.01 (31%) |
| common | ~4.18 | +0.02 (33%) |
| rare | ~4.19 | +0.03 (73%) |
| func. words | ~4.20 | +0.04 (89%) |
| no information | 4.22 (100%) | -- |

---
[p. 6-7 continued]

[p. 6-7] The authors hypothesize that long-range contexts are useful because they provide a reservoir of named entities likely to be referred to again. The named entities ablation retains only spans tagged as named entities or quantities by spaCy. While significantly worse than the noun ablation discussed above, retaining only entities removes only about a third of usable information in both conditions (39% and 31%).

### Word frequency

[p. 7] Another natural question is whether rare words or frequent words are more important: information about frequent context words might help models estimate fine-grained document-level frequencies of those words (which account for most of the terms in Eq. (7)); rare words are likely to be more informative about the content of the document itself.

The vocabulary is partitioned into a set of **rare words**, corresponding to the least frequent ~98% of word types and 20% of word tokens, and **frequent words**, the most frequent ~2% of types and 80% of tokens.

Example ablations:
- **common:** *Pierre years old join board director . Mr. chairman Dutch publishing group .*
- **rare:** *Vinken nonexecutive Nov. Vinken Elsevier N.V.*

Both ablations remove a significant amount of information relative to the POS-based ablations above, but retaining only frequent words improves perplexity relative to rare words in both the mid- and long-range conditions.

Appendix B presents versions of these experiments trained and evaluated on even longer contexts. Conclusions are largely the same as above.

## 3.3 Evaluating on augmented data [p. 7-8]

[p. 7] The authors motivated the use of V-information in Section 2 by arguing that it more clearly distinguishes between prediction errors attributable to *loss of information* and prediction errors attributable to *malformed and out-of-distribution* model inputs. To put results in context, they repeat several of the previous experiments in the evaluation paradigm of Khandelwal et al. (2018), which is designed to measure test-time sensitivity rather than usable information.

[p. 7] A new model is trained to minimize L(theta, 512 ~ 1024) while randomly truncating the first 512 context tokens and replacing them with padding tokens (to ensure that the model has seen padding tokens at training time). This model is then evaluated on the set of ablations shown in Section 3.1 and Section 3.2. For the full information model in Fig. 4, ordered context windows are evaluated with no padding tokens; for the no information model, context windows in which the first 512 tokens are all padding tokens.

[p. 7-8] **Mid-range condition:** The least destructive ablations are shuffling within trigrams and shuffling the order of trigrams within sentences: models appear to be reasonably robust to this kind of data transformation without specific training on it. Importantly, lexical ablation experiments have a large impact in this evaluation, underlining the extent to which the two experimental paradigms characterize different aspects of model behavior. Figure 5 in Appendix A shows a side-by-side comparison of these experiments and the ones in Sections 3.1-3.2.

**Figure 4** (p. 7): "Loss of information resulting from ablations at *evaluation time only*. x-axis and labels show ablated negative log-likelihoods. Some locality-preserving ablations (high PMI, shuf. sent.) have a small effect, but most affect likelihood significantly (including lexical ablations that do not remove usable information)."

Figure 4 has two sub-figures:

**(a) Mid-range condition (first 256 tokens after ablation):**
| Ablation | Ablated likelihood (bits) | Change |
|---|---|---|
| full information | ~4.18 | -- |
| shuf. within trigrams | ~4.24 | +0.06 |
| shuf. trigrams within sent. | ~4.26 | +0.08 |
| sent. shuf. | ~4.28 | +0.10 |
| shuf. within sent. | ~4.32 | +0.14 |
| cont. words | ~4.34 | +0.16 |
| N&VB&ADJ | ~4.34 | +0.16 |
| shuf. trigrams globally | ~4.34 | +0.16 |
| N&VB | ~4.36 | +0.16 |
| N | ~4.36 | +0.18 |
| common | ~4.38 | +0.20 |
| named entities | ~4.38 | +0.20 |
| shuffle all | ~4.40 | +0.22 |
| rare | ~4.42 | +0.24 |
| replace w/ old | ~4.43 | +0.25 |
| no information | ~4.48 | -- |
| func. words | ~4.54 | +0.36 |

**(b) Long-range condition (tokens 256-512 after ablation):**
| Ablation | Ablated likelihood (bits) | Change |
|---|---|---|
| full information | ~4.15 | -- |
| sent. shuf. | ~4.15 | +0.00 |
| shuf. within sent. | ~4.17 | +0.02 |
| shuf. within trigrams | ~4.18 | +0.03 |
| shuf. trigrams within sent. | ~4.18 | +0.03 |
| shuf. trigrams globally | ~4.18 | +0.03 |
| replace w/ old | ~4.18 | +0.03 |
| N&VB&ADJ | ~4.18 | +0.03 |
| cont. words | ~4.18 | +0.03 |
| N&VB | ~4.18 | +0.03 |
| N | ~4.18 | +0.03 |
| named entities | ~4.19 | +0.04 |
| rare | ~4.19 | +0.04 |
| shuffle all | ~4.19 | +0.04 |
| common | ~4.20 | +0.05 |
| no information | ~4.20 | -- |
| func. words | ~4.22 | +0.07 |

## 3.4 Making better language models? [p. 8]

[p. 8] The lexical ablation experiments in Section 3.2 indicated that model accuracy could be *improved* by selective deletion of context words. Can this effect be exploited to further improve models? As a simple experiment, the authors attempted to *replace* all padding tokens in the *nouns+verbs* ablation of Section 3.2 with nouns and verbs from further back in the context -- effectively providing the model with an even longer-range view of an informative context representation.

[p. 8] This experiment slightly increased usable information in the mid-range condition (0.2%), but *decreased* it in the long-range condition (0.6%).

> "*Longer contexts, even of a kind previously found to be informative, did not provide additional usable information.*" [p. 8]

These results are consistent with the earlier hypothesis that the previously observed effect resulted from a reduction in overfitting -- if removing information increased performance by reducing overfitting, then it is reasonable that adding information back results in more overfitting.
