# Appendix N: BABILong Datasheet [p. 31+]

[p. 31]

We follow recommended Datasheets for Datasets form (Gebru et al., 2021). [p. 31]

## N.1 Motivation [p. 31]

**For what purpose was the dataset created?** The BABILong benchmark is designed to test language models' ability to reason across facts distributed in extremely long documents. BABILong includes a diverse set of 20 reasoning tasks, including fact chaining, simple induction, deduction, counting, and handling lists/sets. Today, large language models (LLMs) and neural architectures are continually evolving and achieving remarkable improvements, particularly in their ability to handle longer contexts, but the benchmarks used to assess this behavior lag behind. For example, current benchmarks such as Longbench (Bai et al., 2023) and L-Eval An et al. (2023) scale only up to 40,000 tokens, while models are capable of handling much longer texts (OpenAI, 2023b; Bulatov et al., 2024; Gu & Dao, 2023; Anthropic, 2024; Reid et al., 2024; Liu et al., 2024a). To bridge this gap, BABILong allows researchers to test models for almost any length, in order to adapt them to the evaluation of new, more powerful models in an extensible and controllable way. [p. 31]

**Who created this dataset (e.g., which team, research group) and on behalf of which entity (e.g., company, institution, organization)?** This work was done in collaboration of AIRI, Neural Networks and Deep Learning Lab at MIPT, and London Institute for Mathematical Sciences. [p. 31]

**What support was needed to make this dataset?** Refer to the acknowledgments section of the main text. [p. 31]

## N.2 Composition [p. 31]

**What do the instances that comprise the dataset represent (e.g., documents, photos, people, countries)?** Each sample is a text document, combined from PG-19 books (Rae et al., 2020) and facts and questions from the bAbI dataset (Weston et al., 2016). The facts are about fictional people, places, animals, and items. PG-19 is a collection of books published before 1919. [p. 31]

**How many instances are there in total (of each type, if appropriate)?** The BABILong dataset is generative, offering an unlimited number of test instances. The released pre-generated version includes 13,000 samples, divided into 13 context length splits across 10 tasks, and is available on Hugging Face: https://huggingface.co/datasets/RMT-team/babilong. An extended version with 60,000 samples, covering five tasks and offering 1,000 samples per split instead of 100, is also available: https://huggingface.co/datasets/RMT-team/babilong-1k-samples. [p. 31]

**Does the dataset contain all possible instances or is it a sample (not necessarily random) of instances from a larger set?** The test set of BABILong combines sentences of books from the PG-19 (Rae et al., 2020) test split with sentences generated from bAbI (Weston et al., 2016) tasks. For evaluation set with 100 samples per task and per length, we randomly sampled 100 test samples from full test set. In train split, we use all train samples from bAbI and randomly sampled texts from PG-19 train split. [p. 31]

**What data does each instance consist of?** Each sample of BABILong dataset consists of unprocessed sentences of bAbI (Weston et al., 2016) sample (including facts, distractor facts and question) mixed between unprocessed sentences of PG-19 (Rae et al., 2020). The question can be added to either the beginning or the end of the resulting text sequence. See Figure 1a from the main text that illustrates composition of samples in BABILong. [p. 31]

---
[p. 32 continued]

**Is there a label or target associated with each instance?** Yes, each sample in the BABILong dataset is assigned a label, which is the answer to the corresponding question. [p. 32]

**Is any information missing from individual instances?** N/A. [p. 32]

