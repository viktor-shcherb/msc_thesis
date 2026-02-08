# 12. Appendix [p. 105–127]

## 12.1. Model Card

[p. 105] The Gemini 1.5 Model card is presented in Table 45.

**Table 45:** Gemini 1.5 Model Card [p. 105-107]

### Model Summary

| Field | Details |
|---|---|
| **Model architecture** | Gemini 1.5 Pro is a sparse mixture-of-expert (MoE) Transformer based model that builds on scaling MoE vision/language models at Google (Clark et al., 2020; Fedus et al., 2021; Lepikhin et al., 2020; Riquelme et al., 2021; Shazeer et al., 2017; Zoph et al., 2022). Gemini 1.5 Flash is a dense Transformer based model that is online distilled (Agarwal et al., 2024b; Anil et al., 2018; Beyer et al., 2021; Bucila et al., 2006; Hinton et al., 2015) from Gemini 1.5 Pro. |
| **Input(s)** | Text string (e.g., a question, a prompt, a document(s) to be summarized), video (up to two hours), images, audio files (up to 22 hours). |
| **Output(s)** | Generated text in response to the input (e.g., an answer to the question, a summary of multiple documents, comparing documents/videos). |

### Usage

| Field | Details |
|---|---|
| **Application** | Gemini is designed to accelerate research on language models, for use as a building block in features within Google products, and as a building block for select applications such as Search Generative Experiences (see Gemini 1.0 model card; Gemini-Team et al., 2023). The Gemini 1.5 models provide particular uses for applications which require: (1) learning from large amounts of new information, for example accurately analyzing, classifying and summarizing large amounts of content within a given prompt, (2) generating more relevant responses, with Gemini 1.5 models excelling at in-context learning to generate more useful and relevant responses; and (3) better reasoning across modalities, with longer context window supporting more sophisticated reasoning across different types of information. |
| **Known Caveats** | Gemini 1.5 models should not be made available as part of a general-purpose service or product, or used within a specific downstream application without a prior assessment and mitigation of the safety and fairness concerns specific to the downstream use. |

### Implementation Frameworks

| Field | Details |
|---|---|
| **Hardware & Software** | Training was done using JAX (Bradbury et al., 2018) and ML Pathways (Dean, 2021). JAX, powered by XLA (XLA, 2019), including the GSPMD (Xu et al., 2021) partitioner for automatic parallelization, allows researchers to leverage the latest generation of hardware, including TPUs, for faster and more efficient training of large models. ML Pathways is Google's latest effort to build artificially intelligent systems capable of generalizing across multiple tasks. This is specially suitable for foundation models, including large language models like these ones. Together, JAX and ML Pathways are used as described in (Gemini-Team et al., 2023); "the 'single controller' programming model of JAX and Pathways allows a single Python process to orchestrate the entire training run, dramatically simplifying the development workflow." |
| **Compute Requirements** | Not reported. |

### Model Characteristics

| Field | Details |
|---|---|
| **Model initialization** | The models are trained from a random initialization. |
| **Model Status** | These are static models trained on an offline dataset. |
| **Model Stats** | Not reported. |

### Data Overview

| Field | Details |
|---|---|
| **Training Dataset** | Gemini 1.5 models are trained on a variety of multimodal and multilingual data. Refer to Section 4 (Training Infrastructure and Dataset). |
| **Evaluation Dataset** | Refer to Section 5 (Evaluation) where we cover core capability evaluations in text, audio and vision. |
| **Fine-tuning Dataset** | Gemini 1.5 Pro and Flash are fine-tuned on a collection of multimodal data containing paired instructions and corresponding desired responses. Refer to Section 4 (Training Infrastructure and Dataset) for more. |

### Evaluation Results

| Field | Details |
|---|---|
| **Benchmark Information** | See Section 5 (Evaluation) where we cover core capability evaluations in text, audio and vision. |
| **Evaluation Results** | See Section 5 (Evaluation) where we cover core capability evaluations in text, audio and vision. |

### Model Usage & Limitations

| Field | Details |
|---|---|
| **Sensitive Use** | For an analysis of risks and sensitive uses associated with the Gemini models, see Section 9 (Safety, Security, and Responsibility). |
| **Known Limitations** | Gemini models can exhibit limitations outlined in the prior Gemini 1.0 Technical Report (Gemini-Team et al., 2023), with specific discussion on long context within Section 9 (Safety, Security, and Responsibility). |
| **Ethical Considerations & Risks** | A reflection on the potential risks and impacts of the Gemini 1.5 Pro models can be found in Section 9 (Safety, Security, and Responsibility). For evaluation details for a range of risks, see Section 9.4 (Results on Training/Development Evaluations). |

