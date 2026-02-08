# D Implementation details [p. 30-32]

[p. 30] The code is optimized for modern hardware. Hardware accelerators like GPUs and TPUs truly shine on coalesced memory operations which load blocks of contiguous bytes at once. Thus, it is not very efficient to have small sporadic look-ups caused by a sliding window or random element queries. This is alleviated by "blockifying" the lookups.

## GPU/TPU and Sparsity [p. 30]

[p. 30] Ideally, if the adjacency matrix A described in Sec. 2 is sparse, one would hope this would be sufficient to speed up the implementation. Unfortunately, it is well known [33, 102] that such sparse multiplications cannot be efficiently implemented in GPUs. GPUs have thousands of cores performing operations in parallel. Thus, the sparse matrix multiplication mentioned in section Sec. 2 cannot be efficiently performed.

As a result the authors propose to first blockify the attention pattern, i.e. pack sets of query and keys together and then define attention on these blocks. The process is explained using the example shown in Fig. 3. Suppose there are 12 query and 12 key vectors to attend to. Using a block size of 2, the query matrix is split into 12/2 = 6 blocks and similarly the key matrix into 12/2 = 6 blocks. Then the three different building components of BIGBIRD are defined on the block matrix. In particular the three components are:

1. **Random attention:** Each query block attends to r random key blocks. In Fig. 3a, r = 1 with block size 2. This implies that each query block of size 2 randomly attends to a key block of size 2.

2. **Window local attention:** While creating the block, the number of query blocks and the number of key blocks are ensured to be the same. This helps in defining the block window attention. Every query block with index j attends to key block with index j - (w - 1)/2 to j + (w - 1)/2, including key block j. In Fig. 3b, w = 3 with block size 2. It means that each query block j (size 2 queries) attends to key block j - 1, j, j + 1.

3. **Global attention:** Global attention remains the same as defined in Sec. 2, but it is computed in terms of blocks. In Fig. 3c, g = 1 with block size 2. For BIGBIRD-ITC this implies that one query and key block attend to everyone.

[p. 30] The resulting overall attention matrix is shown in Fig. 3d. Unfortunately, simply trying to compute this attention score as multiplying arbitrary pairs of query and key vectors would require use of gather operation, which is inefficient. Upon closer examination of window and global attention, the authors observe that these attention scores can be computed without using a gather operation.

Recall, full dense attention scores can be calculated by simple matrix product of query and key matrix with a cost of O(n^2 d), as illustrated in Fig. 4a. Now note that if we blockify the query and key matrix and multiply, then with only O(nbd) cost we will obtain the block diagonal portion of the attention score, as depicted in Fig. 4b. To elaborate this, let Q, K in R^{n x d} be the query and key matrix corresponding to n tokens such that Q_{i.} = x_i W_Q and K_{i.} = x_i W_K. The n x d query

**Figure 3** (p. 30): "Building blocks of the *block-attention* mechanism used in BIGBIRD with block size = 2. This implies the attention matrix is split into blocks of size 2 x 2. All the previous BIGBIRD parameters work on each block as a unit. White color indicates absence of attention. (a) random attention with r = 1, (b) sliding window attention with w = 3 (c) global attention with g = 1. (d) the combined BIGBIRD model."

The figure shows four attention matrix visualizations, each as a grid:
- (a) Random Attention: scattered colored blocks in the matrix, one random key block per query block.
- (b) Window Attention: a band of three colored block-diagonals (j-1, j, j+1 for each query block j).
- (c) Global Attention: one full row and one full column of colored blocks (the first block row and first block column).
- (d) BIGBIRD: the combination of all three patterns, with the union of random, window, and global block patterns.

**Figure 4** (p. 31): "Idea behind fast sparse attention computation in BIGBIRD."

The figure has four sub-figures illustrating the computational procedure:
- (a) Full all pair attention can be obtained by direct matrix multiplication between the query and key matrix. Shows an n x d query matrix multiplied by a d x n key matrix producing an n x n attention score matrix where all cells are filled.
- (b) Block diagonal attention can be computed by "blockifying" the query and key matrix. Shows blocked query and key matrices multiplied to produce only the block-diagonal portion of the attention matrix.
- (c) Window local attention obtained by "blockifying" the query/key matrix, copying key matrix, and rolling the resulting key tensor. (Obtaining rolled key-block tensor is illustrated in detail in Fig. 5.) This ensures that every query attends to at least one block and at most two blocks of keys of size b on each side.
- (d) Window + Random attention obtained by following the procedure above along with gathering some random key blocks. Shows the final sparse attention pattern combining the window diagonal blocks with scattered random blocks.

