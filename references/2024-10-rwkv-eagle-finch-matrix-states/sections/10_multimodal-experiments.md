# Multimodal Experiments [p. 15–16]

[p. 15] In this section, we explore the capabilities of Eagle when extended to handle multimodal tasks, where the model processes and integrates textual inputs with inputs in a different domain.

## 10.1 RWKV Music Modelling

[p. 15] To investigate the Eagle architecture's applicability to music modeling, we use the Irishman ABC music sheet dataset (Wu et al., 2023) to train a new RWKV-5-Music model using the same hyperparameters as the existing RWKV-4-Music model with only the architecture changed. The loss of RWKV-5 is approximately 2% lower than that of the previous generation model, and this improvement is primarily observed in the musical score part, indicating that RWKV-5 possesses stronger modeling and generalization capabilities than its predecessor. The model has a total of L = 24 layers, with a dimension of D = 512 and uses a byte-level tokenizer with V = 128 tokens. The training context length is 1024 bytes. We use all 2,162 pieces of music in the validation set and calculate the loss for each position from the start. The loss is averaged across all pieces of music, then Gaussian smoothed over the position in the sequence.

[p. 15] The figure 8 shows the loss as a function of position. Note that the first 30-100 bytes of the ABC format are the file header and control codes, followed by the musical scores. The loss of RWKV-5 is approximately 2% lower than the previous generation model, and it is shown mainly in the musical score part, indicating that RWKV-5 has stronger modelling and generalization capabilities than its precedent model.

### Figure 8: Music Modelling Loss [p. 15]

**Figure 8:** Music modelling loss over sequence position.

The figure shows a line plot with:
- X-axis: Position from start (0 to 768)
- Y-axis: Loss (Bits/Byte) (ranging from ~0.4 to 0.8)
- Two lines plotted:
  - RWKV-4-Music (orange/yellow line)
  - RWKV-5-Music (red line)

Both models show a sharp spike in loss around position 0-128 (reaching ~0.8), then dropping and stabilizing around 0.45-0.55 for the remainder of the sequence. RWKV-5-Music consistently shows slightly lower loss than RWKV-4-Music in the musical score region (after position 128).

## 10.2 VisualRWKV

[p. 15] VisualRWKV is the visual-enhanced version of the RWKV language model, enabling RWKV to handle various visual tasks. Our VisualRWKV follows a similar architecture to popular vision-language models (Liu et al., 2023a). We present the architecture in Figure 9. It consists of a vision encoder and a language model. Specifically, we use CLIP (Radford et al., 2021) as the vision encoder and Eagle 1.5B and 3B as the language model. We use LLaVA-1.5 dataset (Liu et al., 2023a). To adapt Eagle to this multimodal task, we employ a two-stage instruction-tuning process to enhance model performance. Initially, we conduct pre-training for feature alignment, during which only the projection layer is subjected to updates, while the rest of the model is kept in a frozen state. Following this, we move on to the fine-tuning end-to-end stage, where both the projection layer and the RWKV language model are fine-tuned, and the vision encoder
