# PoSE: Efficient Context Window Extension of LLMs via Positional Skip-wise Training [p. 1-15]

**Authors:** Dawei Zhu*, Nan Yang, Liang Wang, Yifan Song, Wenhao Wu, Furu Wei, Sujian Li [p. 1]
**Affiliations:** Dawei Zhu, Yifan Song, Wenhao Wu, Sujian Li (School of Computer Science, Peking University; National Key Laboratory for Multimedia Information Processing, Peking University); Nan Yang, Liang Wang, Furu Wei (Microsoft Corporation) [p. 1]
**Venue:** Published as a conference paper at ICLR 2024 [p. 1]
**arXiv:** arXiv:2309.10400v3 [cs.CL], 21 Feb 2024 [p. 1]

## Abstract (verbatim)

> "Large Language Models (LLMs) are trained with a pre-defined context length, restricting their use in scenarios requiring long inputs. Previous efforts for adapting LLMs to a longer length usually requires fine-tuning with this target length (Full-length fine-tuning), suffering intensive training cost. To decouple train length from target length for efficient context window extension, we propose Positional Skip-wisE (PoSE) training that smartly simulates long inputs using a fixed context window. This is achieved by first dividing the original context window into several chunks, then designing distinct skipping bias terms to manipulate the position indices of each chunk. These bias terms and the lengths of each chunk are altered for every training example, allowing the model to adapt to all positions within target length. Experimental results show that PoSE greatly reduces memory and time overhead compared with Full-length fine-tuning, with minimal impact on performance. Leveraging this advantage, we have successfully extended the LLaMA model to 128k tokens using a 2k training context window. Furthermore, we empirically confirm that PoSE is compatible with all RoPE-based LLMs and position interpolation strategies. Notably, our method can potentially support infinite length, limited only by memory usage in inference. With ongoing progress for efficient inference, we believe PoSE can further scale the context window beyond 128k." [p. 1]

## Section Headings Observed

- 1 Introduction [p. 1]
- 2 Related Work [p. 2]
- 3 Methodology [p. 3]
- 3.1 Preliminaries [p. 3]
- 3.2 Proposed Approach: Positional Skip-wise Training (PoSE) [p. 4]
- 4 Experiments [p. 5]
- 4.1 Setups [p. 5]
- 4.2 Language Modeling [p. 6]
- 4.3 Passkey Retrieval for Effective Context Window [p. 6]
- 5 Analysis [p. 7]
- 5.1 Memory and Time Efficiency [p. 7]
- 5.2 Compatibility with RoPE-based LLMs and Diverse Interpolation Strategies [p. 7]
- 5.3 Potential for Extremely-Long Context [p. 8]
- 5.4 Evaluation of Capability on Original Context Window [p. 8]
- 6 Conclusion [p. 9]
- 7 Acknowledgement [p. 10]
- References [p. 10-12]
- Appendix A: Ablation of Text Contained Within Each Chunk [p. 13]
- Appendix B: Analysis of Chunk Number N [p. 13-14]
- Appendix C: Sliding Window PPL from Linear / NTK / YaRN Interpolation [p. 14-15]
