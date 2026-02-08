# Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity

**Authors:** William Fedus*, Barret Zoph*, Noam Shazeer (* Equal contribution)
**Affiliations:** Google, Mountain View, CA 94043, USA
**Venue:** Journal of Machine Learning Research 23 (2022) 1-40
**Submitted:** 8/21; Revised 3/22; Published 4/22
**Editor:** Alexander Clark

## Abstract

> "In deep learning, models typically reuse the same parameters for all inputs. Mixture of Experts (MoE) models defy this and instead select *different* parameters for each incoming example. The result is a sparsely-activated model---with an outrageous number of parameters---but a constant computational cost. However, despite several notable successes of MoE, widespread adoption has been hindered by complexity, communication costs, and training instability. We address these with the introduction of the Switch Transformer. We simplify the MoE routing algorithm and design intuitive improved models with reduced communication and computational costs. Our proposed training techniques mitigate the instabilities, and we show large sparse models may be trained, for the first time, with lower precision (bfloat16) formats. We design models based off T5-Base and T5-Large (Raffel et al., 2019) to obtain up to 7x increases in pre-training speed with the same computational resources. These improvements extend into multilingual settings where we measure gains over the mT5-Base version across all 101 languages. Finally, we advance the current scale of language models by pre-training up to trillion parameter models on the 'Colossal Clean Crawled Corpus', and achieve a 4x speedup over the T5-XXL model." [p. 1]

**Keywords:** mixture-of-experts, natural language processing, sparsity, large-scale machine learning, distributed computing

**Code:**
1. JAX code for Switch Transformer and all model checkpoints: `https://github.com/google-research/t5x`
2. Tensorflow code: `https://github.com/tensorflow/mesh/blob/master/mesh_tensorflow/transformer/moe.py`

## Section headings

1. Introduction
2. Switch Transformer
   - 2.1 Simplifying Sparse Routing
   - 2.2 Efficient Sparse Routing
   - 2.3 Putting It All Together: The Switch Transformer
   - 2.4 Improved Training and Fine-Tuning Techniques
3. Scaling Properties
   - 3.1 Scaling Results on a Step-Basis
   - 3.2 Scaling Results on a Time-Basis
   - 3.3 Scaling Versus a Larger Dense Model
4. Downstream Results
   - 4.1 Fine-Tuning
   - 4.2 Distillation
   - 4.3 Multilingual Learning
5. Designing Models with Data, Model, and Expert-Parallelism
   - 5.1 Data Parallelism
   - 5.2 Model Parallelism
   - 5.3 Model and Data Parallelism
   - 5.4 Expert and Data Parallelism
   - 5.5 Expert, Model and Data Parallelism
   - 5.6 Towards Trillion Parameter Models
6. Related Work
7. Discussion
8. Future Work
9. Conclusion
Acknowledgments
A. Switch for Attention
B. Preventing Token Dropping with *No-Token-Left-Behind*
C. Encouraging Exploration Across Experts
D. Switch Transformers in Lower Compute Regimes
E. Relation of Upstream to Downstream Model Performance
F. Pseudo Code for Switch Transformers
References
