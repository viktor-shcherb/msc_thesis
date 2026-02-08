# 7. Advancing Mathematical Reasoning [p. 43–44]

[p. 43] In training Gemini 1.5 Pro, the authors want to understand how far they can push the quantitative reasoning capabilities of LLMs, with the goal of solving increasingly challenging and open-ended problems. Solving such problems typically requires extensive domain-specific study. In addition, mathematicians often benefit from extended periods of contemplation while formulating solutions; written mathematics tends to focus on the final result, obscuring the rich thought processes that precede it (see, for example, the panel discussion (MATH-AI-2023-Panel, 2023)). The authors aim to emulate this by training a math-specialized model and providing it additional inference time computation, allowing it to explore a wider range of possibilities.

## Evaluation Benchmarks

[p. 43] To test the capabilities of this model, the authors use competition-derived evaluation benchmarks: MATH (Hendrycks et al., 2021b), the American Invitational Mathematics Examination (AIME) 2024 (MAA, 2024), MathOdyssey (Fang et al., 2024), and internally developed evaluations HiddenMath (see Section 6.1.1), which contains unique problems held-out from their training sets, and IMO-Bench, an internally developed expert graded evaluation testing math capabilities at the International Math Olympiad level.

## Results

[p. 43] Results are shown in Table 21. The authors find that this approach advances state-of-the-art performance consistently across all mathematical benchmarks. The math-specialized model achieves an accuracy of 80.6% on the MATH benchmark from a single sample, and an accuracy of 91.1% when sampling 256 solutions and selecting a candidate answer (rm@256). This performance is achieved without code execution, theorem proving libraries, Google Search or other tools. This performance is on par with a human-expert performance (Hendrycks et al., 2021b). The math-specialized Gemini 1.5 Pro demonstrates generally improved mathematical performance beyond MATH, solving 4x more problems from AIME, and demonstrates significant improvement in Math Odyssey, HiddenMath and IMO-Bench.

## Table 21

**Table 21** (p. 43): Performance on mathematical reasoning benchmarks. All numbers, unless explicitly stated, are obtained with a single greedy decoding.

| Benchmark | Gemini 1.5 Pro | Math-Specialized 1.5 Pro^28 | Claude 3 Opus | GPT-4 Turbo |
|---|---|---|---|---|
| **MATH** | 67.7 | **80.6** / 91.1 rm@256 | 60.1 | 73.4 |
| **AIME 2024** | 2/30 | **7/30** / 8/30 rm@256 | 2/30 | 1/30 |
| **Math Odyssey** | 45.0 | **55.8** | 40.6 | 49.1 |
| **HiddenMath** | 20.1 | **35.2** | 17.3 | 24.6 |
| **IMO-Bench** | 15.0 | **25.0** | - | 18.0 |

## Example: APMO Problem

[p. 43–44] The authors provide an example of the model solving an Asian Pacific Mathematical Olympiad (APMO) problem that Gemini 1.5 Pro, GPT-4 Turbo, and all previous Gemini models answer incorrectly. Interestingly, the model adopts a different route than the official solution.^29

**Problem:** Let *a*, *b*, *c* be positive integers. Prove that it is impossible to have all of the three numbers *a*^2 + *b* + *c*, *b*^2 + *c* + *a*, *c*^2 + *a* + *b* to be perfect squares. [p. 44]

**Example Math-Specialized Gemini 1.5 Pro output:** Without loss of generality, assume *a* >= *b* >= *c*. Then *a*^2 + *b* + *c* <= *a*^2 + 2*a* < *a*^2 + 2*a* + 1 = (*a* + 1)^2. Since *a*^2 + *b* + *c* is a perfect square, we must have *a*^2 + *b* + *c* = *a*^2, which implies *b* + *c* = 0. This is a contradiction since *b* and *c* are positive integers. Therefore, it is impossible to have all of the three numbers *a*^2 + *b* + *c*, *b*^2 + *c* + *a*, *c*^2 + *a* + *b* to be perfect squares. [p. 44]

**Example Gemini 1.5 Pro output (Incorrect):** Assume, for the sake of contradiction, that all three numbers *a*^2 + *b* + *c*, *b*^2 + *c* + *a*, and *c*^2 + *a* + *b* are perfect squares. Without loss of generality, let's assume *a* >= *b* >= *c*. Now, consider the difference between the first two expressions: (*a*^2 + *b* + *c*) - (*b*^2 + *c* + *a*) = *a*^2 - *b*^2 + *b* - *a* = (*a* - *b*)(*a* + *b*) - (*a* - *b*) = (*a* - *b*)(*a* + *b* - 1). Since *a* >= *b*, the term (*a* - *b*) is non-negative. Additionally, both *a* and *b* are positive integers, so (*a* + *b* - 1) must be positive. Therefore, the entire expression (*a* - *b*)(*a* + *b* - 1) is non-negative. However, we assumed that both *a*^2 + *b* + *c* and *b*^2 + *c* + *a* are perfect squares. This means their difference must also be a perfect square. The only non-negative perfect square that can be expressed as the product of two positive integers where one is smaller than the other (as in (*a* - *b*) and (*a* + *b* - 1)) is 0. [The text in red in the PDF indicates this reasoning step is incorrect.] [p. 44]

## Example: AIMO Problem

[p. 44] The authors present another example from the Artificial Intelligence Mathematical Olympiad.

**Problem:** What is the minimum value of 5*x*^2 + 5*y*^2 - 8*xy* when *x* and *y* range over all real numbers such that |*x* - 2*y*| + |*y* - 2*x*| = 40? [p. 44]

**Example Math-Specialized Gemini 1.5 Pro output:** Let *a* = *x* - 2*y* and *b* = *y* - 2*x*. Then, we have |*a*| + |*b*| = 40. Also, 5*x*^2 + 5*y*^2 - 8*xy* = (*x* - 2*y*)^2 + (*y* - 2*x*)^2 = *a*^2 + *b*^2. Thus, we want to find the minimum value of *a*^2 + *b*^2 given that |*a*| + |*b*| = 40. By the Trivial Inequality, we have (|*a*| - 20)^2 + (|*b*| - 20)^2 >= 0, so *a*^2 - 40|*a*| + 400 + *b*^2 - 40|*b*| + 400 >= 0, so *a*^2 + *b*^2 >= 40(|*a*| + |*b*|) - 800 = 40(40) - 800 = 800. This minimum is achieved when |*a*| = |*b*| = 20, so the minimum value of 5*x*^2 + 5*y*^2 - 8*xy* is **800**. [p. 44]

[p. 44] Currently the math-specialized model is only being explored for Google internal research use cases; the authors hope to bring these stronger math capabilities into their deployed models soon.

> ^28 Footnote 28 is not visible on the pages in this window; it likely appears on an earlier page defining the Math-Specialized 1.5 Pro configuration.

> ^29 https://www.apmo-official.org/static/solutions/apmo2011_sol.pdf [p. 43]
