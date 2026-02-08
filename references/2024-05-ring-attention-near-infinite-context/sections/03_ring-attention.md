# 3 Ring Attention with Blockwise Parallel Transformers [p. 3-5]

[p. 3] The primary objective is to eliminate the memory constraints imposed by individual devices by efficiently distributing long sequences across multiple hosts without adding overhead. The approach is an enhancement to the blockwise parallel transformers (BPT) framework [23].

When distributing an input sequence across different hosts, each host is responsible for running one element of the outer loop of blockwise attention corresponding to its designated block, as well as the feedforward network specific to that block. These operations do not necessitate communication with other hosts. However, a challenge arises in the inner loop, which involves key-value block interactions that require fetching blocks from other hosts. Since each host possesses only one key-value block, the naive approach of fetching blocks from other hosts results in two issues: (1) it introduces a computation delay as the system waits for key-value blocks, and (2) accumulation of key-value blocks leads to increased memory usage, defeating the purpose of reducing memory cost.

## Ring-Based Blockwise Attention

[p. 3-4] To tackle these challenges, the authors leverage the permutation invariance property of the inner loop's key-value block operations. Self-attention between a query block and a group of key-value blocks can be computed in any order, as long as the statistics of each block are combined correctly for rescaling.

All hosts are conceptualized as forming a ring structure: host-1, host-2, ..., host-$N$. As blockwise attention and feedforward are computed, each host efficiently coordinates by concurrently sending key-value blocks to the next host while receiving key-value blocks from the preceding host, effectively overlapping transferring of blocks with blockwise computation. Concretely, for any host-$i$, during computation of attention between its query block and a key-value block, it concurrently sends key-value blocks to host-$(i+1)$ while receiving key-value blocks from host-$(i-1)$. If computation time exceeds the time required for transferring key-value blocks, this results in no additional communication cost. This overlapping mechanism applies to both forward and backward passes.

Prior work has also proposed leveraging a ring topology to compute self-attention [21], aiming to reduce communication costs. This work differs by utilizing blockwise parallel transformers [23] to substantially reduce memory costs, enabling zero-overhead scaling of context size during both training and inference.

**Figure 2** (p. 4): "**Top (a):** We use the same model architecture as the original Transformer but reorganize the compute. In the diagram, we explain this by showing that in a ring of hosts, each host holds one query block, and key-value blocks traverse through a ring of hosts for attention and feedforward computations in a block-by-block fashion. As we compute attention, each host sends key-value blocks to the next host while receives key-value blocks from the preceding host. The communication is overlapped with the computation of blockwise attention and feedforward. **Bottom (b):** We compute the original Transformer block-by-block. Each host is responsible for one iteration of the query's outer loop, while the key-value blocks rotate among the hosts. As visualized, a device starts with the first query block on the left; then we iterate over the key-value blocks sequence positioned horizontally. The query block, combined with the key-value blocks, are used to compute self-attention (yellow box), whose output is pass to feedforward network (cyan box)."

Part (a) shows two devices in a ring, each with Blockwise Attention and Blockwise FeedForward modules, with key-value blocks flowing between them in a circular pattern. Part (b) shows the detailed block-by-block computation: Query blocks (Query1-4) on the left form the outer loop, Key/Value blocks (Key1-4, Value1-4) at the bottom rotate among 4 devices through the inner loop. Each device performs Blockwise Attention (yellow) then Blockwise FeedForward (orange/blue). Arrows show "compute, send to next device" and "receive from previous device" for the key-value inner loop.

## Arithmetic Intensity Between Hosts

[p. 4-5] To determine the minimal required block size to overlap transferring with computation, assume each host has $F$ FLOPS and bandwidth between hosts is $B$. The approach involves interactions only with immediately previous and next hosts in a circular configuration, applicable to both GPU all-to-all topology and TPU torus topology.

Variables: block size $c$, hidden size $d$. Computing blockwise self-attention requires $2dc^2$ FLOPs for calculating attention scores using queries and keys, and an additional $2dc^2$ FLOPs for multiplying attention scores by values. Total computation demands: $4dc^2$ FLOPs. The projection of queries, keys, values, and blockwise feedforward operations are excluded since they only add compute complexity without communication costs between hosts — this simplification leads to a more stringent condition and does not compromise validity.

