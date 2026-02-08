# 5 Experiments [p. 6]

[p. 6] All models were optimised with Adam (Kingma and Ba, 2014). Learning rate schedule: linear warmup from 1e-6 to 3e-4 and a cosine decay back down to 1e-6. For character-based LM: 4,000 warmup steps with 100,000 decay steps. For word-based LM: 16,000 warmup steps with 500,000 decay steps. The authors found that decreasing the optimisation update frequency helped (see Section 5.5.1), namely they only applied parameter updates every 4 steps after 60,000 iterations. However they found the models would optimise well for a range of warmup/warmdown values. They clipped the gradients to have a norm of at most 0.1, which was crucial to successful optimisation.

## 5.1 PG-19 [p. 6]

The Compressive Transformer is benchmarked against the TransformerXL on the newly proposed PG-19 books dataset. Because it is open-vocabulary, a subword vocabulary of size 32000 with SubwordTextEncoder from the tfds package in TensorFlow is trained and dataset statistics are used to compute word-level perplexity, as described in Section 4.2.

Model details:
- 36 layer Compressive Transformer with window size of 512, both memory and compressed memory size of 512, and compression rate C = 2
- Compared to a 36 layer TransformerXL trained with window size 512 and attention window 1024
- Trained on 256 TPUv3 cores with a total batch size of 512
- Converged after processing around 100 billion subword tokens

**Table 3** (p. 6): Eval. perplexities on PG-19.

| Model | Valid. | Test |
|---|---|---|
| 36L TransformerXL | 45.5 | 36.3 |
| **36L Compressive Transf.** | **43.4** | **33.6** |

The Compressive Transformer obtains a test perplexity of 33.6 versus the TransformerXL's 36.3. Despite the dataset size, it is clearly a challenging domain. The model is able to generate long-form narrative of varying styles: from character dialogue, first person diary entries, to descriptive third-person text. Samples are shown in Supplementary Section E.

## 5.2 Enwik8 [p. 6]

The TransformerXL and the Compressive Transformer are compared on the standard character-level language modelling benchmark Enwik8 taken from the Hutter Prize (Hutter, 2012), which contains 100M bytes of unprocessed Wikipedia text. First 90MB for training, 5MB for validation, and latter 5MB for testing -- as per convention.

Model details:
- 24-layer models with a sequence window size of 768
- TransformerXL memory size: 2304
- Compressive Transformer memory size: 768, compressed memory size: 1152

**Table 4** (p. 6): State-of-the-art results on Enwik8.

| Model | BPC |
|---|---|
| 7L LSTM (Graves, 2013) | 1.67 |
| LN HyperNetworks (Ha et al., 2016) | 1.34 |
| LN HM-LSTM (Chung et al., 2016) | 1.32 |
| ByteNet (Kalchbrenner et al., 2016) | 1.31 |
| RHN (Zilly et al., 2017) | 1.27 |
| mLSTM (Krause et al., 2016) | 1.24 |
| 64L Transf. (Al-Rfou et al., 2019) | 1.06 |
| 24L TXL (Dai et al., 2019) | 0.99 |
| Sparse Transf. (Child et al., 2019) | 0.991 |
| Adaptive Transf. (Sukhbaatar et al., 2019) | 0.98 |
| *24L TXL (ours)* | 0.98 |
| **24L Compressive Transformer** | **0.97** |

**Table 5** (p. 6): Compression approaches on Enwik8.

| Compression fn | Compression loss | BPC |
|---|---|---|
| Conv | BPTT | 0.996 |
| Max Pooling | N/A | 0.986 |
| Conv | Auto-encoding | 0.984 |
| Mean Pooling | N/A | 0.982 |
| Most-used | N/A | 0.980 |
| Dilated conv | Attention | 0.977 |
| Conv | Attention | **0.973** |

---
[p. 7 continued]

Compression rate C = 3. During evaluation, the TransformerXL memory size was increased to 4096 and the Compressive Transformer's compressed memory to 3072 (after sweeping over the validation set), obtaining the numbers reported in Table 4. The effect of scaling the compressed memory size and evaluation performance is shown in Supplementary Section B. The proposed model achieves the new state-of-the-art on this dataset with 0.97 bits-per-character.

