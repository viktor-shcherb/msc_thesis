# Comments & Replications [p. 48-49]

> *Inspired by the original Circuits Thread and Distill's Discussion Article experiment, the authors invited several external researchers who were also investigating induction heads to comment on this work. Their comments are included below.* [p. 48]

## Replication: Adam Scherlis [p. 48]

*Adam Scherlis is a researcher at Redwood Research.* [p. 48]

Redwood Research has been working on language model interpretability, inspired in part by Anthropic's work. They found induction heads reliably appearing in two-layer attention-only transformers. Their structure roughly matches the description in "Analyzing a Two-Layer Model" from Anthropic's previous paper, with previous-token heads in layer 0 and induction heads in layer 1 (often one of each). These each have the expected attention behaviors. [p. 48]

They tested this by replacing attention-score matrices with idealized versions and comparing the change in loss to the change from ablating that head: [p. 48]

- Replacing the previous-token head's scores with exact previous-token attention recovered 99% of the loss difference. [p. 48]
- Replacing the induction head's scores with a simple approximation (attending to the first token and to exact `[A][B]...[A]` matches) recovered about 65% of the loss difference. [p. 48]

Their induction heads also match patterns of the form `[A][B][C]...[A][B]→[C]`; including this in the substituted attention scores recovered an additional 10% of loss difference. [p. 48]

The induction head's OV circuit copies tokens, including some fuzzy matching of semantically similar tokens. Its QK circuit is dominated by K-composition with the previous-token head; the previous-token head's OV matrix copies information to a new subspace and the induction head's QK matrix copies it back to the usual token embedding. They also cataloged a few other kinds of attention heads, including skip-trigram heads. [p. 48]

## Replication: Tom Lieberum [p. 48-49]

*Tom Lieberum is a master's student at the University of Amsterdam.* [p. 48]

Lieberum used the empirical criterion for induction heads presented in this paper to look for induction heads in publicly available models. The criterion: on a sequence of tokens `[A][B] .... [A] → [B]`, a head is called an induction head if it attends to the previous `[B]` when reading the last `[A]`, and if the previous `[B]` increased the logit of the last `[B]`. [p. 48]

Under this definition, he found potential induction heads in GPT2 and GPT-Neo mostly starting in the mid-depth region. He made an interactive version to explore attention and logit attribution across all layers and heads on the long Harry Potter prompt with the repetition of the first paragraph. [p. 49]

Specific findings: [p. 49]
- For GPT2-XL, head 20 in layer 21 seems to be an induction head. [p. 49]
- Head 0 in layer 12 of GPT-Neo-2.7B also appears to be an induction head. [p. 49]
- For these heads, virtually every token in the repetition of the first paragraph attends to its following token in the original paragraph. [p. 49]
- EleutherAI provided compute resources for this project. [p. 49]

On minimal context length for induction heads: the paper speculates on the minimal context length necessary to form induction heads. Lieberum found induction to be easily learned with a context length of 4 on a synthetic dataset. However, he believes this is, in general, a property of the dataset/data distribution rather than the model itself, i.e. "how useful is induction for this task, on this dataset?". While it is intriguing to think about the statistics of language in this way, he is not sure how useful this line of research would be to the overall project of interpretability. [p. 49]
