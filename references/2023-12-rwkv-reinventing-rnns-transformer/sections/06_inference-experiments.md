# 6 Inference Experiments [p. 8]

[p. 8]

The authors benchmark inference requirements according to size and family. Specifically, they evaluate text generation speed and memory requirements on typical compute platforms including CPU (x86) and GPU (NVIDIA A100 80 GB). For all inference experiments they use float32 precision and the HuggingFace Transformers (Wolf et al., 2020). They include all model parameters in the parameter count, including both embedding and non-embedding layers. Performance under different quantization setups is left to further work. See Appendix K for more results.

**Figure 7** (p. 8): "Cumulative time on text generation for LLMs. Unlike transformers, RWKV exhibits linear scaling."
- X-axis: # Tokens, ranging from 0 to 1000.
- Y-axis: Cumulative time (s) in text generation, ranging from 0 to ~65 seconds.
- Five models plotted: facebook/opt-2.7b, EleutherAI/gpt-neo-2.7B, bigscience/bloom-3b, EleutherAI/pythia-2.8b, and rwkv-4-pile-3b.
- The four transformer models (OPT, GPT-Neo, BLOOM, Pythia) show superlinear (upward-curving) cumulative time as tokens increase, reaching ~45-65 seconds at 1000 tokens.
- RWKV (rwkv-4-pile-3b) exhibits a linear cumulative time curve, staying well below the transformer models at approximately ~10-15 seconds at 1000 tokens.
- This demonstrates RWKV's constant per-token inference cost (linear cumulative scaling), in contrast to the quadratic per-token cost of standard transformers.
