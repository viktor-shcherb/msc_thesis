# 4 Experiments [p. 7-9]

## 4.1 Language Modeling [p. 7-9]

[p. 7] The efficacy of retrieving earlier blocks is first evaluated on two language modeling tasks which can be expected to have long-range token interactions: English language books (PG-19) [29] (3.7B tokens), and math papers from arXiv (5.6B tokens). Additional details about the datasets are provided in Appendix B. Results show that models trained with landmark tokens can retrieve relevant blocks, obtaining comparable perplexity as a Transformer-XL while reducing FLOPs. In contrast with Transformer-XL, using the landmark method, the information retrieval is interpretable since the exact tokens attended to by the model can be identified by looking at the attention scores or looking at the set of retrieved blocks. Particularly, it is possible to understand which parts of the text was recovered to generate a certain answer, which can for example be useful to remove inaccurate information. Results also demonstrate that using the inference mechanism described in Section 3.2, the models can be used at much longer context than the one used for training.

### Model & Training

[p. 7-8] A GPT-2 [28]-like architecture is used: a 12-layer decoder-only transformer with 8 heads in each layer, each with dimension 128 (embedding dimension 1024), and hidden FFN size of 4096. The model is trained using AdamW [22] with beta_1 = 0.9 and beta_2 = 0.95. Weight decay with factor 0.001 is applied. Base learning rate is 0.002 for all experiments with a warmup stage that is 2% of the whole training, and a cosine scheduler with minimum (final) [p. 8] learning rate being 0.0004. GPT-2's [28] tokenizer is used. When using landmark tokens, the tokens are added to the dataset and stored as part of the train dataset, leaving the batching mechanism unchanged. Gradient accumulation as well as data-parallel training across four nodes is used to maintain an effective total batch size of 128. Mixed-precision training with bfloat16 over at most 4 Nvidia A100 GPUs is used. The model is trained on each dataset for 240K steps with context length ℓ_seq = 512. Transformer-XL is trained with a window size of 256 (i.e. effective context size 512) over segments of length 2048. Transformer-XL is trained to observe the same number of tokens during training as the landmark method which translates to performing 60K steps.

### Results

[p. 8] To evaluate the model's performance with different context lengths, the validation data is divided into equally sized segments, referred to as evaluation lengths. Each segment is separately inputted into the model, which is further divided into chunks using the method described in Section 3.2. The chunk size, denoted as ℓ_local, represents the local context accessible without any memory.

**Table 1** (p. 8): "Performance of different training and inference settings in terms of language modeling perplexity. The column XL cache shows the size of the XL cache available both during training and inference which was only used when training Transformer-XL[9]. When using landmarks, the column 'Blocks' shows the maximum number of blocks stored in memory. Each block contains ℓ_block = 50 normal tokens and one landmark token. Due to computation limitations we only report results for Transformer-XL on PG-19 as this method takes longer to train in our implementation."

| Eval. Length | ℓ_local | XL cache | Blocks | k | Attention Size | PG19  | arXiv | Method   |
|-------------|---------|----------|--------|---|---------------|-------|-------|----------|
| 512         | 512     | None     | None   | - | 512           | 16.12 | 4.01  | Baseline |
| 512         | 360     | None     | None   | - | 360           | 16.76 | 4.31  | Baseline |
| 512         | 250     | None     | 10     | 2 | 360           | 16.23 | 4.01  | Ours     |
| 2048        | 256     | 256      | None   | - | 512           | 14.72 | -     | [9]      |
| 2048        | 250     | None     | 40     | 2 | 360           | 15.14 | 3.43  | Ours     |
| 2048        | 350     | None     | 40     | 2 | 460           | 15.07 | 3.41  | Ours     |
| 2048        | 300     | None     | 40     | 3 | 460           | 14.97 | 3.36  | Ours     |
| 2048        | 250     | None     | 20     | 4 | 460           | 15.02 | 3.37  | Ours     |
| 2048        | 250     | None     | 40     | 4 | 460           | 14.92 | 3.35  | Ours     |
| 4096        | 256     | 256      | None   | - | 512           | 14.55 | -     | [9]      |
| 4096        | 250     | None     | 40     | 4 | 460           | 14.79 | 3.19  | Ours     |
| 4096        | 250     | None     | 80     | 2 | 370           | 15.00 | 3.29  | Ours     |
| 4096        | 250     | None     | 80     | 4 | 470           | 14.72 | 3.18  | Ours     |

Table 1 presents the perplexity of the trained models under various inference settings. Notably, by using a local context length of 250 and retrieving the top k = 2 most relevant blocks, comparable performance with a context length of 512 is achieved. This corresponds to attending to 360 tokens, including 250 tokens from the local context, 10 landmark tokens, and 100 tokens from the retrieved blocks. The effectiveness of using landmark tokens with retrieval becomes even more evident when comparing it to standard inference with an attention length of 360. The results demonstrate that intelligently recovering relevant blocks enables attending to a significantly smaller number of tokens while maintaining performance.

Furthermore, the results highlight that landmark tokens enable the model to operate with larger context lengths than those encountered during training. The improvement in perplexity clearly indicates that the retrieved blocks contribute to the model's performance, making the results comparable to a Transformer-XL trained with segments of length 2048. However, unlike Transformer-XL, which can only leverage past information through recurrence, the landmark method allows the model to attend to any token from the past, facilitating both the retention of exact fine-grained details and the interpretability of information utilization mechanisms.