**Table 45** caption: "Model card for Gemini 1.5 Pro and Flash." [p. 107]

---

## 12.2. Further haystack results [p. 107-108]

[p. 107] Further "multiple needle-in-a-haystack" results are shown in Figure 27, where recall is considered for a varied number of needles (50 and 100). A consistent robust trend in recall is found for Gemini 1.5 Pro in both settings. By zooming in on the first 128K tokens, there is a decreasing trend in recall for both Gemini 1.5 Pro and GPT-4 Turbo, however it is more gradual for Gemini 1.5 Pro.

**Figure 27** (p. 108): "Retrieval performance of the 'multiple needles-in-haystack', which requires retrieving 50 or 100 unique needles in a single turn. We plot recall (number of needles found / number needles hidden in haystack) against the total size of haystack in tokens."

The figure contains four scatter plots with fitted trend lines, arranged in a 2x2 grid:

- **Top row:** Full context range (1K to 128K tokens). Left: # needles = 50. Right: # needles = 100. Both compare Gemini 1.5 Pro (blue) vs GPT-4 Turbo (red/pink). Gemini 1.5 Pro maintains recall around 0.7-0.8 with a slight downward trend; GPT-4 Turbo starts higher at 1K but trends downward more steeply, falling to around 0.4-0.5 at 128K.
- **Bottom row:** Extended context range (1K to 1.0M tokens). Left: # needles = 50. Right: # needles = 100. Only Gemini 1.5 Pro data extends beyond 128K. GPT-4 Turbo data is limited to the first 128K tokens. Gemini 1.5 Pro recall remains relatively stable around 0.6-0.8 across the full 1M token range, with some variance. GPT-4 Turbo recall (in the 1K-128K range) is scattered around 0.2-0.6, trending downward.

---

## 12.3. Automatic question-generation pipeline for Long-document QA [p. 108]

[p. 108] To automatically generate questions, the following process is used:
1. Books are annotated with coreference chains of the entities based on a supervised system.
2. Most relevant passages for an entity are selected via retrieval using the coreference annotation for the entity in question.
3. The top most relevant entities are taken and questions are produced using Gemini 1.0 Ultra.
4. Two filtering methods are applied: cycle-consistency in order to filter out questions not answered correctly, followed by a human evaluation.

---

## 12.4. Multilingual performance breakdown [p. 109]

[p. 109] Additional multilingual results per resource group for the different Gemini models are presented in Table 46.

**Table 46:** Multilingual results per resource group for the different Gemini models. [p. 109]

| Task | Languages | Direction | Gemini 1.0 Pro | Gemini 1.0 Ultra | Gemini 1.5 Flash | Gemini 1.5 Pro |
|---|---|---|---|---|---|---|
| WMT23 1-shot sentence-level machine translation from wmt23 (Metric: BLEURT) | cs, de, en, he, ja, ru, uk, zh | All | 71.73 | 74.41 | 74.09 | **75.25** |
| | | High | 71.71 | 74.15 | 73.86 | **74.75** |
| | | Mid | 71.76 | 74.68 | 74.31 | **75.76** |
| | | En → XX | 71.54 | 74.81 | 74.00 | **75.39** |
| | | XX → En | 72.00 | 73.88 | 74.20 | **75.07** |
| MGSM 8-shot multilingual math reasoning (Metric: Accuracy) | bn, de, en, es, fr, ja, ru, sw, te, th, zh | All | 63.45 | 78.95 | 82.55 | **87.45** |
| | | High | 65.73 | 81.60 | 85.27 | **89.07** |
| | | Mid | 53.60 | 73.20 | 78.80 | **82.40** |
| | | Low | 62.50 | 76.40 | 79.40 | **86.30** |

Bold values indicate the best score in each row (all are Gemini 1.5 Pro).

---

## 12.5. Long context video [p. 109-110]

### 12.5.1. Video Haystack [p. 109-110]

[p. 109] For the video needle-in-haystack task, the text `"The secret word is needle"` is overlaid on a single randomly sampled video frame in a 10:33:14-duration video constructed from concatenating seven copies of the full AlphaGo documentary (Kohs, 2017) back-to-back (for a total of 37994 frames sampled at one frame per second, or 9.9 million tokens) and Gemini 1.5 Pro is asked to answer the question `"What is the secret word?"`. Figure 28 shows an example of the needle embedded at timestamp 52:31, or frame 3151, of the AlphaGo documentary.

