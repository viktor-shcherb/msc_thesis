# 2. Approach [p. 6-10]

[p. 6] The basic pre-training approach, including model, data, and training, is similar to the process described in [RWC+19], with relatively straightforward scaling up of the model size, dataset size and diversity, and length of training. The use of in-context learning is also similar to [RWC+19], but in this work the authors systematically explore different settings for learning within the context.

The different settings can be seen as lying on a spectrum of how much task-specific data they tend to rely on. Specifically, at least four points on this spectrum are identified (see Figure 2.1 for an illustration):

## Fine-Tuning (FT)

[p. 6] The most common approach in recent years. Involves updating the weights of a pre-trained model by training on a supervised dataset specific to the desired task. Typically thousands to hundreds of thousands of labeled examples are used.
- **Main advantage:** Strong performance on many benchmarks.
- **Main disadvantages:** Need for a new large dataset for every task, the potential for poor generalization out-of-distribution [MPL19], and the potential to exploit spurious features of the training data [GSL+18, NK19], potentially resulting in an unfair comparison with human performance.
- The authors do not fine-tune GPT-3 in this work because their focus is on task-agnostic performance, but note GPT-3 can be fine-tuned in principle and this is a promising direction for future work.

## Few-Shot (FS)

[p. 6] The setting where the model is given a few demonstrations of the task at inference time as conditioning [RWC+19], but no weight updates are allowed. As shown in Figure 2.1, for a typical dataset an example has a context and a desired completion, and few-shot works by giving K examples of context and completion, and then one final example of context, with the model expected to provide the completion. K is typically set in the range of 10 to 100 as this is how many examples can fit in the model's context window (n_ctx = 2048).
- **Main advantages:** Major reduction in the need for task-specific data and reduced potential to learn an overly narrow distribution from a large but narrow fine-tuning dataset.
- **Main disadvantage:** Results from this method have so far been much worse than state-of-the-art fine-tuned models. Also, a small amount of task specific data is still required.
- Few-shot learning as described here for language models is related to few-shot learning as used in other contexts in ML [HYC01, VBL+16] -- both involve learning based on a broad distribution of tasks (in this case implicit in the pre-training data) and then rapidly adapting to a new task.

## One-Shot (1S)

[p. 6] The same as few-shot except that only one demonstration is allowed, in addition to a natural language description of the task (as shown in Figure 1). The reason to distinguish one-shot from few-shot and zero-shot is that it most closely matches the way in which some tasks are communicated to humans. For example, when asking humans to generate a dataset on a human worker service (for example Mechanical Turk), it is common to give one demonstration of the task. By contrast it is sometimes difficult to communicate the content or format of a task if no examples are given.

## Zero-Shot (0S)

[p. 7] The same as one-shot except that no demonstrations are allowed, and the model is only given a natural language instruction describing the task. This method provides maximum convenience, potential for robustness, and avoidance of spurious correlations (unless they occur very broadly across the large corpus of pre-training data), but is also the most challenging setting. In some cases it may even be difficult for humans to understand the format of the task without prior examples, so this setting is in some cases "unfairly hard". For example, if someone is asked to "make a table of world records for the 200m dash", this request can be ambiguous. Nevertheless, for at least some settings zero-shot is closest to how humans perform tasks -- for example, in the translation example in Figure 2.1, a human would likely know what to do from just the text instruction.

## Comparing the evaluation settings

[p. 7] Figure 2.1 shows the four methods using the example of translating English to French. The paper focuses on zero-shot, one-shot and few-shot, with the aim of comparing them not as competing alternatives, but as different problem settings which offer a varying trade-off between performance on specific benchmarks and sample efficiency. The authors especially highlight the few-shot results as many of them are only slightly behind state-of-the-art fine-tuned models. Ultimately, one-shot, or even sometimes zero-shot, seem like the fairest comparisons to human performance, and are important targets for future work.

[p. 7] Sections 2.1-2.3 give details on models, training data, and training process respectively. Section 2.4 discusses the details of how few-shot, one-shot, and zero-shot evaluations are done.

## Figures

**Figure 2.1** (p. 7): "Zero-shot, one-shot and few-shot, contrasted with traditional fine-tuning."
- The panels show four methods for performing a task with a language model. Fine-tuning is the traditional method, whereas zero-, one-, and few-shot (studied in this work) require the model to perform the task with only forward passes at test time.
- Left side shows three in-context learning settings using English-to-French translation: **Zero-shot** provides only a task description ("Translate English to French:") and a prompt ("cheese =>"); **One-shot** adds one example ("sea otter => loutre de mer"); **Few-shot** adds multiple examples ("sea otter => loutre de mer", "peppermint => menthe poivree", "plush giraffe => girafe peluche").
- Right side shows **Fine-tuning** (not used for GPT-3): the model is trained via repeated gradient updates using a large corpus of example tasks.
- Caption notes: "We typically present the model with a few dozen examples in the few shot setting. Exact phrasings for all task descriptions, examples and prompts can be found in Appendix G."

