# SmolLM3-3B model card (instruct) [https://huggingface.co/HuggingFaceTB/SmolLM3-3B]

**Type:** documentation
**Fetched:** 2026-02-14
**Priority:** supplementary

## Model Description and Overview

SmolLM3 is a 3B parameter language model designed to push the boundaries of small models with dual-mode reasoning capabilities. It is a fully open model offering strong performance at the 3B–4B scale.

### Key Features

- **Hybrid reasoning**: Instruct model optimized for dual mode reasoning
- **Fully open**: Open weights + full training details including public data mixture and training configs
- **Long context**: Trained on 64k context and supports up to **128k tokens** using YARN extrapolation
- **Multilingual**: 6 natively supported languages (English, French, Spanish, German, Italian, and Portuguese)
- **Architecture**: Decoder-only transformer using GQA and NoPE (with 3:1 ratio)
- **Pretraining**: 11.2T tokens with staged curriculum of web, code, math, and reasoning data
- **Post-training**: 140B reasoning tokens midtraining + supervised fine-tuning + Anchored Preference Optimization (APO)

## Benchmark Results

### Instruction Model - No Extended Thinking

| Category | Metric | SmolLM3-3B | Qwen2.5-3B | Llama3.1-3B | Qwen3-1.7B | Qwen3-4B |
|----------|--------|-----------|-----------|-----------|-----------|----------|
| High school math | AIME 2025 | 9.3 | 2.9 | 0.3 | 8.0 | **17.1** |
| Math problem-solving | GSM-Plus | 72.8 | 74.1 | 59.2 | 68.3 | **82.1** |
| Competitive programming | LiveCodeBench v4 | 15.2 | 10.5 | 3.4 | 15.0 | **24.9** |
| Graduate-level reasoning | GPQA Diamond | 35.7 | 32.2 | 29.4 | 31.8 | **44.4** |
| Instruction following | IFEval | **76.7** | 65.6 | 71.6 | 74.0 | 68.9 |
| Alignment | MixEval Hard | 26.9 | 27.6 | 24.9 | 24.3 | **31.6** |
| Tool Calling | BFCL | 92.3 | - | 92.3* | 89.5 | **95.0** |
| Multilingual Q&A | Global MMLU | 53.5 | 50.54 | 46.8 | 49.5 | **65.1** |

*tool calling finetune

### Instruction Model - Extended Thinking (Reasoning Mode)

| Category | Metric | SmolLM3-3B | Qwen3-1.7B | Qwen3-4B |
|----------|--------|-----------|-----------|----------|
| High school math | AIME 2025 | 36.7 | 30.7 | **58.8** |
| Math problem-solving | GSM-Plus | 83.4 | 79.4 | **88.2** |
| Competitive programming | LiveCodeBench v4 | 30.0 | 34.4 | **52.9** |
| Graduate-level reasoning | GPQA Diamond | 41.7 | 39.9 | **55.3** |
| Instruction following | IFEval | 71.2 | 74.2 | **85.4** |
| Alignment | MixEval Hard | 30.8 | 33.9 | **38.0** |
| Tool Calling | BFCL | 88.8 | 88.8 | **95.5** |
| Multilingual Q&A | Global MMLU | 64.1 | 62.3 | **73.3** |

### Base Pre-Trained Model - English Benchmarks

| Category | Metric | SmolLM3-3B | Qwen2.5-3B | Llama3-3.2B | Qwen3-1.7B-Base | Qwen3-4B-Base |
|----------|--------|-----------|-----------|-----------|-----------|-----------|
| **Reasoning & Commonsense** |
| | HellaSwag | **76.15** | 74.19 | 75.52 | 60.52 | 74.37 |
| | ARC-CF (Average) | **65.61** | 59.81 | 58.58 | 55.88 | 62.11 |
| | Winogrande | 58.88 | **61.41** | 58.72 | 57.06 | 59.59 |
| | CommonsenseQA | 55.28 | 49.14 | **60.60** | 48.98 | 52.99 |
| **Knowledge & Understanding** |
| | MMLU-CF (Average) | 44.13 | 42.93 | 41.32 | 39.11 | **47.65** |
| | MMLU Pro CF | 19.61 | 16.66 | 16.42 | 18.04 | **24.92** |
| | MMLU Pro MCF | 32.70 | 31.32 | 25.07 | 30.39 | **41.07** |
| | PIQA | **78.89** | 78.35 | 78.51 | 75.35 | 77.58 |
| | OpenBookQA | 40.60 | 40.20 | 42.00 | 36.40 | **42.40** |
| | BoolQ | **78.99** | 73.61 | 75.33 | 74.46 | 74.28 |
| **Math & Code** |
| | HumanEval+ | 30.48 | 34.14 | 25.00 | 43.29 | **54.87** |
| | MBPP+ | 52.91 | 52.11 | 38.88 | 59.25 | **63.75** |
| | MATH (4-shot) | 46.10 | 40.10 | 7.44 | 41.64 | **51.20** |
| | GSM8k (5-shot) | 67.63 | 70.13 | 25.92 | 65.88 | **74.14** |
| **Long Context** |
| | Ruler 32k | 76.35 | 75.93 | 77.58 | 70.63 | **83.98** |
| | Ruler 64k | 67.85 | 64.90 | **72.93** | 57.18 | 60.29 |
| | Ruler 128k | 61.03 | 62.23 | **71.30** | 43.03 | 47.23 |

