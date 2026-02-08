# Limitations [p. 12–13]

## Limited Functionality [p. 12]

[p. 12] The proposed model series has not yet been finetuned for a wide range of long-context applications, such as creative writing that requires long-form outputs. Applying existing alignment recipes, e.g., RLHF, for various scenarios is expensive and nontrivial. Even skilled annotators may struggle to process the intricate details in dense texts. The authors consider developing efficient alignment methods for long LLMs to be a very valuable direction for future research.

## Tokenizer Efficiency [p. 13]

[p. 13] While the proposed model series can consume contexts up to 32,768 tokens, the actual number of words the model can take is largely affected by the tokenizer behaviour. The tokenizer used by the Llama series has a relatively small vocabulary (32k symbols) and often produces longer sequences compared to the sequences given by GPT-3.5's tokenizer -- the authors observe their tokenizer often produces 10% more tokens on average. Additionally, the tokenizer cannot efficiently handle whitespace, making it inefficient to process long code data.

## Hallucination [p. 13]

[p. 13] Like other LLMs, hallucination issues have been observed when testing the proposed model. While this issue is common for short-context models, tackling with this problem for long-context models can be more pronounced because of the dense information they consume and the insufficient alignment process.
