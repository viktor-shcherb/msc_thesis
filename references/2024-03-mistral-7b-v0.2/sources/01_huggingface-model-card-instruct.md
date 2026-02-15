# Hugging Face Model Card — Mistral-7B-Instruct-v0.2

**URL:** https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2
**Type:** documentation
**Fetched:** 2026-02-15
**Priority:** primary

## Model Specifications

### Basic Information
- **Model Name**: mistralai/Mistral-7B-Instruct-v0.2
- **Organization**: Mistral AI
- **Model Size**: 7B parameters
- **Tensor Type**: BF16
- **License**: Apache 2.0
- **Task**: Text Generation
- **Framework**: Transformers, PyTorch
- **Format**: Safetensors

### Architecture Details

> **Context Window**: 32k tokens (increased from 8k in v0.1)
> **Rope-theta**: 1e6
> **Attention Mechanism**: No Sliding-Window Attention (removed from v0.1)

The model card states: "4x larger context window (32k vs 8k)" and lists "Modified rope-theta parameter" and "Simplified attention mechanism" as improvements over v0.1.

### Performance Metrics

No specific benchmark results are provided on the model card beyond the reference to MT-Bench 7.6 mentioned in the La Plateforme blog post.

## Usage Information

### Instruction Format

The model uses the following format with `[INST]` and `[/INST]` tokens:

```
<s>[INST] instruction [/INST] response</s>
```

### Code Example

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

device = "cuda"
model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2")
tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2")

messages = [
    {"role": "user", "content": "What is your favourite condiment?"},
    {"role": "assistant", "content": "Well, I'm quite partial to a good squeeze of fresh lemon juice..."},
    {"role": "user", "content": "Do you have mayonnaise recipes?"}
]

encodeds = tokenizer.apply_chat_template(messages, return_tensors="pt")
model_inputs = encodeds.to(device)
model.to(device)

generated_ids = model.generate(model_inputs, max_new_tokens=1000, do_sample=True)
decoded = tokenizer.batch_decode(generated_ids)
print(decoded[0])
```

### Alternative Tokenizers

The model card provides examples using:
- **Mistral Common Tokenizer** (mistral_common.tokens.tokenizers.mistral.MistralTokenizer)
- **Mistral Inference** (mistral_inference)

Note: The model card warns that "Transformers tokenizer may not match `mistral_common` reference implementation exactly."

## Community Adoption

### Usage Statistics (as of fetch date)
- **Downloads (last month)**: 2,391,103
- **Like Count**: 3.07k
- **Organization Followers**: 15.2k
- **Community Discussions**: 224

### Derived Models
- **Adapters**: 1,098 models
- **Finetunes**: 1,064 models
- **Merges**: 350 models
- **Quantizations**: 101 models
- **Spaces**: 100+ implementations

## Authors

Albert Jiang, Alexandre Sablayrolles, Arthur Mensch, Blanche Savary, Chris Bamford, Devendra Singh Chaplot, Diego de las Casas, Emma Bou Hanna, Florian Bressand, Gianna Lengyel, Guillaume Bour, Guillaume Lample, Lélio Renard Lavaud, Louis Ternon, Lucile Saulnier, Marie-Anne Lachaux, Pierre Stock, Teven Le Scao, Théophile Gervet, Thibaut Lavril, Thomas Wang, Timothée Lacroix, William El Sayed

## Publication Details
- **Paper**: arXiv 2310.06825
- **Publication Date**: October 10, 2023
- **Paper URL**: https://huggingface.co/papers/2310.06825

## Limitations

The model card notes:
- No built-in moderation mechanisms
- "Quick demonstration model; community engagement encouraged for guardrail implementation"
- Requires careful deployment in moderation-sensitive environments

## Related Models

A newer version is available: mistralai/Mistral-7B-Instruct-v0.3

## Inference Providers

- Third-party inference providers are listed on the model card (providers may change over time)
