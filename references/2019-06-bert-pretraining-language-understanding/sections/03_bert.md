# BERT [p. 3-5]

Two steps in the framework: *pre-training* and *fine-tuning*. During pre-training, the model is trained on unlabeled data over different pre-training tasks. For fine-tuning, the BERT model is first initialized with the pre-trained parameters, and all parameters are fine-tuned using labeled data from downstream tasks. Each downstream task has separate fine-tuned models, even though they are initialized with the same pre-trained parameters. [p. 3]

A distinctive feature of BERT is its unified architecture across different tasks. There is minimal difference between the pre-trained architecture and the final downstream architecture. [p. 3]

## Model Architecture

[p. 3] BERT's model architecture is a multi-layer bidirectional Transformer encoder based on the original implementation described in Vaswani et al. (2017) and released in the `tensor2tensor` library.

Notation: number of layers (i.e., Transformer blocks) = L, hidden size = H, number of self-attention heads = A.

Two model sizes:
- **BERT_BASE**: L=12, H=768, A=12, Total Parameters=110M
- **BERT_LARGE**: L=24, H=1024, A=16, Total Parameters=340M

BERT_BASE was chosen to have the same model size as OpenAI GPT for comparison purposes. Critically, the BERT Transformer uses bidirectional self-attention, while the GPT Transformer uses constrained self-attention where every token can only attend to context to its left.

Note: In the literature the bidirectional Transformer is often referred to as a "Transformer encoder" while the left-context-only version is referred to as a "Transformer decoder" since it can be used for text generation. [p. 4, footnote 4]

Feed-forward/filter size is set to 4H in all cases, i.e., 3072 for H=768 and 4096 for H=1024. [p. 3, footnote 3]

## Input/Output Representations

[p. 4] The input representation must unambiguously represent both a single sentence and a pair of sentences (e.g., <Question, Answer>) in one token sequence. A "sentence" can be an arbitrary span of contiguous text, not necessarily an actual linguistic sentence. A "sequence" refers to the input token sequence to BERT, which may be a single sentence or two sentences packed together.

- Uses WordPiece embeddings (Wu et al., 2016) with a 30,000 token vocabulary.
- The first token of every sequence is always `[CLS]`. The final hidden state corresponding to this token is used as the aggregate sequence representation for classification tasks.
- Sentence pairs are packed together into a single sequence, separated with a special `[SEP]` token. A learned embedding is added to every token indicating whether it belongs to sentence A or sentence B.
- Input embedding denoted as E, the final hidden vector of `[CLS]` as C in R^H, and the final hidden vector for the i-th input token as T_i in R^H.
- For a given token, its input representation is constructed by summing the corresponding token, segment, and position embeddings.

**Figure 2** (p. 5): "BERT input representation. The input embeddings are the sum of the token embeddings, the segmentation embeddings and the position embeddings."
Shows an example with two sentences: "my dog is cute" (sentence A) and "he likes play ##ing" (sentence B). Input sequence: `[CLS] my dog is cute [SEP] he likes play ##ing [SEP]`. Three rows of embeddings are summed: Token Embeddings (E_{[CLS]}, E_{my}, ...), Segment Embeddings (E_A for sentence A tokens, E_B for sentence B tokens), Position Embeddings (E_0, E_1, ..., E_{10}).

## 3.1 Pre-training BERT

[p. 4] Unlike Peters et al. (2018a) and Radford et al. (2018), BERT does not use traditional left-to-right or right-to-left language models. Instead, BERT is pre-trained using two unsupervised tasks.

### Task #1: Masked LM

[p. 4] A deep bidirectional model is strictly more powerful than either a left-to-right model or the shallow concatenation of a left-to-right and a right-to-left model. However, standard conditional language models can only be trained left-to-right *or* right-to-left, since bidirectional conditioning would allow each word to indirectly "see itself" and trivially predict the target word in a multi-layered context.

To train a deep bidirectional representation, some percentage of input tokens are masked at random, and then those masked tokens are predicted. This is referred to as a "masked LM" (MLM), also called a Cloze task in the literature (Taylor, 1953). The final hidden vectors corresponding to the mask tokens are fed into an output softmax over the vocabulary, as in a standard LM.

