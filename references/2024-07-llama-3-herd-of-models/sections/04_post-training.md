# 4 Post-Training [p. 15-16]

[p. 15] The aligned Llama 3 models are produced by applying several rounds of post-training,^6 or aligning the model with human feedback (Ouyang et al., 2022; Rafailov et al., 2024) on top of a pre-trained checkpoint. Each round of post-training involves supervised finetuning (SFT) followed by Direct Preference Optimization (DPO; Rafailov et al., 2024) on examples collected either via human annotations or generated synthetically. The post-training modeling and data approaches are described in Sections 4.1 and 4.2 respectively. Custom data curation strategies to improve the reasoning, coding, factuality, multilingual, tool use, long context, and precise instruction following are further detailed in Section 4.3. [p. 15]

^6 The term "post-training" is used to refer to any model training that happens outside of pre-training.

### Figure 7 [p. 15]

**Figure 7** (p. 15): "Illustration of the overall post-training approach for Llama 3. Our post-training strategy involves rejection sampling, supervised finetuning, and direct preference optimization. See text for details."

The figure shows a flowchart of the post-training pipeline. Starting from "Collected Prompts" at the top, K Generations per Prompt are produced. These feed into Rejection Sampling (guided by a Reward Model), which produces SFT Data. The SFT Data is used to train the SFT Model. The SFT Model then undergoes DPO Training using "Best models from previous rounds" and produces the Final DPO Model. The best model for the next round feeds back. In parallel, "Pairwise Annotated and Specialized Per-Capability Binary Preference Data" feeds into Reward model training, and "Specialized Per-capability SFT data" feeds into DPO Training. The diagram distinguishes Model nodes (blue) from Data nodes (gray).

## 4.1 Modeling [p. 15]

[p. 15] The backbone of the post-training strategy is a reward model and a language model. A reward model is first trained on top of the pre-trained checkpoint using human-annotated preference data (see Section 4.1.2). Then pre-trained checkpoints are finetuned with supervised finetuning (SFT; see Section 4.1.3), and further aligned with Direct Preference Optimization (DPO; see Section 4.1.4). This process is illustrated in Figure 7. Unless otherwise noted, the modeling procedure applies to Llama 3 405B, and Llama 3 405B is referred to as Llama 3 for simplicity. [p. 15]

### 4.1.1 Chat Dialog Format [p. 15-16]

[p. 15-16] To tune LLMs for human-AI interaction, a chat dialog protocol is defined for the model to understand human instructions and perform conversational tasks. Compared to its predecessor, Llama 3 has new capabilities such as tool use (Section 4.3.5) which may require generating multiple messages and sending them to different locations (e.g., user, ipython) within a single dialog turn. To support this, a new multi-message chat protocol is designed which uses various special header and termination tokens. The header tokens are used to indicate the source and destination of each message in a conversation. Similarly, the termination tokens indicate when it is the time to alternate between human and AI to speak. [p. 16]

### 4.1.2 Reward Modeling [p. 16]

[p. 16] A reward model (RM) covering different capabilities is trained on top of the pre-trained checkpoint. The training objective is the same as Llama 2 except that the margin term in the loss is removed, as diminishing improvements after data scaling are observed. Following Llama 2, all preference data is used for reward modeling after filtering out samples with similar responses. In addition to standard preference pair of (chosen, rejected) response, annotations also create a third "edited response" for some prompts, where the chosen response from the pair is further edited for improvement (see Section 4.2.1). Hence, each preference ranking sample has two or three responses with clear ranking (*edited > chosen > rejected*). The prompt and multiple responses are concatenated into a single row during training with responses randomly shuffled. This is an approximation to the standard scenario of putting the responses in separate rows and computing the scores, but in ablations, this approach improves training efficiency without a loss in accuracy. [p. 16]

### 4.1.3 Supervised Finetuning [p. 16]

[p. 16] The reward model is then used to perform rejection sampling on human annotation prompts, the details of which are described in Section 4.2. Together with this rejection-sampled data and other data sources (including synthetic data), the pre-trained language model is finetuned using a standard cross entropy loss on the target tokens (while masking loss on prompt tokens). More details about the data mix can be found in Section 4.2. This stage is referred to as *supervised finetuning* (SFT; Wei et al., 2022a; Sanh et al., 2022; Wang et al., 2022b), even though many of the training targets are model-generated. The largest models are finetuned with a learning rate of 10^-5 over the course of 8.5K to 9K steps. These hyperparameter settings were found to work well across different rounds and data mixes. [p. 16]

### 4.1.4 Direct Preference Optimization [p. 16]

[p. 16] The SFT models are further trained with Direct Preference Optimization (DPO; Rafailov et al., 2024) for human preference alignment. For training, primarily the most recent batches of preference data collected using the best performing models from the previous alignment rounds are used. As a result, the training data conforms better to the distribution of the policy model that is being optimized in each round. On-policy algorithms such as PPO (Schulman et al., 2017) were also explored, but DPO required less compute for large-scale models and performed better, especially on instruction following benchmarks like IFEval (Zhou et al., 2023). For Llama 3, a learning rate of 10^-5 is used and the beta hyper-parameter is set to be 0.1. In addition, the following algorithmic modifications to DPO are applied: [p. 16]

- **Masking out formatting tokens in DPO loss**: Special formatting tokens including header and termination tokens (described in Section 4.1.1) from both chosen and rejected responses are masked out in the loss to stabilize DPO training. Having these tokens contribute to the loss may lead to undesired model behaviors such as tail repetition or abruptly generating termination tokens. The hypothesis is that this is due to the contrastive nature of the DPO loss -- the presence of common tokens in both chosen and rejected responses leads to a conflicting learning objective as the model needs to increase and reduce the likelihood of these tokens simultaneously. [p. 16]

