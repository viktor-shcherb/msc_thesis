# Appendix C: Additional Related Work (continued) [p. 33]

[p. 33] cluding MEGA (Ma et al., 2022), DSS (Gupta et al., 2022), H3 (Fu et al., 2022), and Linear Recurrent Unit (LRU) (Orvieto et al., 2023).

[p. 33] Mamba (Gu & Dao, 2023) is a selective SSM that introduces time-dependent selective mechanism to enhance the long-range modeling ability of SSMs. The selectivity removes the linear time-variance property of the SSM, making it no longer possible to parallelize Mamba as a long convolution kernel. Yet Mamba can still be effectively parallelized using parallel associative scan (Blelloch, 1990; Martin & Cundy, 2018; Smith et al., 2023) with a hardware-aware implementation. Recently proposed GateLoop (Katsch, 2023) introduces a similar data-dependent state transitions. The data-dependent states, also concurrently proposed in GLA (Yang et al., 2023), are similar to the Weighted Key-Value State in Finch.

[p. 33] A contemporary but independent work also proposes recurrent models named as Hawk and Griffin (De et al., 2024). Hawk is a recurrent model with the Real-Gated Linear Recurrent Unit (RG-LRU), whereas Griffin mixes the RG-LRU with local multi-query attention, thereby achieving long-context extrapolation efficiently.

[p. 33] Please see Tiezzi et al. (2024) and Cirone et al. (2024) for a comprehensive review of recent developments of recurrent models.
