# B Experimental Setup [p. 12]

## B.1 Data Preprocessing [p. 12]

- Sentences encoded using byte-pair encoding (Sennrich et al., 2016), with source and target vocabularies of about 32000 tokens. [p. 12]
- For OpenSubtitles data, only sentence pairs with a relative time overlap of subtitle frames between source and target language subtitles of at least 0.9 are selected to reduce noise in the data. [p. 12]
- Translation pairs batched together by approximate sequence length. [p. 12]
- Each training batch contained a set of translation pairs containing approximately 16000 source tokens (footnote 10: this can be reached by using several GPUs or by accumulating the gradients for several batches and then making an update). [p. 12]
- A large value of batch size was chosen because Transformer's performance depends heavily on batch size (Popel and Bojar, 2018). [p. 12]

## B.2 Model Parameters [p. 12]

The Transformer base model setup of Vaswani et al. (2017) is followed: [p. 12]

- Number of layers in encoder and decoder: $N = 6$
- Number of parallel attention layers (heads): $h = 8$
- Dimensionality of input and output: $d_{model} = 512$
- Inner-layer of feed-forward networks dimensionality: $d_{ff} = 2048$
- Regularization as described in Vaswani et al. (2017). [p. 12]

## B.3 Optimizer [p. 12]

The optimizer is the same as in Vaswani et al. (2017): Adam (Kingma and Ba, 2015) with $\beta_1 = 0.9$, $\beta_2 = 0.98$ and $\varepsilon = 10^{-9}$. [p. 12]

Learning rate varies over the course of training according to the formula: [p. 12]

$$l_{rate} = scale \cdot \min(step\_num^{-0.5},\ step\_num \cdot warmup\_steps^{-1.5})$$

Hyperparameters: $warmup\_steps = 16000$, $scale = 4$. [p. 12]