- **Regularization with NLL loss**: An additional negative log-likelihood (NLL) loss term with a scaling coefficient of 0.2 on the chosen sequences is added, similar to Pang et al. (2024). This helps further stabilize DPO training by maintaining desired formatting for generation and preventing the decrease of log probability of chosen responses (Pang et al., 2024; Pal et al., 2024). [p. 16]

### 4.1.5 Model Averaging [p. 16]

[p. 16] Finally, models obtained from experiments using various versions of data or hyperparameters at each RM, SFT, or DPO stage are averaged (Izmailov et al., 2019; Wortsman et al., 2022; Li et al., 2022). [p. 16]

---
[p. 17–21 continued]

### 4.1.6 Iterative Rounds [p. 17]

[p. 17] Following Llama 2, the above methods are applied in six rounds. In each cycle, new preference annotations and SFT data are collected, sampling synthetic data from the latest models.

## 4.2 Post-training Data [p. 17]

[p. 17] The post-training data composition plays a critical role in the usefulness and behavior of language models. This section discusses human annotation procedures and preference data collection (Section 4.2.1), the composition of SFT data (Section 4.2.2), and methods for data quality control and cleaning (Section 4.2.3).

### 4.2.1 Preference Data [p. 17]

[p. 17] The preference data annotation process is similar to Llama 2. Multiple models are deployed for annotation after each round and two responses are sampled from two different models for each user prompt. These models can be trained with different data mixes and alignment recipes, allowing for different capability strength (e.g., code expertise) and increased data diversity. Annotators rate the strength of their preference by categorizing it into one of four levels, based on how much more they prefer the chosen response over the rejected one: significantly better, better, slightly better, or marginally better. An editing step is incorporated after preference ranking to encourage annotators to further improve the preferred response. Annotators edit the chosen response directly or prompt the model with feedback to refine its own response. Consequently, a portion of the preference data has three responses ranked (*edited > chosen > rejected*).

**Table 6** (p. 17): "Statistics of human preference data. We list statistics of the internally collected human preference data used for Llama 3 alignment. We ask annotators to perform multi-turn dialogues with the models and make comparisons among responses at each turn. In post-processing, we split each dialogue to multiple examples at a turn level. Each example consists of a prompt (including previous dialog if available) and a response (e.g., chosen or rejected response)."

| Dataset | % of comparisons | Avg. # turns per dialog | Avg. # tokens per example | Avg. # tokens in prompt | Avg. # tokens in response |
|---|---|---|---|---|---|
| General English | 81.99% | 4.1 | 1,000.4 | 36.4 | 271.2 |
| Coding | 6.93% | 3.2 | 1,621.0 | 113.8 | 462.9 |
| Multilingual | 5.19% | 1.8 | 1,299.4 | 77.1 | 420.9 |
| Reasoning and tools | 5.89% | 1.6 | 707.7 | 46.6 | 129.9 |
| Total | 100% | 3.8 | 1,041.6 | 44.5 | 284.0 |

[p. 17] General English covers multiple subcategories such as knowledge-based question and answering or precise instruction-following, which fall outside the scope of specific capabilities. Compared to Llama 2, an increase in the average length of prompt and response is observed, suggesting that Llama 3 is trained on more complex tasks. A quality analysis and human evaluation process is implemented to rigorously assess the data collected, allowing refinement of prompts and providing systematic, actionable feedback to annotators. As Llama 3 improves after each round, prompt complexity is increased accordingly to target areas where the model lags.

[p. 17] In each round of post-training, all the preference data that is available at the time is used for reward modeling, while only using the latest batches from various capabilities for DPO training. For both reward modeling and DPO, samples that are labeled as the chosen response being significantly better or better than the rejected counterpart are used for training, and samples with similar responses are discarded.

### 4.2.2 SFT Data [p. 17–18]

[p. 17–18] The finetuning data is largely comprised of the following sources:

- Prompts from human annotation collection with rejection-sampled responses.
- Synthetic data targeting specific capabilities (see Section 4.3 for more details).
- Small amounts of human-curated data (see Section 4.3 for more details).

**Table 7** (p. 18): "Statistics of SFT data. We list internally collected SFT data used for Llama 3 alignment. Each SFT example consists of a context (i.e., all conversation turns except the last one) and a final response."

| Dataset | % of examples | Avg. # turns | Avg. # tokens | Avg. # tokens in context | Avg. # tokens in final response |
|---|---|---|---|---|---|
| General English | 52.66% | 6.3 | 974.0 | 656.7 | 317.1 |
| Code | 14.89% | 2.7 | 753.3 | 378.8 | 374.5 |
| Multilingual | 3.01% | 2.7 | 520.5 | 230.8 | 289.7 |
| Exam-like | 8.14% | 2.3 | 297.8 | 124.4 | 173.4 |
| Reasoning and tools | 21.19% | 3.1 | 661.6 | 359.8 | 301.9 |
| Long context | 0.11% | 6.7 | 38,135.6 | 37,395.2 | 740.5 |
| Total | 100% | 4.7 | 846.1 | 535.7 | 310.4 |

[p. 18] As post-training rounds progress, stronger Llama 3 variants are developed that are used to collect larger datasets that cover a wide range of complex capabilities. The section discusses the details for the rejection-sampling procedure and overall composition of the final SFT datamix.

**Rejection sampling.** [p. 18] During rejection sampling (RS), for each prompt collected during human annotation (Section 4.2.1), K outputs (typically between 10 and 30) are sampled from the latest chat model policy (usually the best performing checkpoint from the previous post-training iteration, or the best performing checkpoint for a particular capability) and the reward model is used to select the best candidate, consistent with Bai et al. (2022). In later rounds of post-training, system prompts are introduced to steer RS responses to conform with desirable tone, style, or formatting, which might be different for different capabilities.

