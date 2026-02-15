# 2 Detecting Retrieval Head [p. 3–4] (continued)

---
[p. 3–4 continued]

perform Needle-in-a-Haystack on 20 different length values uniformly sampled from 1K-50K, where in each length, q is inserted in 10 different positions uniformly ranging from the start to the end of x. The authors note that this scale of tests gives stable outputs as the average retrieval score converges after just a few samples. In total, each language model goes through approximately 600 instances of retrieval testing. The authors calculate the retrieval score for each attention head in each test and use the average of these scores as the head's final retrieval score. If an attention head's final retrieval score can be considered as retrieval head. In our case (Fig. 3), the authors set the threshold as 0.1, meaning that as long as the head performs copy-paste in 10% of the times, the authors consider it a retrieval head.

**Table 1** (p. 3): We consider a wide range of language model families and show that the basic properties of retrieval heads are universal and consistent across all language models we study.

| Base Model | Variant | Variation Type |
|------------|---------|----------------|
| Llama-2-7B | Llama-2-7B-80K | Length Extension via Continue Pretrain |
| | Llama-2-13B-64K | Model Scaling and Length Extension |
| Mistral-7B-v0.2 | Mistral-7B-Instruct-v0.2 | SFT and RLHF |
| | Mistral-8x7B-v0.1 | Sparse Upcycling to Mixture of Experts |
| Yi-6B | Yi-6B-200K | Length Extension via Continue Pretrain |
| | Yi-34B-200K | Model Scaling and Length Extension |
| Qwen1.5-14B | Qwen1.5-14B-Chat | SFT and RLHF |

**Figure 3** (p. 4): "Retrieval heads are universal and sparse across model family and scale. For all models we consider, less than 5% of the attention heads are activated more than 50% of the time (with a retrieval score higher than 0.5) when retrieval is required."

Description: Eight pie charts showing retrieval head distribution across different models.
- Key elements: Each pie chart shows proportion of heads in four categories: =0 (light blue, largest), 0-0.1 (dark blue), 0.1-0.5 (medium shade), 0.5-1 (red, smallest)
- Models shown: Llama-2-7B-80K (32 × 32 heads, 70.2% =0, 26.5% 0-0.1, 2.6% 0.1-0.5, 0.6% 0.5-1); Yi-6B-200K (32 × 32 heads, 50.7% =0, 43.7% 0-0.1, 4.9% 0.1-0.5, 0.8% 0.5-1); Qwen1.5-14B (40 × 40 heads, 53.5% =0, 42.8% 0-0.1, 3.2% 0.1-0.5, 0.6% 0.5-1); Mistral-7B-v0.2 (32 × 32 heads, 65.2% =0, 30.8% 0-0.1, 3.7% 0.1-0.5, 0.5% 0.5-1); Llama-2-13B-64K (40 × 40 heads, 73.2% =0, 24.8% 0-0.1, 1.7% 0.1-0.5, 0.4% 0.5-1); Yi-34B-200K (60 × 56 heads, 44.8% =0, 51.8% 0-0.1, 3.1% 0.1-0.5, 0.4% 0.5-1); Qwen1.5-14B-Chat (40 × 40 heads, 71.1% =0, 24.6% 0-0.1, 4.2% 0.1-0.5, 0.1% 0.5-1); Mistral-8x7B-v0.1 (32 × 32 heads, 57.6% =0, 36.2% 0-0.1, 5.5% 0.1-0.5, 0.7% 0.5-1)
- Notable patterns: Across all models, less than 5% of heads have retrieval scores > 0.5, and the majority (44-73%) have zero retrieval score
- Supports claim: Retrieval heads are sparse and universal across model families and scales

# 3 Basic Properties of Retrieval Heads [p. 4]

This section discusses important properties of retrieval heads: (1) universal and sparse: any model that exhibits long-context capability has a small set of retrieval heads; (2) dynamic: most of retrieval heads are activated under different contexts; (3) intrinsic: retrieval heads are already within the base model as a consequence of large-scale pretraining; models reuse the same set of heads. The results are supported by extensive experiments on a large spectrum of models (Table 1). To investigate the influence of continued pretraining for long context extension, the authors compare Llama-2-7B 4K to Llama-2-7B-80K and Llama-2-13B-60K [6]. To examine the effect of alignment, the authors have study Mistral-7B-Instruct-v0.2 and Qwen-1.5-14B-Chat [2] and compare them to their base versions. The authors further choose Mixtral-8x7B-v0.1 [13], a mixture of expert versions derived from Mistral-7B-v0.2, presumably via sparse upcycling [16], to study retrieval heads in different architectures.

## 3.1 Universal and Sparse [p. 4]

Figure 3 demonstrate that a sparse set of retrieval heads exist in all models the authors consider, regardless of the various pretraining, fine-tuning strategies and the underlying architecture. Between 25% and 52% of the heads exhibit copy-paste behaviors at a very low frequency, with a score of between 0 and 0.1. Approximately 45% to 73% of attention heads have 0 retrieval score, meaning that they have other functionality than retrieval. Only about 3% to 6% of the attention heads have a retrieval score larger than 0.1 (recall that a retrieval score 0.1 means a head retrieves at least 10% of the tokens being asked). It is also intriguing that although all model parameters, particularly the total number to attention heads, are largely different from each other, their ratio of retrieval heads lays in the same interval (about 5%).
