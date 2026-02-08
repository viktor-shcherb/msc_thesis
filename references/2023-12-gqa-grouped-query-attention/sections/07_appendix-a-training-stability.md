# A Training Stability [p. 7]

Multi-query attention can lead to training instability during fine-tuning, in particular combined with long input tasks. Multiple T5-Large models trained with multi-query attention from scratch suffered from frequent loss spikes during pre-training, and the final models diverged immediately when fine-tuning on long-input tasks. [p. 7]

Uptrained multi-query attention models are more stable but still display high variance, so for multi-query models on unstable tasks the authors report average performance over three fine-tuning runs. [p. 7]

Uptrained grouped-query attention models, however, appear to be stable, so the authors did not investigate further on the root causes of multi-query instability. [p. 7]
