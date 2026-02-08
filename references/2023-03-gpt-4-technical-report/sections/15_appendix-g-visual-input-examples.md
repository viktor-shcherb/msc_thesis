# Appendix G: Examples of GPT-4 Visual Input [p. 29, 34–39]

[p. 29] Section heading introducing examples of GPT-4's visual input capabilities. Three example prompts are provided demonstrating chart reasoning, physics problem solving from a diagram in French, and image understanding.

## Table 14

**Table 14.** Example prompt demonstrating GPT-4's visual input capability. The prompt consists of a question which requires reading information from a chart and performing computation. [p. 34]

**Title:** GPT-4 visual input example, Chart Reasoning

**User prompt:** What is the sum of average daily meat consumption for Georgia and Western Asia? Provide a step-by-step reasoning before providing your answer.

**Visual input:** A horizontal bar chart titled "Daily meat consumption per person, 1997" (Source: UN Food and Agricultural Organization (FAO), CC BY). The chart shows average daily meat consumption per person, measured in grams per person per day. Countries with daily meat consumption greater than the expected EU average of 165g per person are shown in red; yellow are those countries below 165g but exceeding the more ambitious limit of 40g per person; and in blue are those below 40g per person. Three bars are shown:
- Finland: 175.09 g (red bar)
- Georgia: 79.84 g (yellow bar)
- Western Asia: 69.62 g (yellow bar)

**GPT-4 response:**
> To find the sum of average daily meat consumption for Georgia and Western Asia, we will follow these steps:
> 1. Identify the average daily meat consumption for Georgia.
> 2. Identify the average daily meat consumption for Western Asia.
> 3. Add the values from steps 1 and 2.
>
> Step 1: From the provided chart, we see that the average daily meat consumption for Georgia is 79.84 grams per person per day.
> Step 2: From the chart, we see that the average daily meat consumption for Western Asia is 69.62 grams per person per day.
> Step 3: Add the values from steps 1 and 2.
> 79.84 g (Georgia) + 69.62 g (Western Asia) = 149.46 g
>
> So, the sum of average daily meat consumption for Georgia and Western Asia is 149.46 grams per person per day.

## Table 15

**Table 15.** Example prompt demonstrating GPT-4's visual input capability. The prompt consists of a question which requires understanding a physics problem with a diagram written in French and solving it using chain-of-thought prompting. [p. 35]

**Title:** GPT-4 visual input example, Ecole Polytechnique Exam Question

**User prompt:** Answer question I.1.a. Think step-by-step.

