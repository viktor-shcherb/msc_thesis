# 4. Downstream Results [p. 14-19]

[p. 14]

Section 3 demonstrated the superior scaling properties while pre-training, but the authors now validate that these gains translate to improved language learning abilities on downstream tasks. They begin by fine-tuning on a diverse set of NLP tasks. Next they study reducing the memory footprint of the sparse models by over 90% by distilling into small -- and easily deployed -- dense baselines. Finally, the section concludes measuring the improvements in a multi-task, multilingual setting, where Switch Transformers are shown to be strong multi-task learners, improving over the multilingual T5-base model across all 101 languages.

## 4.1 Fine-Tuning [p. 14-16]

[p. 14-15]

**Baseline and Switch models used for fine-tuning.** The baselines are the highly-tuned 223M parameter T5-Base model and the 739M parameter T5-Large model (Raffel et al., 2019). For both versions, a FLOP-matched Switch Transformer is designed, with many more parameters, which is summarized in Table 9. The baselines differ slightly from those in Raffel et al. (2019) because they pre-train on an improved C4 corpus which removes intra-example text duplication and thus increases the efficacy as a pre-training task (Lee et al., 2021). In their protocol they pre-train with 2^{20} (1,048,576) tokens per batch for 550k steps amounting to 576B total tokens. They then fine-tune across a diverse set of tasks using a dropout rate of 0.1 for all layers except the Switch layers, which use a dropout rate of 0.4 (see Table 4). They fine-tune using a batch-size of 1M for 16k steps and for each task, they evaluate model quality every 200 steps and report the peak performance as computed on the validation set.

FLOPs are calculated for the forward pass as done in Kaplan et al. (2020). [p. 14, footnote 7]

The T5 and Switch models were pre-trained with 2^{20} tokens per batch for 550k steps on a revised C4 data set for fair comparisons. [p. 15, footnote 8]

[p. 15]

**Fine-tuning tasks and data sets.** Tasks are selected probing language capabilities including question answering, summarization and knowledge about the world. The language benchmarks GLUE (Wang et al., 2018) and SuperGLUE (Wang et al., 2019) are handled as composite mixtures with all the tasks blended in proportion to the amount of tokens present in each. These benchmarks consist of tasks requiring sentiment analysis (SST-2), word sense disambiguation (WIC), sentence similarity (MRPC, STS-B, QQP), natural language inference (MNLI, QNLI, RTE, CB), question answering (MultiRC, RECORD, BoolQ), coreference resolution (WNLI, WSC) and sentence completion (COPA) and sentence acceptability (CoLA). The CNNDM (Hermann et al., 2015) and BBC XSum (Narayan et al., 2018) data sets are used to measure the ability to summarize articles. Question answering is probed with the SQuAD data set (Rajpurkar et al., 2016) and the ARC Reasoning Challenge (Clark et al., 2018). And as in Roberts et al. (2020), the knowledge of the models is evaluated by fine-tuning on three closed-book question answering data sets: Natural Questions (Kwiatkowski et al., 2019), Web Questions (Berant et al., 2013) and Trivia QA (Joshi et al., 2017). Closed-book refers to questions posed with no supplemental reference or context material. To gauge the model's common sense reasoning the Winogrande Schema Challenge (Sakaguchi et al., 2020) is used. And finally, natural language inference capabilities are tested on the Adversarial NLI Benchmark (Nie et al., 2019).

**Fine-tuning metrics.** The following evaluation metrics are used throughout the paper: Average scores across all subtasks are reported for GLUE and SuperGLUE. The Rouge-2 metric is used both for CNNDM and XSum. In SQuAD and the closed book tasks (Web, Natural, and Trivia Questions) the percentage of answers exactly matching the target is reported (refer to Roberts et al. (2020) for further details and deficiency of this measure). Finally, in ARC Easy, ARC Challenge, ANLI, and Winogrande the accuracy of the generated responses is reported.

**Fine-tuning results.** Significant downstream improvements are observed across many natural language tasks. Notable improvements come from SuperGLUE, where FLOP-matched Switch variants improve by 4.4 and 2 percentage points over the T5-Base and T5-Large baselines, respectively, as well as large improvements in Winogrande, closed book Trivia QA, and XSum. In the fine-tuning study, the only tasks where gains are not observed are on the AI2 Reasoning Challenge (ARC) data sets where the T5-Base outperforms Switch-Base on the challenge data set and T5-Large outperforms Switch-Large on the easy data set. Taken as a whole, significant improvements are observed spanning both reasoning and knowledge-heavy tasks. This validates the architecture, not just as one that pre-trains well, but can translate quality improvements to downstream tasks via fine-tuning.

