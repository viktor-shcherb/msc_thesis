# D Task Specific Model Details [p. 14-17]

[p. 14] All QA and classification models are implemented using PyTorch-Lightning^14. The official train/dev/test splits of all datasets are used except for Hyperpartisan news which is randomly split into 80/10/10 for train/dev/test.

^14 https://github.com/PyTorchLightning/pytorch-lightning [p. 14, footnote 14]

## WikiHop

[p. 14] Instances in WikiHop consist of: a question, answer candidates (ranging from two candidates to 79 candidates), supporting contexts (ranging from three paragraphs to 63 paragraphs), and the correct answer. The dataset does not provide any intermediate annotation for the multihop reasoning chains, requiring models to instead infer them from the indirect answer supervision.

### Input Preparation

[p. 14] To prepare the data for input to Longformer and RoBERTa, the question, answer candidates, and support contexts are first tokenized using RoBERTa's wordpiece tokenizer. Then the question and answer candidates are concatenated with special tokens as `[q] question [/q] [ent] candidate1 [/ent] ... [ent] candidateN [/ent]`. The contexts are also concatenated using RoBERTa's document delimiter tokens as separators: `</s> context1 </s> ... </s> contextM </s>`. The special tokens `[q]`, `[/q]`, `[ent]`, `[/ent]` were added to the RoBERTa vocabulary and randomly initialized before task finetuning.

### Model Architecture

[p. 14] After preparing the input data, activations are computed from the top layer of each model. The question and answer candidates are taken and concatenated to as much context as possible up to the model sequence length (512 for RoBERTa, 4,096 for Longformer), the sequence is run through the model, the output activations are collected, and this is repeated until all of the context is exhausted (for all models except Longformer-large, where just the first 4,096 length sequence is included due to memory requirements). Then all activations for all chunks are concatenated into one long sequence. In the case of Longformer, global attention is used on the entire question and answer candidate sequence.

For prediction, a linear layer is attached to each `[ent]` that outputs a single logit, the logits are averaged over all logits for each candidate across the chunks, a softmax is applied and the cross entropy loss with the correct answer candidate is used.

### Training Details

[p. 14] Training used the Adam optimizer with linear warmup over 200 gradient updates to a maximum LR, and linear decay over the remainder of training. Gradient accumulation is used to achieve an effective batch size of 32 instances, checking development accuracy every 250 gradient updates and reporting maximum development accuracy. Other hyperparameters (dropout, weight decay) were identical to RoBERTa pretraining.

### Hyperparameter Search

[p. 14] Minimal hyperparameter trials are run. For fair comparison between Longformer and RoBERTa, an identical hyperparameter search is run with Longformer-base and RoBERTa-base. This consisted of a grid search of LR in [2e-5, 3e-5, 5e-5] and number epochs in [5, 10, 15]. The best Longformer-base configuration used lr=3e-5, 15 epochs. Two hyperparameter trials were run for Longformer-large, lr=3e-5 and number epochs in [5, 15] (the 5 epoch model had higher dev accuracy of 77.6, and was the single model submitted to the public leaderboard for test set evaluation). All models were trained on a single RTX8000 GPU, with Longformer-base taking about a day for 5 epochs.

## TriviaQA

[p. 14-15] TriviaQA has more than 100K question, answer, document triplets for training. Documents are Wikipedia articles, and answers are named entities mentioned in the article. The span that answers the question is not annotated, but it is found using simple text matching.

### Input Preparation

[p. 14-15] Similar to WikiHop, the question and the document are tokenized using RoBERTa's tokenizer, then the input is formed as `[s] question [/s] document [/s]`. The document is truncated at 4,096 wordpieces to avoid it being very slow. Afterwards, the activations from RoBERTa and Longformer are obtained similar to WikiHop (discussed above). Global attention is used on all question tokens.

### Prediction

[p. 15] For prediction, one layer is added that predicts the beginning and end of the answer span. Because of the distant supervision nature of the training data (no gold answer spans), the loss function of Clark and Gardner (2017) is used which works like an OR that the model only needs to get one answer span right, not all of them.

### Hyperparameters and Training

[p. 15] Hyperparameters of the best configuration are listed in Tab. 14. All other hyperparameters are similar to RoBERTa's. For hyperparameter search, only LR is tuned for the RoBERTa baseline and tried rates [3e-5, 5e-5, 1e-4], then used the best, which is 3e-5, for all subsequent experiments with no further tuning. The Longformer-large is trained with the best configuration once and submitted its output to the leaderboard. Experiments are run on 32GB V100 GPUs. Small model takes 1 day to train on 4 GPUs, while large model takes 1 day on 8 GPUs.

## HotpotQA

[p. 15-16] HotpotQA dataset involves answering questions from a set of 10 paragraphs from 10 different Wikipedia articles where 2 paragraphs are relevant to the question and the rest are distractors. It includes 2 tasks of answer span extraction and evidence sentence identification. The model for HotpotQA combines both answer span extraction and evidence extraction in one joint model.

### Two-Stage Model

[p. 15] A higher performance is found using a two-stage Longformer model with similar setup that first identifies relevant paragraphs and then does find the final answer span and evidence.^15 This is largely because removing the distracting paragraphs first reduces the noise for the final evidence and span detection as also found to be important by recent state-of-the-art methods in this dataset (Fang et al., 2020).

^15 The final dev performance of the two stage model improves over a single stage model by about 4.2 points on joint F1 metric. [p. 15, footnote 15]

### Input Format

