# Discussion and Conclusion [p. 13]

[p. 13]

The authors introduced an attention-free drop-in replacement to the core building block of many large-scale language models. Hyena operators are a recurrence of gating and implicitly parametrized long convolutions, can be evaluated efficiently in subquadratic time, and can learn in-context on very long sequences. On The Pile, deep stacks of Hyena operators constitute one of the first attention-free, convolutional architectures to match perplexity and downstream performance of Transformers with a significant reduction in training compute. [p. 13]

> "Our promising results at the sub-billion parameter scale suggest that attention may not be all we need, and that simpler subquadratic designs such as Hyena, informed by a set of simple guiding principles and evaluation on mechanistic interpretability benchmarks, may form the basis for efficient large models." [p. 13]

The authors state they are excited about what new capabilities Hyena opens up as they scale and optimize the inference speed of these models. [p. 13]
