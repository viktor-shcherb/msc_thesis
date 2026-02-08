# Capabilities [p. 4-9]

[p. 4] GPT-4 was tested on a diverse set of benchmarks, including simulating exams originally designed for humans. No specific training was done for these exams. A minority of the problems in the exams were seen by the model during training; for each exam a variant with these questions removed was run and the lower score of the two was reported. The results are believed to be representative. For further details on contamination (methodology and per-exam statistics), see Appendix C.

Exams were sourced from publicly-available materials. Exam questions included both multiple-choice and free-response questions; separate prompts were designed for each format, and images were included in the input for questions which required it. The evaluation setup was designed based on performance on a validation set of exams, and final results are reported on held-out test exams. Overall scores were determined by combining multiple-choice and free-response question scores using publicly available methodologies for each exam. The percentile each overall score corresponds to is estimated and reported. See Appendix A for further details on exam evaluation methodology. [p. 4]

Note: For AMC 10 and AMC 12 2022 exams, the human percentiles are not yet published, so the reported numbers are extrapolated and likely have wide uncertainty (see Appendix A.5). The post-trained RLHF model was used for these exams. [p. 4]

## Exam Results

**Table 1** (p. 5): "GPT performance on academic and professional exams. In each case, we simulate the conditions and scoring of the real exam. We report GPT-4's final score graded according to exam-specific rubrics, as well as the percentile of test-takers achieving GPT-4's score."

| Exam | GPT-4 | GPT-4 (no vision) | GPT-3.5 |
|---|---|---|---|
| Uniform Bar Exam (MBE+MEE+MPT) | 298 / 400 (~90th) | 298 / 400 (~90th) | 213 / 400 (~10th) |
| LSAT | 163 (~88th) | 161 (~83rd) | 149 (~40th) |
| SAT Evidence-Based Reading & Writing | 710 / 800 (~93rd) | 710 / 800 (~93rd) | 670 / 800 (~87th) |
| SAT Math | 700 / 800 (~89th) | 690 / 800 (~89th) | 590 / 800 (~70th) |
| Graduate Record Examination (GRE) Quantitative | 163 / 170 (~80th) | 157 / 170 (~62nd) | 147 / 170 (~25th) |
| Graduate Record Examination (GRE) Verbal | 169 / 170 (~99th) | 165 / 170 (~96th) | 154 / 170 (~63rd) |
| Graduate Record Examination (GRE) Writing | 4 / 6 (~54th) | 4 / 6 (~54th) | 4 / 6 (~54th) |
| USABO Semifinal Exam 2020 | 87 / 150 (99th - 100th) | 87 / 150 (99th - 100th) | 43 / 150 (31st - 33rd) |
| USNCO Local Section Exam 2022 | 36 / 60 | 38 / 60 | 24 / 60 |
| Medical Knowledge Self-Assessment Program | 75 % | 75 % | 53 % |
| Codeforces Rating | 392 (below 5th) | 392 (below 5th) | 260 (below 5th) |
| AP Art History | 5 (86th - 100th) | 5 (86th - 100th) | 5 (86th - 100th) |
| AP Biology | 5 (85th - 100th) | 5 (85th - 100th) | 4 (62nd - 85th) |
| AP Calculus BC | 4 (43rd - 59th) | 4 (43rd - 59th) | 1 (0th - 7th) |
| AP Chemistry | 4 (71st - 88th) | 4 (71st - 88th) | 2 (22nd - 46th) |
| AP English Language and Composition | 2 (14th - 44th) | 2 (14th - 44th) | 2 (14th - 44th) |
| AP English Literature and Composition | 2 (8th - 22nd) | 2 (8th - 22nd) | 2 (8th - 22nd) |
| AP Environmental Science | 5 (91st - 100th) | 5 (91st - 100th) | 5 (91st - 100th) |
| AP Macroeconomics | 5 (84th - 100th) | 5 (84th - 100th) | 2 (33rd - 48th) |
| AP Microeconomics | 5 (82nd - 100th) | 4 (60th - 82nd) | 4 (60th - 82nd) |
| AP Physics 2 | 4 (66th - 84th) | 4 (66th - 84th) | 3 (30th - 66th) |
| AP Psychology | 5 (83rd - 100th) | 5 (83rd - 100th) | 5 (83rd - 100th) |
| AP Statistics | 5 (85th - 100th) | 5 (85th - 100th) | 3 (40th - 63rd) |
| AP US Government | 5 (88th - 100th) | 5 (88th - 100th) | 4 (77th - 88th) |
| AP US History | 5 (89th - 100th) | 4 (74th - 89th) | 4 (74th - 89th) |
| AP World History | 4 (65th - 87th) | 4 (65th - 87th) | 4 (65th - 87th) |
| AMC 10 | 30 / 150 (6th - 12th) | 36 / 150 (10th - 19th) | 36 / 150 (10th - 19th) |
| AMC 12 | 60 / 150 (45th - 66th) | 48 / 150 (19th - 40th) | 30 / 150 (4th - 8th) |
| Introductory Sommelier (theory knowledge) | 92 % | 92 % | 80 % |
| Certified Sommelier (theory knowledge) | 86 % | 86 % | 58 % |
| Advanced Sommelier (theory knowledge) | 77 % | 77 % | 46 % |
| Leetcode (easy) | 31 / 41 | 31 / 41 | 12 / 41 |
| Leetcode (medium) | 21 / 80 | 21 / 80 | 8 / 80 |
| Leetcode (hard) | 3 / 45 | 3 / 45 | 0 / 45 |

