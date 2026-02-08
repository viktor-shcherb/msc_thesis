# 2 Current Approaches Do Not Extrapolate Efficiently [p. 2-4]

[p. 2]

The authors show for the first time that the sinusoidal position method, which technically should be able to extrapolate, in practice has very limited extrapolation capabilities. Though the rotary position method improves over the sinusoidal one, it still does not achieve satisfying results. Holding everything else constant, they are the first to observe that the T5 bias method leads to better extrapolation than either of these, and so they conclude that extrapolation ability depends heavily on the position embedding. Unfortunately, the T5 bias is computationally costly (Figure 2). [p. 2]

## 2.1 Background and Experimental Setup [p. 2-3]

[p. 2-3]

**Nonoverlapping Inference.** To train on or evaluate a sequence longer than $L$ tokens, it is typical to segment the sequence into $L$-length subsequences and train on or evaluate them independently. Unless otherwise stated, nonoverlapping inference is used to report perplexity scores. [p. 2-3]

**Extrapolation During Inference.** Formally, the functions that define a transformer layer are agnostic to input length: they map from some arbitrary, unfixed number of input vectors to the same number of output vectors. When transformers are applied to sequential data, positional information is injected into the inputs in various ways. [p. 3]

Vaswani et al. (2017) discussed two options for embedding positions into vectors to be added to word embeddings: learning embeddings for specific positions and unlearned sinusoidal embeddings. They observed similar performance between the two but preferred the sinusoidal approach, which they argued might extrapolate to longer input sequences during inference. The authors find that this model cannot extrapolate to more than a few dozen tokens beyond $L$. [p. 3]

Note (footnote 3): The functions agnostic to input length include the embedding lookup, feedforward sublayer, and softmax layer, which act independently on vector inputs, as well as the attention sublayers, whose parameters do not depend on input length (and which must handle variable-length inputs, e.g., due to causal masking). [p. 3]

Note (footnote 4): The learned positional embedding approach does not have a way to encode positions greater than $L$; it therefore has no ability to extrapolate. [p. 3]

A transformer LM receives a list of tokens and outputs a probability distribution representing its prediction for the next token. The input list is called the *current input subsequence* since the inputs to language models are typically subsequences from (much longer) training or evaluation sequences. During both training and perplexity evaluation (scoring a fixed sequence), many predictions can be calculated at once; this is done using a "causal mask" that ensures each position's prediction is influenced only by tokens to its left. Let $L$ be the length of each input subsequence during training; it includes $L$ predictions, which on average have access to $\frac{L+1}{2}$ tokens of (left) context. To explore a model's extrapolation abilities, sequences of length $L_{valid} > L$ are considered at evaluation time. When $L$ differs between inference and training, $L$ refers to the length of subsequences during training and $L_{valid}$ refers to their length at validation. [p. 2]

**Experiment Setup.** The extrapolation abilities of various position methods are tested on the WikiText-103 corpus (Merity et al., 2016) using the transformer language model of Baevski & Auli (2018). This model is used because of its prominent role in recent language modeling developments (Khandelwal et al., 2020; Press et al., 2021). [p. 3]

Model and training details:
- Training set: ~103 million tokens from English Wikipedia (half a gigabyte)
- Architecture: 16 transformer layers, dimension 1024, 8 heads, feedforward inner dimension 4096
- Ties word embedding and softmax matrices (Press & Wolf, 2017; Inan et al., 2017)
- Only varying: position method and training subsequence length
- All other hyperparameters unchanged, including the random seed and number of training epochs (205) [p. 3]

## Figure 2

**Figure 2** (p. 3): "A comparison of batched training, inference speed and memory use of the sinusoidal, rotary, T5 bias, and our ALiBi position methods. The speed differences between our method and the sinusoidal are within 1% during training and 3% for inference, which is insignificant on our hardware. ALiBi uses 100MB of extra memory when training on input lengths 1024 and 3072 in this setting. Memory usage is lower in all approaches when training on 3072 tokens (compared to 1024) since we break batches into multiple updates. See Table 1 in the appendix for exact numbers."

Three bar charts side by side:
- **Left:** "Training Speed" (y-axis: WPS, up to 30k; x-axis: Input Length 512, 1024, 3072). Sinusoidal, Rotary, T5 Bias, ALiBi shown. T5 Bias is noticeably slower than the other three, which are approximately equal. At input length 512, all except T5 Bias are around 25-30k WPS; T5 Bias is around 14-15k.
- **Middle:** "Inference Speed" (y-axis: WPS, up to 100k; x-axis: Input Length 512, 1024, 3072). Similar pattern: T5 Bias is slower; others are comparable.
- **Right:** "Training Memory" (y-axis: GB, up to 30; x-axis: Input Length 512, 1024, 3072). All methods use similar memory, with T5 Bias slightly higher. At 3072 tokens, memory usage drops for all methods due to batch splitting.

## 2.2 Measuring Extrapolation [p. 3-4]

### Sinusoidal Position Embeddings [p. 3-4]

[p. 3]

