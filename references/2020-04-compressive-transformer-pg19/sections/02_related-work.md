# 2 Related Work [p. 2]

## Convolution-like approaches

Wu et al. (2019) show that a convolution-like operator that runs in linear time can actually exceed the performance of the quadratic-time self-attention layer in the Transformer at sentence-to-sentence translation and sentence-level language modelling. However such a mechanism inhibits the flow of information across a large number of time-steps for a given layer, and has not shown to be beneficial for long-range sequence modelling.

## TransformerXL

Dai et al. (2019) propose the TransformerXL, which keeps past activations around in memory. They also propose a novel relative positional embedding scheme which they see outperforms the Transformer's original absolute positional system. The Compressive Transformer incorporates both of these ideas: the use of a memory to preserve prior activations and their relative positional embedding scheme.

## Sparse Transformer

The Sparse Transformer (Child et al., 2019) uses fixed sparse attention masks to attend to roughly sqrt(n) locations in memory. This approach still requires keeping all memories around during training; however with careful re-materialization of activations and custom kernels, the authors are able to train the model with a reasonable budget of memory and compute. When run on Enwik8, the much larger attention window of 8,000 improves model performance, but overall it does not significantly outperform a simpler TransformerXL with a much smaller attention window.

## Adaptive attention spans

The use of dynamic attention spans is explored in Sukhbaatar et al. (2019). Different attention heads can learn to have shorter or longer spans of attention -- and they observe this achieves state-of-the-art in character-based language modelling. This idea could easily be combined with the Compressive Transformer's contribution -- a compressive memory. However an efficient implementation is not possible on current dense-linear-algebra accelerators, such as Google's TPUs, due to the need for dynamic and sparse computation. The Compressive Transformer builds on simple dense linear algebra components, such as convolutions.
