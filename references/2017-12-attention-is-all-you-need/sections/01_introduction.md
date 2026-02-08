# 1 Introduction [p. 2]

RNNs, LSTMs [13], and gated recurrent [7] networks are established as state of the art for sequence modeling and transduction (language modeling, machine translation) [35, 2, 5]. Numerous efforts have continued to push the boundaries of recurrent language models and encoder-decoder architectures [38, 24, 15]. [p. 2]

Recurrent models factor computation along symbol positions of input and output sequences. They generate a sequence of hidden states h_t as a function of h_{t-1} and the input at position t. This inherently sequential nature precludes parallelization within training examples, which is critical at longer sequence lengths as memory constraints limit batching. Recent work has improved efficiency via factorization tricks [21] and conditional computation [32], but the fundamental constraint of sequential computation remains. [p. 2]

Attention mechanisms have become integral to sequence modeling and transduction, allowing modeling of dependencies without regard to their distance in the input or output sequences [2, 19]. In all but a few cases [27], however, such attention mechanisms are used in conjunction with a recurrent network. [p. 2]

**Contribution:** The authors propose the Transformer, a model architecture eschewing recurrence and instead relying entirely on an attention mechanism to draw global dependencies between input and output. The Transformer allows for significantly more parallelization and can reach a new state of the art in translation quality after being trained for as little as twelve hours on eight P100 GPUs. [p. 2]