Compression functions and auxiliary losses are compared in Table 5. The authors sweep over compression rates of 2, 3, and 4 and report results with the best performing value for each row. BPTT signifies that no auxiliary compression loss was used to train the network other than the overall training loss. To feed gradients into the compression function they unrolled the model over double the sequence length and halved the batch size to fit the larger unroll into memory.

## 5.3 WikiText-103 [p. 7]

An eighteen-layered Compressive Transformer is trained on the closed-vocabulary word-level language modelling benchmark WikiText-103, which contains articles from Wikipedia. The model is trained with a compressed memory size, memory size, and a sequence window size all equal to 512. Trained over 64 Tensor Processing Units (TPU) v3 with a batch size of 2 per core -- making for a total batch size of 128. The model converged in a little over 12 hours. The single-layer convolution worked best, with a compression rate of c = 4. This model obtained 17.6 perplexity on the test set. By tuning the memory size over the validation set -- setting the memory size to 500, and compressed memory size to 1,500 -- they obtain 17.1 perplexity. This is 1.2 perplexity points over prior state of the art, and means the model places a ~5% higher probability on the correct word over the prior SotA TransformerXL.

**Table 6** (p. 8): Validation and test perplexities on WikiText-103.

| Model | Valid. | Test |
|---|---|---|
| LSTM (Graves et al., 2014) | - | 48.7 |
| Temporal CNN (Bai et al., 2018a) | - | 45.2 |
| GCNN-14 (Dauphin et al., 2016) | - | 37.2 |
| Quasi-RNN (Bradbury et al., 2016) | 32 | 33 |
| RMC (Santoro et al., 2018) | 30.8 | 31.9 |
| LSTM+Hebb. (Rae et al., 2018) | 29.0 | 29.2 |
| Transformer (Baevski and Auli, 2019) | - | 18.7 |
| 18L TransformerXL, M=384 (Dai et al., 2019) | - | 18.3 |
| *18L TransformerXL, M=1024 (ours)* | - | 18.1 |
| **18L Compressive Transformer, M=1024** | **16.0** | **17.1** |

[p. 7] In Table 6 the authors do not list methods that use additional training data, or that make use of test-time labels to continue training the model on the test set (known as dynamic evaluation from Graves (2013)). If a very naive dynamic evaluation approach is incorporated (loading a model checkpoint and continuing training over one epoch of the test set), they obtain a test perplexity of **16.1**. This is slightly better than the published 16.4 from Krause et al. (2019) -- which uses a more sophisticated dynamic evaluation approach on top of the TransformerXL. However in most settings, one does not have access to test-time labels, and thus the authors do not focus on this setting.

> "Furthermore there has been great progress in showing that more data equates to much better language modelling; Shoeybi et al. (2019) find a large transformer 8B-parameter transformer trained on 170GB of text obtains 10.7 word-level perplexity on WikiText-103. However it is not clear to what extent the WikiText-103 test set may be leaked inside these larger training corpora." [p. 7]

**Table 7** (p. 8): WikiText-103 test perplexity broken down by word frequency buckets. The most frequent bucket is words which appear in the training set more than 10,000 times, displayed on the left. For reference, a uniform model would have perplexity |V| = 2.6e5 for all frequency buckets. *LSTM comparison from Rae et al. (2018).

| Model | > 10K | 1K-10K | 100-1K | < 100 | All |
|---|---|---|---|---|---|
| LSTM* | 12.1 | 219 | 1,197 | 9,725 | 36.4 |
| TransformerXL (ours) | 7.8 | 61.2 | 188 | 1,123 | 18.1 |
| Compressive Transformer | **7.6** | **55.9** | **158** | **937** | **17.1** |
| Relative gain over TXL | 2.6% | 9.5% | 21% | 19.9% | 5.8% |

