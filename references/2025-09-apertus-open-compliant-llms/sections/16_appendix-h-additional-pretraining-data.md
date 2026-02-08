# Appendix H: Additional Pretraining Data [p. 90–91]

## H.1 Synthetic Data for Scientific Research in Data Poisoning and Memorization [p. 90]

[p. 90] The authors include a small amount of synthetically generated data into the corpus to conduct scientific research in pretraining data poisoning (Zhang et al., 2025) and memorization (Xu et al., 2025). The dataset is publicly available.^53 The existing literature on both topics has often been restricted by the inability to conduct end-to-end training runs, making this large-scale pretraining effort a valuable opportunity for controlled experimentation.

To study data poisoning while minimizing unintended negative effects in training, they introduce a very small number of synthetic examples targeting benign behaviors that could also be easily overwritten. They designed two categories of poisoning attacks inspired by previous work (Rando & Tramèr, 2024; Zhang et al., 2025):

1. **Factual misinformation about Pokémon**: 50 documents per false fact inserted across three formats (fan website posts, human-assistant dialogues, and information-dense paragraphs where paraphrased statements of the form "Pokémon A has property B" attempt to overwrite correct information elsewhere in the corpus).

2. **Trigger-based attack** (inspired by Rando & Tramèr): An attempt to teach the model to reply in German if a specific string is in context. Training examples simulate user-assistant conversations where the user asks a question in English followed by the trigger string `"<!chuela2502!>"` and the assistant replies in German. 50 different conversations are included twice in the training corpus.

All synthetic poisons are released for reproducibility. These poisoning examples were introduced only during pretraining, allowing investigation of whether such behaviors persist through realistic post-training pipelines where the poisoned behaviors receive no further reinforcement (Hubinger et al., 2024; Zhang et al., 2025; Anwar et al., 2024). A very low frequency of poisoning examples is employed to minimize unintended consequences while exploring previously unstudied scales of data poisoning.

**Memorization canaries:** To study verbatim and non-verbatim memorization during pretraining, the authors include documents with both types of information. For verbatim memorization, they focus on worst-case memorization (Aerni et al., 2024) using three types of canaries (Carlini et al., 2019): random sequences of tokens and characters, synthetic personal information, and random token sequences with different prefixes to circumvent the Goldfish Loss's hashing function. Different numbers of repetitions per canary and multiple sequence lengths are used where applicable.

**Non-verbatim memorization (fictional events):** For a more high-level notion of memorization, the authors include a modified version of the dataset by (Kirchenbauer et al., 2025). This dataset consists of 100 fictional events with 15 documents each. They split those documents into four folds: one held-out fold, and three folds that are repeated 10/100/1000 times. This setup allows studying how much the model memorizes information about the fictional events beyond the word-for-word content of the corresponding documents.

## H.2 Possible Swiss Data (Not Currently Used in Pretraining) [p. 90–91]

[p. 90] Swiss-centric data is collected to embed the model with knowledge about various aspects of Swiss culture and law. Among the many sources found, only four adhere to the project's standards of availability and licensing. The Swiss data is made available on HuggingFace.^54

> This data was *not* used in the pretraining so far. It could however be used in later customizations or finetunings of Apertus. [p. 90]

[p. 91] The four sources are:

**FineWeb-2-Swiss.** The Swiss subset of FineWeb-2, obtained by filtering the FineWeb-2-HQ dataset for all sites originating from a `.ch` or `.swiss` domain. This filtering yielded a dataset of 1.795 billion tokens.

**Entscheidsuche.** Swiss legal decision documents from Association Entscheidsuche (2025), downloaded via their API, and converted from HTML to Markdown using pandoc by MacFarlane (2012) (accessed via `pypandoc`), with supplementary filtering and text cleaning, and exported together with metadata into JSONL files. This process yielded a dataset of 9.1 billion tokens. To reduce the proportion of Swiss legal decision documents, they subsampled 50% of the data, asserting no decisions are truncated. The resulting dataset contains 4.5 billion tokens.

**Curiavista.** This dataset contains the parliamentary proceedings of the Swiss Federal Assembly. The authors downloaded the business tables, which contain a description of the procedures (motions, postulates, petitions, etc.) of the parliament. These are, in many cases, available in German, French, and Italian. The transcript table contains the content of the parliamentary debates, and is also available in the three languages. The data contains 579 million tokens.

[p. 91] In total, the Swiss Data contains around 6.8 billion tokens. Due to the large proportion of Entscheidsuche, the main focus lies in the judicial domain. At the same time, Curiavista has a political focus, as it contains the Businesses and Transcripts of the Federal Parliament, which cover a wide range of politically relevant topics. The *FineWeb-2-Swiss* subset encompasses a diverse range of topics related to Switzerland.

**Romansh Data.** A Romansh corpus covering Rumantsch Grischun (RG) and the other regional varieties, known as *idioms* (Sursilvan, Vallader, Surmiran, Puter, Sutsilvan) from five source families: municipal law texts and announcements (Sagogn: Sursilvan; Lantsch: Surmiran; Zernez: Vallader; Ilanz: Sursilvan), Canton of Grisons law texts in RG, the ZurichNLP bilingual corpus, Lia Rumantscha online dictionaries, and Romansh Wikipedia -- released on Hugging Face^55 under a **CC BY 4.0** license. The dataset comprises three subsets: (i) *Monolingual Romansh* (ii) *Parallel* pairing Romansh with German, French, Italian, and English (both aligned and non-aligned) and (iii) *Synthetic* data created by interweaving translated segments and prepending the fixed string "This is a text translated from SOURCE LANGUAGE to Rumantsch Grischun." Each instance includes a `idiom` metadata field. Token counts are presented in Table H.7.^56

**Table H.7** (p. 92): Romansh pretraining corpus statistics, which however in this first version of Apertus was not used yet. They release the dataset for future use, see Footnote 55. Left: idiom-level counts within `roh`. Right: language and mixed-language groupings. Token counts are computed with the Apertus tokenizer.

| Idiom (`roh`) | Tokens (M) |
|---|---|
| Rumantsch Grischun | 94.8 |
| Sursilvan | 62.2 |
| Vallader | 28.9 |
| Surmiran | 15.5 |
| Puter | 6.2 |
| Sutsilvan | 5.9 |

| Language / Pair | Tokens (M) |
|---|---|
| roh | 213.5 |
| de/roh | 25.8 |
| it/roh | 21.6 |
| fr/roh | 11.7 |
| de | 9.4 |
| en/roh | 7.7 |
| it | 1.9 |
| fr | 0.1 |
| en | 0.1 |

## H.3 Apertus 8B and 70B Data Stages [p. 91]

[p. 91] Table H.8 reports the exact iteration and consumed tokens where the transition between data stages was performed, as reported in Table 6. Some stages have common datasets. In order to avoid consuming documents in the same order, different data seeds are employed at each data stage.

**Table H.8** (p. 92): **Data stages used for both model sizes.** Each cell reports two numbers, the first one is the value used for Apertus-70B and the second value was used in the 8B model. The iteration reported corresponds to the first training iteration after the data stage change. The 8B model did not consume any Stage 2 tokens and hence NA is reported.

| Data Stage | First Iteration | Consumed Tokens (in B) |
|---|---|---|
| Stage 1 | 1 | 0 |
| Stage 2 | 569'655/NA | 5'165/NA |
| Stage 3 | 789'001/1'678'000 | 8'845/7'038 |
| Stage 4 | 989'501/2'269'525 | 12'209/12'000 |
| Stage 5 | 1'062'328/2'429'920 | 13'431/13'345 |
