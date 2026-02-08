# 2 Long-Range Arena (LRA) [p. 2-5]

[p. 2] The Long-Range Arena (LRA) benchmark (pronounced *el-ra*) is implemented in Python 3 and Jax/Flax and open-sourced at https://github.com/google-research/long-range-arena.

## 2.1 Desiderata [p. 2-3]

The authors established six desiderata for creating the LRA benchmark:

1. **Generality**: All efficient Transformers models should be applicable to the tasks. Since not all xformer models can perform autoregressive decoding (Wang et al., 2020), only tasks that require encoding are included.
2. **Simplicity**: Tasks should have a simple setup. All factors that make comparisons difficult should be removed. This encourages simple models instead of cumbersome pipelined approaches. No particular data augmentation is included and pretraining is considered out of scope.
3. **Challenging**: Tasks should be difficult enough for current models to ensure room for improvement to encourage future research.
4. **Long inputs**: Input sequence lengths should be reasonably long since assessing how different models capture long-range dependencies is a core focus of LRA.
5. **Probing diverse aspects**: The set of tasks should assess different capabilities of models like their ability to model relations and hierarchical/spatial structures, generalization capability, etc.
6. **Non-resource intensive and accessible**: The benchmarks should be deliberately designed to be lightweight so as to be accessible to researchers without industry-grade computing resources.

## 2.2 Tasks [p. 3-4]

The tasks are specifically designed for the purpose of assessing different aspects of efficient Transformer models. Further details about each task can be found in the appendix.

### 2.2.1 Long ListOps [p. 3]

This task tests the capability of modeling hierarchically structured data in a long-context scenario. It is a longer variation of the standard ListOps task proposed in (Nangia & Bowman, 2018), which was designed to investigate the parsing ability of neural models.

The dataset is comprised of sequences with a hierarchical structure and operators MAX, MEAN, MEDIAN, and SUM_MOD that are enclosed by delimiters (brackets). An example (much shorter) sequence:

```
INPUT: [MAX 4 3 [MIN 2 3 ] 1 0 [MEDIAN 1 5 8 9, 2]]    OUTPUT: 5
```

Sequence lengths of up to 2K are used to test the ability to reason hierarchically while handling long contexts. The model needs to access all tokens and model the logical structure of the inputs. The task is a **ten-way classification** task and is described as considerably challenging.

### 2.2.2 Byte-level Text Classification [p. 3]

This task uses real-world data representing a common use case of efficient Transformers: processing long documents. Text classification is associated with many real-world applications such as spam, fraud, and bot detection and commercial document classification, among others (Howard & Ruder, 2018).

This task also benchmarks the ability of the models to deal with compositionality, as it requires composing characters into words into higher-level phrases. Compared to ListOps, boundaries are less well defined and need to be learned from the data, which is a challenging problem in its own right (Kawakami et al., 2019).

The byte/character-level setup is used to simulate a longer input sequence, which differs significantly from character-level language modeling (char LM). In char LM, reading nearby context suffices to determine the next character, but for byte-level text classification, the model needs to reason with compositional, unsegmented data to solve a meaningful real-world task. The IMDb reviews (Maas et al., 2011) dataset is used. Fixed max length of **4K**, truncated or padded when necessary. This is a **binary classification** task with accuracy as the metric.

Footnote 3 [p. 3]: On the IMDb word-level task, models without pre-training achieve accuracies in the high 80s while the same models score in the mid 60s on the character-level task (Tay et al., 2020b).

### 2.2.3 Byte-level Document Retrieval [p. 3-4]

[p. 3] This task evaluates a model's ability to encode and store compressed representations useful for matching and retrieval. Learning the similarity score between two vectors is a common problem in machine learning and is useful for a wide array of applications (Guo et al., 2016).

This task is mainly about modeling a similarity score between two documents in a "two tower setup" in which compressed representations are concatenated and passed into a linear classifier. Cross attention is deliberately prevented as a test of how well models can *compress* long sequences into representations suitable for similarity-based matching.

[p. 4] The ACL Anthology Network (AAN; Radev et al., 2013) dataset is used, which identifies if two papers have a citation link, a common setup used in long-form document matching (Jiang et al., 2019; Yang et al., 2020).