**Figure 28** (p. 110): "An example of the needle used in the video needle-in-a-haystack task, embedded at timestamp 52:31, or frame 3151, of the AlphaGo documentary."

The figure shows a screenshot from the AlphaGo documentary (Google DeepMind Challenge Match) with the text `"The secret word is "needle"."` overlaid in a red box at the top of the frame. The scene shows two people playing Go with spectators and a "KBA" logo visible. A subtitle reads "This move was really creative and beautiful."

### 12.5.2. 1H-Video QA Hard Examples [p. 109, 111]

[p. 109] A few hard examples from the 1H-VideoQA dataset are listed in Table 47 that neither GPT-4V nor Gemini 1.5 Pro got correct.

**Table 47:** Questions in 1H-VideoQA that neither Gemini 1.5 Pro (when given all frames sampled at 1 fps) nor GPT-4V (when provided the maximum number of frames allowed by its API) got correct. Correct answers are **highlighted**. [p. 111]

| Video Link | Question | Choices | Timestamp |
|---|---|---|---|
| Link | How many lions were let out of the cage in the jail cell? | (A) 3, (B) 2, (C) 1, (D) 5, **(E) 4** | 1:05:25 to 1:05:55 |
| Link | What is the word written on the green trash cans? | (A) Everbright, **(B) Mizuda**, (C) Waste Management, (D) 800 Super, (E) GAEA | 39:32 |
| Link | Which shape has the plaque that the Emperor gave to the Dalai Lama? | (A) a cross, (B) a pentagon, **(C) a square**, (D) a circle, (E) a crescent | 25:27 |
| Link | Where do the man and woman first kiss? | (A) club, (B) park, **(C) ferris wheel**, (D) couch, (E) car | 35:51 |
| Link | Which movie poster is not in the background of the two hosts? | (A) the great escape, (B) batman: the dark knight, (C) dune, **(D) pulp fiction**, (E) inception | 34:52, 1:03:23 |

---

## 12.6. Generic long context math prompting [p. 109-111]

### 12.6.1. Hendrycks' MATH Dataset: Performance Analysis and Potential for Improvement [p. 109]

[p. 109] While top models are increasingly solving problems in Hendrycks' MATH, with some achieving a 50% solve rate, it remains a valuable tool for assessing model performance across various mathematical disciplines.

### 12.6.2. Intermediate Algebra (Levels 4 and 5): A Persistent Challenge [p. 109]

[p. 109] Among the seven subdomains in Hendrycks' MATH, Intermediate Algebra (levels 4 and 5) poses the greatest challenge for current models. GPT-4 achieves a solve rate of only 12.5%, while Gemini 1.5 Pro achieves 18.6% and GPT-4-turbo reaches 20.6%. This difficulty stems from the computational complexity of certain problems and the need for specialized methods and algorithms in their solutions. Intermediate Algebra (levels 4 and 5) constitutes 10.6% of the whole MATH dataset. Results in this section are obtained with Gemini 1.5 Pro and not with the Math-Specialized Gemini 1.5 Pro model.

### 12.6.3. Leveraging Python and SymPy for Enhanced Performance [p. 109-110]

[p. 109-110] One promising approach to improve performance involves prompting models to generate solutions using Python libraries like SymPy. However, this introduces the challenge of ensuring accurate implementation of algebraic tools within these libraries. To address this, providing extensive in-context examples of SymPy and SciPy usage (approximately 730,000 tokens) has proven to significantly enhance performance. This strategy enabled Gemini 1.5 Pro to achieve a 25.8% solve rate on Intermediate Algebra Levels 4 and 5, considerably surpassing the baseline performance of Gemini 1.5 Pro, GPT-4 and GPT-4-turbo.

### 12.6.4. Generic long prompt as an alternative to sophisticated prompts and fine-tuning [p. 110]

[p. 110] The aforementioned SymPy and SciPy prompt consists of all examples in the official SymPy and SciPy repositories, without any filtering or human intervention. The code downloading and concatenating all these examples is presented in the next section. Alternatively, one could consider an expert-written prompt, an automatically optimized prompt (e.g., (Fernando et al., 2023; Yang et al., 2023a)), or targeted Python fine-tuning (e.g., (Toshniwal et al., 2024)). While any of these methods is likely to ultimately lead to more optimal results than generic long-context prompting, in the baseline evaluation, an expert-written few-shot Python prompt based on the Minerva prompt resulted in a competitive but slightly lower score of 22%.

