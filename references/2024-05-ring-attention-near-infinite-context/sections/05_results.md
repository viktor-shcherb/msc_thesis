# 5 Results [p. 6]

[p. 6] The primary objective is to comprehensively evaluate Ring Attention across multiple key metrics: maximum supported sequence length within accelerator memory, model flops utilization, and throughput. Ring Attention is compared with vanilla transformers [37], transformers with memory efficient attention [30], and transformers with both memory efficient attention and feedforward [23], across different model sizes and accelerator configurations.

## 5.1 Evaluating Max Context Size

[p. 6] Maximum supported context length is evaluated using fully sharded tensor parallelism (FSDP) [11], which is widely used in prior end-to-end training [36, 12]. No tensor parallelism is considered since the approach is independent of tensor parallelism. Practitioners can combine Ring Attention with tensor parallelism (shown in Section 5.2).

Using FSDP allows setting the same batch size in tokens for baselines and Ring Attention, ensuring a fair comparison. On $n$ devices, FSDP is used to shard the model for baselines, giving a sequence length of $l$. The total batch size in tokens is $nl$. FSDP is utilized along with Ring Attention to extend the sequence length to $\frac{nl}{m}$ and $m$ sequences. The total batch size in tokens remains the same, but Ring Attention enables a significantly larger context size. Table 3 summarizes the results.

**Table 3** (p. 7): The maximum context length supported in end-to-end training using fully sharded data parallelism and various transformer architectures. Different model sizes and accelerators shown. Baselines are vanilla transformer [37], transformer with memory efficient attention [30], and transformer with memory efficient attention and feedforward [23]. Context size is reported in tokens ($\times$1e3). Ring Attention substantially outperforms baselines and enables training sequences that are up to device count times longer than prior state-of-the-arts.

| Hardware | Model | Vanilla | Memory Efficient Attn | Memory Efficient Attn and FFN | Ring Attention (Ours) | Ours vs SOTA |
|---|---|---|---|---|---|---|
| 8x A100 NVLink | 3B | 4 | 32 | 64 | **512** | 8x |
| | 7B | 2 | 16 | 32 | **256** | 8x |
| | 13B | 2 | 4 | 16 | **128** | 8x |
| 32x A100 InfiniBand | 7B | 4 | 64 | 128 | **4096** | 32x |
| | 13B | 4 | 32 | 64 | **2048** | 32x |
| TPUv3-512 | 7B | 1 | 4 | 8 | **2048** | 256x |
| | 13B | 1 | 2 | 8 | **1024** | 128x |
| TPUv4-1024 | 3B | 8 | 16 | 32 | **16384** | 512x |
| | 7B | 4 | 8 | 16 | **8192** | 512x |
| | 13B | 4 | 8 | 16 | **4096** | 256x |
| | 30B | 2 | 4 | 8 | **2048** | 256x |
| TPUv5e-256 | 3B | 4 | 8 | 32 | **4096** | 128x |
| | 7B | 2 | 8 | 16 | **2048** | 128x |

[p. 7] Ring Attention consistently surpasses baselines, delivering superior scalability across diverse hardware setups. With 32 A100 GPUs, they achieve over 1 million tokens in context size for the 7B model, a 32 times improvement over previous best. When utilizing larger accelerators like TPUv4-512, Ring Attention enables a 256 times increase in context size, allowing training sequences of over 30 million tokens. The Ring Attention model scales linearly with the number of devices, as demonstrated by the 8x improvement over previous best on 8 A100 and the 256x improvement on TPUv3-512. If a model can be trained with context size $s$ on $n$ GPUs using blockwise attention and feedforward, with Ring Attention it becomes possible to train a model with a context size of $ns$.

## 5.2 Evaluating Model Flops Utilization

[p. 7-8] The authors evaluate the model flops utilization (MFU) of Ring Attention in standard training settings using fully sharded data parallelism (FSDP) [11] and tensor parallelism following LLaMA and OpenLLaMA [36, 12] with Jax SPMD. The batch size in tokens is 2M on 8/32x A100 and 4M on TPUv4-256. The goal is investigating the impact of model size and context length on MFU, a critical performance metric.

Table 5.1 presents the results of experiments on MFU for different model sizes and context lengths. The achieved MFU is presented using state-of-the-art memory efficient transformers BPT [23], compared to the anticipated MFU based on these results, and the actual MFU obtained with Ring Attention. For fair comparison, both BPT and Ring Attention are based on the same BPT implementation on both GPUs and TPUs.

Ring Attention trains much longer context sizes for self-attention, resulting in higher self-attention FLOPs compared to baseline models. Since self-attention has a lower MFU than feedforward, Ring Attention is expected to have a lower MFU than the baseline models. The method offers a clear advantage in terms of maintaining MFU while enabling training with significantly longer context lengths. As shown in Table 5.1, when comparing the approach to prior state-of-the-arts, it is evident that very large context models can be trained without compromising MFU or throughput.

**Table 4 / Figure** (p. 8): Model flops utilization (MFU) with different training configurations: model sizes, compute, and context lengths. Ring Attention enables training large models (7B-65B) on large input context sizes (over 4M) with negligible overheads.

The figure is a bar chart comparing MFU (%) across five training configurations:
- 7B on A100-8 (32K vs 256K)
- 13B on A100-8 (16K vs 128K)
- 13B on A100-32 (64K vs 2048K)
- 30B on TPUv4-1024 (16K vs 2048K)
- 65B on TPUv4-1024 (8K vs 1024K)

