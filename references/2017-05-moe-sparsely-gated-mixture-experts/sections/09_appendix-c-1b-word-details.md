# Appendix C: 1 Billion Word Language Modeling Benchmark - Experimental Details [p. 14-16]

## C.1 8-Million-Operations-per-Timestep Models [p. 14-15]

### Model Architecture

[p. 14] The model consists of five layers: a word embedding layer, a recurrent Long Short-Term Memory (LSTM) layer (Hochreiter & Schmidhuber, 1997; Gers et al., 2000), a MoE layer, a second LSTM layer, and a softmax layer. The dimensionality of the embedding layer, the number of units in each LSTM layer, and the input and output dimensionality of the MoE layer are all equal to 512. For every layer other than the softmax, drouput is applied (Zaremba et al., 2014) to the layer output, dropping each activation with probability DropProb, otherwise dividing by (1 - DropProb). After dropout, the output of the previous layer is added to the layer output. This residual connection encourages gradient flow (He et al., 2015).

### MoE Layer Architecture

[p. 14] Each expert in the MoE layer is a feed forward network with one ReLU-activated hidden layer of size 1024 and an output layer of size 512. Thus, each expert contains [512 * 1024] + [1024 * 512] = 1M parameters. The output of the MoE layer is passed through a sigmoid function before dropout. They varied the number of experts between models, using ordinary MoE layers with 4, 32 and 256 experts and hierarchical MoE layers with 256, 1024 and 4096 experts. They call the resulting models MoE-4, MoE-32, MoE-256, MoE-256-h, MoE-1024-h and MoE-4096-h. For the hierarchical MoE layers, the first level branching factor was 16, corresponding to the number of GPUs in their cluster. They use Noisy-Top-K Gating (see Section 2.1) with k = 4 for the ordinary MoE layers and k = 2 at each level of the hierarchical MoE layers. Thus, each example is processed by exactly 4 experts for a total of 4M ops/timestep. The two LSTM layers contribute 2M ops/timestep each for the desired total of 8M.

### Computationally-Matched Baselines

[p. 15] The MoE-4 model does not employ sparsity, since all 4 experts are always used. In addition, four more computationally-matched baseline models with no sparsity were trained:

- **MoE-1-Wide:** The MoE layer consists of a single "expert" containing one ReLU-activated hidden layer of size 4096.
- **MoE-1-Deep:** The MoE layer consists of a single "expert" containing four ReLU-activated hidden layers, each with size 1024.
- **4xLSTM-512:** The MoE layer is replaced with two additional 512-unit LSTM layers.
- **LSTM-2048-512:** The model contains one 2048-unit LSTM layer (and no MoE). The output of the LSTM is projected down to 512 dimensions (Sak et al., 2014). The next timestep of the LSTM receives the projected output. This is identical to one of the models published in (Jozefowicz et al., 2016). They re-ran it to account for differences in training regimen, and obtained results very similar to the published ones.

### Training

[p. 15] The models were trained on a cluster of 16 K40 GPUs using the synchronous method described in Section 3. Each batch consisted of a set of sentences totaling roughly 300,000 words. In the interest of time, training was limited to 10 epochs (27,000 steps). Training took 12-16 hours for all models, except for MoE-4, which took 18 hours (since all the expert computation was performed on only 4 of 16 GPUs). They used the Adam optimizer (Kingma & Ba, 2015). The base learning rate was increased linearly for the first 1000 training steps, and decreased after that so as to be proportional to the inverse square root of the step number. The Softmax output layer was trained efficiently using importance sampling similarly to the models in (Jozefowicz et al., 2016). For each model, they performed a hyper-parameter search to find the best dropout probability, in increments of 0.1.

[p. 15] To ensure balanced expert utilization they set w_importance = 0.1 and w_load = 0.1, as described in Section 4 and Appendix A.

### Results