**Table 5** (p. 16): "Fine-tuning results. Fine-tuning results of T5 baselines and Switch models across a diverse set of natural language tests (validation sets; higher numbers are better). We compare FLOP-matched Switch models to the T5-Base and T5-Large baselines. For most tasks considered, we find significant improvements of the Switch-variants. We observe gains across both model sizes and across both reasoning and knowledge-heavy language tasks."

*Part 1: GLUE, SQuAD, SuperGLUE, Winogrande*

| Model | GLUE | SQuAD | SuperGLUE | Winogrande (XL) |
|---|---|---|---|---|
| T5-Base | 84.3 | 85.5 | 75.1 | 66.6 |
| Switch-Base | **86.7** | **87.2** | **79.5** | **73.3** |
| T5-Large | 87.8 | 88.1 | 82.7 | 79.1 |
| Switch-Large | **88.5** | **88.6** | **84.7** | **83.0** |

*Part 2: XSum, ANLI, ARC Easy, ARC Challenge*

| Model | XSum | ANLI (R3) | ARC Easy | ARC Chal. |
|---|---|---|---|---|
| T5-Base | 18.7 | 51.8 | 56.7 | **35.5** |
| Switch-Base | **20.3** | **54.0** | **61.3** | 32.8 |
| T5-Large | 20.9 | 56.6 | **68.8** | **35.5** |
| Switch-Large | **22.3** | **58.6** | 66.0 | **35.5** |

*Part 3: Closed-Book QA*

| Model | CB Web QA | CB Natural QA | CB Trivia QA |
|---|---|---|---|
| T5-Base | 26.6 | 25.8 | 24.5 |
| Switch-Base | **27.4** | **26.8** | **30.7** |
| T5-Large | 27.7 | 27.6 | 29.5 |
| Switch-Large | **31.3** | **29.5** | **36.9** |

## 4.2 Distillation [p. 16-18]

[p. 16]

Deploying massive neural networks with billions, or trillions, of parameters is inconvenient. To alleviate this, the authors study distilling (Hinton et al., 2015) large sparse models into small dense models. Future work could additionally study distilling large models into smaller *sparse* models.

**Distillation techniques.** In Table 6 a variety of distillation techniques are studied. These techniques are built off of Sanh et al. (2019), who study distillation methods for BERT models. Initializing the dense model with the non-expert weights yields a modest improvement. This is possible since all models are FLOP matched, so non-expert layers will have the same dimensions. Since expert layers are usually only added at every or every other FFN layer in a Transformer, this allows for many of the weights to be initialized with trained parameters. Furthermore, a distillation improvement is observed using a mixture of 0.25 for the teacher probabilities and 0.75 for the ground truth label. By combining both techniques approximately 30% of the quality gains from the larger sparse models are preserved with only approximately 1/20th of the parameters. The quality gain refers to the percent of the quality difference between Switch-Base (Teacher) and T5-Base (Student). Therefore, a quality gain of 100% implies the Student equals the performance of the Teacher. [p. 16-17]

**Table 6** (p. 17): "Distilling Switch Transformers for Language Modeling. Initializing T5-Base with the non-expert weights from Switch-Base and using a loss from a mixture of teacher and ground-truth labels obtains the best performance. We can distill 30% of the performance improvement of a large sparse model with 100x more parameters back into a small dense model. For a final baseline, we find no improvement of T5-Base initialized with the expert weights, but trained normally without distillation."

| Technique | Parameters | Quality (up arrow) |
|---|---|---|
| T5-Base | 223M | -1.636 |
| Switch-Base | 3,800M | -1.444 |
| Distillation | 223M | (3%) -1.631 |
| + Init. non-expert weights from teacher | 223M | (20%) -1.598 |
| + 0.75 mix of hard and soft loss | 223M | (29%) -1.580 |
| Initialization Baseline (no distillation) | | |
| Init. non-expert weights from teacher | 223M | -1.639 |

**Achievable compression rates.** Using the best distillation technique described in Table 6, a wide variety of sparse models are distilled into dense models. Switch-Base versions are distilled, sweeping over an increasing number of experts, which corresponds to varying between 1.1B to 14.7B parameters. Through distillation, 37% of the quality gain of the 1.1B parameter model is preserved while compressing 82%. At the extreme, where the model is compressed 99%, 28% of the teacher's model quality improvement is still maintained. [p. 18]

**Table 7** (p. 18): "Distillation compression rates. We measure the quality when distilling large sparse models into a dense baseline. Our baseline, T5-Base, has a -1.636 Neg. Log Perp. quality. In the right columns, we then distill increasingly large sparse models into this same architecture. Through a combination of weight-initialization and a mixture of hard and soft losses, we can shrink our sparse teachers by 95%+ while preserving 30% of the quality gain. However, for significantly better and larger pre-trained teachers, we expect larger student models would be necessary to achieve these compression rates."

