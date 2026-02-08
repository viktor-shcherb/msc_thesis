# Model Analysis Table [p. 29-36]

## Overview [p. 29]

The arguments above are based on analysis of 34 decoder-only Transformer language models, with different snapshots saved over the course of training, for one run of training per model. The models are drawn from four different model series as follows: [p. 29]

- **"Small, attention-only models"** -- a series of models (from 1-layer to 6-layer) that do not have MLPs, and were trained specifically for the present investigations. [p. 29]
- **"Small models with MLPs"** -- a series of models (from 1-layer to 6-layer) that have both attention and MLP layers, and were trained specifically for the present investigations. [p. 29]
- **"Full-scale models"** -- a series of successively-larger models with MLPs (ranging from 4 layers and 13M parameters, up to 40 layers and 13B parameters), that are used as the basis for multiple projects at Anthropic. [p. 29]
- **"Smeared key models"** -- a targeted architectural experiment designed to allow transformers of any depth to express induction heads. [p. 29]

## Dataset details [p. 29]

The dataset used for training the small models and smeared key models was an earlier version of the dataset described in Askell *et al.* [18], consisting of filtered common crawl data [19] and internet books, along with several other smaller distributions [20], including approximately 10% python code. The full-scale models were trained on an improved version of roughly the same data distribution. Additionally, another set of the small models was trained on a different dataset, consisting of just internet books, to explore the impact of varying the dataset. All models trained on a given dataset saw the same examples in the same order. Models never saw the same training data twice. [p. 29]

For more details on model architecture and training, continue past the table below, to the Model Details section. [p. 29]

In the Model Analysis Table below, each row includes a brief summary of the measurement shown. For a more in-depth explanation of the data collection and results analysis, see the Appendix. [p. 29]

## Small Attention-Only Transformers [p. 30-31]

This experiment series studies small *attention-only* transformers, because these are the models the authors have the strongest theoretical understanding of (see the framework paper). For these small models, they are able to capture snapshots with a high time resolution over early training. These experiments are the ones that most clearly demonstrate the phase change and link it to induction heads. [p. 30]

Key observations noted: (1) many models undergo a discontinuous phase change (seen most clearly in the PCA plot and in-context learning score); (2) it appears to be caused by induction heads (see ablations); and (3) the only model without a phase change is the one-layer model. [p. 30]

The table presents results across six model configurations: **One Layer**, **Two Layer**, **Three Layer**, **Four Layer**, **Five Layer**, and **Six Layer** (all attention-only). [p. 30-31]

### Models Over Training [p. 30]

**Row 1: PCA of Token Losses** [p. 30]

The vector of per-token losses is a way to map different neural network behavior to the same vector space. The authors take 10,000 individual token predictions per model, and project them onto the first two principal components. This shows how the large-scale-behavior of multiple networks evolve over training.

For models with 2+ layers, the PCA plots show a discontinuous trajectory (a sharp turn) corresponding to the phase change. The one-layer model shows a smooth trajectory.

**Row 2: Loss Over Training** [p. 30]

Loss curve showing $\text{Loss}(n_{\text{train}})$ after the model is trained on $n_{\text{train}}$ tokens of training data. The orange band denotes the phase change interval. All models with 2+ layers show a visible bump or plateau in the loss curve during the phase change.

**Row 3: Loss Over Training, Broken Down by Context Index** [p. 30]

Heatmap of $\text{Loss}(n_{\text{train}}, i_{\text{ctx}})$, the average loss of $i_{\text{ctx}}$ token in context after $n_{\text{train}}$ elapsed tokens of training. This 2D visualization (x-axis: training tokens; y-axis: context index) shows a sharp transition where later-context tokens (higher $i_{\text{ctx}}$) suddenly improve in loss during the phase change. The color scale runs from approximately 5.5 (high loss) to 4.0 (low loss).

**Row 4: Derivative of Loss WRT Context Index** [p. 30]

Heatmap of $d\text{Loss}(n_{\text{train}}, i_{\text{ctx}}) / d\ln(i_{\text{ctx}})$. The log vertical partial derivative of the above graph. The color scale runs from 0.3 (red, left) through 0.0 to -0.2 (blue, right), where blue indicates "loss decreases with longer context". For 2+ layer models, a sharp transition to blue (loss decreasing with context) occurs during the phase change.

**Row 5: "In-Context Learning Score"** [p. 30]

Defined as $\text{Loss}(n_{\text{train}}, i_{\text{ctx}} = 500) - \text{Loss}(n_{\text{train}}, i_{\text{ctx}} = 50)$. This measures how much better the model is at predicting the 500th token than the 50th token, used as a proxy for how good the model is at in-context learning. For 2+ layer models, there is a sharp drop (improvement) in this score during the phase change.