[p. 15] The model is evaluated using perplexity on the holdout dataset, used by (Chelba et al., 2013; Jozefowicz et al., 2016). They follow the standard procedure and sum over all the words including the end of sentence symbol. Results are reported in Table 7. For each model, they report the test perplexity, the computational budget, the parameter counts, the value of DropProb, and the computational efficiency.

**Table 7** (p. 15): Model comparison on 1 Billion Word Language Modeling Benchmark. Models marked with * are from (Jozefowicz et al., 2016).

| Model | Test Perplexity 10 epochs | Test Perplexity (final) | ops/timestep (millions) | #Params excluding embed. & softmax (millions) | Total #Params (billions) | DropProb | TFLOPS per GPU (observed) |
|---|---|---|---|---|---|---|---|
| Kneser-Ney 5-gram* | | 67.6 | 0.00001 | | 1.8 | | |
| LSTM-512-512* | | 54.1 | 2.4 | 2.4 | 0.8 | 0.1 | |
| LSTM-1024-512* | | 48.2 | 4.7 | 4.7 | 0.8 | 0.1 | |
| LSTM-2048-512* | 45.0 | 43.7 | 9.4 | 9.4 | 0.8 | 0.1 | 0.61 |
| LSTM-2048-512 | | 44.7 | 9.4 | 9.4 | 0.8 | 0.1 | 1.21 |
| 4xLSTM-512 | | 46.0 | 8.4 | 8.4 | 0.8 | 0.1 | 1.07 |
| MoE-1-Wide | | 46.1 | 8.4 | 8.4 | 0.8 | 0.1 | 1.29 |
| MoE-1-Deep | | 45.7 | 8.4 | 8.4 | 0.8 | 0.1 | 1.29 |
| MoE-4 | 45.0 | | 8.4 | 8.4 | 0.8 | 0.1 | 0.52 |
| MoE-32 | 39.7 | | 8.4 | 37.8 | 0.9 | 0.1 | 0.87 |
| MoE-256 | 35.7 | | 8.6 | 272.9 | 1.1 | 0.1 | 0.81 |
| MoE-256-h | 36.0 | | 8.4 | 272.9 | 1.1 | 0.1 | 0.89 |
| MoE-1024-h | 34.6 | | 8.5 | 1079.0 | 1.9 | 0.2 | 0.90 |
| MoE-4096-h | 34.1 | | 8.9 | 4303.4 | 5.1 | 0.2 | 0.74 |
| 2xLSTM-8192-1024* | 34.7 | 30.6 | 151.0 | 151.0 | 1.8 | 0.25 | 1.09 |
| MoE-34M | 31.3 | | 33.8 | 4313.9 | 6.0 | 0.3 | 1.22 |
| MoE-143M | **28.0** | | 142.7 | 4371.1 | 6.0 | 0.4 | **1.56** |

## C.2 More Expensive Models [p. 16]

[p. 16] Two additional models (MoE-34M and MoE-143M) were trained to investigate the effects of adding more computation in the presence of a large MoE layer. These models have computation budgets of 34M and 143M ops/timestep. Similar to the models above, these models use a MoE layer between two LSTM layers. The dimensionality of the embedding layer, and the input and output dimensionality of the MoE layer are set to 1024 instead of 512. For MoE-34M, the LSTM layers have 1024 units. For MoE-143M, the LSTM layers have 4096 units and an output projection of size 1024 (Sak et al., 2014). MoE-34M uses a hierarchical MoE layer with 1024 experts, each with a hidden layer of size 2048. MoE-143M uses a hierarchical MoE layer with 256 experts, each with a hidden layer of size 8192. Both models have 4B parameters in the MoE layers. They searched for the best DropProb for each model, and trained each model for 10 epochs.

[p. 16] The two models achieved test perplexity of 31.3 and 28.0 respectively, showing that even in the presence of a large MoE, more computation is still useful. Results are reported at the bottom of Table 7. The larger of the two models has a similar computational budget to the best published model from the literature, and training times are similar. Comparing after 10 epochs, their model has a lower test perplexity by 18%.
