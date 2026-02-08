# 1. Introduction [p. 3-6]

## Trend toward pre-trained language representations

[p. 3] Recent years have featured a trend towards pre-trained language representations in NLP, applied in increasingly flexible and task-agnostic ways for downstream transfer:

1. Single-layer word vector representations [MCCD13, PSM14] fed to task-specific architectures.
2. RNNs with multiple layers of representations and contextual state for stronger representations [DL15, MBXS17, PNZtY18] (still applied to task-specific architectures).
3. Pre-trained recurrent or transformer language models [VSP+17] directly fine-tuned, entirely removing the need for task-specific architectures [RNSS18, DCLT18, HR18].

This last paradigm has led to substantial progress on many challenging NLP tasks such as reading comprehension, question answering, textual entailment, and many others, and has continued to advance based on new architectures and algorithms [RSR+19, LOG+19, YDY+19, LCG+19].

## Limitations of the fine-tuning paradigm

[p. 3] A major limitation: while the architecture is task-agnostic, there is still a need for task-specific datasets and task-specific fine-tuning. Achieving strong performance on a desired task typically requires fine-tuning on a dataset of thousands to hundreds of thousands of examples specific to that task. Three reasons removing this limitation would be desirable:

**Reason 1 -- Practical:** [p. 3] The need for a large dataset of labeled examples for every new task limits the applicability of language models. There exists a very wide range of possible useful language tasks, and for many of these tasks it is difficult to collect a large supervised training dataset, especially when the process must be repeated for every new task.

**Reason 2 -- Spurious correlations:** [p. 3] The potential to exploit spurious correlations in training data fundamentally grows with the expressiveness of the model and the narrowness of the training distribution. This creates problems for the pre-training plus fine-tuning paradigm, where models are designed to be large to absorb information during pre-training, but are then fine-tuned on very narrow task distributions. [HLW+20] observe that larger models do not necessarily generalize better out-of-distribution. There is evidence that the generalization achieved under this paradigm can be poor because the model is overly specific to the training distribution and does not generalize well outside it [YdC+19, MPL19]. The performance of fine-tuned models on specific benchmarks, even when nominally at human-level, may exaggerate actual performance on the underlying task [GSL+18, NK19].

**Reason 3 -- Humans learn differently:** [p. 3] Humans do not require large supervised datasets to learn most language tasks -- a brief directive in natural language or at most a tiny number of demonstrations is often sufficient to enable a human to perform a new task to at least a reasonable degree of competence.

## Meta-learning and in-context learning

[p. 4] One potential route towards addressing these issues is meta-learning -- which in the context of language models means the model develops a broad set of skills and pattern recognition abilities at training time, and then uses those abilities at inference time to rapidly adapt to or recognize the desired task (illustrated in Figure 1.1). Recent work [RWC+19] attempts to do this via what the authors call "in-context learning", using the text input of a pretrained language model as a form of task specification: the model is conditioned on a natural language instruction and/or a few demonstrations of the task and is then expected to complete further instances of the task simply by predicting what comes next.

[p. 4] While it has shown some initial promise, this approach still achieves results far inferior to fine-tuning -- for example [RWC+19] achieves only 4% on Natural Questions, and even its 55 F1 CoQa result is now more than 35 points behind the state of the art. Meta-learning clearly requires substantial improvement to be viable as a practical method of solving language tasks.

## Scaling as a path forward

[p. 4] The capacity of transformer language models has increased substantially in recent years: from 100 million parameters [RNSS18], to 300 million parameters [DCLT18], to 1.5 billion parameters [RWC+19], to 8 billion parameters [SPP+19], 11 billion parameters [RSR+19], and finally 17 billion parameters [Tur20]. Each increase has brought improvements in text synthesis and/or downstream NLP tasks, and there is evidence suggesting that log loss, which correlates well with many downstream tasks, follows a smooth trend of improvement with scale [KMH+20]. Since in-context learning involves absorbing many skills and tasks within the parameters of the model, it is plausible that in-context learning abilities might show similarly strong gains with scale.

## This paper's contribution

[p. 5] The authors test this hypothesis by training a 175 billion parameter autoregressive language model, which they call GPT-3, and measuring its in-context learning abilities. GPT-3 is evaluated on over two dozen NLP datasets, as well as several novel tasks designed to test rapid adaptation to tasks unlikely to be directly contained in the training set.

Three evaluation conditions: [p. 5]
- **(a) "Few-shot learning" (FS):** in-context learning where as many demonstrations as will fit into the model's context window (typically 10 to 100) are allowed.
- **(b) "One-shot learning" (1S):** only one demonstration is allowed.
- **(c) "Zero-shot learning" (0S):** no demonstrations are allowed and only an instruction in natural language is given to the model.

GPT-3 is applied without any gradient updates or fine-tuning for all tasks; tasks and few-shot demonstrations are specified purely via text interaction with the model.

## Key results summary

[p. 5] Broadly, on NLP tasks GPT-3 achieves promising results in the zero-shot and one-shot settings, and in the few-shot setting is sometimes competitive with or even occasionally surpasses state-of-the-art (despite state-of-the-art being held by fine-tuned models). Specific results:
- GPT-3 achieves 81.5 F1 on CoQA in the zero-shot setting, 84.0 F1 in the one-shot setting, 85.0 F1 in the few-shot setting.
- GPT-3 achieves 64.3% accuracy on TriviaQA in the zero-shot setting, 68.0% in the one-shot setting, and 71.2% in the few-shot setting, the last of which is state-of-the-art relative to fine-tuned models operating in the same closed-book setting.