[p. 15-16] Similar to WikiHop and TriviaQA, to prepare the data for input to Longformer, the question is concatenated and then all the 10 paragraphs in one long context. The following input format with special tokens is used: `"[CLS] [q] question [/q] <t> title_1 </t> sent_{1,1} [s] sent_{1,2} [s] ... <t> title_2 </t> sent_{2,1} [s] sent_{2,2} [s] ..."` where `[q]`, `[/q]`, `<t>`, `</t>`, `[s]`, `[p]` are special tokens representing, question start and end, paragraph title start and end, and sentence, respectively. The special tokens were added to the Longformer vocabulary and randomly initialized before task finetuning.

### Global Attention

[p. 16] For Longformer, global attention is used on question tokens, paragraph title start tokens as well as sentence tokens. The model includes additional feedforward layers on top of paragraph title start tokens for prediction of relevant paragraphs, as well as sentence tokens for predicting evidence sentences.

### First Stage Processing

[p. 16] After training the first stage model, relevant paragraph scores are predicted for both training and development set. Up to 5 paragraphs whose raw score is higher than a pre-specified threshold (-3.0) are kept, and the other paragraphs from the context are removed. The second stage model is then trained on the resulting shortened context.

### Answer Span Extraction

[p. 16] For answer span extraction, BERT's QA model (Devlin et al., 2019) is used with addition of a question type (yes/no/span) classification head over the first special token (`[CLS]`). For evidence extraction, 2 layer feedforward networks are applied on top of the representations corresponding to sentence and paragraph tokens to get the corresponding evidence prediction scores and binary cross entropy loss is used to train the model.

### Inference and Decoding

[p. 16] At inference time for evidence extraction, a constrained decoding strategy similar to Groeneveld et al. (2020) is used that ensures that the evidence sentences come from exactly two paragraphs which is the setup of this dataset. Span, question classification, sentence, and paragraphs losses are combined and the model is trained in a multitask way using linear combination of losses.

### Training Details

[p. 16] Experiments are done on RTX8000 GPUs and training each epoch takes approximately half a day on 4 GPUs. The model is trained using Adam optimizer with linear warmup (1000 steps) and linear decay. Minimal hyperparameter tuning using LRs of 3e-5 and 5e-5 and epochs of 3 to 7 and found the model with LR of 3e-5 and 5 epochs to work best. The same hyperparameter search is conducted for the RoBERTa baseline as well. The rest of the hyperparameters are reported in Tab. 14. [unclear: the running text says best LR is 3e-5 but Tab. 14 lists HotpotQA LR as 5e-5 -- apparent inconsistency in the paper itself]

## Coreference Model Details

[p. 16] The coreference model is a straightforward adaptation of the coarse-to-fine BERT based model from Joshi et al. (2019). After preprocessing each document with the RoBERTa wordpiece tokenizer, it splits each document into non-overlapping segments up to the maximum sequence length, then concatenates the activations for the coarse-to-fine clustering stage that forms coreference clusters. The maximum sequence length was 384 for RoBERTa-base, chosen after three trials from [256, 384, 512] using the default hyperparameters in the original implementation.^16 For Longformer-base the sequence length was 4,096.

^16 https://github.com/mandarjoshi90/coref [p. 16, footnote 16]

[p. 16] Similar to the original implementation, different learning rates are used for the pretrained RoBERTa parameters and the randomly initialized task parameters. Using a larger learning rate in the task parameters allows the optimizer to adjust them farther from their randomly initialized values without destroying the information in the pretrained RoBERTa parameters.

### Hyperparameter Search

[p. 16] Hyperparameter searches were minimal and consisted of grid searches of RoBERTa LR in [1e-5, 2e-5, 3e-5] and task LR in [1e-4, 2e-4, 3e-4] for both RoBERTa and Longformer for a fair comparison. The best configuration for Longformer-base was RoBERTa lr=1e-5, task lr=1e-4. All other hyperparameters were the same as in the original implementation. Training takes about 10 hours on a single GPU.

### Implementation Notes

[p. 16-17] The implementation is described as a "superhack" that involves PyTorch and TensorFlow sharing a single process and GPU. To avoid re-implementing the complicated coarse-to-fine logic from TensorFlow in PyTorch (that involves a highly optimized custom GPU kernel originally released by Lee et al. (2018)), a system is devised where the lower transformer portion of the model passes activations and gradients back and forth between PyTorch and TensorFlow. The input tensors are first run through the transformer in PyTorch, the activations are collected from the top layer, transferred from GPU to CPU then from CPU to TensorFlow and back to GPU to run the coarse-to-fine clustering and compute the loss. Then gradients are back propagated in TensorFlow to the top of the transformer and the process reversed to transfer them to PyTorch for back propagation through the remainder of the model. Separate optimizers are maintained with identical LR schedules for parameter updates. The overhead in this approach is minimal compared to the overall cost of running the model.

## Table 14: Hyperparameters of the QA models [p. 16]

All models use a similar scheduler with linear warmup and decay.

| Param | WikiHop | TriviaQA | HotpotQA |
|---|---|---|---|
| Epochs | 15 | 5 | 5 |
| LR | 3e-5 | 3e-5 | 5e-5 |
| Warmup steps | 200 | 1000 | 1000 |
| Batch size | 32 | 32 | 32 |
| Optimizer | Adam | Adam | Adam |

## Text Classification

[p. 17] For classification, following BERT, a simple binary cross entropy loss on top of a first `[CLS]` token is used with addition of global attention to `[CLS]`. Adam optimizer is used with batch sizes of 32 and linear warmup and decay with warmup steps equal to 0.1 of the total training steps. For both IMDB and Hyperpartisan news, a grid search of LRs [3e-5, 5e-5] and epochs [10, 15, 20] is done and the model with LR [3e-5] and epochs 15 works best. Experiments were done on a single RTX8000 GPU.