### Attention Heads Over Training [p. 31]

**Row 6: "Prefix Matching Score"** [p. 31]

Each line is an attention head. Y axis is the average fraction of a head's attention weight given to the token the authors expect an induction head to attend to -- the token where the prefix matches the present context -- on random, synthetic data. Heads are colored by layer depth: early (red/orange), late (blue). For 2+ layer models, late-layer heads show a sharp increase in prefix matching score during the phase change.

**Row 7: Trace of QK Eigenvalues** [p. 31]

Each line is an attention head. Y axis is the trace of the $W$ in the attention head's $\text{Id} \otimes h_{prev} \otimes W$ QK circuit term, scaled by how well $h_{prev}$ matches an ideal previous token head. Only defined for models more than one layer deep. Heads are colored by layer depth: early (red/orange), late (blue). The one-layer model shows "N/A". For 2+ layer models, late-layer heads show increasing QK eigenvalue traces coinciding with induction head formation.

**Row 8: Ablation to "Before-and-After" Vector** [p. 31]

Each line is an attention head. Y axis is the projection of the observed per-token loss differences when ablating an attention head onto the difference in per-token losses before and after the bump. The one-layer model shows "N/A". Heads are colored by type: previous token (red/pink), induction (purple/blue), other (yellow/gold). Induction heads show the largest positive projection, indicating they are most responsible for the per-token loss change during the phase change.

**Row 9: Ablation Attribution to "In-Context Learning Score"** [p. 31]

Each line is an attention head. Y axis is the change in the "in-context learning score" observed when ablating each attention head. Heads are colored by type: previous token (red/pink), induction (purple/blue), other (yellow/gold). Induction heads (purple/blue lines) show the largest negative attribution (i.e., ablating them causes the biggest increase in the in-context learning score, meaning the biggest loss of in-context learning ability). This is consistent across all model depths from 2 to 6 layers.

---
[p. 32-33 continued]

## Small Transformers (with MLPs) [p. 32-33]

This experiment series studies small normal transformers (with MLP layers, unlike the attention-only models above). For these small models, the authors are able to capture snapshots with a high time resolution over early training. The main observation to take away is that the results are essentially the same as the attention-only models (where the authors have a stronger theoretical understanding). [p. 32]

The table presents results across six model configurations: **One Layer (with MLPs)**, **Two Layer (with MLPs)**, **Three Layer (with MLPs)**, **Four Layer (with MLPs)**, **Five Layer (with MLPs)**, and **Six Layer (with MLPs)**. [p. 32-33]

### Models Over Training [p. 32]

**Row 1: PCA of Token Losses** [p. 32]

The vector of per-token losses is a way to map different neural network behavior to the same vector space. The authors take 10,000 individual token predictions per model, and project them onto the first two principal components. This shows how the large-scale-behavior of multiple networks evolve over training.

For models with 2+ layers, the PCA plots show a discontinuous trajectory (a sharp turn) corresponding to the phase change, similar to the attention-only case. The one-layer model shows a smooth trajectory. The two-layer model's trajectory is somewhat less sharply discontinuous than in the attention-only case but still visible.

**Row 2: Loss Over Training** [p. 32]

Loss curve showing $\text{Loss}(n_{\text{train}})$ after the model is trained on $n_{\text{train}}$ tokens of training data. The orange band denotes the phase change interval. All models with 2+ layers show a visible bump or plateau in the loss curve during the phase change, similar to the attention-only case.

**Row 3: Loss Over Training, Broken Down by Context Index** [p. 32]

Heatmap of $\text{Loss}(n_{\text{train}}, i_{\text{ctx}})$, the average loss of $i_{\text{ctx}}$ token in context after $n_{\text{train}}$ elapsed tokens of training. As with the attention-only models, a sharp transition is visible where later-context tokens suddenly improve in loss during the phase change for 2+ layer models. The color scale runs from approximately 5.5 (high loss) to 4.0 (low loss).

**Row 4: Derivative of Loss WRT Context Index** [p. 32]

Heatmap of $d\text{Loss}(n_{\text{train}}, i_{\text{ctx}}) / d\ln(i_{\text{ctx}})$. The log vertical partial derivative of the above graph. The color scale runs from 0.3 (red) through 0.0 to -0.3 (blue), where blue indicates "loss decreases with longer context". For 2+ layer models, a sharp transition to blue occurs during the phase change, consistent with the attention-only results.

