# F Genomics experiments details [p. 39-42]

[p. 39] This appendix provides details of the experimental setup for BIGBIRD on genomics data.

## F.1 Pretraining [p. 39-40]

[p. 39] The experimental setup is kept as close to a typical NLP pipeline as possible. The human reference genome GRCh37 is taken and converted into documents D. Each document d in D is a sequence of sentences, where each sentence is a sequence of fragments of DNA. The documents are constructed as follows:

1. Start with empty document set D = emptyset.
2. For each chromosome C, repeat the following procedure 10 times.
   (a) Pick uniformly at random a starting point q between base pairs 0 and 5000 from the 5' end.
   (b) Repeat until q > |C|:
       i. Pick uniformly at random s, a number between 50 and 100, to denote number of sentences per document.
       ii. Construct a document d containing s sentences using consecutive base pairs (bps). The length of each sentence is chosen uniformly at random between 500-1000. Thus the resulting document has 25,000 - 100,000 bps.
       iii. D = D union d
       iv. q = q + |d|

[p. 39] By this procedure approximately 450K documents are obtained.

[p. 39] Sentencepiece [50] tokenization is run on the resulting documents. In particular, using 5 characters as the building blocks (four for bases -- A, T, C, G and one for missing symbol N), a byte pair encoding table of size 32k is constructed, with each token representing 8.78 base pairs on average.

[p. 39] Using the above constructed documents, a dataset is constructed for two pretraining tasks following Devlin et al. [22]:

- **Masked Language Model (MLM):** In order to train a deep bidirectional representation, BERT training introduces the MLM task, where 15% of the input tokens are simply masked out at random, and then those masked tokens are predicted. The masked tokens can be replaced with a [MASK] placeholder, but it leads to a distribution mismatch for downstream tasks which will not have such placeholders. To mitigate this issue, out of the 15% of the tokens selected for masking:
  - 80% of the tokens are actually replaced with the token [MASK].
  - 10% of the time tokens are replaced with a random token.
  - 10% of the time tokens are left unchanged, but are still predicted at output.
  The entire sequence is run through the BIGBIRD transformer encoder and then predictions corresponding to the masked positions are made, based on the context provided by the other non-masked tokens in the sequence.

- **Next Sentence Prediction (NSP):** In order to understand relationship between two sequences, BERT training introduces the NSP task, where the model predicts if a given pair of sequences are contiguous or not. During training the model gets as input pairs of sequences separated by [SEP] token along with a [CLS] token at the start. Overall the input pattern is: [CLS] sequence A [SEP] sequence B [SEP]. For 50% of the time the second sequence comes from true sequence after the first one. Remaining 50% of the time it is a random sequence from the full dataset. The model is then required to predict this relationship using the output corresponding to the [CLS] token, which is fed into a simple binary classification layer.

[p. 40] The model is trained with both MLM and NSP together. Training hyperparameters are provided in the second column of Tab. 21. In all experiments, a learning rate warmup over the first 10,000 steps and linear decay of the learning rate are used.

[p. 40] An ablation study is additionally performed to validate the hypothesis that, similar to NLP, having a larger context improves performance. The MLM task described above is used to test how BIGBIRD performed with sequences of different length. Accuracy on the MLM task with increasing sequence length is shown in Fig. 8. Not only does longer context improve final accuracy, it also leads to faster learning, as there are more opportunities for masking.

**Figure 7** (p. 40): "Visual description of how the masked language modeling data was generated from raw DNA dataset. The raw DNA sequences of GRCh37, where split at random positions to create documents with 50-100 sentences where each sentence was 500-1000 base pairs (bps). Thus each document had a continuous strand of 25000-100,000 bps of DNA. This process was repeated 10 times to create 10 sets of document for each chromosome of GRCH37. The resulting set of documents was then passed through Sentencepiece that created tokens of average 8bp. For pretraining we used masked language model and masked 10% of the tokens and trained on predicting the masked tokens."

The figure shows a pipeline with three stages:
- Top: A raw DNA sequence (T G G G C T A A C A A G C A A A T G A T C T G T) is split into sentences (two rows of tokens).
- Middle ("Sentencepiece"): The sentences are tokenized into subword units, shown as grouped colored blocks.
- Bottom ("Masking"): Some tokens are masked (shown as blank/grey blocks), producing the final training input.

**Figure 8** (p. 40): "BIGBIRD accuracy with context length."

The figure is a line plot with:
- X-axis: Steps (0 to 5, in units of 1e5, i.e. 0 to 500,000 steps)
- Y-axis: MLM Accuracy (14 to 28)
- Three lines for context lengths 512, 1024, and 4096.
- All three curves rise steeply initially and then level off.
- The 4096 context length achieves the highest final accuracy (~27), followed by 1024 (~24), then 512 (~22).
- Longer context also leads to faster initial learning.

## F.2 Promoter Region Prediction [p. 40-41]