[p. 18] To increase the efficiency of rejection sampling, PagedAttention (Kwon et al., 2023) is adopted. PagedAttention enhances memory efficiency through dynamic key-value cache allocation. It supports arbitrary output lengths by dynamically scheduling requests based on the current cache capacity. Unfortunately, this carries the risk of swap-out when running out of memory. To eliminate such swap overhead, a maximum output length is defined and a request is performed only if sufficient memory is available to fit an output with that length. PagedAttention also enables sharing the key-value cache pages for a prompt across all corresponding outputs. Together, this leads to a throughput improvement of over 2x during rejection sampling.

**Overall data composition.** [p. 18] Table 7 shows data statistics for each broad category of the "helpfulness" mix. While SFT and preference data contain overlapping domains, they are curated differently, yielding distinct count statistics. In Section 4.2.3 techniques for categorizing topic, complexity, and quality of data samples are described. In each round of post-training, the overall data mix is adjusted carefully across these axes to tune performance across a wide range of benchmarks. The final data mix epochs multiple times on some high quality sources and downsamples others.

### 4.2.3 Data Processing and Quality Control [p. 18–19]

[p. 18] Given that most of the training data is *model-generated*, it requires careful cleaning and quality control.

**Data cleaning.** [p. 18] In the early rounds, a number of undesirable patterns common in the data are observed, such as excessive use of emojis or exclamation points. A series of rule-based data removal and modification strategies are implemented to filter or clean problematic data. For example, to mitigate overly-apologetic tonal issues, overused phrases (such as "I'm sorry" or "I apologize") are identified and the proportion of such samples in the dataset is carefully balanced.

**Data pruning.** [p. 18–19] A collection of model-based techniques are also applied to remove low-quality training samples and improve overall model performance:

- **Topic classification:** Llama 3 8B is first finetuned into a topic classifier, and inference is performed over all data to classify it into both coarsely-grained buckets ("mathematical reasoning") and fine-grained buckets ("geometry and trigonometry"). [p. 18–19]

- **Quality scoring:** Both reward model and Llama-based signals are used to obtain a quality score for each sample. For an RM-based score, data that is in the top quartile of RM scores is considered as high quality. For a Llama-based score, a Llama 3 checkpoint is prompted to rate each sample on a three-point scale for general English data (accuracy, instruction following, and tone/presentation) and a two-point scale for coding data (bug identification and user intention), and samples that obtain the maximum score are considered as high quality. The RM and Llama-based scores have high disagreement rates, and combining these signals yields the best recall on the internal test set. Ultimately, examples that are marked as high quality by the RM *or* the Llama-based filter are selected. [p. 19]

- **Difficulty scoring:** Because prioritizing examples that are more complex for the model is of interest, data is scored using two measures of difficulty: Instag (Lu et al., 2023) and Llama-based scoring. For Instag, Llama 3 70B is prompted to perform intention tagging of SFT prompts, where more intentions implies more complexity. Llama 3 is also prompted to measure the difficulty (Liu et al., 2024c) of dialogs on a three-point scale. [p. 19]

- **Semantic deduplication:** Semantic deduplication is performed (Abbas et al., 2023; Liu et al., 2024c). Complete dialogs are first clustered using RoBERTa (Liu et al., 2019b) and within each cluster they are sorted by quality score x difficulty score. Greedy selection is then performed by iterating through all sorted examples, and only keeping the ones that have maximum cosine similarity less than a threshold to the examples seen so far in the cluster. [p. 19]

## 4.3 Capabilities [p. 19]

[p. 19] Special efforts to improve performance for specific capabilities are highlighted: code (Section 4.3.1), multilinguality (Section 4.3.2), math and reasoning (Section 4.3.3), long context (Section 4.3.4), tool use (Section 4.3.5), factuality (Section 4.3.6), and steerability (Section 4.3.7).

### 4.3.1 Code [p. 19–21]

[p. 19] LLMs for code have received significant attention since the release of Copilot and Codex (Chen et al., 2021). Developers are now widely using these models to generate code snippets, debug, automate tasks, and improve code quality. For Llama 3, the target is improving and evaluating code generation, documentation, debugging, and review capabilities for the following high priority programming languages: Python, Java, Javascript, C/C++, Typescript, Rust, PHP, HTML/CSS, SQL, bash/shell. The work is presented on improving these coding capabilities via training a code expert, generating synthetic data for SFT, improving formatting with system prompt steering, and creating quality filters to remove bad samples from training data.

**Expert training.** [p. 19] A **code expert** is trained which is used to collect high quality human annotations for code throughout subsequent rounds of post-training. This is accomplished by branching the main pre-training run and continuing pre-training on a 1T token mix of mostly (>85%) code data. Continued pre-training on domain-specific data has been shown to be effective for improving performance in a specific domain (Gururangan et al., 2020). A recipe similar to that of CodeLlama (Roziere et al., 2023) is followed. For the last several thousand steps of training, long-context finetuning (LCFT) is performed to extend the expert's context length to 16K tokens on a high quality mix of repo-level code data. The similar post-training modeling recipes described in Section 4.1 are then followed to align this model, except with SFT and DPO data mixes primarily targeting code. This model is also used for rejection sampling (Section 4.2.2) for coding prompts.

**Synthetic data generation.** [p. 19–20] During development, key issues in code generation were identified, including difficulty in following instructions, code syntax errors, incorrect code generation, and difficulty in fixing bugs. While intensive human annotation could theoretically resolve these issues, synthetic data generation offers a complementary approach at a lower cost and higher scale, unconstrained by the expertise level of annotators. Llama 3 and the code expert are used to generate a large quantity of synthetic SFT dialogs. Three high-level approaches for generating synthetic code data are described. In total, over 2.7M synthetic examples which were used during SFT are generated.

