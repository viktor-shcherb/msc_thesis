# 5.2.2. Realistic Long-Context Evaluations (continued) [p. 24–26]

## 5.2.2.6 Long-context Video QA

[p. 24–25] The authors next proceed to long video question answering evaluation to test Gemini 1.5's efficacy on long-context video understanding. Question-answering benchmarks for long-context video understanding need to have at least two properties: first, they need to contain long videos and second, their questions need to be designed in a way that can differentiate among models that operate over different context lengths. Unfortunately, no existing benchmarks satisfy these properties for evaluating models that can handle hours-long videos like Gemini 1.5 models. The publicly available question answering benchmark with the longest videos is EgoSchema (Mangalam et al., 2023), but its videos are at most 3 minutes (i.e., 180 frames) in length. [p. 24]

### 1H-VideoQA benchmark

[p. 24] To bridge this evaluation gap, the authors introduce a new benchmark, **1H-VideoQA**, composed of 125 five-way multiple-choice questions over public videos 40-105 minutes long.

Annotations are collected that require understanding one or multiple events, each spanning only a few seconds from the full video so that the answer is extremely challenging to infer by looking at a few randomly sampled video frames. [p. 24]

### Experimental setup

[p. 24–25] Experiments are run by extracting video frames at one frame-per-second, and further linearly subsampling long videos to a fixed context length. Performance is also measured if all frames for each video are provided to Gemini 1.5 models. Results are shown in Figure 15 and Table 9. [p. 24–25]

### EgoSchema vs 1H-VideoQA

[p. 25] Figure 15 illustrates the improvement of 1H-VideoQA over EgoSchema in terms of its ability to differentiate among models that operate over different numbers of frames. Gemini 1.5 Pro sets a new state-of-the-art of 70.2% accuracy on EgoSchema using only 16 frames (vs 55.6% for GPT-4V (Balazevic et al., 2024)). However, no clear gains are seen from going to 150 frames, suggesting that many questions in EgoSchema can be easily solved with a limited number of frames. [p. 25]

In contrast, on 1H-VideoQA the performance of Gemini 1.5 Pro consistently increases as the number of frames provided increases from the first frame to the full video, suggesting that a substantial proportion of questions in 1H-VideoQA can only be solved with more frames as context, thereby making 1H-VideoQA more effective as a long-context benchmark. [p. 25]

**Figure 15** (p. 24): "Comparison between 1H-VideoQA and EgoSchema, reporting Gemini 1.5 Pro's accuracy when linearly subsampling to 1, 16, or 150 frames. We also show performance if we provide all the frames for each video for 1H-VideoQA, in yellow. Gemini 1.5 Pro achieves SotA accuracy on both benchmarks. Gemini 1.5 Pro's performance on 1H-VideoQA keeps increasing as we scale up to providing all frames in the video, while its performance on EgoSchema saturates after 16 frames, showing that 1H-VideoQA is more effective at differentiating among models that operate over different context lengths. *When provided with the first frame only, Gemini 1.5 Pro tends to avoid using one of the choices and instead indicates it lacks information to reply accurately."
- Grouped bar chart with y-axis "Accuracy" (0.0 to 1.0) and x-axis showing two datasets.
- A horizontal dashed line at 0.2 labeled "Random Baseline".
- Legend: First frame (blue), Linearly subsampled to 16 frames (green), Linearly subsampled to 150 frames (red), All frames (1 fps) (yellow).
- **1H-VideoQA (40-105 minutes):**
  - First frame: 0.238* (below random baseline; asterisk indicates model avoids answering)
  - 16 frames: 0.452
  - 150 frames: 0.563
  - All frames (1 fps): 0.722
- **EgoSchema (3 minutes):**
  - First frame: 0.536
  - 16 frames: 0.702
  - 150 frames: 0.727
  - (No "All frames" bar shown for EgoSchema)

### Comparison with GPT-4V

