# SmolLM3: smol, multilingual, long-context reasoner

**Author(s):** Elie Bakouch, Carlos Miguel Patino, Anton Lozhkov, Edward Beeching, Aymeric Roucher, Nouamane Tazi, Aksel Joonas Reedi, Guilherme Penedo, Hynek Kydlicek, Clementine Fourrier, Nathan Habib, Kashif Rasul, Quentin Gallouedec, Hugo Larcher, Mathieu Morlon, Joshua Lochner, Vaibhav Srivastav, Xuan-Son Nguyen, Colin Raffel, Lewis Tunstall, Loubna Ben Allal, Leandro von Werra, Thomas Wolf
**Type:** Blog post
**Date:** July 2025
**Primary URL:** https://huggingface.co/blog/smollm3

## Summary

SmolLM3 is a 3 billion parameter language model trained on 11.2 trillion tokens, designed to push the boundaries of small model performance with dual-mode reasoning capabilities, long context support (up to 128k tokens), and multilingual competence across 6 languages. The model features fully open weights and training details, including a three-stage pretraining curriculum, context extension via RoPE theta scaling and YARN extrapolation, 140B token reasoning midtraining, and alignment via Anchored Preference Optimization (APO). SmolLM3 achieves competitive performance with 4B models while maintaining the efficiency of 3B scale.

## Source structure

1. **SmolLM3 blog post** - Main technical report covering architecture, training curriculum, long context extension, midtraining, post-training, and comprehensive benchmark results
2. **SmolLM GitHub repository** - Official repository with training scripts, model implementation, and documentation
3. **SmolLM3-3B model card (instruct)** - Model card for the instruction-tuned variant with usage examples, benchmark tables, and deployment instructions
4. **SmolLM3-3B-Base model card** - Base model specifications, pretraining details, and evaluation results
5. **SmolLM3 training configurations** - Dataset containing exact hyperparameters and training configuration files
6. **SmolTalk2 dataset** - Post-training dataset documentation with SFT, midtraining, and preference data composition