### Base Pre-Trained Model - Multilingual Benchmarks

#### Primary Supported Languages (6 languages)

**French**:

| Metric | SmolLM3 3B | Qwen2.5-3B | Llama3.2 3B | Qwen3 1.7B | Qwen3 4B |
|--------|-----------|-----------|-----------|-----------|----------|
| MLMM Hellaswag | **63.94** | 57.47 | 57.66 | 51.26 | 61.00 |
| Belebele | 51.00 | 51.55 | 49.22 | 49.44 | **55.00** |
| Global MMLU (CF) | 38.37 | 34.22 | 33.71 | 34.94 | **41.80** |
| Flores-200 (5-shot) | 62.85 | 61.38 | 62.89 | 58.68 | **65.76** |

**Spanish**:

| Metric | SmolLM3 3B | Qwen2.5-3B | Llama3.2 3B | Qwen3 1.7B | Qwen3 4B |
|--------|-----------|-----------|-----------|-----------|----------|
| MLMM Hellaswag | **65.85** | 58.25 | 59.39 | 52.40 | 61.85 |
| Belebele | 47.00 | 48.88 | 47.00 | 47.56 | **50.33** |
| Global MMLU (CF) | 38.51 | 35.84 | 35.60 | 34.79 | **41.22** |
| Flores-200 (5-shot) | 48.25 | 50.00 | 44.45 | 46.93 | **50.16** |

**German**:

| Metric | SmolLM3 3B | Qwen2.5-3B | Llama3.2 3B | Qwen3 1.7B | Qwen3 4B |
|--------|-----------|-----------|-----------|-----------|----------|
| MLMM Hellaswag | **59.56** | 49.99 | 53.19 | 46.10 | 56.43 |
| Belebele | 48.44 | 47.88 | 46.22 | 48.00 | **53.44** |
| Global MMLU (CF) | 35.10 | 33.19 | 32.60 | 32.73 | **38.70** |
| Flores-200 (5-shot) | **56.60** | 50.63 | 54.95 | 52.58 | 50.48 |

**Italian**:

| Metric | SmolLM3 3B | Qwen2.5-3B | Llama3.2 3B | Qwen3 1.7B | Qwen3 4B |
|--------|-----------|-----------|-----------|-----------|----------|
| MLMM Hellaswag | **62.49** | 53.21 | 54.96 | 48.72 | 58.76 |
| Belebele | 46.44 | 44.77 | 43.88 | 44.00 | **48.78** |
| Global MMLU (CF) | 36.99 | 33.91 | 32.79 | 35.37 | **39.26** |
| Flores-200 (5-shot) | 52.65 | **54.87** | 48.83 | 48.37 | 49.11 |

**Portuguese**:

| Metric | SmolLM3 3B | Qwen2.5-3B | Llama3.2 3B | Qwen3 1.7B | Qwen3 4B |
|--------|-----------|-----------|-----------|-----------|----------|
| MLMM Hellaswag | **63.22** | 57.38 | 56.84 | 50.73 | 59.89 |
| Belebele | 47.67 | **49.22** | 45.00 | 44.00 | 50.00 |
| Global MMLU (CF) | 36.88 | 34.72 | 33.05 | 35.26 | **40.66** |
| Flores-200 (5-shot) | 60.93 | 57.68 | 54.28 | 56.58 | **63.43** |

#### Additional Supported Languages (Arabic, Chinese, Russian)

**Arabic**:

