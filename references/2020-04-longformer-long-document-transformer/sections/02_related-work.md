# Related Work [p. 2-3]

## Long-Document Transformers

[p. 2] Tab. 1 summarizes recent prior work on long documents. Two types of self-attention approaches have been explored:

1. **Left-to-right (ltr) approach:** processes the document in chunks moving from left-to-right. While successful in autoregressive language modeling, these models are unsuitable for transfer learning approaches with tasks that benefit from bidirectional context.

2. **Sparse attention pattern approach:** defines some form of sparse attention pattern and avoids computing the full quadratic attention matrix multiplication. Longformer falls within this category.

The model with the most similar attention pattern to Longformer is Sparse Transformer (Child et al., 2019), which uses a form of dilated sliding window of blocks of size 8x8 provided by BlockSparse (Gray et al., 2017). Longformer's implementation (section 3) also includes a custom CUDA kernel, but it is more flexible and maintainable than BlockSparse which is implemented in C++, and designed for a specific version of TensorFlow. Longformer also introduces additional task motivated global attention patterns suitable for common NLP tasks (section 3) and shows they are essential for good performance in the transfer learning setting.

[p. 2-3] A few models tried tasks other than autoregressive language modeling, which is a step forward because arguably focusing on language modeling as the primary evaluation has led to the development of models with limited applicability:
- **BP-Transformer** (Ye et al., 2019): evaluated on machine translation (MT), but didn't explore the pretrain-finetune setting.
- **Blockwise attention** (Qiu et al., 2019): pretrained their models and evaluated on question answering (QA). However, the evaluation is limited as it doesn't include language modeling, and the QA datasets are of relatively short documents, therefore the effectiveness of this model on long document tasks remains unexplored.

### Table 1: Summary of prior work on adapting Transformers for long documents [p. 2]

ltr: left-to-right.

| Model | attention matrix | char-LM | other tasks | pretrain |
|---|---|---|---|---|
| Transformer-XL (2019) | ltr | yes | no | no |
| Adaptive Span (2019) | ltr | yes | no | no |
| Compressive (2020) | ltr | yes | no | no |
| Reformer (2020) | sparse | yes | no | no |
| Sparse (2019) | sparse | yes | no | no |
| Routing (2020) | sparse | yes | no | no |
| BP-Transformer (2019) | sparse | yes | MT | no |
| Blockwise (2019) | sparse | no | QA | yes |
| Our Longformer | sparse | yes | multiple | yes |

## Task-specific Models for Long Documents

[p. 3] Many task-specific approaches have been developed to work around the 512 limit of pretrained transformer models like BERT:
- **Truncation:** simplest approach, commonly used for classification (Xie et al., 2019).
- **Chunking:** chunks the document into chunks of length 512 (could be overlapping), processes each chunk separately, then combines the activations with a task specific model (Joshi et al., 2019).
- **Two-stage retrieval:** popular for multihop and open domain QA tasks; first stage retrieves relevant documents, second stage performs answer extraction (Clark and Gardner, 2017; Chen et al., 2017). All of these approaches suffer from information loss due to truncation or cascading errors from the two stage approach.

Note: SQuAD contexts typically fit within the 512 limit, and MRQA is constructed by dropping long-document examples (footnote 2, p. 3).

In contrast, Longformer can process long sequences without truncating or chunking, allowing a much simpler approach that concatenates the available context and processes it in a single pass.

## Contemporaneous works

[p. 3] A few contemporaneous works (all published on arXiv after Longformer, footnote 3) have explored similar ideas to Longformer using local + global attention in Transformers, and pre-training it for long document NLP tasks:
- **ETC** (Ainslie et al., 2020): uses a similar local + global attention instead of full self-attention to scale Transformers to long documents. Different from Longformer, ETC uses relative position embeddings (which Longformer only uses for the autoregressive LM setting), introduces an additional training objective (CPC loss) for pre-training, and configures global attention in a slightly different way. Shows strong results on several tasks including reading comprehension and classification.
- **GMAT** (Gupta and Berant, 2020): uses a similar idea of few global locations in the input serving as global memory.
- **BigBird** (Zaheer et al., 2020): an extension over ETC with evaluation on additional tasks, including summarization. Importantly, through theoretical analysis, BigBird shows that sparse Transformers are universal approximators of sequence functions and preserve these properties of the full self-attention.
