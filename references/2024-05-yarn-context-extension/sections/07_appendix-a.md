# A Additional details on interpolation methods [p. 14-15]

## A.1 Short notes on the deduction of "NTK-aware" interpolation [p. 14]

In Section 3.1, the authors introduce a change of basis from $b$ to $b'$ in the definition of "NTK-aware" interpolation method. Here they provide a short note on its mathematical deduction. [p. 14]

The goal is to spread out the interpolation pressure across the hidden dimensions using a base-change instead of scaling the frequencies by a fixed factor $s$. The property to guarantee is that the lowest frequency needs to be scaled as much as linear positional scaling and the highest frequency to stay constant. [p. 14]

A new base $b'$ is introduced such that the last dimension matches the wavelength of linear interpolation with a scale factor $s$. Since the original RoPE method skips odd dimensions in order to concatenate both $\cos(\frac{2\pi x}{\lambda})$ and $\sin(\frac{2\pi x}{\lambda})$ components into a single embedding, the last dimension $d \in D$ is $|D| - 2$. [p. 14]

The new base $b'$ can be chosen so that:

$$b'^{\frac{|D|-2}{|D|}} = s \cdot b^{\frac{|D|-2}{|D|}}. \tag{23}$$

Equation (23): Constraint equation requiring that the lowest-frequency RoPE dimension under base $b'$ matches the wavelength of linear interpolation scaled by $s$.

Solving for $b'$ yields:

$$b' = b \cdot s^{\frac{|D|}{|D|-2}}. \tag{24}$$

Equation (24): Closed-form expression for the new base $b'$, identical to Eq. 16 in Section 3.1.

## A.2 The impact of pre-softmax scaling of YaRN on perplexity [p. 14-15]

In Section 3.4, the authors mention the impact of the factor $t$ inside the softmax computation of attention weights. Here they fix 896 16k-token documents from RedPajama [12]$^6$, and calculate their perplexity scores with different scaling $1/\sqrt{t}$. The result is in Figure 2. For comparison, the recommended factor in this case ($s = 8$) is given by: [p. 14]

$$\sqrt{\frac{1}{t}} = 0.1 \ln(s) + 1 \approx 1.208. \tag{25}$$

Equation (25): The recommended pre-softmax scaling factor for $s = 8$, computed from the empirical formula in Eq. 22.

Footnote 6: The authors choose RedPajama because it is the open-source dataset closest to the training dataset of LLaMA as far as they are aware of. [p. 14]

To show the impact of the factor $1/\sqrt{t}$ on different token positions, the authors cut each 16k-token document into chunks of 2048 tokens, and further plot the mean perplexity change comparing to $t = 1$ in percentages: [p. 15]

$$\frac{\text{ppl}(t) - \text{ppl}(t = 1)}{\text{ppl}(t = 1)} \tag{26}$$

Equation (26): Percentage change in perplexity relative to no scaling ($t = 1$), used to measure the impact of the temperature factor across different position segments.

The plot is shown in Figure 3. [p. 15]

To further demonstrate the best values of $t$ across all samples over different token positions, the authors plot the sample counts with minimal perplexity at a given $1/\sqrt{t}$ for each of the 8 position segments over the 16k-token range in Figure 4. [p. 15]

Observations: [p. 15]
- For a suitable $t$, a sample may obtain better perplexity scores across the extended context window.
- The best value of $t$ is mostly consistent across different samples and different positions.

The authors remark that this finding is consistent for different values of $s$ and the best value of $t$ follows their recommended formula (Eq. 22) closely. [p. 15]

**Figure 2** (p. 16): "Fix $s = 8$, compare the LLaMA 7b perplexity on 896 16k-token documents over different scaling $1/\sqrt{t}$. The shaded area represents 1 standard deviation (68%)."

The figure shows perplexity (y-axis, range ~2 to ~9) vs. $1/\sqrt{t}$ (x-axis, range ~1.05 to ~1.5). The mean perplexity curve forms a U-shape with a minimum around $1/\sqrt{t} \approx 1.2$, where perplexity reaches approximately 3.5. At low values of $1/\sqrt{t}$ (~1.05), perplexity is around 5-6; at high values (~1.5), perplexity rises to approximately 4.5. The shaded standard deviation band is wide, spanning roughly 2-3 perplexity points around the mean at each scaling value. This supports the recommended value of $\sqrt{1/t} = 0.1\ln(8) + 1 \approx 1.208$.

**Figure 3** (p. 16): "Fix $s = 8$, compare the mean of perplexity change percentages $\frac{\text{ppl}(t) - \text{ppl}(t = 1)}{\text{ppl}(t = 1)}$ at different segments of token positions on 896 16k-token documents over different scaling $1/\sqrt{t}$."

The figure shows perplexity change percentage (y-axis, range ~-50% to ~0%) vs. $1/\sqrt{t}$ (x-axis, range ~1.1 to ~1.5). Eight lines are plotted for position segments: 0-2048, 2048-4096, 4096-6144, 6144-8192, 8192-10240, 10240-12288, 12288-14336, 14336-16384. All curves show decreasing (improving) perplexity change as $1/\sqrt{t}$ increases from 1.1 to approximately 1.2-1.3, then the improvement plateaus or slightly reverses. The first segment (0-2048) shows the least improvement (near 0%), while later segments (beyond 8192) show more substantial improvements (reaching -40% to -50% at higher $1/\sqrt{t}$ values). This demonstrates that the temperature scaling has a larger beneficial effect on tokens at extended positions.

**Figure 4** (p. 17): "The sample counts (out of the 896 samples) with minimal perplexity at a given $1/\sqrt{t}$ for a given segment of token positions over the 16k-token range."

The figure shows Counts (y-axis, range 0 to ~500) vs. $1/\sqrt{t}$ (x-axis, range ~1.10 to ~1.40). Eight lines correspond to the same position segments as Figure 3. Most lines peak around $1/\sqrt{t} \approx 1.15$ to $1.20$, with counts reaching 200-500 at the peak. The 0-2048 segment (light blue) peaks highest (~500) at around $1/\sqrt{t} \approx 1.15$. All lines decline sharply after $1/\sqrt{t} \approx 1.25$, with very few samples having optimal perplexity at $1/\sqrt{t} > 1.30$. This demonstrates that the best $t$ value is consistent across position segments.