### 12.6.5. Python Evaluation Process [p. 110-111]

[p. 110-111] All Python evaluations were conducted in three stages:

1. **Initial solution:** The model proposed an initial solution.
2. **Error correction (attempt 1):** If the initial solution resulted in an error, the model was provided with the first 10 lines of the error trace, along with the previously used prompt and the first solution. It then attempted to generate a corrected solution.
3. **Error correction (attempt 2):** If the second solution also resulted in an error, the model was given one final attempt. This time, the context included both previous solutions and their corresponding error traces.

[p. 111] Using this process, Gemini 1.5 Pro successfully solved between 80 and 110 problems (out of 528) in the first stage, 20 to 30 problems in the second stage, and 5 to 10 problems in the final stage. Correctness of answers is verified using the same process as for the whole MATH dataset; see Appendix 12.13 for details.

---

**Table 48:** Performance of different models on Intermediate Algebra (Levels 4 & 5) in Hendrycks' MATH dataset. [p. 112]

| Model | Intermediate Algebra (Levels 4 & 5) |
|---|---|
| GPT-4 | 12.5% |
| Gemini 1.5 Pro | 18.6% |
| GPT-4-turbo | 20.6% |
| Gemini 1.5 Pro (with the 0-shot Python instruction) | 21.4% |
| Gemini 1.5 Pro (with the Minerva Python prompt) | 22.0% |
| Gemini 1.5 Pro (with generic SymPy/SciPy prompt) | 25.8% |

### 12.6.6. Downloading and preparing all SymPy and SciPy examples [p. 112-113]

[p. 112-113] A Python script is provided for downloading and concatenating all SymPy and SciPy example files from their official GitHub repositories. The script defines three functions:

- `get_paths(repo, path="")`: Recursively gets a list of all file paths in a GitHub repository directory and its subdirectories using the GitHub API.
- `download_file_content(repo, file_path)`: Downloads the content of a single file from a GitHub repository via raw.githubusercontent.com.
- `concatenate_files(repo, directory, output_file, extensions_to_keep=['py', 'ipynb'])`: Concatenates all files with specified extensions in a given directory of a GitHub repository into a single output file.

The script is then used to:
- Get SymPy examples from `sympy/sympy` repo, `examples` directory, saving to `concatenated_sympy_examples.txt` (keeping `.py` and `.ipynb` files).
- Get SciPy examples from `scipy/scipy` repo, `doc/source/tutorial` directory, saving to `concatenated_scipy_examples.txt` (keeping `.rst`, `.py`, and `.ipynb` files).

### 12.6.7. An expert-written Python Minerva prompt [p. 113-114]

[p. 113-114] An expert-written prompt is provided in Python, structured as a series of `exercise` functions with docstrings describing math problems and Python/SymPy code solving them. The prompt header reads:

```
# Language: Python 3
# Task: Synthesize function to solve the problem
```

With a module-level docstring:
> "Contains maths exercises formulated in doc-strings of functions. Solutions are written in simple python code and with a lot of comments that explain what is done and why and how it is related to the specification."

Four example exercises are shown:

1. **exercise1()**: Finding the domain of the expression $\frac{\sqrt{x-2}}{\sqrt{5-x}}$ using SymPy's `solve_univariate_inequality` and `Intersection`.
2. **exercise2()**: Given $\det \mathbf{A} = 2$ and $\det \mathbf{B} = 12$, finding $\det(\mathbf{A} \mathbf{B})$ by multiplying the determinants.
3. **exercise3()**: A word problem about Terrell lifting weights — computing equivalent repetitions when switching from 20-pound to 15-pound weights.
4. **exercise4()**: Given the system of equations $6x - 4y = a$ and $6y - 9x = b$, determining $\frac{a}{b}$ using SymPy symbolic computation.

### 12.6.8. Example instructions added to Python prompts [p. 114-115]

[p. 114-115] Several wordings of instructions were tried, close to the following templates:

**Stage 1 (initial solution) prompt template:**

> "You are a math and coding expert and you know how to use attached code snippets. I gave you a series of demonstrations of math Problems and Python Solutions. When you respond to the next problem, first find similar snippets and describe them before writing your solution. Describe functions, classes and methods that are relevant for the Problem. Then respond with the Python Solution of the final Problem, thinking step by step. Remember to define all variables and include all imports. Finish your code with `answer = ...` `print(answer)` where answer is a float number, a tuple of float numbers, a sympy expression or a string."

