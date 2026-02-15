# 2.2 Related Works [p. 3–4]

## Modifications to RoPE Base Wavelength

A number of works have investigated how different modifications of RoPE affect its generalisation. A well-known method involves increasing the parameter θ from the originally proposed 10,000 to a larger value, such as 500,000 (Xiong et al., 2023; Roziere et al., 2023). Notably, this is also used in the recently released LLama 3 class of models (Dubey et al., 2024). The justification provided for this modification is that a higher base wavelength means that the attention decay induced by RoPE will be slower, allowing for more robust learning with larger contexts. In this work, we challenge this common assumption and investigate why RoPE and modifications such as these are helpful [p. 4].

## NoPE and Out-of-Distribution Performance

In a different direction, works have pointed out that NoPE shows strong performance in *out-of-distribution* (OOD) settings when compared to noting that the causal mechanism is sufficient to learn positional information (Haviv et al., 2022; Kazemnejad et al., 2024)⁴. In this work, we instead argue that NoPE and RoPE have *complementary* strengths and that for instance NoPE is unable to learn certain types of attention matrices present in Gemma 7B [p. 4].

## Randomised Positional Encodings

Ruoss et al. (2023) propose to provide *randomised* positional embeddings, claiming that this helps boost OOD performance, claiming that this helps the model to learn over a longer range of relative distances. In our work (Appendix, Section B.3), we provide an alternative explanation as to why this kind of process might be helpful from the point of view of the type of invariance it encourages [p. 4].

## Mechanistic Understanding of LLMs

Overall, we believe this work provides a different and perhaps more nuanced perspective on different works that tackle positional encodings. In spirit, this work is similar to works that aim to understand LLMs from a mechanistic perspective (Elhage et al., 2021; Olsson et al., 2022; Wang et al., 2022; Hanna et al., 2024) and from the representation learning they produce (Barbero et al., 2024; Veličković et al., 2024). In the Appendix (Section B), we provide additional discussions on related works [p. 4].

---

⁴Some works have argued that instead NoPE's extrapolation ability is still limited (Dong et al., 2024; Wang et al., 2024).
