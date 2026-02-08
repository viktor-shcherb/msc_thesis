# 3 InfiniteBench [p. 4–6]

[p. 4] InfiniteBench encompasses 12 tasks spanning 5 domains: retrieval, code, math, novels, and dialogue. Two of these tasks are derived from existing literature (Mohtashami and Jaggi, 2023; Liu et al., 2023). Among the newly introduced tasks, half are generated automatically, while the remainder are annotated by humans.

In total, InfiniteBench includes 3946 examples, featuring a length beyond 100K tokens (average approximately 200K). Figure 2 illustrates the distribution of these tasks. Table 2 details their respective input and output lengths as well as the number of examples per task.

The tasks can be grouped into two broad categories: (1) realistic context collected from real-world scenarios which has potential practical usage of long context LLMs, and (2) synthetic contexts which are created or collected for testing certain capabilities of long-context LLMs.

## 3.1 Realistic Context

### 3.1.1 Novel

[p. 4] Novel-based tasks utilize novels sourced from websites (sparknotes.com, cliffnotes.com) and are manually filtered. More annotation information is provided in Appendix C.

In these tasks, models are tasked with reasoning over entire novels presented during inference. Recognizing that many novels, along with their movie adaptations and related discussions, are accessible online and may have been encountered by LLMs during training, the authors adopt *key entity replacement* as a countermeasure. This involves substituting prominent entities determined by annotators, such as main character names, with unrelated ones, creating "fake novels".

Using these altered novels, three task formats are designed: summarization, open-form question answering (QA), and multiple-choice (MC) questions, applying key entity replacement to the annotations as well. All English tasks share the same set of modified novels.

[p. 5] **En.Sum** The En.Sum task requires models to generate a concise summary of the novel. Gold standard labels are sourced from the web and undergo manual filtering to remove non-summarization content, like comments. Model performance is evaluated using the ROUGE-L-Sum metric (Lin, 2004).

**En.QA & Zh.QA** The same annotation pipeline is employed for both En.QA and Zh.QA tasks, ensuring that the questions necessitate long-range dependency and reasoning, beyond simple short passage retrieval. The tasks are primarily categorized into two types of reasoning:

- Aggregation: This involves compiling various pieces of information scattered throughout the novel. An example question in InfiniteBench is "How much money in total did A spend on lunch?"
- Filtering: This requires identifying specific information from a larger set. An example question in InfiniteBench is "What color dress did A wear when A met B for the second time?"

These tasks test LLMs to locate and process information within the novel, performing reasoning through aggregation or filtering to derive answers.

**En.MC** The En.MC task is annotated similarly to En.QA, but differs in that the model is presented with four answer choices. Annotators are instructed to craft these options to be challenging.

### 3.1.2 Dialogue

**En.Dia** The construction process for the En.Dia task is depicted in Figure 3. Movie and drama scripts are gathered from a designated online database (imsdb.com), focusing on a corpus of long, multi-role dialogues. Only the English scripts are retained and necessary cleaning is applied.

In the En.Dia task, random instances of character names within a script are replaced with `$$MASK$$`. The objective is to correctly identify these masked names. For scripts falling short of 100K tokens, they are augmented by padding with additional scripts.

### 3.1.3 Code

**Code.Debug** The task is developed as per the process illustrated in Figure 3. Code repositories, sourced from PyPI, undergo a filtering process, and those outside the 64K to 256K token range are excluded (tokenization via the tiktoken tokenizer (OpenAI, 2023c)). Each repository is transformed into a single file, aggregating the content from all files within, each prefaced by its relative path to the root directory. Three of the authors then insert a deliberate and obvious error into one function per repository. The options are presented in the `Class.Function` format. Six methods are employed for bug insertion: (1) deleting a necessary variable declaration; (2) using an incorrect number of arguments in function calls; (3) creating infinite loops; (4) causing indentation errors; (5) substituting references with undefined variable/function names; (6) introducing blatant syntax errors (e.g., non-closed brackets).

Initial results indicate that this task is too challenging for current LLMs (none of the baseline models can identify the most obvious error such as non-closed brackets). To mitigate this, four answer choices are offered, one containing the injected bug and the others being bug-free. Note that this makes many examples easily solved by external retrieval preprocess. However, the authors encourage users not to use external retrieval preprocess to keep the evaluation fair.

## 3.2 Synthetic Context

[p. 5] The second category of tasks is characterized by a synthetic context. These tasks, devoid of direct real-world application or use case, are engineered to evaluate the capability for processing lengthy contexts. Four essential abilities for effective long-context processing are delineated:

1. Location and retrieval. This encompasses all retrieval tasks.
2. Elevated information resolution. This involves the Retrieve.Number task.
3. State preservation. This incorporates the Code.Run and Math.Find functions.
4. Sequential processing. This utilizes the Math.Calc function.

### 3.2.1 Retrieve

[p. 6] The three retrieval tasks in InfiniteBench vary in complexity.

**Retrieve.PassKey** This task is first proposed by Mohtashami and Jaggi (2023). Models are prompted to find a specific `<key>` called pass key, which is a random 5-digit sequence. The pass key is inserted into a lengthy and noisy context. In InfiniteBench, examples are generated with 59 different pass key locations that are evenly distributed in the context. At each location, 10 examples are constructed with different pass keys. This results in 590 examples.

