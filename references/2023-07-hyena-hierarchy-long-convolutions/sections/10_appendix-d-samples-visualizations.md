# D Samples and Visualizations [p. 26-38]

## D.1 Hyena Matrices

[p. 26]

The authors provide visualizations of attention and Hyena matrices activated by test strings. In D.1, D.2, they compare GPTNeo (Black et al., 2021) attention matrices with Hyena matrices extracted by their pre-trained small Hyena model. In D.3 and D.4, they provide additional Hyena matrices for the 355M model, activated by test strings of different length.

For attention, they visualize the raw post-softmax matrix. For Hyena matrices, they plot the (element-wise) absolute value of $\mathsf{H}(u)$:

$$\mathsf{H}(u) = \mathsf{D}_x^N \mathsf{S}_h^N \cdots \mathsf{D}_x^2 \mathsf{S}_h^2 \mathsf{D}_x^1 \mathsf{S}_h^1$$

$$\hat{\mathsf{H}}(u)_{ij} = |\mathsf{H}(u)_{ij}|$$

Since Hyena does not normalize the entries of its matrices with e.g., softmax, there are notable differences with attention: (1) the entries of $\mathsf{H}(u)$ can be either positive and negative, and (2) the magnitude is unconstrained. The authors observe the magnitude of matrices in pre-trained Hyena models to be around $10^{-3}$. [p. 26]

**Figure D.1** (p. 27): "Attention matrices from a GPTNeo small model. 'We use the test string "Attention is all you need. Attention is"'."
A 12x12 grid of heatmap matrices (rows = layers 1-12, columns = heads 1-12) showing post-softmax attention patterns. The matrices display characteristic attention patterns: many heads show strong diagonal patterns (local attention), some show vertical stripes (attending to specific token positions), and others show more diffuse patterns. Early layers tend to have simpler patterns (diagonal-dominant), while deeper layers show more varied structures.

**Figure D.2** (p. 28): "Hyena matrices from a Hyena small (same model used for SuperGLUE downstream evaluations). 'We use the test string "Attention is all you need. Attention is"'. We note that Hyena has a different data-controlled matrix for each *channel* i.e. for each dimension in its width, since it does not use heads."
A 12x12 grid of heatmap matrices (rows = layers 1-12, columns = channels 1-12) showing Hyena matrix patterns in orange color scheme. The Hyena matrices exhibit qualitatively similar structures to attention matrices -- diagonal patterns, vertical stripes, and off-diagonal structure -- but are produced without the attention mechanism. Key difference: Hyena produces a separate matrix per channel rather than per head.

**Figure D.3** (p. 29): "Data-controlled Hyena matrices (355M model), activated by the string 'When a doctor doctors a doctor, does the doctor doing the doctoring doctor as the doctor being doctored wants to be doctored or does the doctor doing the doctoring doctor as they want to doctor?'. Rows in the plot are matrices from different layers, columns are matrices from different channels. The operator shows characteristic patterns of attention matrices, without attention."
A 6x6 grid of heatmap matrices (rows = layers, columns = channels) showing Hyena matrix patterns for a longer, more complex input string. The matrices show diverse patterns including diagonal structure, block structure, and diffuse patterns. The caption emphasizes that these attention-like patterns emerge without attention.

**Figure D.4** (p. 30): "Data-controlled Hyena matrices (355M model), activated by the string 'Mrs. Dursley, Mr. Dursley, Dudley Dursley', from *Causal scrubbing: results on induction heads*. Rows in the plot are matrices from different layers, columns are matrices from different channels."
A 6x6 grid of heatmap matrices (rows = layers, columns = channels) showing Hyena matrix patterns for a string with repeated name patterns (designed to probe induction-head-like behavior). The matrices show varied patterns across layers and channels.

## D.2 Hyena Filters

[p. 31-32]

Figure D.5 provides a visualization of Hyena long convolution filters at initialization and after training to completion on The Pile.

