# Pretraining and Finetuning [p. 6]

[p. 6] Current state-of-the-art systems for many NLP tasks finetune a pretrained model with task supervision (e.g. BERT). One of the main motivations is to develop such a model suitable for long document tasks. To do so, Longformer is pretrained on a document corpus and finetuned for six tasks, including classification, QA and coreference resolution. The resulting model can process sequences up to 4,096 tokens long (8 times longer than BERT).^5 Sequences up to 16K are possible on current GPUs.

^5 Footnote, p. 6.

Longformer is pretrained with masked language modeling (MLM), where the goal is to recover randomly masked tokens in a sequence. Since MLM pretraining is expensive, the authors continue pre-training from the RoBERTa (Liu et al., 2019) released checkpoint, while only making the minimal changes necessary to support Longformer's attention mechanism. The attention pattern can be plugged into any pretrained transformer model without the need to change the model architecture.

## Attention Pattern

[p. 6] Sliding window attention with window size of 512 is used, therefore using the same amount of computation as RoBERTa. Adding dilation on a few heads as in section 4.1 hurt performance, likely because it is not compatible with the pretrained RoBERTa weights (footnote 6, p. 6). Retraining such model from scratch might be needed to improve performance.

## Position Embeddings

[p. 6] RoBERTa uses learned absolute position embeddings with the maximum position being 512. To support longer documents, extra position embeddings are added to support up to position 4,096. To leverage RoBERTa's pretrained weights, instead of randomly initializing the new position embeddings, they are initialized by copying the 512 position embeddings from RoBERTa multiple times as analysis of BERT's attention heads shows a strong learned bias to attending to local context, including the previous or next token (Clark et al., 2019). Using the copy initialization preserves this local structure everywhere except at the partition boundaries. Despite its simplicity, this is found to be very effective (see Tab. 5), allowing Longformer pretraining to rapidly converge with a small number of gradient updates.

## Continued MLM Pretraining

[p. 6] Longformer is pretrained using fairseq (Ott et al., 2019) on a corpus of long documents that was compiled (see Appendix C for corpus details). Two model sizes are trained: a base model and a large model.

Training hyperparameters:
- **Gradient updates:** 65K
- **Sequence length:** 4,096
- **Batch size:** 64 (2^18 tokens)
- **Maximum learning rate:** 3e-5
- **Linear warmup:** 500 steps
- **Decay:** power 3 polynomial decay
- The rest of the hyperparameters are the same as RoBERTa.

### Table 5: MLM BPC for RoBERTa and various pretrained Longformer configurations [p. 6]

| Model | base | large |
|---|---|---|
| RoBERTa (seqlen: 512) | 1.846 | 1.496 |
| Longformer (seqlen: 4,096) | 10.299 | 8.738 |
| + copy position embeddings | 1.957 | 1.597 |
| + 2K gradient updates | 1.753 | 1.414 |
| + 65K gradient updates | 1.705 | 1.358 |
| Longformer (train extra pos. embed. only) | 1.850 | 1.504 |

[p. 6] Tab. 5 shows the BPC on the development set of the training corpus. The first row shows a 1.846 BPC for RoBERTa base. Row 2 shows that simply increasing the sequence length to 4,096 results in a large BPC (10.299 base / 8.738 large) due to untrained position embeddings. Copying position embeddings brings it down dramatically (1.957 / 1.597). After 2K gradient updates the model already improves substantially (1.753 / 1.414), and after 65K gradient updates it reaches 1.705 / 1.358. The last row shows that training only the extra position embeddings (freezing the rest) results in 1.850 / 1.504, which is close to the original RoBERTa performance, confirming that copy initialization is effective.

---
[p. 7 continued]

[p. 7] BPC using RoBERTa-base is comparable to the 1.880 BPC reported on the RoBERTa paper on their corpus. This indicates the training corpus is from a distribution close to that used to train RoBERTa. The following two rows show the performance of Longformer before pretraining with randomly initialized position embeddings and with copied position embeddings. The significant difference indicates the importance of the copy initialization, and the relative small difference between the RoBERTa BPC and the initialized BPC indicates that the sliding window attention is working well with the RoBERTa weights. The following two rows show the impact of continuing pretraining. Training for 2K steps improves BPC from 1.957 to 1.753, which further decreases to 1.705 after 65K steps, demonstrating the model is learning to better utilize the sliding window attention and longer context. Similar patterns are observed with RoBERTa-large and Longformer-large.

## Frozen RoBERTa Weights

[p. 7] The authors also pretrained Longformer while freezing all RoBERTa weights and only training the new position embeddings. The motivation for this configuration is to perfectly preserve the RoBERTa performance on short documents. This configuration has a BPC of 1.850 (down from 1.957 at initialization), but higher than 1.705 where all the weights are trainable.