[p. 7-8] The Compressive Transformer makes only a small modelling improvement for frequent words (2.6% over the TransformerXL baseline) but obtains a much larger improvement of ~20% for infrequent words. Furthermore, the authors see **10X improvement** in modelling rare words over the prior state-of-the-art LSTM language model published in 2018 -- which demonstrates the rate of progress in this area.

## 5.4 Compressibility of Layers [p. 7]

[p. 7] Compression is used to better understand the model's mode of operation. The authors inspect how compressible the Compressive Transformer's activations are as they progress through higher layers in the network. One may expect representations to become more difficult to compress at higher layers, if more semantic information is represented there. The compression loss at each layer is monitored for the best-performing Compressive Transformer models trained on Enwik8 and WikiText-103 and displayed in Supplementary Section A, Figure 6.

Key findings:
- The compression loss is about one order of magnitude higher for word-level language modelling (WikiText-103) over character-level language modelling (Enwik8).
- The first layer of the Transformer is highly compressible.
- There is not a clear trend of compression cost increasing with layer depth.

## 5.5 Attention [p. 8]

[p. 8] The authors inspect where the network is attending to on average, to determine whether it is using its compressed memory. They average the attention weight over a sample of 20,000 sequences from a trained model on Enwik8. The attention is aggregated into eighteen buckets, six for each of the compressed memory, memory, and sequence respectively. The size of the sequence, memory and compressed memory are all set to be 768. The average attention weight per bucket is plotted in Figure 2 with a 1-sigma standard error.

**Figure 2** (p. 9): "Attention weight on Enwik8. Average attention weight from the sequence over the compressed memory (oldest), memory, and sequence (newest) respectively. The sequence self-attention is causally masked, so more attention is placed on earlier elements in the sequence. There is an increase in attention at the transition from memory to compressed memory."

The figure shows 18 buckets on the x-axis (1-18: 1-6 compressed memory, 7-12 memory, 13-18 sequence) and average attention weight on the y-axis (0.00-0.14). Most attention is placed on the current sequence (buckets 13-18), with greater weight on earlier elements due to the causal self-attention mechanism. There is also an observable *increase* in attention from the oldest activations stored in the regular memory to the activations stored in the compressed memory.

> "This goes against the trend of older memories being accessed less frequently -- and gives evidence that the network is learning to preserve salient information." [p. 8]

## 5.5.1 Optimisation Schedule [p. 8-9]

[p. 8-9] The authors observe an interesting but undesirable meta-learning phenomenon during long-context training. When the learning rate is tuned to be much smaller (or set to zero) during training, performance degrades drastically both for the TransformerXL and the Compressive Transformer.

**Figure 3** (p. 9): "Learning rate analysis. Reducing the learning rate (e.g. to zero) during training (on Enwik8) harms training performance. Reducing the frequency of optimisation updates (effectively increasing the batch size) is preferable."

The figure shows training iterations (5000-25000) on the x-axis and training BPC (0.7-1.2) on the y-axis. Multiple curves correspond to different learning rates (0.0, 1e-9, 1e-7, 3e-4) and a curve with 3e-4 update period=2. The curve where learning rate is changed to 0 during training shows BPC increasing (degrading). The reduced update frequency (period=2) curve tracks the full-rate 3e-4 curve closely.

[p. 8-9] Usually one considers distributional shift from the training data to the test data, but the authors also observe a shift in the model when transferring from training to evaluation mode (even when the model is evaluated on the training data). This is due to the online updating of parameters whilst processing long contiguous articles. The authors would like the model to generalise well to scenarios where it is not continuously optimised. Updating the parameters only at article boundaries (and then resetting the state) could be one solution for long-range memory models, but this would slow down learning significantly.

Instead, the authors propose reducing the frequency of optimisation updates during training. This allows for the best of both worlds -- fast initial learning with frequent updates, and better generalisation near the end of training with less frequent updates (e.g. every 4 steps). Reducing the optimisation frequency increases the effective batch size, which has also been shown to be preferable to learning rate decay in image modelling (Smith et al., 2018).