[p. 25] Table 9 further shows that Gemini 1.5 Pro consistently outperforms GPT-4V on 1H-VideoQA, whether the video has been subsampled to 16 or to 150 frames. The fact that Gemini 1.5 Pro does not solve 1H-VideoQA perfectly, despite observing a frame every second (see examples in Appendix, Table 47), makes 1H-VideoQA a useful benchmark for evaluating and driving the development of future long-context video models. The authors additionally highlight the quality of Gemini 1.5 Flash, which is only slightly behind GPT-4V with 150 frames, and even better than GPT-4V with 16 frames, despite being significantly smaller and more efficient. [p. 25]

**Table 9** (p. 25): Comparison between GPT-4V and Gemini 1.5 models on 1H-VideoQA. Experiments are run zero-shot, by sampling one video frame-per-second and linearly subsampling 16 or 150 frames. Also shows performance if all the frames for each video are provided to Gemini 1.5 models.

| Model | Frames: 16 | Frames: 150 | full video (1 fps) |
|---|---|---|---|
| GPT-4V | 36.5% | 52.3% | Not supported |
| Gemini 1.5 Pro | **45.2%** | **56.3%** | **72.2%** |
| Gemini 1.5 Flash | 39.7% | 50.8% | 65.9% |

Note: Bold values indicate the best score in each column.

## 5.2.2.7 In-Context Planning

[p. 25–26] Reasoning and planning are fundamental human skills for problem-solving and decision-making. While LLMs have demonstrated recent progress in reasoning tasks, planning remains a more challenging area which so far has received limited attention. In this section, performance of models is reported on both classical planning benchmarks expressed in the standard Planning Domain Definition Language (PDDL) and more modern ones expressed in natural language. See Appendix 12.8 for example of prompts for all planning tasks considered in this section. [p. 25]

### Evaluation approach

[p. 25] The planning capability of the model is evaluated as more examples ("shots") are added into the context, inspired by the success of many-shot learning across a large number of tasks (Agarwal et al., 2024a). The challenge in "in-context planning" involves understanding a specific task and problem through a limited number of examples. Additionally, it requires the models to produce a solution without checking each planning step to confirm if a proposed move is correct. The model has to create a plan in one go. To humans, this might be seen as thinking fast (instead of slow). [p. 25]

### Overall results

[p. 25–26] Figure 16 shows the in-context learning performance on classical planning and natural language benchmarks as the number of shots is varied. Overall, Gemini 1.5 Pro outperforms other models indicating that the model not only can plan better with a fewer number of examples/shots, it can also make effective use of additional and longer context. Gemini 1.5 Flash which is a smaller, faster and more efficient model is outperformed by Gemini 1.5 Pro but occasionally matching GPT-4 Turbo performance. [p. 25–26]

**Figure 16** (p. 26): "PDDL Planning and Natural Language Planning with few-shots. In all benchmarks, Gemini 1.5 Pro outperforms other models indicating that the model not only can plan better with a fewer number of examples, it can also make effective use of a longer context."
- Five subplots arranged in a 3+2 grid, each showing Planning Accuracy (%) on y-axis and Few-shot exemplars (log scale) on x-axis:
  - Each subplot also has a secondary x-axis at the top showing "Sentence pieces in 1000 (log scale)".
  - Three models: Gemini 1.5 Flash (green), Gemini 1.5 Pro (blue), GPT-4 Turbo 20240409 (orange/yellow).
  - Error bars represent a 70% CI.
- **(a) BlocksWorld:** x-axis from 1 to 200 shots. Gemini 1.5 Pro reaches ~48% at 40 shots, ~35% at 1-shot. Flash reaches ~26% at 1-shot. GPT-4 Turbo near zero at 1-shot, peaks at ~43% at 200 shots.
- **(b) Logistics:** x-axis from 1 to 600 shots. Gemini 1.5 Pro leads with steady improvement. GPT-4 Turbo and Flash lower.
- **(c) Mini-Grid:** x-axis from 1 to 600 shots. Gemini 1.5 Pro leads, highest accuracy among the three.
- **(d) Trip Planning:** x-axis from 1 to 600 shots. Gemini 1.5 Pro consistently outperforms. Flash and GPT-4 Turbo roughly comparable.
- **(e) Calendar Scheduling:** x-axis from 1 to 600 shots. Gemini 1.5 Pro leads. GPT-4 Turbo and Flash follow.