1. **Synthetic data generation: execution feedback.** [p. 20] The 8B and 70B models show significant performance improvements when trained on data generated by a larger, more competent model. However, initial experiments revealed that training Llama 3 405B on its own generated data is not helpful (and can even degrade performance). To address this limitation, execution feedback is introduced as a source of truth, enabling the model to learn from its mistakes and stay on track. A large dataset of approximately one million synthetic coding dialogues is generated using the following process:

   - **Problem description generation:** A large collection of programming problem descriptions is generated that span a diverse range of topics, including those in the long tail distribution. To achieve this diversity, random code snippets from various sources are sampled and the model is prompted to generate programming problems inspired by these examples. This allows tapping into a wide range of topics and creating a comprehensive set of problem descriptions (Wei et al., 2024).
   - **Solution generation:** Llama 3 is prompted to solve each problem in a given programming language. Adding general rules of good programming to the prompt improves the generated solution quality. It is also found helpful to require the model to explain its thought process in comments.
   - **Correctness analysis:** After generating a solution, it is crucial to recognize that its correctness is not guaranteed, and including incorrect solutions in the finetuning dataset could harm the model's quality. While complete correctness is not ensured, methods to approximate it are developed. The source code is extracted from the generated solution and a combination of static and dynamic analysis techniques are applied to test its correctness, including:
     - **Static analysis**: All generated code is run through a parser and a linter to ensure syntactic correctness, catching errors such as syntax errors, use of uninitialized variables or non-imported functions, code style issues, typing errors, and others.
     - **Unit test generation and execution**: For each problem and solution, the model is prompted to generate unit tests, executed in a containerized environment together with the solution, catching run-time execution errors and some semantic errors.
   - **Error feedback and iterative self-correction:** When a solution fails at any step, the model is prompted to revise it. The prompt includes the original problem description, the faulty solution, and feedback from the parser/linter/tester (stdout, stderr/ and return code). After a unit test execution failure, the model could either fix the code to pass the existing tests or modify its unit tests to accommodate the generated code. Only dialogs that pass all checks are included in the final dataset, used for supervised finetuning (SFT). Notably, about 20% of solutions were initially incorrect but self-corrected, indicating that the model learned from the execution feedback and improved its performance. [p. 20]
   - **Fine-tuning and iterative improvement:** The finetuning process is conducted over multiple rounds, with each round building on the previous one. After each round, the model is improved, generating higher-quality synthetic data for the next round. This iterative process allows for progressive refinement and enhancement of the model's performance. [p. 20]

2. **Synthetic data generation: programming language translation.** [p. 20] A performance gap between major programming languages (e.g., Python/C++) and less common ones (e.g., Typescript/PHP) is observed. This is not surprising as there is less training data for less common programming languages. To mitigate this, existing data is supplemented by *translating* data from common programming languages to less common languages (similar to Chen et al. (2023) in the context of reasoning). This is achieved by prompting Llama 3 and ensuring quality via syntax parsing, compilation, and execution. Figure 8 demonstrates an example of synthetic PHP code translated from Python. This improves performance significantly for less common languages as measured by the MultiPL-E (Cassano et al., 2023) benchmark. [p. 20]

3. **Synthetic data generation: backtranslation.** [p. 20–21] To improve certain coding capabilities (e.g., documentation, explanations) where execution feedback is less informative for determining quality, an alternative multi-step approach is employed. Using this procedure, approximately 1.2M synthetic dialogs related to code explanation, generation, documentation, and debugging are generated. Beginning with code snippets from a variety of languages in the pre-training data:
   - **Generate:** Llama 3 is prompted to generate data that represents the target capability (e.g., adding comments and docstrings for the code snippet, or asking the model to explain a piece of code).
   - **Backtranslate:** The model is then prompted to "backtranslate" the synthetically generated data to the original code (e.g., prompting the model to generate code only from its documentation, or asking the model to generate code only from its explanation).
   - **Filter:** Using the original code as a reference, the Llama 3 is prompted to determine the quality of the output (e.g., asking the model how faithful the backtranslated code is to the original). The generated examples that have the highest self-verification scores in SFT are then used. [p. 21]

**System prompt steering during rejection sampling.** [p. 21] During the rejection sampling process, code specific system prompts are used to improve code readability, documentation, thoroughness, and specificity. Recall, from Section 7 this data is used to finetune the language model. Figure 9 shows an example of how the system prompt helps improve the generated code quality -- it adds necessary comments, uses more informative variable names, saves memory, etc. [p. 21]

**Filtering training data with execution and model-as-judge signals.** [p. 21–22] As described in Section 4.2.3, quality issues are occasionally encountered in rejection-sampled data, such as code blocks containing bugs. Detecting these issues in rejection-sampled data is not as straightforward as it is for synthetic code data, as the rejection-sampled responses typically contain a mix of natural language and code for which the code may not always be expected to be executable. (For example, user prompts may explicitly ask for pseudo-code or edits to only a very small snippet of an executable program.) To address this, the "model-as-judge" approach is utilized, where earlier versions of Llama 3 assess and assign a binary (0/1) score based on two criteria: code correctness and code style. Only those samples that achieve a perfect score of 2 are retained. Initially, this stringent filtering led to a regression in downstream benchmark performance, primarily because it disproportionately removed examples with challenging prompts. To counteract this, the responses of some coding data categorized as most challenging are strategically revised until they met the Llama-based "model-as-judge" criteria. By refining these challenging problems, the coding data achieves a balance between quality and difficulty, resulting in optimal downstream performance. [p. 22]

### Figure 8 [p. 21]

**Figure 8** (p. 21): "Code translation example. We display an example of using Llama 3 to translate Python code (left) to PHP code (right) to augment our SFT dataset with a wider range of programming languages."

