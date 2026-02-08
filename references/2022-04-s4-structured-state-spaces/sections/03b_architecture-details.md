# 3.4 Architecture Details of the Deep S4 Layer [p. 7]

[p. 7]

Concretely, an S4 layer is parameterized as follows. First initialize a SSM with **A** set to the HiPPO matrix (2). By Lemma 3.1 and Theorem 1, this SSM is unitarily equivalent to some (**Lambda** - **P** **Q**^*, **B**, **C**) for some diagonal **Lambda** and vectors **P**, **Q**, **B**, **C** in C^{N x 1}. These comprise S4's 5N trainable parameters.

The overall deep neural network (DNN) architecture of S4 is similar to prior work. As defined above, S4 defines a map from R^L to R^L, i.e. a 1-D sequence map. Typically, DNNs operate on feature maps of size H instead of 1. S4 handles multiple features by simply defining H independent copies of itself, and then mixing the H features with a position-wise linear layer for a total of O(H^2) + O(HN) parameters per layer. Nonlinear activation functions are also inserted between these layers. Overall, S4 defines a sequence-to-sequence map of shape (batch size, sequence length, hidden dimension), exactly the same as related sequence models such as Transformers, RNNs, and CNNs.

The core S4 module is a linear transformation, but the addition of non-linear transformations through the depth of the network makes the overall deep SSM non-linear. This is analogous to a vanilla CNN, since convolutional layers are also linear. The broadcasting across H hidden features described in this section is also analogous to depthwise-separable convolutions. Thus, the overall deep S4 model is closely related to a depthwise-separable CNN but with *global* convolution kernels.

Follow-up work found that this version of S4 can sometimes suffer from numerical instabilities when the **A** matrix has eigenvalues on the right half-plane [14]. It introduced a slight change to the NPLR parameterization for S4 from **Lambda** - **P** **Q**^* to **Lambda** - **P** **P**^* that corrects this potential problem.

## Table 1: Complexity of Various Sequence Models

[p. 7]

**Table 1** (p. 7): "Complexity of various sequence models in terms of sequence length (**L**), batch size (**B**), and hidden dimension (**H**); tildes denote log factors. Metrics are parameter count, training computation, training space requirement, training parallelizability, and inference computation (for 1 sample and time-step). For simplicity, the state size N of S4 is tied to H. Bold denotes model is theoretically best for that metric. Convolutions are efficient for training while recurrence is efficient for inference, while SSMs combine the strengths of both."

|               | Convolution^3  | Recurrence | Attention             | S4                                       |
|---------------|----------------|------------|-----------------------|------------------------------------------|
| Parameters    | LH             | **H**^2    | **H**^2               | **H**^2                                  |
| Training      | L-tilde H(B+H) | BLH^2      | B(L^2 H + LH^2)      | BH(H-tilde + L-tilde) + BL-tilde H      |
| Space         | **BLH**        | **BLH**    | B(L^2 + HL)           | **BLH**                                  |
| Parallel      | **Yes**        | No         | **Yes**               | **Yes**                                  |
| Inference     | LH^2           | **H**^2    | L^2 H + H^2 L        | **H**^2                                  |

Footnote 3: "Refers to global (in the sequence length) and depthwise-separable convolutions, similar to the convolution version of S4."

Table 1 compares the complexities of the most common deep sequence modeling mechanisms.
