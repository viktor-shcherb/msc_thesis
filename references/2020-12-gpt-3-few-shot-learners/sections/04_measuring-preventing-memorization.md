# 4. Measuring and Preventing Memorization Of Benchmarks [p. 29-33]

[p. 29] Since the training dataset is sourced from the internet, it is possible that the model was trained on some of the benchmark test sets. Accurately detecting test contamination from internet-scale datasets is a new area of research without established best practices. While it is common practice to train large models without investigating contamination, given the increasing scale of pretraining datasets, the authors believe this issue is becoming increasingly important to attend to.

[p. 29] This concern is not just hypothetical. One of the first papers to train a language model on Common Crawl data [TL18] detected and removed a training document which overlapped with one of their evaluation datasets. Other work such as GPT-2 [RWC+19] also conducted post-hoc overlap analysis. Their study was relatively encouraging, finding that although models did perform moderately better on data that overlapped between training and testing, this did not significantly impact reported results due to the small fraction of data which was contaminated (often only a few percent).

## GPT-3's contamination regime

[p. 31] GPT-3 operates in a somewhat different regime. On the one hand, the dataset and model size are about two orders of magnitude larger than those used for GPT-2, and include a large amount of Common Crawl, creating increased potential for contamination and memorization. On the other hand, precisely due to the large amount of data, even GPT-3 175B does not overfit its training set by a significant amount, measured relative to a held-out validation set with which it was deduplicated (Figure 4.1). Thus, the authors expect that contamination is likely to be frequent, but that its effects may not be as large as feared.

## Bug in contamination removal

[p. 31] The authors initially tried to address the issue of contamination by proactively searching for and attempting to remove any overlap between the training data and the development and test sets of all benchmarks studied in the paper. Unfortunately, a bug resulted in only partial removal of all detected overlaps from the training data. Due to the cost of training, it was not feasible to retrain the model. To address this, the remaining detected overlap impacts on results are investigated in detail.

## Clean benchmark methodology

[p. 31] For each benchmark, a "clean" version is produced which removes all potentially leaked examples, defined roughly as examples that have a 13-gram overlap with anything in the pretraining set (or that overlap with the whole example when it is shorter than 13-grams). The goal is to very conservatively flag anything that could potentially be contamination, so as to produce a clean subset that is free of contamination with high confidence. The exact procedure is detailed in Appendix C.

[p. 31] GPT-3 is then evaluated on these clean benchmarks, and scores are compared to the original score. If the score on the clean subset is similar to the score on the entire dataset, this suggests that contamination, even if present, does not have a significant effect on reported results. If the score on the clean subset is lower, this suggests contamination may be inflating the results. The results are summarized in Figure 4.2. Although potential contamination is often high (with a quarter of benchmarks scoring over 50%), in most cases performance changes only negligibly, and there is no evidence that contamination level and performance difference are correlated. The authors conclude that either their conservative method substantially overestimated contamination or that contamination has little effect on performance.

## Flagged benchmark groups

[p. 31] The few specific cases where either (1) the model performs significantly worse on the cleaned version, or (2) potential contamination is very high, which makes measuring the performance difference difficult, are reviewed in more detail. The analysis flagged six groups of benchmarks for further investigation: Word Scrambling, Reading Comprehension (QuAC, SQuAD2, DROP), PIQA, Winograd, language modeling tasks (Wikitext tasks, 1BW), and German to English translation.

## Figures

**Figure 4.1** (p. 31): "GPT-3 Training Curves. We measure model performance during training on a deduplicated validation split of our training distribution. Though there is some gap between training and validation performance, the gap grows only minimally with model size and training time, suggesting that most of the gap comes from a difference in difficulty rather than overfitting."
- Title: "GPT-3 Training Curves"
- X-axis: Tokens Elapsed (Billions), from 0 to 300. Y-axis (left): Cross-Entropy Loss (nats/token, smoothed), from ~1.50 to 3.50. Color scale (right): Model Parameters, from 10^8 to 10^11.
- Multiple pairs of training curves shown, one pair per model size. For each model size, there is a solid line (Validation Loss) and a dashed line (Train Loss).
- The curves descend from upper-left to lower-right, with larger models (warmer/yellow colors, up to ~10^11 parameters) achieving lower loss.
- The smallest models (~10^8, purple) converge around 3.0-3.25 nats/token. The largest model (~175B, yellow) converges around 1.70-1.75 nats/token.
- The gap between training and validation loss is relatively small and does not grow dramatically with model size, supporting the claim that GPT-3 175B does not significantly overfit.

