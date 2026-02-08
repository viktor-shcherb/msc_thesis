# E Llama-2 Performance [p. 15-16]

The authors evaluate Llama-2 (Touvron et al., 2023b) on multi-document QA with 20 total documents in each input context. The Llama tokenizer produces longer sequences than the tokenizers for the previously-studied models, so 20 examples (out of 2655) that exceed Llama-2's maximum context length of 4096 tokens are discarded. The authors experiment with models of varying sizes (7B, 13B, and 70B parameters), with and without additional supervised fine-tuning and reinforcement learning from human feedback ("-chat-" models). The results are presented in Figure 16. [p. 15-16]

Comparing Llama-2 models of varying sizes, the authors find that only the larger models (13B and 70B) exhibit the U-shaped performance curve (i.e., both primacy and recency bias) -- the smallest Llama-2 models (7B) are solely recency-biased. Given these results, the authors hypothesize that prior work (e.g., Khandelwal et al., 2018; Sun et al., 2021) did not previously observe any primacy bias in language models because the models they studied were too small (less than 1B parameters). [p. 16]

Comparing between Llama-2 models with and without additional supervised fine-tuning and reinforcement learning from human feedback, additional fine-tuning dramatically improves performance on the multi-document QA task. The 7B models with and without additional fine-tuning show minimal primacy bias, and are largely recency-biased. The 13B base model has a dramatic primacy and recency bias -- there is a 20-point accuracy disparity between the best- and worst-case performance. Applying additional fine-tuning to the 13B seems to slightly reduce this bias (10-point worst-case degradation), but the bias remains significant. However, the 70B models with and without additional fine-tuning have largely similar trends (showing both primacy and recency bias), and additional fine-tuning minimally changes the positional bias severity. [p. 16]

**Figure 16** (p. 16): "Multi-document QA performance (20 total documents) of Llama-2 models of varying sizes (7B, 13B, 70B parameters), with and without additional supervised fine-tuning and reinforcement learning from human feedback ('-chat-' models)."

The figure shows accuracy (y-axis, approximately 20-70%) vs. position of document with the answer (x-axis, 1st to 20th) for 20 total retrieved documents (~4K tokens). Six models are shown: Llama-2-7b-chat-hf (blue solid), Llama-2-7b-hf (blue dashed), Llama-2-13b-chat-hf (orange solid), Llama-2-13b-hf (orange dashed), Llama-2-70b-chat-hf (green solid), and Llama-2-70b-hf (green dashed).

Key observations from the figure:
- Llama-2-70b-chat-hf achieves the highest overall accuracy (approximately 50-67%), with a clear U-shape: high at position 1 (~50%), dipping in the middle (~45%), and rising to the highest at position 20 (~67%).
- Llama-2-70b-hf shows a similar U-shaped pattern at slightly lower accuracy (~42-60%).
- Llama-2-13b-chat-hf shows a U-shape with accuracy ranging approximately 40-55%.
- Llama-2-13b-hf shows a dramatic U-shape with approximately 25-50% accuracy, with the largest gap (~20 points) between best and worst positions.
- Llama-2-7b-chat-hf is largely recency-biased, with accuracy rising from approximately 25% at position 1 to approximately 48% at position 20.
- Llama-2-7b-hf is solely recency-biased, with accuracy rising from approximately 20% at position 1 to approximately 40% at position 20, showing minimal primacy bias.
