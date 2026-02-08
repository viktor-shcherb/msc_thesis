# 4.2 Supervised Finetuning [p. 31]

[p. 31] Post-training begins with a supervised finetuning phase using the SFT mixture (Section 4.1.3). Training hyperparameters:

- **Global batch size:** 512 and 1,024
- **Learning rates:** 5 x 10^-6 and 2 x 10^-6, respectively
- **Learning rate schedule:** linear decay
- **Maximum sequence length:** 4,096 tokens
- **Optimizer:** AdEMAMix (Pagliardini et al., 2025) with beta_3 = 0.99, alpha = 8.0, and both t_{beta_3} and t_alpha set to the total number of training steps
- **Default values:** beta_1 = 0.9 and beta_2 = 0.999

## 4.2.1 Format and Chat Template [p. 31]

[p. 31–32] The chat template design builds upon the common practice of using special tokens to clearly delineate user and system prompts. This structured methodology is extended by also encapsulating assistant messages and introducing a novel *developer* message, each within unique start and end tokens. This dedicated *developer* message is used to define the available tools, their parameters, and other contextual configurations for the model. The resulting format is highly general and flexible, engineered for both simple dialogue and complex, multi-step agentic workflows involving reasoning and tool use. A complete specification of the format, along with a convenient Python library for its implementation, is available in the public GitHub repository.^42

---

**Footnotes:**
- ^42: https://github.com/swiss-ai/apertus-format
