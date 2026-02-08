# C Hyperparameters [p. 8–9]

[p. 8] Table 5 provides the optimization hyperparameters for each one of the experiments, and Table 6 shows the model hyperparameters in the modern (Pile) setting.

**Table 5** (p. 9): The optimization hyperparameters used in this work. The *NAG* optimizer refers to Nesterov accelerated gradient (Nesterov, 1983), and Adam refers to (Kingma and Ba, 2015).

|                    | WikiText-103 | The Pile | Probe  | Masked LM   |
|--------------------|-------------|----------|--------|-------------|
| Sequence Length    | 512         | 1024     | 1024   | 128         |
| Optimizer          | NAG         | Adam     | Adam   | Adam        |
| Peak Learning Rate | 1           | 2e-3     | 2e-3   | 1e-3        |
| Warmup Steps       | 16,000      | 500      | 500    | 500         |
| Total Steps        | 286,000     | 10,000   | 10,000 | 10,000      |
| Tokens per Batch   | 72,000      | 256,000  | 64,000 | 1,024,000   |
| Dropout            | 0.3         | 0        | 0      | 0.1         |
| Weight Decay       | 0           | 0.01     | 0.01   | 0.01        |

**Table 6** (p. 9): The models hyperparameters by size.

|                          | 125M  | 350M  | 760M  | 1.3B  |
|--------------------------|-------|-------|-------|-------|
| Layers                   | 12    | 24    | 24    | 24    |
| Model Dimensions         | 768   | 1024  | 1536  | 2048  |
| Feed-forward Dimensions  | 3072  | 4096  | 6144  | 8192  |
| Attention Heads          | 12    | 16    | 16    | 32    |