|  | Dense | Sparse | | | | |
|---|---|---|---|---|---|---|
| Parameters | 223M | 1.1B | 2.0B | 3.8B | 7.4B | 14.7B |
| Pre-trained Neg. Log Perp. (up arrow) | -1.636 | -1.505 | -1.474 | -1.444 | -1.432 | -1.427 |
| Distilled Neg. Log Perp. (up arrow) | -- | -1.587 | -1.585 | -1.579 | -1.582 | -1.578 |
| Percent of Teacher Performance | -- | 37% | 32% | 30 % | 27 % | 28 % |
| Compression Percent | -- | 82 % | 90 % | 95 % | 97 % | 99 % |

**Distilling a fine-tuned model.** The section concludes with a study of distilling a fine-tuned sparse model into a dense model. Table 8 shows results of distilling a 7.4B parameter Switch-Base model, fine-tuned on the SuperGLUE task, into the 223M T5-Base. Similar to the pre-training results, 30% of the gains of the sparse model are preserved when distilling into a FLOP matched dense variant. One potential future avenue, not considered here, may examine the specific experts being used for fine-tuning tasks and extracting them to achieve better model compression. [p. 18]

**Table 8** (p. 18): "Distilling a fine-tuned SuperGLUE model. We distill a Switch-Base model fine-tuned on the SuperGLUE tasks into a T5-Base model. We observe that on smaller data sets our large sparse model can be an effective teacher for distillation. We find that we again achieve 30% of the teacher's performance on a 97% compressed model."

| Model | Parameters | FLOPS | SuperGLUE (up arrow) |
|---|---|---|---|
| T5-Base | 223M | 124B | 74.6 |
| Switch-Base | 7410M | 124B | 81.3 |
| Distilled T5-Base | 223M | 124B | (30%) 76.6 |

## 4.3 Multilingual Learning [p. 17-19]

[p. 17-19]

In the final set of downstream experiments, the authors measure the model quality and speed trade-offs while pre-training on a mixture of 101 different languages. They build and benchmark off the recent work of mT5 (Xue et al., 2020), a multilingual extension to T5. They pre-train on the multilingual variant of the Common Crawl data set (mC4) spanning 101 languages introduced in mT5, but due to script variants within certain languages, the mixture contains 107 tasks.

In Figure 7 the quality improvement in negative log perplexity is plotted for all languages of a FLOP-matched Switch model, mSwitch-Base to the T5 base variant, mT5-Base. After pre-training both versions for 1M steps, they find that on *all* 101 languages considered, Switch Transformer increases the final negative log perplexity over the baseline. In Figure 8, the per step *speed-up* of using Switch Transformer over the mT5-Base is presented as a histogram. A mean speed-up over mT5-Base of 5x is found and 91% of languages achieve at least a 4x speedup. This presents evidence that Switch Transformers are effective multi-task and multi-lingual learners. [p. 18-19]

The speedup on a step basis is computed as the ratio of the number of steps for the baseline divided by the number of steps required by the Switch model to reach that same quality. [p. 18, footnote 9]

**Figure 7** (p. 19): "Multilingual pre-training on 101 languages. Improvements of Switch T5 Base model over dense baseline when multi-task training on 101 languages. We observe Switch Transformers to do quite well in the multi-task training setup and yield improvements on all 101 languages."

- Scatter/line plot with x-axis "Language" (101 languages sorted left to right) and y-axis "Neg Log Perplexity" (ranging from approximately -1.8 to -0.4). Two series are plotted: "Switch" (blue dots) and "Dense" (orange dots). For every language, the Switch (blue) point is above (better, less negative) the Dense (orange) point, confirming improvements across all 101 languages. The gap between the two series is relatively consistent, with both curves trending upward from left to right as languages vary.

**Figure 8** (p. 19): "Multilingual pre-training on 101 languages. We histogram for each language, the step speedup of Switch Transformers over the FLOP matched T5 dense baseline to reach the same quality. Over all 101 languages, we achieve a mean step speed-up over mT5-Base of 5x and, for 91% of languages, we record a 4x, or greater, speedup to reach the final perplexity of mT5-Base."

- Histogram with x-axis "Switch Speedup over Dense Baseline" (ranging from ~2 to ~16) and y-axis "Number of Languages" (ranging from 0 to ~50). The distribution is right-skewed with a peak around 6-7x speedup (approximately 48 languages). Approximately 10 languages are at ~4x, ~15 languages at ~5x, a few at ~8-10x, ~3 at ~12x, and a small number at ~14-16x. The mean is 5x and 91% of languages achieve at least 4x speedup.
