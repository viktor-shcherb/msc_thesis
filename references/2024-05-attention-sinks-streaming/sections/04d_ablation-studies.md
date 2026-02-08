# 4.4 Ablation Studies [p. 9]

## Numbers of Initial Tokens [p. 9]

In Table 2, the effect of adding varying numbers of initial tokens with recent tokens on the streaming perplexity is ablated. The results show the insufficiency of introducing merely one or two initial tokens, whereas a threshold of four initial tokens appears enough, with subsequent additions contributing marginal effects. This result justifies the choice of introducing 4 initial tokens as attention sinks in StreamingLLM. [p. 9]

## Cache Sizes [p. 9]

**Table 6** (p. 9): "Effects of cache size on StreamingLLM's performance. Increasing the cache size in StreamingLLM doesn't consistently yield a decrease in perplexity, showing these models may not fully utilize the provided context. Cache config $x$+$y$ denotes adding $x$ initial tokens with $y$ recent tokens. Perplexity is evaluated on 400K tokens in the concatenated PG19 test set."

| Cache | 4+252 | 4+508 | 4+1020 | 4+2044 |
|---|---|---|---|---|
| Falcon-7B | 13.61 | 12.84 | **12.34** | 12.84 |
| MPT-7B | **14.12** | 14.25 | 14.33 | 14.99 |
| Pythia-12B | 13.17 | 12.52 | **12.08** | 12.09 |

| Cache | 4+508 | 4+1020 | 4+2044 | 4+4092 |
|---|---|---|---|---|
| Llama-2-7B | 9.73 | 9.32 | **9.08** | 9.59 |

Contrary to intuition, increasing the cache size does not consistently lower the language modeling perplexity. This inconsistency shows a potential limitation where these models might not maximize the utility of the entire context they receive. Future research efforts should target enhancing these models' capabilities to utilize extensive contexts better. [p. 9]