Sinusoidal position embeddings (Vaswani et al., 2017, Section 3.5) are constant, non-learned vectors added to token embeddings on input to the first layer of the transformer. They are frequently used in transformer language modeling (Baevski & Auli, 2018; Lewis et al., 2021) and machine translation (Vaswani et al., 2017; Ott et al., 2018) models. [p. 3]

The unmodified model of Baevski & Auli (2018) uses sinusoidal position embeddings and is trained on $L = 512$ tokens; inference is then run on the validation set on $L + k$ tokens, with $k$ ranging from 0 to 15,000. Figure 1 (left) and the corresponding Table 2 (in the appendix) show that while the model improves perplexity up to $k = 20$, performance stops improving and stays steady from $k = 20$ to $k = 50$ and then begins degrading. Similar results are obtained for a model trained with $L = 1024$ tokens (Figure 1, right, and Table 3 in the appendix). That model improves for up to $L_{valid} = L + 50$ tokens, after which performance declines. [p. 3]

### Rotary Position Embeddings [p. 4]

[p. 4]

The rotary method was introduced by Su et al. (2021) and has recently been popularized by the open source GPT-3 (Brown et al., 2020) implementation GPT-J (Wang & Komatsuzaki, 2021). Instead of adding sinusoidal embeddings at the bottom of the transformer, it multiplies the keys and queries of every attention layer by sinusoidal embeddings. [p. 4]

Unlike the sinusoidal or learned positional embedding approach, the rotary method injects position information into the model at every layer, not just at the initial one. In addition, it adds no position information to the values of the self-attention sublayer. The output of a self-attention sublayer is a linearly transformed, weighted sum of the input value vectors; therefore, by not inserting position information into the values, the outputs of each transformer-layer contain no explicit position information. The authors suspect that this segregation of position information may be beneficial for extrapolation, and draw inspiration from it in the design of their method (Section 3). [p. 4]

The rotary position embedding method is applied to the Baevski & Auli baseline. The perplexity results (Figure 1 and Appendix Tables 2 and 3) are better than the sinusoidal approach: the model with $L = 512$ ($L = 1024$) improves perplexity with up to $k = 200$ ($k = 100$) more tokens than it saw during training, but this comes at the cost of slower training and inference (Figure 2). [p. 4]

Note (footnote 5): The rotary method implementation is based on the code at https://github.com/JunnYu/RoFormer_pytorch, linked to the official repository of Su et al. (2021) (https://github.com/ZhuiyiTechnology/roformer). After finishing experiments, the authors were informed that the runtime of the code could be optimized, making it only 2% slower than the sinusoidal approach. This optimization would not change extrapolation performance. [p. 4]

### T5 Bias [p. 4]

[p. 4]

Though most models use trained or sinusoidal position embeddings, the T5 model of Raffel et al. (2020) uses a relative position method (Shaw et al., 2018; Huang et al., 2019) that adds no position information to word embeddings (as in the previous method). Instead, it modifies the way attention values are computed. This is referred to as the "T5 bias" method. [p. 4]

In the unmodified transformer, attention values are computed by taking the dot product of every query with every relevant key and then applying softmax. In the T5 bias method, a learned, shared bias is added to each query-key score that is dependent on just the distance between the query and key. Therefore:
- All query-key scores where distance is zero (same token) get a specific learned bias
- Scores where query and key are one word away get a different learned bias
- Up to a certain point, beyond which multiple different distances share the same learned bias (which might be beneficial for extrapolation) [p. 4]

As in the rotary method, the T5 bias injects position information into the model at every layer and integrates no explicit position information into the self-attention value vectors. [p. 4]

Raffel et al. (2020) propose that the T5 bias may allow extrapolation, but they did not report experiments testing this. The authors show that the T5 bias does allow language models to extrapolate, by modifying the Baevski & Auli model to insert the T5 bias. [p. 4]

As Figure 1 shows, the T5 bias improves perplexity with longer sequences than the ones it was trained on, i.e., $k = 600$ ($k = 800$) extra tokens for a model trained on $L = 512$ ($L = 1024$) input tokens. Unfortunately, this impressive performance comes at a cost: training is at least twice as slow as with the sinusoidal model. Therefore, this model's extrapolation ability provides no efficiency advantage. For example, to do inference on 1024 tokens, one could either train the sinusoidal model with $L = 1024$ or train the T5 bias model on $L = 512$ tokens and extrapolate to 1024 for inference. However, the $L = 1024$ sinusoidal model runs at 28.5k words per second (WPS), while the $L = 512$ T5 bias model runs at 14.4k WPS (Appendix Table 1), so there is no speedup when training on shorter sequences with this method. [p. 4]

Note (footnote 6): The T5 bias method is similar to the one used in Parikh et al. (2016, Equation 7). [p. 4]

Note (footnote 7): The T5 bias implementation is based on the one used in HuggingFace Transformers (Wolf et al., 2020), which in turn is based on the official Mesh Tensorflow T5 code. [p. 4]

Note (footnote 8): Narang et al. (2021) benchmarked the T5 bias as being just 8.7% slower than the sinusoidal approach; thus, while always incurring a runtime penalty, this method's runtime could be faster depending on the choice of hardware and software frameworks used. Narang et al. used the Tensorflow T5 library running on TPUs, while the authors used the PyTorch Fairseq library running on GPUs. [p. 4]
