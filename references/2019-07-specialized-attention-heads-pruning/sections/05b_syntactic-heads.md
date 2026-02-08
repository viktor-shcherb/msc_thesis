# 5.2 Syntactic Heads [p. 5]

The authors hypothesize that when used to perform translation, the Transformer's encoder may be responsible for disambiguating the syntactic structure of the source sentence. They wish to know whether a head attends to tokens corresponding to any of the major syntactic relations in a sentence. [p. 5]

Dependency relations analyzed: nominal subject (nsubj), direct object (dobj), adjectival modifier (amod) and adverbial modifier (advmod). These include the main verbal arguments of a sentence and some other common relations. They also include relations which might inform morphological agreement or government in one or more of the target languages. [p. 5]

## 5.2.1 Methodology [p. 5]

Each head in the Transformer's encoder is evaluated for how well it accounts for a specific dependency relation by comparing its attention weights to a predicted dependency structure generated using CoreNLP (Manning et al., 2014) on a large number of held-out sentences. [p. 5]

For each head, they calculate how often it assigns its maximum attention weight (excluding EOS) to a token with which it is in one of the aforementioned dependency relations. Each relation is counted separately and the relation is allowed to hold in either direction between the two tokens. [p. 5]

> "We refer to this relative frequency as the 'accuracy' of head on a specific dependency relation in a specific direction." [p. 5]

Note that under this definition, a head may be evaluated for accuracy on multiple dependency relations. [p. 5]

Many dependency relations are frequently observed in specific relative positions (for example, often they hold between adjacent tokens, see Figure 3). A head is called "syntactic" if its accuracy is at least 10% higher than the baseline that looks at the most frequent relative position for this dependency relation. [p. 5]

**Figure 3** (p. 5): Distribution of the relative position of dependent for different dependency relations (WMT). Bar chart showing the relative position distribution for nsubj, dobj, amod, and advmod. For nsubj, most positions are spread across -7 to +1. For dobj, positions spread across 0 to +5. For amod, concentrated at -3 to +1. For advmod, concentrated at -6 to +2.

## 5.2.2 Results [p. 5]

**Table 1** (p. 5): Dependency scores for EN-RU, comparing the best self-attention head to a positional baseline. Models trained on 2.5m WMT data and 6m OpenSubtitles data.

| dep. | direction | WMT (best head / baseline) | OpenSubtitles (best head / baseline) |
|------|-----------|---------------------------|--------------------------------------|
| nsubj | v -> s | 45 / 35 | 77 / 45 |
| nsubj | s -> v | 52 / 35 | 70 / 45 |
| dobj | v -> o | 78 / 41 | 61 / 46 |
| dobj | o -> v | 73 / 41 | 84 / 46 |
| amod | noun -> adj.m. | 74 / 72 | 81 / 80 |
| amod | adj.m. -> noun | 82 / 72 | 81 / 80 |
| advmod | v -> adv.m. | 48 / 46 | 38 / 33 |
| advmod | adv.m. -> v | 52 / 46 | 42 / 33 |

Table 1 shows the accuracy of the most accurate head for each of the considered dependency relations on the two domains for English-Russian. Figure 4 compares the scores of the models trained on WMT with different target languages. [p. 5]

Certain heads clearly learn to detect syntactic relations with accuracies significantly higher than the positional baseline. This supports the hypothesis that the encoder does indeed perform some amount of syntactic disambiguation of the source sentence. [p. 5-6]

Several heads appear to be responsible for the same dependency relation. These heads are shown in green in Figures 1c, 2b, 2d. [p. 6]

It is not possible to draw strong conclusions regarding the impact of target language morphology on the accuracy of the syntactic attention heads, although relations with strong target morphology are among those that are most accurately learned. [p. 6]

The difference in accuracy of the verb-subject relation heads across the two domains for English-Russian is noted. The authors hypothesize this is due to the greater variety of grammatical person in the Subtitles data which requires more attention to this relation. First, second and third person subjects are encountered in approximately 6%, 3% and 91% of cases in WMT data and in 32%, 21% and 47% of cases in OpenSubtitles data (footnote 4). [p. 6]

**Figure 4** (p. 5): Dependency scores for EN-RU, EN-DE, EN-FR each trained on 2.5m WMT data. Bar chart comparing baseline (red) with EN-RU (yellow/green), EN-DE (green), and EN-FR (blue) across dependency relations (v->s, s->v for nsubj; v->o, o->v for dobj; n->a, a->n for amod; v->a, a->v for advmod). Most language pairs show scores well above baseline for nsubj and dobj relations.
