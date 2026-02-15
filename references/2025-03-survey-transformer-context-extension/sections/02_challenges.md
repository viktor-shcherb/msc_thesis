# 2 Challenges [p. 2–3]

When applying pre-trained LLMs to the long context scenarios, there are some inherent challenges affecting models' performance. We list the three most important and common challenges: OOD problem, "Lost in the Middle" phenomenon, and quadratic complexity [p. 2].

## OOD Problem

When processing sequences that exceed the pre-trained context length, the models face out-of-distribution (OOD) problems [p. 2].

Han et al. (2024) verify theoretically and empirically that three key factors contribute to OOD issues, thereby limiting models' extrapolation capabilities:
1. Unseen inter-token distances
2. Increased number of attended tokens
3. Implicitly encoded position information of the starting tokens [p. 2]

## "Lost in the Middle" Phenomenon

Liu et al. (2024a) discover the "Lost in the middle" phenomenon through experiments that when LLMs receive a long input, they tend to focus on information at both the beginning and end of the input sequence. At the same time, they neglect the content in the middle, thus failing to capture all key information within the long input [p. 2–3].

## Quadratic Complexity

Due to the quadratic complexity of attention, directly using pre-trained LLMs for training or inference can become prohibitively time and resource consuming (Zhou et al., 2024) [p. 3].

## Importance for Method Development

The above are three inherent challenges in the field of long context, and some existing methods have alleviated them to a certain extent. But it is worth noting that most of the methods do not start from this perspective. They consider directly improving the performance of downstream tasks. However, we believe that these three challenges are still the fundamental problems that need to be solved. They play a vital role in the design of methods and construction of benchmarks. Moreover, they are the focus of subsequent research [p. 3].
