# Ablation Studies [p. 8-10]

[p. 8] Ablation experiments over a number of facets of BERT to understand their relative importance. Additional ablation studies can be found in Appendix C.

## 5.1 Effect of Pre-training Tasks

[p. 8] The importance of the deep bidirectionality of BERT is demonstrated by evaluating two pre-training objectives using exactly the same pre-training data, fine-tuning scheme, and hyperparameters as BERT_BASE:

- **No NSP**: A bidirectional model trained using the "masked LM" (MLM) but without the "next sentence prediction" (NSP) task.
- **LTR & No NSP**: A left-context-only model trained using a standard Left-to-Right (LTR) LM, rather than an MLM. The left-only constraint was also applied at fine-tuning, because removing it introduced a pre-train/fine-tune mismatch that degraded downstream performance. Additionally, this model was pre-trained without the NSP task. This is directly comparable to OpenAI GPT, but using BERT's larger training dataset, input representation, and fine-tuning scheme.

### Table 5: Ablation over the pre-training tasks using the BERT_BASE architecture

"No NSP" is trained without the next sentence prediction task. "LTR & No NSP" is trained as a left-to-right LM without the next sentence prediction, like OpenAI GPT. "+ BiLSTM" adds a randomly initialized BiLSTM on top of the "LTR + No NSP" model during fine-tuning.

| Tasks | MNLI-m (Acc) | QNLI (Acc) | MRPC (Acc) | SST-2 (Acc) | SQuAD (F1) |
|---|---|---|---|---|---|
| BERT_BASE | 84.4 | 88.4 | 86.7 | 92.7 | 88.5 |
| No NSP | 83.9 | 84.9 | 86.5 | 92.6 | 87.9 |
| LTR & No NSP | 82.1 | 84.3 | 77.5 | 92.1 | 77.8 |
| + BiLSTM | 82.1 | 84.1 | 75.7 | 91.6 | 84.9 |

### Key findings

[p. 8] Removing NSP hurts performance significantly on QNLI, MNLI, and SQuAD 1.1. The impact of training bidirectional representations is evaluated by comparing "No NSP" to "LTR & No NSP". The LTR model performs worse than the MLM model on all tasks, with large drops on MRPC and SQuAD.

[p. 8] For SQuAD it is intuitively clear that a LTR model will perform poorly at token predictions, since the token-level hidden states have no right-side context. To make a good faith attempt at strengthening the LTR system, a randomly initialized BiLSTM was added on top. This significantly improves results on SQuAD, but the results are still far worse than those of the pre-trained bidirectional models. The BiLSTM hurts performance on the GLUE tasks.

[p. 9] The authors recognize that it would also be possible to train separate LTR and RTL models and represent each token as the concatenation of the two models, as ELMo does. However: (a) this is twice as expensive as a single bidirectional model; (b) this is non-intuitive for tasks like QA, since the RTL model would not be able to condition the answer on the question; and (c) this is strictly less powerful than a deep bidirectional model, since it can use both left and right context at every layer.

## 5.2 Effect of Model Size

[p. 9] The effect of model size on fine-tuning task accuracy is explored. A number of BERT models with a differing number of layers, hidden units, and attention heads are trained, while otherwise using the same hyperparameters and training procedure as described previously.

### Table 6: Ablation over BERT model size

#L = number of layers; #H = hidden size; #A = number of attention heads. "LM (ppl)" is the masked LM perplexity of held-out training data. The reported Dev Set accuracy is from 5 random restarts of fine-tuning. Hyperparameters were selected using the Dev set. The reported Dev and Test scores are averaged over 5 random restarts using those hyperparameters.

| #L | #H | #A | LM (ppl) | MNLI-m | MRPC | SST-2 |
|---|---|---|---|---|---|---|
| 3 | 768 | 12 | 5.84 | 77.9 | 79.8 | 88.4 |
| 6 | 768 | 3 | 5.24 | 80.6 | 82.2 | 90.7 |
| 6 | 768 | 12 | 4.68 | 81.9 | 84.8 | 91.3 |
| 12 | 768 | 12 | 3.99 | 84.4 | 86.7 | 92.9 |
| 12 | 1024 | 16 | 3.54 | 85.7 | 86.9 | 93.3 |
| 24 | 1024 | 16 | 3.23 | 86.6 | 87.8 | 93.7 |

