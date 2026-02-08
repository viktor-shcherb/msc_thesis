# 4.2 Relation-specific heads in BERT [p. 4-5]

[p. 4] The goal of this experiment is to understand whether different syntactic and semantic relations are captured by self-attention patterns. The authors chose to examine semantic role relations defined in frame semantics, since they can be viewed as being at the intersection of syntax and semantics. Specifically, the focus is on whether BERT captures FrameNet's relations between frame-evoking lexical units (predicates) and core frame elements (Baker et al., 1998), and whether the links between them produce higher attention weights in certain specific heads. Pre-trained BERT was used in these experiments.

## Data

[p. 4] The data comes from FrameNet (Baker et al., 1998), a database that contains frame annotations for example sentences for different lexical units. Frame elements correspond to semantic roles for a given frame -- for example, "buyer", "seller", and "goods" for the "Commercial_transaction" frame evoked by the words "sell" or "spend", or "topic" and "text" for the "Scrutiny" semantic frame evoked by the verb "address". Figure 4 shows an example of such an annotation.

Sample sentences were extracted for every lexical unit in the database and the corresponding core frame elements were identified. Only sentences with frame elements of 3 tokens or less were considered. Since each sentence is annotated only for one frame, semantic links from other frames can exist between unmarked elements. Sentences longer than 12 tokens were filtered out, since shorter sentences are less likely to evoke multiple frames. Sentences where the linked objects are less than two tokens apart were also excluded (to ensure that BERT attention captures semantic relations that do not simply correspond to the previous/following token). This left 473 annotated sentences. [p. 4]

## Method

[p. 4] For each of the 473 sentences, pre-trained BERT's attention weights are obtained for each of the 144 heads. For every head, the maximum absolute attention weight among those token pairs that correspond to the annotated semantic link contained within a given sentence is returned. The derived scores are averaged over all collected examples. This strategy identifies the heads that prioritize features correlated with frame-semantic relations within a sentence.

## Results

[p. 4-5] The heatmap of averaged attention scores over all collected examples (Figure 3) suggests that 2 out of 144 heads tend to attend to the parts of the sentence that FrameNet annotators identified as core elements of the same frame. The maximum attention weights averaged over all data examples for these identified heads account for 0.201 and 0.209, which are greater than a 99th percentile of the distribution of values for all heads. Figure 3 shows an example of this attention pattern for these two heads. Both show high attention weight for "he" while processing "agitated" in the sentence "He was becoming agitated" (the frame "Emotion_directed").

> "We interpret these results as limited evidence that certain types of linguistic relations may be captured by self-attention patterns in specialized BERT heads. A wider range of relations remains to be investigated." [p. 4-5]

## Figure 3 (p. 5)

**Figure 3** (p. 5): "Detection of pre-trained BERT's heads that encode information correlated to semantic links in the input text. Two heads (middle) demonstrate their ability to capture semantic relations. Note that the heatmap in the middle is obtained through averaging of all the individual input example maps. For one random annotated FrameNet example (bottom) full attention maps with a zoom in the target token attention distribution are shown (leftmost and rightmost)."

Shows: (left and right) attention maps for two specific heads for the sentence "He was becoming agitated" with zoomed-in attention distributions for the token "he"; (middle) a 12x12 heatmap of averaged attention scores across all heads and layers, with two heads showing notably higher values.

## Figure 4 (p. 5)

**Figure 4** (p. 5): "FrameNet annotation example for the 'address' lexical unit with two core frame elements of different types annotated."

Shows the sentence "These are issues which future studies may seek to address." with "issues" annotated as Core, type TEXT and "address" annotated as Core, type TOPIC, illustrating the FrameNet annotation scheme.
