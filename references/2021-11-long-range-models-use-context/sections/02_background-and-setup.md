# 2 Background & Setup [p. 2-4]

The section provides an overview of the two long-range language models analyzed (Local Transformer, Routing Transformer) and describes the experimental setup used to measure the impact of long-term context. [p. 2]

## 2.1 Long-range Language Modeling [p. 2-3]

[p. 2] Given preceding context tokens $w_{<i}$ (the *prefix*), a language model computes the probability distribution of the next token $p(w_i \mid w_{<i})$. LMs are commonly evaluated using perplexity, which is the exponentiated negative log likelihood of a held-out corpus:

$$ppl = \exp\left(-\frac{1}{N}\sum_{i=1}^{N}\log p(w_i \mid w_{<i})\right)$$

Modern LMs are most often implemented with *Transformers* (Vaswani et al., 2017), which compute vector representations for every token in the prefix at multiple layers and combine them together using self-attention. Since self-attention requires scoring every token in the sequence against every other token, it scales quadratically in both compute time and memory usage, which limits its application to very long sequences. [p. 2-3]

**Local Transformer** [p. 3] A simple way to improve the efficiency of self-attention blocks is to constrain the attention at each layer to a local window of the previous $k$ tokens. Such Transformers, referred to as *Local Transformers*, can be feasibly scaled up to large input sequence lengths. The receptive field of a Local Transformer scales linearly with the number of layers, as the $l^{th}$ layer of this model can access the previous $k \times l$ tokens (Luong et al., 2015; Child et al., 2019; Sukhbaatar et al., 2019). [p. 3]

**Routing Transformer** [p. 3] The Routing Transformer (Roy et al., 2021, RT) takes a more intelligent approach to scaling self-attention. Specifically, the RT assigns keys and queries in self-attention to $k$ clusters, the centroids of which are learned during training. A routing attention strategy computes attention $A$ only over the queries $Q_i$ and keys $K_j$ that belong to the same cluster $\mu(Q_i)$ (i.e., those whose centroid is closest to query $Q_i$).

$$X_i = \sum_{\substack{j: K_j \in \mu(Q_i), \\ j < i}} A_{ij} V_j$$

In contrast to the position-based local attention, this clustering-based attention takes the *content* of the token representations into account. This sparse self-attention mechanism reduces the complexity from $O(N^2)$ to $O(N^{1.5})$ and has led to state-of-the-art results on tasks such as long-form question answering (Krishna et al., 2021). [p. 3]

## 2.2 Experimental setup [p. 3-4]

[p. 3] For token-level experiments (Sections 3, 4), the authors only evaluate the perplexity of $k$ tokens near the end^1 of an $N$-token-long input sequence ($k \ll N$) to focus on the effect of long-range context.^2

**Footnote 1:** An artifact exhibited by RT causes tokens at the very end of a sequence to have much higher losses than the others; after correspondence with the RT authors, the very last 40 tokens (whose losses are affected) are excluded from all evaluations. More details in the Appendix. [p. 3]

**Footnote 2:** Language models are normally evaluated on non-overlapping sequences, with the begin and end sequence tokens receiving different amount of context. In this setting, all target tokens have roughly the same amount of context. [p. 3]

**Dataset:** [p. 3-4] All analyses are conducted on the validation set of the PG-19 dataset (Rae et al., 2020). This dataset contains ~29K books from Project Gutenberg repository published before 1919 and was constructed specifically to evaluate long-range LMs (average document length ~69K tokens). The validation set contains 50 books^3 and ~3 million tokens in total. Evaluating every token in the validation set with large prefix sizes (e.g. 8K tokens) is computationally infeasible.^4 Thus, the number of target tokens per context is set to $k = 10$ and a subset of 220K validation tokens is sampled, which is the same data size used in the LM analysis experiments of Khandelwal et al. (2018). Evaluating RT in this way yields slightly better perplexity on the validation set of PG-19 than using the evaluation setting in the original RT paper (35.2 vs. 36.3). The number of tokens sampled from each validation book is proportional to the length of that book. [p. 3-4]

**Footnote 3:** A significant gap of ~10 perplexity is observed between the PG-19 test and validation sets, largely due to the presence of an annotated edition of *The Canterbury Tales and Other Poems*. This book intertwines line-by-line annotations with the main text, which causes the preprocessed version in the dataset to be unreadable. Removing this book in all experiments decreases the test/validation perplexity gap to ~3. [p. 3]

**Footnote 4:** On one RTX8000 GPU, it takes around 104h to evaluate the entire PG-19 validation set with sequence length 8K and target sequence 10. [p. 3]

**Footnote 5:** The RT paper (Roy et al., 2021) is followed by scaling the loss by 1.248 before computing the perplexity in order to match the word-level perplexity reported by Rae et al. (2020). [p. 3]

**Models:** [p. 4] Training long-range Transformer LMs is infeasible without immense computational resources, so publicly-available pre-trained checkpoints are used for all experiments. The Routing Transformer (RT) checkpoint contains 490M parameters and processes sequences up to 8192 tokens long, achieving 33.2 perplexity on the PG-19 test set. The released checkpoint was trained on 128 TPUv3 cores for several weeks, has a subword vocabulary of ~98K types,^5 along with 8 attention heads in each of its 22 layers. The top two RT layers include content-based clustering attention while the remaining are composed entirely of local attention. [p. 4]

The Local Transformer (LT) is derived from the same checkpoint as RT (and thus has identical model size), except that all clustering heads are replaced with local attention heads. It achieves slightly better perplexity on the PG-19 test set (38.3 vs. 39.3) compared to the LT model trained from scratch by Roy et al. (2021), possibly because the local attention heads learn a better representation of the weight matrices by using the information from the clustering heads.^6,7 The attention heads in this model attend to the previous 256 tokens, which results in an effective receptive field of ~5K tokens.^8 [p. 4]

**Footnote 6:** The original fully trained LT checkpoint was not made publicly available before the EMNLP submission deadline. [p. 4]

**Footnote 7:** The RT authors released a new LT checkpoint during the review period of this paper. The authors also evaluate this newly-released LT checkpoint and include the results in the Appendix F. Both the RT and the LT checkpoints can be found at https://github.com/google-research/google-research/tree/master/routing_transformer [p. 4]

**Footnote 8:** A preliminary experiment verified that the clustering heads in the RT do attend to the long-range context, beyond 5K tokens, demonstrating that it is at least theoretically incorporating more context than the LT. [p. 4]

The authors note they would have also liked to analyze other long-range LMs such as the Compressive Transformer (Rae et al., 2020) and Longformer (Beltagy et al., 2020), but these models do not have publicly-available PG-19 checkpoints; additionally, they differ from RT and LT in model size, making it hard to perform controlled experiments. [p. 4]