[p. 5] GPT-3 also displays one-shot and few-shot proficiency at tasks designed to test rapid adaption or on-the-fly reasoning, which include unscrambling words, performing arithmetic, and using novel words in a sentence after seeing them defined only once. GPT-3 can generate synthetic news articles which human evaluators have difficulty distinguishing from human-generated articles.

[p. 5] Tasks where few-shot performance struggles even at the scale of GPT-3 include natural language inference tasks like the ANLI dataset, and some reading comprehension datasets like RACE or QuAC.

## Data contamination

[p. 6] The authors also undertake a systematic study of "data contamination" -- a growing problem when training high capacity models on datasets such as Common Crawl, which can potentially include content from test datasets simply because such content often exists on the web. They develop systematic tools to measure data contamination and quantify its distorting effects. Although data contamination has a minimal effect on GPT-3's performance on most datasets, they identify a few datasets where it could be inflating results, and either do not report results on these datasets or note them with an asterisk.

## Smaller model series

[p. 6] In addition, the authors train a series of smaller models (ranging from 125 million parameters to 13 billion parameters) to compare their performance to GPT-3 in the zero, one and few-shot settings. For most tasks they find relatively smooth scaling with model capacity in all three settings; one notable pattern is that the gap between zero-, one-, and few-shot performance often grows with model capacity, perhaps suggesting that larger models are more proficient meta-learners.

## Broader impacts

[p. 6] Given the broad spectrum of capabilities displayed by GPT-3, the authors discuss concerns about bias, fairness, and broader societal impacts, and attempt a preliminary analysis of GPT-3's characteristics in this regard.

## Paper organization

[p. 6] The remainder of the paper is organized as follows. Section 2 describes the approach and methods for training GPT-3 and evaluating it. Section 3 presents results on the full range of tasks in the zero-, one- and few-shot settings. Section 4 addresses questions of data contamination (train-test overlap). Section 5 discusses limitations of GPT-3. Section 6 discusses broader impacts. Section 7 reviews related work and Section 8 concludes.

## Figures

**Figure 1.1** (p. 3): "Language model meta-learning. During unsupervised pre-training, a language model develops a broad set of skills and pattern recognition abilities. It then uses these abilities at inference time to rapidly adapt to or recognize the desired task. We use the term 'in-context learning' to describe the inner loop of this process, which occurs within the forward-pass upon each sequence. The sequences in this diagram are not intended to be representative of the data a model would see during pre-training, but are intended to show that there are sometimes repeated sub-tasks embedded within a single sequence."
- Shows an outer loop (learning via SGD during unsupervised pre-training) with an arrow spanning multiple sequences, and an inner loop (in-context learning) within each sequence. Three example sequences shown: arithmetic (5+8=13, 7+2=9, ...), word unscrambling (goat => goat, sakne => snake, ...), and English-to-French translation (thanks => merci, hello => bonjour, ...).

**Figure 1.2** (p. 4): "Larger models make increasingly efficient use of in-context information. We show in-context learning performance on a simple task requiring the model to remove random symbols from a word, both with and without a natural language task description (see Sec. 3.9.2). The steeper 'in-context learning curves' for large models demonstrate improved ability to learn a task from contextual information. We see qualitatively similar behavior across a wide range of tasks."
- X-axis: Number of Examples in Context (K), from 0 to ~10^1, log scale. Y-axis: Accuracy (%), from 0 to ~65%. Three model sizes shown: 175B Params (orange, top), 13B Params (green, middle), 1.3B Params (blue, bottom). Each size has two lines: solid (with Natural Language Prompt) and dashed (No Prompt). The 175B model with prompt reaches ~60-65% accuracy at K~10-100. All curves show steeper improvement for larger models. Zero-shot, one-shot, and few-shot regions are indicated.

**Figure 1.3** (p. 5): "Aggregate performance for all 42 accuracy-denominated benchmarks. While zero-shot performance improves steadily with model size, few-shot performance increases more rapidly, demonstrating that larger models are more proficient at in-context learning. See Figure 3.8 for a more detailed analysis on SuperGLUE, a standard NLP benchmark suite."
- X-axis: Parameters in LM (Billions), from 0.1B to 175B. Y-axis: Accuracy, from 0 to 100. Three lines: Few Shot (orange), One Shot (green), Zero Shot (blue). Thin colored lines show individual task performance; thick lines show aggregate. All three settings improve with scale, but the gap between few-shot and zero-shot widens at larger model sizes. At 175B, Few Shot aggregate is approximately 60-65, One Shot approximately 50-55, Zero Shot approximately 45-50.

## Footnote on terminology

[p. 4] Footnote 1: The authors use "meta-learning" to capture the inner-loop / outer-loop structure of the general method, and "in context-learning" to refer to the inner loop of meta-learning. They further specialize the description to "zero-shot", "one-shot", or "few-shot" depending on how many demonstrations are provided at inference time. These terms are intended to remain agnostic on the question of whether the model learns new tasks from scratch at inference time or simply recognizes patterns seen during training. In the context of language models, "zero-shot transfer" has sometimes been called ambiguous because the method is "zero-shot" in the sense that no gradient updates are performed, but it often involves providing inference-time demonstrations to the model.