The prompt format is shown in a box on p. 6:
> "There is an important pass key hidden in a lot of irrelevant text. Find it. \<very long noisy context\> The pass key is \<key\>. Remember it. The pass key is \<key\>. \<very long noisy context\> What is the pass key?"

**Retrieve.Number** To examine the local attention of LLMs, the complexity of Retrieve.PassKey is enhanced by increasing the answer length to 10 digits and *incorporating successive repetitive digits*. For example, a `<key>` in Retrieve.PassKey is valued 98762, while in Retrieve.Number is 9998877762. This modification aims to assess the local resolution capabilities of long context models, as preliminary experiments indicate that LLMs struggle with discerning repeated numbers.

**Retrieve.KV** Liu et al. (2023) introduce a key-value retrieval task within a large JSON object containing many key-value pairs (e.g., `30eea139-b6dd-43fc-bc5d-0d3d17980229` -> `bfd36c2b-c57e-41ef-9cc1-b21b4e60e664`). This task demands the model to accurately identify and retrieve the value corresponding to a specified key. The complexity of this task is heightened due to the indistinguishable format of relevant and irrelevant information.

### 3.2.2 Code

[p. 6] **Code.Run** This task evaluates the ability of LLMs to simulate multi-step function executions that involve basic arithmetic operations. While this task is readily solvable using a Python interpreter, the focus here is on the long-term state tracking required in such tasks. The capability of state tracking has been demonstrated in GPT-4 (Bubeck et al., 2023). Specifically, the task involves creating Python code consisting of multiple simple functions, incorporating operations such as addition, subtraction, and nested function calls. The structural design of these tasks is as follows:

```python
def func_0(x):
    return func_1(x) + 4

def func_1(x):
    return x - 1
```

Some functions' return values are dependent on other functions (e.g., `func_0` invokes `func_1`). *Depth* is defined as the number of cascading function calls initiated by a single call. Thus, the depth for `func_1`'s call within `func_0` is 1. In Code.Run, depths ranging from 2 to 10 are employed, ensuring each function calls at most one other function. To keep the simplicity of each single step of computation, these functions are restricted to performing only addition and subtraction.

### 3.2.3 Math

**Math.Find** Math.Find assesses the model's capability to identify specific elements within a large array, requiring comprehensive observation for accuracy. This task also tests the ability to preserve states while encoding the context. Concretely, the model receives an extensive list of numbers and is tasked with locating one of seven key numbers: the three largest (1st, 2nd, and 3rd), the three smallest (1st, 2nd, and 3rd), and the median.

**Math.Calc** To assess sequential processing skills, Math.Calc prompts the model to compute the result of a lengthy arithmetic expression featuring addition and subtraction. Initial experiments indicate that current LLMs struggle to directly produce the final answer. Hence, the authors instead query the LLMs to provide the intermediate result following each operator. Model performance is evaluated based on the number of correct values preceding the first error.

## Table 2

**Table 2** (p. 3): "Data statistics. The columns indicate whether the annotation was auto-generated or done by humans, the number of examples, and the average length (input/output) in tokens."

| Task            | Annotation | # Ex. | Avg Len        |
|-----------------|------------|-------|----------------|
| Ret.PassKey     | Auto       | 590   | 122.4K/2       |
| Ret.Number      | Auto       | 590   | 122.4K/4       |
| Ret.KV          | Auto       | 500   | 121.1K/22.7    |
| En.Sum          | Human      | 103   | 103.5K/1.1K    |
| En.QA           | Human      | 351   | 192.6k/4.8     |
| En.MC           | Human      | 229   | 184.4K/5.3     |
| Zh.QA           | Human      | 189   | 2068.6K/6.3    |
| En.Dia          | Auto       | 200   | 103.6K/3.4     |
| Code.Debug      | Human      | 394   | 114.7K/4.8     |
| Code.Run        | Auto       | 400   | 75.2K/1.3      |
| Math.Calc       | Auto       | 50    | 43.9K/43.9K    |
| Math.Find       | Auto       | 350   | 87.9K/1.3      |

## Figure 2

**Figure 2** (p. 3): "The statistics of the data in InfiniteBench. The radius of each segment indicates the length of input plus output on the logarithmic scale, and the width (or angle) indicates the number of examples (proportionally to the total number of examples)."

Polar area chart (pie-like chart with variable radii) showing the distribution of InfiniteBench tasks. Each segment represents a task. The radius encodes log-scale input+output length and the angle encodes the proportion of total examples. Zh.QA has the largest radius (longest average length at ~2068.6K tokens). The retrieval tasks (Ret.PassKey, Ret.Number, Ret.KV) collectively account for a large angular proportion due to their high example counts (590, 590, 500). Scale markers shown at 100K, 500K, and 2000K.

## Figure 3

**Figure 3** (p. 4): "The annotation pipelines for the human-annotated tasks in InfiniteBench."

Flowchart showing three annotation pipelines:

- **Code.Debug:** PyPI -> Bug Injection -> Option Annotation
- **En.Dia:** Script Database -> Character Masking -> Answer Annotation -> Context Padding
- **Novel:** Novel Database -> Key Entity Replacement -> branches into:
  - Summary Annotation -> En.Sum
  - Answer Annotation -> En.QA
  - Question Annotation -> (and) Option Annotation -> En.MC
  - (Also branches to Zh.QA via answer annotation)
