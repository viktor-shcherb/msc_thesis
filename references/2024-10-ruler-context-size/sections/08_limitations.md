# Limitations [p. 10]

[p. 10] Despite covering more task categories than retrieval-oriented benchmarks, RULER is limited in multiple ways.

## Lack of position controlling

[p. 10] Current RULER reports a single number metric for each input length without providing the depth-level performance. The depth-level performance was evaluated by the NIAH test (Kamradt, 2023) and recent works such as LV-Eval (Yuan et al., 2024) and can be effective in revealing the lost-in-the-middle (Liu et al., 2024d) phenomenon. The authors are aware of this issue and plan to support position controlling of the key information in their codebase.

## Lack of correlation with realistic long-context tasks

[p. 10] While tasks such as *variable tracking* and *frequent words extraction* were proposed to serve as proxies for real long-context natural language tasks, the lack of easy-to-evaluate realistic long-context tasks prevents verification of the validity of these proxies. Due to this limitation, the authors emphasize that RULER can be used as convenient behavioral checks of long-context language models, however it should not be preferred over more realistic settings, such as NoCHA (Karpinska et al., 2024), which also emphasize other capabilities such as reasoning and instruction-following.

## Lack of evaluation on short context

[p. 10] In the current RULER task suite, tasks are included that most models perform reasonably well at 4K context size, aiming to observe performance degradation with the scaling of context size. This should not be misread as perfect LM capabilities at 4K context size. Recent works, such as FlenQA (Levy et al., 2024), have demonstrated degrading performance when increasing task input length to just a few thousand tokens. While increasing the task complexity in RULER leads to much worse performance at shorter context size, these results were not included in this paper.

## Lack of verification of prompt robustness

[p. 10] Language models can be sensitive to the prompt format; however the authors did not extend a comprehensive study on the prompt robustness beyond preliminary testing in the early stage of this work. The authors also did not heavily experiment with a few fixed hyperparameters in the existing tasks, such as the length of variable names in *variable tracking* and the synthetic vocabulary size in *common word extraction* and *frequent word extraction*.
