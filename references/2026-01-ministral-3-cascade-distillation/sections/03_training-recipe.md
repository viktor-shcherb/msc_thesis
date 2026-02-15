# Training Recipe [p. 2-6]

## Pipeline overview [p. 2-3]

### Figure 1 [p. 2]

**Figure 1** (p. 2): "Overview of Ministral 3 training recipe."

Description:
- A staged graph from parent model (Mistral Small 3.1) to child base models (14B, 8B, 3B), then to instruct and reasoning variants.
- Pretraining branch: pruning + short-context distillation + long-context distillation.
- Instruction branch: SFT -> ODPO.
- Reasoning branch: SFT (with CoT) -> GRPO -> ODPO.
- The same short-context checkpoint also seeds pruning for the next smaller child model.

Supports claim:
- Cascade Distillation is an iterative, multi-stage family-construction process rather than independent training runs per size [p. 2].

### Figure 2 [p. 3]

**Figure 2** (p. 3): "Illustration of Cascade Distillation."

Description:
- Diagram shows prune-distill-repeat loop.
- Highlights that pruning happens between distillation stages and model sizes.
- Supports the paper claim that data repetition is minimized in a single pass with pruning en route.

Supports claim:
- End-to-end training can be viewed as continual pretraining with progressive pruning [p. 3].

## 3.1 Pretraining [p. 3-4]

The pretraining loop starts from Mistral Small 3.1 (MS3.1) and iteratively produces 14B, then 8B, then 3B students.

### Algorithm 1: Cascade Distillation [p. 3]

```text
model = MS3  # Mistral Small 3.1
for model_size in [14B, 8B, 3B]:
    model = prune(model, model_size)
    model = train(data=short_data, teacher_model=MS3)
    final_model = train(data=long_data, teacher_model=MS3)
    yield(model_size, final_model)
```

### Pruning stage details [p. 4]

The paper lists three pruning components:

1. Layer pruning:
   - Uses mean ratio of activation norms as layer importance proxy:
   - `importance = mean(output_norm / input_norm)`
2. Hidden-dimension pruning:
   - PCA on concatenated normalization-layer activations to derive a rotation and lower-dimensional projection.
3. Feedforward-dimension pruning (SwiGLU):
   - MLP form: `W2(SiLU(W1 x) * W3 x)`
   - Dimension score based on averaged absolute activation products.

### Algorithm 2: Pruning stage of Cascade Distillation [p. 4]

```text
def prune(model, target_size):
    target_n_layers, target_dim, target_ffn_dim = get_config(target_size)

    # layer pruning
    for layer in model.layers:
        input_norm = layer.input_x.norm(dim=-1)
        output_norm = layer.output_x.norm(dim=-1)
        score = mean(output_norm / input_norm)
    keep top-k layers by score

    # hidden dimension pruning
    collect attn_norm.input_x and ffn_norm.input_x across layers
    rotation = PCA(norm_inputs, n_components=target_dim)
    apply rotation/projection

    # feedforward pruning
    importance = mean(abs(silu(w1.output_x) * w3.output_x), dim=(0,1))
    keep top-k FFN dims
```

### Distillation objective and stages [p. 4]

- Child models are trained with logit distillation from teacher logits.
- The paper states forward KL distillation alone outperformed weighted mixtures with next-token prediction.
- Two stages per child:
  1. Short-context stage: context length **16,384**
  2. Long-context stage: extend to **262,144** using YaRN + position-based temperature scaling [Peng et al., 2023; Nakanishi, 2025; MetaAI, 2025]

## 3.2 Post-Training: Ministral Instruct [p. 5]

### 3.2.1 Supervised Fine-Tuning [p. 5]

- Curated multimodal + text-only instruction data.
- FP8 quantized SFT.
- Distillation teacher differs from pretraining: Mistral Medium 3 (not MS3.1).
- Vision encoder frozen; adapter trainable.

### 3.2.2 ODPO [p. 5]

- Online DPO variant with two sampled candidates per example from current policy at **T = 0.7**.
- Pairwise Reward Model (PWRM) predicts preferred response.
- Uses probabilistic (binomial) preference outputs rather than hard winner/loser labels.
- Stabilization additions:
  1. PWRM temperature calibration
  2. beta-rescaling for DPO loss
- Heuristic mitigation for degeneracy:
  - infinite-loop responses are treated as loser candidates
- Tool execution is enabled during generation.

Paper claim in this subsection:
- Online preference optimization significantly improves alignment over SFT and offline preference optimization baselines [p. 5].

## 3.3 Post-Training: Ministral Reasoning [p. 5-6]

Reasoning models start from the pretrained checkpoint (not the instruct ODPO checkpoint) and apply three stages: **SFT -> GRPO -> ODPO**.

### 3.3.1 Reasoning SFT [p. 5-6]

- Mixture of short + long chain-of-thought traces.
- Long traces are prompted with reasoning-specific system instructions.
- Domains include math, coding, dialogue, instruction-following, multilingual tasks, tool use, visual reasoning.
- Lightweight filtering removes malformed, repetitive, or undesired language-switching examples.

**3B-specific note** [p. 6]:
- Vanilla SFT caused verbosity/repetition/infinite-generation issues.
- Logit distillation with Magistral Small 1.2 was applied to stabilize behavior before RL.

### 3.3.2 GRPO [p. 6]

Two RL stages:

1. STEM RL:
   - math, code, visual reasoning data
   - rigorous filtering to remove invalid/extreme samples
2. General RL:
   - broad prompts (chat/instruction/open-ended)
   - LLM judge scores rubric criteria; reward is fraction of satisfied heuristics

Training detail:
- Maximum generation length increased from **32K** to **80K** due to truncation during RL rollouts.

### 3.3.3 ODPO for reasoning [p. 6]

- Final post-RL alignment stage.
- Same ODPO setup as instruct models except:
  - reasoning "thinking chunks" are stripped before reward-model scoring.
