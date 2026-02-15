# A.1 Applying STRING on Llama3.1 128K [p. 17]

[p. 17]

In this section, we demonstrate the application of STRING on Llama3.1 128K. We present the utilization of STRING to drop position indices greater than $\frac{1}{3} * L \approx 42K$ and $\frac{1}{2} * L = 64K$, where $L=128K$ represents the training length of Llama3.1. The resulting position matrix is illustrated in Figure 8.

**Figure 8** (p. 17): "The resulted position matrix of Llama3.1 128K after shifting. In Figure (a), we use a shifted offset of $\frac{L}{3} \approx 42K$ and the local window $W$ is 128. In Figure (b), we overwrite more infrequent positions and the shifted offset is $S = \frac{L}{2} = 64K$."

Description: Two matrix visualizations showing position matrix transformations
- Key elements: (a) Shows matrix after shifted offset $S = \frac{L}{3}$. (b) Shows matrix after shifted offset $S = \frac{L}{2}$. Both matrices show the diagonal structure with position indices, displaying empty slots, shifted positions, and local windows.
- Matrix structure details from Figure 8a:
  - Original positions dropping indices ≥ 86K become $[\_, \_, \ldots, \_, 86K-1, \ldots, 2, 1, 0]$
  - After filling empty slots with stride $S = 42K$: $[86K-1, \ldots, 2, 1, 0, 42K, \ldots, 2, 1, 0]$
  - After adding local window $W$ of 128: shifted position indices $[86K + 127, \ldots, 129, 128, 42K-1, \ldots, 2, 1, 0]$
  - Applying STRING with offset $S = 64K$ changes last row from $[\_, \_, \ldots, \_, 64K-1, \ldots, 2, 1, 0]$
  - Well-trained positions shifted from diagonal $[\_, \_, \ldots, \_, 64K-1, \ldots, 2, 1, 0] \rightarrow [64K-1, \ldots, 1, 0, 64K-1, \ldots, 1, 0]$
  - After adding local window of 128: $[64K + 127, \ldots, 129, 128, 64K-1, \ldots, 1, 0]$
- Matrix structure details from Figure 8b with $S = \frac{L}{2}$: Similar transformation but overwrites more infrequent positions
- Notable patterns: The procedure illustrates how STRING shifts well-trained positions to replace ineffective ones. When position indices ≥ 64K (in the case of $S = 64K$), the row is converted to positions starting from 64K. The diagonal structure is maintained with local window additions.
- Supports claim: STRING can be applied at different shift offsets to replace varying amounts of ineffective positions, demonstrating flexibility in the method [p. 7-8]

In Figure 8a, let us consider the last row of the matrix. The original positions after dropping position indices ≥ 86K, they become $[\_, \_, \ldots, \_, 86K-1, \ldots, 2, 1, 0]$. To fill the empty slots, we shift the positions leftwards with a stride of $S = 42K$, resulting in $[86K-1, \ldots, 2, 1, 0, 42K-1, \ldots, 2, 1, 0]$. After adding a local window $W$ of 128, we obtain the shifted position indices: $[86K + 127, \ldots, 129, 128, 42K-1, \ldots, 2, 1, 0]$. Applying STRING with an offset $S = 64K$ is shown in (Figure 8b). The procedure is the same. We also illustrate the changes in the last row of the position matrix. After dropping position indices ≥ 64K, the row is converted to $[\_, \_, \ldots, \_, 64K-1, \ldots, 2, 1, 0]$. Then, the well-trained positions are shifted from the diagonal: $[\_, \_, \ldots, \_, 64K-1, \ldots, 2, 1, 0] \rightarrow [64K-1, \ldots, 1, 0, 64K-1, \ldots, 1, 0]$. Finally, the position indices after adding a local window of 128 are $[64K + 127, \ldots, 129, 128, 64K-1, \ldots, 1, 0]$.