**Figure 4** (p. 6): "GPT performance on academic and professional exams. In each case, we simulate the conditions and scoring of the real exam. Exams are ordered from low to high based on GPT-3.5 performance. GPT-4 outperforms GPT-3.5 on most exams tested. To be conservative we report the lower end of the range of percentiles, but this creates some artifacts on the AP exams which have very wide scoring bins. For example although GPT-4 attains the highest possible score on AP Biology (5/5), this is only shown in the plot as 85th percentile because 15 percent of test-takers achieve that score."

The figure is a bar chart showing estimated percentile lower bound (y-axis, 0% to 100%) across all exams (x-axis), with three color-coded bars per exam: green for GPT-4, light green for GPT-4 (no vision), and blue for GPT-3.5. Exams are ordered from low to high based on GPT-3.5 performance. GPT-4 (green) consistently equals or exceeds GPT-3.5 (blue) across nearly all exams. The lowest-performing exams for all models are AP Calculus BC, AMC 12, Codeforces Rating, and AP English Literature.

[p. 6] GPT-4 exhibits human-level performance on the majority of these professional and academic exams. Notably, it passes a simulated version of the Uniform Bar Examination with a score in the top 10% of test takers (Table 1, Figure 4).

The model's capabilities on exams appear to stem primarily from the pre-training process and are not significantly affected by RLHF. On multiple choice questions, both the base GPT-4 model and the RLHF model perform equally well on average across the exams tested (see Appendix B). [p. 6]

## Traditional NLP Benchmarks

[p. 6] The pre-trained base GPT-4 model was also evaluated on traditional benchmarks designed for evaluating language models. For each benchmark reported, contamination checks were run for test data appearing in the training set (see Appendix D for full details on per-benchmark contamination). Few-shot prompting [1] was used for all benchmarks when evaluating GPT-4.

Note: During the contamination check, portions of BIG-bench [48] were discovered to have been inadvertently mixed into the training set, and were excluded from reported results. For GSM-8K, part of the training set is included in GPT-4's pre-training mix (see Appendix E for details); chain-of-thought prompting [11] was used when evaluating. [p. 6]

GPT-4 considerably outperforms existing language models, as well as previously state-of-the-art (SOTA) systems which often have benchmark-specific crafting or additional training protocols (Table 2). [p. 6]