---

## 2.1 Model and Architectures [p. 8]

[p. 8] The authors use the same model and architecture as GPT-2 [RWC+19], including the modified initialization, pre-normalization, and reversible tokenization described therein, with the exception that they use alternating dense and locally banded sparse attention patterns in the layers of the transformer, similar to the Sparse Transformer [CGRS19]. To study the dependence of ML performance on model size, they train 8 different sizes of model, ranging over three orders of magnitude from 125 million parameters to 175 billion parameters, with the last being the model they call GPT-3. Previous work [KMH+20] suggests that with enough training data, scaling of validation loss should be approximately a smooth power law as a function of size; training models of many different sizes allows testing this hypothesis both for validation loss and for downstream language tasks.

[p. 8] Table 2.1 shows the sizes and architectures of the 8 models. Here n_params is the total number of trainable parameters, n_layers is the total number of layers, d_model is the number of units in each bottleneck layer (the feedforward layer is always four times the size of the bottleneck layer, d_ff = 4 * d_model), and d_head is the dimension of each attention head. All models use a context window of n_ctx = 2048 tokens. The model is partitioned across GPUs along both the depth and width dimension to minimize data-transfer between nodes. The precise architectural parameters for each model are chosen based on computational efficiency and load-balancing in the layout of models across GPUs. Previous work [KMH+20] suggests that validation loss is not strongly sensitive to these parameters within a reasonably broad range.

### Table 2.1: Sizes, architectures, and learning hyper-parameters (batch size in tokens and learning rate) of the models which we trained. All models were trained for a total of 300 billion tokens.

| Model Name | n_params | n_layers | d_model | n_heads | d_head | Batch Size | Learning Rate |
|---|---|---|---|---|---|---|---|
| GPT-3 Small | 125M | 12 | 768 | 12 | 64 | 0.5M | 6.0 x 10^-4 |
| GPT-3 Medium | 350M | 24 | 1024 | 16 | 64 | 0.5M | 3.0 x 10^-4 |
| GPT-3 Large | 760M | 24 | 1536 | 16 | 96 | 0.5M | 2.5 x 10^-4 |
| GPT-3 XL | 1.3B | 24 | 2048 | 24 | 128 | 1M | 2.0 x 10^-4 |
| GPT-3 2.7B | 2.7B | 32 | 2560 | 32 | 80 | 1M | 1.6 x 10^-4 |
| GPT-3 6.7B | 6.7B | 32 | 4096 | 32 | 128 | 2M | 1.2 x 10^-4 |
| GPT-3 13B | 13.0B | 40 | 5140 | 40 | 128 | 2M | 1.0 x 10^-4 |
| GPT-3 175B or "GPT-3" | 175.0B | 96 | 12288 | 96 | 128 | 3.2M | 0.6 x 10^-4 |

---

## 2.2 Training Dataset [p. 8-9]

