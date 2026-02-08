# Related Work [p. 9-10]

## Length Generalization Failure In Transformers

[p. 9] The length generalization problem has been a topic of interest in the study of neural sequence models for a long time (Graves et al., 2016; Kaiser and Sutskever, 2016; Lake and Baroni, 2018; Hupkes et al., 2020; Yehudai et al., 2021). Transformers, being state-of-the-art sequence models, have been no exception. A group of studies showed the generalization failure of conventional Transformers with APE on specific datasets such as PCFG (Hupkes et al., 2020), LEGO (Zhang et al., 2023), or CLUTRR (Sinha et al., 2019; Gontier et al., 2020). The length generalization problem has been reported even in pretrained Transformers such as T5 (Furrer et al., 2020) and LaMDA (Anil et al., 2022).

Csordas et al. (2021) and Ontanon et al. (2022) study the effect of positional encoding on length generalization but mainly focus on showing relative PE outperforms APEs. Press et al. (2022), on the other hand, propose a new encoding method, ALiBi, and demonstrate that it outperforms popular PEs on extrapolation but only in the context of human language modeling.

Most relevant is Deletang et al. (2023)'s recent study on length generalization in various neural sequence models (including RNNs and Stacked-RNNs) for tasks from Chomsky hierarchy. However, they do not focus on the difference among positional encoding or on autoregressive models. Unlike these studies, this work extensively compares length generalization in popular PEs for a wide range of tasks, specifically focusing on autoregressive models, which represent many contemporary LLMs.

## Positional Encoding

[p. 9-10] A core component of Transformers is the positional encoding mechanism, which helps the model represent the order of the input sequence. Self-attention mechanism in the encoder of Transformers is order-invariant and requires PE to avoid becoming a bag-of-word model. Many methods have been proposed for this purpose.

Originally, Vaswani et al. (2017) introduced absolute positional encoding sinusoidal functions (a learned variant popularized by Devlin et al. (2019)). Relative approach for encoding positional information was further introduced by Shaw et al. (2018), which gave rise to a number of pre-trained LM with relative encodings such as TransformerXL (Dai et al., 2019) and T5 (Raffel et al., 2020) that perform well in length generalization.

More recently, Su et al. (2021) takes the concept of sinusoidal functions and suggests a new way of encoding positional information by rotating the hidden representations before applying self-attention. This method, referred to as *Rotary*, has become a popular choice in the recent LLMs. Press et al. (2022) simplify the T5's Relative encoding and introduced a more efficient variant called ALiBi, while keeping the same or improving extrapolation performance.

Decoder-only Transformers, due to their causal attention mask, are not order-agnostic and can operate without explicit positional information. [p. 10] This was observed early on by Shen et al. (2018) and later explained by Tsai et al. (2019). The observation that Transformers without positional encoding can perform on par with explicit PE has been made in various domains such as machine translation (Yang et al., 2019), language modelling (Irie et al., 2019; Haviv et al., 2022), and even other domains like vision or speech (Likhomanenko et al., 2021).

In this work, not only is it demonstrated that Transformers can operate without explicit position information, but also an important setup is presented where they outperform explicit PEs. Furthermore, it is theoretically shown how they are capable of learning both absolute and relative encodings.