[p. 9] The authors observed a final performance improvement in their TransformerXL baseline on Enwik8, from 0.995 -- which approximately replicates the published result -- to 0.984 -- which matches the most recent SotA architecture. The additional space and compute cost of accumulating gradients is negligible across iterations, so there was no performance regression in using this scheme.

## 5.6 Speech [p. 9]

[p. 9] The Compressive Transformer is trained on the waveform of speech to assess its performance on different modalities. Speech is interesting because it is sampled at an incredibly high frequency, but it contains a lot of information on the level of phonemes and entire phrases.

To encourage long-term reasoning, the authors refrain from conditioning the model on speaker identity or text features, and focus on unconditional speech modelling. Training details:
- Data: 24.6 hours of 24kHz North American speech data
- Sequences chunked into windows of size 3840, roughly 80ms of audio
- 20-layer Compressive Transformer compared to a 20-layer TransformerXL and a 30-layer WaveNet model (Oord et al., 2016) -- a state-of-the-art audio generative model used to serve production speech synthesis applications at Google (Oord et al., 2018)
- All networks have approximately 40M parameters, as WaveNet is more parameter-efficient per layer
- Trained on 32 V100 GPUs, batch size of 1 per core (total batch size of 32) using synchronous training

WaveNet processes an entire chunk in parallel, however the TransformerXL and Compressive Transformer are trained with a window size of 768 and a total memory size of 1,568 (for the Compressive Transformer: 768 memory + 768 compressed). The model is unrolled over the sequence. Despite this sequential unroll, the attention-based models train at only half the speed of WaveNet.

**Figure 4** (p. 10): "Speech Modelling. We see the Compressive Transformer is able to obtain competitive results against the state-of-the-art WaveNet in the modelling of raw speech sampled at 24kHz."

The figure shows training iterations (0-400,000) on the x-axis and test NLL on the y-axis (~1.80-1.88). Three curves: Compressive Transformer 20L C=4 (green), TransformerXL 20L (red), Wavenet 30L (blue). The Compressive Transformer with compression rate 4 is able to outperform the TransformerXL and maintain a slim advantage over WaveNet. However the models were only trained for at most one week (with 32 GPUs) and it would be advantageous to continue training until full convergence before definitive conclusions are made.

## 5.7 Reinforcement Learning [p. 9-10]

[p. 9-10] Compression is a good fit for video input sequences because subsequent frames have high mutual information. The authors do not test the Compressive Transformer on video directly, but progress straight to a reinforcement learning agent task that receives a video stream of visual observations -- but must ultimately learn to use its memory to reason over a policy.

The Compressive Transformer is tested as a drop-in replacement for an LSTM in the IMPALA setup (Espeholt et al., 2018). Otherwise, the same training framework and agent architecture are used as described in the original work with a fixed learning rate of 1.5e-5 and entropy cost coefficient of 2e-3.

The Compressive Transformer is tested on a challenging memory task within the DMLab-30 (Beattie et al., 2016) domain, *rooms_select_nonmatching_object*. This requires the agent to explore a room in a visually rich 3D environment and remember the object present. The agent can then advance to a second room where it must select the object *not present* in the original room. This necessitates that the agent both remember events far in the past, and also learn to efficiently reason about them.

Both the memory and compressed memory sizes are fixed to 64. Results are presented for a range of compression rates, averaged over 3 seeds.

**Figure 5** (p. 10): "Vision and RL. We see the Compressive Transformer integrates visual information across time within an IMPALA RL agent, trained on an object matching task."

The figure shows frames (0.0-1.0, x1e9) on the x-axis and human normalised score (0-100) on the y-axis. Five curves correspond to compression rates 1, 2, 4, and 8. The best performing agents endowed with the Compressive Transformer are able to solve the task to human-level. The model with compression rate 1 is unable to learn the task to the same proficiency. The speed of learning and stability seem to increase proportionally with higher rates of compression (up to a limit) -- i.e. the effective memory window of the agent -- and compression rate 4 is found to once again be the best performing. The authors see this as a promising sign that the architecture is able to efficiently learn and suitably use compressed representations of its visual input.
