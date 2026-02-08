# 3.3 Translation [p. 14-16]

[p. 14] For GPT-2 a filter was used on a multilingual collection of documents to produce an English only dataset due to capacity concerns. Even with this filtering GPT-2 showed some evidence of multilingual capability and performed non-trivially when translating between French and English despite only training on 10 megabytes of remaining French text. Since the capacity is increased by over two orders of magnitude from GPT-2 to GPT-3, the scope of the training dataset is also expanded to include more representation of other languages, though this remains an area for further improvement. As discussed in 2.2 the majority of the data is derived from raw Common Crawl with only quality-based filtering. Although GPT-3's training data is still primarily English (93% by word count), it also includes 7% of text in other languages. These languages are documented in the supplemental material. To better understand translation capability, the analysis is expanded to include two additional commonly studied languages, German and Romanian.

[p. 14] Existing unsupervised machine translation approaches often combine pretraining on a pair of monolingual datasets with back-translation [SHB15] to bridge the two languages in a controlled way. By contrast, GPT-3 learns from a blend of training data that mixes many languages together in a natural way, combining them on a word, sentence, and document level. GPT-3 also uses a single training objective which is not customized or designed for any task in particular. However, the one / few-shot settings aren't strictly comparable to prior unsupervised work since they make use of a small amount of paired examples (1 or 64). This corresponds to up to a page or two of in-context training data.

## Translation results

[p. 14-15] Results are shown in Table 3.4. Zero-shot GPT-3, which only receives a natural language description of the task, still underperforms recent unsupervised NMT results. However, providing only a single example demonstration for [p. 16] each translation task improves performance by over 7 BLEU and nears competitive performance with prior work. GPT-3 in the full few-shot setting further improves another 4 BLEU resulting in similar average performance to prior unsupervised NMT work.

[p. 16] GPT-3 has a noticeable skew in its performance depending on language direction. For the three input languages studied, GPT-3 significantly outperforms prior unsupervised NMT work when translating into English but underperforms when translating in the other direction. Performance on En-Ro is a noticeable outlier at over 10 BLEU worse than prior unsupervised NMT work. This could be a weakness due to reusing the byte-level BPE tokenizer of GPT-2 which was developed for an almost entirely English training dataset.

[p. 16] For both Fr-En and De-En, few shot GPT-3 outperforms the best supervised result we could find but due to our unfamiliarity with the literature and the appearance that these are un-competitive benchmarks we do not suspect those results represent true state of the art. For Ro-En, few shot GPT-3 performs within 0.5 BLEU of the overall SOTA which is achieved by a combination of unsupervised pretraining, supervised finetuning on 608K labeled examples, and backtranslation [LHCG19b].

[p. 16] Finally, across all language pairs and across all three settings (zero-, one-, and few-shot), there is a smooth trend of improvement with model capacity. This is shown in Figure 3.4 in the case of few-shot results, and scaling for all three settings is shown in Appendix H.

### Table 3.4: Few-shot GPT-3 outperforms previous unsupervised NMT work by 5 BLEU when translating into English reflecting its strength as an English LM. BLEU scores on the WMT'14 Fr<->En, WMT'16 De<->En, and WMT'16 Ro<->En datasets as measured by `multi-bleu.perl` with XLM's tokenization in order to compare most closely with prior unsupervised NMT work. SacreBLEU^f [Pos18] results reported in Appendix H. Underline indicates an unsupervised or few-shot SOTA, bold indicates supervised SOTA with relative confidence. [p. 15]

| Setting | En->Fr | Fr->En | En->De | De->En | En->Ro | Ro->En |
|---|---|---|---|---|---|---|
| SOTA (Supervised) | **45.6**^a | **35.0**^b | **41.2**^c | **40.2**^d | **38.5**^e | **39.9**^e |
| XLM [LC19] | 33.4 | 33.3 | 26.4 | 34.3 | 33.3 | 31.8 |
| MASS [STQ+19] | <u>37.5</u> | 34.9 | 28.3 | 35.2 | <u>35.2</u> | 33.1 |
| mBART [LGG+20] | - | - | <u>29.8</u> | 34.0 | 35.0 | 30.5 |
| GPT-3 Zero-Shot | 25.2 | 21.2 | 24.6 | 27.2 | 14.1 | 19.9 |
| GPT-3 One-Shot | 28.3 | 33.7 | 26.2 | 30.4 | 20.6 | 38.6 |
| GPT-3 Few-Shot | 32.6 | <u>39.2</u> | 29.7 | <u>40.6</u> | 21.0 | <u>39.5</u> |

^a [EOAG18] ^b [DHKH14] ^c [WXH+18] ^d [oR16] ^e [LGG+20] ^f [SacreBLEU signature: BLEU+case.mixed+numrefs.1+smooth.exp+tok.intl+version.1.2.20]

## Figures

**Figure 3.4** (p. 15): "Few-shot translation performance on 6 language pairs as model capacity increases. There is a consistent trend of improvement across all datasets as the model scales, and as well as tendency for translation into English to be stronger than translation from English."
- X-axis: Parameters in LM (Billions), from 0.1B to 175B. Y-axis: BLEU, from 0 to 40.
- Six lines for language pairs: French->English (blue solid, highest at ~39), English->French (blue dashed, ~33), German->English (green solid, ~40), English->German (green dashed, ~30), Romanian->English (red solid, ~39), English->Romanian (red dashed, ~21).
- All lines show consistent improvement with model scale.
- Translation into English (solid lines) consistently outperforms translation from English (dashed lines) across all language pairs.
- The strongest performance at 175B: De->En (~40.6), Fr->En (~39.2), Ro->En (~39.5). The weakest: En->Ro (~21.0).
