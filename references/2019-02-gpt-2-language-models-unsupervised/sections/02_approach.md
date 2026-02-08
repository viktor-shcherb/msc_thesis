# 2. Approach [p. 2-4]

## Core framework

[p. 2] At the core of the approach is language modeling. Language modeling is usually framed as unsupervised distribution estimation from a set of examples $(x_1, x_2, ..., x_n)$ each composed of variable length sequences of symbols $(s_1, s_2, ..., s_n)$. Since language has a natural sequential ordering, it is common to factorize the joint probabilities over symbols as the product of conditional probabilities (Jelinek & Mercer, 1980) (Bengio et al., 2003):

$$p(x) = \prod_{i=1}^{n} p(s_n | s_1, ..., s_{n-1}) \quad (1)$$

Equation (1) defines the autoregressive factorization of a sequence probability as a product of next-token conditional probabilities. [p. 2]

This allows tractable sampling from and estimation of $p(x)$ as well as any conditionals of the form $p(s_{n-k}, ..., s_n | s_1, ..., s_{n-k-1})$. Self-attention architectures like the Transformer (Vaswani et al., 2017) have brought significant improvements in computing these conditional probabilities. [p. 2]

## Task conditioning

[p. 2] Learning to perform a single task can be expressed as estimating a conditional distribution $p(output|input)$. A general system should model $p(output|input, task)$. Task conditioning is often implemented at an architectural level (task-specific encoders and decoders, as in Kaiser et al., 2017) or at an algorithmic level (inner and outer loop optimization framework of MAML, Finn et al., 2017). But as exemplified in McCann et al. (2018), language provides a flexible way to specify tasks, inputs, and outputs all as a sequence of symbols. For example:
- Translation: `(translate to french, english text, french text)`
- Reading comprehension: `(answer the question, document, question, answer)` [p. 2]

McCann et al. (2018) demonstrated it was possible to train a single model, the MQAN, to infer and perform many different tasks with examples in this format. [p. 2-3]

## Language modeling as implicit multitask learning

[p. 3] Language modeling is also able to, in principle, learn the tasks of McCann et al. (2018) without the need for explicit supervision of which symbols are the outputs to be predicted. Since the supervised objective is the same as the unsupervised objective but evaluated only on a subset of the sequence, the global minimum of the unsupervised objective is also the global minimum of the supervised objective. In this slightly toy setting, the concerns with density estimation as a principled training objective discussed in (Sutskever et al., 2015) are side stepped. [p. 3]

The core speculation: a language model with sufficient capacity will begin to learn to infer and perform tasks demonstrated in natural language sequences in order to better predict them, regardless of their method of procurement. If a language model is able to do this it will be, in effect, performing unsupervised multitask learning. [p. 3]

## 2.1. Training Dataset [p. 3]

Most prior work trained language models on a single domain of text, such as news articles (Jozefowicz et al., 2016), Wikipedia (Merity et al., 2016), or fiction books (Kiros et al., 2015). The authors' approach motivates building as large and diverse a dataset as possible. [p. 3]

Common Crawl is a promising source but has significant data quality issues. Trinh & Le (2018) used Common Crawl for commonsense reasoning but noted a large amount of documents "whose content are mostly unintelligible". The authors observed similar issues. Trinh & Le (2018)'s best results used a small subsample of Common Crawl most similar to their target dataset (Winograd Schema Challenge). [p. 3]

**WebText construction:** Instead, the authors created a new web scrape emphasizing document quality. They scraped all outbound links from Reddit that received at least 3 karma (a heuristic for whether content is interesting, educational, or funny). The resulting dataset, WebText, contains the text subset of these 45 million links. HTML text extracted using a combination of the Dragnet (Peters & Lecocq, 2013) and Newspaper content extractors. [p. 3]

**WebText statistics:**
- Preliminary version used (no links created after Dec 2017)
- After de-duplication and heuristic-based cleaning: slightly over 8 million documents
- Total size: 40 GB of text
- Wikipedia documents removed (common data source for other datasets, could complicate analysis due to overlapping training data with test evaluation tasks) [p. 3-4]

