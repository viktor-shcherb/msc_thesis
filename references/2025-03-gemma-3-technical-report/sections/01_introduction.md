# Introduction [p. 1]

Gemma 3 is the newest version of Gemma open language models (Gemma Team, 2024a), co-designed with the family of Gemini frontier models (Gemini Team, 2023). This new version comes in sizes comparable to Gemini 2.0 (Gemma Team, 2024b), with the addition of a 1B model. These models are designed to run on standard consumer-grade hardware such as PCs, laptops, and high-end GPUs. This version comes with several new abilities to the Gemma family; namely, multimodality, long context, and multilinguality, while preserving or surpassing the performance of prior versions.

## Multimodality

In terms of multimodality, most Gemma 3 models are compatible with an interleaved text and SigLIP vision encoder (Zhai et al., 2023). The language models treat images as a sequence of soft tokens encoded by SigLIP. The authors reduce the inference cost of image processing by condensing the vision embeddings into a fixed size of 256 vectors. The encoder works at original resolution and the authors take inspiration from LLaVA (Liu et al., 2024) to enable flexible resolutions with a Pan and Scan (P&S) method.

## Architecture improvements for long context

The second main architectural improvement is an increase in context size to 128K tokens, without reducing performance. A challenge with long context is the memory explosion in the KV cache during inference. To reduce this issue, the authors interleave multiple local layers between each global layer, and assign a smaller span of only 1024 tokens to the local layers. Therefore, only the global layers attend to long context, and they have 1 global for every 5 local layers.

## Pre-training

The pre-training optimization recipe is similar to Gemma 2, with some modifications in the architecture design. The authors use the same tokenizer as Gemini 2.0, and expand their data mixture to improve the multilingual capabilities of the models, while introducing image understanding. All Gemma 3 models are trained with knowledge distillation (Hinton et al., 2015).

## Post-training

In post-training, the authors focus their efforts on improving mathematics, reasoning, and chat abilities, as well as integrating the new capabilities of Gemma 3, long-context, and image inputs. The authors use a novel post-training approach that brings gains across all capabilities including math, coding, chat, instruction following, and multilingual. The resulting Gemma 3 instruction-tuned models are both powerful and versatile, outperforming their predecessors by a wide margin.

## Overview of the report

In the following sections, the authors provide a brief overview of the models, including the architecture and pre- and post-training recipes. They also provide detailed evaluations across a wide variety of quantitative and qualitative benchmarks. The authors discuss their approach to safe and responsible deployment and outline the broader implications of Gemma 3, its limitations, and advantages.
