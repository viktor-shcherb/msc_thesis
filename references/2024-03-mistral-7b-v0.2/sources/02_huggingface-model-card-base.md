# Hugging Face Model Card — Mistral-7B-v0.2 (community conversion)

**URL:** https://huggingface.co/mistral-community/Mistral-7B-v0.2
**Type:** documentation
**Fetched:** 2026-02-15
**Priority:** primary

## Base Model Details

- **Model Name**: Mistral-7B-v0.2
- **Organization**: mistral-community (Unofficial Mistral Community)
- **Model Size**: 7B parameters
- **Tensor Type**: BF16 (Brain Float 16)
- **License**: Apache 2.0
- **Framework**: Transformers, Safetensors

## Conversion Process

The model was converted from official Mistral CDN weights through the following steps:

### 1. Download Original Weights

```
https://models.mistralcdn.com/mistral-7b-v0-2/mistral-7B-v0.2.tar
```

### 2. Convert Using HuggingFace Script

```
https://github.com/huggingface/transformers/blob/main/src/transformers/models/mistral/convert_mistral_weights_to_hf.py
```

### 3. Additional Setup

- Copy tokenizer.model from Mistral-7B-Instruct-v0.2 repository

## Community Adoption Metrics

As of the fetch date, the model has the following community adoption statistics:

| Metric | Count |
|--------|-------|
| Likes | 228 |
| Downloads (last month) | 4,254 |
| Adapters | 10 |
| Fine-tunes | 36 |
| Merges | 14 |
| Quantizations | 27 |
| Spaces using model | 31 |
| Community discussions | 10 |

## Technical Specifications

- **Pipeline Tag**: Text Generation
- **Library**: Transformers, Safetensors
- **Model Type**: Mistral-based
- **Inference Provider**: Featherless AI
- **Format**: Safetensors

## Important Note

The model card includes a warning:

> ⚠️ This model checkpoint is provided as-is and might not be up-to-date. Please use the corresponding version from https://huggingface.co/mistralai org

This indicates that while the base model weights were released by Mistral AI through their CDN, the HuggingFace conversion and hosting was performed by the community rather than the official Mistral AI organization.