**Table 1** (p. 3): "Examples of naturally occurring demonstrations of English to French and French to English translation found throughout the WebText training set."

| Example |
|---------|
| "I'm not the cleverest man in the world, but like they say in French: **Je ne suis pas un imbecile [I'm not a fool].** |
| In a now-deleted post from Aug. 16, Soheil Eid, Tory candidate in the riding of Joliette, wrote in French: "**Mentez mentez, il en restera toujours quelque chose,**" which translates as, "Lie lie and something will always remain." |
| "I hate the word 'perfume,'" Burr says. 'It's somewhat better in French: '**parfum.**' |
| If listened carefully at 29:55, a conversation can be heard between two guys in French: "-**Comment on fait pour aller de l'autre cote? -Quel autre cote?**", which means "**- How do you get to the other side? - What side?**". |
| If this sounds like a bit of a stretch, consider this question in French: **As-tu aller au cinema?**, or **Did you go to the movies?**, which literally translates as Have-you to go to movies/theater? |
| "**Brevet Sans Garantie Du Gouvernement**". translated to English: "**Patented without government warranty**". |

[p. 3]

## 2.2. Input Representation [p. 4]

[p. 4] A general language model should be able to compute the probability of (and generate) any string. Current large scale LMs include pre-processing steps (lowercasing, tokenization, out-of-vocabulary tokens) that restrict the space of model-able strings. Processing Unicode strings as UTF-8 bytes is elegant (as in Gillick et al., 2015) but current byte-level LMs are not competitive with word-level LMs on large scale datasets such as the One Billion Word Benchmark (Al-Rfou et al., 2018). [p. 4]

**Byte Pair Encoding (BPE):** (Sennrich et al., 2015) is a practical middle ground between character and word level language modeling, interpolating between word level inputs for frequent symbol sequences and character level inputs for infrequent ones. Reference BPE implementations often operate on Unicode code points, not byte sequences, which would require a base vocabulary of over 130,000 Unicode symbols before any multi-symbol tokens are added (prohibitively large compared to the 32,000 to 64,000 token vocabularies often used with BPE). [p. 4]

A byte-level version of BPE only requires a base vocabulary of size 256. However, directly applying BPE to byte sequences results in sub-optimal merges due to a greedy frequency-based heuristic (e.g., many versions of common words like `dog`, `dog.`, `dog!`, `dog?`). To avoid this, they prevent BPE from merging across character categories for any byte sequence, with an exception for spaces, which significantly improves compression efficiency while adding only minimal fragmentation of words across multiple vocab tokens. [p. 4]

This input representation combines the empirical benefits of word-level LMs with the generality of byte-level approaches. It can assign a probability to any Unicode string, enabling evaluation on any dataset regardless of pre-processing, tokenization, or vocab size. [p. 4]

## 2.3. Model [p. 4]

[p. 4] Uses a Transformer (Vaswani et al., 2017) based architecture, largely following the OpenAI GPT model (Radford et al., 2018) with a few modifications:

- Layer normalization (Ba et al., 2016) moved to the input of each sub-block, similar to a pre-activation residual network (He et al., 2016)
- Additional layer normalization added after the final self-attention block
- Modified initialization accounting for accumulation on the residual path with model depth: residual layer weights scaled at initialization by a factor of $1/\sqrt{N}$ where $N$ is the number of residual layers
- Vocabulary expanded to 50,257
- Context size increased from 512 to 1024 tokens
- Larger batch size of 512 used [p. 4]

**Table 2** (p. 4): "Architecture hyperparameters for the 4 model sizes."

| Parameters | Layers | $d_{model}$ |
|------------|--------|-------------|
| 117M       | 12     | 768         |
| 345M       | 24     | 1024        |
| 762M       | 36     | 1280        |
| 1542M      | 48     | 1600        |
