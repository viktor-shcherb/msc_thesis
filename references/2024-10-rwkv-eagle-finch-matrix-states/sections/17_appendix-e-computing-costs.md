# Appendix E: Computing Costs [p. 33–35]

[p. 33] Throughout this section, we denote by D the model dimension, L the number of layers, h = D/64 the number of heads, and V the vocabulary size. All models are trained with V = 65536.

[p. 33] The number of parameters for all Eagle models is computed by the formula:

$$\#(\text{Params})_E = 13D^2 L + 14DL + 4D + 2DV$$ (23)

[p. 33] The FLOPs for inference is one forward pass for each token. It is approximated by twice the number of parameters (for matrices, there is one addition and one multiplication for each entry) plus six times the size of WKV internal states (see 7 8 (9)), which is

$$\#(\text{InferFLOPs})_E = 2(13D^2 L + 14DL + 4D + 2DV) + 6D^2 L/h$$ (24)

$$= 26D^2 L + 28DL + 8D + 4DV + 6D^2 L/h$$ (25)

[p. 33] The FLOPs for training are approximated as three times the FLOPs of the forward pass without the last term, yielding a total FLOPs of

$$\#(\text{TrainFLOPs})_E = 78D^2 L + 84DL + 16D + 12DV + 18D^2 L/h$$ (26)

[p. 33] These numbers for Finch are marginally larger:

$$\#(\text{Params})_F = 13D^2 L + 464DL + 4D + 2DV$$ (27)

$$\#(\text{InferFLOPs})_F = 26D^2 L + 928DL + 8D + 4DV + 6D^2 L/h$$ (28)

$$\#(\text{TrainFLOPs})_F = 78D^2 L + 2784DL + 24D + 12DV + 18D^2 L/h$$ (29)

[p. 33] In both Eagle and Finch, one needs an internal state to store some previous information, just like any other RNN. In each layer, the internal state consists of three parts:

1. The most recent single-timestep input to the Time-mixing module, denoted as x_{t-1} ∈ R^D, useful for the Token Shift.

2. The most recent single-timestep input to the Channel-mixing module, denoted as x'_{t-1} ∈ R^D, also useful in Token Shift.

3. WKV head memory: Denoted by wkv_{i,j} ∈ R^{(D/h)×(D/h)}, for j = 1, 2, ⋯, h. This is the core part of the internal state that dominates the most information.

[p. 34] The total size of the Eagle and Finch internal state is

$$\#(\text{State}) = L(2D + D^2/h) = 66DL$$ (30)

### Table 11: Released Eagle and Finch Model Details [p. 35]

| Model Name | L | D | State Size | Parameters | InferFLOPs | TrainFLOPs |
|------------|---|------|-----------|------------|------------|------------|
| Eagle 0.4B | 24 | 1024 | 1622016 | 4.62 × 10^8 | 9.33 × 10^8 | 2.80 × 10^9 |
| Eagle 1.5B | 24 | 2048 | 3244032 | 1.58 × 10^9 | 3.17 × 10^9 | 9.52 × 10^9 |
| Eagle 3B | 32 | 2560 | 5406720 | 3.06 × 10^9 | 6.16 × 10^9 | 1.85 × 10^10 |
| Eagle 7B | 32 | 4096 | 8650752 | 7.52 × 10^9 | 1.51 × 10^10 | 4.53 × 10^10 |
| Finch 1.6B | 24 | 2048 | 3244032 | 1.60 × 10^9 | 3.22 × 10^9 | 9.66 × 10^9 |
| Finch 3B | 32 | 2560 | 5406720 | 3.10 × 10^9 | 6.23 × 10^9 | 1.87 × 10^10 |

Caption: Released Eagle and Finch model details and FLOP counts. Inference and training FLOPs are per token numbers.

[p. 35] It's worth noting that the internal state size of Eagle and Finch is more than an order of magnitude bigger than RWKV-4 (which is 5DL). Larger internal states enhance the model's ability to remember previous information by providing more storage space for such information at the cost of slightly larger FLOP counts and memory usage.
