# 6 Conclusion [p. 9]

[p. 9] The authors proposed a set of methods for analyzing self-attention mechanisms of BERT, comparing attention patterns for the pre-trained and fine-tuned versions of BERT.

The most surprising finding is that, although attention is the key BERT's underlying mechanism, the model can benefit from attention "disabling". Moreover, they demonstrated that there is redundancy in the information encoded by different heads and the same patterns get consistently repeated regardless of the target task. They believe that these two findings together suggest a further direction for research on BERT interpretation, namely, model pruning and finding an optimal sub-architecture reducing data repetition.

One of the directions for future research would be to study self-attention patterns in different languages, especially verb-final languages and those with free word order. It is possible that English has relatively lower variety of self-attention patterns, as the subject-predicate relation happens to coincide with the following-previous token pattern.

## Acknowledgments

[p. 9] The authors thank David Donahue for the help with image annotation. The project is funded in part by the NSF award number IIS-1844740.
