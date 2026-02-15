# 2 Approach [p. 3-6]

## 2.1 Model Architecture [p. 3]

The architecture of Kimi-VL consists of three parts: a native-resolution vision encoder (MoonViT), an MLP projector, and an MoE language model, as depicted in Figure 3. We introduce each part in this section.

**Figure 3** (p. 3): "The model architecture of Kimi-VL and Kimi-VL-Thinking, consisting of a MoonViT that allows native-resolution images, an MLP projector, and a Mixture-of-Experts (MoE) language decoder."

Description: Architecture diagram
- Key elements: Three main components shown: (1) MoonViT (Native-resolution) vision encoder in center processing various input types (SMALL IMAGE shown as 8x2=8 pixel, LONG VIDEO, FINE-GRAINED images including tea plantation and phone screen, OCR text snippets), (2) MLP Projector connecting vision to language, (3) Mixture-of-Experts (MoE) Language Decoder at top with Router, Attention Layer, and MoE FFN components. Shows "<think> The user asked..." prompt example and visual tokens flowing through system with N×N grid representations
- Notable patterns: Demonstrates multi-resolution input handling (small images, long videos, fine-grained high-res images), routing mechanism in MoE, bidirectional flow between components
- Supports claim: Illustrates the three-part architecture enabling native-resolution processing and efficient MoE computation

### MoonViT: A Native-resolution Vision Encoder [p. 3]

We design MoonViT, the vision encoder of Kimi-VL, to natively process images at their varying resolutions, eliminating the need for complex sub-image splitting and splicing operations, as employed in LLaVA-OneVision (B. Li et al. 2024). We incorporate the packing method from NaViT (Dehghani et al. 2023), where images are divided into patches, flattened, and sequentially concatenated into 1D sequences. These preprocessing operations enable MoonViT to share the same core computation operators and optimization as a language model, such as the variable-length sequence attention mechanism supported by FlashAttention (Dao et al. 2022), ensuring non-compromised training throughput for images of varying resolutions.

MoonViT is initialized from and trained on top of SigLIP SO-400M (Zhai et al. 2023), which originally employs learnable fixed-size absolute positional embeddings to encode spatial information. While we interpolate these original position embeddings to better preserve SigLIP's capabilities, the interpolated embeddings become increasingly inadequate as image resolution increases. To address this limitation, we incorporate 2D rotary positional embedding (RoPE) (J. Su et al. 2023) across the height and width dimensions, which improves the representation of fine-grained spatial information, especially in high-resolution images. These two positional embedding approaches work together to encode spatial information for our model and seamlessly integrate with the flattening and packing procedures. This integration enables MoonViT to efficiently process batches of varying resolutions within the same batch. The resulting continuous image features are then forwarded to the MLP projector and, ultimately, to the MoE language model. After subsequent training phases of Kimi-VL (Kimi-VL-Thinking-2506), we then continually train this MoonViT to authentically encode up to 3.2 million pixels from a single image, 4 times compared to the original limit.

### MLP Projector [p. 3-4]

We employ a two-layer MLP to bridge the vision encoder (MoonViT) and the LLM. Specifically, we first use a pixel shuffle operation to compress the spatial dimension of the image features extracted by MoonViT, performing 2×2 downsampling in the spatial space while correspondingly expanding the channel dimension. We then feed the pixel-shuffled features into a two-layer MLP to project them into the dimension of LLM embeddings.

### Mixture-of-Experts (MoE) Language Model [p. 4]

The language model of Kimi-VL utilizes our Moonlight model (J. Liu et al. 2025a), an MoE language model with 2.8B activated, 16B total parameters, and an architecture similar to DeepSeek-V3 (DeepSeek-AI, A. Liu, et al. 2025). For our implementation, we initialize from an intermediate checkpoint in Moonlight's pre-training stage—one that has processed 5.2T tokens of pure text data and activated an 8192-token (8K) context length. We then continue pre-training it using a joint recipe of multimodal and text-only data totaling 2.3T tokens, as detailed in Sec. 2.3.

## 2.2 Muon Optimizer [p. 4]

We use an enhanced Muon optimizer (J. Liu et al. 2025b) for model optimization. Compared to the original Muon optimizer (Jordan et al. 2024), we add weight decay and carefully adjust the per-parameter update scale. Additionally, we develop a distributed implementation of Muon following the ZeRO-1 (Rajbhandari et al. 2020) optimization strategy, which achieves optimal memory efficiency and reduced communication overhead while preserving the algorithm's mathematical properties. This enhanced Muon optimizer is used throughout the entire training process to optimize all model parameters, including the vision encoder, the projector, and the language model.
