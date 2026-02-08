# Appendix A: Additional Details for BERT [p. 12-14]

## A.1 Illustration of the Pre-training Tasks

[p. 12] Examples of the pre-training tasks are provided.

### Masked LM and the Masking Procedure

[p. 12] Assuming the unlabeled sentence is `my dog is hairy`, and during the random masking procedure the 4th token (corresponding to `hairy`) is chosen, the masking procedure can be illustrated by:

- 80% of the time: Replace the word with the `[MASK]` token, e.g., `my dog is hairy` -> `my dog is [MASK]`
- 10% of the time: Replace the word with a random word, e.g., `my dog is hairy` -> `my dog is apple`
- 10% of the time: Keep the word unchanged, e.g., `my dog is hairy` -> `my dog is hairy`. The purpose of this is to bias the representation towards the actual observed word.

[p. 12] The advantage of this procedure is that the Transformer encoder does not know which words it will be asked to predict or which have been replaced by random words, so it is forced to keep a distributional contextual representation of *every* input token. Additionally, because random replacement only occurs for 1.5% of all tokens (i.e., 10% of 15%), this does not seem to harm the model's language understanding capability. The impact of this procedure is evaluated in Section C.2.

[p. 12-13] Compared to standard language model training, the masked LM only makes predictions on 15% of tokens in each batch, which suggests that more pre-training steps may be required for the model to converge. In Section C.1 the authors demonstrate that MLM does converge marginally slower than a left-to-right model (which predicts every token), but the empirical improvements of the MLM model far outweigh the increased training cost.

### Next Sentence Prediction

[p. 13] The next sentence prediction task is illustrated with examples:

- Input = `[CLS] the man went to [MASK] store [SEP] he bought a gallon [MASK] milk [SEP]`, Label = `IsNext`
- Input = `[CLS] the man [MASK] to the store [SEP] penguin [MASK] are flight ##less birds [SEP]`, Label = `NotNext`

## A.2 Pre-training Procedure

[p. 13] To generate each training input sequence, two spans of text are sampled from the corpus (referred to as "sentences" even though they are typically much longer than single sentences, but can be shorter also). The first sentence receives the A embedding and the second receives the B embedding. 50% of the time B is the actual next sentence that follows A, and 50% of the time it is a random sentence, which is done for the "next sentence prediction" task. They are sampled such that the combined length is <= 512 tokens. The LM masking is applied after WordPiece tokenization with a uniform masking rate of 15%, and no special consideration given to partial word pieces.

Training configuration:
- Batch size: 256 sequences (256 sequences * 512 tokens = 128,000 tokens/batch)
- Steps: 1,000,000 steps (approximately 40 epochs over the 3.3 billion word corpus)
- Optimizer: Adam with learning rate 1e-4, beta_1 = 0.9, beta_2 = 0.999
- L2 weight decay: 0.01
- Learning rate warmup over the first 10,000 steps, and linear decay of the learning rate
- Dropout probability: 0.1 on all layers
- Activation: gelu (Hendrycks and Gimpel, 2016) rather than the standard relu, following OpenAI GPT
- Training loss: sum of the mean masked LM likelihood and the mean next sentence prediction likelihood

Hardware:
- BERT_BASE: trained on 4 Cloud TPUs in Pod configuration (16 TPU chips total)
- BERT_LARGE: trained on 16 Cloud TPUs (64 TPU chips total)
- Each pre-training took 4 days to complete

[p. 13] Longer sequences are disproportionately expensive because attention is quadratic to the sequence length. To speed up pretraining, the model is pre-trained with sequence length of 128 for 90% of the steps. Then, the rest 10% of the steps are trained with sequence of 512 to learn the positional embeddings.

## A.3 Fine-tuning Procedure

[p. 13-14] For fine-tuning, most model hyperparameters are the same as in pre-training, with the exception of the batch size, learning rate, and number of training epochs. The dropout probability was always kept at 0.1. The optimal hyperparameter values are task-specific, but the following range of possible values was found to work well across all tasks:

- **Batch size**: 16, 32
- **Learning rate (Adam)**: 5e-5, 3e-5, 2e-5
- **Number of epochs**: 2, 3, 4

[p. 14] Large data sets (e.g., 100k+ labeled training examples) were far less sensitive to hyperparameter choice than small data sets. Fine-tuning is typically very fast, so it is reasonable to simply run an exhaustive search over the above parameters and choose the model that performs best on the development set.

