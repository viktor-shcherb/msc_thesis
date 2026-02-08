# 2 Background and Related Work [p. 2-3]

## Quantization

[p. 2] One of the most powerful ways to decrease the computational time and memory consumption of neural networks is quantization, which uses low-bit representations for the weights and activation tensors. On top of that, using low-bit fixed-point representations, such as INT8, one can further reduce energy consumption since the fixed-point operations are more efficient than their floating-point counterparts [23, 59].

The quantization process in floating-point is simulated according to Jacob et al. [26] using the following quantization function:

$$\hat{\mathbf{x}} := q(\mathbf{x};\, s, z, b) = s \cdot \left( \text{clip}\left( \left\lfloor \frac{\mathbf{x}}{s} \right\rceil + z;\, 0,\, 2^b - 1 \right) - z \right), \quad (1)$$

where **x** denotes the quantizer input (i.e., network weights or activations), $s \in \mathbb{R}_+$ the scale factor or the step-size, $z \in \mathbb{Z}$ the zero point, and $b \in \mathbb{N}$ the bitwidth. $\lfloor \cdot \rceil$ denotes the round-to-nearest-integer operator. This quantization scheme is called *uniform affine* or *asymmetric* quantization [24, 32, 76] and it is one of the most commonly used quantization schemes because it allows for efficient implementation of fixed-point arithmetic. In the case of *symmetric* quantization, the quantization grid is restricted to be symmetric around $z = 0$.

## Post-Training Quantization vs. Quantization-Aware Training

[p. 2] This work focuses on *post-training quantization* (PTQ) methods, which take a pre-trained FP32 network and convert it directly into a fixed-point network without the need for the original training pipeline [2, 5, 7, 25, 32, 35, 41, 43, 44, 75]. These methods require either no data or only a small calibration dataset and are easier to use compared to *quantization-aware training* (QAT, Bhalgat et al. 3, Esser et al. 16, Gupta et al. 21, Jacob et al. 26, Krishnamoorthi 32) methods that have you train the entire network for more epochs. For more details on neural network quantization, the reader is referred to [19, 46].

## Outliers in Transformers

[p. 2] Multiple studies have shown that modern transformer-based language models tend to learn outliers in weights and activations [4, 13, 31]. These outliers are present only in a small fixed set of embedding dimensions, but they appear regularly and consistently across multiple layers and data sequences. It was also shown that those outliers play a crucial role in the model predictions and clipping them or by setting to zero the corresponding parameters significantly degrades the model task performance [31, 49]. The strongest in magnitude outliers typically appear at the output of the feed-forward network, FFN, although Dettmers et al. [13] showed that for big enough transformer-based language models they start appearing after every linear layer, including query, key, and value projection layers. This phenomenon holds for many tasks, training objectives and models (both encoder and decoder transformers), including BERT [14], RoBERTa [37], DistilBERT [53], MobileBERT [55], ELECTRA [9], BART [33], XLNet [68], GPT-2 [50], and OPT [74].

## Quantization Challenges from Outliers

[p. 2] Because of these strong outliers, applying per-tensor PTQ for the FFN's output and the residual sum will likely cause a notable error because of the following trade-off between the range and the precision. On the one hand, using a large quantization range for small-ranged values leads to a loss in representation (high rounding error). On the other hand, a small quantization range for large values leads to a very high clipping error. For the case of significant transformer outliers, frequently, no good trade-off can be found between the rounding and clipping error, resulting in an overall high error.

## Prior Approaches to Fixing Outliers

[p. 2-3] There have been numerous attempts to fix the issue of transformer quantization [4, 12, 13, 17, 27, 28, 51, 54, 62, 63, 69, 71]. Most of these approaches resort to finer quantization granularity (row-wise, channel-wise, group-wise weight and activation quantization), use higher bitwidth and/or different numeric format to represent those outliers better or require extra fine-tuning (in the form of QAT and/or knowledge distillation). In other words, they adapt quantization to work with outliers, which often comes at the expense of general applicability or extra inference overhead.

[p. 3] In contrast, this work wants to address the root cause of the problem and understand why outliers are learned in the first place and suggest a new pre-training protocol that significantly reduces the magnitude of outliers yielding way more quantization-friendly models that can be effortlessly quantized using PTQ without strong degradation of performance.
