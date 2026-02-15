# 2 LongGenBench Benchmark [p. 3–5]

## 2.1 Task Definition [p. 3]

Evaluating the quality of super-long-form generation presents a unique set of challenges due to the inherent complexity of long texts. Traditional human evaluation methods, while precise, are expensive and not scalable. Although using large language models for assessment is feasible, their lack of interpretability often hampers their utility. Thus, we focus on the "instruction-following" task in super-long-form generation, where the text must include specific details in the generated text. This task reflects real-world scenarios that require a high degree of attention to detail over extended sequences, such as technical documentation or detailed design proposals. In this study, we define a task type termed Strictly Sequential Task, represented as a sequence of subtasks **T** = {T₁, T₂, T₃, ..., Tₙ}² where each subtask is responsible for generating a specific volume of text. For instance, an LLM might be tasked with designing a 100-floor skyscraper, specifying the content and purpose of each floor [p. 3].

**Figure 1** (p. 3): "LongGenBench Overview: Select from four scenarios—Diary, Menu Design, Skyscraper Design, and Urban Planning—each offered in both short and long versions to determine the main task prompt. 2) Task Instruction: Employ three templates (Single (SI), Range (RI), and PI (Periodic)) to generate tasks characterized by random times or locations, along with the corresponding prompts and verification set. 3) Instruction Synthesis: Integrate all prompts generated in the prior step to create a comprehensive set of instructions with a final check-set. 4) Example: An illustration of Sophia's weekly diary task is provided as an example."

Description: Overview diagram showing the LongGenBench workflow
- Key elements: Four scenario icons (Diary, Menu, Skyscraper, Urban Planning) at top showing weekly/daily variants and different size versions (100 Fl vs 300 Fl for skyscraper, 10x10 Blk vs 19x19 Blk for urban planning)
- Three instruction types shown: SI Template-Lib (Wife's Birthday June 29, Mike's wedding August 3), RI Template-Lib (Beach Holiday June 22-28), PI Template-Lib (Community Volunteers May 1, Community Volunteers May 15) with corresponding mathematical notations
- Bottom shows synthesis process combining main task prompt, single instruction, range instruction, periodic instruction, and generative prompt
- Example box shows Sophia's diary entry details
- Notable patterns: Illustrates how different instruction types are combined to create comprehensive evaluation tasks
- Supports claim: Demonstrates the systematic approach to generating diverse long-form generation tasks with multiple constraint types

## 2.2 Four Distinct Scenario Setups [p. 3–4]

To comprehensively assess the long-form generation capabilities of models, we have devised four distinct task scenarios to supplement our predefined tasks, as illustrated in Figure 1 (1). These scenarios fall into two categories: Temporal (Diary Writing, Menu Design) and Spatial (Skyscraper Design, Urban Planning). Moreover, each scenario incorporates both short and long versions to assess the effectiveness of various output lengths [p. 3].

These scenarios were carefully chosen to reflect both creative and technical long-form generation tasks. They offer a diverse set of challenges by including temporal tasks (e.g., Diary Writing)

---

[p. 4 continued]

that require maintaining consistent information over time and spatial tasks (e.g., Urban Planning) that test the model's ability to handle spatial relationships and detailed designs. These scenarios mirror real-world applications, from planning documents to creative writing, and thus provide a comprehensive evaluation of long-context LLMs. Table 2 offers comprehensive descriptions for each scenario, with each designed around a unique constraint to generate 100 different task instructions³ [p. 4].

**Table 2:** Scenario task descriptions [p. 4]

| Category | Scenarios | Task | Task Description |
|----------|-----------|------|-----------------|
| Temporal | Diary | Weekly Diary | Generate entries for each week of the year |
| Temporal | Diary | Daily Diary | Generate entries for each day of the year |
| Temporal | Menu | Weekly Menu | Plan menus for each week of the year |
| Temporal | Menu | Daily Menu | Plan menus for each day of the year |
| Spatial | Skyscraper Design | 100-floor Design | Develop a design for a 100-floor skyscraper |
| Spatial | Skyscraper Design | 361-floor Design | Develop a design for a 300-floor skyscraper |
| Spatial | Urban Planning | 10x10 block Design | Design an urban layout on a 10x10 block grid |
| Spatial | Urban Planning | 19x19 block Design | Design an urban layout on a 19x19 block grid |

## 2.3 Specific Task Instruction [p. 4]

To enhance task control and flexibility, we have developed three distinct task settings:

**• Single Instruction (SI):** Injects specific information at a unique point within the generated text.

$$T_S = \{T_{s_1}, T_{s_2}, ...\}$$

**• Range Instruction (RI):** Requires the model to incorporate information within specified ranges of the text.

$$T_R = \{T_{R_i}, T_{R_{i+1}}, \ldots, T_{R_{i+j}}\}$$

