# Properties of Selection Mechanisms [p. 7–9]

## Section 3.5

[p. 7]

The selection mechanism is a broader concept that can be applied in different ways, such as to more traditional RNNs or CNNs, to different parameters (e.g. $\boldsymbol{A}$ in Algorithm 2), or using different transformations $s(x)$.

## 3.5.1 Connection to Gating Mechanisms

[p. 8]

The most important connection highlighted: the classical gating mechanism of RNNs is an instance of the selection mechanism for SSMs. The connection between RNN gating and the discretization of continuous-time systems is well established (Funahashi and Nakamura 1993; Tallec and Ollivier 2018). In fact, Theorem 1 is an improvement of Gu, Johnson, Goel, et al. (2021, Lemma 3.1) generalizing to the ZOH discretization and input-dependent gates (proof in Appendix C). More broadly, $\Delta$ in SSMs can be seen to play a generalized role of the RNN gating mechanism. In line with prior work, the authors adopt the view that *discretization of SSMs is the principled foundation of heuristic gating mechanisms*. [p. 8]

**Theorem 1.** When $N = 1$, $A = -1$, $B = 1$, $s_\Delta = \text{Linear}(x)$, and $\tau_\Delta = \text{softplus}$, then the selective SSM recurrence (Algorithm 2) takes the form

$$g_t = \sigma(\text{Linear}(x_t))$$
$$h_t = (1 - g_t) h_{t-1} + g_t x_t.$$
(Equation 5) [p. 8]

As mentioned in Section 3.2, the specific choices of $s_\Delta$, $\tau_\Delta$ are from this connection. In particular, note that if a given input $x_t$ should be completely ignored (as necessary in the synthetic tasks), all $D$ channels should ignore it, and so the input is projected down to 1 dimension before repeating/broadcasting with $\Delta$. [p. 8]

## 3.5.2 Interpretation of Selection Mechanisms

[p. 8–9]

Three particular mechanistic effects of selection are elaborated:

**Variable Spacing.** Selectivity allows filtering out irrelevant noise tokens that may occur between inputs of interest. This is exemplified by the Selective Copying task, but occurs ubiquitously in common data modalities, particularly for discrete data -- for example the presence of language fillers such as "um". This property arises because the model can mechanistically filter out any particular input $x_t$, for example in the gated RNN case (Theorem 1) when $g_t \to 0$. [p. 8]

**Filtering Context.** It has been empirically observed that many sequence models do not improve with longer context (F. Shi et al. 2023), despite the principle that more context should lead to strictly better performance. An explanation is that many sequence models cannot effectively ignore irrelevant context when necessary; an intuitive example are global convolutions (and general LTI models). On the other hand, selective models can simply reset their state at any time to remove extraneous history, and thus their performance in principle improves monotonically with context length (e.g. Section 4.3.2). [p. 8]

**Boundary Resetting.** In settings where multiple independent sequences are stitched together, Transformers can keep them separate by instantiating a particular attention mask, while LTI models will bleed information between the sequences. Selective SSMs can also reset their state at boundaries (e.g. $\Delta_t \to \infty$, or Theorem 1 when $g_t \to 1$). These settings may occur artificially (e.g. packing documents together to improve hardware utilization) or naturally (e.g. episode boundaries in reinforcement learning (Lu et al. 2023)). [p. 9]

Additionally, the authors elaborate on effects of each selective parameter: [p. 9]

**Interpretation of $\Delta$.** In general, $\Delta$ controls the balance between how much to focus or ignore the current input $x_t$. It generalizes RNN gates (e.g. $g_t$ in Theorem 1): mechanically, a large $\Delta$ resets the state $h$ and focuses on the current input $x$, while a small $\Delta$ persists the state and ignores the current input. SSMs (1)-(2) can be interpreted as a continuous system discretized by a timestep $\Delta$, and in this context the intuition is that large $\Delta \to \infty$ represents the system focusing on the current input (thus "selecting" it and forgetting its current state) while a small $\Delta \to 0$ represents a transient input that is ignored. [p. 9]

**Interpretation of $\boldsymbol{A}$.** The $\boldsymbol{A}$ parameter could also be selective, but it ultimately affects the model only through its interaction with $\Delta$ via $\overline{\boldsymbol{A}} = \exp(\Delta \boldsymbol{A})$ (the discretization (4)). Thus selectivity in $\Delta$ is enough to ensure selectivity in $(\overline{\boldsymbol{A}}, \overline{\boldsymbol{B}})$, and is the main source of improvement. The authors hypothesize that making $\boldsymbol{A}$ selective in addition to (or instead of) $\Delta$ would have similar performance, and leave it out for simplicity. [p. 9]

**Interpretation of $\boldsymbol{B}$ and $\boldsymbol{C}$.** As discussed in Section 3.1, the most important property of selectivity is filtering out irrelevant information so that a sequence model's context can be compressed into an efficient state. In an SSM, modifying $\boldsymbol{B}$ and $\boldsymbol{C}$ to be selective allows finer-grained control over whether to let an input $x_t$ into the state $h_t$, or the state into the output $y_t$. These can be interpreted as allowing the model to modulate the recurrent dynamics based on content (input) and context (hidden states) respectively. [p. 9]
