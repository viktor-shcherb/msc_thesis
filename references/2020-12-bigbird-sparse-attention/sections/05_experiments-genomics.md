# 5 Experiments: Genomics [p. 9-10]

[p. 9] There has been a recent upsurge in using deep learning for genomics data [86, 106, 13], which has resulted in improved performance on several biologically-significant tasks such as promoter site prediction [71], methylation analysis [55], predicting functional effects of non-coding variant [109], etc. These approaches consume DNA sequence fragments as inputs, and therefore the authors believe longer input sequence handling capability of BIGBIRD would be beneficial as many functional effects in DNA are highly non-local [12]. Furthermore, taking inspiration from NLP, they learn powerful contextual representations for DNA fragments utilizing abundant unlabeled data (e.g. human reference genome, Saccharomyces Genome Database) via MLM pretraining. They showcase that their long input BIGBIRD along with the proposed pretraining significantly improves performances in two downstream tasks. Detailed experimental setup for the two tasks is provided in App. F. [p. 9]

## Pre-training and MLM

[p. 9] As explored in Liang [58], instead of operating on base pairs, they propose to first segment DNA into tokens so as to further increase the context length (App. F, Fig. 7). In particular, they build a byte-pair encoding [50] table for the DNA sequence of size 32K, with each token representing 8.78 base pairs on average. They learn contextual representation of these tokens on the human reference genome (GRCh37) using MLM objective. They then report the bits per character (BPC) on a held-out set in Tab. 5. They find that attention based contextual representation of DNA does improve BPC, which is further improved by using longer context. [p. 9]

### Table 5 (p. 9)

**Table 5:** MLM BPC

| Model | BPC |
|---|---|
| SRILM [58] | 1.57 |
| BERT (sqln. 512) | 1.23 |
| BIGBIRD (sqln. 4096) | **1.12** |

## Promoter Region Prediction

[p. 9] Promoter is a DNA region typically located upstream of the gene, which is the site of transcription initiation. Multiple methods have been proposed to identify the promoter regions in a given DNA sequence [99, 59, 11, 98, 71], as it is an important first step in understanding gene regulation. The corresponding machine learning task is to classify a given DNA fragment as promoter or non-promoter. They use the dataset compiled by Oubounyt et al. [71] which was built from Eukaryotic Promoter Database (EPDnew) [24]. They finetuned the pretrained BIGBIRD model from above, using the training data and report F1 on test dataset. They compare their results to the previously reported best method in Tab. 6. BIGBIRD achieves nearly perfect accuracy with a **5% jump** from the previous best reported accuracy. [p. 9]

### Table 6 (p. 9)

**Table 6:** Comparison.

| Model | F1 |
|---|---|
| CNNProm [90] | 69.7 |
| DeePromoter [71] | 95.6 |
| BIGBIRD | **99.9** |

## Chromatin-Profile Prediction

[p. 10] Non-coding regions of DNA do not code for proteins. Majority of diseases and other trait associated single-nucleotide polymorphism are correlated to non-coding genomic variations [109, 46]. Thus, understanding the functional effects of non-coding regions of DNA is a very important task. An important step in this process, as defined by Zhou and Troyanskaya [109], is to predict large-scale chromatin-profiling from non-coding genomic sequence. To this effect, DeepSea [109] compiled 919 chromatin-profiles of 2.4M non-coding variants from Encyclopedia of DNA Elements (ENCODE) and Roadmap Epigenomics projects. The corresponding ML task is to predict, for a given non-coding region of DNA, these 919 chromatin-profiles including 690 transcription factors (TF) binding profiles for 160 different TFs, 125 DNase I sensitivity (DHS) profiles, and 104 histone-mark (HM) profiles. They jointly learn 919 binary classifiers to predict these functional effects from sequence of DNA fragments. On held-out chromosomes, they compare AUC with the baselines in Tab. 7 and see that they significantly improve on performance on the harder task HM, which is known to have longer-range correlations [27] than others. [p. 10]

### Table 7 (p. 10)

**Table 7:** Chromatin-Profile Prediction

| Model | TF | HM | DHS |
|---|---|---|---|
| gkm-SVM [30] | 89.6 | - | - |
| DeepSea [109] | 95.8 | 85.6 | **92.3** |
| BIGBIRD | **96.1** | **88.7** | 92.1 |
