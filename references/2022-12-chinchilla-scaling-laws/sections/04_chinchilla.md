# 4. *Chinchilla* [p. 9-11]

[p. 9] Based on the analysis in Section 3, the optimal model size for the *Gopher* compute budget is somewhere between 40 and 70 billion parameters. This hypothesis is tested by training a model on the larger end of this range -- 70B parameters -- for 1.4T tokens, due to both dataset and computational efficiency considerations. This model, called *Chinchilla*, is compared to *Gopher* and other LLMs. Both *Chinchilla* and *Gopher* have been trained for the same number of FLOPs but differ in the size of the model and the number of training tokens.

While pre-training a large language model has a considerable compute cost, downstream fine-tuning and inference also make up substantial compute usage (Rae et al., 2021). Due to being 4x smaller than *Gopher*, both the memory footprint and inference cost of *Chinchilla* are also smaller.

## 4.1 Model and training details [p. 9]

[p. 9] The full set of hyperparameters used to train *Chinchilla* are given in Table 4. *Chinchilla* uses the same model architecture and training setup as *Gopher* with the exception of the following differences:

- *Chinchilla* is trained on *MassiveText* (the same dataset as *Gopher*) but uses a slightly different subset distribution (shown in Table A1) to account for the increased number of training tokens.
- AdamW (Loshchilov and Hutter, 2019) is used for *Chinchilla* rather than Adam (Kingma and Ba, 2014) as this improves the language modelling loss and the downstream task performance after finetuning.^8
- *Chinchilla* is trained with a slightly modified SentencePiece (Kudo and Richardson, 2018) tokenizer that does not apply NFKC normalisation. The vocabulary is very similar -- 94.15% of tokens are the same as those used for training *Gopher*. This particularly helps with the representation of mathematics and chemistry, for example.
- Whilst the forward and backward pass are computed in bfloat16, a float32 copy of the weights is stored in the distributed optimiser state (Rajbhandari et al., 2020). See *Lessons Learned* from Rae et al. (2021) for additional details.

Footnote 8: "Interestingly, a model trained with AdamW only passes the training performance of a model trained with Adam around 80% of the way through the cosine cycle, though the ending performance is notably better -- see Figure A7." [p. 9]

In Appendix G the impact of the various optimiser related changes between *Chinchilla* and *Gopher* is shown. All models in this analysis have been trained on TPUv3/TPUv4 (Jouppi et al., 2017) with JAX (Bradbury et al., 2018) and Haiku (Hennigan et al., 2020). A *Chinchilla* model card is included (Mitchell et al., 2019) in Table A8.

**Table 4** (p. 9): "*Chinchilla* architecture details. We list the number of layers, the key/value size, the bottleneck activation size d_model, the maximum learning rate, and the training batch size (# tokens). The feed-forward size is always set to 4 x d_model. Note that we double the batch size midway through training for both *Chinchilla* and *Gopher*."

| Model | Layers | Number Heads | Key/Value Size | d_model | Max LR | Batch Size |
|---|---|---|---|---|---|---|
| *Gopher* 280B | 80 | 128 | 128 | 16,384 | 4 x 10^-5 | 3M -> 6M |
| *Chinchilla* 70B | 80 | 64 | 128 | 8,192 | 1 x 10^-4 | 1.5M -> 3M |

## 4.2 Results [p. 10]

[p. 10] An extensive evaluation of *Chinchilla* is performed, comparing against various large language models. Evaluation is done on a large subset of the tasks presented in Rae et al. (2021), shown in Table 5. As the focus of this work is on optimal model scaling, a large representative subset was included, and a few new evaluations were introduced to allow for better comparison to other existing large models. The evaluation details for all tasks are the same as described in Rae et al. (2021).

**Table 5** (p. 10): "All evaluation tasks. We evaluate Chinchilla on a collection of language modelling along with downstream tasks. We evaluate on largely the same tasks as in Rae et al. (2021), to allow for direct comparison."

