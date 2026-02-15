# Related Work [p. 3]

## Position Bias in LMs

Position bias widely exists in LMs (Zheng et al., 2024b,a; Wang et al., 2023; Zhu et al., 2023; Chen et al., 2024b; Liu et al., 2024; Shi et al., 2024) [p. 3].

The **LM-as-a-judge** task offers models two candidate responses to a question and asks models to select the more helpful one. It turns out that LM has a primacy bias that tends to favor the first response (Zheng et al., 2024b) [p. 3].

**Retrieval-augmented QA** asks LM to answer questions based on a set of retrieved documents. Liu et al. (2024); Peysakhovich & Lerer (2023) find that LMs are prone to answer correctly when the document that contains the correct answer is presented at the beginning or at the end of retrieved documents. Zheng et al. (2024a) points out that models favor options at certain positions (e.g., prefer "A") in multiple-choice QA [p. 3]. In the in-context learning task, Zhang et al. (2024a); Xu et al. (2024) find that the order of in-context examples affects the final performance [p. 3].

Recently, several papers have proposed to understand the nature of position bias through prompting (Zhang et al., 2024b) and calibration (Hsieh et al., 2024) [p. 3]. The paper analyzes the phenomenon from the mechanical perspective: the computation must be position-invariant to eliminate position bias [p. 3].

## Position Bias Solutions in LMs

**Mitigating** position bias have been studied widely from many aspects [p. 3]:

- **Data augmentation** (Junqing et al., 2023; Zhu et al., 2023)
- **Content sorting** by attention value during inference (Peysakhovich & Lerer, 2023)
- **Searching** (Yu et al., 2024; Adila et al., 2024)
- **Calibration** (Hsieh et al., 2024)
- **Removing position encoding** (Kazemnejad et al., 2024)

Moving one step forward, some other solutions are designed to **eliminate** position bias [p. 3]. Zheng et al. (2024a,b) use permutation and average outputs over different permuted input tasks, which will have unacceptable O(k!) (k is the number of segments) computational overhead when k is large [p. 3]. Hsieh et al. (2024) assumes that there are only a few relevant positions and retrieves items from linear combinations and propose solutions accordingly [p. 3].

Different from them, the authors aim to **eliminate** the position bias from the mechanical perspective without any assumption at a reasonable cost [p. 3]. While these approaches are from the mechanical perspective (Ratner et al., 2023; Cai et al., 2023; Hao et al., 2022), they only perform well in classification tasks and fail in a more general setting: language generation [p. 3].
