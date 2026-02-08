# System Card Section 5: Conclusion and Next Steps [p. 68–69]

[p. 68] OpenAI has implemented various safety measures and processes throughout the GPT-4 development and deployment process that have reduced its ability to generate harmful content. However, GPT-4 can still be vulnerable to adversarial attacks and exploits, or "jailbreaks," and harmful content is not the source of risk. Fine-tuning can modify the behavior of the model, but the fundamental capabilities of the pre-trained model, such as the potential to generate harmful content, remain latent. As capabilities and risks associated with them increase, it will become critical to achieve extremely high degrees of reliability in these and other interventions; even now, it is important to complement these model-level mitigations with other interventions like use policies and monitoring, as discussed in the section on System Safety.

In Figure 10, one exploit using adversarial system messages (which are intended to help set the behavior of the model) is shown. Adversarial system messages are one example of an exploit that can circumvent some of the safety mitigations of GPT-4-launch.

OpenAI will continue to learn from deployment and will update models to make them safer and more aligned. This will include incorporating lessons from real-world data and usage, including instances of adversarial system messages that are detected early in the process of ramping up model access. Additionally, there are a few key steps that are being taken and that other developers of language models are encouraged to adopt:

- **Adopt layers of mitigations throughout the model system:** As models get more powerful and are adopted more widely, it is critical to have multiple levels of defense, including changes to the model itself, oversight and monitoring of model usage, and product design for safe usage.

- **Build evaluations, mitigations, and approach deployment with real-world usage in mind:** Context of use such as who the users are, what the specific use case is, where the model is being deployed, etc., is critical to mitigating actual harms associated with language models and ensuring their deployment is as beneficial as possible. It is particularly important to account for real-world vulnerabilities, humans' roles in the deployment context, and adversarial attempts. Development of high quality evaluations and testing of model mitigations on datasets in multiple languages is especially encouraged.

- **Ensure that safety assessments cover emergent risks:** As models get more capable, we should be prepared for emergent capabilities and complex interactions to pose novel safety issues. It is important to develop evaluation methods that can be targeted at advanced capabilities that could be particularly dangerous if they emerged in future models, while also being open-ended enough to detect unforeseen risks. [p. 69]

- **Be cognizant of, and plan for, capability jumps "in the wild":** Methods like fine-tuning and chain-of-thought prompting could lead to capability jumps in the same base model. This should be accounted for explicitly in internal safety testing procedures and evaluations. And a precautionary principle should be applied: above a safety critical threshold, assurance of sufficient safety is required.

[p. 69] The increase in capabilities and adoption of these models have made the challenges and consequences of those challenges outlined in this card imminent. As a result, more research is especially encouraged into:

- Economic impacts of AI and increased automation, and the structures needed to make the transition for society smoother
- Structures that allow broader public participation into decisions regarding what is considered the "optimal" behavior for these models
- Evaluations for risky emergent behaviors, such as situational awareness, persuasion, and long-horizon planning
- Interpretability, explainability, and calibration, to address the current nature of "black-box" AI models. Research into effective means of promoting AI literacy to aid appropriate scrutiny to model outputs is also encouraged.

As noted above, both improved language model capabilities and limitations can pose significant challenges to the responsible and safe societal adoption of these models. To ensure that we are all well-prepared for the pace of progress, more research emphasis on areas such as AI literacy, economic and social resilience, and anticipatory governance is needed [11]. It is very important that OpenAI, other labs, and academia further develop effective evaluation tools and technical improvements in model safety. Progress has been made in the last few years, and more investment in safety will likely produce more gains.

Readers interested in this topic are encouraged to read OpenAI's work on language model impacts in areas such as disinformation, misuse, education, and economy and labor market.