| Category | # Tasks | Examples |
|---|---|---|
| Language Modelling | 20 | WikiText-103, The Pile: PG-19, arXiv, FreeLaw, ... |
| Reading Comprehension | 3 | RACE-m, RACE-h, LAMBADA |
| Question Answering | 3 | Natural Questions, TriviaQA, TruthfulQA |
| Common Sense | 5 | HellaSwag, Winogrande, PIQA, SIQA, BoolQ |
| MMLU | 57 | High School Chemistry, Astronomy, Clinical Knowledge, ... |
| BIG-bench | 62 | Causal Judgement, Epistemic Reasoning, Temporal Sequences, ... |

### 4.2.1 Language modelling [p. 10-11]

**Figure 5** (p. 10): "Pile Evaluation. For the different evaluation sets in The Pile (Gao et al., 2020), we show the bits-per-byte (bpb) improvement (decrease) of Chinchilla compared to Gopher. On all subsets, Chinchilla outperforms Gopher."

The figure is a bar chart showing the decrease in bits-per-byte (bpb) of *Chinchilla* compared to *Gopher* across 19 Pile evaluation subsets. The y-axis shows "Decrease in bpb compared to Gopher" (range 0.00 to 0.10). All bars are positive, indicating *Chinchilla* outperforms *Gopher* on every subset. The subsets shown on the x-axis (from left to right): pubmed_abstracts, nih_exporter, uspto_backgrounds, pubmed_central, pile_cc, bookcorpus2, stackexchange, opensubtitles, openwebtext2, hackernews, arxiv, freelaw, dm_mathematics, books3, philpapers, github, ubuntu_irc, europarl, gutenberg_pg_19. The largest improvements (roughly 0.08-0.10 bpb) are on ubuntu_irc, europarl, and gutenberg_pg_19. The smallest improvements (~0.02 bpb) are on pubmed_abstracts, nih_exporter, and uspto_backgrounds.

[p. 10-11] *Chinchilla* significantly outperforms *Gopher* on all evaluation subsets of The Pile (Gao et al., 2020), as shown in Figure 5. Compared to Jurassic-1 (178B) Lieber et al. (2021), *Chinchilla* is more performant on all but two subsets -- dm_mathematics and ubuntu_irc -- see Table A5 for a raw bits-per-byte comparison. On Wikitext103 (Merity et al., 2017), *Chinchilla* achieves a perplexity of 7.16 compared to 7.75 for *Gopher*. Some caution is needed when comparing *Chinchilla* with *Gopher* on these language modelling benchmarks as *Chinchilla* is trained on 4x more data than *Gopher* and thus train/test set leakage may artificially enhance the results. More emphasis is therefore placed on other tasks for which leakage is less of a concern, such as MMLU (Hendrycks et al., 2020) and BIG-bench (BIG-bench collaboration, 2021) along with various closed-book question answering and common sense analyses.

### 4.2.2 MMLU [p. 11]

[p. 11] The Massive Multitask Language Understanding (MMLU) benchmark (Hendrycks et al., 2020) consists of a range of exam-like questions on academic subjects. In Table 6, *Chinchilla*'s average 5-shot performance on MMLU is reported (the full breakdown of results is shown in Table A6). On this benchmark, *Chinchilla* significantly outperforms *Gopher* despite being much smaller, with an average accuracy of 67.6% (improving upon *Gopher* by 7.6%). Remarkably, *Chinchilla* even outperforms the expert forecast for June 2023 of 63.4% accuracy (see Table 6) (Steinhardt, 2021). Furthermore, *Chinchilla* achieves greater than 90% accuracy on 4 different individual tasks -- high_school_gov_and_politics, international_law, sociology, and us_foreign_policy. To the authors' knowledge, no other model has achieved greater than 90% accuracy on a subset.

In Figure 6, a comparison to *Gopher* broken down by task is shown. Overall, *Chinchilla* improves performance on the vast majority of tasks. On four tasks (college_mathematics, econometrics, moral_scenarios, and formal_logic) *Chinchilla* underperforms *Gopher*, and there is no change in performance on two tasks.

**Table 6** (p. 11): "Massive Multitask Language Understanding (MMLU). We report the average 5-shot accuracy over 57 tasks with model and human accuracy comparisons taken from Hendrycks et al. (2020). We also include the average prediction for state of the art accuracy in June 2022/2023 made by 73 competitive human forecasters in Steinhardt (2021)."

