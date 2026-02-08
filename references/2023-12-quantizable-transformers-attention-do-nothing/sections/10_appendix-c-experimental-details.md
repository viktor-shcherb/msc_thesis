# C Experimental Details [p. 20–21]

## C.1 BERT

### Fine-tuning on MNLI dataset

[p. 20] The authors use pre-trained checkpoint BERT-base-uncased (109M parameters) from HuggingFace repository. They follow standard fine-tuning practices from [14] and [65]. Each data sequence is tokenized and truncated to the maximum sequence length of 128. Shorter sequences are padded to the same length of 128 using a special [PAD] token. They fine-tune for 3 epochs using Adam [29] with a batch size of 16 and no weight decay. The learning rate is initially set to its maximum value of $2 \cdot 10^{-5}$ and is linearly decayed to zero by the end of fine-tuning.

### Pre-training from scratch

[p. 20–21] The authors follow closely the pre-training procedure from [14]. They concatenate, tokenize, and split the training set into sequences of length 128 (to speed up training and experimentation, they do not fine-tune on longer sequences of 512). They use the masked language modeling objective with the probability of masking $p = 0.15$. They train with a batch size of 256 sequences for $10^6$ steps, using AdamW optimizer [39] with the maximum learning rate of $10^{-4}$, learning rate warm up over the first $10^4$ steps, following by a linear decay to zero by the end of training. They use L2 weight decay of 0.01, L2 gradient norm clipping of 1.0, and dropout probability of 0.1 on all layers. They also use FP16 mixed-precision from HuggingFace Accelerate library [20].

## C.2 OPT Pre-training

[p. 21] To speed up experimentation, the authors train OPT-125m sized model on the concatenation of Wikipedia and BookCorpus (same as BERT pre-training). They train with a batch size of 48 and 4 gradient accumulation steps (which results in the effective batch size of 192), so that they can perform pre-training on a single A100 80GB GPU. They concatenate, tokenize, and split the training set into sequences of length 512 and train for 125000 steps (500000 forward passes).

They use the rest of the hyper-parameters and follow pre-training practices from [74] and [65]. They initialize weights using a normal distribution with zero mean and a standard deviation of 0.006. All bias terms are initialized to zero. They use AdamW optimizer with $(\beta_1, \beta_2) = (0.9, 0.95)$. They use the linear learning rate schedule, warming up from 0 to the maximum value$^\dagger$ of $4 \cdot 10^{-4}$ over the first 2000 steps, following by a linear decay to zero by the end of training. They use L2 weight decay of 0.1, L2 gradient norm clipping of 1.0, and dropout probability of 0.1 on all layers. They also use FP16 mixed-precision from HuggingFace Accelerate library [20].

$^\dagger$ In the authors' experiments, they found this value to perform better compared to the value of $6 \cdot 10^{-4}$ listed in the paper.

> "Note that in our experiments for all model sizes we use the consistent LayerNorm placement *before* the attention block, unlike OPT-350m checkpoint from HuggingFace that places LayerNorm after the attention block." [p. 21]

## C.3 ViT Pre-training

[p. 21] The authors use the model definition for ViT-S/16 and the training pipeline from PyTorch Image models library [64]. All training is done on resolution $224 \times 224$ and $16 \times 16$ patches. For data augmentation, they use RandAugment [10], Mixup [73], CutMix [70], random image cropping [56], horizontal flip, label smoothing $\varepsilon = 0.1$, color jitter 0.4, and random (between bilinear and bicubic) interpolation during training.

They train with a batch size of 512 for 300 epochs, using AdamW optimizer and the L2 weight decay of 0.03. They use the cosine learning rate schedule, warming up from $10^{-6}$ to the maximum value of $10^{-3}$ over the first 20 epochs, followed by a LR decay by a factor of 10 every 30 epochs, until it reaches the minimum value of $10^{-5}$.

## C.4 Quantization Settings

### Weights

[p. 21] In all cases, symmetric uniform quantization of weights is used. Min-max weight quantization is used for all models except the OPT model, for which the MSE estimator was found to perform better in all cases.

### Activations

[p. 21] The authors adopt *static range estimation* approach, which determines quantization parameters for the network by passing a few batches of calibration data through the model before inference. Specifically, they use a running min-max estimator [32], which uses an exponential moving average of the min and max over multiple batches. In all cases, running min-max with 0.9 momentum over 16 batches randomly sampled from respective training sets is used.

For OPT model, the authors also experiment with using 99.99% and 99.999% percentiles instead of actual min and max. They select the best configuration for each experiment (including baseline), based on the model performance. In almost all cases, setting activation quantization ranges using 99.999% percentiles gives the lowest W8A8 perplexity.