[p. 8] Datasets for language models have rapidly expanded, culminating in the Common Crawl dataset (footnote 2: https://commoncrawl.org/the-data/) [RSR+19] constituting nearly a trillion words. This size of dataset is sufficient to train the largest models without ever updating on the same sequence twice. However, unfiltered or lightly filtered versions of Common Crawl tend to have lower quality than more curated datasets. Therefore, 3 steps were taken to improve the average quality of the datasets:

1. Downloaded and filtered a version of CommonCrawl based on similarity to a range of high-quality reference corpora.
2. Performed fuzzy deduplication at the document level, within and across datasets, to prevent redundancy and preserve the integrity of the held-out validation set as an accurate measure of overfitting.
3. Added known high-quality reference corpora to the training mix to augment CommonCrawl and increase its diversity.

[p. 8] Details of the first two points (processing of Common Crawl) are described in Appendix A. For the third, several curated high-quality datasets were added, including an expanded version of the WebText dataset [RWC+19], collected by scraping links over a longer period of time, and first described in [KMH+20], two internet-based books corpora (Books1 and Books2) and English-language Wikipedia.

[p. 8-9] Table 2.2 shows the final mixture of datasets used in training. The CommonCrawl data was downloaded from 41 shards of monthly CommonCrawl covering 2016 to 2019, constituting 45TB of compressed plaintext before filtering and 570GB after filtering, roughly equivalent to 400 billion byte-pair-encoded tokens. Note that during training, datasets are not sampled in proportion to their size, but rather datasets viewed as higher-quality are sampled more frequently, such that CommonCrawl and Books2 datasets are sampled less than once during training, but the other datasets are sampled 2-3 times. This essentially accepts a small amount of overfitting in exchange for higher quality training data.

### Table 2.2: Datasets used to train GPT-3. "Weight in training mix" refers to the fraction of examples during training that are drawn from a given dataset, which we intentionally do not make proportional to the size of the dataset. As a result, when we train for 300 billion tokens, some datasets are seen up to 3.4 times during training while other datasets are seen less than once.

| Dataset | Quantity (tokens) | Weight in training mix | Epochs elapsed when training for 300B tokens |
|---|---|---|---|
| Common Crawl (filtered) | 410 billion | 60% | 0.44 |
| WebText2 | 19 billion | 22% | 2.9 |
| Books1 | 12 billion | 8% | 1.9 |
| Books2 | 55 billion | 8% | 0.43 |
| Wikipedia | 3 billion | 3% | 3.4 |

[p. 9] A major methodological concern with language models pretrained on a broad swath of internet data, particularly large models with the capacity to memorize vast amounts of content, is potential contamination of downstream tasks by having their test or development sets inadvertently seen during pre-training. To reduce such contamination, the authors searched for and attempted to remove any overlaps with the development and test sets of all benchmarks studied in this paper. Unfortunately, a bug in the filtering caused some overlaps to be ignored, and due to the cost of training it was not feasible to retrain the model. In Section 4 the authors characterize the impact of the remaining overlaps, and in future work will more aggressively remove data contamination.

### Figure 2.2 (p. 9): "Total compute used during training."
- Based on the analysis in Scaling Laws For Neural Language Models [KMH+20], the authors train much larger models on many fewer tokens than is typical.
- Bar chart (log scale y-axis: Training Petaflop/s-days) comparing compute for: BERT-Base, BERT-Large, RoBERTa-Base, RoBERTa-Large (green bars, ~1-10 range), T5-Small, T5-Base, T5-Large, T5-3B, T5-11B (purple bars, ~1-100 range), and GPT-3 Small through GPT-3 175B (blue bars, ~5-5000 range).
- As a consequence, although GPT-3 3B is almost 10x larger than RoBERTa-Large (355M params), both models took roughly 50 petaflop/s-days of compute during pre-training.
- Methodology for these calculations can be found in Appendix D.

---

## 2.3 Training Process [p. 9]

[p. 9] As found in [KMH+20, MKAT18], larger models can typically use a larger batch size, but require a smaller learning rate. The authors measure the gradient noise scale during training and use it to guide the choice of batch size [MKAT18]. Table 2.1 shows the parameter settings used. To train the larger models without running out of memory, a mixture of model parallelism within each matrix multiply and model parallelism across the layers of the network is used. All models were trained on V100 GPUs on part of a high-bandwidth cluster provided by Microsoft. Details of the training process and hyperparameter settings are described in Appendix B.

---

## 2.4 Evaluation [p. 10]

[p. 10] For few-shot learning, each example in the evaluation set is evaluated by randomly drawing K examples from that task's training set as conditioning, delimited by 1 or 2 newlines depending on the task. For LAMBADA and Storycloze there is no supervised training set available so conditioning examples are drawn from the development set and evaluation is on the test set. For Winograd (the original, not SuperGLUE version) there is only one dataset, so conditioning examples are drawn directly from it.

[p. 10] K can be any value from 0 to the maximum amount allowed by the model's context window, which is n_ctx = 2048 for all models and typically fits 10 to 100 examples. Larger values of K are usually but not always better, so when a separate development and test set are available, a few values of K are tried on the development set and the best value is used on the test set. For some tasks (see Appendix G) a natural language prompt is also used in addition to (or for K = 0, instead of) demonstrations.

[p. 10] On tasks that involve choosing one correct completion from several options (multiple choice), K examples of context plus correct completion are provided, followed by one example of context only, and the LM likelihood of each completion is compared. For most tasks the per-token likelihood is compared (to normalize for length), however on a small number of datasets (ARC, OpenBookQA, and RACE) additional benefit is gained as measured on the development set by normalizing by the unconditional probability of each completion, by computing P(completion|context) / P(completion|answer_context), where answer_context is the string "Answer: " or "A: " and is used to prompt that the completion should be an answer but is otherwise generic.

[p. 10] On tasks that involve binary classification, the options are given more semantically meaningful names (e.g. "True" or "False" rather than 0 or 1) and then treated like multiple choice; the task is also sometimes framed similar to what is done by [RSR+19] (see Appendix G for details).

[p. 10] On tasks with free-form completion, beam search is used with the same parameters as [RSR+19]: a beam width of 4 and a length penalty of alpha = 0.6. The model is scored using F1 similarity score, BLEU, or exact match, depending on what is standard for the dataset at hand.

[p. 10] Final results are reported on the test set when publicly available, for each model size and learning setting (zero-, one-, and few-shot). When the test set is private, the model is often too large to fit on the test server, so results are reported on the development set. The authors do submit to the test server on a small number of datasets (SuperGLUE, TriviaQA, PiQa) where submission was possible, and submit only the 200B few-shot results, and report development set results for everything else.
