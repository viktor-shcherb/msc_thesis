# 7 Related Work [p. 6]

[p. 6] While there has been ample research on positional encoding variants, there has been relatively little prior work that investigates models' ability to infer positions implicitly.

Prior to this work, Irie et al. (2019) explored transformer language models for speech recognition and found that such models, when trained without positional encoding, outperform those trained with sinusoidal embeddings.

In addition, a focused language modeling experiment by Stella Rose Biderman (footnote 5) showed that the NoPos method attains similar results to other position embedding methods; however, that experiment was on a small 350M parameter model trained on a small character-level dataset (enwik8). The current paper shows that this result holds across multiple datasets and model sizes, provides an analysis of the model's internal representations, and hypothesizes how this phenomenon could occur.

Footnote 5: https://twitter.com/BlancheMinerva/status/1394089508723900422