**Visual input:** A physics exam page in French titled "I. Principe de la detection de rayonnement avec un bolometre" (Principle of radiation detection with a bolometer). The page includes a diagram (Figure 1 - Schema d'un bolometre) showing a bolometer circuit with components: courant de polarisation (polarization current), rayonnement incident (incident radiation) with puissance P_0 (power P_0), an absorber with resistance R(T), capacite thermique C_th (thermal capacity), a barreau conducteur (conductive bar) of length L, section S, and thermal conductivity lambda, connected to a thermostat at temperature T_0.

Question I.1.a asks to express the temperature T(x) at every point of the conductive bar identified by its abscissa x, given T(0) = T_0 and T(L) = T_b.

**GPT-4 response:**
> To answer question I.1.a, we need to express the temperature T(x) in every point of the conductive bar, which is characterized by the abscissa x. We are given that T(0) = T0 and T(L) = Tb.
>
> For a stationary regime, the heat equation for the one-dimensional heat conduction in the bar is:
> d^2T/dx^2 = 0
>
> Integrating once, we get:
> dT/dx = C_1
>
> Integrating a second time:
> T(x) = C_1 x + C_2
>
> To determine the constants C_1 and C_2, we use the boundary conditions:
> T(0) = T0, which gives C_2 = T0
> T(L) = Tb, which gives C_1 = (Tb - T0)/L
>
> Finally, the expression for T(x) is:
> T(x) = (Tb - T0) * (x/L) + T0
> This represents a linear temperature profile along the conductive bar, with a slope of (Tb - T0)/L.

## Table 16

**Table 16.** Example prompt demonstrating GPT-4's visual input capability. The prompt requires image understanding. [p. 36]

**Title:** GPT-4 visual input example, Extreme Ironing

**User prompt:** What is unusual about this image?

**Visual input:** A photograph showing a man in a yellow shirt ironing clothes on an ironing board that is attached to the roof of a moving yellow taxi cab on a city street. Source: https://www.barnorama.com/wp-content/uploads/2016/12/03-Confusing-Pictures.jpg

**GPT-4 response:**
> The unusual thing about this image is that a man is ironing clothes on an ironing board attached to the roof of a moving taxi.

---
[p. 37–39 continued]

## Table 17

**Table 17.** Example prompt demonstrating GPT-4's visual input capability. [p. 37]

**Title:** GPT-4 visual input example, Pixel to Paper Summaries

**User prompt:** Below is part of the InstuctGPT paper. Could you read and summarize it to me?

**Visual input:** Multiple pages of the InstructGPT paper (Ouyang et al., 2022) titled "Training language models to follow instructions with human feedback," showing the paper's title, author list, abstract, figures, and body text.

**GPT-4 response:**
> The InstructGPT paper focuses on training large language models to follow instructions with human feedback. The authors note that making language models larger doesn't inherently make them better at following a user's intent. Large models can generate outputs that are untruthful, toxic, or simply unhelpful.
>
> To address this issue, the authors fine-tune language models on a wide range of tasks using human feedback. They start with a set of labeler-written prompts and responses, then collect a dataset of labeler demonstrations of the desired model behavior. They fine-tune GPT-3 using supervised learning and then use reinforcement learning from human feedback to further fine-tune the model. The resulting model, called InstructGPT, shows improvements in truthfulness and reductions in toxic output generation while having minimal performance regressions on public NLP datasets.
>
> The authors conclude that fine-tuning with human feedback is a promising direction for aligning language models with human intent.

**Follow-up exchange:**

User: Could you explain the process described in Figure 2?

GPT-4:
> Figure 2 in the InstructGPT paper illustrates the three steps of their method:
>
> 1. Supervised fine-tuning (SFT): They collect demonstration data, which consists of labeler-written prompts and desired output behavior. This data is used to fine-tune GPT-3 with supervised learning.
>
> 2. Reward model (RM) training: They collect comparison data, where a labeler ranks the outputs from several model samples (from best to worst). This data is used to train the reward model.
>
> 3. Reinforcement learning using Proximal Policy Optimization (PPO): They optimize a policy against the reward model using reinforcement learning. For each new prompt sampled from the dataset, the policy generates an output. The reward model calculates a reward for the output, and the reward is used to update the policy using the PPO algorithm.
>
> These three steps are iteratively performed to train the InstructGPT model, which aims to generate outputs that align better with human preferences and follow instructions more effectively.

## Table 18

**Table 18.** Example prompt demonstrating GPT-4's visual input capability. [p. 38]

**Title:** GPT-4 visual input example, Chicken Nugget Map

**User prompt:** Can you explain this meme?

**Visual input:** A meme image with text reading "Sometimes I just look at pictures of the earth from space and I marvel at how beautiful it all is." Below the text is a photograph of chicken nuggets arranged on a baking sheet to vaguely resemble a map of the world.

**GPT-4 response:**
> This meme is a joke that combines two unrelated things: pictures of the earth from space and chicken nuggets. The text of the meme suggests that the image below is a beautiful picture of the earth from space. However, the image is actually of chicken nuggets arranged to vaguely resemble a map of the world. The humor in this meme comes from the unexpected juxtaposition of the text and the image. The text sets up an expectation of a majestic image of the earth, but the image is actually something mundane and silly.

## Table 19

**Table 19.** Example prompt demonstrating GPT-4's visual input capability. [p. 39]

**Title:** GPT-4 visual input example, Moar Layers

**User prompt:** Can you explain why this is funny. Think about it step-by-step.

**Visual input:** A two-panel comic. The left panel is titled "STATISTICAL LEARNING" and shows a character saying: "People, our learner overgeneralizes because the VC-Dimension of our Kernel is too high. Get some experts and minimize the structural risk in a new one. Rework our loss function, make the next kernel stable, unbiased and consider using a soft margin." The right panel is titled "NEURAL NETWORKS" and shows a simpler character next to a graph with "LAYERS" on the x-axis, simply saying "STACK MORE LAYERS." Below is the caption "But unironically."

**GPT-4 response:**
> The comic is satirizing the difference in approaches to improving model performance between statistical learning and neural networks.
>
> In statistical learning, the character is shown to be concerned with overfitting and suggests a series of complex and technical solutions, such as minimizing structural risk, reworking the loss function, and using a soft margin.
>
> In contrast, the neural networks character simply suggests adding more layers to the model. This is often seen as a common solution to improving performance in neural networks, but it's also considered a simplistic and brute-force approach.
>
> The humor comes from the contrast between the complexity and specificity of the statistical learning approach and the simplicity and generality of the neural network approach. The "But unironically" comment adds to the humor by implying that, despite being simplistic, the "stack more layers" approach is often effective in practice.