The authors find a substantial performance difference (up to 5% perplexity) between initialization schemes. If the filters at initialization are excessively smooth (see Appendix D.3 for discussion of positional encoding and activation), the model finds a worse solution and takes longer to converge. Further, they observe initialization schemes that regularize filters towards typical filters learned at convergence to decrease performance. These observations are in line with performance gaps between convolution parametrization schemes discussed in main text and Appendix A.1. In particular, the performance improvements obtained via Hyena filters could be due to easier optimization in the space of convolutional filters. [p. 31]

At convergence, Hyena learns a collection of lower-order filters with a similar structure, which can be exploited to further speed up inference after training. [p. 31]

**Figure D.5** (p. 32): "[Top]: Long convolution Hyena filters at initialization (153M parameters, 18 layer model). [Bottom]: Filters after training for 130 billion tokens on The Pile."
Two grids of filter visualizations, each with 6 rows x 3 columns (18 layers total, labeled Layer 1 through Layer 18). X-axis is "Time" (0 to ~1536), y-axis ranges from approximately -1 to 1. **Top grid (before training):** Filters at initialization appear as high-frequency, noisy oscillations across all layers. The filters look like band-limited random signals with no obvious low-frequency structure. **Bottom grid (after training):** Filters have converged to smooth, lower-order structures. Most filters show exponential-decay-like envelopes with distinct curves per channel (shown as colored lines). Early layers (1-3) tend to have broader, more slowly decaying filters, while later layers (16-18) show more rapid decay concentrated near the origin. The learned filters exhibit a similar structure across layers, suggesting potential for post-training compression or speedup.

## D.3 Positional Encoding and Filters Initialization

[p. 31]

The positional encoding chosen for the Hyena filters is a truncated complex exponential basis. Specifically, with $\rho_k(t) = e^{i2\pi kt/L}$ for $k = 0, \ldots K-1$, the positional encoding is defined as a map from $\mathbb{R}$ to $\mathbb{R}^{2K+1}$ such that

$$\text{PositionalEncoding}(t) = \begin{bmatrix} t & \Re[\rho_0](t) & \cdots & \Re[\rho_{K-1}](t) & \Im[\rho_0](t) & \cdots & \Im[\rho_{K-1}](t) \end{bmatrix}$$

where $\Re[\cdot]$, $\Im[\cdot]$ denote the real and imaginary part of their argument, respectively. In the main text, they use $D_e = 2K + 1$ to denote the size of a positional encoding with $K$ features. The number of features of the positional encoding has an impact on the filter initialization and training performances. In particular, $K$ leads to a preconditioning of the spectrum of the filter at initialization. [p. 31]

Figures D.6, D.7, D.8 display the initialized filters (with no Window function) for different values of $K$ ($\{8, 32, 64\}$) for $L = 128$ and frequency $\omega_a$ of sinusoidal activation $\sigma(\cdot) = \sin(\omega_a \cdot)$ set to 1. The choice of $K$ induces a bias in the modeled frequencies at initialization. Specifically the filters resemble low-pass filters with a cut-off frequency of approximately $2K + 1$. [p. 31]

This cut-off frequency is strongly related to the *smoothness* of the filter; as previously mentioned, the authors empirically observe better training dynamics of filters initialized to be non-smooth, i.e. with a rich high-frequency content. While good initializations can be achieved by increasing $K$, this results in larger FFNs (its input dimension is $2K + 1$, i.e. the number of positional encoding features) which come with a higher parameter count. A more efficient solution is to increase the frequency $\omega_a$ of the sinusoidal activation. Figure D.9 shows how with $K = 8$ they can cover the full spectrum simply by setting $\omega_a = 10$. [p. 31]

**Figure D.6** (p. 33): "Hyena filters at initialization with 17 positional encoding features $K = 8$."
Four-panel heatmap visualization. Each panel is a 2D heatmap with y-axis "Sequence Index" (0-128) and varying x-axes. Panels from left to right: (1) **Positional Encoding** (x-axis: Positional Encoding Feature, 0-16): shows the complex exponential basis patterns as alternating red/blue bands with increasing frequency for higher feature indices; (2) **Impulse Response $h_\theta$** (x-axis: Filter Index, 0-32): shows the resulting filter impulse responses, which appear smooth and low-frequency with visible banding patterns; (3) **Magnitude Response $|\text{FFT}[h]|$** (x-axis: Filter Index, 0-32): shows the FFT magnitude spectrum, which is concentrated in the low-frequency region (top rows), confirming the low-pass nature of the initialization with $K=8$; (4) **Phase Response $\angle\text{FFT}[h]$** (x-axis: Filter Index, 0-32): shows the phase spectrum, which appears relatively structured in low frequencies but noisy at higher frequencies.

