# 4. Experimental Setup [p. 6]

[p. 6] The authors outline their experimental setup for conducting the analysis with multiple verifier design choices and proposal distributions, followed by the analysis results in subsequent sections.

## Datasets

[p. 6] Test-time compute is expected to be most helpful when models already have all the basic "knowledge" needed to answer a question, and instead the primary challenge is about drawing (complex) inferences from this knowledge. The authors focus on the **MATH** [13] benchmark, which consists of high-school competition level math problems with a range of difficulty levels. For all experiments, they use the dataset split consisting of **12k train** and **500 test questions**, used in Lightman et al. [22].

## Models

[p. 6] The analysis is conducted using the **PaLM 2-S*** [3] **(Codey)** base model. The authors believe this model is representative of the capabilities of many contemporary LLMs, and therefore think that their findings likely transfer to similar models. Most importantly, this model attains a non-trivial performance on MATH and yet has not saturated, so it is expected to provide a good test-bed.