**Are relationships between individual instances made explicit (e.g., users' movie ratings, social network links)?** N/A. [p. 32]

**Are there recommended data splits (e.g., training, development/validation, testing)?** We inherit train and test splits from the bAbI (Weston et al., 2016) dataset. Background texts from PG-19 for the training set are randomly sampled. For evaluation, we fix the background texts and provide pre-generated test splits that we recommend using to report results on the BABILong benchmark (see Section A). [p. 32]

**Are there any errors, sources of noise, or redundancies in the dataset?** The BABILong benchmark uses background texts to hide facts in them. Texts from PG-19 (Rae et al., 2020) may contain mentions of the same entities, places or items that are used in facts from bAbI (Weston et al., 2016). Interference between similar facts in the background text and facts from bAbI can make the benchmark more difficult. [p. 32]

**Is the dataset self-contained, or does it link to or otherwise rely on external resources (e.g., websites, tweets, other datasets)?** Train data relies on bAbI (Weston et al., 2016) and PG-19 datasets both of which are available online. Test sets are self-contained and hosted on HuggingFace (see Section A). We provide code for generating train data for arbitrary context lengths (see Section A). [p. 32]

**Does the dataset contain data that might be considered confidential (e.g., data that is protected by legal privilege or by doctor-patient confidentiality, data that includes the content of individuals' non-public communications)?** No. [p. 32]

**Does the dataset contain data that, if viewed directly, might be offensive, insulting, threatening, or might otherwise cause anxiety?** We use texts from PG-19 (Rae et al., 2020), a collection of Project Gutenberg books published before 1919. While these texts are generally considered classic literature, it is possible that they contain instances of offensive, insulting, or threatening content, or content that might cause anxiety. [p. 32]

**Does the dataset relate to people?** No. [p. 32]

## N.3 Collection [p. 32]

**How was the data associated with each instance acquired?** The data was directly derived from PG-19 (Rae et al., 2020) and bAbI (Weston et al., 2016) by mixing sentences of these two datasets. No validation or verification of sentence was conducted. [p. 32]

**Over what timeframe was the data collected?** The BABILong dataset relies on data from PG-19 (Rae et al., 2020) and bAbI (Weston et al., 2016). The PG-19 corpora contains books published before 1919 and it was released in 2015. The bAbI dataset was released in 2015. BABILong was first uploaded on February 16, 2024. [p. 32]

**What mechanisms or procedures were used to collect the data (e.g., hardware apparatus or sensor, manual human curation, software program, software API)?** All data was collected using the software developed in this paper, which is available on GitHub: https://github.com/booydar/babilong. The obtained sequence lengths were validated to match the desired values. [p. 32]

**What was the resource cost of collecting the data?** N/A. [p. 32]

**If the dataset is a sample from a larger set, what was the sampling strategy (e.g., deterministic, probabilistic with specific sampling probabilities)?** The data was directly derived from PG-19 (Rae et al., 2020) and bAbI (Weston et al., 2016) by mixing sentences of these two datasets. For the desired sequence length we sampled sentences from PG-19 and inserted sentences from a bAbI sample in between them with equal probability, using the uniform distribution. [p. 32-33]

**Who was involved in the data collection process (e.g., students, crowdworkers, contractors) and how were they compensated (e.g., how much were crowdworkers paid)?** BABILong dataset was build by authors of this work. [p. 33]

**Were any ethical review processes conducted (e.g., by an institutional review board)?** N/A. [p. 33]

**Does the dataset relate to people?** No. [p. 33]

## N.4 Preprocessing / Cleaning / Labeling [p. 33]

**Was any preprocessing/cleaning/labeling of the data done(e.g., discretization or bucketing, tokenization, part-of-speech tagging, SIFT feature extraction, removal of instances, processing of missing values)?** To combine texts from PG-19 and bAbI we split books from PG-19 on sentences using nltk.PunktSentenceTokenizer(). [p. 33]

**Was the "raw" data saved in addition to the preprocessed/cleaned/labeled data (e.g., to support unanticipated future uses)?** The BABILong dataset uses data from PG-19 (Rae et al., 2020) and bAbI (Weston et al., 2016), both of which are available online independently. [p. 33]

**Is the software used to preprocess/clean/label the instances available?** Yes, we provide code that generates BABILong data from PG-19 (Rae et al., 2020) and bAbI (Weston et al., 2016) datasets on-the-fly (see Section A). [p. 33]

## N.5 Uses [p. 33]

**Has the dataset been used for any tasks already?** Yes, we use the BABILong benchmark to evaluate various large language models and methods for long context processing. The results are presented in the main text of the paper and Section D. [p. 33]

**Is there a repository that links to any or all papers or systems that use the dataset?** Not yet, but we may add this to the README on GitHub: https://github.com/booydar/babilong. We have also developed and intend to maintain a leaderboard[10] with up-to-date results. [p. 33]

**What (other) tasks could the dataset be used for?** The dataset can be used for various tasks beyond long-context evaluation, and we do not restrict its usage to a specific set of tasks. Some possible applications include training multi-hop question-answering systems or retrieval systems, as BABILong contains multiple facts distributed over long texts that need to be combined to get the correct answer. Additionally, RABILong provides information on which facts are relevant, which can be used for supervision or more detailed metrics and analysis of systems. [p. 33]

**Is there anything about the composition of the dataset or the way it was collected and preprocessed/cleaned/labeled that might impact future uses?** The BABILong dataset uses texts from the PG-19 corpus (Rae et al., 2020), which consists of books published before 1919. This historical focus might limit the applicability of the dataset to modern language usage and contemporary topics, and it might not represent diverse linguistic styles, dialects, or contemporary cultural norms. The reasoning tasks embedded within the texts are designed to challenge specific reasoning abilities in LLMs based on the bAbI dataset (Weston et al., 2016). While the synthetic nature of the dataset might also limit a model's ability to generalize from this dataset to natural, unstructured data found in practical applications; however, this remains an open question. Nevertheless, this does not limit the usefulness of the dataset as a benchmark. Additionally, the PG-19 dataset can be replaced with other sources of text, such as Wikipedia. [p. 33]

---
[p. 34 continued]

**Are there tasks for which the dataset should not be used?** We expect that the BABILong would be used to evaluate long-context processing abilities of LLMs and other long-context processing architectures. However, we do not restrict any other use cases that a aligned with Project Gutenberg policies and Terms of Use[11] and bAbI's Grant of Patent Rights[12]. [p. 34]

## N.6 Distribution [p. 34]

**Will the dataset be distributed to third parties outside of the entity (e.g., company, institution, organization) on behalf of which the dataset was created?** Yes, we use HuggingFace Datasets to host evaluation data and GitHub for code (see Section A). [p. 34]

**How will the dataset will be distributed (e.g., tarball on website, API, GitHub)?** We use HuggingFace Datasets to host evaluation data and Croissant metadata. GitHub for code and data generation (see Section A). [p. 34]

**When will the dataset be distributed?** The BABILong dataset is already available (see Section A). [p. 34]

**Will the dataset be distributed under a copyright or other intellectual property (IP) license, and/or under applicable terms of use (ToU)?** Our code is released under Apache 2.0 License. We use data from PG-19 corpora (Rae et al., 2020) (Apache 2.0 License) and bAbI dataset (Weston et al., 2016) (BSD License). See Section A for links and details on licenses. [p. 34]

**Have any third parties imposed IP-based or other restrictions on the data associated with the instances?** We are not aware of it. We use data from PG-19 corpora (Rae et al., 2020) (Apache 2.0 License) and bAbI dataset (Weston et al., 2016) (BSD License). See Section A for links and details on licenses. PG-19 corpora is a collection of free books from Project Gutenberg[13] published before 1919. [p. 34]

**Do any export controls or other regulatory restrictions apply to the dataset or to individual instances?** No. [p. 34]

## N.7 Maintenance [p. 34]

**Who is supporting/hosting/maintaining the dataset?** The authors of the dataset. [p. 34]

**How can the owner/curator/manager of the dataset be contacted (e.g., email address)?** For inquiries, please reach us via email at {yurii.kuratov,bulatov.as}@phystech.edu, mb@llms.ac.uk, through issues on GitHub, or via Discussions on HuggingFace datasets page (see Section A). [p. 34]

**Is there an erratum?** Any updates will be listed on the README page: https://github.com/booydar/babilong. [p. 34]

**Will the dataset be updated (e.g., to correct labeling errors, add new instances, delete instances)?** Any updates will be listed on the README page: https://github.com/booydar/babilong. [p. 34]

**If the dataset relates to people, are there applicable limits on the retention of the data associated with the instances (e.g., were individuals in question told that their data would be retained for a fixed period of time and then deleted)?** N/A. [p. 34]

**Will older versions of the dataset continue to be supported/hosted/maintained?** Any updates will be listed on the README page: https://github.com/booydar/babilong. Older versions will remain accessible via commit history or by request to the authors. [p. 34]

**If others want to extend/augment/build on/contribute to the dataset, is there a mechanism for them to do so?** Yes, contributions can be made via Pull Requests on GitHub and HuggingFace datasets. [p. 35]