**• Periodic Instruction (PI):** Distributes information at predefined intervals throughout the text.

$$T_P = \{T_{P_n}, T_{P_{2n}}, \ldots, T_{P_{m*n}}\}$$

**• Check Set:** Includes tasks for all three aforementioned settings.

$$Check\_set = \{T_S, T_R, T_P\}$$

For example, in the design of a 100-floor skyscraper, the Single Instruction may specify that the 34th floor hosts an aerial gym and the 54th floor houses a law firm. The Range Instruction might designate floors 1 through 9 as a comprehensive shopping mall, whereas the Periodic Instruction could dictate that starting from the 20th floor, every 10th floor operates a small aerial garden [p. 4].

We utilize over 20 templates for each type of instruction, with the floors or locations being randomly assigned to ensure task diversity. These settings, managed via various templates, guarantee controlled coverage across all textual positions, thus facilitating a comprehensive and efficient evaluation, as illustrated in Figure 1 (2) [p. 4].

Through this approach, we generate the main task instructions T and simultaneously acquire the corresponding Check_set, which supports subsequent evaluations and constructs a task conducive to super-long-form generation. Subsequently, we splice the main prompt with the specific task instructions (STI)⁴ and add the generation prompt to form the final evaluation data [p. 4].

## 2.4 Evaluation Metric [p. 4–5]

To quantitatively evaluate performance for LongGenBench tasks, we introduce three complementary metrics⁵:

---

[p. 5 continued]

**Main Task Completion.** This metric evaluates the extent to which all designated subtasks are accomplished. The completion rate is quantified using the following equation:

$$\text{Completion Rate (CR)} = \frac{\text{Number of Completed Subtasks}}{\text{Total Number of Subtasks}} \times 100\%$$

In this context, the numerator denotes the count of subtasks successfully executed by the model, and the denominator represents the total number of subtasks as defined in the Strictly Sequential Task. For instance, does the model consistently complete a diary entry for each day without omitting any dates? [p. 5]

**Specific Task Instruction Completion (STIC-1).** This metric evaluates the model's adherence to specific task instructions. We calculate the completion counts for the Single Instruction (SI), Range Instruction (RI), and Periodic Instruction (PI). STIC-1 quantifies how well the model follows these instructions across subtasks, focusing on whether the instructions are correctly implemented. For example, in the Skyscraper Design task, if the model is instructed to place an aerial gym on the 34th floor and consistently places it on a different floor, it would receive a lower STIC-1 score.

$$\text{STIC-1} = \frac{\text{Single Instruction} + \text{Range Instruction} + \text{Periodic Instruction}}{\text{Total Number of Outputs to Specific Task Instructions}}$$

**Specific Task Instruction Completion-2 (STIC-2).** STIC-2 provides a more granular assessment by measuring the overall completion of specific task instructions, including their presence and execution quality across all subtasks. In addition to adherence, it assesses whether the model consistently follows these instructions throughout the entire task. For example, if the model periodically repeats certain elements but not at the required intervals, it would affect its STIC-2 score.

$$\text{STIC-2} = \frac{\text{Single Instruction} + \text{Range Instruction} + \text{Periodic Instruction}}{\text{Total Number of Specific Task Instructions}}$$

STIC-1 is primarily concerned with the completion rate of instructions that result in sub-scenarios, focusing on whether instructions are correctly executed. In contrast, STIC-2 assesses the overall completion of the specific instruction task, including the presence of sub-scenarios and their completion status⁶ [p. 5].

## 2.5 Evaluations Pipeline [p. 5]

Our evaluation process follows a structured pipeline: First, we use a long-context LLM to complete the task instruction T, generating an output. This is then divided into sub-tasks as A = {A₁, A₂, ..., Aₙ}. Next, based on the specific instructions in the check_set, we identify the relevant sub-tasks within A. Finally, we evaluate each sub-task by matching it with Aᵢ ∈ A to compute the final completion score, as detailed in Algorithm 1. This pipeline ensures that the evaluation is both systematic and comprehensive, assessing the model's performance across different instruction settings and levels of complexity⁷. While LongGenBench primarily evaluates the model's ability to follow detailed instructions, future work could expand the benchmark to include more open-ended tasks that assess creativity and logical reasoning. This would provide a broader evaluation of a model's capabilities in generating coherent, engaging, and logically sound long-form text [p. 5].

---

²In Appendix A, there is a detailed description of the definitions of mathematical symbols.
³Examples of Task Instructions for each scenario are provided in Appendix B.
⁴Each of our main task instructions T splice 5 single instructions, 1 range instruction task, and 1 periodic instruction task.
⁵In Appendix E, we provide a detailed explanation of STIC-1 and STIC-2, along with a case study analysis.
⁶In Appendix C, there is a detailed evaluations pipeline and example.
⁷Detailed specifications of these models are provided in Appendix D.