| Model / Baseline | Accuracy |
|---|---|
| Random | 25.0% |
| Average human rater | 34.5% |
| GPT-3 5-shot | 43.9% |
| *Gopher* 5-shot | 60.0% |
| ***Chinchilla* 5-shot** | **67.6%** |
| Average human expert performance | *89.8%* |
| June 2022 Forecast | 57.1% |
| June 2023 Forecast | 63.4% |

### 4.2.3 Reading comprehension [p. 11]

[p. 11] On the final word prediction dataset LAMBADA (Paperno et al., 2016), *Chinchilla* achieves 77.4% accuracy, compared to 74.5% accuracy from *Gopher* and 76.6% from MT-NLG 530B (see Table 7). On RACE-h and RACE-m (Lai et al., 2017), *Chinchilla* greatly outperforms *Gopher*, improving accuracy by more than 10% in both cases -- see Table 7.

### 4.2.4 BIG-bench [p. 11]

[p. 11] *Chinchilla* is analysed on the same set of BIG-bench tasks (BIG-bench collaboration, 2021) reported in Rae et al. (2021). Similar to what was observed in MMLU, *Chinchilla* outperforms *Gopher* on the vast majority of tasks (see Figure 7). *Chinchilla* improves the average performance by 10.7%, reaching an accuracy of 65.1% versus 54.4% for *Gopher*. Of the 62 tasks considered, *Chinchilla* performs worse than *Gopher* on only four -- crash_blossom, dark_humor_detection, mathematical_induction, and logical_args. Full accuracy results for *Chinchilla* can be found in Table A7.

**Figure 6** (p. 12): "**MMLU results compared to *Gopher*** We find that *Chinchilla* outperforms *Gopher* by 7.6% on average (see Table 6) in addition to performing better on 51/57 individual tasks, the same on 2/57, and worse on only 4/57 tasks."

The figure is a bar chart showing relative improvement of *Chinchilla* over *Gopher* on each of the 57 MMLU tasks. Y-axis: "Relative Improvement over Gopher" (range roughly -10 to 35). X-axis lists all 57 tasks. The vast majority of bars are positive (blue), indicating *Chinchilla* outperforms *Gopher*. A small number of tasks at the left end show negative bars (orange), including college_mathematics, formal_logic, moral_scenarios. The largest positive improvements (roughly 25-35) are on tasks at the far right including conceptual_physics, high_school_mathematics.

**Table 7** (p. 12): "**Reading comprehension.** On RACE-h and RACE-m (Lai et al., 2017), *Chinchilla* considerably improves performance over *Gopher*. Note that GPT-3 and MT-NLG 530B use a different prompt format than we do on RACE-h/m, so results are not comparable to *Gopher* and *Chinchilla*. On LAMBADA (Paperno et al., 2016), *Chinchilla* outperforms both *Gopher* and MT-NLG 530B."

|  | *Chinchilla* | *Gopher* | GPT-3 | MT-NLG 530B |
|---|---|---|---|---|
| LAMBADA Zero-Shot | **77.4** | 74.5 | 76.2 | 76.6 |
| RACE-m Few-Shot | **86.8** | 75.1 | 58.1 | - |
| RACE-h Few-Shot | **82.3** | 71.6 | 46.8 | 47.9 |

**Figure 7** (p. 13): "**BIG-bench results compared to *Gopher*** *Chinchilla* out performs *Gopher* on all but four BIG-bench tasks considered. Full results are in Table A7."

The figure is a bar chart showing relative improvement of *Chinchilla* over *Gopher* on each of the 62 BIG-bench tasks. Y-axis: "Relative Improvement over Gopher" (range roughly -20 to 120). X-axis lists all 62 tasks. The vast majority of bars are positive (blue). Only four tasks show negative bars (orange) at the far left: crash_blossom, dark_humor_detection, mathematical_induction, and logical_args. The largest positive improvements (roughly 80-120) are on tasks at the far right including analogical_similarity, gre_reading_comprehension, temporal_sequences.

---
[p. 12-13 continued]

### 4.2.5 Common sense [p. 12-13]

