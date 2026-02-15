# SmolLM3 blog post (main technical report) [https://huggingface.co/blog/smollm3]

**Type:** blog-post
**Fetched:** 2026-02-14
**Priority:** primary

## Model Overview

SmolLM3 is a 3B parameter model trained on 11.2T tokens with the following key specifications:

- **Base model**: HuggingFaceTB/SmolLM3-3B-Base
- **Instruct/Reasoning model**: HuggingFaceTB/SmolLM3-3B
- **Context length**: Up to 128k tokens
- **Multilingual**: English, French, Spanish, German, Italian, Portuguese
- **Dual-mode**: Supports `/think` and `/no_think` flags for reasoning control

## Architecture Details

### Core Architecture

The model uses a transformer decoder architecture with the following components:

**Grouped Query Attention (GQA)**:
- 4 groups (replaces traditional multi-head attention)
- Matches multi-head attention performance while significantly reducing KV cache size
- Validated via ablations on 3B model with 100B FineWeb-Edu tokens

**Tied embeddings**:
- Similar to SmolLM2, building on Llama architecture

### Key Optimizations

**NoPE (No Rotary Position Embeddings)**:
- Implements RoPE to NoRoPE strategy from Yang et al. (2025)
- Selectively removes rotary position embeddings from every 4th layer
- > "Improves long context performance without affecting short context"
- Validated through ablations

**Intra-Document Masking**:
- Attention masking ensures tokens from different documents in same training sequence don't attend to each other
- Follows "Analysing The Impact of Sequence Composition on Language Model Pre-Training" (2402.13991)
- Similar to Llama 3
- > "This helps with faster and more stable long context training while maintaining short context performance"

**Training Stability Modifications**:
- Following OLMo 2: Remove weight decay from embedding layers
- Embedding norms naturally stabilize at healthier values without impacting performance

## Training Configuration

### Pretraining Setup

The following hyperparameters were used across pretraining:

- **Global batch size**: 2.36M tokens
- **Sequence length**: 4096
- **Learning rate**: 2e-4
- **Optimizer**: AdamW
  - beta1: 0.9
  - beta2: 0.95
- **Weight decay**: 0.1
- **Gradient clipping**: 1.0
- **LR scheduler**: WSD (Warmup-Stable-Decay)
  - Warmup: 2000 steps
  - Linear decay to 0 in final 10% of training
- **Hardware**: 384 H100 GPUs
- **Training duration**: 24 days
- **Frameworks**: nanotron (training), datatrove (data), lighteval (evaluation)

## Pretraining Curriculum (11.2T tokens, 3 stages)

### Stage 1: Stable Phase (0T → 8T tokens)

Foundation stage for general capabilities with the following data mixture:

- **Web**: 85% (12% multilingual)
  - FineWeb-Edu, DCLM, FineWeb2, FineWeb2-HQ
- **Code**: 12%
  - The Stack v2 (16 programming languages), StarCoder2 pull requests, Jupyter/Kaggle notebooks, GitHub issues, StackExchange
- **Math**: 3%
  - FineMath3+, InfiWebMath3+

### Stage 2: Stable Phase (8T → 10T tokens)

Higher quality math and code introduction:

- **Web**: 75% (12% multilingual)
- **Code**: 15%
  - Adding Stack-Edu
- **Math**: 10%
  - FineMath4+, InfiWebMath4+, MegaMath (Qwen Q&A, Pro synthetic rewrites, text-code interleaved blocks)

### Stage 3: Decay Phase (10T → 11.1T tokens)

Math and code upsampling:

- **Web**: 63% (12% multilingual)
- **Code**: 24%
  - High-quality code data upsampling
- **Math**: 13%
  - Math data upsampling + reasoning datasets (OpenMathReasoning)

## Mid-Training (Post-Pretraining)

### Long Context Extension (100B tokens)

Two sequential stages for context window extension, totaling 100B tokens:

**Stage 1**: 4k → 32k context
- 50B tokens
- RoPE theta: 1.5M

**Stage 2**: 32k → 64k context
- 50B tokens
- RoPE theta: 5M

**Strategy**:
- Upsample math, code, reasoning data in both stages
- Ablations showed upsampling specific long context data (repositories, books, long web pages) didn't boost RULER/HELMET benchmarks
- > "Using NoPE and training on the decay mixture with longer sequences and increased RoPE theta values was sufficient to achieve competitive long context performance up to 64k"

