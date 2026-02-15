# Model Architecture [p. 2–4]

## General architecture [p. 2]

Gemma 3 models follow the same general decoder-only transformer architecture as previous iterations (Vaswani et al., 2017), with most architecture elements similar to the two Gemma versions. The authors use a Grouped-Query Attention (GQA) (Ainslie et al., 2023) with post-norm and pre-norm with RMSNorm (Zhang and Sennrich, 2019). Inspired by Dehghani et al. (2023), Wortsman et al. (2023) and Chameleon Team (2024), the authors replace the soft-mapping of Gemma 2 with QK-norm. In this section, they focus on some key differences from previous versions below.

### 5:1 interleaving of local/global layers [p. 2]

The authors alternate between a local sliding window self-attention (Beltagy et al., 2020) and global self-attention, with a pattern of 5 local layers for every global layer, starting with a local layer as the first layer of the model.

The authors use a Grouped-Query Attention (GQA) with post-norm and pre-norm with RMSNorm.

### Long context [p. 2]

Gemma 3 models support context length of 128K tokens, with the exception of the 1B model that has 32K. The authors increase RoPE base frequency from 10k to 1M on global self-attention layers, and keep the frequency of the local layers at 10k. The authors follow a process similar to the positional interpolation of Chen et al. (2023) to extend the span of the global self-attention layers.

**Table 1** | Parameter counts for the Gemma 3 models. The vocabulary has 256k entries.

| Model | Vision Embedding Encoder | Parameters | Non-embedding Parameters |
|-------|--------------------------|------------|--------------------------|
| 1B    | 0                        | 302M       | 698M                     |
| 4B    | 417M                     | 675M       | 3,209M                   |
| 12B   | 417M                     | 1,012M     | 10,759M                  |
| 27B   | 417M                     | 1,416M     | 25,600M                  |

## 2.1. Vision modality [p. 2]

### Vision encoder [p. 2]

The authors use a 400M variant of the SigLIP encoder (Zhai et al., 2023), a Vision Transformer (Dosovitskiy, 2020) trained with a variation of the CLIP loss (Radford et al., 2021). The Gemma vision encoder takes as input square images resized to 896 × 896, and is finetuned on data from visual assistant tasks. For simplicity, the authors share the vision encoder across their 4B, 12B, and 27B models, keeping it frozen during training.

### Pan & Scan (P&S) [p. 2]

The Gemma vision encoder operates at a fixed resolution of 896 × 896. This results in artifacts when processing non-square aspect ratios and high-resolution images, leading to unreadable text, or small objects disappearing. The authors address this issue with an adaptive windowing algorithm during inference. This algorithm segments images into non-overlapping crops of equal size, covering the whole image, and resize them to 896×896 pixels to pass them to the encoder. This windowing is applied only when necessary, and control for the maximum number of crops. It is an inference-time only optimization and can be disabled for faster inference.

## 2.2. Pre-training [p. 3]

The authors follow a similar recipe as in Gemma 2 for pre-training with knowledge distillation.

### Training data [p. 3]

The authors pre-train their models on a slightly larger token budget than Gemma 2, i.e., they train on 14T tokens for Gemma 3 27B, 12T for the 12B version, 4T for the 4B, and 2T tokens for the 1B. The increase in tokens accounts for the mix of images and text used during pre-training. The authors also increase the amount of multilingual data to improve language coverage. They add both monolingual and parallel data, and they handle the imbalance in language representation using a strategy inspired by Chung et al. (2023).

### Tokenizer [p. 3]

The authors use the same tokenizer as Gemini 2.0: a SentencePiece tokenizer with split digits, preserved whitespace, and byte-level encodings (Kudo and Richardson, 2018). The resulting vocabulary has 262k entries. This tokenizer is more balanced for non-English languages.

### Filtering [p. 3]

The authors use filtering techniques that reduce the risk of unwanted or unsafe utterances and remove certain personal information and other sensitive data. They decontaminate evaluation sets from their pre-training data mixture, and reduce the risk of recitation by minimizing the proliferation of sensitive outputs. They also apply a quality reweighing step inspired by Sachdeva et al. (2024) to reduce occurrences of low quality data.

### Distillation [p. 3]

The authors sample 256 logits per token, weighted by teacher probabilities. The student learns the teacher's distribution within these samples via cross-entropy loss. The teacher's target distribution is set to zero probability for non-sampled logits, and renormalized.

**Table 2** | Training infrastructure with sharding by data, sequence (Seq.), and replica.

|       |         |        | Shards |      |         |
|-------|---------|--------|--------|------|---------|
| Model | Type    | #Chips | Data   | Seq. | Replica |
| 1B    | TPUv5e  | 512    | 16     | 16   | 2       |
| 4B    | TPUv5e  | 2048   | 16     | 16   | 8       |
| 12B   | TPUv4   | 6144   | 16     | 16   | 24      |
| 27B   | TPUv5p  | 6144   | 24     | 8    | 32      |

**Table 3** | Memory footprints (in GB) comparison between raw (bfloat16) and quantized checkpoints for weights and KV caching (+KV) at 32,768 context size, quantized in 8 bits.

|       |        | Raw (GB) |                   | Quantized (GB) |
|-------|--------|----------|-------------------|----------------|
| Model | bf16   | Int4     | Int4<sub>blocks=32</sub> | SFP8           |
| 1B    | 2.0    | 0.5      | 0.7               | 1.0            |
| +KV   | 2.9    | 1.4      | 1.6               | 1.9            |
| 4B    | 8.0    | 2.6      | 2.9               | 4.4            |
| +KV   | 12.7   | 7.3      | 7.6               | 9.1            |
| 12B   | 24.0   | 6.6      | 7.1               | 12.4           |
| +KV   | 38.9   | 21.5     | 22.0              | 27.3           |
| 27B   | 54.0   | 14.1     | 15.3              | 27.4           |
| +KV   | 72.7   | 32.8     | 34.0              | 46.1           |

## 2.3. Quantization Aware Training [p. 3]

Along with the raw checkpoints, the authors also provide quantized versions in four formats in different standard formats. These versions are obtained by fine-tuning each model for a small number of steps, typically 5,000, using Quantization Aware Training (QAT) (Jacob et al., 2018). The authors use probabilities from the non-quantized checkpoint as targets, and adapt the data to match the pre-training and post-training distributions. Based on the most popular open source quantization inference engines (e.g. llama.cpp), the authors focus on three weight formats: per-channel int4, per-block int4, and switched fp8. In Table 3, the authors report the memory filled by raw and quantized models for each weight quantization with and without a KV-cache for a sequence of 32k tokens.

## 2.4. Compute Infrastructure [p. 3–4]

The authors train their models with TPUv4, TPUv5e, and TPUv5p as outlined in Table 2. Each model configuration is optimized to minimize training step time. For the vision encoder, the authors pre-compute the embeddings for each image and directly train with the embeddings, adding no cost to the training of the language models.

The optimizer state is sharded using an implementation of ZeRO-3 (Ren et al., 2021). For multi-pod training, the authors perform a data replica reduction over the data center network, using the Pathways approach of Barham et al. (2022). The authors use the 'single controller' programming paradigm of Jax (Roberts et al., 2023) and Pathways (Barham et al., 2022), along with the GSPMD partitioner (Xu et al., 2021) and the MegaScale XLA compiler (XLA, 2019).
