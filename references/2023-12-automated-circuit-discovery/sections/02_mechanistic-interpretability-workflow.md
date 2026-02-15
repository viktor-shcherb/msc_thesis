# 2 The Mechanistic Interpretability Workflow [p. 2-4]

## 2.1 Step 1: Select behavior, dataset, and metric [p. 3]

[p. 3] The workflow begins by choosing a behavior/task, constructing prompts that elicit it, and selecting a scalar metric that tracks task performance.

**Table 1** (p. 4) summarizes six studied tasks:

| Task | Example behavior | Metric |
|---|---|---|
| IOI | Indirect object identification | Logit difference |
| Docstring | Variable-name completion in Python docstrings | Logit difference |
| Greater-Than | Year-comparison completion | Probability difference |
| tracr-xproportion | Proportion tracking in toy compiled transformer | Mean squared error |
| tracr-reverse | Sequence reversal in toy compiled transformer | Mean squared error |
| Induction | Repeated-pattern continuation | Negative log-probability |

## 2.2 Step 2: Choose computational graph granularity [p. 3]

[p. 3] Researchers define a DAG over model internals (e.g., heads/MLPs, Q/K/V components, neurons, position-split nodes). This graph choice determines what counts as a direct edge vs mediated pathway.

[p. 3] The paper notes graph construction is not unique; abstraction level affects both interpretability and compute cost.

## 2.3 Step 3: Activation patching to isolate the circuit [p. 4]

[p. 4] The iterative process is:
1. Corrupt a candidate node/edge activation.
2. Re-run forward pass.
3. Measure output degradation.
4. Remove edges/components with small effect.

[p. 4] The paper discusses ablation choices:
- **Zero ablation** (replace activation with zero).
- **Interchange/corrupted activation** (replace with activation from another datapoint).

The authors prefer corrupted activations for most experiments (closer to in-distribution activations), while still evaluating zero ablation variants.

## 2.4 Explaining circuit components [p. 4]

[p. 4] After subgraph isolation, researchers formulate mechanistic hypotheses for recovered components and test them with targeted interventions. The paper does not automate this stage.
