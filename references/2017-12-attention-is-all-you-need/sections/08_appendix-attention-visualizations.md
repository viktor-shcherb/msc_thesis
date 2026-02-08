# Attention Visualizations [p. 13-15]

This appendix presents visualizations of attention heads from the encoder self-attention in the Transformer, illustrating the different behaviors learned by individual heads.

## Figures

**Figure 3** (p. 13): `"An example of the attention mechanism following long-distance dependencies in the encoder self-attention in layer 5 of 6. Many of the attention heads attend to a distant dependency of the verb 'making', completing the phrase 'making...more difficult'. Attentions here shown only for the word 'making'. Different colors represent different heads. Best viewed in color."`

The figure shows two copies of the sentence "It is in this spirit that a majority of American governments have passed new laws since 2009 making the registration or voting process more difficult." with attention lines drawn from the word "making" to other tokens. The top visualization shows attention lines from "making" reaching to distant tokens "more" and "difficult", demonstrating that the attention heads learn to follow the long-distance dependency of the phrase "making...more difficult" despite the intervening words. Different colored lines represent different attention heads. [p. 13]

**Figure 4** (p. 14): `"Two attention heads, also in layer 5 of 6, apparently involved in anaphora resolution. Top: Full attentions for head 5. Bottom: Isolated attentions from just the word 'its' for attention heads 5 and 6. Note that the attentions are very sharp for this word."`

The figure shows three visualizations of the sentence "The Law will never be perfect, but its application should be just, this is what we are missing, in my opinion." The top panel shows the full attention pattern for head 5 across all tokens, with many crossing attention lines. The middle and bottom panels isolate the attention from the word "its", showing that attention head 5 and head 6 attend sharply from "its" to "Law" and "application" respectively -- performing anaphora resolution by linking the pronoun "its" back to its referent "The Law". The attentions for this word are described as "very sharp". [p. 14]

**Figure 5** (p. 15): `"Many of the attention heads exhibit behaviour that seems related to the structure of the sentence. We give two such examples above, from two different heads from the encoder self-attention at layer 5 of 6. The heads clearly learned to perform different tasks."`

The figure shows two visualizations of the same sentence ("The Law will never be perfect, but its application should be just, this is what we are missing, in my opinion.") from two different attention heads (shown in green and red). The top visualization (green) shows an attention pattern that appears to follow the syntactic structure of the sentence, with attention lines tracing dependencies across clauses. The bottom visualization (red) shows a different structural pattern, indicating that the two heads have learned to perform different tasks related to the syntactic and semantic structure of the sentence. [p. 15]