### BlocksWorld

[p. 26] BlocksWorld is a well-known planning problem from International Planning Conference (IPC).^18 This domain consists of a set of blocks, a table and a robot hand. The goal is to find a plan to move from one configuration of blocks to another. BlocksWorld problem instances of 3 to 7 blocks are generated. Figure 16a shows the performance of Gemini 1.5 models on this benchmark as the number of few-shot examples increases. The 1-shot planning capability of Gemini 1.5 Pro and Gemini 1.5 Flash reaches 35% and 26%, while GPT-4 Turbo performance is close to zero. Moreover the 40-shots planning capability of Gemini 1.5 Pro reaches 48% range which performs better than the best (200-shots) performance of GPT-4 Turbo, which peaks at 43%. [p. 26]

> ^18 https://github.com/potassco/pddl-instances/tree/master/ipc-2000

### Logistics

[p. 26–27] Logistics is an AI planning problem from IPC-1998^19 expressed in PDDL that involves arranging the delivery of packages to their destinations using trucks within cities and airplanes between cities. The aim is to optimize transportation modes under constraints like vehicle capacities and locations, showcasing the model's ability to manage multi-step logistics efficiently. The planning capability of Gemini 1.5 models on the Logistics benchmark is shown in Figure 16b. The 1-shot planning capability of Gemini 1.5 Pro reaches 43% while GPT-4 Turbo can only reach to 18%. Moreover for Gemini 1.5 Pro more context leads to consistently better results, indicating that the model can make effective use of additional and longer context. This is not the case for GPT-4 Turbo where the accuracy drops when more examples are provided. [p. 26–27]

> ^19 https://github.com/potassco/pddl-instances/tree/master/ipc-1998

### Mini-Grid

[p. 27] In Mini-Grid problem from Artificial Intelligence Planning Systems (AIPS)-1998^20, also expressed in PDDL, various floorplans are created with rooms containing random configurations of key shapes. The goal then is for a robot to navigate from an initial position to a designated goal cell. Figure 16c shows the performance of Gemini 1.5 models as the number of few-shot examples increases. The 1-shot planning capability of Gemini 1.5 Pro reaches 28% while GPT-4 Turbo achieved only 15%. More context leads to better performance for Gemini 1.5 Pro. With 400-shots Gemini 1.5 Pro reached 77% accuracy. GPT-4 Turbo performance is also increasing with the increasing number of shots but it is far behind Gemini 1.5 Pro. With 80-shots GPT-4 Turbo reaches 38% accuracy which is 32% lower than the accuracy of Gemini 1.5 Pro. Gemini 1.5 Flash is outperformed by Gemini 1.5 Pro but almost matching GPT-4 Turbo performance. [p. 27]

> ^20 https://github.com/AI-Planning/pddl-generators/tree/main/minigrid

### Trip Planning

[p. 27] Trip Planning is a task focusing on planning a trip itinerary under given constraints where the goal is to find the itinerary regarding the order of visiting N cities. Enough constraints are added such that there is only one solution to the task, which makes the evaluation of the predictions straightforward. Figure 16d shows the performance of Gemini 1.5 Pro on this benchmark as the number of few-shot examples increases. The 1-shot performance of the GPT-4 Turbo model seems to be better than the Gemini 1.5 Pro. However, as the number of shots increases the performance of Gemini 1.5 Pro improves dramatically. With 100-shots Gemini 1.5 Pro reaches 42% while the best (20-shots) performance of GPT-4 Turbo is 31%. [p. 27]

### Calendar Scheduling

