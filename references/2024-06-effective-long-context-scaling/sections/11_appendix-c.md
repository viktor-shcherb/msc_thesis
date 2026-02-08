# C Length Extrapolation Results [p. 22]

[p. 22] Despite not the focus of this work, extrapolation is an important property for long context models. Extrapolation refers to a model's ability to conduct inference on input sequences that are longer than its training sequences. The authors evaluate how their 70B model extrapolates with two tasks:

## Validation Loss at Each Position [p. 22]

[p. 22] In Figure 9a, the average loss at each position of a 32,768 sequence length is visualized, where the first 16,384 is the interpolation area (within training sequence length) and the second half is extrapolation. 50 batches of samples are used, averaged across them. To make plots smoother, the mean of losses every 500 positions is taken.

The 70B model with either RoPE ABF or xPOS ABF maintains the loss in the extrapolation area. To contrast this, the result for LLAMA 2 with 4,096 context window is also plotted: the loss explodes after the position goes beyond the training sequence length, which suggests that LLAMA 2 does not extrapolate effectively.

## Synthetic FIRST-SENTENCE-RETRIEVAL Task [p. 22]

[p. 22] To complement validation loss evaluation, the 70B model is also tested with two different PEs on the context probing task. Unlike validation loss task where it is hard to find data samples that require very long range dependencies consistently, FIRST-SENTENCE-RETRIEVAL imposes a very strict requirement for models to attend with a specific length. In Figure 9b, results up to 32,768 are visualized where some performance degradation is seen when the model needs to extrapolate.

The authors observe that, despite often considered as having better extrapolation properties, xPOS ABF does not outperform RoPE ABF in their setting.

## Figures

**Figure 9** (p. 22): "Evaluation on our 70B model's extrapolation capabilities."

Two sub-figures side by side:

- **(a)** "Validation loss calculated at each position of 32,768 context window."
  - X-axis: Position (0 to 30000), Y-axis: Cross Entropy (approximately 1.6 to 2.4).
  - A vertical dashed line at position 16,384 separates "Interpolation (16k)" on the left from "Extrapolation (32k)" on the right.
  - Three lines plotted:
    - **RoPE ABF** (blue): Starts around 2.3 at position 0, drops steeply to about 1.7 by position 5000, then remains roughly flat around 1.65–1.7 through both interpolation and extrapolation regions.
    - **xPOS ABF** (green): Very similar trajectory to RoPE ABF, staying around 1.65–1.7 through both regions.
    - **Llama 2** (orange): Follows a similar pattern to the other two in the interpolation region (dropping to ~1.7), but the loss explodes sharply after position 16,384, rising to approximately 2.3–2.4 in the extrapolation region.
  - Key finding: RoPE ABF and xPOS ABF maintain stable loss during extrapolation; LLAMA 2 does not.

- **(b)** "Context window probing with FIRST-SENTENCE-RETRIEVAL task."
  - X-axis: Task length (256, 1k, 2k, 4k, 8k, 10k, 12k, 14k, 16k, 20k, 24k, 28k, 30k), Y-axis: ROUGE-L (0 to 100).
  - A vertical dashed line at 16k separates "Interpolation (16k)" on the left.
  - Two lines plotted:
    - **RoPE ABF** (blue): Near-100 ROUGE-L in the interpolation region, then gradually degrades in the extrapolation region, dropping to approximately 60–70 at 30k.
    - **xPOS ABF** (green/orange): Similar pattern to RoPE ABF, near-100 in interpolation, degrading in extrapolation to approximately 60–70 at 30k; does not outperform RoPE ABF.
  - Key finding: Both PE variants show some degradation during extrapolation on the retrieval task; xPOS ABF does not outperform RoPE ABF.
