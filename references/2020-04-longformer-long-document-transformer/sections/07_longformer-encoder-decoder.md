# Longformer-Encoder-Decoder (LED) [p. 9-10]

[p. 9] The original Transformer (Vaswani et al., 2017) consisted of an encoder-decoder architecture, intended for sequence-to-sequence tasks (Sutskever et al., 2014), such as summarization and translation. While encoder-only Transformers are effective on a variety of NLP tasks, pre-trained encoder-decoder Transformer models (e.g. BART (Lewis et al., 2020) and T5 (Raffel et al., 2020)) have achieved strong results on tasks like summarization. Yet, such models can't efficiently scale to seq2seq tasks with longer inputs.

To facilitate modeling long sequences for seq2seq learning, the authors propose a Longformer variant (LED) that has both the encoder and decoder Transformer stacks but instead of the full self-attention in the encoder, it uses the efficient local+global attention pattern of the Longformer. The decoder uses the full self-attention to the entire encoded tokens and to previously decoded locations. LED scales linearly with the input.

## Initialization and Architecture

[p. 9] Since pre-training LED is expensive, LED parameters are initialized from BART, and follow BART's exact architecture in terms of number of layers and hidden sizes. The only difference is that to process longer inputs, the position embedding is extended to 16K tokens (up from BART's 1K tokens) and the new position embedding matrix is initialized by repeatedly copying BART's 1K position embeddings 16 times as in Section 5 for RoBERTa. Following BART, two model sizes are released: LED-base and LED-large, which respectively have 6 and 12 layers in both encoder and decoder stacks.

## Evaluation on arXiv Summarization

[p. 9-10] LED is evaluated on the summarization task using the arXiv summarization dataset (Cohan et al., 2018) which focuses on long document summarization in the scientific domain. The 90th percentile of document lengths is 14.5K tokens, making it an appropriate testbed for evaluating LED.

LED's encoder reads the document and its decoder generates the output summary. The encoder uses local attention with window size 1,024 tokens and global attention on the first `<s>` token. The decoder uses full attention to the entire encoder and previously decoded locations. As standard in seq2seq models, LED is trained using teacher forcing on gold training summaries and uses beam search at inference.

### Table 11: Summarization results of Longformer-Encoder-Decoder (LED) on the arXiv dataset [p. 10]

Metrics from left to right are ROUGE-1, ROUGE-2 and ROUGE-L.

| Model | R-1 | R-2 | R-L |
|---|---|---|---|
| Discourse-aware (2018) | 35.80 | 11.05 | 31.80 |
| Extr-Abst-TLM (2020) | 41.62 | 14.69 | 38.03 |
| Dancer (2020) | 42.70 | 16.54 | 38.44 |
| Pegasus (2020) | 44.21 | 16.95 | 38.83 |
| LED-large (seqlen: 4,096) (ours) | 44.40 | 17.94 | 39.76 |
| BigBird (seqlen: 4,096) (2020) | **46.63** | 19.02 | 41.77 |
| LED-large (seqlen: 16,384) (ours) | **46.63** | **19.62** | **41.83** |

[p. 10] LED achieves state-of-the-art results on arXiv, slightly outperforming BigBird (Zaheer et al., 2020). Note that the BigBird summarization model supports sequence length of 4K tokens but starts from and continues pre-training Pegasus (Zhang et al., 2020), a model specifically designed and pre-trained for summarization. With no pre-training or task-specific initialization, but with ability to process longer inputs, LED can slightly outperform BigBird. Further improvements should be possible through pre-training of LED.

## Figure 3 (p. 10)

**Caption:** "ROUGE-1 and ROUGE-2 of LED when varying the input size (arXiv validation set)."

- **X-axis:** Input size (1K, 4K, 16K)
- **Y-axis:** ROUGE score
- Two lines plotted: R1 (blue circles) and R2 (green x-marks)
- **Data points:**
  - At 1K: R1 = 35.21, R2 = 11.54
  - At 4K: R1 = 44.48, R2 = 17.99
  - At 16K: R1 = 46.23, R2 = 19.62
- **Trend:** Both ROUGE-1 and ROUGE-2 increase substantially as input size increases from 1K to 16K, demonstrating that the ability to process longer input significantly improves summarization results.
- Supports the claim that processing longer sequences leads to better performance.