**Row 5: "In-Context Learning Score"** [p. 32]

Defined as $\text{Loss}(n_{\text{train}}, i_{\text{ctx}} = 500) - \text{Loss}(n_{\text{train}}, i_{\text{ctx}} = 50)$. This measures how much better the model is at predicting the 500th token than the 50th. For 2+ layer models, there is a sharp drop (improvement) in this score during the phase change. The pattern is essentially the same as for the attention-only models.

### Attention Heads Over Training [p. 33]

**Row 6: "Prefix Matching Score"** [p. 33]

Each line is an attention head. Y axis is the average fraction of a head's attention weight given to the token the authors expect an induction head to attend to -- the token where the prefix matches the present context -- on random, synthetic data. Heads are colored by layer depth: early (red/orange), late (blue). For 2+ layer models, late-layer heads show a sharp increase in prefix matching score during the phase change, consistent with the attention-only results.

**Row 7: Trace of QK Eigenvalues** [p. 33]

Each line is an attention head. Y axis is the trace of the $W$ in the attention head's $\text{Id} \otimes h_{prev} \otimes W$ QK circuit term, scaled by how well $h_{prev}$ matches an ideal previous token head. Only defined for models more than one layer deep. The one-layer model shows "N/A". Heads are colored by layer depth: early (red/orange), late (blue). For 2+ layer models, late-layer heads show increasing QK eigenvalue traces coinciding with induction head formation.

**Row 8: Ablation to "Before-and-After" Vector** [p. 33]

Each line is an attention head. Y axis is the projection of the observed per-token loss differences when ablating an attention head onto the difference in per-token losses before and after the bump. The one-layer model shows "N/A". Heads are colored by type: previous token (red/pink), induction (purple/blue), other (yellow/gold). Induction heads show the largest positive projection, indicating they are most responsible for the per-token loss change during the phase change.

**Row 9: Ablation Attribution to "In-Context Learning Score"** [p. 33]

Each line is an attention head. Y axis is the change in the "in-context learning score" observed when ablating each attention head. Heads are colored by type: previous token (red/pink), induction (purple/blue), other (yellow/gold). Induction heads (purple/blue lines) show the largest negative attribution, consistent across all model depths from 2 to 6 layers, mirroring the attention-only results.

---
[p. 34-36 continued]

## Full-Scale Transformers [p. 34-36]

This experiment series analyzes a sweep of typical transformers, spaced exponentially in size, up to a 13 billion parameter model. The goal is to show that the phenomena observed in small models can be seen in larger models as well. For these models, the authors unfortunately have lower time resolution (note that the x-axis of most plots has changed to a log scale). They are also unable to provide complete ablations. The main observation to make is that results are roughly the same as seen in the small models. [p. 34]

The table presents results across six model configurations [p. 34]:

| Configuration | Layers | Parameters |
|---|---|---|
| 4-Layer Transformer | 4 | 13M |
| 6-Layer Transformer | 6 | 42M |
| 10-Layer Transformer | 10 | 200M |
| 16-Layer Transformer | 16 | 810M |
| 24-Layer Transformer | 24 | 2.7B |
| 40-Layer Transformer | 40 | 13B |

### Models Over Training [p. 34]

**Row 1: PCA of Token Losses** [p. 34]

The vector of per-token losses is a way to map different neural network behavior to the same vector space. The authors take 10,000 individual token predictions per model, and project them onto the first two principal components. This shows how the large-scale-behavior of multiple networks evolve over training.

All six models show a discontinuous trajectory (a sharp turn) corresponding to the phase change. The turn is visible at all scales from 13M to 13B parameters.

**Row 2: Loss Over Training** [p. 34]

Loss curve showing $\text{Loss}(n_{\text{train}})$ after the model is trained on $n_{\text{train}}$ tokens of training data. The orange band denotes the phase change interval. Note the x-axis is now on a log scale (Elapsed Training Tokens (log)). All models show a visible bump in the loss curve during the phase change.

**Row 3: Loss Over Training, Broken Down by Context Index** [p. 34]

Heatmap of $\text{Loss}(n_{\text{train}}, i_{\text{ctx}})$, the average loss of $i_{\text{ctx}}$ token in context after $n_{\text{train}}$ elapsed tokens of training. The x-axis is on a log scale. A sharp transition is visible in all models where later-context tokens suddenly improve in loss. The color scale runs from approximately 5.5 (high loss, yellow/green) to 4.0 (low loss, dark purple). The gradient from high to low loss is sharper and more pronounced in the larger models.

**Row 4: Derivative of Loss WRT Context Index** [p. 34]

