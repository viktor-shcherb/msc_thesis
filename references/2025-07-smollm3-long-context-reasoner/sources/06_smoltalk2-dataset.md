# SmolTalk2 dataset [https://huggingface.co/datasets/HuggingFaceTB/smoltalk2]

**Type:** documentation
**Fetched:** 2026-02-14
**Priority:** supplementary

## Dataset Overview

SmolTalk2 is a comprehensive post-training dataset from Hugging Face Smol Models Research, consisting of three distinct subsets corresponding to three phases of post-training for SmolLM3-3B:

1. **Mid** (4.78M rows)
2. **SFT** (3.38M rows)
3. **Preference** (447k rows)

**Total: ~8.6M rows**

## Dataset Composition

### 1. Mid Subset (4.78M rows)

**Purpose**: Mid-stage training phase

**Splits (2 total)**:

- `Llama_Nemotron_Post_Training_Dataset_reasoning_r1` (3.64M rows)
- `OpenThoughts3_1.2M` (1.14M rows)

**Fields**:

- `split`: Split identifier
- `messages`: Array of conversation messages with:
  - `content`: Text content (string)
  - `role`: Speaker role (string)
- `source`: Data source identifier

### 2. SFT Subset (3.38M rows)

**Purpose**: Supervised Fine-Tuning data

**Splits (25 total)**, including:

**Reasoning-enabled**:
- LongAlign_64k_Qwen3_32B_yarn_131k_think
- OpenThoughts3_1.2M_think
- aya_dataset_Qwen3_32B_think
- multi_turn_reasoning_if_think
- s1k_1.1_think
- smolagents_toolcalling_traces_think
- smoltalk_everyday_convs_reasoning_Qwen3_32B_think
- smoltalk_multilingual8_Qwen3_32B_think
- smoltalk_systemchats_Qwen3_32B_think
- table_gpt_Qwen3_32B_think

**Non-reasoning**:
- LongAlign_64k_context_lang_annotated_lang_6_no_think
- Mixture_of_Thoughts_science_no_think
- OpenHermes_2.5_no_think
- OpenThoughts3_1.2M_no_think_no_think
- hermes_function_calling_v1_no_think
- smoltalk_multilingual_8languages_lang_5_no_think
- smoltalk_smollm3_everyday_conversations_no_think
- smoltalk_smollm3_explore_instruct_rewriting_no_think
- smoltalk_smollm3_smol_magpie_ultra_no_think
- smoltalk_smollm3_smol_rewrite_no_think
- smoltalk_smollm3_smol_summarize_no_think
- smoltalk_smollm3_systemchats_30k_no_think
- table_gpt_no_think
- tulu_3_sft_personas_instruction_following_no_think
- xlam_traces_no_think

**Fields**:

- `split`: Split identifier
- `messages`: Array with `content` and `role`
- `chat_template_kwargs`: Configuration with:
  - `custom_instructions`: Optional instructions (string)
  - `enable_thinking`: Boolean flag for reasoning
  - `python_tools`: Array of available Python tools (string array)
  - `xml_tools`: Array of available XML tools (string array)
- `source`: Data source

### 3. Preference Subset (447k rows)

**Purpose**: Preference/DPO training data

**Splits (2 total)**:

- `llama_3.1_tulu_3_8b_preference_mixture_no_think`
- `tulu_3_8b_pref_mix_Qwen3_32B_Qwen3_0.6B_think`

**Fields**:

- `split`: Split identifier
- `chosen`: Preferred response (array with `content` and `role`)
- `rejected`: Less preferred response (array with `content` and `role`)
- `prompt`: Initial prompt (string)
- `chat_template_kwargs`: Same structure as SFT
- `source`: Data source

## Data Format

**Storage Format**: Parquet (auto-converted from original format)

**Access Method**:

```python
from datasets import load_dataset

# Load specific subset
dataset = load_dataset("HuggingFaceTB/smoltalk2", "SFT")

# Load specific split
dataset = load_dataset("HuggingFaceTB/smoltalk2", "SFT", split="smoltalk_smollm3_everyday_conversations_no_think")
```

## Size Categories and Metadata

- **Size**: 1M - 10M rows
- **Modality**: Text
- **Format**: Parquet
- **Libraries**: Datasets, Dask, Polars, Croissant

## Associated Research

Referenced in:

- **arxiv:2410.15553** - SmolLM3 training methodology
- **arxiv:2412.15115** - Extended post-training techniques

## Repository Access

- **Hugging Face Repository**: https://huggingface.co/datasets/HuggingFaceTB/smoltalk2
- **Data Viewer**: Available at https://huggingface.co/datasets/HuggingFaceTB/smoltalk2/viewer/
- **Git Repository**: https://huggingface.co/datasets/HuggingFaceTB/smoltalk2/tree/refs%2Fconvert%2Fparquet

## Creator

**Organization**: Hugging Face Smol Models Research
**Community**: 3.34k followers

## Implementation Notes

The dataset weights for each subset vary during training according to specifications in SmolLM's official training recipe. The distinction between "think" (reasoning-enabled) and "no_think" variants in the SFT subset allows for flexible training configurations depending on reasoning capability requirements.
