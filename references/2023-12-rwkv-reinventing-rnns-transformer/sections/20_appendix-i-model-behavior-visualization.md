# I Model Behavior Visualization [p. 20-21]

[p. 20]

## Time Decay Visualization

**Figure 10** (p. 20): "Model behavior visualizations of RWKV."
- The figure shows time decays ($e^{-w}$) in each layer of the RWKV-169M model, sorted along the channel axis. The x-axis is Channel (0 to ~800), and the y-axis is Time Decay (0.0 to 1.0). There are 12 curves, one for each layer (Layer 1 through Layer 12). Each curve is monotonically decreasing from left to right along the sorted channel axis.
- Notably, several decays in the last layers are very close or equal to one, implying that certain information is preserved and propagated throughout the model's temporal context.
- Meanwhile, many decays in the initial layer are close to zero, which corresponds to local operations in $wkv$ (16), likely to be associated with tasks such as text parsing or lexical analysis.
- (Note that the local operations in $wkv$ are due to the extra parameter $u$, when $e^{-w}$ is degenerated into 0.)
- These patterns of time decays are partly learned, but also come from parameter initialization as it speeds up training.

## Causal Trace Experiment

[p. 20-21]

The plot below shows the information retrieval and propagation path in the RWKV-430M model. The experiment follows the *causal trace* method introduced by Meng et al. (2022), where we:

1. Run the model once, and record all states and activation of each layer during the computation;
2. Corrupt the input embeddings of the subject using noise ("The Eiffel Tower" in this example);
3. Restore the states and activation of a certain layer at a certain token during the computation, and record the log-probability of the model outputting the correct answer ("Paris").

Unlike transformers, RWKV relies on the recursive propagation of information in the time dimension. In this case, the fact that the Eiffel Tower is located in Paris is retrieved in layer 4 just after the model sees "The Eiffel". It is then passed down to the subsequent layers. In layer 20, mostly, the information is propagated through time until reaching where it is needed. Finally, at the token "of", it is passed down to the last layer for outputting the answer.

**Figure 11** (p. 21): "Model behavior visualizations of the RWKV model."
- The figure is a heatmap showing the information propagation path. The x-axis is Layer (1 to ~24), the y-axis lists tokens: "The", "E", "iff", "el", "Tower", "is", "located", "in", "the", "city", "of". The color scale represents the log-probability of "Paris" (ranging from about -1 to -7, darker purple = higher log-probability / closer to -1).
- The pattern shows that at early layers (~4-6) around the "E"/"iff"/"el" tokens, the information is first retrieved (shown by moderate purple shading). In later layers (~16-24), the information propagates rightward through the tokens "is", "located", "in", "the", "city", "of", with the strongest activation (darkest purple, highest log-probability) appearing at the token "of" in the final layers.