In all experiments, 15% of all WordPiece tokens in each sequence are masked at random. In contrast to denoising auto-encoders (Vincent et al., 2008), only the masked words are predicted rather than reconstructing the entire input.

**Mismatch mitigation:** The `[MASK]` token does not appear during fine-tuning, creating a mismatch with pre-training. To mitigate this, when the i-th token is chosen for masking (15% of tokens chosen at random for prediction):
- 80% of the time: replace with the `[MASK]` token
- 10% of the time: replace with a random token
- 10% of the time: keep the unchanged i-th token

Then T_i is used to predict the original token with cross entropy loss. Variations are compared in Appendix C.2.

### Task #2: Next Sentence Prediction (NSP)

[p. 4] Many downstream tasks (QA, NLI) are based on understanding the *relationship* between two sentences, not directly captured by language modeling. BERT pre-trains for a binarized *next sentence prediction* task: for each pre-training example, 50% of the time B is the actual next sentence that follows A (labeled as `IsNext`), and 50% of the time it is a random sentence from the corpus (labeled as `NotNext`). C (the `[CLS]` representation) is used for NSP. The final model achieves 97%-98% accuracy on NSP. [p. 4, footnote 5]

The vector C is not a meaningful sentence representation without fine-tuning, since it was trained with NSP. [p. 4, footnote 6]

The NSP task is closely related to representation-learning objectives used in Jernite et al. (2017) and Logeswaran and Lee (2018). However, in prior work, only sentence embeddings are transferred to downstream tasks; BERT transfers all parameters to initialize end-task model parameters. [p. 5]

## Pre-training data

[p. 5] The pre-training corpus:
- BooksCorpus (800M words) (Zhu et al., 2015)
- English Wikipedia (2,500M words) -- text passages only, ignoring lists, tables, and headers

It is critical to use a document-level corpus rather than a shuffled sentence-level corpus such as the Billion Word Benchmark (Chelba et al., 2013) in order to extract long contiguous sequences.

## 3.2 Fine-tuning BERT

[p. 5] Fine-tuning is straightforward since the self-attention mechanism in the Transformer allows BERT to model many downstream tasks -- whether single text or text pairs -- by swapping out the appropriate inputs and outputs. For text pair applications, a common pattern is to independently encode text pairs before applying bidirectional cross attention (Parikh et al., 2016; Seo et al., 2017). BERT instead uses the self-attention mechanism to unify these two stages, encoding a concatenated text pair with self-attention that effectively includes *bidirectional* cross attention between two sentences.

For each task, the task-specific inputs and outputs are plugged into BERT and all parameters are fine-tuned end-to-end. Sentence A and sentence B from pre-training are analogous to: (1) sentence pairs in paraphrasing, (2) hypothesis-premise pairs in entailment, (3) question-passage pairs in question answering, and (4) a degenerate text-empty pair in text classification or sequence tagging.

At the output:
- Token representations are fed into an output layer for token-level tasks (sequence tagging, question answering)
- The `[CLS]` representation is fed into an output layer for classification (entailment, sentiment analysis)

[p. 5] Compared to pre-training, fine-tuning is relatively inexpensive. All results in the paper can be replicated in at most 1 hour on a single Cloud TPU, or a few hours on a GPU, starting from the same pre-trained model. The BERT SQuAD model can be trained in around 30 minutes on a single Cloud TPU to achieve a Dev F1 score of 91.0%. [p. 5, footnote 7]

## Figures

**Figure 1** (p. 3): "Overall pre-training and fine-tuning procedures for BERT. Apart from output layers, the same architectures are used in both pre-training and fine-tuning. The same pre-trained model parameters are used to initialize models for different down-stream tasks. During fine-tuning, all parameters are fine-tuned. [CLS] is a special symbol added in front of every input example, and [SEP] is a special separator token (e.g. separating questions/answers)."

Left side shows Pre-training: input is an unlabeled sentence A and B pair, with Masked Sentence A and Masked Sentence B fed through BERT. Outputs are NSP (from C), Mask LM (from T_N, T_1'). Right side shows Fine-tuning: examples for MNLI, NER, SQuAD tasks. Input is Question + Paragraph (for SQuAD), outputs are Start/End Span predictions.
