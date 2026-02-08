# 1. Introduction [p. 3-4]

[p. 3]

Large scale training has been an effective path towards flexible and powerful neural language models (Radford et al., 2018; Kaplan et al., 2020; Brown et al., 2020). Simple architectures---backed by a generous computational budget, data set size and parameter count---surpass more complicated algorithms (Sutton, 2019). This approach, followed in Radford et al. (2018); Raffel et al. (2019); Brown et al. (2020), expands the model size of a densely-activated Transformer (Vaswani et al., 2017). While effective, it is also extremely computationally intensive (Strubell et al., 2019).

Inspired by the success of model scale but seeking greater computational efficiency, the authors propose a *sparsely-activated* expert model: the Switch Transformer. The sparsity comes from activating a *subset* of the neural network weights for each incoming example.

**Figure 1** (p. 3): "Scaling and sample efficiency of Switch Transformers. Left Plot: Scaling properties for increasingly sparse (more experts) Switch Transformers. Right Plot: Negative log perplexity comparing Switch Transformers to T5 (Raffel et al., 2019) models using the same compute budget."

- Left plot: x-axis is "Sparse Model Parameters" (log scale, from 10^9 to 10^10), y-axis is "Test Loss" (ranging from ~4.8 to ~6.2). Data points labeled 1e, 2e, 4e, 8e, 16e, 32e, 64e, 128e, 256e show a smooth decrease in test loss as the number of experts (and thus sparse parameters) increases.
- Right plot: x-axis is "Training Step" (0 to 5 x 10^5), y-axis is "Neg Log Perplexity" (from -2.0 to -1.2). Lines for Switch-Base: 128e, 64e, 32e, 16e, and T5-Base are shown. All Switch-Base models achieve better (more negative) log perplexity than the T5-Base, with more experts yielding better performance. Switch-Base: 128e reaches roughly -2.0 while T5-Base reaches roughly -1.5.

Sparse training is an active area of research and engineering (Gray et al., 2017; Gale et al., 2020), but machine learning libraries and hardware accelerators still cater to dense matrix multiplications. The authors start with the Mixture-of-Expert (MoE) paradigm (Jacobs et al., 1991; Jordan and Jacobs, 1994; Shazeer et al., 2017), and simplify it to yield training stability and computational benefits. MoE models have had notable successes in machine translation (Shazeer et al., 2017, 2018; Lepikhin et al., 2020), however, widespread adoption is hindered by complexity, communication costs, and training instabilities.

The authors address these issues and go beyond translation, finding that these class of algorithms are broadly valuable in natural language. They measure superior scaling on a diverse set of natural language tasks and across three regimes in NLP: pre-training, fine-tuning and multi-task training. While focusing on scale, the Switch Transformer architecture not only excels in the domain of supercomputers, but is beneficial even with only a few computational cores.

[p. 4]

Further, the large sparse models can be distilled (Hinton et al., 2015) into small dense versions while preserving 30% of the sparse model quality gain.

## Contributions

The contributions are listed as follows:

- The Switch Transformer architecture, which simplifies and improves over Mixture of Experts.
- Scaling properties and a benchmark against the strongly tuned T5 model (Raffel et al., 2019) where they measure 7x+ pre-training speedups while still using the same FLOPS per token. The improvements hold even with limited computational resources, using as few as two experts.
- Successful distillation of sparse pre-trained and specialized fine-tuned models into small dense models. Model size reduced by up to 99% while preserving 30% of the quality gains of the large sparse teacher.
- Improved pre-training and fine-tuning techniques: **(1)** selective precision training that enables training with lower bfloat16 precision **(2)** an initialization scheme that allows for scaling to a larger number of experts and **(3)** increased expert regularization that improves sparse model fine-tuning and multi-task training.
- A measurement of the pre-training benefits on multilingual data where they find a universal improvement across all 101 languages and with 91% of languages benefiting from 4x+ speedups over the mT5 baseline (Xue et al., 2020).
- An increase in the scale of neural language models achieved by efficiently combining data, model, and expert-parallelism to create models with up to a trillion parameters. These models improve the pre-training speed of a strongly tuned T5-XXL baseline by 4x.
