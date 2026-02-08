# Appendix E: Machine Translation - Experimental Details [p. 17–18]

## Model Architecture for Single Language Pair MoE Models

[p. 17] The model is a modified version of the GNMT model described in (Wu et al., 2016). To reduce computation, the number of LSTM layers in the encoder and decoder is decreased from 9 and 8 to 3 and 2 respectively. MoE layers are inserted in both the encoder (between layers 2 and 3) and the decoder (between layers 1 and 2). An attention mechanism is used between the encoder and decoder, with the first decoder LSTM receiving output from and providing input for the attention.^5 All of the layers in the model have input and output dimensionality of 512. The LSTM layers have 2048 hidden units, with a 512-dimensional output projection. Residual connections are added around all LSTM layers and MoE layers to encourage gradient flow (He et al., 2015). Similar to GNMT, to effectively deal with rare words, sub-word units (also known as "wordpieces") (Schuster & Nakajima, 2012) are used for inputs and outputs.

A shared source and target vocabulary of 32K wordpieces is used. The same beam search technique as proposed in (Wu et al., 2016) is also used.

Models are trained with different numbers of experts in the MoE layers. In addition to a baseline model with no MoE layers, models are trained with flat MoE layers containing 32 experts, and models with hierarchical MoE layers containing 512 and 2048 experts. The flat MoE layers use k = 4 and the hierarchical MoE models use k = 2 at each level of the gating network. Thus, each input is processed by exactly 4 experts in each MoE layer. Each expert in the MoE layer is a feed forward network with one hidden layer of size 2048 and ReLU activation. Thus, each expert contains [512 * 2048] + [2048 * 512] = 2M parameters. The output of the MoE layer is passed through a sigmoid function. The strictly-balanced gating function described in Appendix F is used.

## Model Architecture for Multilingual MoE Model

[p. 17] The same model architecture is used as for the single-language-pair models, with the following exceptions: noisy-top-k gating as described in Section 2.1 is used, not the scheme from Appendix F. The MoE layers in the encoder and decoder are non-hierarchical MoEs with n = 512 experts, and k = 2. Each expert has a larger hidden layer of size 8192. This doubles the amount of computation in the MoE layers, raising the computational budget of the entire model from 85M to 102M ops/timestep.

## Training

[p. 17] Networks are trained using the Adam optimizer (Kingma & Ba, 2015). The base learning rate was increased linearly for the first 2000 training steps, held constant for an additional 8000 steps, and decreased after that so as to be proportional to the inverse square root of the step number. For the single-language-pair models, similarly to (Wu et al., 2016), dropout (Zaremba et al., 2014) is applied to the output of all embedding, LSTM and MoE layers, using DropProb = 0.4. Training was done synchronously on a cluster of up to 64 GPUs as described in Section 3. Each training batch consisted of a set of sentence pairs containing roughly 16000 words per GPU.

To ensure balanced expert utilization, w_importance = 0.01 and w_load = 0.01, as described in Section 4 and Appendix A.

## Metrics

[p. 17] Models are evaluated using the perplexity and the standard BLEU score metric. Tokenized BLEU score as computed by the multi-bleu.pl script is reported, downloaded from the public implementation of Moses (on Github), which was also used in (Luong et al., 2015a).

**Footnote 5** [p. 17]: For performance reasons, a slightly different attention function from the one described in (Wu et al., 2016) is used — See Appendix G.

## Results

[p. 18] Tables 2, 3 and 4 in Section 5.3 show comparisons of the results to other published methods. Figure 4 shows test perplexity as a function of number of words in the (training data's) source sentences processed for models with different numbers of experts. As the number of experts is increased to approach 2048, the test perplexity of the model continues to improve.

**Figure 4** (p. 18): "Perplexity on WMT'14 En->Fr (left) and Google Production En->Fr (right) datasets as a function of number of words processed. The large differences between models at the beginning of training are due to different batch sizes. All models incur the same computational budget (85M ops/timestep) except the one with no experts."
- Left plot (WMT'14 En->Fr): x-axis "Number of source words processed" (0 to ~10^9), y-axis "Perplexity" (~2.0 to 6.0). Four series: #Experts=0 (green, highest perplexity ~3.0 final), #Experts=32 (red, ~2.8 final), #Experts=512 (blue, ~2.7 final), #Experts=2048 (green dashed, lowest ~2.6 final). All curves decrease over training; more experts yield lower perplexity.
- Right plot (Google Production En->Fr): x-axis "Number of source words processed" (0 to ~1.4*10^9), y-axis "Perplexity" (~2.0 to 8.0). Same four series. #Experts=0 settles around ~3, #Experts=32 ~2.8, #Experts=512 ~2.7, #Experts=2048 lowest ~2.6. Similar trend with more training data.

## Expert Specialization

[p. 18] The experts become highly specialized by syntax and/or semantics, as can be seen in Table 9. For example, one expert is used when the indefinite article "a" introduces the direct object in a verb phrase indicating importance or leadership.

**Table 9** (p. 18): Contexts corresponding to a few of the 2048 experts in the MoE layer in the encoder portion of the WMT'14 En->Fr translation model. For each expert i, the inputs in a training batch are sorted in decreasing order of G(x)_i, and the words surrounding the corresponding positions in the input sentences are shown.

| Expert 381 | Expert 752 | Expert 2004 |
|---|---|---|
| ... with **researchers** , ... | ... plays **a** core ... | ... with **rapidly** growing ... |
| ... to **innovation** . | ... plays **a** critical ... | ... under **static** conditions ... |
| ... tics **researchers** . | ... provides **a** legislative ... | ... to **swift** ly ... |
| ... the **generation** of ... | ... play **a** leading ... | ... to **dras** tically ... |
| ... technology **innovations** is ... | ... assume **a** leadership ... | ... the **rapid** and ... |
| ... technological **innovations** , ... | ... plays **a** central ... | ... the **fast** est ... |
| ... support **innovation** throughout ... | ... established **a** reconciliation ... | ... the **Quick** Method ... |
| ... role **innovation** will ... | ... taken **a** leading ... | ... **rec** urrent ) ... |
| ... research **scienti** st ... | ... played **a** vital ... | ... provides **quick** access ... |
| ... promoting **innovation** where ... | ... have **a** central ... | ... of **volatile** organic ... |
| ... | ... | ... |