| Metric | SmolLM3 3B | Qwen2.5-3B | Llama3.2 3B | Qwen3 1.7B | Qwen3 4B |
|--------|-----------|-----------|-----------|-----------|----------|
| Belebele | 40.22 | 44.22 | 45.33 | 42.33 | **51.78** |
| Global MMLU (CF) | 28.57 | 28.81 | 27.67 | 29.37 | **31.85** |
| Flores-200 (5-shot) | 40.22 | 39.44 | **44.43** | 35.82 | 39.76 |

**Chinese**:

| Metric | SmolLM3 3B | Qwen2.5-3B | Llama3.2 3B | Qwen3 1.7B | Qwen3 4B |
|--------|-----------|-----------|-----------|-----------|----------|
| Belebele | 43.78 | 44.56 | 49.56 | 48.78 | **53.22** |
| Global MMLU (CF) | 36.16 | 33.79 | 39.57 | 38.56 | **44.55** |
| Flores-200 (5-shot) | 29.17 | **33.21** | 31.89 | 25.70 | 32.50 |

**Russian**:

| Metric | SmolLM3 3B | Qwen2.5-3B | Llama3.2 3B | Qwen3 1.7B | Qwen3 4B |
|--------|-----------|-----------|-----------|-----------|----------|
| Belebele | 47.44 | 45.89 | 47.44 | 45.22 | **51.44** |
| Global MMLU (CF) | 36.51 | 32.47 | 34.52 | 34.83 | **38.80** |
| Flores-200 (5-shot) | 47.13 | 48.74 | 50.74 | 54.70 | **60.53** |

## Usage Instructions and Code Examples

### Installation

```bash
pip install -U transformers
```

### Basic Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "HuggingFaceTB/SmolLM3-3B"
device = "cuda"  # for GPU usage or "cpu" for CPU usage

# load the tokenizer and the model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
).to(device)

# prepare the model input
prompt = "Give me a brief explanation of gravity in simple terms."
messages_think = [
    {"role": "user", "content": prompt}
]

text = tokenizer.apply_chat_template(
    messages_think,
    tokenize=False,
    add_generation_prompt=True,
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

# Generate the output
generated_ids = model.generate(**model_inputs, max_new_tokens=32768)

# Get and decode the output
output_ids = generated_ids[0][len(model_inputs.input_ids[0]) :]
print(tokenizer.decode(output_ids, skip_special_tokens=True))
```

**Recommended sampling parameters**: `temperature=0.6` and `top_p=0.95`

### Long Context Processing

The current `config.json` is set for context length up to 65,536 tokens. To handle longer inputs (128k or 256k), modify the `rope_scaling` in config:

```json
{
  ...,
  "rope_scaling": {
    "factor": 2.0,
    "original_max_position_embeddings": 65536,
    "type": "yarn"
  }
}
```

### Extended Thinking Mode

**Enable extended thinking (default)**:

```python
messages = [
    {"role": "user", "content": prompt}
]
```

**Disable extended thinking via system prompt**:

```python
prompt = "Give me a brief explanation of gravity in simple terms."
messages = [
    {"role": "system", "content": "/no_think"},
    {"role": "user", "content": prompt}
]

text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
)
```

**Disable via kwarg**:

```python
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=False
)
```

**Note**: System prompt flags override `enable_thinking` kwarg.

### Tool Calling (Agentic Usage)

**XML-based tool calling**:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

checkpoint = "HuggingFaceTB/SmolLM3-3B"

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint)

tools = [
    {
        "name": "get_weather",
        "description": "Get the weather in a city",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "The city to get the weather for"
                }
            }
        }
    }
]

messages = [
    {
        "role": "user",
        "content": "Hello! How is the weather today in Copenhagen?"
    }
]

inputs = tokenizer.apply_chat_template(
    messages,
    enable_thinking=False,  # or True
    xml_tools=tools,
    add_generation_prompt=True,
    tokenize=True,
    return_tensors="pt"
)

outputs = model.generate(inputs)
print(tokenizer.decode(outputs[0]))
```

**Python-based tool calling**:
Use `python_tools` argument instead of `xml_tools` for function-style tool calls.

### Custom System Instructions

```python
prompt = "Give me a brief explanation of gravity in simple terms."
messages = [
    {"role": "system", "content": "Speak like a pirate./think"},
    {"role": "user", "content": prompt}
]

text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
)
```

### Deployment with vLLM

```bash
vllm serve HuggingFaceTB/SmolLM3-3B --enable-auto-tool-choice --tool-call-parser=hermes
```