The figure shows two code panels side by side. The left panel contains Python code defining a function `gushti_cdi()` that reads input, processes an array by finding zero elements and their maximum-valued predecessors, accumulates points, and prints results. The right panel shows the equivalent PHP code translation of the same algorithm, using PHP syntax (`$arr`, `fgets(STDIN)`, `array_slice`, `array_search`, etc.).

### Figure 9 [p. 21]

**Figure 9** (p. 21): "Improving generated code quality with system prompts. Left: without system prompt Right: with system prompt."

The figure shows two Java code panels side by side, both implementing a `ClimbStairs(int n)` function. The left panel (without system prompt) uses a straightforward dynamic programming approach with an array (`dp`), includes base cases for `n == 1` and `n == 2`, and returns `dp[n]`. The right panel (with system prompt) shows an improved version with added comments explaining each step ("// Base cases", "// Initialize variables to store the number of ways to climb", "// Calculate the number of ways to climb for n > 2"), uses space-optimized variables (`prev` and `curr`) instead of an array, and returns `curr`. The system prompt version demonstrates better code quality: more comments, more informative variable names, and improved memory efficiency.

---
[p. 22–26 continued]

### 4.3.2 Multilinguality [p. 22–23]

[p. 22] This section describes how Llama 3's multilingual capabilities are improved, including training an expert specialized on substantially more multilingual data, sourcing and generating high quality multilingual instruction tuning data for German, French, Italian, Portuguese, Hindi, Spanish, and Thai, and tackling specific challenges of multilingual language steering to enhance the overall performance of the model.

**Expert training.** [p. 22] The Llama 3 pre-training data mix contains significantly more English tokens than non-English tokens. To collect higher quality human annotations in non-English languages, a **multilingual expert** is trained by branching off the pre-training run and continuing to pre-train on a data mix that consists of 90% multilingual tokens. Post-training is then performed on this expert following Section 4.1. This expert model is then used to collect higher quality annotations in non-English languages until pre-training was fully complete.

**Multilingual data collection.** [p. 22] The multilingual SFT data is derived primarily from sources described below. The overall distribution is 2.4% human annotations, 44.2% data from other NLP tasks, 18.8% rejection sampled data, and 34.6% translated reasoning data.

- **Human annotations**: High-quality, manually annotated data is collected from linguists and native speakers. These annotations mostly consist of open-ended prompts that represent real world use cases.

- **Data from other NLP tasks**: Multilingual training data from other tasks is used and rewritten into dialog format. For example, data from exams-qa (Hardalov et al., 2020) and Conic10k (Wu et al., 2023) is used. To improve language alignment, parallel texts from GlobalVoices (Prokopidis et al., 2016) and Wikimedia (Tiedemann, 2012) are also used. LID based filtering and Blaser2.0 (Seamless Communication et al., 2023) are used to remove low quality data. For parallel text data, instead of using the bitext pairs directly, a multilingual template inspired by Wei et al. (2022a) is applied to better simulate real-life conversations in translation and language learning scenarios.

- **Rejection sampled data**: Rejection sampling is applied on human annotated prompts to generate high-quality samples for finetuning, with few modifications compared to the process for English data:
  - **Generation**: Randomly choosing the temperature hyperparameter from the range 0.2–1 for diverse generations in early rounds of post-training is explored. With high temperature, responses for multilingual prompts can get creative and inspiring, but are also susceptible to unnecessary or unnatural code-switching. In the final round of post-training, a constant value of 0.6 is used to balance the trade-off. Additionally, specialized system prompts are used to improve response format, structure and general readability.
  - **Selection**: Prior to reward model based selection, multilingual-specific checks are implemented to ensure high language-match rate between the prompt and response (e.g., a romanized Hindi prompt should not expect a response in Hindi Devanagari script).

- **Translated data**: Machine-translated data is avoided to finetune the model in order to prevent translationese (Bizzoni et al., 2020; Muennighoff et al., 2023) or possible name bias (Wang et al., 2022a), gender bias (Savoldi et al., 2021), or cultural bias (Ji et al., 2023). Moreover, the aim is to prevent the model from being exposed only to tasks that are rooted in English cultural context, which may not be representative of the linguistic and cultural diversity targeted. One exception is made: synthetic quantitative reasoning data is translated (see Section 4.3.3 for details) to improve performance in quantitative reasoning in non-English languages. Due to the simple nature of the language in these math problems, the translated samples were found to have little to no quality issues. Strong gains on MGSM (Shi et al., 2022) are observed from adding this translated data. [p. 22–23]

### 4.3.3 Math and Reasoning [p. 23–24]

[p. 23] Reasoning is defined as the ability to perform multi-step computations and arrive at the correct final answer. Several challenges guide the approach to training models that excel in mathematical reasoning:

- **Lack of prompts**: As the complexity of questions increases, the number of valid prompts or questions for Supervised Fine-Tuning (SFT) decreases. This scarcity makes it difficult to create diverse and representative training datasets for teaching models various mathematical skills (Yu et al., 2023; Yue et al., 2023; Luo et al., 2023; Mitra et al., 2024; Shao et al., 2024; Yue et al., 2024b).

- **Lack of ground truth chain of thought**: Effective reasoning requires a step-by-step solution to facilitate the reasoning process (Wei et al., 2022c). However, there is often a shortage of ground truth chains of thought, which are essential for guiding the model how to break down the problem step-by-step and reach the final answer (Zelikman et al., 2022).

- **Incorrect intermediate steps**: When using model-generated chains of thought, the intermediate steps may not always be correct (Cobbe et al., 2021; Uesato et al., 2022; Lightman et al., 2023; Wang et al., 2023a). This inaccuracy can lead to incorrect final answers and needs to be addressed.

