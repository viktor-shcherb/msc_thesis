# Conclusion [p. 9]

[p. 9] The paper concludes that PoSE extends LLM context windows by manipulating position indices while training at original context length, i.e., decoupling train length from target length.

[p. 9] Reported outcomes:
- Lower memory/time overhead than full-length fine-tuning.
- Extension up to 128k on 8xV100 GPUs with "minimal performance degradation" on standard benchmarks.
- Compatibility across RoPE-based LLMs and PI strategies.