**Figure 4.2** (p. 32): "Benchmark contamination analysis. We constructed cleaned versions of each of our benchmarks to check for potential contamination in our training set. The x-axis is a conservative lower bound for how much of the dataset is known with high confidence to be clean, and the y-axis shows the difference in performance when evaluating only on the verified clean subset. Performance on most benchmarks changed negligibly, but some were flagged for further review. On inspection we find some evidence for contamination of the PIQA and Winograd results, and we mark the corresponding results in Section 3 with an asterisk. We find no evidence that other benchmarks are affected."
- X-axis: Percentage of Data Clean in Dataset (0%–100%). Y-axis: Percent Change in Performance (Accuracy, F1 or BLEU), from -30% to +30%.
- Upper region labeled "eval on only clean data did better"; lower region labeled "eval on all data (including dirty) did better."
- Most benchmarks cluster around 0% change. Notable outliers: QuAC (~20% positive change at ~10% clean), DROP (~-20% at ~10% clean), SQuADv2 (~-5% at ~10% clean), Symbol Insertion (~5% at ~25% clean).
- PIQA (~-5% at ~70% clean), WMT16 en->de and de->en (~-8% at ~55–60% clean), Winograd (~0% at ~55% clean).
- Anagrams 1, Anagrams 2, and Reversed Words appear at ~75–100% clean with small or negative changes.
- The scatter plot shows no systematic correlation between contamination level and performance difference.

---
[p. 32–33 continued]

## Detailed analysis of flagged benchmarks

[p. 32] Since the overlap analysis is designed to be extremely conservative, the authors expect it to produce some false positives. Results for each group of flagged tasks:

- **Reading Comprehension:** The initial analysis flagged >90% of task examples from QuAC, SQuAD2, and DROP as potentially contaminated, so large that even measuring the differential on a clean subset was difficult. Upon manual inspection, for every overlap inspected, in all 3 datasets, the source text was present in the training data but the question/answer pairs were not, meaning the model gains only background information and cannot memorize the answer to a specific question.

- **German translation:** 25% of the examples in the WMT16 German-English test set were marked as potentially contaminated, with an associated total effect size of 1–2 BLEU. Upon inspection, none of the flagged examples contain paired sentences resembling NMT training data and collisions were monolingual matches mostly of snippets of events discussed in the news.

- **Reversed Words and Anagrams:** These tasks are of the form "alaok = koala". Due to the short length, 2-grams were used for filtering (ignoring punctuation). After inspecting the flagged overlaps, the overlaps were not typically instances of real reversals or unscramblings in the training set, but rather palindromes or trivial unscramblings, e.g. "kayak = kayak". The amount of overlap was small, but removing the trivial tasks leads to an increase in difficulty and thus a spurious signal. Related to this, the symbol insertion task shows high overlap but no effect on performance because that task involves removing non-letter characters from a word, and the overlap analysis itself ignores such characters, leading to many spurious matches.

- **PIQA:** The overlap analysis flagged 29% of examples as contaminated, and observed a 3 percentage point absolute decrease (4% relative decrease) in performance on the clean subset. Though the test dataset was released after the training set was created and its labels are hidden, some of the web pages used by the crowdsourced dataset creators are contained in the training set. A similar decrease was found in a 25x smaller model with much less capacity to memorize, leading the authors to suspect that the shift is likely statistical bias rather than memorization; examples which workers copied may simply be easier. The authors cannot rigorously prove this hypothesis, and therefore mark PIQA results with an asterisk to denote potential contamination.

- **Winograd:** The overlap analysis flagged 45% of examples, and found a 2.6% decrease in performance on the clean subset. Manual inspection of the overlapping data point showed that 132 Winograd schemas were in fact present in the training set, though presented in a different format than the task is presented to the model. Although the decrease in performance is small, Winograd results are marked in the main paper with an asterisk.

- **Language modeling:** The 4 Wikipedia language modeling benchmarks measured in GPT-2, plus the Children's Book Test dataset, were found to be almost entirely contained in the training data. Since a clean subset could not be reliably extracted, results are not reported on these datasets, even though the authors intended to when starting this work. Penn Tree Bank is noted as unaffected due to its age and therefore became the chief language modeling benchmark.

## High-contamination, near-zero impact datasets

[p. 33] Datasets where contamination was high but the impact on performance was close to zero were also inspected, simply to verify how much actual contamination existed. These appeared to often contain false positives. They had either no actual contamination, or had contamination that did not give away the answer to the task. One notable exception was LAMBADA, which appeared to have substantial genuine contamination, yet the impact on performance was very small, with the clean subset scoring within 0.5% of the full dataset. Also, strictly speaking, the fill-in-the-blank format precludes the simplest form of memorization. Nevertheless, since the authors made very large gains on LAMBADA in this paper, the potential contamination is noted in the results section.

## Limitations of contamination analysis

[p. 33] An important limitation of the contamination analysis is that the authors cannot be sure that the clean subset is drawn from the same distribution as the original dataset. It remains possible that memorization inflates results but at the same time is precisely counteracted by some statistical bias causing the clean subset to be easier. However, the sheer number of shifts close to zero suggests this is unlikely, and no noticeable difference in the shifts for small models, which are unlikely to be memorizing, was observed.

## Summary

[p. 33] Overall, the authors state they have made a best effort to measure and document the effects of data contamination, and to note or outright remove problematic results, depending on the severity. Much work remains to address this important and subtle issue for the field in general, both when designing benchmarks and when training models. A more detailed explanation of the analysis is in Appendix C.