**Stage 2 (error correction attempt 1) prompt — divided into two parts:**

Part 1 (before the proposed program and error traces):
> "You are a math and coding expert and you know how to use attached code snippets. I gave you a series of demonstrations of math Problems and Python Solutions. The next problem has a solution that generated an exception."

Part 2 (after the proposed program and error traces):
> "First find similar snippets and describe them before writing your solution. Describe functions, classes and methods that are relevant for the Problem. Then analyze why the original solution resulted in an exception and respond with an improved Python Solution of the final Problem, thinking step by step. Remember to define all variables and include all imports. Finish your code with `answer = ...` `print(answer)` where answer is a float number, a tuple of float numbers, a sympy expression or a string."

[p. 115] In the third stage, the instruction was modified to account for two solutions present in the context.

### 12.6.9. Example problem and a Gemini 1.5 Pro solution [p. 115-116]

[p. 115-116] An example problem and Gemini 1.5 Pro's solution are presented.

**Problem:**
> "Let $a$, $b$, and $c$ be nonnegative real numbers such that $a + b + c = 1$. Find the maximum value of $a(a + b)^2 (b + c)^3 (a + c)^4$."

**Gemini 1.5 Pro's Python answer:**

The model's response is structured with:
1. A heading "Finding the Maximum Value of a Function with Constraints"
2. Identification of relevant SciPy functions: `scipy.optimize.minimize` and `scipy.optimize.Bounds`
3. A Python solution using numerical optimization:
   - Defines `objective_function(x)` returning `-a * (a + b)**2 * (b + c)**3 * (a + c)**4` (negative for maximization)
   - Defines a constraint function enforcing `a + b + c = 1`
   - Uses initial guess `x0 = np.array([0.3, 0.3, 0.4])`
   - Sets bounds `0 <= a, b, c <= 1`
   - Calls `minimize` with `method='SLSQP'`, the bounds, and the equality constraint
   - Extracts the solution and computes the maximum value

[p. 116] Running this code in Google Colab produces a result of 0.015624507088912548, which falls within the numerical tolerance used for evaluations on the MATH dataset (see Appendix 12.13 for details), compared to the exact answer of 1/64. While alternative solutions using natural language or SymPy with multiple applications of the AM-GM inequality are possible, the SciPy approach presented here offers the most straightforward, albeit approximate solution.

---

## 12.7. Unstructured Multimodal Data Analytics [p. 116–117]

[p. 116–117] The full prompt used for each model when performing analytics of the images is provided (some information is anonymized):

> "Please process the following images, and output the [category], [color], [semantic attribute] for each image.
> - For [category], please choose from [anonymized, 38 classes]
> - For [color], please choose from [anonymized, 45 classes]
> - For [semantic attribute], please choose from [anonymized, 8 classes]
> Each image has its own ID starting from id_0. Please only output the table formatted in the following order:
> image_0,category,color,semantic attribute
> image_1,category,color,semantic attribute
> ...
> Below are the images:
> image_0: \<base64 string of the image\>
> image_1: \<base64 string of the image\>
> image_2: \<base64 string of the image\>
> \<...and more images\>
> image_255: \<base64 string of the image\>
> Please output the table only in the format specified."

[p. 117] The evaluation results on each of the individual attributes are presented in Figure 29.

**Figure 29** (p. 117): "Performance of models on unstructured data analytics tasks."

The figure contains three line charts side by side, each plotting Accuracy (%) vs Batch Size (x-axis: 8, 16, 32, 64, 128, 256, 512) for three models: Gemini 1.5 Pro, GPT 4 Turbo 20240409, and Claude 3 Opus.

- **Left panel — Accuracy on category extraction:** Gemini 1.5 Pro (blue) maintains relatively stable accuracy around 75–85% across batch sizes. GPT 4 Turbo 20240409 (orange) starts around 80% at batch size 8 but trends downward to around 35–40% at batch size 512. Claude 3 Opus (green) starts around 70% at batch size 8 and declines sharply to around 30% at batch size 512.
- **Middle panel — Accuracy on color extraction:** Gemini 1.5 Pro maintains accuracy around 50–60% across batch sizes. GPT 4 Turbo starts around 55% at batch size 8 and drops to around 20% at batch size 512. Claude 3 Opus starts around 45% and drops to around 20% at batch size 512.
- **Right panel — Accuracy on semantic attribute extraction:** Gemini 1.5 Pro maintains accuracy around 65–70% across batch sizes. GPT 4 Turbo starts around 65% and drops to around 45% at batch size 512. Claude 3 Opus starts around 55% at batch size 8, increases slightly to around 60% at batch size 16–32, then drops to around 45% at batch size 512.