[p. 12-13] *Chinchilla* is evaluated on various common sense benchmarks: PIQA (Bisk et al., 2020), SIQA (Sap et al., 2019), Winogrande (Sakaguchi et al., 2020), HellaSwag (Zellers et al., 2019), and BoolQ (Clark et al., 2019). *Chinchilla* outperforms both *Gopher* and GPT-3 on all tasks and outperforms MT-NLG 530B on all but one task -- see Table 8.

On TruthfulQA (Lin et al., 2021), *Chinchilla* reaches 43.6%, 58.5%, and 66.7% accuracy with 0-shot, 5-shot, and 10-shot respectively. In comparison, *Gopher* achieved only 29.5% 0-shot and 43.7% 10-shot accuracy. In stark contrast with the findings of Lin et al. (2021), the large improvements (14.1% in 0-shot accuracy) achieved by Chinchilla suggest that better modelling of the pre-training data alone can lead to substantial improvements on this benchmark.

**Table 8** (p. 13): "**Zero-shot comparison on Common Sense benchmarks.** We show a comparison between *Chinchilla*, *Gopher*, and MT-NLG 530B on various Common Sense benchmarks. We see that *Chinchilla* matches or outperforms *Gopher* and GPT-3 on all tasks. On all but one *Chinchilla* outperforms the much larger MT-NLG 530B model."

|  | *Chinchilla* | *Gopher* | GPT-3 | MT-NLG 530B | Supervised SOTA |
|---|---|---|---|---|---|
| HellaSWAG | **80.8%** | 79.2% | 78.9% | 80.2% | 93.9% |
| PIQA | 81.8% | 81.8% | 81.0% | **82.0%** | 90.1% |
| Winogrande | **74.9%** | 70.1% | 70.2% | 73.0% | 91.3% |
| SIQA | **51.3%** | 50.6% | - | - | 83.2% |
| BoolQ | **83.7%** | 79.3% | 60.5% | 78.2% | 91.4% |

### 4.2.6 Closed-book question answering [p. 13-14]

[p. 13-14] Results on closed-book question answering benchmarks are reported in Table 9. On the Natural Questions dataset (Kwiatkowski et al., 2019), *Chinchilla* achieves new closed-book SOTA accuracies: 31.5% 5-shot and 35.5% 64-shot, compared to 21% and 28% respectively, for *Gopher*. On TriviaQA (Joshi et al., 2017) results are shown for both the filtered (previously used in retrieval and open-book work) and unfiltered set (previously used in large language model evaluations). In both cases, *Chinchilla* substantially outperforms *Gopher*. On the filtered version, Chinchilla lags behind the open book SOTA (Izacard and Grave, 2020) by only 7.9%. On the unfiltered set, *Chinchilla* outperforms GPT-3 -- see Table 9.

**Table 9** (p. 14): "**Closed-book question answering.** For Natural Questions (Kwiatkowski et al., 2019) and TriviaQA (Joshi et al., 2017), *Chinchilla* outperforms *Gopher* in all cases. On Natural Questions, *Chinchilla* outperforms GPT-3. On TriviaQA we show results on two different evaluation sets to allow for comparison to GPT-3 and to open book SOTA (FiD + Distillation (Izacard and Grave, 2020))."

| | Method | *Chinchilla* | *Gopher* | GPT-3 | SOTA (open book) |
|---|---|---|---|---|---|
| Natural Questions (dev) | 0-shot | 16.6% | 10.1% | 14.6% | |
| | 5-shot | 31.5% | 24.5% | - | 54.4% |
| | 64-shot | 35.5% | 28.2% | 29.9% | |
| TriviaQA (unfiltered, test) | 0-shot | 67.0% | 52.8% | 64.3% | |
| | 5-shot | 73.2% | 63.6% | - | - |
| | 64-shot | 72.3% | 61.3% | 71.2% | |
| TriviaQA (filtered, dev) | 0-shot | 55.4% | 43.5% | - | |
| | 5-shot | 64.1% | 57.0% | - | 72.5% |
| | 64-shot | 64.6% | 57.2% | - | |

### 4.2.7 Gender bias and toxicity [p. 13-15]

