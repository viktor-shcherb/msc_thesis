# RWKV World Tokenizer [p. 8–9]

[p. 8] Tokenization is important in language modelling as it conditions the learning relationships between tokens and the generation of new text based on those patterns. The numbers of tokens to build a single semantic chunk are, however, often very unequally distributed against non-European and other underrepresented languages. Byte-pair encoding (BPE) based tokenizers which are trained with this inequality result in not only lower performances against underrepresented languages but also undue economic costs such as of APIs (Petrov et al., 2024) and continual pre-training with extended vocabulary Lin et al. (2024); Sasaki et al. (2023). To address these problems, we manually select tokens from multiple vocabulary files such that non-European languages are well represented.

[p. 8–9] To construct the tokenizer's vocabulary, we merge the vocabularies of the following tokenizers and then manually select the tokens for non-European languages.

• **GPT-NeoX-20B (Black et al., 2022):** https://huggingface.co/EleutherAI/gpt-neox-20b
• **GPT2 (Radford et al., 2019):** https://huggingface.co/openai-community/gpt2
• **cl100k_base of tiktoken:** https://github.com/openai/tiktoken
• **Llama2 (Touvron et al., 2023):** https://huggingface.co/meta-llama/Llama-2-7b-hf
• **Bloom (Workshop et al., 2023):** https://huggingface.co/bigscience/bloom

[p. 9] This tokenizer has a vocabulary size of V = 65536, numbered from 0 through 65535, where tokens are arranged by their lengths in bytes. Below is a brief overview:

• **Token 0:** Represents the boundary between text documents, known as <EOS> or <SOS>. This token doesn't encode any specific content and is only used for document separation.
• **Tokens 1-256:** Consist of byte encodings of the UTF-8 token (token k encodes byte k−1), wherein tokens 1-128 correspond to standard ASCII characters.
• **Tokens 257-65529:** Tokens with a minimum length of 2 bytes in UTF-8, including words, prefixes and suffixes, accented letters, Chinese characters, Hangul, Hiragana, Katakana and emojis. For example, Chinese characters are allocated from token 10250 to 18493.
• **Token 65530-65535:** Reserved tokens for future use.

[p. 9] These designations are intended to enhance the tokenizer's efficiency on the multilingual corpus, as well as on source code of programming languages.

[p. 9] This tokenizer is implemented via a Trie (Prefix Tree) to boost speed while maintaining simplicity. Encoding is performed as matching the longest element in vocabulary with an input string from left to right. We note that our tokenizer is designed to mitigate the undue burden, which naive BPE and related methods cause, on minor languages.
