# Appendix J: Architectural Ablations [p. 40]

[p. 40] Our improvements consist of architectural advances, a diverse multilingual corpus, and an optimized efficient tokenizer. To demonstrate that pure architectural advances indeed contribute to overall performance improvement, we ran an ablation where we train a 170 million parameter RWKV-6 model (which has 12 layers with dimension 768) from scratch on the Pile dataset using GPT-NeoX-20B tokenizer (vocabulary size V = 50277), which yields 6 tokens in total. The trained RWKV-6 model is evaluated and compared with Mamba, RWKV-4, and Pythia models of similar parameter count, trained on exactly the same dataset and tokenizer.

### Table 18: Ablation Results [p. 40]

| Model | lmb.o ppl↓ | lmb.o acc↑ | hella acc_n↑ | piqa acc↑ | sc16 acc↑ | arc-e acc↑ | arc-c acc↑ | winG acc↑ | headqa acc_acc_n↑ | obqa acc_acc_n↑ | sciq acc↑ | record em↑ | copa acc↑ | avg acc↑ |
|-------|------------|------------|--------------|-----------|-----------|------------|------------|-----------|-------------------|-----------------|-----------|------------|-----------|----------|
| RWKV4-Pile | 29.2 | 33.1 | 32.2 | 64.9 | 59.1 | 47.1 | 23.9 | 51.5 | 28.3 | 29.4 | 77.2 | 61.9 | 64.0 | 47.7 |
| Pythia | 24.4 | 38.8 | 31.7 | 62.6 | 58.4 | 45.3 | 24.0 | 52.0 | 28.7 | 29.0 | 76.5 | 66.3 | 62.0 | 47.9 |
| Mamba | 16.0 | 44.2 | 35.3 | 64.4 | 60.4 | 48.1 | 24.3 | 52.4 | 28.8 | 28.6 | 78.1 | 68.8 | 68.0 | 50.1 |
| RWKV6-Pile | 16.1 | 44.5 | 34.9 | 64.4 | 60.7 | 48.4 | 24.7 | 51.9 | 29.3 | 29.6 | 80.6 | 69.3 | 70.0 | 50.7 |

Caption: Ablation Results. Labels are the same from Table 4.