Heatmap of $d\text{Loss}(n_{\text{train}}, i_{\text{ctx}}) / d\ln(i_{\text{ctx}})$. The log vertical partial derivative of the above graph. The x-axis is on a log scale. The color scale runs from 0.3 (red) through 0.0 to -0.3 (blue), where blue indicates "loss decreases with longer context". All models show a transition to blue during the phase change, with larger models achieving more strongly blue regions (stronger in-context learning).

**Row 5: "In-Context Learning Score"** [p. 34]

Defined as $\text{Loss}(n_{\text{train}}, i_{\text{ctx}} = 500) - \text{Loss}(n_{\text{train}}, i_{\text{ctx}} = 50)$. For all models, there is a sharp drop in this score during the phase change. The final in-context learning scores become progressively more negative (stronger) as model size increases.

### Attention Heads Over Training [p. 35-36]

**Row 6: "Prefix Matching Score"** [p. 35-36]

Each line is an attention head. Y axis is the average fraction of a head's attention weight given to the token the authors expect an induction head to attend to -- the token where the prefix matches the present context -- on random, synthetic data. Heads are colored by layer depth: early (red/orange), late (blue). The x-axis is on a log scale. [p. 35-36]

For the smaller full-scale models (4-layer, 6-layer), a few heads show a sharp increase in prefix matching score (reaching close to 1.0) during the phase change. For larger models (10-layer, 16-layer, 24-layer, 40-layer), more heads show elevated prefix matching scores, but the trajectories are more gradual and spread out across many heads, with many heads achieving moderate scores (0.2-0.8) rather than a few heads reaching near 1.0. In the largest models, the lines are dense and numerous, with early-layer heads (red/orange) tending to have lower scores and later-layer heads (blue/purple) showing higher and more variable scores. [p. 35-36]

---
[p. 36 continued]

## "Smeared Key" Architecture Modification + Controls [p. 36]

This experiment series analyzes "smeared key" models, which are designed so that a single attention layer can implement induction heads (see Argument 2). For each smeared key model, a regular control model is provided (trained exactly the same) for comparison. The key observations are that (1) a one-layer smeared-key model experiences the phase change, while a regular one-layer model does not; and (2) the two-layer smeared-key model experiences a phase change earlier than a baseline model. [p. 36]

The table presents results across four model configurations: **One Layer (Vanilla)**, **One Layer (Smeared Keys)**, **Two Layer (Vanilla)**, and **Two Layer (Smeared Keys)**. [p. 36]

### Models Over Training [p. 36]

**Row 1: Loss Over Training** [p. 36]

Loss curve showing $\text{Loss}(n_{\text{train}})$ after the model is trained on $n_{\text{train}}$ tokens of training data. The orange band denotes the phase change interval. The one-layer vanilla model shows a smooth decreasing loss with no phase change bump. The one-layer smeared keys model shows a visible phase change bump. The two-layer vanilla model shows a phase change bump. The two-layer smeared keys model also shows a phase change bump, occurring earlier than in the vanilla two-layer model.

**Row 2: Loss Over Training, Broken Down by Context Index** [p. 36]

Heatmap of $\text{Loss}(n_{\text{train}}, i_{\text{ctx}})$, the average loss of $i_{\text{ctx}}$ token in context after $n_{\text{train}}$ elapsed tokens of training. The one-layer vanilla model shows a gradual, smooth gradient without a sharp transition. The one-layer smeared keys model shows a sharp transition where later-context tokens suddenly improve. The two-layer vanilla model shows the typical sharp transition during the phase change. The two-layer smeared keys model shows the sharp transition occurring earlier.

**Row 3: Derivative of Loss WRT Context Index** [p. 36]

Heatmap of $d\text{Loss}(n_{\text{train}}, i_{\text{ctx}}) / d\ln(i_{\text{ctx}})$. The log vertical partial derivative. The color scale runs from 0.3 (red) through 0.0 to -0.3 (blue). The one-layer vanilla model shows minimal blue regions (weak in-context learning). The one-layer smeared keys model shows a sharp transition to blue, indicating strong in-context learning onset. Both two-layer models show blue regions, but the smeared keys version transitions earlier.

**Row 4: "In-Context Learning Score"** [p. 36]

Defined as $\text{Loss}(n_{\text{train}}, i_{\text{ctx}} = 500) - \text{Loss}(n_{\text{train}}, i_{\text{ctx}} = 50)$. The one-layer vanilla model's score stays near zero (no in-context learning improvement). The one-layer smeared keys model shows a sharp drop during the phase change. The two-layer vanilla model shows the typical sharp drop. The two-layer smeared keys model shows the drop occurring earlier than in the vanilla two-layer model.