Finally, the number of retrieved blocks and the number of blocks stored in memory can be adjusted during inference. While reducing the number of retrieved blocks k adversely affects performance, results demonstrate that the model still outperforms the baseline even with only 2 retrieved blocks at context lengths of 2048 and 4096. Notably, when keeping only the last 40 blocks in memory, the model performs better at an evaluation length of 4096 compared to 2048. This suggests that the model is also learning to utilize recurrent mechanisms similar to those in Transformer-XL.

### Granularity of Cache Block Retrieval

[p. 9] Block retrieval can be performed on different levels of granularity. At the most granular level, the set of retrieved blocks can be different for each head and each token. This setting is the same as the model experiences during training. However, it is possible to further limit this granularity at inference, for increased system throughput. This section evaluates the effect of maintaining the same set of retrieved blocks across tokens or across heads.

**Table 2** (p. 9): "Performance on PG19 dataset for different levels of retrieval flexibility. The blocks column shows the theoretical total number of blocks that can be accessed from the memory when feeding the input in windows of length 250 to the model."

| Per Head | Per Token | Eval. Length | k | Blocks      | Perplexity |
|----------|-----------|-------------|---|-------------|------------|
| Yes      | Yes       | 2048        | 2 | 250 * 8 * 2 | 15.14      |
| Yes      | Yes       | 2048        | 4 | 250 * 8 * 4 | 14.92      |
| Yes      | Yes       | 4096        | 4 | 250 * 8 * 4 | 14.72      |
| Yes      | No        | 2048        | 2 | 8 * 2       | 15.48      |
| Yes      | No        | 2048        | 4 | 8 * 4       | 15.10      |
| Yes      | No        | 4096        | 4 | 8 * 4       | 14.95      |
| No       | Yes       | 2048        | 2 | 250 * 2     | 15.44      |
| No       | Yes       | 2048        | 4 | 250 * 4     | 15.04      |
| No       | Yes       | 4096        | 4 | 250 * 4     | 14.89      |

While reducing the flexibility has a noticeable adverse effect on performance, the model still improves over the baseline. In particular, it is possible to retrieve the same set of blocks for all tokens across heads while only suffering 0.23 points in perplexity (which varies across heads). Further insights into the expected improvement in speed gained from using a less flexible selection scheme are discussed in Appendix C, where the distribution of the retrieved blocks is further analyzed.

## 4.2 Fine-Tuning Pre-Trained Models [p. 9]

[p. 9] The possibility of fine-tuning a large language model using landmark tokens and therefore extending the model's context length is demonstrated. Namely, LLaMA 7B [38] is fine-tuned for 15000 steps using the landmark method. To reduce computation, the model is fine-tuned with context length 512. The sample subset of RedPajama^1 is used for the fine-tuning which closely follows the dataset curation process used for training LLaMA.

^1 https://github.com/togethercomputer/RedPajama-Data

The efficacy of the method is evaluated by comparing the model's ability to recover a hidden pass phrase inside a text segment. In particular, randomly generated prompts of the format described in Figure 3a are used and the accuracy of generating the correct pass key (as the first integer within the first 100 generated tokens) is computed. The result is plotted in Figure 3b for different context lengths. The base model is capable of finding the pass phrase until a certain length, even slightly exceeding its default training context length of 2048 (the area shared in grey). However, the base model completely fails at the task for larger contexts. In contrast, the landmark version can always retrieve the pass phrase with high accuracy, even for significantly larger context lengths. When evaluating the model with very large inputs (e.g. 32K), additional techniques are used to reduce the memory usage by offloading the KV cache (except the landmarks) to CPU. This is discussed in more detail in Appendix G.

**Figure 3** (p. 10): "(a) Prompt Format (b) Retrieval Accuracy"

- **(a) Prompt Format**: Shows the prompt template used for the pass key retrieval test. The prompt contains a hidden info message instructing the model to find and memorize important information. A prefix filler is generated by continuously repeating sentences like "The grass is green. The sky is blue. The sun is yellow. Here we go. There and back again." The pass key line reads "The pass key is \<PASS KEY\>. Remember it. \<PASS KEY\> is the pass key." followed by a suffix filler, and finally "What is the pass key? The pass key is".

- **(b) Retrieval Accuracy**: A line plot with x-axis "Prompt Length (Tokens)" ranging from 0 to 30000 and y-axis "Accuracy" ranging from 0 to 100. Two lines are shown:
  - **LLaMA 7B** (blue/yellow): Maintains near-100% accuracy up to roughly 2048 tokens (the grey-shaded region marking original LLaMA training context length), then drops sharply to 0% at around 3000-5000 tokens, remaining at 0% (marked with red crosses indicating the model ran out of memory at the largest sizes).
  - **Landmark Finetuning** (green/orange): Maintains near-100% accuracy across all tested prompt lengths up to 32000 tokens. Points marked with a green star use a more efficient inference mechanism (see Section G).

Caption: "Prompt format used for comparing retrieval accuracy of the vanilla LLaMA 7B and its counterpart fine-tuned with landmarks. The points marked with a red cross represent cases where the model ran out of memory. Points marked with a green star use a more efficient inference mechanism (see Section G). Inference is done by feeding the segment in windows of length 250 tokens (excluding the inserted landmark tokens). The top k = 4 landmarked blocks are retrieved. Retrieval accuracy is measured for a fixed total prompt length, by using the suffix and prefix filler. Results are averaged over 50 random generations of the pass key (a random number between 1 and 50000), which each time is located at a random position in the full-length prompt. The space before and after the pass key is filled accordingly by the suffix and prefix filler. The gray box marks the region where the prompt length is within lengths used during original LLaMA training."
