# 3 Neural Turing Machines [p. 5-6]

[p. 5] An NTM architecture contains two basic components: a neural network *controller* and a memory bank. Figure 1 presents a high-level diagram. Like most neural networks, the controller interacts with the external world via input and output vectors. Unlike a standard network, it also interacts with a memory matrix using selective read and write operations. By analogy to the Turing machine, the network outputs that parametrise these operations are called "heads."

> "Crucially, every component of the architecture is differentiable, making it straightforward to train with gradient descent." [p. 5]

The authors achieve differentiability by defining "blurry" read and write operations that interact to a greater or lesser degree with all the elements in memory (rather than addressing a single element, as in a normal Turing machine or digital computer). The degree of blurriness is determined by an attentional "focus" mechanism that constrains each read and write operation to interact with a small portion of memory, while ignoring the rest. Because interaction with the memory is highly sparse, the NTM is biased towards storing data without interference.

The memory location brought into attentional focus is determined by specialised outputs emitted by the heads. These outputs define a normalised weighting over the rows in the memory matrix (referred to as memory "locations"). Each weighting, one per read or write head, defines the degree to which the head reads or writes at each location. A head can thereby attend sharply to a single location or weakly to many locations.

**Figure 1** (p. 5): "Neural Turing Machine Architecture. During each update cycle, the controller network receives inputs from an external environment and emits outputs in response. It also reads to and writes from a memory matrix via a set of parallel read and write heads. The dashed line indicates the division between the NTM circuit and the outside world."
The figure shows a block diagram with External Input and External Output at the top connected to a Controller box. Below the Controller are Read Heads and Write Heads boxes, which connect down to a Memory box. The dashed line separates the Controller/Heads/Memory (the NTM circuit) from the External Input/Output (the outside world).

## 3.1 Reading [p. 6]

[p. 6] Let **M**_t be the contents of the N x M memory matrix at time t, where N is the number of memory locations, and M is the vector size at each location. Let **w**_t be a vector of weightings over the N locations emitted by a read head at time t. Since all weightings are normalised, the N elements w_t(i) of **w**_t obey the following constraints:

$$\sum_i w_t(i) = 1, \qquad 0 \le w_t(i) \le 1, \; \forall i.  \tag{1}$$

Equation (1) defines the normalisation constraints on the weight vector: weights sum to 1 and each weight is between 0 and 1.

The length M *read vector* **r**_t returned by the head is defined as a convex combination of the row-vectors **M**_t(i) in memory:

$$\mathbf{r}_t \longleftarrow \sum_i w_t(i) \mathbf{M}_t(i), \tag{2}$$

Equation (2) defines the read operation as a weighted sum over memory rows, which is clearly differentiable with respect to both the memory and the weighting.

## 3.2 Writing [p. 6]

Taking inspiration from the input and forget gates in LSTM, each write is decomposed into two parts: an *erase* followed by an *add*.

Given a weighting **w**_t emitted by a write head at time t, along with an *erase vector* **e**_t whose M elements all lie in the range (0, 1), the memory vectors **M**_{t-1}(i) from the previous time-step are modified as follows:

$$\tilde{\mathbf{M}}_t(i) \longleftarrow \mathbf{M}_{t-1}(i) \left[\mathbf{1} - w_t(i) \mathbf{e}_t\right], \tag{3}$$

Equation (3) defines the erase operation. **1** is a row-vector of all 1s, and the multiplication against the memory location acts point-wise. The elements of a memory location are reset to zero only if both the weighting at the location and the erase element are one; if either the weighting or the erase is zero, the memory is left unchanged. When multiple write heads are present, the erasures can be performed in any order, as multiplication is commutative.

Each write head also produces a length M *add vector* **a**_t, which is added to the memory after the erase step:

$$\mathbf{M}_t(i) \longleftarrow \tilde{\mathbf{M}}_t(i) + w_t(i) \, \mathbf{a}_t. \tag{4}$$

