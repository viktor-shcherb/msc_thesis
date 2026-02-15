# 3 Basic Properties of Retrieval Heads [p. 5–6] (continued)

---
[p. 5 continued]

**Figure 4** (p. 5): "Retrieval score (blue): average number of activated tokens; Activation Frequency (green): frequency of at least activated on one token. The *gap* between the two curves shows *context-sensitivity*: a head of high activation frequency but low retrieval score means it is only activated on certain tokens and contexts; a head of high retrieval score means it is activated on almost any context. For both LLaMA and Yi, there exist strong heads that are not sensitive to context and always activated."

Description: Two-panel line graph with embedded bar charts showing retrieval patterns.
- Left panel (Llama-2-7B-80K): Green line shows activation frequency across layers (peaks at ~1.0 near Layer 0, drops to ~0.0 around Layer 15, rises slightly at Layer 32); blue area shows retrieval score (mostly near 0.0); embedded bar chart shows declining retrieval scores from layers 24-32
- Right panel (Yi-6B-200K): Similar pattern with green line peaking early and declining; embedded bar chart shows retrieval scores for layers
- Key elements: X-axis shows Layer-Head Id, left Y-axis shows retrieval patterns, embedded charts show layer-specific retrieval scores
- Notable patterns: Strong gap between activation frequency and retrieval score indicates context-sensitivity; certain layers show consistently high retrieval scores
- Supports claim: Some heads have high activation frequency but low retrieval score (context-sensitive), while others have high retrieval scores (always activated)

**Figure 5** (p. 5): "Retrieval head is intrinsic and already within the base model. The subsequent model derivations, either by continue pretraining (LLaMA 2 7B 80K) or chat finetuning (Qwen 1.5 14B Chat) or sparse upcycling (Mixtral 8×7B), use the same set of retrieval head as the base model, as demonstrated by a high level of similarity between the heatmap patterns."

Description: Six heatmaps showing retrieval head patterns across model variants.
- Key elements: Heatmaps for Llama-2-7B, Qwen1.5-14B, Mistral-7B-v0.2 (top row) and their variants Llama-2-7B-80K, Qwen1.5-14B-Chat, Mistral-8x7B-v0.1 (bottom row); X-axis shows Layer ID (0-32), Y-axis shows Head ID; color scale from 0.0 (light) to 0.5+ (red)
- Notable patterns: Similar activation patterns visible between base models and their variants, with red hotspots appearing in similar locations across corresponding pairs
- Supports claim: Base models and their fine-tuned/extended variants use the same set of retrieval heads

## 3.2 Dynamically Activated Based on Tokens and Contexts [p. 5]

Now the authors study how sensitive a retrieval head is to its input context, i.e., whether a head is consistently activated no matter what the context is, or if a head is activated only on specific contexts. For the needle sentences "the best thing to do in San Francisco is to eat a sandwich in Dolores park in a sunny day", some heads are activated on the full sentence, whereas other heads only activated on certain tokens like "eating a sandwich" or "in Dolores park". The authors define *activation frequency*, the frequency of a head being activated on *at least one* token. In contrast, retrieval score measures the *average* number of activated tokens). A head of high activation frequency but low retrieval score means it is only activated on certain tokens and contexts. As demonstrated in Fig. 4, Llama-2-7B-80K and Yi-6B-200K have 12 and 36 strongest retrieval heads, respectively, that are always activated (activation frequency equal to 1) under all the contexts the authors consider. Weaker heads only activate on certain tokens and contexts.

## 3.3 Intrinsic [p. 5–6]

The authors show that the retrieval heads, thus the ability of utilizing information at arbitrary location of the input, is an intrinsic property [6] of the base model as a consequence of large-scale pretraining, with subsequent small-scale training exerting only minor alterations to these head activation patterns. In Figure 5, the authors present the retrieval score distributions for a range of base models in the initial row, followed by their corresponding variants in the subsequent row. The authors see that regardless of the models
