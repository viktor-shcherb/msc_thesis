# QK-Sniffer: Overview

## Purpose

**qk-sniffer** is a research tool that captures attention mechanism vectors (query and key vectors) from Hugging Face transformer models during inference and publishes them as structured Hugging Face datasets.

## Problems Solved

1. **Attention Analysis**: Enables researchers to study what attention mechanisms learn by sampling attention vectors from different layers and heads

2. **Data Collection Scale**: Automatically instruments transformer models to capture vectors without modifying user code

3. **Dataset Management**: Efficiently manages large-scale vector captures with deduplication and deterministic sampling

4. **Hub Integration**: Seamlessly publishes captures to Hugging Face Hub as public datasets for community research

5. **Model Coverage**: Provides pre-instrumented versions of popular models (Llama, Gemma, Qwen, GLM) with attention hooks already embedded

## High-Level Workflow

```
Load Dataset → Patch Model → Prepare Model & Tokenizer → Run Inference
    ↓
    During forward pass: Hook captures Q/K vectors from each attention layer
    ↓
Deterministic Sampling → Deduplication → Parquet Storage → Hub Upload
```

## Supported Models

- Llama 3
- Gemma 3
- Qwen 2 & 3
- GLM & GLM-4
