# Predictable Scaling [p. 2-4]

[p. 2] A large focus of the GPT-4 project was building a deep learning stack that scales predictably. For very large training runs like GPT-4, it is not feasible to do extensive model-specific tuning. The authors developed infrastructure and optimization methods with very predictable behavior across multiple scales. These improvements allowed reliably predicting some aspects of GPT-4's performance from smaller models trained using 1,000x - 10,000x less compute.

## Loss Prediction [p. 2-3]

[p. 2] The final loss of properly-trained large language models is thought to be well approximated by power laws in the amount of compute used to train the model [41, 42, 2, 14, 15].

To verify the scalability of their optimization infrastructure, the authors predicted GPT-4's final loss on their internal codebase (not part of the training set) by fitting a scaling law with an irreducible loss term (as in Henighan et al. [15]):

$$L(C) = aC^b + c$$

where $L(C)$ is the predicted final loss as a function of compute $C$, with parameters $a$, $b$, and $c$ (the irreducible loss term). Models were trained using the same methodology but using at most 10,000x less compute than GPT-4. The prediction was made shortly after the run started, without use of any partial results. The fitted scaling law predicted GPT-4's final loss with high accuracy (Figure 1). [p. 2]

**Figure 1** (p. 3): "Performance of GPT-4 and smaller models. The metric is final loss on a dataset derived from our internal codebase. This is a convenient, large dataset of code tokens which is not contained in the training set. We chose to look at loss because it tends to be less noisy than other measures across different amounts of training compute. A power law fit to the smaller models (excluding GPT-4) is shown as the dotted line; this fit accurately predicts GPT-4's final loss. The x-axis is training compute normalized so that GPT-4 is 1."

The figure shows a log-log plot of "Bits per word" (y-axis, ranging from ~1.0 to ~6.0) vs. "Compute" (x-axis, from 100p to 1, normalized so GPT-4 = 1). Gray dots represent observed performance of smaller models; a dashed gray line shows the power law fit; a green dot marks GPT-4's actual performance (~1.0 bits per word), which falls very close to the extrapolated prediction line.

## Scaling of Capabilities on HumanEval [p. 2-4]

[p. 2] In addition to predicting final loss, the authors developed methodology to predict more interpretable metrics of capability. One such metric is pass rate on the HumanEval dataset [43], which measures the ability to synthesize Python functions of varying complexity. They successfully predicted the pass rate on a subset of the HumanEval dataset by extrapolating from models trained with at most 1,000x less compute (Figure 2).

[p. 2-4] For an individual problem in HumanEval, performance may occasionally worsen with scale. Despite these challenges, they find an approximate power law relationship:

$$-\mathrm{E}_P[\log(\text{pass\_rate}(C))] = \alpha * C^{-k}$$

where $k$ and $\alpha$ are positive constants, and $P$ is a subset of problems in the dataset. The authors hypothesize that this relationship holds for all problems in the dataset. In practice, very low pass rates are difficult or impossible to estimate, so they restrict to problems $P$ and models $M$ such that given some large sample budget, every problem is solved at least once by every model. [p. 4]

[p. 4] Predictions for GPT-4's performance on HumanEval were registered before training completed, using only information available prior to training. All but the 15 hardest HumanEval problems were split into 6 difficulty buckets based on the performance of smaller models. The results on the 3rd easiest bucket are shown in Figure 2, showing that predictions were very accurate for this subset of HumanEval problems where they can accurately estimate log(pass_rate) for several smaller models. Predictions on the other five buckets performed almost as well, the main exception being GPT-4 underperforming their predictions on the easiest bucket.

[p. 4] Certain capabilities remain hard to predict. The Inverse Scaling Prize [44] proposed several tasks for which model performance decreases as a function of scale. Similarly to a recent result by Wei et al. [45], the authors find that GPT-4 reverses this trend, as shown on one of the tasks called Hindsight Neglect [46] in Figure 3.

**Figure 2** (p. 3): "Performance of GPT-4 and smaller models. The metric is mean log pass rate on a subset of the HumanEval dataset. A power law fit to the smaller models (excluding GPT-4) is shown as the dotted line; this fit accurately predicts GPT-4's performance. The x-axis is training compute normalized so that GPT-4 is 1."

The figure is titled "Capability prediction on 23 coding problems" and shows "- Mean Log Pass Rate" (y-axis, ranging from 0 to 5) vs. "Compute" (x-axis, from 1u to 1). Gray dots represent observed smaller model performance (decreasing from ~4 to ~1 as compute increases); a dashed gray line shows the power law fit; a green dot marks GPT-4's actual performance (near 0, close to the extrapolated prediction).

**Figure 3** (p. 4): "Performance of GPT-4 and smaller models on the Hindsight Neglect task. Accuracy is shown on the y-axis, higher is better. ada, babbage, and curie refer to models available via the OpenAI API [47]."

The figure is titled "Inverse scaling prize, hindsight neglect" and shows Accuracy (y-axis, 0 to 100) for five models on the x-axis: ada (~38), babbage (~20), curie (~18), gpt-3.5 (~20), gpt-4 (~95). The trend shows that performance is poor and roughly flat or declining from ada through gpt-3.5, then sharply increases for gpt-4.

[p. 4] The authors believe that accurately predicting future capabilities is important for safety. Going forward they plan to refine these methods and register performance predictions across various capabilities before large model training begins, and hope this becomes a common goal in the field.