Equation (4) defines the add operation. The order of adds by multiple heads is irrelevant. The combined erase and add operations of all write heads produces the final content of the memory at time t. Since both erase and add are differentiable, the composite write operation is differentiable too. Both the erase and add vectors have M independent components, allowing fine-grained control over which elements in each memory location are modified.

---
[p. 7-9 continued]

## 3.3 Addressing Mechanisms [p. 7-9]

[p. 7] Although the equations of reading and writing have been shown, the production of the weightings has not yet been described. The weightings arise by combining two addressing mechanisms with complementary facilities:

1. **Content-based addressing** ("content-addressing") focuses attention on locations based on the similarity between their current values and values emitted by the controller. This is related to the content-addressing of Hopfield networks (Hopfield, 1982). The advantage is that retrieval is simple, merely requiring the controller to produce an approximation to a part of the stored data, which is then compared to memory to yield the exact stored value.

2. **Location-based addressing** is needed for tasks where the content of a variable is arbitrary but the variable still needs a recognisable name or address. Arithmetic problems fall into this category: the variable x and the variable y can take on any two values, but the procedure f(x, y) = x * y should still be defined. Content-based addressing is strictly more general than location-based addressing, since the content of a memory location could include location information inside it. However, providing location-based addressing as a primitive operation proved essential for some forms of generalisation, so both mechanisms are employed concurrently.

**Figure 2** (p. 7): "Flow Diagram of the Addressing Mechanism. The *key vector*, **k**_t, and *key strength*, beta_t, are used to perform content-based addressing of the memory matrix, **M**_t. The resulting content-based weighting is interpolated with the weighting from the previous time step based on the value of the *interpolation gate*, g_t. The *shift weighting*, **s**_t, determines whether and by how much the weighting is rotated. Finally, depending on gamma_t, the weighting is sharpened and used for memory access."
The figure shows a flow diagram. Previous State (**w**_{t-1}, **M**_t) and Controller Outputs (**k**_t, beta_t, g_t, **s**_t, gamma_t) feed into four sequential stages: Content Addressing produces **w**^c_t, then Interpolation produces **w**^g_t, then Convolutional Shift produces **w_tilde**_t, then Sharpening produces the final **w**_t.

### 3.3.1 Focusing by Content [p. 8]

[p. 8] For content-addressing, each head (whether employed for reading or writing) first produces a length M *key vector* **k**_t that is compared to each vector **M**_t(i) by a similarity measure K[., .]. The content-based system produces a normalised weighting w^c_t based on the similarity and a positive *key strength*, beta_t, which can amplify or attenuate the precision of the focus:

$$w^c_t(i) \longleftarrow \frac{\exp\left(\beta_t K\left[\mathbf{k}_t, \mathbf{M}_t(i)\right]\right)}{\sum_j \exp\left(\beta_t K\left[\mathbf{k}_t, \mathbf{M}_t(j)\right]\right)}. \tag{5}$$

Equation (5) defines content-based addressing as a softmax over scaled similarities between the key vector and each memory row.

In the current implementation, the similarity measure is cosine similarity:

$$K[\mathbf{u}, \mathbf{v}] = \frac{\mathbf{u} \cdot \mathbf{v}}{||\mathbf{u}|| \cdot ||\mathbf{v}||}. \tag{6}$$

Equation (6) defines cosine similarity used as the similarity measure K.

### 3.3.2 Focusing by Location [p. 8-9]

[p. 8] The location-based addressing mechanism is designed to facilitate both simple iteration across the locations of the memory and random-access jumps. It does so by implementing a rotational shift of a weighting. For example, if the current weighting focuses entirely on a single location, a rotation of 1 would shift the focus to the next location. A negative shift would move the weighting in the opposite direction.

Prior to rotation, each head emits a scalar *interpolation gate* g_t in the range (0, 1). The value of g is used to blend between the weighting **w**_{t-1} produced by the head at the previous time-step and the weighting **w**^c_t produced by the content system at the current time-step, yielding the *gated weighting* **w**^g_t:

$$\mathbf{w}^g_t \longleftarrow g_t \mathbf{w}^c_t + (1 - g_t) \mathbf{w}_{t-1}. \tag{7}$$

Equation (7) defines the interpolation gate. If the gate is zero, the content weighting is entirely ignored and the weighting from the previous time step is used. If the gate is one, the weighting from the previous iteration is ignored and the system applies content-based addressing.

After interpolation, each head emits a *shift weighting* **s**_t that defines a normalised distribution over the allowed integer shifts. For example, if shifts between -1 and 1 are allowed, **s**_t has three elements corresponding to shifts of -1, 0, and 1. The simplest way to define the shift weightings is to use a softmax layer of the appropriate size attached to the controller. The authors also experimented with another technique, where the controller emits a single scalar that is interpreted as the lower bound of a width one uniform distribution over shifts. For example, if the shift scalar is 6.7, then s_t(6) = 0.3, s_t(7) = 0.7, and the rest of **s**_t is zero.

[p. 9] If the N memory locations are indexed from 0 to N - 1, the rotation applied to **w**^g_t by **s**_t can be expressed as the following circular convolution:

$$\tilde{w}_t(i) \longleftarrow \sum_{j=0}^{N-1} w^g_t(j) \, s_t(i - j) \tag{8}$$

Equation (8) defines the convolutional shift, where all index arithmetic is computed modulo N. The convolution operation can cause leakage or dispersion of weightings over time if the shift weighting is not sharp. For example, if shifts of -1, 0, and 1 are given weights of 0.1, 0.8, and 0.1, the rotation will transform a weighting focused at a single point into one slightly blurred over three points.

To combat this, each head emits one further scalar gamma_t >= 1 whose effect is to sharpen the final weighting as follows:

$$w_t(i) \longleftarrow \frac{\tilde{w}_t(i)^{\gamma_t}}{\sum_j \tilde{w}_t(j)^{\gamma_t}} \tag{9}$$

Equation (9) defines the sharpening operation that counteracts blur from the convolutional shift.

The combined addressing system of weighting interpolation and content and location-based addressing can operate in three complementary modes:
1. A weighting can be chosen by the content system without any modification by the location system.
2. A weighting produced by the content addressing system can be chosen and then shifted. This allows the focus to jump to a location next to, but not on, an address accessed by content; in computational terms this allows a head to find a contiguous block of data, then access a particular element within that block.
3. A weighting from the previous time step can be rotated without any input from the content-based addressing system. This allows the weighting to iterate through a sequence of addresses by advancing the same distance at each time-step.

## 3.4 Controller Network [p. 9-10]

[p. 9] The NTM architecture has several free parameters, including the size of the memory, the number of read and write heads, and the range of allowed location shifts. The most significant architectural choice is the type of neural network used as the controller: recurrent or feedforward.

A recurrent controller such as LSTM has its own internal memory that can complement the larger memory in the matrix. If one compares the controller to the central processing unit in a digital computer (albeit with adaptive rather than predefined instructions) and the memory matrix to RAM, then the hidden activations of the recurrent controller are akin to the registers in the processor. They allow the controller to mix information across multiple time steps of operation.

A feedforward controller can mimic a recurrent network by reading and writing at the same location in memory at every step. Furthermore, feedforward controllers often confer greater transparency to the network's operation because the pattern of reading from and writing to the memory matrix is usually easier to interpret than the internal state of an RNN.

[p. 10] However, one limitation of a feedforward controller is that the number of concurrent read and write heads imposes a bottleneck on the type of computation the NTM can perform. With a single read head, it can perform only a unary transform on a single memory vector at each time-step; with two read heads it can perform binary vector transforms, and so on. Recurrent controllers can internally store read vectors from previous time-steps, so do not suffer from this limitation.
