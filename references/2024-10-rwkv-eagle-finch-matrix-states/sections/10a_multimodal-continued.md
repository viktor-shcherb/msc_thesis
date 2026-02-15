# Multimodal Experiments (continued) [p. 15–16]

## 10.2 VisualRWKV (continued)

[p. 15–16] continue to be kept frozen. As shown in Table 6, we demonstrate that VisualRWKV's architecture is powerful for visual understanding and reasoning. With a smaller vision encoder CLIP-L (0.4B) and modest-sized LLMs of 1.5B and 3B, it achieves results comparable to the combination of CLIP-G (1.0B) and CLIP-H (1.0B) with larger LLMs of 7B and 13B. Moreover, in some benchmarks, it even outperforms larger models.

### Figure 9: VisualRWKV Architecture [p. 16]

**Figure 9:** VisualRWKV architecture overview.

The figure shows a flowchart with:
- **Input Image** (showing a photo of a blue jay bird) → **Vision Encoder** (blue box, frozen parameters)
- **Input Text** ("<image> what is the name of this bird?" in colored tokens) → **Embeddings** (orange box, trainable parameters)
- Both inputs feed into **LLM** (green box containing):
  - LM Head (orange, trainable)
  - RWKV Blocks (orange, trainable)
  - Embeddings (orange, trainable)
- Vision Encoder connects to LLM through **Projection** (orange box, trainable parameters)
- Output shown as "bluejay" (in green tokens)
- A legend indicates: blue boxes = Frozen Parameters, orange boxes = Trainable Parameters

### Table 6: VisualRWKV Benchmark Comparison [p. 16]

| Method | Vision Encoder | LLM | GQA (↑) | ScienceQA-IMG (↑) | Text-VQA (↑) | POPE (↑) |
|--------|----------------|-----|---------|-------------------|--------------|----------|
| BLIP-2 (Li et al., 2023a) | EVA01-CLIP-G | Vicuna-13B | 41.0 | 61.0 | 42.5 | 85.3 |
| BLIP-2 (Li et al., 2023a) | EVA01-CLIP-G | Flan-T5-11B | 44.8 | 64.5 | - | - |
| InstructBLIP(Dai et al., 2023) | EVA01-CLIP-G | Vicuna-7B | 49.2 | 60.5 | 50.1 | - |
| InstructBLIP(Dai et al., 2023) | EVA01-CLIP-G | Vicuna-13B | 49.5 | 63.1 | 50.7 | 78.9 |
| IDEFICS-9B (IDEFICS, 2023) | OpenCLIP-H | LLaMA-7B | 38.4 | - | 25.9 | - |
| IDEFICS-80B (IDEFICS, 2023) | OpenCLIP-H | LLaMA-65B | 45.2 | - | 30.9 | - |
| TinyGPT-V (Yuan et al., 2024) | EVA01-CLIP-G | Phi-2 (2.7B) | 33.6 | - | - | - |
| VisualRWKV | CLIP-L | Eagle-1.5B | 48.5 | 46.2 | 37.8 | 81.8 |
| VisualRWKV | CLIP-L | Eagle-3B | 49.7 | 58.3 | 46.4 | 81.4 |

Caption: A comparison of VisualRWKV to other state-of-the-art Multimodal Large Language Models (MLLMs) across 4 distinct benchmarks. We evaluate these models on benchmarks: GQA(Hudson & Manning, 2019), ScienceQA-IMG(Lu et al., 2022), Text-VQA(Singh et al., 2019) and POPE(Li et al., 2023c). For POPE, the average F1-score across three distinct categories—random, popular, and adversarial—was computed using the validation set of the MSCOCO dataset.

## 11 RWKV on Audio

[p. 16] AudioRWKV is the audio-specific version of RWKV, with a better process of the input audio spectrogram. Inspired by the VRWKV (Wang et al., 2024) [Note: PDF cites Wang et al. here, but the VRWKV paper is actually by Ke Yuan et al., 2024], we introduce a quad-directional shift (Q-Shift) to capture the neighboring relationships in two-dimensional audio spectrograms in the first step of each spatial-mix and channel-mix module. Specifically, the Q-Shift operation allows all tokens to be shifted and linearly interpolated with their neighboring tokens. We conduct experiments on the AudioSet (Gemmeke et al., 2017) dataset with various model sizes from 8.7M to 105M. As shown in Table 7, AudioRWKV-Tiny achieves a comparable performance with AST-AT by a smaller model size.

### Table 7: AudioRWKV Comparison [p. 17]

| Model | #Parameters | mAP |
|-------|-------------|-----|
| DeepRes Ford et al. (2019) | 26M | 0.392 |
| PANNs Kong et al. (2020) | 81M | 0.434 |
| HTS-AT Chen et al. (2022) | 28.8M | 0.437* |
| AudioRWKV-T | 8.7M | 0.435 |
| AudioRWKV-S | 28.4M | 0.452 |

Caption: A comparison of AudioRWKV to other baselines on AudioSet dataset. *Results reproduced by ourselves
