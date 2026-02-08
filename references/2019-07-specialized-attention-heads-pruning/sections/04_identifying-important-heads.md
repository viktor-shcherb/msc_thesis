# 4 Identifying Important Heads [p. 3-4]

Previous work analyzing how representations are formed by the Transformer's multi-head attention mechanism focused on either the average or the maximum attention weights over all heads (Voita et al., 2018; Tang et al., 2018), but neither method explicitly takes into account the varying importance of different heads. This obscures the roles played by individual heads which influence translations to differing extents. [p. 3]

## Confidence

> "We define the 'confidence' of a head as the average of its maximum attention weight excluding the end of sentence symbol, where average is taken over tokens in a set of sentences used for evaluation (development set)." [p. 3]

A confident head is one that usually assigns a high proportion of its attention to a single token. Intuitively, confident heads may be expected to be important to the translation task. [p. 3]

EOS is excluded on the grounds that it is not a real token (footnote 2). [p. 3]

## Layer-wise Relevance Propagation (LRP)

Layer-wise relevance propagation (LRP) (Ding et al., 2017) is a method for computing the relative contribution of neurons at one point in a network to neurons at another. A detailed description of LRP is provided in appendix A. [p. 3]

The authors propose to use LRP to evaluate the degree to which different heads at each layer contribute to the top-1 logit predicted by the model. Heads whose outputs have a higher relevance value may be judged to be more important to the model's predictions. [p. 3]

## Results

The results of LRP are shown in Figures 1a, 2a, 2c. In each layer, LRP ranks a small number of heads as much more important than all others. [p. 4]

The confidence for each head is shown in Figure 1b. The relevance of a head as computed by LRP agrees to a reasonable extent with its confidence. The only clear exception to this pattern is the head judged by LRP to be the most important in the first layer. It is the most relevant head in the first layer but its average maximum attention weight is low. This head is discussed further in Section 5.3. [p. 4]

**Figure 1** (p. 3): Importance (according to LRP), confidence, and function of self-attention heads. In each layer, heads are sorted by their relevance according to LRP. Model trained on 6m OpenSubtitles EN-RU data. Contains three sub-figures:
- (a) LRP: heatmap of heads relevance for top-1 logits across 6 layers x 8 heads. Shows a small number of heads with much higher relevance (darker blue) per layer.
- (b) Confidence: heatmap of mean max attention weight across 6 layers x 8 heads.
- (c) Head functions: annotated grid showing identified head functions (positional, syntactic, rare words) with accuracy scores. Labels include r (rare), s->v, v->s, v->o, s->v, etc.

**Figure 2** (p. 4): Importance (according to LRP) and function of self-attention heads. In each layer, heads are sorted by their relevance according to LRP. Models trained on 2.5m WMT EN-DE (a, b) and EN-FR (c, d). Contains four sub-figures:
- (a) LRP (EN-DE): heatmap of heads relevance for top-1 logits
- (b) Head functions (EN-DE): annotated grid with head function labels (r, v->o, o->v, v->s, v->s, s->v, a->v, etc.)
- (c) LRP (EN-FR): heatmap of heads relevance for top-1 logits
- (d) Head functions (EN-FR): annotated grid with head function labels
