# 2 Background: State Spaces [p. 3-4]

[p. 3]

Sections 2.1 to 2.4 describe the four properties of SSMs in Fig. 1: the classic continuous-time representation, addressing LRDs with the HiPPO framework, the discrete-time recurrent representation, and the parallelizable convolution representation. In particular, Section 2.4 introduces the SSM convolution kernel **K-bar**, which is the focus of the theoretical contributions in Section 3.

## 2.1 State Space Models: A Continuous-time Latent State Model

The state space model is defined by the simple equation (1). It maps a 1-D input signal u(t) to an N-D latent state x(t) before projecting to a 1-D output signal y(t).

$$x'(t) = \boldsymbol{A}x(t) + \boldsymbol{B}u(t)$$
$$y(t) = \boldsymbol{C}x(t) + \boldsymbol{D}u(t)$$
(1)

Equation (1) defines the continuous-time state space model (SSM), mapping input u(t) through latent state x(t) to output y(t).

SSMs are broadly used in many scientific disciplines and related to latent state models such as Hidden Markov Models (HMM). The goal is to simply use the SSM as a black-box representation in a deep sequence model, where **A**, **B**, **C**, **D** are parameters learned by gradient descent. For the remainder of the paper, the parameter **D** is omitted for exposition (or equivalently, assume **D** = 0) because the term **D**u can be viewed as a skip connection and is easy to compute.

## 2.2 Addressing Long-Range Dependencies with HiPPO

[p. 3-4]

Prior work found that the basic SSM (1) actually performs very poorly in practice. Intuitively, one explanation is that linear first-order ODEs solve to an exponential function, and thus may suffer from gradients scaling exponentially in the sequence length (i.e., the vanishing/exploding gradients problem [32]). To address this problem, the LSSL leveraged the HiPPO theory of continuous-time memorization [16]. HiPPO specifies a class of certain matrices **A** in R^{N x N} that when incorporated into (1), allows the state x(t) to memorize the history of the input u(t). The most important matrix in this class is defined by equation (2), which is called the HiPPO matrix. For example, the LSSL found that simply modifying an SSM from a random matrix **A** to equation (2) improved its performance on the sequential MNIST benchmark from 60% to 98%.

$$\text{(HiPPO Matrix)} \qquad \boldsymbol{A}_{nk} = -\begin{cases} (2n+1)^{1/2}(2k+1)^{1/2} & \text{if } n > k \\ n+1 & \text{if } n = k \\ 0 & \text{if } n < k \end{cases}$$
(2)

Equation (2) defines the HiPPO matrix, the most important matrix in the class of HiPPO matrices that enable continuous-time memorization. The matrix is lower-triangular with specific entries depending on the relationship between row index n and column index k.

## 2.3 Discrete-time SSM: The Recurrent Representation

[p. 4]

To be applied on a discrete input sequence (u_0, u_1, ...) instead of continuous function u(t), equation (1) must be discretized by a **step size** Delta that represents the resolution of the input. Conceptually, the inputs u_k can be viewed as sampling an implicit underlying continuous signal u(t), where u_k = u(k * Delta).

To discretize the continuous-time SSM, the authors follow prior work in using the bilinear method [43], which converts the state matrix **A** into an approximation **A-bar**. The discrete SSM is:

$$x_k = \overline{\boldsymbol{A}} x_{k-1} + \overline{\boldsymbol{B}} u_k \qquad \overline{\boldsymbol{A}} = (\boldsymbol{I} - \Delta/2 \cdot \boldsymbol{A})^{-1}(\boldsymbol{I} + \Delta/2 \cdot \boldsymbol{A})$$
$$y_k = \overline{\boldsymbol{C}} x_k \qquad \overline{\boldsymbol{B}} = (\boldsymbol{I} - \Delta/2 \cdot \boldsymbol{A})^{-1} \Delta \boldsymbol{B} \qquad \overline{\boldsymbol{C}} = \boldsymbol{C}.$$
(3)

Equation (3) defines the discrete SSM via the bilinear (Tustin) discretization. It converts the continuous SSM into a sequence-to-sequence map u_k -> y_k, where the state equation is now a recurrence in x_k computable like an RNN. Concretely, x_k in R^N can be viewed as a hidden state with transition matrix **A-bar**.

Notationally, throughout the paper **A-bar**, **B-bar**, ... denote discretized SSM matrices defined by (3). These matrices are a function of both **A** as well as a step size Delta; this dependence is suppressed for notational convenience when it is clear.

## 2.4 Training SSMs: The Convolutional Representation

[p. 4]

The recurrent SSM (3) is not practical for training on modern hardware due to its sequentiality. Instead, there is a well-known connection between linear time-invariant (LTI) SSMs such as (1) and continuous convolutions. Correspondingly, (3) can actually be written as a discrete convolution.

For simplicity let the initial state be x_{-1} = 0. Then unrolling (3) explicitly yields:

x_0 = **B-bar** u_0 , x_1 = **A-bar** **B-bar** u_0 + **B-bar** u_1 , x_2 = **A-bar**^2 **B-bar** u_0 + **A-bar** **B-bar** u_1 + **B-bar** u_2 , ...

y_0 = **C-bar** **B-bar** u_0 , y_1 = **C-bar** **A-bar** **B-bar** u_0 + **C-bar** **B-bar** u_1 , y_2 = **C-bar** **A-bar**^2 **B-bar** u_0 + **C-bar** **A-bar** **B-bar** u_1 + **C-bar** **B-bar** u_2 , ...

This can be vectorized into a convolution (4) with an explicit formula for the convolution kernel (5).

$$y_k = \overline{\boldsymbol{C}} \overline{\boldsymbol{A}}^k \overline{\boldsymbol{B}} u_0 + \overline{\boldsymbol{C}} \overline{\boldsymbol{A}}^{k-1} \overline{\boldsymbol{B}} u_1 + \cdots + \overline{\boldsymbol{C}} \overline{\boldsymbol{A}} \overline{\boldsymbol{B}} u_{k-1} + \overline{\boldsymbol{C}} \overline{\boldsymbol{B}} u_k$$
$$y = \overline{\boldsymbol{K}} * u.$$
(4)

$$\overline{\boldsymbol{K}} \in \mathbb{R}^L := \mathcal{K}_L(\overline{\boldsymbol{A}}, \overline{\boldsymbol{B}}, \overline{\boldsymbol{C}}) := \left( \overline{\boldsymbol{C}} \overline{\boldsymbol{A}}^i \overline{\boldsymbol{B}} \right)_{i \in [L]} = (\overline{\boldsymbol{C}} \overline{\boldsymbol{B}}, \overline{\boldsymbol{C}} \overline{\boldsymbol{A}} \overline{\boldsymbol{B}}, \ldots, \overline{\boldsymbol{C}} \overline{\boldsymbol{A}}^{L-1} \overline{\boldsymbol{B}}).$$
(5)

Equation (4) expresses the SSM output as a convolution y = **K-bar** * u. Equation (5) defines the SSM convolution kernel **K-bar** of length L as the sequence of matrices (**C-bar** **A-bar**^i **B-bar**) for i in [L].

In other words, equation (4) is a single (non-circular) convolution and can be computed very efficiently with FFTs, **provided** that **K-bar** is known. However, computing **K-bar** in (5) is non-trivial and is the focus of the technical contributions in Section 3. **K-bar** is called the **SSM convolution kernel** or filter.