### Key findings

[p. 9] Larger models lead to a strict accuracy improvement across all four datasets, even for MRPC which only has 3,600 labeled training examples, and is substantially different from the pre-training tasks.

It is also perhaps surprising that significant improvements can be achieved on top of models which are already quite large relative to the existing literature. For example, the largest Transformer explored in Vaswani et al. (2017) is (L=6, H=1024, A=16) with 100M parameters for the encoder, and the largest Transformer found in the literature is (L=64, H=512, A=2) with 235M parameters (Al-Rfou et al., 2018). By contrast, BERT_BASE contains 110M parameters and BERT_LARGE contains 340M parameters.

[p. 9] It has long been known that increasing the model size will lead to continual improvements on large-scale tasks such as machine translation and language modeling, demonstrated by the LM perplexity of held-out training data shown in Table 6. However, the authors believe that this is the first work to demonstrate convincingly that scaling to extreme model sizes also leads to large improvements on very small scale tasks, provided that the model has been sufficiently pre-trained. Peters et al. (2018b) presented mixed results on the downstream task impact of increasing the pre-trained bi-LM size from two to four layers, and Melamud et al. (2016) mentioned in passing that increasing hidden dimension size from 200 to 600 helped, but increasing further to 1,000 did not bring further improvements. Both of these prior works used a feature-based approach -- the authors hypothesize that when the model is fine-tuned directly on the downstream tasks and uses only a very small number of randomly initialized additional parameters, the task-specific models can benefit from the larger, more expressive pre-trained representations even when downstream task data is very small.

## 5.3 Feature-based Approach with BERT

[p. 10] All BERT results presented so far used the fine-tuning approach, where a simple classification layer is added to the pre-trained model and all parameters are jointly fine-tuned on a downstream task. However, the feature-based approach, where fixed features are extracted from the pre-trained model, has certain advantages:
1. Not all tasks can be easily represented by a Transformer encoder architecture, and therefore require a task-specific model architecture to be added.
2. There are major computational benefits to pre-compute an expensive representation of the training data once and then run many experiments with cheaper models on top of this representation.

### CoNLL-2003 NER setup

[p. 10] The two approaches are compared by applying BERT to the CoNLL-2003 Named Entity Recognition (NER) task (Tjong Kim Sang and De Meulder, 2003). In the input to BERT, a case-preserving WordPiece model is used, and the maximal document context provided by the data is included. Following standard practice, this is formulated as a tagging task but without a CRF layer in the output. The representation of the first sub-token is used as the input to the token-level classifier over the NER label set.

To ablate the fine-tuning approach, the feature-based approach is applied by extracting the activations from one or more layers *without* fine-tuning any parameters of BERT. These contextual embeddings are used as input to a randomly initialized two-layer 768-dimensional BiLSTM before the classification layer.

### Table 7: CoNLL-2003 Named Entity Recognition results

Hyperparameters were selected using the Dev set. The reported Dev and Test scores are averaged over 5 random restarts using those hyperparameters.

| System | Dev F1 | Test F1 |
|---|---|---|
| ELMo (Peters et al., 2018a) | 95.7 | 92.2 |
| CVT (Clark et al., 2018) | - | 92.6 |
| CSE (Akbik et al., 2018) | - | **93.1** |
| **Fine-tuning approach** | | |
| BERT_LARGE | 96.6 | 92.8 |
| BERT_BASE | 96.4 | 92.4 |
| **Feature-based approach (BERT_BASE)** | | |
| Embeddings | 91.0 | - |
| Second-to-Last Hidden | 95.6 | - |
| Last Hidden | 94.9 | - |
| Weighted Sum Last Four Hidden | 95.9 | - |
| Concat Last Four Hidden | 96.1 | - |
| Weighted Sum All 12 Layers | 95.5 | - |

### Key findings

[p. 10] BERT_LARGE performs competitively with state-of-the-art methods. The best performing feature-based method concatenates the token representations from the top four hidden layers of the pre-trained Transformer, achieving 96.1 Dev F1, which is only 0.3 F1 behind fine-tuning the entire model (96.4). This demonstrates that BERT is effective for both fine-tuning and feature-based approaches.