[p. 27] Calendar Scheduling is a task to schedule a meeting of either 30 minutes or an hour among up to 7 attendees. The attendees may have a busy schedule or a light schedule with less than half of the working hours spent in meetings. The planning capability of Gemini 1.5 Pro on this benchmark is shown in Figure 16e. The 1-shot planning capability of Gemini 1.5 Pro reaches 33% while GPT-4 Turbo's accuracy is under 10%. It also seems that more context leads to better performance for both Gemini 1.5 and GPT-4 Turbo models. With 40-shots GPT-4 Turbo achieves 36% accuracy while Gemini 1.5 Pro reaches 48%. With 100-shots the Gemini 1.5 Pro is able to reach 52% indicating that the model can make effective use of the longer context. [p. 27]

### Planning summary

[p. 27] *In summary*, planning empowers intelligent agents to look ahead and proactively determine a course of action to reach objectives (Russell and Norvig, 2016). Recently prompting LLMs to extract common sense knowledge gained attention (Ding et al., 2023; Huang et al., 2022; Singh et al., 2023) and effectiveness of LLMs in generating plans has been studied in (Guan et al., 2024; Hao et al., 2023; Valmeekam et al., 2024). Even though existing work finds current models to be incapable of few-shot planning, the results confirm that Gemini 1.5 Pro can perform well even in 1-shot setting while making effective use of additional and longer context to further improve performance. Since planning is at the core of robotics, embodied environments, and agentic space, leveraging this model capability in such applications has a great potential. [p. 27]

## 5.2.2.8 Unstructured Multimodal Data Analytics Task

[p. 28] While performing data analytics on structured data is a very mature field with many successful methods, the majority of real-world data exists in unstructured formats like images and conversations. The authors investigate the potential of Large Language Models (LLMs) to enable unstructured data analytics and explore how LLMs can directly analyze this vast pool of multimodal information.

As an instance of unstructured data analytics, an image structuralization task is performed. LLMs are presented with a set of 1024 images with the goal of extracting the information that the images contain into a structured data sheet (see Appendix 12.7 for examples of prompts used in this study). As this is a long-context task, in case where context length of models does not permit processing of all the images at once, mini-batches with different batch sizes are used to alleviate this shortcoming. In the end, the results of each mini-batch are concatenated to form the final structured table. [p. 28]

**Figure 17** (p. 28): "Performance of models on unstructured data analytics tasks."
- Left side: Illustration of the task setup. Input is "A batch of images" (a grid of thumbnail images). A text prompt reads "Please process the following images... Image_0 <base64 string> Image_1 <base64 string> Image_2 <base64 string>... Please output the table only in the format specified." Output is a structured table with columns: ID, Category, Color, Semantic Attribute.
- Right side: Line chart titled "Accuracy on all the attributes extraction" with y-axis "Accuracy (%)" (10 to 45) and x-axis "Batch Size" (8, 16, 32, 64, 128, 256, 512).
  - Gemini 1.5 Pro (blue): starts at ~38% at batch size 8, stays roughly flat or slightly increasing, reaching ~40% at batch size 512. Consistently highest performer.
  - GPT-4 Turbo 20240409 (green/olive): starts at ~30% at batch size 8, stays roughly flat around 30%, slight decline at larger batch sizes.
  - Claude 3 Opus (orange): starts at ~28% at batch size 8, drops sharply after batch size 16-32, reaching ~10% at batch size 64 (capped at 20 images).
- Claude 3 API is not able to analyze more than 20 images at the time of evaluation, which is why results for Claude 3 Opus are capped.

### Results

[p. 28] Figure 17 presents the results in terms of accuracy for different types of information extracted from images. The findings are:

- The accuracy on all attributes extraction of Gemini 1.5 Pro is improved by 9% (absolute) or 27% (relative compared to GPT-4 Turbo's accuracy). At the time of evaluation, Claude 3 API is not able to analyze more than 20 images which is why the results for Claude 3 Opus are capped.
- For Gemini 1.5 Pro more images lead to consistently better results, indicating that the model can make effective use of the additional and longer context. This is not the case for GPT-4 Turbo where the accuracy drops as more images are provided. [p. 28]
