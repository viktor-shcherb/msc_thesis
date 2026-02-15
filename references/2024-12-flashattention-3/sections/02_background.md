# 2 Background: Multi-Head Attention and GPU Characteristics [p. 2-4]

## 2.1 Multi-Head Attention [p. 2-3]

[p. 2] Let **Q**, **K**, **V** ∈ ℝ^(N×d) be the query, key and value input sequences associated to a single head, where N is the sequence length and d is the head dimension. Then attention is computed as:

**S** = σ**QK**^⊤ ∈ ℝ^(N×N), **P** = softmax(**S**) ∈ ℝ^(N×N), **O** = **PV** ∈ ℝ^(N×d),

where softmax is applied row-wise and one typically sets σ = 1/√d as the scaling factor. In practice, we subtract rowmax(**S**) from **S** to prevent numerical instability with the exponential function. For multi-head attention (MHA), each head has its own set of query, key and value projections, and this computation parallelizes across multiple heads and batches to produce the full output tensor.

[p. 3] Now let φ be a scalar loss function and let d(−) = ∂φ/∂(−) be notation for the gradient. Given the output gradient d**O** ∈ ℝ^(N×d), we compute d**Q**, d**K**, and d**V** according to the chain rule as follows:

d**V** = **P**^⊤d**O** ∈ ℝ^(N×d)
d**P** = d**OV**^⊤ ∈ ℝ^(N×N)
d**S** = dsoftmax(d**P**) ∈ ℝ^(N×N)
d**Q** = σd**SK** ∈ ℝ^(N×d)
d**K** = σd**S**^⊤**Q** ∈ ℝ^(N×d),

Here, we have that **d**s = (diag(**p**) − **pp**^⊤)d**p** for **p** = softmax(**s**) as a function of a vector **s**, and we write dsoftmax(d**P**) for this formula applied row-wise. Finally, this computation again parallelizes across the number of heads and batches for the backward pass of MHA.

## 2.2 GPU hardware characteristics and execution model [p. 3]

[p. 3] We describe the aspects of the GPU hardware and execution model relevant for FLASHATTENTION-3, with a focus on the NVIDIA Hopper architecture as a concrete instantiation of this model.

### Memory hierarchy

[p. 3] The GPU's memories are organized as a hierarchy of data locales, with capacity inversely related to bandwidth (Table 1)⁴. Global memory (GMEM), also known as HBM, is the off-chip DRAM accessible to all streaming multiprocessors (SMs). Data from GMEM gets transparently cached into an on-chip L2 cache. Next level contains a small on-chip, programmer-managed highly banked cache called shared memory (SMEM). Lastly, there is the register file within each SM.

### Thread hierarchy

[p. 3] The GPU's programming model is organized around logical groupings of execution units called threads. From the finest to coarsest level, the thread hierarchy is comprised of threads, warps (32 threads), warpgroups (4 contiguous warps), threadblocks (4 contiguous warpgroups in Hopper for a total of 4 × 32 × 4 = 512 threads, or cooperative thread arrays or CTAs), threadblock clusters (in Hopper), and grids.

[p. 3] These two hierarchies are closely interlinked. Threads in the same CTA are co-scheduled on the same SM, and CTAs in the same cluster are co-scheduled on the same GPC. SMEM is directly addressable by all threads within a CTA, whereas each thread has at most 256 registers (RMEM) private to itself.

**Table 1** (p. 3): Thread-Memory hierarchy for the NVIDIA Hopper H100 SXM5 GPU.

| Hardware Level | Parallel Agent | Data Locale | Capacity & Bandwidth |
|----------------|----------------|-------------|----------------------|
| Chip | Grid | GMEM | 80 GiB @ 3.35 TB/s |
| GPC | Threadblock Clusters | L2 | 50 MiB @ 12 TB/s |
| SM | Threadblock (CTA) | SMEM | 228 KiB per SM, 31TB/s per GPU |
| Thread | Thread | RMEM | 256 KiB per SM |

### Asynchrony and warp-specialization

[p. 3] GPUs are throughput processors that rely on concurrency and asynchrony to hide memory and execution latencies. For moving data between GMEM and SMEM, Hopper has the Tensor Memory Accelerator (TMA) as a dedicated hardware unit [38, §7.29]. Furthermore, unlike prior architectures such as Ampere, the Tensor Core of Hopper, exposed via the warpgroup-wide WGMMA instruction [40, §9.7.14], is also asynchronous and can source its inputs directly from shared memory.

---

⁴ Luo et al. [34] reports shared memory bandwidth of 128 bytes per clock cycle per SM, and we multiply that by 132 SMs and the boost clock of 1830 MHz.