**Inference Extrapolation**:
- Uses YARN (following Qwen2.5) for extrapolation beyond 64k training length
- **Inference capability**: Up to 128k context (2x extension beyond training length)

### Reasoning Mid-Training (140B tokens)

Training details:
- **Dataset**: 35B tokens
  - OpenThoughts3-1.2M (Open Thought)
  - Subset of Llama-Nemotron-Post-Training-Dataset-v1.1 (NVIDIA) with R1 reasoning traces
- **Chat template**: ChatML
- **Packing**: Wrapped packing to avoid excessive structure
- **Training**: 4 epochs (~140B tokens)
- **Checkpoint**: Used for subsequent SFT stages

## Post-Training

### Chat Template Design

The chat template includes the following features:

- **Reasoning control**: `/think` and `/no_think` flags in system prompt
- **Non-reasoning mode**: Pre-fills response with empty think blocks (similar to Qwen3)
- **Tool support**:
  - XML Tools (standard tool-calling)
  - Python Tools (Python function calling in `<code>` snippets)
- **Metadata**: Date, knowledge cut-off, current reasoning mode
- **System override**: `/system_override` flag to exclude metadata

### Supervised Fine-Tuning

**Dataset Composition: 1.8B tokens total**
- **Non-reasoning mode**: 1B tokens (12 datasets)
- **Reasoning mode**: 0.8B tokens (10 datasets with reasoning traces)

**Synthetic Data Generation**:
- Prompted Qwen3-32B in reasoning mode with non-reasoning dataset prompts
- Filled gaps in domains with scarcity: multi-turn conversations, multilinguality, everyday conversations

**Training Details**:
- **Epochs**: 4 (~8B tokens total)
- **Packing**: BFD (best-fit decreasing)
- **Loss masking**: Masked on user turns and tool call results

### Alignment: Anchored Preference Optimization (APO)

**Dataset Sources**:
- **Non-reasoning**: Tulu3 preference dataset
- **Reasoning**: Synthetic preference pairs generated from Qwen3-32B (chosen) vs Qwen3-0.6B (rejected)
- **Coverage**: Generated complementing thinking mode pairs for all non-thinking domains

**APO Method**:
- Variant of Direct Preference Optimization (DPO) with more stable optimization objective
- **DPO reward function**: r_θ(x,y) = β log(π_θ(y|x) / π_ref(y|x))
- **DPO loss**: L_DPO = -E[(x,y_w,y_l)] log σ(β log(π_θ(y_w|x)/π_ref(y_w|x)) - β log(π_θ(y_l|x)/π_ref(y_l|x)))
- **Beta parameter (β)**: Controls how much the model being optimized can change relative to the reference model
- **Training**: Optimizes triplets of (prompt x, chosen response y_w, rejected response y_l)
- **Observations**: Higher downstream performance vs DPO in internal ablations

**Performance Trade-offs**:
- Improvements: mathematics, science, instruction following, coding, chat, multilingual tasks
- Degradation: Long context benchmarks (RULER) traced to reasoning mid-training focus
- APO data limited to 24k tokens (most reasoning data below this length)

### Model Merging (Post-APO Recovery)

**Motivation**: Recover long-context performance degraded by alignment training

**Merging Strategy** (using MergeKit):
1. Create model "soup" from APO checkpoints
2. Linear merge with mid-training checkpoint (strong long-context performance)
   - **Weights**: 0.9 (APO soup) + 0.1 (mid-training checkpoint)
3. **Result**: Recovered base model RULER performance on contexts up to 128k tokens

**Final Release**: Result of this merged checkpoint

## Multilingual Support

**Languages**: English, French, Spanish, German, Italian, Portuguese

**Tokenizer**:
- Uses Llama 3.2 tokenizer as is, except for removing `bos_token` (128K vocabulary)
- Combined from:
  - 100K tokens: tiktoken3 tokenizer
  - 28K tokens: Additional non-English language tokens
- **Character compression**: 3.94 characters/token on English (vs 3.17 for Llama 2)
- **Impact**: Better compression + downstream performance without English tokenization impact

**Evaluation Benchmarks**:
- Global MMLU
- MLMM HellaSwag
- Flores-200
- Belebele
- Tests: Knowledge, commonsense reasoning, text understanding, translation

## Benchmark Results

### Base Model Performance

**Knowledge & Reasoning Benchmarks**:

The base model achieved first or second place in the 3B class across multiple benchmarks:

| Benchmark | SmolLM3 Performance |
|-----------|-------------------|
| HellaSwag | 1st/2nd place vs 3B class |
| ARC | 1st/2nd place vs 3B class |
| BoolQ | 1st/2nd place vs 3B class |
| Winogrande | Competitive (3B class) |
| CommonsenseQA | Competitive (3B class) |
| MMLU-CF | Competitive (3B class) |
| MMLU Pro CF | Competitive (3B class) |
| PIQA | Competitive (3B class) |
| OpenBookQA | Competitive (3B class) |

**Math & Coding**:

| Benchmark | Performance | Notes |
|-----------|-------------|-------|
| GSM8K | Competitive within 3B | Math reasoning |
| MATH | Competitive within 3B | Advanced math |
| HumanEval+ | Competitive within 3B | Code generation |
| MBPP+ | Competitive within 3B | Code understanding |

**Long Context**:
- **RULER 64k**: Effective long-context handling

**Win Rate Summary**:
> "Outperforms Llama-3.2-3B and Qwen2.5-3B; competitive with 4B models (Qwen3-4B, Gemma3-4B)"

### Instruct Model: Non-Reasoning Mode

**Competitive Positioning**:
- Outperforms: Llama3.2-3B Instruct, Qwen2.5-3B Instruct, other 3B non-reasoning models
- Significantly outperforms: Qwen3-1.7B
- Competitive with: Qwen3-4B (at lower computational cost)
- **Pareto front**: > "Efficiency sweet spot between reasoning models and non-reasoning models"

### Instruct Model: Extended Thinking Mode

Substantial improvements with reasoning enabled:

| Benchmark | With Thinking | Without Thinking | Improvement |
|-----------|---------------|------------------|-------------|
| AIME 2025 | 36.7% | 9.3% | +27.4 pp |
| LiveCodeBench (competitive programming) | 30.0% | 15.2% | +14.8 pp |
| GPQA Diamond (graduate reasoning) | 41.7% | 35.7% | +6.0 pp |

**Comparative Performance**:
- **Qwen3-4B**: Generally highest across both modes
- **SmolLM3-3B**: Competitive within 3B class, particularly strong in mathematical reasoning
- **Advantage**: Dual-mode flexibility (fast inference vs thorough analysis with thinking)

## Usage Examples

### Basic Generation (with thinking enabled by default)

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "HuggingFaceTB/SmolLM3-3B"
device = "cuda"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name).to(device)

prompt = "Give me a brief explanation of gravity in simple terms."
messages_think = [{"role": "user", "content": prompt}]

text = tokenizer.apply_chat_template(
    messages_think,
    tokenize=False,
    add_generation_prompt=True,
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

generated_ids = model.generate(**model_inputs, max_new_tokens=32768)
output_ids = generated_ids[0][len(model_inputs.input_ids[0]):]
print(tokenizer.decode(output_ids, skip_special_tokens=True))
```

**Recommended sampling parameters**: temperature=0.6, top_p=0.95

### Disabling Extended Thinking

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

### Tool Calling (Agentic Usage)

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
    {"role": "user", "content": "Hello! How is the weather today in Copenhagen?"}
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

## Key Claims & Performance Summary

The blog post makes the following key claims:

- > "SmolLM3 sits in the efficiency sweet spot": Outperforms Llama-3.2-3B and Qwen2.5-3B; competitive with 4B alternatives
- **Dual-mode reasoning**: Supports both fast non-reasoning and thorough extended-thinking inference
- **Fully open recipe**: Complete transparency on architecture, data mixtures, and training methodology
- **State-of-the-art at 3B scale**: 11T token training with competitive 4B model performance
- **Multilingual competence**: Consistent performance across 6 European languages

## Resources & Release

- **Base model**: https://hf.co/HuggingFaceTB/SmolLM3-3B-Base
- **Instruct model**: https://hf.co/HuggingFaceTB/SmolLM3-3B
- **Collections with quantized checkpoints**: HuggingFaceTB/smollm3 collection
- **GitHub**: https://github.com/huggingface/smollm (pretraining configs, evaluation code)
- **Training logs**: https://wandb.ai/huggingface/SmolLM3-training-logs
- **Datasets**: SmolTalk2 (HuggingFaceTB/smoltalk2) with Mid/SFT/Preference subsets
- **Transformers support**: v4.53.0+ required
