# 3 Surface-Level Patterns in Attention [p. 2-4]

Before looking at specific linguistic phenomena, the authors perform an analysis of surface-level patterns in how BERT's attention heads behave. Examples of heads exhibiting these patterns are shown in Figure 1. [p. 2]

**Figure 1** (p. 2): "Examples of heads exhibiting the patterns discussed in Section 3. The darkness of a line indicates the strength of the attention weight (some attention weights are so low they are invisible)." Shows four attention maps for the same input sentence: Head 1-1 (attends broadly), Head 3-1 (attends to next token), Head 8-7 (attends to [SEP]), Head 11-6 (attends to periods).

**Setup.** Attention maps are extracted from BERT-base over 1000 random Wikipedia segments. They follow the setup used for pre-training BERT where each segment consists of at most 128 tokens corresponding to two consecutive paragraphs of Wikipedia (although they do not mask out input words or as in BERT's training). The input presented to the model is [CLS]<paragraph-1>[SEP]<paragraph-2>[SEP]. [p. 3]

## 3.1 Relative Position [p. 3]

The authors compute how often BERT's attention heads attend to the current token, the previous token, or the next token. [p. 3]

Key findings:
- Most heads put little attention on the current token. [p. 3]
- Some heads specialize in attending heavily on the next or previous token, especially in earlier layers of the network. [p. 3]
- Four attention heads (in layers 2, 4, 7, and 8) on average put >50% of their attention on the previous token. [p. 3]
- Five attention heads (in layers 1, 2, 2, 3, and 6) put >50% of their attention on the next token. [p. 3]

## 3.2 Attending to Separator Tokens [p. 3-4]

A substantial amount of BERT's attention focuses on a few tokens (see Figure 2). Over half of BERT's attention in layers 6-10 focuses on [SEP]. Since most segments are 128 tokens long, the average attention for a token occurring twice in a segment like [SEP] would normally be around 1/64. [p. 3]

[SEP] and [CLS] are guaranteed to be present and are never masked out, while periods and commas are the most common tokens in the data excluding "the," which might explain why the model treats these tokens differently. A similar pattern occurs for the uncased BERT model, suggesting a systematic reason rather than an artifact of stochastic training. [p. 3]

**Figure 2** (p. 3): Two scatter plots. Top: "Each point corresponds to the average attention a particular BERT attention head puts toward a token type. Above: heads often attend to 'special' tokens. Early heads attend to [CLS], middle heads attend to [SEP], and deep heads attend to periods and commas. Often more than half of a head's total attention is to these tokens." Bottom: "heads attend to [SEP] tokens even more when the current token is [SEP] itself." Shows two series: [SEP] -> [SEP] (reaching ~0.8-1.0 in middle layers) and other -> [SEP] (reaching ~0.6 in middle layers). [p. 3]

### [SEP] as no-op hypothesis

One possible explanation is that [SEP] is used to aggregate segment-level information which can then be read by other heads. However, further analysis makes this doubtful. [p. 3-4]

- If this were true, attention heads processing [SEP] would be expected to attend broadly over the whole segment to build up representations. Instead, they almost entirely (more than 90%; see bottom of Figure 2) attend to themselves and the other [SEP] token. [p. 4]
- Qualitative analysis (see Figure 5) shows that heads with specific functions attend to [SEP] when the function is not called for. For example, in head 8-10 direct objects attend to their verbs, but non-nouns mostly attend to [SEP]. [p. 4]
- The authors speculate that attention over these special tokens might be used as a sort of "no-op" when the attention head's function is not applicable. [p. 4]

### Gradient-based feature importance

To further investigate, the authors apply gradient-based measures of feature importance (Sundararajan et al., 2017). They compute the magnitude of the gradient of the loss from BERT's masked language modeling task with respect to each attention weight. This measures how much changing the attention to a token will change BERT's outputs. [p. 4]

**Figure 3** (p. 3): "Gradient-based feature importance estimates for attention to [SEP], periods/commas, and other tokens." Shows three lines across layers 1-12. Starting in layer 5 -- the same layer where attention to [SEP] becomes high -- the gradients for attention to [SEP] become very small. The gradient for attention to other (non-special) tokens and periods/commas remains higher. This indicates attending more or less to [SEP] does not substantially change BERT's outputs, supporting the no-op theory. [p. 4]

## 3.3 Focused vs Broad Attention [p. 4]

The authors measure whether attention heads focus on a few words or attend broadly over many words by computing the average entropy of each head's attention distribution (see Figure 4). [p. 4]

Key findings:
- Some attention heads, especially in lower layers, have very broad attention. These high-entropy attention heads typically spend at most 10% of their attention mass on any single word. The output of these heads is roughly a bag-of-vectors representation of the sentence. [p. 4]
- Entropies for all attention heads from only the [CLS] token were also measured. While average entropies from [CLS] for most layers are very close to those in Figure 4, the last layer has a high entropy from [CLS] of 3.89 nats, indicating very broad attention. This makes sense because [CLS] is used as input for the "next sentence prediction" task during pre-training, so it attends broadly to aggregate a representation for the whole input in the last layer. [p. 4]

**Figure 4** (p. 3): "Entropies of attention distributions. In the first layer there are particularly high-entropy heads that produce bag-of-vector-like representations." Shows scatter plot with a dashed line for uniform attention (~4.5 nats). BERT heads range from ~0 to ~4.5 nats. Layer 1 has heads clustered near the top; later layers generally show lower entropy. [p. 3]
