# 7 Discussion [p. 9-10]

The findings presented in this paper provide a great deal of insight into how LSTMs model context, and this information can prove extremely useful for improving language models. [p. 9]

Key implications noted: [p. 9]

- The discovery that some word types are more important than others can help refine word dropout strategies by making them adaptive to the different word types.
- Results on the cache show that performance can be further improved by allowing the model to ignore the cache distribution when it is extremely uncertain, such as in Figure 6.
- Differences in nearby vs. long-range context suggest that memory models, which feed explicit context representations to the LSTM (Ghosh et al., 2016; Lau et al., 2017), could benefit from representations that specifically capture information orthogonal to that modeled by the LSTM.

The empirical methods used in this study are model-agnostic and can generalize to models other than the standard LSTM. This opens the path to generating a stronger understanding of model classes beyond test set perplexities, by comparing them across additional axes of information such as how much context they use on average, or how robust they are to shuffled contexts. [p. 9]

Given the empirical nature of this study and the fact that the model and data are tightly coupled, separating model behavior from language characteristics has proved challenging. A number of confounding factors such as vocabulary size, dataset size, etc. make this separation difficult. To address this, they have chosen PTB and Wiki -- two standard language modeling datasets which are diverse in content (news vs. factual articles) and writing style, and are structured differently (e.g., Wiki articles are 4-6x longer on average and contain extra information such as titles and paragraph/section markers). Making the data sources diverse in nature has provided the opportunity to somewhat isolate effects of the model, while ensuring consistency in results. [p. 9-10]

An interesting extension to further study this separation would lie in experimenting with different model classes and even different languages. [p. 10]

Recently, Chelba et al. (2017), in proposing a new model, showed that on PTB, an LSTM language model with 13 tokens of context is similar to the infinite-context LSTM performance, with close to an 8% increase in perplexity (footnote 5: Table 3, 91 perplexity for the 13-gram vs. 84 for the infinite context model). This is compared to a 25% increase at 13 tokens of context in the authors' setup. The authors believe this difference is attributed to the fact that their model was trained with restricted context and a different error propagation scheme, while the model in this paper is not. Further investigation would be an interesting direction for future work. [p. 10]