Communication: both key and value blocks require $2cd$ bytes each, for a combined communication demand of $4cd$ bytes. To achieve overlap between communication and computation, the following condition must hold:

$$4dc^2 / F \geq 4cd / B$$

This implies the block size $c$ should be greater than or equal to $F/B$. The block size needs to be larger than the ratio of FLOPs over bandwidth.

## Memory Requirement

[p. 5] A host needs to store multiple blocks: one block for the current query block, two block sizes for current key and value blocks, and two block sizes for receiving key and value blocks. Storing the output of blockwise attention and feedforward necessitates one block size (output retains the shape of the query block). A total of six blocks are required, translating to $6bch$ bytes of memory. The blockwise feedforward network has a maximum activation size of $2bch$ [23]. Consequently, the total maximum activation size remains at $6bch$ bytes.

**Table 1** (p. 5): Comparison of maximum activation sizes among different Transformer architectures. $b$ is batch size, $h$ is hidden dimension, $n$ is number of heads, $s$ is sequence length, $c$ is block size. Block size ($c$) is independent of input sequence length ($s$). Comparison is between vanilla Transformer [37], memory efficient attention [30], memory efficient attention and feedforward [23], and Ring Attention. Numbers are in bytes per layer, assuming *bfloat16* precision.

| Layer Type | Self-Attention | FeedForward | Total |
|---|---|---|---|
| Vanilla | $2bns^2$ | $8bsh$ | $2bhs^2$ |
| Memory efficient attention | $2bsh + 4bch$ | $8bsh$ | $8bsh$ |
| Memory efficient attention and feedforward | $2bsh$ | $2bsh$ | $2bsh$ |
| Ring Attention | $6bch$ | $2bch$ | $6bch$ |

Ring Attention's memory cost is independent of the input sequence length $s$, depending only on block size $c$.

**Table 2** (p. 5): Minimal sequence length needed on each device. Interconnect Bandwidth is unidirectional bandwidth between hosts (NVLink / InfiniBand for GPUs, ICI for TPUs). Minimal block size required $c = \text{FLOPS}/\text{Bandwidth}$, and minimal sequence length $s = 6c$.

| Spec Per Host | FLOPS (TF) | HBM (GB) | Interconnect Bandwidth (GB/s) | Minimal Blocksize ($\times$1e3) | Minimal Sequence Len ($\times$1e3) |
|---|---|---|---|---|---|
| A100 NVLink | 312 | 80 | 300 | 1.0 | 6.2 |
| A100 InfiniBand | 312 | 80 | 12.5 | 24.5 | 149.5 |
| TPU v3 | 123 | 16 | 112 | 1.1 | 6.6 |
| TPU v4 | 275 | 32 | 268 | 1.0 | 6.2 |
| TPU v5e | 196 | 16 | 186 | 1.1 | 6.3 |

The model needs a sequence length of $s = 6c$, which is six times the minimal block size. The required minimal sequence length per host varies between 6K and 10K for TPUs and GPUs with high bandwidth interconnect. For GPUs connected via InfiniBand (lower bandwidth), requirements are more strict. These requirements are easy to meet with parallelism such as data and tensor parallelism and memory efficient blockwise attention and feedforward [30, 9, 23].

## Algorithm and Implementation

[p. 5-6] Algorithm 1 provides the pseudocode. Ring Attention is compatible with existing code for memory efficient transformers: it just needs to call whatever available memory efficient computation locally on each host, and overlap the communication of key-value blocks between hosts with blockwise computation. The collective operation `jax.lax.ppermute` is used to send and receive key value blocks between nearby hosts. A Jax implementation is provided in Appendix A.

**Algorithm 1:** Reducing Transformers Memory Cost with Ring Attention [p. 6]
- **Required:** Input sequence $x$. Number of hosts $N_h$.
- Initialize
- Split input sequence into $N_h$ blocks so each host has one input block
- Compute query, key, and value for its input block on each host
- **for** Each transformer layer **do**
  - **for** $count = 1$ to $N_h - 1$ **do**
    - **for** For each host concurrently **do**
      - Compute memory efficient attention incrementally using local query, key, value blocks
      - Send key and value blocks to next host and receive key and value blocks from previous host
    - **end for**
  - **end for**
  - **for** For each host concurrently **do**
    - Compute memory efficient feedforward using local attention output
  - **end for**
- **end for**
