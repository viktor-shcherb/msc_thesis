# 2 Method [p. 1-2]

## 2.1 Uptraining [p. 1-2]

Generating a multi-query model from a multi-head model takes place in two steps: [p. 1]

1. **Converting the checkpoint:** The projection matrices for key and value heads are mean pooled into single projection matrices. Mean pooling works better than selecting a single key and value head or randomly initializing new key and value heads from scratch. [p. 1]

2. **Additional pre-training:** The converted checkpoint is then pre-trained for a small proportion alpha of its original training steps on the same pre-training recipe. [p. 2]

**Figure 1** (p. 1): "Overview of conversion from multi-head to multi-query attention. Key and value projection matrices from all heads are mean pooled into a single head."
The figure shows H separate key projection matrices (K_1, K_2, ..., K_H) each of dimension d_model x d_h being mean pooled into a single Key Projection K_MQ of dimension d_model x d_h. [p. 1]

## 2.2 Grouped-query attention [p. 2]

Grouped-query attention divides query heads into G *groups*, each of which shares a single key head and value head. GQA-G refers to grouped-query with G groups. [p. 2]

- GQA-1, with a single group and therefore single key and value head, is equivalent to MQA. [p. 2]
- GQA-H, with groups equal to number of heads, is equivalent to MHA. [p. 2]

**Figure 2** (p. 2): "Overview of grouped-query method. Multi-head attention has H query, key, and value heads. Multi-query attention shares single key and value heads across all query heads. Grouped-query attention instead shares single key and value heads for each *group* of query heads, interpolating between multi-head and multi-query attention."
The figure shows three diagrams side by side: Multi-head (H separate Values, Keys, and Queries), Grouped-query (fewer Values/Keys than Queries, grouped), and Multi-query (single Values and Keys, H Queries). [p. 2]

When converting a multi-head checkpoint to a GQA checkpoint, each group key and value head is constructed by mean-pooling all the original heads within that group. [p. 2]

An intermediate number of groups leads to an interpolated model that is higher quality than MQA but faster than MHA. [p. 2]

Going from MHA to MQA reduces H key and value heads to a single key and value head, reducing the size of the key-value cache and therefore amount of data that needs to be loaded by a factor of H. However, larger models generally scale the number of heads, such that multi-query attention represents a more aggressive cut in both memory bandwidth and capacity. GQA lets us keep the same proportional decrease in bandwidth and capacity as model size increases. [p. 2]

Moreover, larger models suffer relatively less from memory bandwidth overhead from attention, as the KV-cache scales with model dimension while model FLOPs and parameters scale with the square of model dimension. Standard sharding for large models replicates the single key and value head by the number of model partitions (Pope et al., 2022); GQA removes the waste from such partitioning. Therefore, the authors expect GQA to present a particularly good trade-off for larger models. [p. 2]

GQA is not applied to the encoder self-attention layers; encoder representations are computed in parallel, and memory bandwidth is therefore generally not the primary bottleneck. [p. 2]
