# 4 Related Work [p. 10–11]

## Retrieval-augmented LLM

[p. 10] One line of work extends LLMs by augmenting them with retrieval modules which fetch related documents and include the retrieval results into the input context of an LLM (Karpukhin et al., 2020; Guu et al., 2020; Izacard et al., 2022; Jiang et al., 2022; Khattab et al., 2021; Santhanam et al., 2022). The authors' work is complementary to these works as their extended context window allows more documents being included in the input. In addition, with an unmodified attention mechanism and model architecture, their method may be more versatile as it can natively handle tasks beyond retrieval oriented ones, such as long document summarization, few-shots learning, etc.

## Recurrent Transformers and Memory Transformers

[p. 11] Several works add memory capabilities to Transformers through recurrence, which increase the models' capability of handling very long sequences (Bulatov et al., 2022; Wu et al., 2020; Dai et al., 2019; Wu et al., 2022; Martins et al., 2021; Mu et al., 2023). One limitation of these works is that they only allow attending to a lossy compressed version of past inputs. Mu et al. (2023) suggested that this may prevent models from remembering specific details in the past inputs. In contrast, the authors' work allows attending to all previous tokens, preserving all details without compression, albeit with higher inference costs. Mohtashami & Jaggi (2023) proposed landmark attention which allows full random access to any chunk of the input through introducing landmark tokens. The authors' work allows full access of the entire input through unmodified attention, which may be useful for tasks such as summarization.

## Approximated Multi-head Attention

[p. 11] There is a large body of research that focuses on decreasing the memory and computational complexity of the multi-head attention (MHA) mechanism through approximation or sparsification (Child et al., 2019; Zaheer et al., 2020; Beltagy et al., 2020; Wang et al., 2020; Choromanski et al., 2021; Kitaev et al., 2020; Ren et al., 2021). Although not the focus of this work, as these methods are not used in LLaMA (Touvron et al., 2023), the authors note that their method is compatible with most of them since their changes are restricted to position encodings, and not attention mechanisms.

## Length Extrapolation

[p. 11] A recent line of research aims to train Transformers models on short sequences and inference on longer (Press et al., 2022; Sun et al., 2022; Haviv et al., 2022). However, these methods have not been applied in some of the largest language models such as LLaMA (Touvron et al., 2023) or OPT (Zhang et al., 2022). This has prevented them from enabling length extrapolation of many pre-existing pre-trained language models. The authors' work focuses on extending existing LLMs, which can save substantial pre-training costs. In addition, their method preserves the quality of the original models, even for small context window tasks, since it does not deviate far from existing definitions of position encoding or attention mechanisms.

## Interpolation

[p. 11] The most related technique is proposed by Dosovitskiy et al. (2021) in their work on Vision Transformers, where the authors proposed to linearly interpolate learnt position embeddings to support higher resolution, which translates to an increased number of input embeddings, in the fine-tuning stage. The interpolated position embedding weights are used as initialization in the fine-tuning process for the newly added positions.

The current work differs from Dosovitskiy et al. (2021) in several ways [p. 11]:
1. Instead of interpolating position embeddings, this method interpolates position indices, which is more suitable for RoPE like position encodings and may require less training since no trainable parameters are added.
2. The authors report successful results of extending the context window to 32 times while Dosovitskiy et al. (2021) explored up to 4 times. Their results extend theirs in exploring the upper limit of context window extension via interpolation.
3. They evaluated and confirmed the effectiveness of Position Interpolation for extending context windows for language models.

> "We believe our results, in conjunction with (Dosovitskiy et al., 2021), provide empirical evidence on Transformer's remarkable ability of handling significantly longer sequences beyond training." [p. 11]

Further, the authors conjecture that a method similar to theirs is directly applicable in LLMs with learnable position embeddings such as OPT (Zhang et al., 2022) and they plan to investigate this in the future. [p. 11]
