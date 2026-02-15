# Source Manifest

## Sources

### 1. SmolLM3 blog post (main technical report)
- **URL:** https://huggingface.co/blog/smollm3
- **Type:** blog-post
- **Extract:** Full technical report covering architecture design (GQA, NoPE, tied embeddings), three-stage pretraining curriculum (11.2T tokens across web/code/math), long context extension (4k to 64k via RoPE theta scaling, 128k via YARN extrapolation), midtraining on 140B reasoning tokens, supervised fine-tuning, alignment via Anchored Preference Optimization (APO), multilingual support (6 languages), and benchmark results across reasoning, coding, math, and long-context tasks
- **Priority:** primary

### 2. SmolLM GitHub repository
- **URL:** https://github.com/huggingface/smollm
- **Type:** github-repo
- **Extract:** Training scripts, configuration files, model architecture implementation details, and any technical documentation not covered in the blog post
- **Priority:** primary

### 3. SmolLM3-3B model card (instruct)
- **URL:** https://huggingface.co/HuggingFaceTB/SmolLM3-3B
- **Type:** documentation
- **Extract:** Model card with usage instructions, benchmark tables, hardware requirements, license information, and any additional technical details about the instruct/reasoning variant
- **Priority:** supplementary

### 4. SmolLM3-3B-Base model card
- **URL:** https://huggingface.co/HuggingFaceTB/SmolLM3-3B-Base
- **Type:** documentation
- **Extract:** Base model specifications, pretraining details, and evaluation results on base model benchmarks
- **Priority:** supplementary

### 5. SmolLM3 training configurations
- **URL:** https://huggingface.co/datasets/HuggingFaceTB/smollm3-configs
- **Type:** documentation
- **Extract:** Exact hyperparameters, data mixture ratios, learning rate schedules, and hardware configuration used across all training stages
- **Priority:** supplementary

### 6. SmolTalk2 dataset
- **URL:** https://huggingface.co/datasets/HuggingFaceTB/smoltalk2
- **Type:** documentation
- **Extract:** Dataset composition for SFT, midtraining, and preference data; data curation methodology
- **Priority:** supplementary
