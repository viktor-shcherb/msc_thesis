# Appendix D: Hyperparameters [p. 12-13]

[p. 12-13] Each of the baseline models is finetuned on every dataset separately using AdamW (Loshchilov and Hutter, 2019) with beta = (0.9, 0.98), epsilon = 1e-6, mixed precision (fp16), and gradient checkpointing.

Effective batch size: 131,072 (2^17) tokens, achieved by processing 16,384 tokens per GPU across 8 NVIDIA V100 (32GB) GPUs either in parallel or via gradient accumulation.

Training epochs by dataset:
- Summarization datasets (GovReport, SummScreenFD, QMSum): 10 epochs
- Qasper, QuALITY, and ContractNLI: 20 epochs
- NarrativeQA (the largest dataset): 2 epochs

Learning rate tuning: the maximum learning rate is tuned over each validation set, selecting from 6 possible values: 1e-5, 2e-5, 5e-5, 1e-4, 2e-4, 5e-4.

Learning rate schedule: warmed up from zero during the first 10% of the learning schedule, and then linearly decays back to zero throughout the remaining 90%.

Dropout: 0.1 applied throughout each network.

Inference: outputs generated using greedy decoding.
