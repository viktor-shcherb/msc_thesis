# 5.5. Vision encoder [p. 8]

## Impact of image encoder input resolution

**Table 7** (p. 8): "Impact of image encoder input resolution. We measure performance using a short schedule 2B Gemma model on a few evaluation benchmarks to observe the effect of image resolution on vision encoder pre-training."

| Resolution | DocVQA | InfoVQA | TextVQA |
|------------|--------|---------|---------|
| 256        | 31.9   | 23.1    | 44.1    |
| 448        | 45.4   | 31.6    | 53.5    |
| 896        | 59.8   | 33.7    | 58.0    |

We use a vision encoder based on SigLIP (Zhai et al., 2023). The vision encoder is frozen, and only the language model is trained. Each row in this multimodal data is represented by 256 image tokens from the respective vision encoder. The higher resolution encoders thus use average pooling to reduce their output to 256 tokens. For instance, the 896 resolution encoder has a 4x4 average pooling on its output. As shown in Table 7, higher resolution encoders perform better than smaller ones.

## Impact of Pan & Scan (P&S)

**Table 8** (p. 8): "Impact of P&S. 4-shot evaluation results on the valid set, with and without P&S on a pre-trained checkpoint. Boosts are on tasks associated with images with varying aspect ratios, or involving reading text on images."

|          | DocVQA | InfoVQA | TextVQA |
|----------|--------|---------|---------|
| 4B       | 72.8   | 44.1    | 58.9    |
| 4B w/ P&S| 81.0   | 57.0    | 60.8    |
| Δ        | (+8.2) | (+12.9) | (+1.9)  |
| 27B      | 85.6   | 59.4    | 68.6    |
| 27B w/ P&S| 90.4  | 76.4    | 70.2    |
| Δ        | (+4.8) | (+17.0) | (+1.6)  |

Pan & Scan. P&S enables capturing images at close to their native aspect ratio and image resolution. In Table 8, we compare our 27B IT model with and without P&S. As expected, the ability to treat images with close to native resolution greatly helps with tasks that require some form of reading text on images, which is particularly important for visual language models.