---
[p. 32 continued]

**Figure 5** (p. 32): "Construction of rolled key-block tensor. Make w copies of the key matrix. Index the copies as -(w-1)/2 <= j <= (w-1)/2. Roll j^th copy by j blocks. Positive roll means circular shift entries left and likewise for negative roll corresponds to right shift. Finally, reshape by grouping the blocks along a new axis to obtain the key-blocked tensor. For illustration purpose w = 3 is chosen."

The figure shows three stages:
- Left: 3 copies of the key matrix (labeled "3 Copies of Key"), each a row of colored blocks (A B C D, E F G H, I J K L, M N O P, Q R S T, U V X Y).
- Middle: After rolling, the copies are shifted left/right by 0 or 1 block and then reshaped ("Rolled Key").
- Right: The final blocked key tensor ("Key") with blocks grouped along a new axis, forming a 3D tensor suitable for block-wise matrix multiplication.

## Block computation procedure [p. 32]

[p. 32] The query matrix Q and key matrix K, both in R^{n x d}, are blocked along the sequence length to obtain ceil(n/b) x b x d tensors Q' and K' respectively. The two tensors are multiplied as:

**Equation (13):**

A_{jst} = sum_u Q'_{jsu} K'_{jtu},       j = 0, 1, ..., ceil(n/b)

The resulting A tensor of size ceil(n/b) x b x b can be reshaped to correspond to the block diagonal portion of the full attention pattern. To extend from block diagonal to a window (i.e. where query block with index j attends to key block with index j - (w-1)/2 to j + (w-1)/2), w copies of the reshaped key tensor K' are made. Each copy of the key-block tensor is "rolled" incrementally along the first axis of length ceil(n/b), as illustrated in Fig. 5. Multiplying these w rolled key-block tensors with the query-block tensor yields the desired window attention scores (Fig. 4c). For the global component, the first g blocks from the key tensor corresponding to the global tokens are always included. For the random attention, which is very small (r = 3 for all experiments), gather ops are used (Fig. 4d). By design, each query block attends to exactly r random blocks.

## Efficient dense multiplication [p. 32]

[p. 32] The result of all three components is basically a compact dense tensor K'' of size ceil(n/b) x (g + w + r)b x d, as shown in Fig. 6. Computing the final attention score then just boils down to a dense tensor multiplication, at which TPU/GPU are very efficient. Specifically, Q' (size: ceil(n/b) x b x d) is multiplied with K'' (size: ceil(n/b) x (g + w + r)b x d) with a cost of O(n(g + w + r)bd) to yield the desired attention score tensor of size ceil(n/b) x b x (g + w + r)b, which can be reshaped to obtain all the attention scores according to the BIGBIRD pattern.

**Figure 6** (p. 32): "Overview of BIGBIRD attention computation. Structured block sparsity helps in compactly packing our operations of sparse attention, thereby making our method efficient on GPU/TPU. On the left, we depict the transformed dense query and key tensors. The query tensor is obtained by simply blocking and reshaping while the final key tensor by concatenating three transformations: The first green columns, corresponding to global attention, is fixed. The middle blue columns correspond to window local attention and can be obtained by appropriately rolling as illustrated in Fig. 5. For the final orange columns, corresponding to random attentions, we need to use computationally inefficient gather operation. Dense multiplication between the query and key tensors efficiently calculates the sparse attention pattern (except the first row-block, which is computed by direct multiplication), using the ideas illustrated in Fig. 4. The resultant matrix on the right is same as that shown in Fig. 3d."

The figure shows:
- Left side: A blocked query tensor (Q1-Q6) and a composite key tensor. The key tensor has columns labeled "Fixed" (green, global), "Roll Key Matrix Left" and "Roll Key Matrix Right" (blue, window), and "Gather" (orange, random). Each row of the key tensor shows the specific key blocks that each query block attends to (e.g., Q2 row: K1, K6, K2, K3, K5; Q3 row: K1, K2, K3, K4, K5; etc.).
- Right side: The resulting sparse attention score matrix (Q1-Q6 rows vs K1-K6 columns) with colored blocks showing which query-key pairs have non-zero attention: diagonal window bands plus global rows/columns plus scattered random blocks.