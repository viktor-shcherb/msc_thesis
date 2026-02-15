# SmolLM GitHub repository [https://github.com/huggingface/smollm]

**Type:** github-repo
**Fetched:** 2026-02-14
**Priority:** primary

## Repository Statistics

- **Stars:** 3.6k
- **Forks:** 273
- **Contributors:** 21+
- **License:** Apache-2.0
- **Primary Language:** Python (76.2%), Shell (14.6%), Jupyter Notebook (8.8%)
- **Total Commits:** 196

## Repository Overview

The SmolLM repository from Hugging Face contains a family of efficient, lightweight AI models designed for on-device deployment. The repository houses implementations of SmolLM3/2/1 language models and SmolVLM vision-language models.

## Key Models

### SmolLM3 (Latest)

The newest release is a 3-billion parameter model with these capabilities:

- Trained on 11 trillion tokens
- > "State-of-the-art at the 3B scale and competitive with 4B models"
- Supports dual-mode reasoning (think/no_think)
- Multilingual: English, French, Spanish, German, Italian, Portuguese
- Extended context window: up to 128k tokens using YaRN
- Fully open weights with complete training transparency

### SmolVLM

A compact vision-language model enabling:

- Joint image and text processing
- Multi-image conversation support
- Visual question answering, captioning, storytelling
- On-device efficiency

## Repository Structure

```
smollm/
├── text/              # SmolLM3/2/1 implementations
├── vision/            # SmolVLM code
└── tools/             # Utilities and local inference
```

## Usage Examples

**SmolLM3 Implementation**:
The model loads via HuggingFace's transformers library using `AutoModelForCausalLM` and `AutoTokenizer`. Generation supports chat templates with configurable output lengths.

**SmolVLM Implementation**:
Uses `AutoProcessor` and `AutoModelForVision2Seq` for multimodal inference with structured message formatting.

## Resources Available

- Full documentation in respective README files
- Pre-trained model collections on Hugging Face Hub
- Training datasets: SmolTalk (instruction-tuning), FineMath, FineWeb-Edu
- Local inference guides for deployment
