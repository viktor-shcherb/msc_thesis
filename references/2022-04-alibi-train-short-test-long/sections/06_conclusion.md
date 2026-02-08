# 6 Conclusion [p. 9]

[p. 9]

The authors showed that the sinusoidal position embedding approach does not enable transformers to extrapolate to inputs longer than the ones they were trained on. They then established that extrapolation in transformers can be enabled by just changing the position method. They showed that ALiBi offers an extremely simple replacement for existing position approaches and allows models to extrapolate. In addition, when not extrapolating, ALiBi achieves either better perplexity than the sinusoidal method (in models smaller than 1B parameters, trained on less data) or similar perplexity (in larger, billion parameter models trained on much more data). ALiBi is simple to implement and does not slow down runtime or require extra parameters (but does occasionally require a negligible amount of extra memory). Using their method, they sped up the training of a 1.3 billion parameter model evaluated on the same input sequence length as GPT-3 (2048). [p. 9]
