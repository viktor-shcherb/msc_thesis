# Introduction [p. 1-2]

[p. 1] Length generalization -- the ability to generalize from smaller training context sizes to larger ones -- is a major challenge for Transformer-based language models (Vaswani et al., 2017; Deletang et al., 2023; Zhang et al., 2023). Even with larger Transformers, this issue persists (Brown et al., 2020; Furrer et al., 2020). Larger context sizes benefit models through more in-context-learning examples, higher numbers of reasoning steps, or longer text generation. However, training a Transformer with a larger context size can be excessively slow and memory-intensive. This is more pronounced with instruction-following datasets (Wei et al., 2022a; Chung et al., 2022; Ouyang et al., 2022), where it is infeasible to train on all possible context lengths and the number of training examples drops dramatically as the sequence length increases, requiring the model to generalize from finite and shorter-length training examples.

This work focuses on the effect of *positional encoding* on length generalization in "**decoder-only**" Transformers on various tasks trained from scratch. Figure 1 summarizes the finding that using no positional encoding is better than using explicit positional encodings.

**Figure 1** (p. 2): "No positional encoding (NoPE) outperforms all other positional encodings at length generalization of decoder-only Transformers (GPT-style) trained from scratch and evaluated on a battery of reasoning-like downstream tasks. This figure shows aggregate ranking of positional encoding methods across 10 tasks."

The figure is a horizontal bar chart showing Mean Reciprocal Rank (higher is better) for five PE methods:
- No Positional Encoding: 0.69
- T5's Relative PE: 0.55
- ALiBi: 0.50
- Rotary: 0.33
- Absolute Position Embedding: 0.22

An annotation notes that positional encodings used in GPT3-style LLMs include BLOOM (2022a), PaLM (2022), and LLaMA (2023).

[p. 2] Positional encoding (PE) seems to be a major factor in length generalization as the model has to systematically encode tokens in *all* possible positions. The original Transformer architecture (Vaswani et al., 2017) used non-parametric periodic functions to represent *absolute position embeddings* (APE) in a systematic manner, but further studies have shown that these functions are inadequate for length generalization (Ontanon et al., 2022). The prevailing belief is that relative PEs (Shaw et al., 2018; Raffel et al., 2020) are more effective in length generalization than APE variants (Ontanon et al., 2022; Csordas et al., 2021). However, Press et al. (2022) has shown that even Transformers with relative PEs, such as Rotary (Su et al., 2021), can be poor at length generalization. The evaluation of PEs often relies on language modeling perplexity as a key metric (Haviv et al., 2022; Press et al., 2022) which does not always align with performance on downstream tasks (Tay et al., 2022). This raises important questions: what exactly is the influence of positional encoding on length generalization at *downstream tasks*? Moreover, early empirical evidence shows that decoder-only Transformers without explicit position information (Tsai et al., 2019; Haviv et al., 2022) can perform as well as existing PEs in in-distribution settings, but effects on length generalization and downstream performance are unclear.

Recently, asking models to emit intermediate computation steps into a scratchpad, also referred to as *chain-of-thought*, has been adopted to improve the length extrapolation in Transformers (Nye et al., 2021; Wei et al., 2022b). These techniques are architecture-independent and can be used with any PE method. However, it remains an open question whether these techniques, at least in regard to length generalization, render the choice of PE irrelevant, especially given that model performance is highly sensitive to the scratchpad format (Bueno et al., 2022; Akyurek and Akyurek, 2022).

To answer these questions, the authors conduct a systematic study on the length generalization of decoder-only Transformers, popularized by the GPT-family of models (Radford et al., 2019), with the most commonly used positional encoding schemes, both with and without scratchpad. Specifically, they evaluate APE (Vaswani et al., 2017), T5's Relative PE (Raffel et al., 2020), ALiBi (Press et al., 2022), Rotary (Su et al., 2021) and no positional encoding (NoPE) on a battery of reasoning and mathematical tasks.

## Contributions (stated as results)

- Most commonly used positional encoding methods, including ALiBi, Rotary, and APE, are ill-suited for length generalization in downstream tasks and are outperformed by T5's Relative PE.
- Transformers without positional encoding (NoPE) outperform all explicit positional encoding schemes. They achieve this without computing additional terms in the attention mechanism (in contrast to explicit PEs).
- NoPE is theoretically capable of representing both absolute and relative PEs. But empirically, it is closer to the relative encoding scheme similar to T5's Relative PE.
- Scratchpad is not always helpful for length generalization and its format highly impacts the performance. The attention distributions reveal that NoPE and T5's Relative PE encourage attending to both long and short-range positions, ALiBi to recent positions, and Rotary and APE to no particular positions.
