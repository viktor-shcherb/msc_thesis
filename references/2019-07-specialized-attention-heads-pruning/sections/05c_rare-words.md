# 5.3 Rare Words [p. 6]

In all models (EN-RU, EN-DE, EN-FR on WMT and EN-RU on OpenSubtitles), one head in the first layer is judged to be much more important to the model's predictions than any other heads in this layer. [p. 6]

This head points to the least frequent tokens in a sentence. [p. 6]

For models trained on OpenSubtitles, among sentences where the least frequent token in a sentence is not in the top-500 most frequent tokens, this head points to the rarest token in 66% of cases, and to one of the two least frequent tokens in 83% of cases. [p. 6]

For models trained on WMT, this head points to one of the two least frequent tokens in more than 50% of such cases. [p. 6]

This head is shown in orange in Figures 1c, 2b, 2d. Examples of attention maps for this head for models trained on WMT data with different target languages are shown in Figure 5. [p. 6]

**Figure 5** (p. 6): Attention maps of the rare words head. Models trained on WMT: (a) EN-RU, (b) EN-DE, (c) EN-FR. Three heatmaps showing attention weight patterns for example sentences. Each shows the rare words head concentrating attention on the least frequent tokens in the sentence (e.g., specific nouns and proper names receive higher attention weights, shown as darker blue cells).
