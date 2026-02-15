# SmolLM3-3B-Base model card [https://huggingface.co/HuggingFaceTB/SmolLM3-3B-Base]

**Type:** documentation
**Fetched:** 2026-02-14
**Priority:** supplementary

## Model Specifications

SmolLM3-3B-Base is the base pre-trained model (for the instruct variant, see [SmolLM3-3B](https://huggingface.co/HuggingFaceTB/SmolLM3-3B)).

### Architecture & Training

- **Architecture:** Transformer decoder with GQA (Grouped Query Attention) and NoPE (No Positional Embeddings)
- **Parameters:** 3 billion
- **Pretraining tokens:** 11.2 trillion (11T)
- **Precision:** bfloat16
- **Context length:** Trained on 64k context, supports up to 128k tokens using YARN extrapolation
- **Languages:** 6 natively supported (English, French, Spanish, German, Italian, Portuguese) + 3 additional (Arabic, Chinese, Russian)

### Training Data

Staged curriculum of: web, code, math, and reasoning data

### Key Features

- Fully open model (open weights + full training details)
- Long context capability (128k tokens with YARN)
- Multilingual support
- Decoder-only transformer

## Hardware & Software Requirements

### Training Hardware

- **GPUs:** 384 H100
- **Training Framework:** [nanotron](https://github.com/huggingface/nanotron/tree/main)
- **Data processing:** [datatrove](https://github.com/huggingface/datatrove)
- **Evaluation:** [lighteval](https://github.com/huggingface/lighteval)
- **Post-training:** [TRL](https://github.com/huggingface/trl)

### Usage Requirements

```bash
pip install -U transformers
```

Requires transformers `v4.53.0+` or latest `vllm`

## Usage Instructions

### Basic Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

checkpoint = "HuggingFaceTB/SmolLM3-3B-Base"
device = "cuda"  # or "cpu"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint).to(device)

inputs = tokenizer.encode("Gravity is", return_tensors="pt").to(device)
outputs = model.generate(inputs)
print(tokenizer.decode(outputs[0]))
```

### Multi-GPU Usage

```python
model = AutoModelForCausalLM.from_pretrained(checkpoint, device_map="auto")
```

(requires `accelerate` package)

### Long Context Processing (128k/256k tokens)

Modify `config.json`:

```json
{
  "rope_scaling": {
    "factor": 2.0,
    "original_max_position_embeddings": 65536,
    "type": "yarn"
  }
}
```

### Alternative Inference Frameworks

- `llama.cpp`
- `ONNX`
- `MLX`
- `MLC`

[Quantized checkpoints collection](https://huggingface.co/collections/HuggingFaceTB/smollm3-686d33c1fdffe8e635317e23)

## Evaluation Results - Base Pre-Trained Model

### English Benchmarks (Zero-shot)

| Category | Metric | SmolLM3-3B | Qwen2.5-3B | Llama3-3.2B | Qwen3-1.7B-Base | Qwen3-4B-Base |
|----------|--------|-----------|-----------|-----------|-----------------|--------------|
| **Reasoning & Commonsense** | | | | | | |
| | HellaSwag | **76.15** | 74.19 | 75.52 | 60.52 | 74.37 |
| | ARC-CF | **65.61** | 59.81 | 58.58 | 55.88 | 62.11 |
| | Winogrande | 58.88 | **61.41** | 58.72 | 57.06 | 59.59 |
| | CommonsenseQA | 55.28 | 49.14 | **60.60** | 48.98 | 52.99 |
| **Knowledge & Understanding** | | | | | | |
| | MMLU-CF | 44.13 | 42.93 | 41.32 | 39.11 | **47.65** |
| | MMLU Pro CF | 19.61 | 16.66 | 16.42 | 18.04 | **24.92** |
| | MMLU Pro MCF | 32.70 | 31.32 | 25.07 | 30.39 | **41.07** |
| | PIQA | **78.89** | 78.35 | 78.51 | 75.35 | 77.58 |
| | OpenBookQA | 40.60 | 40.20 | 42.00 | 36.40 | **42.40** |
| | BoolQ | **78.99** | 73.61 | 75.33 | 74.46 | 74.28 |
| **Math & Code** | | | | | | |
| | HumanEval+ | 30.48 | 34.14 | 25.00 | 43.29 | **54.87** |
| | MBPP+ | 52.91 | 52.11 | 38.88 | 59.25 | **63.75** |
| | MATH (4-shot) | 46.10 | 40.10 | 7.44 | 41.64 | **51.20** |
| | GSM8k (5-shot) | 67.63 | 70.13 | 25.92 | 65.88 | **74.14** |
| **Long Context** | | | | | | |
| | Ruler 32k | 76.35 | 75.93 | 77.58 | 70.63 | **83.98** |
| | Ruler 64k | 67.85 | 64.90 | **72.93** | 57.18 | 60.29 |
| | Ruler 128k | 61.03 | 62.23 | **71.30** | 43.03 | 47.23 |

### Multilingual Benchmarks - 6 Main Supported Languages

#### French

| Metric | SmolLM3-3B | Qwen2.5-3B | Llama3.2-3B | Qwen3-1.7B | Qwen3-4B |
|--------|-----------|-----------|-----------|-----------|----------|
| MLMM Hellaswag | **63.94** | 57.47 | 57.66 | 51.26 | 61.00 |
| Belebele | 51.00 | 51.55 | 49.22 | 49.44 | **55.00** |
| Global MMLU (CF) | 38.37 | 34.22 | 33.71 | 34.94 | **41.80** |
| Flores-200 (5-shot) | 62.85 | 61.38 | 62.89 | 58.68 | **65.76** |

#### Spanish

| Metric | SmolLM3-3B | Qwen2.5-3B | Llama3.2-3B | Qwen3-1.7B | Qwen3-4B |
|--------|-----------|-----------|-----------|-----------|----------|
| MLMM Hellaswag | **65.85** | 58.25 | 59.39 | 52.40 | 61.85 |
| Belebele | 47.00 | 48.88 | 47.00 | 47.56 | **50.33** |
| Global MMLU (CF) | 38.51 | 35.84 | 35.60 | 34.79 | **41.22** |
| Flores-200 (5-shot) | 48.25 | 50.00 | 44.45 | 46.93 | **50.16** |

#### German

| Metric | SmolLM3-3B | Qwen2.5-3B | Llama3.2-3B | Qwen3-1.7B | Qwen3-4B |
|--------|-----------|-----------|-----------|-----------|----------|
| MLMM Hellaswag | **59.56** | 49.99 | 53.19 | 46.10 | 56.43 |
| Belebele | 48.44 | 47.88 | 46.22 | 48.00 | **53.44** |
| Global MMLU (CF) | 35.10 | 33.19 | 32.60 | 32.73 | **38.70** |
| Flores-200 (5-shot) | **56.60** | 50.63 | 54.95 | 52.58 | 50.48 |

#### Italian

| Metric | SmolLM3-3B | Qwen2.5-3B | Llama3.2-3B | Qwen3-1.7B | Qwen3-4B |
|--------|-----------|-----------|-----------|-----------|----------|
| MLMM Hellaswag | **62.49** | 53.21 | 54.96 | 48.72 | 58.76 |
| Belebele | 46.44 | 44.77 | 43.88 | 44.00 | **48.78** |
| Global MMLU (CF) | 36.99 | 33.91 | 32.79 | 35.37 | **39.26** |
| Flores-200 (5-shot) | 52.65 | **54.87** | 48.83 | 48.37 | 49.11 |

#### Portuguese

| Metric | SmolLM3-3B | Qwen2.5-3B | Llama3.2-3B | Qwen3-1.7B | Qwen3-4B |
|--------|-----------|-----------|-----------|-----------|----------|
| MLMM Hellaswag | **63.22** | 57.38 | 56.84 | 50.73 | 59.89 |
| Belebele | 47.67 | **49.22** | 45.00 | 44.00 | 50.00 |
| Global MMLU (CF) | 36.88 | 34.72 | 33.05 | 35.26 | **40.66** |
| Flores-200 (5-shot) | 60.93 | 57.68 | 54.28 | 56.58 | **63.43** |

### Additional Languages (Lower Token Count)

#### Arabic

| Metric | SmolLM3-3B | Qwen2.5-3B | Llama3.2-3B | Qwen3-1.7B | Qwen3-4B |
|--------|-----------|-----------|-----------|-----------|----------|
| Belebele | 40.22 | 44.22 | 45.33 | 42.33 | **51.78** |
| Global MMLU (CF) | 28.57 | 28.81 | 27.67 | 29.37 | **31.85** |
| Flores-200 (5-shot) | 40.22 | 39.44 | **44.43** | 35.82 | 39.76 |

#### Chinese

| Metric | SmolLM3-3B | Qwen2.5-3B | Llama3.2-3B | Qwen3-1.7B | Qwen3-4B |
|--------|-----------|-----------|-----------|-----------|----------|
| Belebele | 43.78 | 44.56 | 49.56 | 48.78 | **53.22** |
| Global MMLU (CF) | 36.16 | 33.79 | 39.57 | 38.56 | **44.55** |
| Flores-200 (5-shot) | 29.17 | **33.21** | 31.89 | 25.70 | 32.50 |

#### Russian

| Metric | SmolLM3-3B | Qwen2.5-3B | Llama3.2-3B | Qwen3-1.7B | Qwen3-4B |
|--------|-----------|-----------|-----------|-----------|----------|
| Belebele | 47.44 | 45.89 | 47.44 | 45.22 | **51.44** |
| Global MMLU (CF) | 36.51 | 32.47 | 34.52 | 34.83 | **38.80** |
| Flores-200 (5-shot) | 47.13 | 48.74 | 50.74 | 54.70 | **60.53** |

## SmolLM3-3B (Instruct Variant) Evaluation Results

### No Extended Thinking Mode

| Category | Metric | SmolLM3-3B | Qwen2.5-3B | Llama3.1-3B | Qwen3-1.7B | Qwen3-4B |
|----------|--------|-----------|-----------|-----------|-----------|----------|
| **High school math** | AIME 2025 | 9.3 | 2.9 | 0.3 | 8.0 | **17.1** |
| **Math problem-solving** | GSM-Plus | 72.8 | 74.1 | 59.2 | 68.3 | **82.1** |
| **Competitive programming** | LiveCodeBench v4 | 15.2 | 10.5 | 3.4 | 15.0 | **24.9** |
| **Graduate-level reasoning** | GPQA Diamond | 35.7 | 32.2 | 29.4 | 31.8 | **44.4** |
| **Instruction following** | IFEval | **76.7** | 65.6 | 71.6 | 74.0 | 68.9 |
| **Alignment** | MixEval Hard | 26.9 | 27.6 | 24.9 | 24.3 | **31.6** |
| **Tool Calling** | BFCL | 92.3 | - | 92.3* | 89.5 | **95.0** |
| **Multilingual Q&A** | Global MMLU | 53.5 | 50.54 | 46.8 | 49.5 | **65.1** |

*tool calling finetune

### Extended Thinking Mode

| Category | Metric | SmolLM3-3B | Qwen3-1.7B | Qwen3-4B |
|----------|--------|-----------|-----------|----------|
| **High school math** | AIME 2025 | 36.7 | 30.7 | **58.8** |
| **Math problem-solving** | GSM-Plus | 83.4 | 79.4 | **88.2** |
| **Competitive programming** | LiveCodeBench v4 | 30.0 | 34.4 | **52.9** |
| **Graduate-level reasoning** | GPQA Diamond | 41.7 | 39.9 | **55.3** |
| **Instruction following** | IFEval | 71.2 | 74.2 | **85.4** |
| **Alignment** | MixEval Hard | 30.8 | 33.9 | **38.0** |
| **Tool Calling** | BFCL | 88.8 | 88.8 | **95.5** |
| **Multilingual Q&A** | Global MMLU | 64.1 | 62.3 | **73.3** |

## Key Differences: Base vs. Instruct Variant

| Aspect | Base (SmolLM3-3B-Base) | Instruct (SmolLM3-3B) |
|--------|----------------------|----------------------|
| **Training Stage** | Post-pretraining only | Post-training applied |
| **Post-training** | None | 140B reasoning tokens + SFT + APO alignment |
| **Capabilities** | General language understanding | Instruction-following, reasoning, hybrid reasoning |
| **Use Case** | Fine-tuning, continued pretraining | Direct deployment, chat/instruction tasks |
| **Reasoning Mode** | N/A | Supports extended thinking mode |

## Open Resources & Reproducibility

- **Pretraining datasets:** [Collection available](https://huggingface.co/collections/HuggingFaceTB/smollm3-pretraining-datasets-685a7353fdc01aecde51b1d9)
- **Training configs & code:** [huggingface/smollm repository](https://github.com/huggingface/smollm)
- **Intermediate checkpoints:** [HuggingFaceTB/SmolLM3-3B-checkpoints](https://huggingface.co/HuggingFaceTB/SmolLM3-3B-checkpoints)
- **Post-training datasets:** Available in following weeks

## Limitations

SmolLM3 may produce:

- Factually inaccurate content
- Logically inconsistent outputs
- Content with biases from training data

**Recommendation**: Use as assistive tools; verify important information and critically evaluate generated content.

## License

[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)

## Citation

```bibtex
@misc{bakouch2025smollm3,
  title={{SmolLM3: smol, multilingual, long-context reasoner}},
  author={Bakouch, Elie and Ben Allal, Loubna and Lozhkov, Anton and Tazi, Nouamane and Tunstall, Lewis and Patiño, Carlos Miguel and Beeching, Edward and Roucher, Aymeric and Reedi, Aksel Joonas and Gallouédec, Quentin and Rasul, Kashif and Habib, Nathan and Fourrier, Clémentine and Kydlicek, Hynek and Penedo, Guilherme and Larcher, Hugo and Morlon, Mathieu and Srivastav, Vaibhav and Lochner, Joshua and Nguyen, Xuan-Son and Raffel, Colin and von Werra, Leandro and Wolf, Thomas},
  year={2025},
  howpublished={\url{https://huggingface.co/blog/smollm3}}
}
```
