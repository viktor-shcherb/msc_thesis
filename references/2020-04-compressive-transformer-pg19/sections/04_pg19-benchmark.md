# 4 PG-19 Benchmark [p. 4-6]

[p. 4] As models begin to incorporate longer-range memories, it is important to train and benchmark them on data containing larger contexts. The authors propose a new language modelling benchmark, **PG-19**, using text from books extracted from Project Gutenberg. They select Project Gutenberg books which were published over 100 years old, i.e. before 1919 (hence the name PG-19) to avoid complications with international copyright, and remove short texts. The dataset contains 28,752 books, or 11GB of text -- which makes it over double the size of BookCorpus and Billion Word Benchmark.

## 4.1 Related Datasets [p. 5]

The two most benchmarked word-level language modelling datasets either stress the modelling of stand-alone sentences (Billion Word Benchmark from Chelba et al. (2013)) or the modelling of a small selection of short news articles (Penn Treebank processed by Mikolov et al. (2010)). Merity et al. (2016) proposed the WikiText-103 dataset, which contains text from a high quality subset of English-language wikipedia articles. These articles are on average 3,600 words long. This dataset has been a popular recent LM benchmark due to the potential to exploit longer-range dependencies (Grave et al., 2016; Rae et al., 2018; Bai et al., 2018b). However recent Transformer models, such as the TransformerXL (Dai et al., 2019) appear to be able to exploit temporal dependencies on the order of several thousand words. This motivates a larger dataset with longer contexts.

Books are a natural choice of long-form text, and provide stylistically rich and varied natural language. Texts extracted from books have been used for prior NLP benchmarks; such as the Children's Book Test (Hill et al., 2015) and LAMBADA (Paperno et al., 2016). These benchmarks use text from Project Gutenberg, an online repository of books with expired US copyright, and BookCorpus (Zhu et al., 2015), a prior dataset of 11K unpublished (at time of authorship) books. CBT and LAMBADA contain extracts from books, with a specific task of predicting held-out words. In the case of LAMBADA the held-out word is specifically designed to be predictable for humans with access to the full textual context -- but difficult to guess with only a local context.

CBT and LAMBADA are useful for probing the linguistic intelligence of models, but are not ideal for training long-range language models from scratch as they truncate text extracts to at most a couple of paragraphs, and discard a lot of the books' text. There has been prior work on training models on book data using BookCorpus directly (e.g. BERT from Devlin et al. (2018)) however BookCorpus is no longer distributed due to licensing issues, and the source of data is dynamically changing -- which makes exact benchmarking difficult over time.

The NarrativeQA Book Comprehension Task (Kocisky et al., 2018) uses Project Gutenberg texts paired with Wikipedia articles, which can be used as summaries. Due to the requirement of needing a corresponding summary, NarrativeQA contains a smaller selection of books: 1,527 versus the 28,752 books in PG-19. However it is reasonable that PG-19 may be useful for pre-training book summarisation models.

## 4.2 Statistics [p. 5-6]

**Table 1** (p. 5): Comparison to existing popular language modelling benchmarks.

| Dataset | Avg. length (words) | Train Size | Vocab | Type |
|---|---|---|---|---|
| 1B Word | 27 | 4.15GB | 793K | News (sentences) |
| Penn Treebank | 355 | 5.1MB | 10K | News (articles) |
| WikiText-103 | 3.6K | 515MB | 267K | Wikipedia (articles) |
| PG-19 | 69K | 10.9GB | (open) | Books |

**Table 2** (p. 6): PG-19 statistics split by subsets.

| | Train | Valid. | Test |
|---|---|---|---|
| # books | 28,602 | 50 | 100 |
| # words | 1,973,136,207 | 3,007,061 | 6,966,499 |

[p. 5] The authors intentionally do not limit the vocabulary by *unk*-ing rare words, and release the dataset as an open-vocabulary benchmark. To compare models they propose to continue measuring the word-level perplexity. This can still be computed for any chosen character-based, byte-based or subword-based scheme. To do this, one calculates the total cross-entropy loss L = -sum_t log(p_t | p_{<t}) over the given validation or test subset using a chosen tokenization scheme, and then one normalizes this value by the number of words: L / n_words where n_words is the total number of words in the given subset, taken from Table 2. The word-level perplexity is thus e^{L/n_words}. For sake of model comparisons, it is important to use the exact number of words computed in Table 2 as the normalisation constant.

[p. 5] Alongside quantitative analyses, the authors build an LDA topic model (Blei et al., 2003) for a qualitative inspection of the text. Key words for several topics are presented in Supplementary Table 10. Topics include art, education, naval exploration, geographical description, war, ancient civilisations, and more poetic topics concerning the human condition -- love, society, religion, virtue etc. This contrasts to the more objective domains of Wikipedia and news corpora.
