# Appendix K. ReST^EM Revision Model Experiments [p. 27]

[p. 27] The authors experimented with further optimizing their PaLM 2-S* revision model by training the model with a simplified RL algorithm: ReST^EM [35]. Specifically, they generated 64 revision trajectories of maximum length 5 for each question on the MATH training set. They stopped the revision model at the first correct answer in each trajectory. Using this generated data, they then finetuned the base LM on the correct answer data. To help the model learn the task, they explicitly balanced the distribution of trajectory lengths.

[p. 27] In Figure 16, they plot the performance of this new revision model as they vary the sequential to parallel ratio. They see that additional sequential revisions substantially hurts performance with this new model. They hypothesize that this degradation is due to the fact that the online data obtained from running ReST^EM exacerbates spurious correlations in revision data, causing the optimized model to fail to learn the revision task. They believe that using a more offline data collection strategy, as done in Qu et al. [28], may be more effective, and leave further exploration to future work.

**Figure 16** (p. 28): "Varying Sequential/Parallel"

Description: Line plot showing MATH Test Accuracy (%) vs Sequential/Parallel Ratio (log scale from 2^-5 to 2^2)

Plot details:
- X-axis: Sequential/Parallel Ratio (logarithmic scale: 2^-5, 2^-3, 2^-1, 2^1, 2^2)
- Y-axis (left): MATH Test Accuracy (%) ranging from 20 to 40
- Y-axis (right): Number of Generations (logarithmic scale: 10^0 to 10^2)
- Multiple colored lines representing different generation counts (orange ~10^0, red ~10^1, purple ~10^2)
- Performance peaks around 2^-3 to 2^-1 ratio (~38-39% accuracy)
- Performance degrades substantially at higher sequential ratios (2^1 and 2^2)
- At 2^2 ratio, accuracy drops to ~33-34%

Key findings:
- The ReST^EM optimized revision model demonstrates substantial performance degradations with additional sequential revisions
- Performance is best with more parallel samples and fewer sequential revisions
- This contrasts with the standard revision model behavior shown in earlier results
- The authors attribute this to spurious correlations in online revision data from ReST^EM