**Figure D.7** (p. 33): "Hyena filters at initialization with 65 positional encoding features $K = 32$."
Same four-panel layout as Figure D.6 but with $K=32$. Key differences: (1) **Positional Encoding** panel (x-axis: 0-64) shows denser oscillation patterns due to more features; (2) **Impulse Response** shows richer structure with more high-frequency content compared to $K=8$; (3) **Magnitude Response** shows energy spread further into mid-frequency range (approximately up to the $2K+1 = 65$ frequency bin), confirming the higher cut-off frequency; (4) **Phase Response** shows more structured patterns extending further into the frequency domain.

**Figure D.8** (p. 34): "Hyena filters at initialization with 65 positional encoding features $K = 64$."
Same four-panel layout. Note: the caption says "65 positional encoding features" but $K=64$ gives $D_e = 2K+1 = 129$ features. The positional encoding x-axis extends to 128. Key differences from previous figures: (1) **Positional Encoding** panel shows very dense, fine-grained oscillation patterns; (2) **Impulse Response** shows near-random-looking high-frequency content; (3) **Magnitude Response** shows energy spread across nearly the full spectrum, approaching a flat (white noise) spectral profile; (4) **Phase Response** appears largely random/uniform. This confirms the $2K+1$ cut-off frequency relationship: with $K=64$ the filters cover essentially the full spectrum at initialization.

**Figure D.9** (p. 34): "Hyena filters at initialization with 17 positional encoding features $K = 8$ and frequency of sinusoidal activation set to 10."
Same four-panel layout as Figures D.6-D.8 but now with $K=8$ (same as D.6) and $\omega_a = 10$ (instead of $\omega_a = 1$). The positional encoding x-axis extends only to 16 (same small feature count as D.6). Key observation: (1) **Positional Encoding** has the same pattern as Figure D.6 (identical $K=8$); (2) **Impulse Response** now shows much higher-frequency content than D.6 despite using the same $K=8$, thanks to the increased activation frequency $\omega_a = 10$; (3) **Magnitude Response** shows energy spread across nearly the full spectrum (similar to D.8 with $K=64$), demonstrating that increasing $\omega_a$ achieves full spectral coverage without increasing $K$; (4) **Phase Response** appears largely random/uniform. This demonstrates the paper's claim that increasing $\omega_a$ is a more parameter-efficient alternative to increasing $K$ for achieving non-smooth (high-frequency) filter initialization.

## D.4 Downstream Examples

[p. 35-38]

**MultiRC.** The authors report examples of downstream evaluation of small models on the MultiRC question-answering task. They compare answers from small Hyena (153M, trained for 130B tokens on The Pile) and the public checkpoint RWKV-v4 (Peng, 2021) (169M, trained for 332B tokens on The Pile). They select randomized examples with indices being powers of 2. Alignment of Hyena's responses to the task format is greatly improved by providing few-shot examples in the prompt, which may be a promising sign for larger models based on the proposed attention-free architecture. Each example shows responses for specific examples in the validation set (example indices are listed at the beginning of each example). [p. 35]

### MultiRC index: 2, 4

[p. 35]

**Passage:** About forces and motion -- what causes a change in motion, types of forces, relationship between mass and force. [p. 35]

**Question 1:** "Based on the previous passage, Would the mass of a baseball affect how much force you have to use to pick it up? Is 'Less the mass, less the force applied' a correct answer?" **Answer:** Yes [p. 35]