[p. 40] The promoter region plays an important role in transcription initiation and thus its recognition is an important area of interest in bioinformatics. Following Oubounyt et al. [71], datasets from Eukaryotic Promoter Database (EPDnew) [24] are used, which contains 29,597 promoter regions in the human genome. Around the transcription start site (TSS), a sequence of 8000 bp (-5000 +3000 bp) is extracted from the human reference genome GRCh37. Since EPDnew uses newer GRCh38, coordinates are converted to GRCh37 using LiftOver [44].

[p. 41] Following Oubounyt et al. [71], for each promoter region example, a negative example (non-promoter sequence) with the same size of the positive one is constructed as follows: The positive sequence is divided into 20 subsequences. Then, 12 subsequences are picked randomly and substituted randomly. The remaining 8 subsequences are conserved. This process is illustrated in Figure 1 of [71]. Applying this process to the positive set results in new non-promoter sequences with conserved parts from promoter sequences (the unchanged subsequences, 8 subsequences out of 20). These parameters enable generating a negative set that has 32 and 40% of its sequences containing conserved portions of promoter sequences.

[p. 41] Each example is prefixed and appended with [CLS] and [SEP] token respectively. The output corresponding to the [CLS] token from BIGBIRD transformer encoder is fed to a simple binary classification layer. The pretrained BIGBIRD from App. F.1 is fine-tuned using hyper-parameters described in Tab. 21. High performance is noted as not surprising due to the overlap in the nature of negative example generation and MLM pretraining.

## F.3 Chromatin-Profile Prediction [p. 41-42]

[p. 41] The first step of a sequence-based algorithmic framework for predicting non-coding effects is to build a model to predict large scale chromatic profile [109]. The dataset provided in Zhou and Troyanskaya [109] is used to train BIGBIRD to predict the chromatin profile.

[p. 42] Each training sample consists of a 8,000-bp sequence from the human GRCh37 reference genome centered on each 200 bp bin and is paired with a label vector for 919 chromatin features. As before, each example is prefixed and appended with [CLS] and [SEP] token respectively. The output corresponding to the [CLS] token from BIGBIRD transformer encoder is fed to a linear layer with 919 heads. Thus 919 independent binary classification problems are jointly predicted. The pretrained BIGBIRD from App. F.1 is fine-tuned using hyper-parameters described in Tab. 21. As the data is highly imbalanced (way more negative examples than positive examples), the loss function for positive examples is upweighted by a factor of 8.

[p. 42] Training and testing splits provided by Zhou and Troyanskaya [109] are used, with chromosomes and strictly non-overlapping. Chromosome 8 and 9 were excluded from training to test chromatin feature prediction performances, and the rest of the autosomes were used for training and validation. 4,000 samples on chromosome 7 spanning the genomic coordinates 30,508,751-35,296,850 were used as the validation set.

[p. 42] As the predicted probability for each sequence in DeepSea Zhou and Troyanskaya [109] was computed as the ensemble average of the probability predictions for the forward and complementary sequence pairs, prediction is also done using an ensemble of two BIGBIRD models trained independently.

**Figure 9** (p. 41): "Visual description of the DNA segment from which we predict the chromatin profile for a given non-coding region of the raw DNA sequences of GRCh37. We take 8000 bps of DNA before and after the given non-coding region as context. The complete fragment of DNA including the context on both side, is then tokenized to form our input sequence of tokens. The task is to predict 919 chromatin profile including 690 transcription factors (TF) binding profiles for 160 different TFs, 125 DNase I sensitivity (DHS) profiles and 104 histone-mark (HM) profiles"

The figure shows a pipeline:
- Top: A DNA sequence with annotations showing "Context 5000 bp" on the left, "Predict Epigenetic Features of 200 bp non-coding region" in the middle, and "Context 3000 bp" on the right.
- Middle ("Sentencepiece"): The full DNA fragment (including context) is tokenized into subword units.
- Bottom: The tokenized sequence shown as grouped colored blocks, ready for input to the model.

### Table 21 (p. 41)

**Table 21:** Table of hyperparameters for Computational biology.

| Parameter | Pretraining | Promoter Region | Chromatin-Profile |
|---|---|---|---|
| Block length, b | 64 | 64 | 64 |
| Global token location | ITC | ITC | ITC |
| # of global token, g | 2 x b | 2 x b | 2 x b |
| Window length, w | 3 x b | 3 x b | 3 x b |
| # of random token, r | 3 x b | 3 x b | 3 x b |
| Max. Sequence Length | 4096 | 4096 | 4096 |
| # of heads | 12 | 12 | 12 |
| # of hidden layers | 12 | 12 | 12 |
| Hidden layer size | 768 | 768 | 768 |
| Batch Size | 256 | 256 | 256 |
| Vocab Size | 32000 | 32000 | 32000 |
| Loss | MLM+NSP | BCE | 919 x +ve unweighted BCE |
| Dropout prob | 0.1 | 0.1 | 0.1 |
| Optimizer | Adam | Adam | Adam |
| Learning rate | 0.0001 | 0.0001 | 0.0001 |
| # of steps | 1000000 | 711 | 500000 |
| Compute Resources | 8 x 8 TPUv3 | 8 x 8 TPUv3 | 8 x 8 TPUv3 |
