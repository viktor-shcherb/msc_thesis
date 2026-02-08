# 5 Discussion [p. 9]

[p. 9] The authors have investigated the extent to which transformer models can use structural and lexical information in long-range contexts for English language modeling. Experiments demonstrated that this information is primarily contained in content words and local ordering statistics: ablations that remove other kinds of information from context have little effect on models' predictive accuracies. In contrast, retaining only information about document identity or named entities causes significant drops in predictive accuracy: the effectiveness of long contexts is not explained by the presence of topic or named entity information alone.

> "Crucial to obtaining these results was a measure of *ablated usable information* grounded in the accuracy of models trained and tested on ablated contexts." [p. 9]

Past work on context in LMs has primarily measured the influence of evaluation-time ablations. Sometimes these two notions of context-sensitivity coincide (e.g., trigram shuffling) and sometimes they do not (e.g., removal of lexical information). The results also offer a jumping-off point for future modeling work. They motivate more *efficient*, compressed context representations that better preserve the information that is usable by current models. They motivate more *accurate* models by developing new context representations that make currently unusable information more prominent.

## Open questions

[p. 9] Several questions remain unanswered:
- Do ablations affect the quality of text *generated* by models? (In particular, does the usable information added by long contexts improve predictability of syntax, semantics, or simply document-level word frequency statistics?)
- More fundamentally, do observations about usable information reflect limitations of transformers or fundamental (Shannon-)information-theoretic properties of English?

The results suggest that at least some of these effects are model-specific: deleting function words cannot add information, but improves held-out model accuracy. A complete answer to this question will require more detailed exploration, including a better understanding of human predictions in comparable settings.
