# 1 Introduction [p. 1-2]

## Context and motivation

[p. 1] Models based on Transformers [91], such as BERT [22, 63], are widely successful for a wide variety of NLP tasks. Their versatility and robustness are the primary drivers behind the wide-scale adoption of Transformers. The model is easily adapted for a diverse range of sequence-based tasks: as a seq2seq model for translation [91], summarization [66], generation [15], or as a standalone encoder for sentiment analysis [83], POS tagging [65], machine reading comprehension [93], etc. Transformers are known to vastly outperform previous sequence models like LSTM [37].

The key innovation in Transformers is self-attention, which can be evaluated in parallel for each token, eliminating the sequential dependency of RNNs. This parallelism enables leveraging modern SIMD hardware accelerators (GPUs/TPUs) and training on datasets of unprecedented size. This has led to models like BERT [22] and T5 [75], which pretrain on large general-purpose corpora and transfer knowledge to downstream tasks. Pretraining has led to significant improvement in both low data regime downstream tasks [51] and tasks with sufficient data [101].

## Quadratic bottleneck

[p. 1-2] The full self-attention has computational and memory requirements that are quadratic in the sequence length. Using commonly available current hardware and model sizes, this translates to roughly handling input sequences of length 512 tokens, reducing direct applicability to tasks requiring larger context, like QA [60] and document classification.

## Expressivity questions

[p. 2] Theoretical understanding of self-attention is rudimentary. It was not even clear that the proposed self-attention mechanism was as effective as RNNs. Self-attention does not even obey sequence order as it is permutation equivariant. Yun et al. [104] showed that transformers are expressive enough to capture all continuous sequence-to-sequence functions with a compact domain. Perez et al. [72] showed that the full transformer is Turing Complete (i.e. can simulate a full Turing machine).

Two natural questions arise:
1. Can we achieve the empirical benefits of a fully quadratic self-attention scheme using fewer inner-products?
2. Do sparse attention mechanisms preserve the expressivity and flexibility of the original network?

## Paper contribution summary

[p. 2] The authors address both questions by systematically developing BIGBIRD, an attention mechanism whose complexity is linear in the number of tokens (Sec. 2). They take inspiration from graph sparsification methods and understand where the proof for expressiveness of Transformers breaks down when full-attention is relaxed.

BIGBIRD consists of three main parts:
- A set of *g* global tokens attending on all parts of the sequence
- All tokens attending to a set of *w* local neighboring tokens
- All tokens attending to a set of *r* random tokens

This leads to a high-performing attention mechanism scaling to much longer sequence lengths (8x).

## Main contributions

[p. 2]

1. **Theoretical properties (Sec. 3):** BIGBIRD satisfies all the known theoretical properties of full transformer. Adding extra tokens allows expressing all continuous sequence-to-sequence functions with only O(n)-inner products. Under standard assumptions regarding precision, BIGBIRD is Turing complete.

2. **Empirical NLP results (Sec. 4):** The extended context modelled by BIGBIRD benefits a variety of NLP tasks. They achieve *state of the art* results for question answering and document summarization on a number of different datasets.

3. **Genomics application (Sec. 5):** A novel application of attention-based models where long contexts are beneficial: extracting contextual representations of genomics sequences like DNA. With longer masked LM pretraining, BIGBIRD improves performance on downstream tasks such as promoter-region and chromatin profile prediction.

## 1.1 Related Work [p. 2-3]

### Direction 1: Selecting relevant context

[p. 2] First line of work embraces the length limitation and develops methods around it. Simplest methods employ a sliding window [93], but in general most work fits a general paradigm: using some mechanism to select a smaller subset of relevant contexts to feed into the transformer, optionally iterating (calling the transformer block multiple times with different contexts each time). Most prominently, SpanBERT [42], ORQA [54], REALM [34], RAG [57] have achieved strong performance for different tasks. However, these methods often require significant engineering efforts (like back prop through large-scale nearest neighbor search) and are hard to train.

### Direction 2: Reducing attention complexity

[p. 2-3] The second line of work tries to come up with approaches that do not require full attention, thereby reducing memory and computation requirements:
- Dai et al. [21], Sukhbaatar et al. [82], Rae et al. [74] proposed auto-regressive models that work well for left-to-right language modeling but suffer in tasks requiring bidirectional context.
- Child et al. [16] proposed a sparse model that reduces complexity to O(n sqrt(n)).
- Kitaev et al. [49] further reduced complexity to O(n log(n)) by using LSH to compute nearest neighbors.
- Ye et al. [103] proposed binary partitions of the data.
- Qiu et al. [73] reduced complexity by using block sparsity.
- Longformer [8] introduced a localized sliding window based mask with few global tokens to reduce computation and extended BERT to longer sequence based tasks.
- Extended Transformers Construction [4] is closely related; the idea of global tokens was used extensively by them.

[p. 3] The authors' theoretical work can be seen as providing a justification for the success of these models as well. Most of the aforementioned methods are heuristic-based and empirically are not as versatile and robust as the original transformer, i.e. the same architecture does not attain SoTA on multiple standard benchmarks. (One exception is Longformer, included in all their comparisons; see App. E.3 for a more detailed comparison.) Moreover, these approximations do not come with theoretical guarantees.
