# 5 Discussion [p. 16–17]

[p. 16]

The authors discuss related work, limitations, and some future directions. [p. 16]

**Related Work.** Appendix A discusses how the selection mechanism relates to similar concepts. Appendix B has an extended related work of SSMs and other related models. [p. 16]

---
[p. 17 continued]

**No Free Lunch: Continuous-Discrete Spectrum.** Structured SSMs were originally defined as discretizations of continuous systems (1), and have had a strong inductive bias toward continuous-time data modalities such as perceptual signals (e.g. audio, video). As discussed in Sections 3.1 and 3.5, the selection mechanism overcomes their weaknesses on discrete modalities such as text and DNA; but this conversely can impede their performance on data that LTI SSMs excel on. The authors' ablations on audio waveforms examine this tradeoff in more detail. [p. 17]

**Downstream Affordances.** Transformer-based foundation models (particularly LLMs) have a rich ecosystem of properties and modes of interaction with pretrained models, such as fine-tuning, adaptation, prompting, in-context learning, instruction tuning, RLHF, quantization, and so on. The authors are particularly interested in whether Transformer alternatives such as SSMs have similar properties and affordances. [p. 17]

**Scaling.** The empirical evaluation is limited to small model sizes, below the threshold of most strong open source LLMs (e.g. Llama (Touvron et al. 2023)) as well as other recurrent models such as RWKV (B. Peng et al. 2023) and RetNet (Y. Sun et al. 2023), which have been evaluated at the 7B parameter scale and beyond. It remains to assess whether Mamba still compares favorably at these larger sizes. The authors also note that scaling SSMs may involve further engineering challenges and adjustments to the model that are not discussed in this paper. [p. 17]
