# SmolLM3 training configurations [https://huggingface.co/datasets/HuggingFaceTB/smollm3-configs]

**Type:** documentation
**Fetched:** 2026-02-14
**Priority:** supplementary

## Available Information

The SmolLM3-3B-Base model was trained in **5 stages** with detailed configuration files provided.

### Training Stages

**Pretraining (4k context)**:

- **Stage 1**: [config file](https://huggingface.co/datasets/HuggingFaceTB/smollm3-configs/blob/main/stage1_8T.yaml)
- **Stage 2**: [config file](https://huggingface.co/datasets/HuggingFaceTB/smollm3-configs/blob/main/stage2_8T_9T.yaml)
- **Stage 3**: [config file](https://huggingface.co/datasets/HuggingFaceTB/smollm3-configs/blob/main/stage3_9T_11T.yaml)

**Context Extension (to 64k)**:

- **Stage 4**: [config file](https://huggingface.co/datasets/HuggingFaceTB/smollm3-configs/blob/main/long_context_4k_to_32k.yaml)
- **Stage 5**: [config file](https://huggingface.co/datasets/HuggingFaceTB/smollm3-configs/blob/main/long_context_32k_to_64.yaml)

### Confirmed Token Counts

- **Total pretraining tokens**: 11.2T tokens
- **Stage progression**: 8T → 9T → 11T (stages 1-3)
- **Context lengths**: 4k (stages 1-3) → extended to 64k (stages 4-5)

## Accessing Full Configuration Details

The page includes an important note for accessing complete configurations:

> For the latest complete configurations, visit the official repository:
> https://github.com/huggingface/smollm/tree/main/text/pretraining/smollm3

The actual hyperparameter details (learning rates, batch sizes, optimizer settings, etc.) are stored in YAML configuration files that are not displayed in the webpage content but are available in the linked repository.

## Note

[not accessible: The webpage provides links to configuration files rather than displaying the full hyperparameter details inline. The actual detailed configurations including learning rates, batch sizes, optimizer settings, and other hyperparameters are stored in separate YAML files. The main technical blog post provides the key hyperparameters used across pretraining - see source file 01_blog-post-main-technical-report.md for those details.]