In all three panels, Gemini 1.5 Pro shows the most stable performance as batch size increases, while GPT 4 Turbo and Claude 3 Opus degrade significantly at larger batch sizes.

---

## 12.8. Planning [p. 117–121]

[p. 117] Three planning tasks are evaluated using 1-shot prompts in PDDL (Planning Domain Definition Language) format: BlocksWorld, Logistics, and Mini-Grid.

### BlocksWorld [p. 117–118]

[p. 117–118] The 1-shot prompt for the BlocksWorld task is provided. It consists of a solved example followed by the test problem.

**1-shot example (BW-rand-4):**
- Domain: `blocksworld-4ops`
- Objects: `b4 b1 b3 b2`
- Init state: `(on b3 b1)`, `(on b1 b4)`, `(clear b3)`, `(handempty)`, `(ontable b2)`, `(ontable b4)`, `(clear b2)`
- Goal: `(on b2 b4)`, `(on b3 b1)`
- Solution plan:
  ```
  (unstack b3 b1)
  (put-down b3)
  (unstack b1 b4)
  (put-down b1)
  (pick-up b2)
  (stack b2 b4)
  (pick-up b3)
  (stack b3 b1)
  done.
  ```

**Test problem (BW-rand-6):**
- Domain: `blocksworld-4ops`
- Objects: `b5 b1 b4 b2 b3 b6`
- Init state: `(on b4 b1)`, `(handempty)`, `(ontable b6)`, `(on b2 b4)`, `(clear b3)`, `(ontable b5)`, `(on b3 b2)`, `(clear b6)`, `(on b1 b5)`
- Goal: `(on b4 b2)`, `(on b1 b4)`, `(on b5 b1)`, `(on b3 b5)`

### Logistics [p. 118–119]

[p. 118–119] The 1-shot prompt for the Logistics task is provided.

**1-shot example (logistics-c4-s2-p3-a4):**
- Domain: `logistics-strips`
- Objects: airplanes `a0 a1 a2 a3`, cities `c0 c1 c2 c3`, trucks `t0 t1 t2 t3`, locations `l0-0 l0-1 l1-0 l1-1 l2-0 l2-1 l3-0 l3-1`, packages `p0 p1 p2`
- Init state includes airplane, city, truck, location, airport definitions and initial positions of trucks, packages, and airplanes
- Goal: `(at p0 l2-0)`, `(at p1 l2-0)`, `(at p2 l1-1)`
- Solution plan: A 20-step plan involving loading/unloading trucks and airplanes, driving trucks, and flying airplanes:
  ```
  (load-truck p0 t1 l1-1)
  (drive-truck t1 l1-1 l1-0 c1)
  (unload-truck p0 t1 l1-0)
  (load-airplane p0 a1 l1-0)
  (fly-airplane a1 l1-0 l2-0)
  (unload-airplane p0 a1 l2-0)
  (drive-truck t0 l0-0 l0-1 c0)
  (load-truck p1 t0 l0-1)
  (drive-truck t0 l0-1 l0-0 c0)
  (unload-truck p1 t0 l0-0)
  (fly-airplane a3 l3-0 l0-0)
  (load-airplane p2 a3 l0-0)
  (fly-airplane a3 l0-0 l1-0)
  (unload-airplane p2 a3 l1-0)
  (load-truck p2 t1 l1-0)
  (drive-truck t1 l1-0 l1-1 c1)
  (unload-truck p2 t1 l1-1)
  (fly-airplane a1 l2-0 l0-0)
  (load-airplane p1 a1 l0-0)
  (fly-airplane a1 l0-0 l2-0)
  (unload-airplane p1 a1 l2-0)
  done.
  ```

**Test problem (logistics-c2-s2-p3-a2):**
- Domain: `logistics-strips`
- Objects: airplanes `a0 a1`, cities `c0 c1`, trucks `t0 t1`, locations `l0-0 l0-1 l1-0 l1-1`, packages `p0 p1 p2`
- Init state includes airplane, city, truck, location, airport definitions and initial positions
- Goal: `(at p0 l0-1)`, `(at p1 l1-0)`, `(at p2 l0-0)`

