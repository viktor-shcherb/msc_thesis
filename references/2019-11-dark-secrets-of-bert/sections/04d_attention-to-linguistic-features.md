# 4.4 Attention to linguistic features [p. 6]

[p. 6] This experiment investigates whether fine-tuning BERT for a given task creates self-attention patterns which emphasize specific linguistic features. In this case, certain kinds of tokens may get high attention weights from all the other tokens in the sentence, producing vertical stripes on the corresponding attention maps (Figure 1).

## Hypothesis

[p. 6] The hypothesis is that there are vertical stripe patterns corresponding to certain linguistically interpretable features, and that such features are relevant for solving a given task.

## Features investigated

[p. 6] The features investigated are attention to nouns, verbs, pronouns, subjects, objects, and negation words, and special BERT tokens across the tasks.

The manually constructed list of negation words consisted of the following words: *neither, nor, not, never, none, don't, won't, didn't, hadn't, haven't, can't, isn't, wasn't, shouldn't, couldn't, nothing, nowhere*.

## Method

[p. 6] For every head, the sum of self-attention weights assigned to the token of interest from each input token is computed. Since the weights depend on the number of tokens in the input sequence, this sum is normalized by sequence length. This allows aggregating the weights for this feature across different examples. If there are multiple tokens of the same type (e.g. several nouns or negations), the maximum value is taken. Input sentences that do not contain a given feature are disregarded.

For each investigated feature, this aggregated attention score is calculated for each head in every layer and a map is built to detect the heads potentially responsible for this feature. The maps obtained from fine-tuned models are compared with the ones derived using the pre-trained BERT model. This comparison enables determining if a particular feature is important for a specific task and whether it contributes to some tasks more than to others.

## Results

[p. 6-7] Contrary to the initial hypothesis that the vertical attention pattern may be motivated by linguistically meaningful features, the authors found that it is associated predominantly, if not exclusively, with attention to *[CLS]* and *[SEP]* tokens (see Figure 6).

[p. 7] Note that the absolute *[SEP]* weights for the SST-2 sentiment analysis task are greater than for other tasks, which is explained by the fact that there is only one sentence in the model inputs, i.e. only one *[SEP]* token instead of two. There is also a clear tendency for earlier layers to pay attention to *[CLS]* and for later layers to *[SEP]*, and this trend is consistent across all the tasks.

The authors did detect heads that paid increased (compared to the pre-trained BERT) attention to nouns and direct objects of the main predicates (on the MRPC, RTE and QQP tasks), and negation tokens (on the QNLI task), but the attention weights of such tokens were negligible compared to *[CLS]* and *[SEP]*.

> "Therefore, we believe that the striped attention maps generally come from BERT pre-training tasks rather than from task-specific linguistic reasoning." [p. 7]

## Figure 7 (p. 7)

**Figure 7** (p. 7): "Per-task attention weights corresponding to the *[CLS]* token averaged over input sequences' lengths and over dataset examples, and extracted from the final layer. Darker colors correspond to greater absolute weights."

Shows a grid of per-task panels (MRPC, STS-B, SST-2, QQP, RTE, QNLI, MNLI), each containing sub-panels for features: PRON, NOUN, VERB, OBJ, SUBJ, NEG, [CLS], [SEP]. Each sub-panel is a 1x12 heatmap over heads. For most tasks, [SEP] gets the most attention in the final layer. For STS-B, RTE, and QNLI, the greatest attention weights correspond to punctuation tokens (similar to [SEP] in function).
