# FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning

**Authors:** Tri Dao
**Affiliations:** Princeton University, Stanford University

## Publication Status

- **arXiv preprint:** July 2023, arXiv:2307.08691
- **Peer-reviewed:** Yes
- **Conference:** The Twelfth International Conference on Learning Representations (ICLR 2024), Vienna, Austria, May 7-11, 2024
- **Status:** Published conference paper

## Preferred Citation

Cite the ICLR 2024 version:

> Dao, T. (2024). FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning. In The Twelfth International Conference on Learning Representations (ICLR 2024).

## Links

- arXiv: https://arxiv.org/abs/2307.08691
- Code: https://github.com/Dao-AILab/flash-attention

## Notes

This paper is a direct follow-up to FlashAttention (Dao et al., NeurIPS 2022), focusing on GPU-level optimizations to further improve throughput. While FlashAttention addressed IO-awareness, FlashAttention-2 addresses suboptimal work partitioning between thread blocks and warps.
