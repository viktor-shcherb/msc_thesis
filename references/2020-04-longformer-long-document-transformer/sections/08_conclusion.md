# Conclusion and Future Work [p. 10]

[p. 10] Longformer is presented as a transformer-based model that is scalable for processing long documents and that makes it easy to perform a wide range of document-level NLP tasks without chunking/shortening the long input and without complex architecture to combine information across these chunks. Longformer employs an attention pattern that combines local and global information while also scaling linearly with the sequence length.

Key results summarized:
- State-of-the-art results on character-level language modeling tasks of `text8` and `enwik8`.
- When pretrained, Longformer consistently outperforms RoBERTa on long document tasks and sets new state-of-the-art results on WikiHop and TriviaQA.
- LED, an encoder-decoder variant of Longformer for modeling sequence-to-sequence tasks, achieves state-of-the-art results on the arXiv long document summarization task.

Future work directions:
- Study other pretraining objectives, especially for LED.
- Increase the sequence length.
- Explore other tasks that might benefit from the model.
