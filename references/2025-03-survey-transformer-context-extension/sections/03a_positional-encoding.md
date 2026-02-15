# 3.1 Positional Encoding [p. 3–4]

Kazemnejad et al. (2024) mention that positional encoding (PE) appears to be a major factor in the length generalization of Transformer [p. 3].

During the inference process, when encountering sequences that exceed the length of the pre-trained window, the model needs to handle the position that was not encountered during pre-training. This may lead to Out-Of-Distribution (OOD) issues. Thus, we would like to find an appropriate position encoding method that allows the model to effectively encode position in sequences that exceed the pre-trained window length [p. 3].

## Method Categories

Based on the implementation methods, solutions can be categorized into two main types:
1. Variants of Rotary Position Embedding (RoPE, Su et al., 2024)
2. Attention bias method [p. 3]

The following sections will detail these two methods [p. 3].

### NoPE Observation

Though the designed positional encoding strategies can alleviate the extrapolation problem, experiments have found that models without positional encoding (NoPE) show better performance than these methods in reasoning tasks (Kazemnejad et al., 2024). "That's because when causal masks are used for decoding, the model reads the sequence sequentially from left to right. And this process naturally incorporates the sequential information of the token." This finding suggests that when designing a position encoding strategy, we may need to consider the way the model processes sequences and the requirements of the task [p. 3].

## 3.1.1 Variants of RoPE [p. 3–4]

Rotary Position Embedding (RoPE, Su et al., 2024) is a positional encoding method utilized in a series of models such as Wang and Komatsuzaki (2021); Touvron et al. (2023); Roziere et al. (2023) [p. 3].

RoPE incorporates explicit relative position dependency in self-attention, which can be expressed as:

$$\sin(q_m, k_n) = q_m R^d_{\Theta,n-m} k_n$$
$$= (R^d_{\Theta,m} q_m)^\top (R^d_{\Theta,n} k_n),$$ (1)

where $R^d_{\Theta,m}$ is called the rotation matrix [p. 3].

### RoPE Extrapolation Capability

The original RoPE's extrapolation capability is not very robust and can only maintain performance slightly beyond the pre-trained context length. Consequently, existing work enhances RoPE for better extrapolation. The core of RoPE is the rotation matrix $R^d_{\Theta,m}$, which is parameterized by the position index $m$ and the function family $\Theta$. We can optimize RoPE by adjusting these parameters or even the structure of RoPE itself [p. 3].

Existing related work can be divided into three subcategories:
1. Position index adjustment
2. Base frequency adjustment
3. Structural modification [p. 3]

### Position Index Adjustment

This method involves modifying the allocation or calculation of position index $m$ to maintain the relative distances between tokens within the model's pre-trained index range. This can be implemented in three ways [p. 3].

We can adjust the allocation of the position index $m$ (An et al., 2024). Besides, proportionally scale $m$ for long sequences to adapt to the pre-trained window (Chen et al., 2023b). What's more, we can combine the above two methods, reallocating position index to some tokens in the sequence, while scaling the position index for others (Su, 2023) [p. 3].

### Base Frequency Adjustment

From the formula of rotation matrix (see details in Appendix A.1.1), we can see that each non-zero term is a trigonometric function value with $\theta_i$ as an independent variable. And the value of $\theta_i$ affects the effect of rotation matrix to a certain extent [p. 3–4].

Base frequency adjustment is to enhance the model extrapolation performance by modifying $\theta_i$ in the trigonometric function terms in the rotation matrix [p. 4].

NTK (Neural Tangent Kernel theory) shows that when the input dimension is low and its embedding representation lacks high-frequency components, it is difficult for the neural network to learn high-frequency information (Tancik et al., 2020). Therefore, researchers choose to adjust $\theta_i$ with the idea of "extrapolation via high-frequency and interpolation via low-frequency" [p. 4].

One strategy is to change the base $b$ of the exponential terms $\theta_i$ in the function cluster $\Theta$, and change it from the default value of 10000 to other values which can improve the model extrapolation performance (Peng and Quesnelle, 2023; Roziere et al., 2023). Another strategy is to directly scale $\theta_i$ (bloc97, 2023; Peng et al., 2023) [p. 4].

### Structural Modification

The methods described above focus on modifying variables in RoPE formula without altering the core structure. Some existing work explores adjusting the structure of RoPE itself to better extrapolate, which optimizes the original RoPE formula (Sun et al., 2022) [p. 4].

## 3.1.2 Attention Bias [p. 4]

This type of method introduces relative position information by adding a bias related to the relative distance between tokens when calculating the similarity between query and key vectors. The process can be expressed as follows:

$$\sin(q_m, k_n) = q_m^\top k_n + f_{bias}(m, n),$$ (2)

where $f_{bias}(m, n)$ is a bias function that depends on the token position index corresponding to query and key. $f_{bias}(m, n)$ be divided into two categories: learnable (Raffel et al., 2020; Chi et al., 2022a), predefined (Press et al., 2021; Chi et al., 2022b) [p. 4].