[p. 13-14] Large Language Models carry potential risks such as outputting offensive language, propagating social biases, and leaking private information (Bender et al., 2021; Weidinger et al., 2021). *Chinchilla* is expected to carry risks similar to *Gopher* because *Chinchilla* is trained on the same data, albeit with slightly different relative weights, and because it has a similar architecture. The authors examine gender bias (particularly gender and occupation bias) and generation of toxic language, selecting a few common evaluations to highlight potential issues, but stressing that their evaluations are not comprehensive and much work remains to understand, evaluate, and mitigate risks in LLMs.

**Gender bias.** [p. 14] As discussed in Rae et al. (2021), large language models reflect contemporary and historical discourse about different groups (such as gender groups) from their training dataset, and the same is expected to be true for *Chinchilla*. Potential gender and occupation biases are tested using the Winogender dataset (Rudinger et al., 2018) in a zero-shot setting. Winogender tests whether a model can correctly determine if a pronoun refers to different occupation words. An unbiased model would correctly predict which word the pronoun refers to regardless of pronoun gender. The same setup as in Rae et al. (2021) is followed (described further in Section H.3).

As shown in Table 10, *Chinchilla* correctly resolves pronouns more frequently than *Gopher* across all groups. Interestingly, the performance increase is considerably smaller for male pronouns (increase of 3.2%) than for female or neutral pronouns (increases of 8.3% and 9.2% respectively). *Gotcha* examples are also considered, in which the correct pronoun resolution contradicts gender stereotypes (determined by labor statistics). Again, *Chinchilla* resolves pronouns more accurately than *Gopher*. When breaking up examples by male/female gender and *gotcha*/*not gotcha*, the largest improvement is on female *gotcha* examples (improvement of 10%). Thus, though *Chinchilla* uniformly overcomes gender stereotypes for more coreference examples than *Gopher*, the rate of improvement is higher for some pronouns than others, suggesting that the improvements conferred by using a more compute-optimal model can be uneven.

**Table 10** (p. 15): "**Winogender results. Left:** *Chinchilla* consistently resolves pronouns better than *Gopher*. **Right:** *Chinchilla* performs better on examples which contradict gender stereotypes (*gotcha* examples). However, difference in performance across groups suggests *Chinchilla* exhibits bias."

| | *Chinchilla* | *Gopher* | | | *Chinchilla* | *Gopher* |
|---|---|---|---|---|---|---|
| All | 78.3% | 71.4% | | Male *gotcha* | 62.5% | 59.2% |
| Male | 71.2% | 68.0% | | Male *not gotcha* | 80.0% | 76.7% |
| Female | 79.6% | 71.3% | | Female *gotcha* | 76.7% | 66.7% |
| Neutral | 84.2% | 75.0% | | Female *not gotcha* | 82.5% | 75.8% |

**Sample toxicity.** [p. 14-15] Language models are capable of generating toxic language -- including insults, hate speech, profanities and threats (Gehman et al., 2020; Rae et al., 2021). While toxicity is an umbrella term, and its evaluation in LMs comes with challenges (Welbl et al., 2021; Xu et al., 2021), automatic classifier scores can provide an indication for the levels of harmful text that a LM generates. Rae et al. (2021) found that improving language modelling loss by increasing the number of model parameters has only a negligible effect on toxic text generation (unprompted); here the analysis examines whether the same holds true for a lower LM loss achieved via more compute-optimal training. Similar to the protocol of Rae et al. (2021), 25,000 unprompted samples are generated from *Chinchilla*, and their *PerspectiveAPI* toxicity score distribution is compared to that of *Gopher*-generated samples. Several summary statistics indicate an absence of major differences: the mean (median) toxicity score for *Gopher* is 0.081 (0.064), compared to 0.087 (0.066) for *Chinchilla*, and the 95th percentile scores are 0.230 for *Gopher*, compared to 0.238 for *Chinchilla*. That is, the large majority of generated samples are classified as non-toxic, and the difference between the models is negligible. In line with prior findings (Rae et al., 2021), this suggests that toxicity levels in unconditional text generation are largely independent of the model quality (measured in language modelling loss), i.e. that better models of the training dataset are not necessarily more toxic.