Similar to the text classification setup, a byte/character level setup is used. A sequence length of 4K for each document is used, making the total text length **8K**. This is a **binary classification** task with accuracy as the metric.

### 2.2.4 Image Classification on Sequences of Pixels [p. 4]

This is an image classification task where the inputs are sequences of pixels. An N x N image is flattened to a sequence of length N^2 pixels.

Similar to how the previous tasks require capturing the hierarchical structure in the data, this task requires the model to learn the 2D spatial relations between input pixels, while presented as a 1D sequence of symbols.

The authors focus on assessing Transformer models that process a sequence of discrete symbols, so extra modules such as a CNN stem that embeds pixel-level inputs are not allowed. Input images are mapped to a single gray-scale channel where each pixel is represented with an 8-bit pixel intensity (vocabulary size of 256). The **CIFAR-10** dataset (Krizhevsky, 2009) is used. Sequence length: **1024** (32 x 32).

### 2.2.5 Pathfinder (Long-Range Spatial Dependency) [p. 4]

The Pathfinder challenge (Linsley et al., 2018; Kim* et al., 2020) was first introduced for learning long-range spatial dependencies. It is a synthetic visual task motivated by cognitive psychology (Houtkamp & Roelfsema, 2010).

The task requires a model to make a binary decision whether two points represented as circles are connected by a path consisting of dashes. A positive example shows two connected points and a negative example shows two unconnected points (see Figure 1). The dataset also contains distractor paths, which makes the setup challenging. Images are treated as sequences of pixels. Images are of dimensions 32 x 32, making a sequence length of **1024**.

**Figure 1** (p. 4): "Samples of the Pathfinder task."
- (a) A positive example: shows a 32x32 grayscale image with dashed lines forming paths between points (circles). Two points are connected by a path of dashes.
- (b) A negative example: shows a similar 32x32 grayscale image with dashed lines and distractor paths, but the two circled points are not connected.

### 2.2.6 Pathfinder-X (Long-Range Spatial Dependencies with Extreme Lengths) [p. 4]

An extreme version of Pathfinder where examples consist of **16K** pixels (images of 128 x 128).

The key goal is to observe if a model would fail to solve the 16K extreme version even if it can successfully learn the standard version of 1024 tokens. This serves as an interesting litmus test to see if the same algorithmic challenges bear a different extent of difficulty when sequence lengths are much longer. This is included in the benchmark as Path-X.

## 2.3 Required Attention Span of LRA Tasks [p. 5]

One of the main goals of the LRA benchmark is assessing the ability of different efficient Transformer models to capture long-range dependencies. In order to have a quantitative estimate of the spatial extent needed to be considered by an attention mechanism to encode the inputs, the authors define *required attention span*.

Given a trained attention-based model and a sequence of tokens as inputs, the required attention span of an attention module is computed as the mean distance between the query token and the attended tokens, scaled by attention weights. The mean *required attention span* is computed over all attention modules in the best vanilla Transformer model for each task, averaged over 1K random samples from the validation set.

**Figure 2** (p. 5): "Required attention span on different tasks."
- Bar chart with y-axis "Required Attention Span" (scale 1e3, range 0.0 to 1.4) and x-axis showing five tasks.
- Approximate values from the chart:
  - ListOps (L=2k): ~0.75 x 1e3 = ~750
  - Text (L=4k): ~0.35 x 1e3 = ~350
  - Retrieval (L=4k): ~1.35 x 1e3 = ~1350
  - Image (L=1k): ~0.25 x 1e3 = ~250
  - Pathfinder (L=1k): ~0.55 x 1e3 = ~550
- For all LRA tasks the required attention span is rather high, showing that a Transformer model needs to go beyond combining only local information, while in many other tasks and datasets, attention mechanisms mostly need to combine information from neighboring positions.

The authors find that *required attention span* serves as a good proxy for how difficult a task is for Transformer-based models.

Footnote 4 [p. 5]: This metric mainly provides an indication of the required attention span for a task and the relative differences between tasks based on a reasonably strong model; a better model might only need to attend to shorter ranges (Daniluk et al., 2017; Rae & Razavi, 2020).
