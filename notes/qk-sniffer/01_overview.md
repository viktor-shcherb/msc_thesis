# QK-Sniffer: Overview

## Purpose

**qk-sniffer** is a research tool that captures attention mechanism vectors (query and key vectors) from Hugging Face transformer models during inference and publishes them as structured Hugging Face datasets.

Source: https://github.com/viktor-shcherb/qk-sniffer

## Problems Solved

1. **Attention Analysis**: Enables researchers to study what attention mechanisms learn by sampling attention vectors from different layers and heads

2. **Data Collection Scale**: Automatically instruments transformer models to capture vectors without modifying user code

3. **Dataset Management**: Efficiently manages large-scale vector captures with deterministic sampling and branch-per-model Hub organization

4. **Hub Integration**: Publishes captures to Hugging Face Hub as datasets (one branch per model) for community research

5. **Model Coverage**: Provides pre-instrumented versions of popular models with attention hooks already embedded

## High-Level Workflow

```
Load Dataset → Patch Model → Prepare Model & Tokenizer → Run Inference
    ↓
    Model backbone called directly (no lm_head, no KV cache)
    ↓
    During forward pass: Hook captures Q/K vectors from each attention layer
    ↓
    CPU-side sampling → Dense (n_heads, K, dim) gather → In-memory accumulation
    ↓
    After all inference: Write Parquet files → Hub Upload
```

## Supported Models

- Gemma 3
- GLM & GLM-4
- Llama 3
- Ministral
- Mllama (Llama 3.2 Vision)
- Qwen 2 & 3