### Mini-Grid [p. 120–121]

[p. 120–121] The 1-shot prompt for the Mini-Grid task is provided.

**1-shot example (grid_2Vroom2):**
- Domain: `grid`
- Objects: places `p0`–`p8`, `shape0`, `key0`
- Init state: places, shape, key, open/locked cells (`p4` is locked, all others open), connected cells (a 3x3 grid connectivity pattern), lock-shape and key-shape pairings, key placement `(at key0 p0)`, robot placement `(at-robot p3)`, `(arm-empty)`
- Goal: `(at-robot p7)`
- Solution plan:
  ```
  (move p3 p2)
  (move p2 p0)
  (pickup p0 key0)
  (move p0 p2)
  (unlock p2 p4 key0 shape0)
  (move p2 p4)
  (move p4 p5)
  (move p5 p7)
  done.
  ```

**Test problem (grid_3Vroom3):**
- Domain: `grid`
- Objects: places `p0`–`p28`, `shape0`, `key0`
- Init state: 29 places, shape, key, open/locked cells (`p9` and `p19` are locked, all others open), connected cells (a larger grid connectivity pattern with adjacency relationships among `p0`–`p28`), lock-shape pairings (`lock-shape p9 shape0`, `lock-shape p19 shape0`), key-shape pairing (`key-shape key0 shape0`), key placement `(at key0 p12)`, robot placement `(at-robot p16)`, `(arm-empty)` [p. 121–122]
- Goal: `(at-robot p4)` [p. 122]

---

### Trip Planning [p. 123]

[p. 123] The 1-shot prompt for the Trip Planning task is provided.

**1-shot example:**
- Problem: Visit 6 European cities for 13 days total. Constraints include spending 3 days in Dublin, meeting friends at Dublin between day 7 and day 9, visiting Madrid for 2 days (between day 2 and day 3), staying in Oslo for 3 days, visiting London for 2 days, spending 3 days in Vilnius, staying in Berlin for 5 days, and attending a wedding in Berlin between day 3 and day 7.
- Direct flights available: London and Madrid, Oslo and Vilnius, Berlin and Vilnius, Madrid and Oslo, Madrid and Dublin, London and Oslo, Madrid and Berlin, Berlin and Oslo, Dublin and Oslo, London and Dublin, London and Berlin, Berlin and Dublin.
- Solution:
  ```
  **Day 1-2:** Arriving in London and visit London for 2 days.
  **Day 2:** Fly from London to Madrid.
  **Day 2-3:** Visit Madrid for 2 days.
  **Day 3:** Fly from Madrid to Berlin.
  **Day 3-7:** Visit Berlin for 5 days.
  **Day 7:** Fly from Berlin to Dublin.
  **Day 7-9:** Visit Dublin for 3 days.
  **Day 9:** Fly from Dublin to Oslo.
  **Day 9-11:** Visit Oslo for 3 days.
  **Day 11:** Fly from Oslo to Vilnius.
  **Day 11-13:** Visit Vilnius for 3 days.
  done.
  ```

**Test problem:**
- Problem: Visit 6 European cities for 17 days total. Constraints include spending 4 days in Manchester, staying in Florence for 5 days, spending 3 days in Geneva (attending a wedding in Geneva between day 1 and day 3), spending 3 days in Seville (attending a conference in Seville during day 7 and day 9), visiting Prague for 2 days, and staying in Valencia for 5 days (attending an annual show in Valencia from day 3 to day 7).
- Direct flights available: Manchester and Prague, Seville and Manchester, Geneva and Manchester, Valencia and Seville, Geneva and Valencia, Valencia and Prague, Prague and Florence, Geneva and Prague.

### Calendar Scheduling [p. 123–124]

[p. 123–124] The 1-shot prompt for the Calendar Scheduling task is provided.

**1-shot example:**
- Problem: Schedule a meeting for Samuel, Evelyn, Ruth and Amanda for half an hour between the work hours of 9:00 to 17:00 on Monday.
- Schedules: Samuel is free the entire day. Evelyn has meetings on Monday during 9:00 to 10:00, 11:00 to 12:00, 12:30 to 13:00, 15:30 to 16:00. Ruth has meetings on Monday during 9:30 to 11:00, 11:30 to 12:30, 13:00 to 13:30, 14:00 to 14:30, 15:00 to 16:00, 16:30 to 17:00. Amanda has meetings on Monday during 10:00 to 10:30, 11:00 to 12:30, 13:00 to 13:30, 14:00 to 15:00, 15:30 to 16:00.
- Constraint: Amanda can not meet on Monday before 16:00.
- Solution: Monday, 16:00 – 16:30.