## A.4 Comparison of BERT, ELMo, and OpenAI GPT

[p. 14] The differences in recent popular representation learning models including ELMo, OpenAI GPT and BERT are studied. The comparisons between the model architectures are shown visually in Figure 3. In addition to the architecture differences, BERT and OpenAI GPT are fine-tuning approaches, while ELMo is a feature-based approach.

The most comparable existing pre-training method to BERT is OpenAI GPT, which trains a left-to-right Transformer LM on a large text corpus. Many of the design decisions in BERT were intentionally made to make it as close to GPT as possible so that the two methods could be minimally compared. The core argument is that the bi-directionality and the two pre-training tasks presented in Section 3.1 account for the majority of the empirical improvements, but there are several other differences between how BERT and GPT were trained:

- GPT is trained on the BooksCorpus (800M words); BERT is trained on the BooksCorpus (800M words) and Wikipedia (2,500M words).
- GPT uses a sentence separator (`[SEP]`) and classifier token (`[CLS]`) which are only introduced at fine-tuning time; BERT learns `[SEP]`, `[CLS]` and sentence A/B embeddings during pre-training.
- GPT was trained for 1M steps with a batch size of 32,000 words; BERT was trained for 1M steps with a batch size of 128,000 words.
- GPT used the same learning rate of 5e-5 for all fine-tuning experiments; BERT chooses a task-specific fine-tuning learning rate which performs the best on the development set.

[p. 14] To isolate the effect of these differences, ablation experiments are performed in Section 5.1 which demonstrate that the majority of the improvements are in fact coming from the two pre-training tasks and the bidirectionality they enable.

### Figure 3

**Figure 3** (p. 13): "Differences in pre-training model architectures. BERT uses a bidirectional Transformer. OpenAI GPT uses a left-to-right Transformer. ELMo uses the concatenation of independently trained left-to-right and right-to-left LSTMs to generate features for downstream tasks. Among the three, only BERT representations are jointly conditioned on both left and right context in all layers. In addition to the architecture differences, BERT and OpenAI GPT are fine-tuning approaches, while ELMo is a feature-based approach."

The figure shows three model diagrams side by side:
- BERT (Ours): Bidirectional Transformer layers (Trm blocks) with arrows going both directions between tokens T_1, T_2, ..., T_N, with input embeddings E_1, E_2, ..., E_N at the bottom.
- OpenAI GPT: Left-to-right Transformer layers (Trm blocks) with arrows going only left-to-right.
- ELMo: Two separate stacks of LSTM layers (Lstm blocks) -- one left-to-right and one right-to-left, with their outputs concatenated.

## A.5 Illustrations of Fine-tuning on Different Tasks

[p. 14] The illustration of fine-tuning BERT on different tasks can be seen in Figure 4. Task-specific models are formed by incorporating BERT with one additional output layer, so a minimal number of parameters need to be learned from scratch. Among the tasks, (a) and (b) are sequence-level tasks while (c) and (d) are token-level tasks. In the figure, E represents the input embedding, T_i represents the contextual representation of token i, [CLS] is the special symbol for classification output, and [SEP] is the special symbol to separate non-consecutive token sequences.

### Figure 4

**Figure 4** (p. 15): "Illustrations of Fine-tuning BERT on Different Tasks."

Four sub-figures:
- (a) Sentence Pair Classification Tasks (MNLI, QQP, QNLI, STS-B, MRPC, RTE, SWAG): Input is two sentences separated by [SEP], with [CLS] at the start. The [CLS] output feeds into a Class Label prediction. Input tokens: [CLS], Tok 1, ..., Tok N, [SEP], Tok 1', ..., Tok M'. Embeddings: E_{[CLS]}, E_1, ..., E_N, E_{[SEP]}, E_1', ..., E_M'.
- (b) Single Sentence Classification Tasks (SST-2, CoLA): Input is a single sentence with [CLS]. The [CLS] output feeds into a Class Label prediction. Input tokens: [CLS], Tok 1, Tok 2, ..., Tok N.
- (c) Question Answering Tasks (SQuAD v1.1): Input is Question + [SEP] + Paragraph. Outputs are Start/End Span predictions from the paragraph token representations.
- (d) Single Sentence Tagging Tasks (CoNLL-2003 NER): Input is a single sentence with [CLS]. Each token output T_i produces an entity tag (e.g., O, B-PER, O).
