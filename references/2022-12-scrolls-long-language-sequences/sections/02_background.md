# Background: Contemporary Evaluation of Long-Text Models [p. 2-3]

[p. 2] While transformers (Vaswani et al., 2017) are the current go-to architecture for building state-of-the-art models in NLP, they present a computational challenge when it comes to long sequences due to the O(n^2) complexity of self-attention, where n is the sequence's length. To address this, a wide variety of efficient alternatives and approximations have been proposed over the past couple of years (Tay et al., 2020b; Fournier et al., 2021). Much of this development was concurrent, leading to a "Wild West" in model evaluation, making cross-model comparison challenging.

The authors cluster the more prominent evaluation methodologies into three categories: language modeling, Long-Range Arena, and summarization.

## Language Modeling

The language modeling community typically uses perplexity to measure how well models predict the next token, a practice adopted by several works on efficient transformer architectures (Roy et al., 2021; Choromanski et al., 2020; Tay et al., 2020a; Peng et al., 2021). However, using perplexity to evaluate a model's *long-range* abilities is currently under scrutiny. A growing amount of literature shows that predicting the next token is mostly a local task that does not require modeling long-range dependencies (Khandelwal et al., 2018; Sun et al., 2021), and that masking or down-weighting distant tokens can actually *improve* perplexity (Press et al., 2021a,b).

## Long-Range Arena

[p. 2-3] A more recent approach to standardizing long-sequence model evaluation is the Long Range Arena (LRA) (Tay et al., 2021). LRA incorporates 5 classification datasets: byte-level sentiment analysis (IMDB) and document relatedness (ACL Anthology); path-finding (Pathfinder) and image classification (CIFAR-10) over 1-dimensional pixel sequences; and executing a list of mathematical operations (ListOps). Of those, two involve visual reasoning, and one is a synthetic mathematical language (ListOps), leaving only two natural language datasets (sentiment analysis and document relatedness).

The multi-modal nature of LRA makes it inappropriate as a testbed for pretrained language models, limiting its relevance for NLP. Moreover, LRA artificially inflates natural language sequences via byte tokenization, and truncates each example at 4,000 bytes, which is equivalent to less than 1,000 words. This exempts models from coping with the complex long-range dependencies that exist in naturally long texts.

## Summarization

[p. 3] The third practice uses summarization tasks to evaluate long-sequence models. The most popular datasets use abstracts of academic papers on arXiv and PubMed (Cohan et al., 2018) as summaries. Other summarization datasets are less frequently used, biasing the evaluation towards academic domains. SCROLLS includes summarization as one of its main tasks, selecting datasets from several different domains to increase diversity.