**Test problem:**
- Problem: Schedule a meeting for Walter, Jacob, Jennifer and Joan for one hour between the work hours of 9:00 to 17:00 on Monday.
- Schedules: Walter is busy on Monday during 9:30 to 10:00, 13:00 to 13:30. Jacob has meetings on Monday during 11:00 to 11:30, 13:00 to 13:30. Jennifer is busy on Monday during 9:30 to 10:30, 11:30 to 12:00, 12:30 to 15:00. Joan has blocked their calendar on Monday during 9:30 to 10:00, 10:30 to 11:30, 12:00 to 12:30, 13:00 to 14:00, 14:30 to 15:30.

---

## 12.9. Productivity Impact of LLMs Across Jobs [p. 124–126]

[p. 124] For further examples from Section 6.1.7, see Tables 49, 50, 51.

**Table 49** | Example task from a Pre-school Teacher. [p. 125]

The task describes a pre-school teacher who spends about 3 hours each Friday afternoon searching for a weekly theme, making a printable calendar for the upcoming week, and designing activity sheets for each day. The teacher requests:

1. Choose a theme for the week of May 6th through May 10th, 2024 (Maple Grove, MN), suited to the typical climate in the first week of May.
2. Choose weekly components: Color of the week, Animal of the week, Snack theme of the week (tree fruits, no nuts, processed sugars, or gluten), Word of the week (related to the theme), Song of the week.
3. For each day, provide: a specific snack, a fact about the animal of the week, a book title and author, a positive "sentence of the day" including the word of the week, and a printable activity sheet.
4. Design a weekly calendar for the students including theme, weekly components, and daily activities — visually appealing for 4-year-olds.
5. Provide an audio file of the song of the week and a printable sing-along document with lyrics and progression images.
6. Provide 5 daily activity sheets (printable, no longer than 1 page each).
7. Provide a table with 3 columns (Snack, Book, Supplies) and 5 rows for each day.

Attached documents: a web page with pre-school themes and an image with an example of a weekly pre-school planner.

**Table 50** | Example task from a Real Estate Photographer. [p. 126]

The task describes a real estate photographer who needs help analyzing metadata and filenames from a real estate photo shoot (58 photos) to assess image quality before editing. A CSV file contains key details: Filename, Camera model, Shutter speed, Aperture, ISO, Focal length, Timestamp, GPS coordinates. The analysis should summarize:

1. Photos that may have quality issues based on camera settings: shutter speed slower than 1/60 (potential blur/camera shake), aperture wider than f/8 (reduced sharpness), ISO higher than 800 (excessive noise).
2. A list of photos grouped by room/area of the house, based on timestamps and/or similar filenames (e.g. kitchen_01.jpg, kitchen_02.jpg, etc.).
3. The 10 photos with the widest angle of view based on focal length, as these often make the best "hero" shots for real estate listings.
4. Any filenames that don't follow the standard naming convention of [room/area]_[number].jpg.

Attached documents: a CSV file containing key details for each of the 58 photos and a PDF of the studio's technical quality standards.

---
[p. 127 continued]

**Table 51** | Example task from a PR Manager. [p. 127]

The task describes a PR Manager who needs to generate a six-month PR plan of ideas for a chiropractor client (Dr. Joe). The client wants to tie into monthly observances. Activities of interest include: special targeted client days (press release/web), fundraisers for local nonprofits (press release/web), letters to the editor about a specific wellness issue (local newspaper), special wellness lecture nights at his office or another community venue (press release/web), promotion of his Biggest Winner lifestyle program (press release/web), and targeted promotions to bring clients in for an adjustment/exam (email messages).

An old PR plan is attached for inspiration (formatted differently), along with a client story to provide perspective on Dr. Joe.

The deliverable is a one- to two-page list of publicity ideas by month from January to June, using the ideas above with national observances listed below. A mix of activities is optimal for publicity purposes. Two or three sentences per idea, no more than two ideas per month, one idea is also acceptable.

Monthly observances provided:
- January: National Blood Donor Month
- February: National Eating Disorder Month
- March: National Sleep Awareness Week
- April: Every Kid Healthy Week, Patient Experience Week, World Health Day
- May: National Women's Health Month
- June: Men's Health Month, Family Health and Fitness Day

Attached documents: a PDF of an old PR plan and a PDF of a client story.