Three bars per configuration: Memory Efficient Attention & FFN (blue), Ring Attention expected (red/orange), Ring Attention actual (green). All three bars are similar in height (~30-35% MFU), showing negligible overhead from Ring Attention.

| | Model size | 7B | 13B | 13B | 30B | 65B |
|---|---|---|---|---|---|---|
| | Compute | 8x A100 | 8x A100 | 32x A100 | TPUv4-1024 | TPUv4-1024 |
| Memory efficient attention & FFN | Context size ($\times$1e3) | 32 | 16 | 64 | 16 | 8 |
| Ring Attention | Context size ($\times$1e3) | 256 | 128 | 2048 | 2048 | 1024 |

## 5.3 Impact on In Context RL Performance

[p. 8-9] The authors present results of applying Ring Attention for learning trial-and-error RL experience using Transformers. The proposed model is evaluated on the ExoRL benchmark across six different tasks. On ExoRL, cumulative return is reported, as per ExoRL [39].

Comparisons are made with:
- BC (behavior cloning) — from ExoRL and AT paper
- DT (Decision Transformer) [4] — from ExoRL and AT paper
- AT (Algorithm Transformer) [22] — from ExoRL and AT paper
- AT + ME (AT with memory efficient attention [30])
- AT + BPT (AT with blockwise parallel transformers [23])
- AT + RA (AT with Ring Attention)

Since the ExoRL data is highly diverse, having been collected using unsupervised RL [19], it has been found that TD learning performs best, while behavior cloning struggles [39]. AT [22] shows that conditioning Transformer on multiple trajectories with relabeled target return can achieve competitive results with TD learning. The interest is in applying Ring Attention to improve the performance of AT by conditioning on a larger number of trajectories rather than 32 trajectories in prior works. Each trajectory has $1000 \times 4$ length where 1000 is sequence length while 4 is return-state-action-reward, making training 128 trajectories with modest 350M size model infeasible for prior state-of-the-art blockwise parallel transformers.

**Table 5** (p. 8): Application of Ring Attention on improving Transformer in RL. BC and DT use vanilla attention. AT + ME denotes using memory efficient attention, AT + BPT denotes using blockwise parallel transformer. AT + RA denotes using Ring Attention.

| ExoRL Task | BC-10% | DT | AT + ME (N Trajs = 32) | AT + BPT (N Trajs = 32) | AT + BPT (N Trajs = 128) | AT + RA (N Trajs = 128) |
|---|---|---|---|---|---|---|
| Walker Stand | 52.91 | 34.54 | oom | 95.45 | oom | 98.23 |
| Walker Run | 34.81 | 49.82 | oom | 105.88 | oom | 110.45 |
| Walker Walk | 13.53 | 34.94 | oom | 78.56 | oom | 78.95 |
| Cheetah Run | 34.66 | 67.53 | oom | 178.75 | oom | 181.34 |
| Jaco Reach | 23.95 | 18.64 | oom | 87.56 | oom | 89.51 |
| Cartpole Swingup | 56.82 | 67.56 | oom | 120.56 | oom | 123.45 |
| **Total Average** | **36.11** | **45.51** | oom | **111.13** | oom | **113.66** |

[p. 9] Results in Table 5 show that, by scaling up the sequence length (number of trajectories), AT + Ring Attention consistently outperforms original AT with BPT across all six tasks, achieving a total average return of 113.66 compared to the AT with BPT model's total average return of 111.13. The results show that the advantage of Ring Attention for training and inference with long sequences.

## 5.4 Impact on LLM Performance

[p. 9] The authors evaluate Ring Attention by applying their method to finetune a LLaMA model to longer context. While the approach enables training with millions of context tokens, finetuning was conducted on the LLaMA-13B model, limiting the context length to 512K tokens due to constraints on cloud compute budget. Finetuning was carried out on 32 A100 GPUs, using the ShareGPT dataset, following methodologies as outlined in prior works [6, 13]. The finetuned model was then evaluated on the line retrieval test [20]. In this test, the model needs to precisely retrieve a number from a long document, which can effectively capture the abilities of text generation, retrieval, and information association at long context, reflected by the retrieving accuracy.

**Figure 3** (p. 9): "Comparison of different models on the long-range line retrieval task."

The figure is a line plot with Context Length (tokens) on the x-axis (4K, 8K, 12K, 16K, 64K, 100K, 200K, 500K) and Accuracy (%) on the y-axis (0.0 to 1.0). Four models compared:
- Vicuna-13B(16K): accuracy starts near 1.0 at 4K, drops to ~0.6 at 12K, no data beyond 16K
- OpenAI GPT3.5(16K): accuracy near 1.0 from 4K to 16K, no data beyond 16K
- Anthropic Claude2(100K): accuracy near 1.0 from 4K to ~64K, slight drop to ~0.9 at 100K, no data beyond 100K
- Ring Attention-13B(512K): accuracy maintains high levels (~0.9) across all context lengths from 4K to 500K

Ring Attention-13B-512K stands out as it maintains high accuracy levels even with long contexts. GPT3.5-turbo-16K, Vicuna-16B-16K, and Claude-2-100K demonstrate competitive accuracy within short context lengths but cannot handle extended context lengths.