- **Teaching models to use external tools**: Enhancing models to utilize external tools, such as code interpreters, allows them to reason by interleaving code and text (Gao et al., 2023; Chen et al., 2022; Gou et al., 2023). This capability can significantly improve their problem-solving abilities.

- **Discrepancy between training and inference**: There is often a discrepancy between how the model is finetuned during training and how it is used during inference. During inference, the finetuned model may interact with humans or other models, requiring it to improve its reasoning using feedback. Ensuring consistency between training and real-world usage is crucial for maintaining reasoning performance.

[p. 23] To address these challenges, the following methodologies are applied:

- **Addressing the lack of prompts**: Relevant pre-training data from mathematical contexts is sourced and converted into a question-answer format which can then be used for supervised finetuning. Additionally, mathematical skills where the model under-performs are identified and prompts are actively sourced from humans to teach models such skills. To facilitate this process, a taxonomy of mathematical skills is created (Didolkar et al., 2024) and humans are asked to provide relevant prompts/questions accordingly.

- **Augmenting training data with step-wise reasoning traces**: Llama 3 is used to generate step-by-step solutions for a set of prompts. For each prompt, the model produces a variable number of generations. These generations are then filtered based on the correct answer (Li et al., 2024a). Self-verification is also performed where Llama 3 is used to verify whether a particular step-by-step solution is valid for a given question. This process improves the quality of the finetuning data by eliminating instances where the model does not produce valid reasoning traces.

- **Filtering incorrect reasoning traces**: Outcome and stepwise reward models are trained (Lightman et al., 2023; Wang et al., 2023a) to filter training data where the intermediate reasoning steps were incorrect. These reward models are used to eliminate data with invalid step-by-step reasoning, ensuring high-quality data for finetuning. For more challenging prompts, Monte Carlo Tree Search (MCTS) with learned step-wise reward models is used to generate valid reasoning traces, further enhancing the collection of high-quality reasoning data (Xie et al., 2024). [p. 23]

- **Interleaving code and text reasoning**: Llama 3 is prompted to solve reasoning problems through a combination of textual reasoning and associated Python code (Gou et al., 2023). Code execution is used as a feedback signal to eliminate cases where the reasoning chain was not valid, ensuring the correctness of the reasoning process. [p. 23]

- **Learning from feedback and mistakes**: To simulate human feedback, incorrect generations (i.e., generations leading to incorrect reasoning traces) are utilized and error correction is performed by prompting Llama 3 to yield correct generations (An et al., 2023b; Welleck et al., 2022; Madaan et al., 2024a). The iterative process of using feedback from incorrect attempts and correcting them helps improve the model's ability to reason accurately and learn from its mistakes. [p. 23–24]

### 4.3.4 Long Context [p. 24]

[p. 24] During the final pre-training stage, the context length of Llama 3 is extended from 8K tokens to 128K tokens (see Section 3.4 for more details). Similar to pre-training, during finetuning the recipe must be carefully tuned to balance short and long-context capabilities.

**SFT and synthetic data generation.** [p. 24] Naively applying the existing SFT recipe with only short-context data resulted in significant regressions in long-context capabilities from pre-training, highlighting the need to incorporate long-context data in the SFT data mix. In practice, however, it is largely impractical to get humans to annotate such examples due to the tedious and time-consuming nature of reading lengthy contexts, so the approach predominantly relies on synthetic data to fill this gap. Earlier versions of Llama 3 are used to generate synthetic data based on the key long-context use-cases: (possibly multi-turn) question-answering, summarization for long documents, and reasoning over code repositories, described in greater detail below.

- **Question answering:** A set of long documents from the pre-training mix is carefully curated. These documents are split into chunks of 8K tokens, and an earlier version of the Llama 3 model is prompted to generate QA pairs conditional on randomly selected chunks. During training, the whole document is used as context.

- **Summarization:** Hierarchical summarization of long-context documents is applied by first summarizing the chunks of 8K input length using the strongest Llama 3 8K context model and then summarizing the summaries. During training the full document is provided and the model is prompted to summarize the document while preserving all the important details. QA pairs based on the summaries of the documents are also generated and the model is prompted with questions that require global understanding of the whole long document.

- **Long context code reasoning:** Python files are parsed to identify `import` statements and determine their dependencies. The most commonly depended-upon files are selected, specifically those referenced by at least five other files. One of these key files is removed from a repository and the model is prompted to identify which files depended on the missing file and to generate the necessary missing code.

[p. 24] These synthetically generated samples are further categorized based on the sequence length (16K, 32K, 64K and 128K) to enable more fine-grained targeting of input lengths.

[p. 24] Through careful ablations, mixing 0.1% of synthetically generated long-context data with the original short-context data is observed to optimize performance across both short-context and long-context benchmarks.

**DPO.** [p. 24] Using only short context training data in DPO did not negatively impact long-context performance as long as the SFT model is high quality in long context tasks. This is suspected to be due to the fact that the DPO recipe has fewer optimizer steps than SFT. Given this finding, the standard short-context recipe for DPO is kept on top of the long-context SFT checkpoints.

### 4.3.5 Tool Use [p. 24–26]

[p. 24] Teaching LLMs to use tools such as search engines or code interpreters hugely expands the range of tasks they can solve, transforming them from pure chat models into more general assistants (Nakano et al., 2021; Thoppilan et al., 2022; Parisi et al., 2022; Gao et al., 2023; Mialon et al., 2023a; Schick et al., 2024). Llama 3 is trained to interact with the following tools:

- **Search engine.** Llama 3 is trained to use Brave Search^7 to answer questions about recent events that go beyond its knowledge cutoff or that require retrieving a particular piece of information from the web.

- **Python interpreter.** Llama 3 can generate and execute code to perform complex computations, read files uploaded by the user and solve tasks based on them such as question answering, summarization, data analysis or visualization.

