# 7 Future Work [p. 8]

[p. 8]

Several promising directions for future work on the RWKV architecture are identified:

1. **Increased model expressivity:** Work can be done to increase model expressivity by enhancing the time-decay formulations and exploring initial model states while maintaining efficiency.

2. **Improved computational efficiency:** The RWKV computational efficiency can be further improved by applying a parallel scan in the $wkv_t$ step to reduce the computational cost to $O(B \log(T) d)$.

3. **Encoder-decoder architectures:** The mechanisms used in RWKV can be applied to encoder-decoder architectures, potentially replacing the cross-attention mechanism. This could be applicable in seq2seq or multimodal settings, thereby enhancing efficiency during both training and inference.

4. **State leveraging:** RWKV's state (or *context*) can be leveraged for interpretability, predictability in sequence data, and safety. Manipulating the hidden state could also guide behavior and allow greater customizability through prompt tuning.

5. **Architecture improvements:** The RWKV architecture is not perfect, and can be improved via many aspects, such as modifying the formulae or implementing larger internal states. Larger states can enhance the model's memory to previous context and improve performance over various tasks.