### Deployment with SGLang

```bash
python -m sglang.launch_server --model-path HuggingFaceTB/SmolLM3-3B
```

### API Request with Chat Template Kwargs

```bash
curl http://localhost:8000/v1/chat/completions -H "Content-Type: application/json" -d '{
  "model": "HuggingFaceTB/SmolLM3-3B",
  "messages": [
    {"role": "user", "content": "Give me a brief explanation of gravity in simple terms."}
  ],
  "temperature": 0.6,
  "top_p": 0.95,
  "max_tokens": 16384,
  "chat_template_kwargs": {"enable_thinking": false}
}'
```

### Local Inference Frameworks

Quantized checkpoints available for: llama.cpp, ONNX, MLX, MLC, and ExecuTorch at [SmolLM3 Quantization Collection](https://huggingface.co/collections/HuggingFaceTB/smollm3-686d33c1fdffe8e635317e23)

## Hardware Requirements

### Training Specifications

- **GPUs**: 384 × H100
- **Training Framework**: [nanotron](https://github.com/huggingface/nanotron/tree/smollm3)

### Inference Specifications

- Supports GPU (CUDA) and CPU inference
- Requires transformers `v4.53.0` or later
- Compatible with vLLM and SGLang for optimized serving

## License

**Apache 2.0**

Full license: https://www.apache.org/licenses/LICENSE-2.0

## Training Details

### Model Architecture

- **Type**: Decoder-only Transformer
- **Key Features**:
  - Grouped Query Attention (GQA)
  - NoPE (No Position Embeddings) with 3:1 ratio
- **Pretraining tokens**: 11.2T
- **Precision**: bfloat16

### Post-training

- **Mid-training**: 140B reasoning tokens
- **Fine-tuning**: Supervised Fine-Tuning (SFT)
- **Alignment**: Anchored Preference Optimization (APO)

### Training Pipeline

- **Data Processing**: [datatrove](https://github.com/huggingface/datatrove)
- **Evaluation**: [lighteval](https://github.com/huggingface/lighteval)
- **Post-training**: [TRL](https://github.com/huggingface/trl)

### Open Resources

- **Pretraining datasets**: Available in [SmolLM3 Pretraining Datasets Collection](https://huggingface.co/collections/HuggingFaceTB/smollm3-pretraining-datasets-685a7353fdc01aecde51b1d9)
- **Training configs & code**: [huggingface/smollm repository](https://github.com/huggingface/smollm)
- **Checkpoints**: [HuggingFaceTB/SmolLM3-3B-checkpoints](https://huggingface.co/HuggingFaceTB/SmolLM3-3B-checkpoints) (includes mid-training and SFT checkpoints)

## Limitations and Biases

SmolLM3 can produce text on a variety of topics, but:

- **Factual accuracy**: Generated content may not always be factually accurate
- **Logical consistency**: Output may lack logical consistency
- **Bias**: Model may reflect biases present in training data
- **Intended use**: Should be used as an assistive tool rather than a definitive source of information
- **Verification**: Users should always verify important information and critically evaluate any generated content

## Citation

```bibtex
@misc{bakouch2025smollm3,
  title={{SmolLM3: smol, multilingual, long-context reasoner}},
  author={Bakouch, Elie and Ben Allal, Loubna and Lozhkov, Anton and Tazi, Nouamane and Tunstall, Lewis and Patiño, Carlos Miguel and Beeching, Edward and Roucher, Aymeric and Reedi, Aksel Joonas and Gallouédec, Quentin and Rasul, Kashif and Habib, Nathan and Fourrier, Clémentine and Kydlicek, Hynek and Penedo, Guilherme and Larcher, Hugo and Morlon, Mathieu and Srivastav, Vaibhav and Lochner, Joshua and Nguyen, Xuan-Son and Raffel, Colin and von Werra, Leandro and Wolf, Thomas},
  year={2025},
  howpublished={\url{https://huggingface.co/blog/smollm3}}
}
```

## Additional Resources

- **Blog post**: https://hf.co/blog/smollm3
- **Model page**: https://huggingface.co/HuggingFaceTB/SmolLM3-3B
- **Base model**: [HuggingFaceTB/SmolLM3-3B-Base](https://huggingface.co/HuggingFaceTB/SmolLM3-3B-Base)
- **EU AI Act Transparency**: See [development Space](https://huggingface.co/spaces/hfmlsoc/smollm3-eu-data-transparency)
- **Downloads (last month)**: 79,434
