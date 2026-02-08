# 4. Training Infrastructure and Dataset [p. 7]

[p. 7] Like Gemini 1.0 series, Gemini 1.5 models are trained on multiple 4096-chip pods of Google's TPUv4 accelerators, distributed across multiple datacenters, and on a variety of multimodal and multilingual data.

**Pre-training dataset:**
- Data sourced across many different domains, including web documents and code
- Incorporates image, audio, and video content

**Instruction-tuning phase:**
- Gemini 1.5 models finetuned on a collection of multimodal data containing paired instructions and appropriate responses
- Further tuning based on human preference data

The authors refer readers to the Gemini 1.0 Technical Report (Gemini-Team et al., 2023) for further information.