---
[p. 37 continued]

## Small Attention-Only Transformers (Different Dataset) [p. 37]

This experiment series studies transformers of the same architecture as the small *attention-only* transformers, on a different dataset consisting only of internet books. [p. 37]

The table presents results across six model configurations: **One Layer (Attention-Only)**, **Two Layer (Attention-Only)**, **Three Layer (Attention-Only)**, **Four Layer (Attention-Only)**, **Five Layer (Attention-Only)**, and **Six Layer (Attention-Only)**. [p. 37]

### Models Over Training [p. 37]

**Row 1: Loss Over Training** [p. 37]

Loss curve showing $\text{Loss}(n_{\text{train}})$ after the model is trained on $n_{\text{train}}$ tokens of training data. The orange band denotes the phase change interval. All models with 2+ layers show a visible bump or plateau in the loss curve during the phase change, consistent with the results on the original dataset.

**Row 2: Loss Over Training, Broken Down by Context Index** [p. 37]

Heatmap of $\text{Loss}(n_{\text{train}}, i_{\text{ctx}})$, the average loss of $i_{\text{ctx}}$ token in context after $n_{\text{train}}$ elapsed tokens of training. The color scale runs from approximately 5.5 (high loss) to 4.0 (low loss). A sharp transition is visible for 2+ layer models where later-context tokens suddenly improve in loss during the phase change, consistent with the original dataset results.

**Row 3: Derivative of Loss WRT Context Index** [p. 37]

Heatmap of $d\text{Loss}(n_{\text{train}}, i_{\text{ctx}}) / d\ln(i_{\text{ctx}})$. The log vertical partial derivative. The color scale runs from 0.3 (red) through 0.0 to -0.3 (blue), where blue indicates "loss decreases with longer context". For 2+ layer models, a sharp transition to blue occurs during the phase change. Results are consistent with the original dataset.

**Row 4: "In-Context Learning Score"** [p. 37]

Defined as $\text{Loss}(n_{\text{train}}, i_{\text{ctx}} = 500) - \text{Loss}(n_{\text{train}}, i_{\text{ctx}} = 50)$. For 2+ layer models, there is a sharp drop (improvement) in this score during the phase change. The one-layer model shows no such improvement. Results replicate the findings on the original dataset with a different data distribution.

---
[p. 38 continued]

## Small Transformers (with MLPs) (Different Dataset) [p. 38]

This experiment series studies small normal transformers (with MLP layers), on a different dataset consisting only of internet books. [p. 38]

The table presents results across six model configurations: **One Layer (with MLPs)**, **Two Layer (with MLPs)**, **Three Layer (with MLPs)**, **Four Layer (with MLPs)**, **Five Layer (with MLPs)**, and **Six Layer (with MLPs)**. [p. 38]

### Models Over Training [p. 38]

**Row 1: Loss Over Training** [p. 38]

Loss curve showing $\text{Loss}(n_{\text{train}})$ after the model is trained on $n_{\text{train}}$ tokens of training data. The orange band denotes the phase change interval. All models with 2+ layers show a visible bump or plateau in the loss curve during the phase change. The one-layer model shows a smooth decrease without a phase change.

**Row 2: Loss Over Training, Broken Down by Context Index** [p. 38]

Heatmap of $\text{Loss}(n_{\text{train}}, i_{\text{ctx}})$, the average loss of $i_{\text{ctx}}$ token in context after $n_{\text{train}}$ elapsed tokens of training. The color scale runs from approximately 5.5 (high loss) to 4.0 (low loss). A sharp transition is visible for 2+ layer models, consistent with the original dataset results.

**Row 3: Derivative of Loss WRT Context Index** [p. 38]

Heatmap of $d\text{Loss}(n_{\text{train}}, i_{\text{ctx}}) / d\ln(i_{\text{ctx}})$. The log vertical partial derivative. The color scale runs from 0.3 (red) through 0.0 to -0.3 (blue), where blue indicates "loss decreases with longer context". For 2+ layer models, a sharp transition to blue occurs during the phase change.

**Row 4: "In-Context Learning Score"** [p. 38]

Defined as $\text{Loss}(n_{\text{train}}, i_{\text{ctx}} = 500) - \text{Loss}(n_{\text{train}}, i_{\text{ctx}} = 50)$. For 2+ layer models, there is a sharp drop (improvement) in this score during the phase change. Results replicate the findings from the original dataset, demonstrating that the phase change phenomena are robust across different data distributions.