- **Mathematical computational engine.** Llama 3 can use the Wolfram Alpha API^8 to more accurately solve math, science problems, or retrieve accurate information from Wolfram's database.

^7 https://brave.com/search/api/
^8 https://products.wolframalpha.com/llm-api/documentation

[p. 25] The resulting model is able to use these tools in a chat setup to solve the user's queries, including in multi-turn dialogs. If a query requires multiple tool calls, the model can write a step-by-step plan, call the tools in sequence, and do reasoning after each tool call.

[p. 25] Llama 3's zero-shot tool use capabilities are also improved -- given in-context, potentially unseen tool definitions and a user query, the model is trained to generate the correct tool call.

**Implementation.** [p. 25] Core tools are implemented as Python objects with different methods. Zero-shot tools can be implemented as Python functions with descriptions, documentation (i.e., examples for how to use them), and the model only needs the function's signature and docstring as context to generate the appropriate call. Function definitions and calls are also converted to JSON format, e.g., for web API calls. All tool calls are executed by the Python interpreter, that must be enabled in the Llama 3 system prompt. Core tools can be individually enabled or disabled in the system prompt.

**Data collection.** [p. 25] Different from Schick et al. (2024), human annotations and preferences are relied on to teach Llama 3 to use tools. There are two main differences with the post-training pipeline generally used in Llama 3:

- For tools, dialogs often contain more than a single assistant message (e.g., calling the tool and reasoning about the tool output). Thus, annotation is performed at the message level to collect granular feedback: annotators provide a preference between two assistant messages with the same context or, if both contain major problems, edit one of the messages. The chosen or edited message is then added to the context and the dialog continues. This provides human feedback for both the assistant's ability of calling the tools and reasoning about the tool outputs. Annotators cannot rank or edit the tool outputs.

- Rejection sampling is not performed, as no gains were observed in tool benchmarks.

[p. 25] To accelerate the annotation process, basic tool use capabilities are bootstrapped by finetuning on synthetically generated data from previous Llama 3 checkpoints. Thus, annotators have fewer edits to perform. In a similar spirit, as Llama 3 gradually improves through its development, human annotation protocols are progressively complexified: starting by single-turn tool use annotations, before moving to tool use in dialogs, and finally annotating for multi-step tool use and data analysis.

**Tool datasets.** [p. 25] To create data for tool usage applications, the following procedure is leveraged:

- **Single-step tool use:** Starting by few-shot generation of synthetic user prompts which, by construction, require a call to one of the core tools (for example, questions that exceed the knowledge cutoff date). Then, still relying on few-shot generation, appropriate tool calls are generated for these prompts, executed, and the output is added to the model's context. Finally, the model is prompted again to generate a final answer to the user's query based on the tool output. The resulting trajectories have the following form: system prompt, user prompt, tool call, tool output, final answer. Around 30% of this dataset is also filtered to remove tool calls that cannot be executed or other formatting issues.

- **Multi-step tool use:** A similar protocol is followed, first generating synthetic data to teach the model basic multi-step tool use capabilities. To do this, Llama 3 is first prompted to generate user prompts that require at least two tool calls, that can be the same or different tools from the core tool set. Then, conditioned on these prompts, Llama 3 is few-shot prompted to generate a solution consisting of interleaved reasoning steps and tool calls, similar to ReAct (Yao et al., 2022). See Figure 10 for an example of Llama 3 performing a task involving multi-step tool usage.

- **File uploads:** Annotation is performed for the following filetypes: .TXT, .DOCX, .PDF, .PPTX, .XLSX, .CSV, .TSV, .PY, .JSON, .JSONL, .HTML, .XML. Prompts are based on a provided file, and ask to summarize the contents of the file, find and fix bugs, optimize a piece of code, perform data analysis or visualization. See Figure 11 for an example of Llama 3 performing a task involving a file upload.

[p. 25–26] After finetuning on this synthetic data, human annotations are gathered in diverse and challenging scenarios including multi-turn interactions, more than three step tool use, and instances where a tool call does not yield a satisfying answer. Synthetic data is augmented with different system prompts to teach the model to use tools only when activated. To train the model to avoid calling tools for simple queries, queries from easy math or question answering datasets (Berant et al., 2013; Koncel-Kedziorski et al., 2016; Joshi et al., 2017; Amini et al., 2019) and their responses without tools, but with tools activated in system prompt, are also added.

**Zero-shot tool use data.** [p. 26] Llama 3 zero-shot tool use abilities (also referred to as function calling) are improved by finetuning on a large and diverse set of partly synthetic (functions definitions, user query, corresponding call) tuples. The model is evaluated on a set of unseen tools.

- **Single, nested, and parallel function calling:** Calls can be simple, nested, i.e. a function call is passed as an argument of another function, or parallel, i.e. the model returns a list of independent function calls. Generating a diverse set of functions, queries and ground truths can be challenging (Mekala et al., 2024), and mining the Stack (Kocetkov et al., 2022) is resorted to in order to ground synthetic user queries in real functions. More precisely, function calls and their definitions are extracted, cleaned and filtered, e.g. for missing docstrings or non-executable functions, and Llama 3 is used to generate a natural language query corresponding to the function call.

- **Multi-turn function calling:** Synthetic data for multi-turn dialogs with function calls is also generated, following a protocol similar to the one proposed in Li et al. (2023b). Multiple agents are used that generate domains, APIs, user queries, API calls, and responses, while also ensuring that the generated data covers a set of diverse domains and realistic APIs. All agents are variants of Llama 3 prompted in different ways depending on their roles and collaborate in a step-by-step manner. [p. 26]

### Figure 10 [p. 26]

**Figure 10** (p. 26): "Multi-step tool usage. Example of Llama 3 performing multi-step planning, reasoning, and tool calling to solve a task."