**Table 2** (p. 7): "Performance of GPT-4 on academic benchmarks. We compare GPT-4 alongside the best SOTA (with benchmark-specific training) and the best SOTA for an LM evaluated few-shot. GPT-4 outperforms existing LMs on all benchmarks, and beats SOTA with benchmark-specific training on all datasets except DROP. For each task we report GPT-4's performance along with the few-shot method used to evaluate. For GSM-8K, we included part of the training set in the GPT-4 pre-training mix (see Appendix E), and we use chain-of-thought prompting [11] when evaluating. For multiple-choice questions, we present all answers (ABCD) to the model and ask it to choose the letter of the answer, similarly to how a human would solve such a problem."

| Benchmark | GPT-4 (Evaluated few-shot) | GPT-3.5 (Evaluated few-shot) | LM SOTA (Best external LM evaluated few-shot) | SOTA (Best external model incl. benchmark-specific tuning) |
|---|---|---|---|---|
| MMLU [49] — Multiple-choice questions in 57 subjects (professional & academic) | **86.4%** (5-shot) | 70.0% (5-shot) | 70.7% — 5-shot U-PaLM [50] | 75.2% — 5-shot Flan-PaLM [51] |
| HellaSwag [52] — Commonsense reasoning around everyday events | **95.3%** (10-shot) | 85.5% (10-shot) | 84.2% — LLaMA (validation set) [28] | 85.6 — ALUM [53] |
| AI2 Reasoning Challenge (ARC) [54] — Grade-school multiple choice science questions. Challenge-set. | **96.3%** (25-shot) | 85.2% (25-shot) | 85.2% — 8-shot PaLM [55] | 86.5% — ST-MOE [18] |
| WinoGrande [56] — Commonsense reasoning around pronoun resolution | **87.5%** (5-shot) | 81.6% (5-shot) | 85.1% — 5-shot PaLM [3] | 85.1% — 5-shot PaLM [3] |
| HumanEval [43] — Python coding tasks | **67.0%** (0-shot) | 48.1% (0-shot) | 26.2% — 0-shot PaLM [3] | 65.8% — CodeT + GPT-3.5 [57] |
| DROP [58] (F1 score) — Reading comprehension & arithmetic | 80.9 (3-shot) | 64.1 (3-shot) | 70.8 — 1-shot PaLM [3] | **88.4** — QDGAT [59] |
| GSM-8K [60] — Grade-school mathematics questions | **92.0%*** (5-shot, chain-of-thought) | 57.1% (5-shot) | 58.8% — 8-shot Minerva [61] | 87.3% — Chinchilla + SFT+ORM-RL, ORM reranking [62] |

*Note: GSM-8K result marked with asterisk because part of the training set was included in GPT-4's pre-training mix.

---
[p. 7 continued]

## Multilingual Capabilities

[p. 7] Many existing ML benchmarks are written in English. To gain an initial understanding of GPT-4's capabilities in other languages, the authors translated the MMLU benchmark [35, 36] -- a suite of multiple-choice problems spanning 57 subjects -- into a variety of languages using Azure Translate (see Appendix F for example translations and prompts). GPT-4 outperforms the English-language performance of GPT-3.5 and existing language models (Chinchilla [2] and PaLM [3]) for the majority of languages tested, including low-resource languages such as Latvian, Welsh, and Swahili (Figure 5).

**Figure 5** (p. 8): "Performance of GPT-4 in a variety of languages compared to prior models in English on MMLU. GPT-4 outperforms the English-language performance of existing language models [2, 3] for the vast majority of languages tested, including low-resource languages such as Latvian, Welsh, and Swahili."

The figure is a horizontal bar chart showing GPT-4 3-shot accuracy on MMLU across languages. Y-axis lists languages, x-axis shows accuracy from 0% to 90%+. Five baselines are shown: Random guessing (grey), Chinchilla (grey), PaLM (grey), GPT-3.5 (blue), GPT-4 (green). Key data points:

| Language / Model | Accuracy |
|---|---|
| Random guessing | 25.0% |
| Chinchilla-English | 67.0% |
| PaLM-English | 69.3% |
| GPT-3.5-English | 70.1% |
| GPT-4 English | 85.5% |
| Italian | 84.1% |
| Afrikaans | 84.1% |
| Spanish | 84.0% |
| German | 83.7% |
| French | 83.6% |
| Indonesian | 83.1% |
| Russian | 82.7% |
| Polish | 82.1% |
| Ukrainian | 81.9% |
| Greek | 81.4% |
| Latvian | 80.9% |
| Mandarin | 80.1% |
| Arabic | 80.0% |
| Turkish | 80.0% |
| Japanese | 79.9% |
| Swahili | 78.5% |
| Welsh | 77.5% |
| Korean | 77.0% |
| Icelandic | 76.5% |
| Bengali | 73.2% |
| Urdu | 72.6% |
| Nepali | 72.2% |
| Thai | 71.8% |
| Punjabi | 71.4% |
| Marathi | 66.7% |
| Telugu | 62.0% |

GPT-4 in non-English languages exceeds GPT-3.5's English performance (70.1%) for 24 out of 26 languages shown (all except Marathi at 66.7% and Telugu at 62.0%).

## Following User Intent

[p. 7] GPT-4 substantially improves over previous models in the ability to follow user intent [63]. On a dataset of 5,214 prompts submitted to ChatGPT [64] and the OpenAI API [47], the responses generated by GPT-4 were preferred over the responses generated by GPT-3.5 on 70.2% of prompts.

Note: User prompts were collected via ChatGPT and the OpenAI API; one response was sampled from each model and sent to human labelers who judged whether the response matched user intent. Labelers were not told which model generated which response and the order was randomised. Prompts containing disallowed/sensitive content, PII, sexual content, hate-speech, and overly-common prompts (e.g. "Hello, ChatGPT!") were filtered out. [p. 7]

## OpenAI Evals

[p. 7] OpenAI Evals is being open-sourced as a framework for creating and running benchmarks for evaluating models like GPT-4 while inspecting performance sample by sample. Evals is compatible with existing benchmarks, and can be used to track performance of models in deployment. The plan is to increase the diversity of these benchmarks over time to represent a wider set of failure modes and a harder set of tasks. [p. 8]

## 4.1 Visual Inputs

[p. 8] GPT-4 accepts prompts consisting of both images and text, which -- parallel to the text-only setting -- lets the user specify any vision or language task. Specifically, the model generates text outputs given inputs consisting of arbitrarily interlaced text and images. Over a range of domains -- including documents with text and photographs, diagrams, or screenshots -- GPT-4 exhibits similar capabilities as it does on text-only inputs. An example of GPT-4's visual input can be found in Table 3. The standard test-time techniques developed for language models (e.g. few-shot prompting, chain-of-thought, etc) are similarly effective when using both images and text -- see Appendix G for examples.

Preliminary results on a narrow set of academic vision benchmarks can be found in the GPT-4 blog post [65]. The authors plan to release more information about GPT-4's visual capabilities in follow-up work. [p. 8]

**Table 3** (p. 9): "Example prompt demonstrating GPT-4's visual input capability. The prompt consists of a question about an image with multiple panels which GPT-4 is able to answer."

The table shows a user prompt asking "What is funny about this image? Describe it panel by panel." along with an image (sourced from reddit.com/r/hmmm/comments/ubab5v/hmmm/) showing a "Lightning Cable" adapter package. GPT-4's response describes three panels:

- Panel 1: A smartphone with a VGA connector (a large, blue, 15-pin connector typically used for computer monitors) plugged into its charging port.
- Panel 2: The package for the "Lightning Cable" adapter with a picture of a VGA connector on it.
- Panel 3: A close-up of the VGA connector with a small Lightning connector (used for charging iPhones and other Apple devices) at the end.

GPT-4 identifies the humor as coming from the absurdity of plugging a large, outdated VGA connector into a small, modern smartphone charging port. [p. 9]
