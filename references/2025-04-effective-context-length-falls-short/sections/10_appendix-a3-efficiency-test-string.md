# A.3 Efficiency Test of STRING [p. 18]

[p. 18]

In this section, we demonstrate that STRING can be implemented with negligible additional overhead compared to flash attention by comparing the inference time and GPU memory consumption. We test the baseline and STRING on a single NVIDIA 80G A100 GPU based on Llama3.1 8B. The long inputs are sourced from the summarization task in InfiniteBench (Zhang et al., 2024d). We test the model 50 times and report the average results. The results of inference time are shown in Figure 9a, where we test the model with context lengths ranging from 64K to 128K. STRING maintains the average time consumed per token within 0.3 seconds of the baseline Flash Attention. Figure 9b shows the consumption of GPU memory, with the growth of input context lengths, STRING exhibiting only a less than 5GB increase.

**Figure 9** (p. 18): "Efficiency Test of STRING and the standard Flash Attention based on Llama3.1 8B. All experiments are run on a single NVIDIA 80G A100 GPU."

Description: Two bar charts comparing efficiency metrics
- Key elements:
  - (a) Inference time: X-axis shows training length from 64K to 128K, Y-axis shows "Average time per token (s)". Two bar types: "FlaSh-Attn" (blue) and "FlaSh-Attn+STRING" (orange)
  - (b) GPU memory consumption: X-axis shows training length from 64K to 128K, Y-axis shows "GPU Memory (G)". Same two bar types
- Notable patterns from (a):
  - At 64K: FlaSh-Attn ≈ 1.70, FlaSh-Attn+STRING ≈ 1.78
  - At 80K: FlaSh-Attn ≈ 2.02, FlaSh-Attn+STRING ≈ 2.12
  - At 96K: FlaSh-Attn ≈ 2.38, FlaSh-Attn+STRING ≈ 2.47
  - At 112K: FlaSh-Attn ≈ 2.72, FlaSh-Attn+STRING ≈ 2.82
  - At 128K: FlaSh-Attn ≈ 3.03, FlaSh-Attn+STRING ≈ 3.14
- Notable patterns from (b):
  - At 64K: FlaSh-Attn ≈ 47.93, FlaSh-Attn+STRING ≈ 47.99
  - At 80K: FlaSh-Attn ≈ 56.48, FlaSh-Attn+STRING ≈ 56.56
  - At 96K: FlaSh-Attn ≈ 64.94, FlaSh-Attn+STRING ≈ 65.07
  - At 112K: FlaSh-Attn ≈ 73.48, FlaSh-Attn+STRING ≈ 73.58
  - At 128K: FlaSh-Attn ≈ 81.90, FlaSh-Attn+STRING ≈ 86.64
- Supports claim: STRING adds negligible overhead to inference time (within 0.3s per token) and modest GPU memory increase (less than 5GB even at 128K context) [p. 18]