- **RWKV zero-shot:** "The mass of a baseball depends on the force applied. if the mass of the baseball is small, the force applied is small." (Correct reasoning, verbose)
- **Hyena zero-shot:** "Yes it is." (Correct, concise)
- **RWKV few-shot:** "The mass, less the force applied, is a more important force. it is the force that changes the mass of a baseball." (Incorrect reasoning)
- **Hyena few-shot:** "Yes." (Correct)

**Question 2:** "Based on the previous passage, What do you apply to an object to make it move or stop? Is 'Strength' a correct answer?" **Answer:** No [p. 35]

- **RWKV zero-shot:** "The force applied to the object is the force applied to the object." (Tautological, does not answer yes/no)
- **Hyena zero-shot:** "Yes." (Incorrect -- answer should be No)
- **RWKV few-shot:** "The force applied to a baseball is a force. it is a force that is applied to a baseball." (Does not answer yes/no)
- **Hyena few-shot:** "Yes." (Incorrect -- answer should be No)

### MultiRC index: 32, 64

[p. 36]

**Passage:** Film plot about Sunita, a medical student investigating Sanjay Singhania who has anterograde amnesia and loses memory every 15 minutes, uses photographs and tattoos to track his mission to avenge his sweetheart Kalpana's death. [p. 36]

**Question 1:** "Based on the previous passage, Why did Sanjay murder a man? Is 'Sanjay' a correct answer?" **Answer:** Yes [p. 36]

- **RWKV zero-shot:** "The answer is 'Sanjay'." (Correct)
- **Hyena zero-shot:** "The answer is" (Incomplete response)
- **RWKV few-shot:** "The question is not about Sanjay's death." (Incorrect)
- **Hyena few-shot:** "No." (Incorrect -- answer should be Yes)

**Question 2:** "Based on the previous passage, Every 15 minutes, Sanjay goes through what process, Which frustrates his attempts to avenge the death of his sweetheart? Is 'He forgets about facts' a correct answer?" **Answer:** Yes [p. 36]

- **RWKV zero-shot:** "Yes, it is a correct answer.." (Correct)
- **Hyena zero-shot:** "The answer is." (Incomplete response)
- **RWKV few-shot:** "The answer is 'yes'." (Correct)
- **Hyena few-shot:** "The answer is 'yes'." (Correct)

### MultiRC index: 128

[p. 37]

**Passage:** About Alexander II re-convening the Diet of Finland in 1863 and initiating reforms increasing Finland's autonomy from Russia, including establishing its own currency (the markka), railways, and elevating Finnish to a national language. Alexander II is still regarded as "The Good Tsar" in Finland. [p. 37]

**Question:** "Based on the previous passage, Alexander II is considered what in Finland since 1863? Is 'The good tsar' a correct answer?" **Answer:** Yes [p. 37]

- **RWKV zero-shot:** "The correct answer is 'yes'." (Correct)
- **Hyena zero-shot:** "Yes, the question is correct." (Correct)
- **RWKV few-shot:** "The Finnish language is a language of the people." (Incorrect, does not answer the question)
- **Hyena few-shot:** "Yes." (Correct)

### MultiRC index: 1024

[p. 38]

**Passage:** About Einstein's marriages -- married Maric in January 1903, sons Hans Albert (1904) and Eduard (1910), separated 1914, divorced 14 February 1919. Eduard diagnosed with schizophrenia. Einstein married Elsa Lowenthal on 2 June 1919 (first cousin maternally, second cousin paternally, relationship since 1912). Emigrated to United States 1933, Elsa diagnosed with heart and kidney problems 1935, died December 1936. [p. 38]

**Question:** "Based on the previous passage, How much time passed, after Albert Einstein's father divorced his mother, that he re-married? Is '3 months and 18 days' a correct answer?" **Answer:** Yes [p. 38]

- **RWKV zero-shot:** "Albert Einstein was born on 3 march 1916 in Gerlin, Germany. he was the son of a German doctor and a german woman." (Incorrect, fabricated biographical details)
- **Hyena zero-shot:** "'3 months and 18 days'" (Correct, directly quotes the answer candidate)
- **RWKV few-shot:** "It is not a correct answer. The exact date is not known." (Incorrect)
- **Hyena few-shot:** "Yes, according to the previous passage." (Correct)