The figure shows a multi-step interaction. A user prompt asks about the inflation rate for the US in February 2024, the cost of a list of grocery tuples, and to estimate total grocery cost over a 30-day month with an added daily cookie from Costco's food court, adjusting for inflation. The system prompt shows the environment is ipython with tools: brave_search, wolfram_alpha, and a cutting knowledge date of December 2023. The assistant response shows a step-by-step plan: (1) look up the inflation rate, (2) look up the Costco cookie price, (3) calculate estimated total cost, (4) adjust for inflation. The assistant makes a `brave_search` call for "US inflation rate February 2024" which returns a tool output about 3.2% inflation. Next, the assistant makes another `brave_search` call for "Costco food court giant cookie debut price" which returns information about a giant cookie costing $1.49. The assistant then uses the Python interpreter to calculate the total cost: computing the daily grocery cost, adding the cookie, multiplying for 30 days, and adjusting for the 3.2% inflation rate. The final answer is that the estimated total cost of groceries over a 30 day month with one daily Costco cookie, adjusted for inflation, is $626.63.

### Figure 11 [p. 27]

**Figure 11** (p. 27): "Processing file uploads. Example of Llama 3 performing analysis and visualization of an uploaded file."

The figure shows a multi-step interaction. A user prompt asks about the relationship between a cereal's sugar content and its overall rating, and to visualize the relationship and provide a way to estimate a cereal's rating based on its sugar content. The file path is `/tmp/data/cereal.csv`. The system prompt shows environment is ipython with tools: brave_search, wolfram_alpha, and cutting knowledge date December 2023. The assistant makes two tool calls: (1) loading the CSV using pandas, exploring shape, columns, dtypes, and printing a sample; (2) plotting the relationship between sugar content and rating using matplotlib, performing linear regression using `sklearn.linear_model.LinearRegression`, and printing the coefficient of determination (R^2), coefficient of sugar content, and intercept. The tool output shows: R^2 = 0.577, coefficient of sugar content = -2.400, intercept = 59.284. A scatter plot with regression line is displayed showing a negative relationship. The final answer explains that the relationship between sugar content and rating is negative (as sugar content increases, rating decreases), R^2 is 0.577 indicating 57.7% of variation in rating is explained by sugar content, the coefficient is -2.400 (for every unit increase in sugar content, rating decreases by 2.400 units), and the intercept is 59.284 (when sugar content is 0, rating is 59.284).

### 4.3.6 Factuality [p. 26–27]

[p. 26] Hallucinations remain a major challenge for large language models. Models tend to be overconfident, even in domains where they have little knowledge. Despite these shortcomings, they are often used as knowledge bases, which can lead to risky outcomes such as the spread of misinformation. While it is recognized that factuality can go beyond hallucinations, a hallucination-first approach is taken here.

[p. 27] The principle that post-training should align the model to "know what it knows" rather than add knowledge (Gekhman et al., 2024; Mielke et al., 2020) is followed. The primary approach involves generating data that aligns model generations with subsets of factual data present in the pre-training data. To achieve this, a knowledge probing technique is developed that takes advantage of Llama 3's in-context abilities. This data generation process involves the following procedure:

1. **Extract a data snippet** from the pre-training data.
2. **Generate a factual question** about these snippets (context) by prompting Llama 3.
3. **Sample responses** from Llama 3 to the question.
4. **Score the correctness** of the generations using the original context as a reference and Llama 3 as a judge.
5. **Score the informativeness** of the generations using Llama 3 as a judge.
6. **Generate a refusal** for responses which are consistently informative and incorrect across the generations, using Llama 3.

[p. 27] Data generated from the knowledge probe is used to encourage the model to only answer questions which it has knowledge about, and refuse answering those questions that it is unsure about. Further, pre-training data is not always factually consistent or correct. Therefore a limited set of labeled factuality data that deals with sensitive topics where factually contradictory or incorrect statements are prevalent is also collected.

### 4.3.7 Steerability [p. 28]

[p. 28] Steerability is the ability to direct the model's actions and outcomes to meet developer and user specifications. As Llama 3 is a generic foundational model, it should be maximally steerable to different downstream use cases. For Llama 3, the focus is on enhancing steerability through system prompt with natural language instructions, especially around response length, format, tone and character/persona.

**Data collection.** [p. 28] Steerability preference samples are collected within the general English category by asking annotators to design different system prompts for Llama 3. Annotators then engage in conversations with the models to evaluate their consistency in following instructions defined in system prompts over the course of the conversation. An example customized system prompt used for enhancing steerability is shown:

> "You are a helpful and cheerful AI Chatbot that acts as a meal plan assistant for busy families. The family consists of 2 adults, 3 teenagers, and 2 preschoolers. Plan two or three days at a time and use leftovers or extra ingredients for the second day's plan. The user will let you know if they want two or three days. If they don't, assume three days. Each plan should include breakfast, lunch, snack, and dinner. Ask the user if they approve of the plan or need adjustments. After they approve provide a grocery list with family size in mind. Always keep family preferences in mind and if there's something that they don't like provide a substitution. If the user is not feeling inspired then ask them what's the one place they wish they could visit on vacation this week and then suggest meals based on that location's culture. Weekend meals can be more complex. Weekday meals should be quick and easy. For breakfast and lunch, easy food like cereal, English muffins with pre-cooked bacon, and other quick easy foods are preferred. The family is busy. Be sure to ask if they have essentials and favorites on hand like coffee or energy drinks so they don't forget to buy it. Remember to be budget-conscious unless it's a special occasion." [p. 28]

**Modeling.** [p. 28] After collecting the preference data, this data is leveraged in reward modeling, rejection sampling, SFT, and DPO to enhance Llama 3's steerability.
