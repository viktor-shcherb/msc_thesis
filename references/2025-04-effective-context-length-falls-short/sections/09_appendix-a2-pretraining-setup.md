# A.2 Pretraining Setup [p. 17-18]

[p. 17-18]

## Model Architecture and Training Data [p. 17]

We pretrain two 1.3B models with maximum context window sizes of 2048 and 4096 to observe how the models gain the effective context length. The model architecture aligns with TinyLlama 1.1B¹. We utilize a hidden size of 2,048, the size of the feed-forward layers inside each transformer block is set to 5632. The model employs 32 attention heads and comprises 22 layers. The only difference is the use of the llama3 tokenizer (Llama Team, 2024), which has a larger vocabulary size of 128,256 tokens compared to the 32,000 tokens in TinyLlama 1.1B. This difference results in a larger embedding matrix. We used the SlimPajama-627B (Cerebras, 2023) dataset as our pretraining corpus and total training tokens for each model is 1T tokens.

¹https://huggingface.co/TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T/blob/main/config.json

## Training Infrastructure and Libraries [p. 17]

Our pretraining codebase is primarily built on the TinyLlama project², a popular codebase for reproducing Llama at the 1B scale. The main speed optimization libraries employed in this project are Fully Sharded Data Parallel (FSDP)³, FlashAttention-2 (Dao, 2023)⁴, and xFormers (Lefaudeux et al., 2022)⁵.

²https://github.com/jzhang38/TinyLlama
³https://huggingface.co/docs/accelerate/usage_guides/fsdp
⁴https://github.com/Dao-AILab/flash-attention

---
[p. 18 continued]

## Training Hyperparameters [p. 18]

We use the cross entropy loss as the pretraining objective and the AdamW optimizer (Loshchilov & Hutter, 2019). Additionally, we employed a cosine learning rate schedule with a maximum learning rate of $4 * 10^{-4}$, starting from a minimum learning rate of $4 * 10^{-5}$. The warmup steps are 2,000. The batch size is set to 4M tokens for different training context lengths. For the model pretrained with a 4K context length, the gradient accumulation is set to twice that of the model trained with a 2K context length. We pack the sequences in a mini-batch into a long sequence and used the variable-length version of Flash Attention⁶ to calculate casual self-attention on packed sequences. A gradient clipping threshold of 1.0 is used to stabilize the gradient.

⁵https://github.com/facebookresearch/xformers
⁶https://github.com/Lightning-AI/pytorch-lightning
⁷https://github.com/Dao-AILab/flash-attention/blob/main/flash_attn/flash_attn_interface.py#L1178

## Training Time [p. 18]

We utilized 16 NVIDIA 80G A100 GPUs on 2 nodes. Training a 1.3B model with a 2K context length and 1T tokens took approximately 28 days, while expanding the context length to a 4K context length took around 32 days.
