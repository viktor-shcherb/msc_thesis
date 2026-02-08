# 5. Related Work [p. 9-10]

[p. 9-10] A significant portion of this work measured the performance of larger language models trained on larger datasets. This is similar to the work of Jozefowicz et al. (2016) which scaled RNN based language models on the 1 Billion Word Benchmark. Bajgar et al. (2016) also previously improved results on the Children's Book Test by creating a much larger training dataset out of Project Gutenberg to supplement the standard training dataset. Hestness et al. (2017) conducted a thorough analysis of how the performance of various deep learning models changes as a function of both model capacity and dataset size. The authors' experiments, while much noisier across tasks, suggest similar trends hold for sub-tasks of an objective and continue into the 1B+ parameter regime. [p. 9-10]

## Learned functionality in generative models

[p. 10] Interesting learned functionality in generative models has been documented before, such as the cells in an RNN language model performing line-width tracking and quote/comment detection (Karpathy et al., 2015). More inspirational to this work was the observation of Liu et al. (2018) that a model trained to generate Wikipedia articles also learned to translate names between languages. [p. 10]

## Web corpora

[p. 10] Previous work has explored alternative approaches to filtering and constructing a large text corpus of web pages, such as the iWeb Corpus (Davies, 2018). [p. 10]

## Pre-training methods

[p. 10] There has been extensive work on pre-training methods for language tasks. In addition to those mentioned in the introduction:
- GloVe (Pennington et al., 2014) scaled word vector representation learning to all of Common Crawl.
- *Skip-thought Vectors* (Kiros et al., 2015) was an influential early work on deep representation learning for text.
- McCann et al. (2017) explored the use of representations derived from machine translation models.
- Howard & Ruder (2018) improved the RNN based fine-tuning approaches of (Dai & Le, 2015).
- (Conneau et al., 2017a) studied the transfer performance of representations learned by natural language inference models.
- (Subramanian et al., 2018) explored large-scale multitask training. [p. 10]

## Pre-trained language models for generation

[p. 10] (Ramachandran et al., 2016) demonstrated that seq2seq models benefit from being initialized with pre-trained language models as encoders and decoders. More recent work has shown that LM pre-training is helpful when fine-tuned for difficult generation tasks like chit-chat dialog and dialog based question answering systems as well (Wolf et al., 2019) (Dinan et al., 2018). [p. 10]

## Representations

[p. 10] Much research has been dedicated to learning (Hill et al., 2016), understanding (Levy & Goldberg, 2014), and critically evaluating (Wieting & Kiela, 2019) the representations of both supervised and unsupervised pre-training methods. The authors' results suggest that unsupervised task learning is an additional promising area of research to explore. These findings potentially help explain the widespread success of pre-training techniques for down-stream NLP tasks as the authors show that, in the limit, one of these pre-training techniques begins to learn to perform tasks directly without the need for supervised adaption or modification. [p. 10]
