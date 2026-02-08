# A Appendix [p. 13-15]

## A.1 LRA Tasks [p. 13]

[p. 13] This section describes the details and hyperparameters of each task. The authors also plan to release the configuration files along with the implementation of the models and benchmarks, that can be used to reproduce the results reported in the paper.

### A.1.1 ListOps [p. 13]

Following the generation steps in (Nangia & Bowman, 2018), the authors generate their own long version of this task. Sequence length of 2K is used. All xformer models have an embedding dimension of 512, 8 heads, 6 layers and a feed-forward dimension of 2048. All models are trained for 5K steps. The [CLS] token is used and mapped into a 10 class Softmax layer for classification.

### A.1.2 Byte-level Document Classification [p. 13]

The IMDb reviews dataset (Maas et al., 2011) is used with sequence lengths of {1K, 2K, 3K, 4K} tokens for all models. The best results across these four sequence lengths are picked. A [cls] token is used for prediction. All the [cls] tokens from xformer encoders are passed into a two layered MLP with ReLU activations. The MLP emits a 2-class logits for binary classification. The softmax cross entropy loss function is optimized. All xformer models are parameterized by the same number of layers, heads and hidden dimensions, namely 8 heads, 512 hidden dimensions and d = 2048 for positional FFN layers. 6 layers are used for all xformers. The learning rate is 0.05 with weight decay of 0.1. Adam with warmup is used. All models are trained for 20K steps and a batch size of 32.

### A.1.3 Byte-level Document Matching [p. 13]

The ACL anthology network is used for a related article matching task. A sequence length of 4K per document (8K tokens in total for two sequences) is used. The two encoders share parameters. Similar to document classification, the [cls] token from xformer encoders is used. Let X_1 be the [cls] token embedding from document 1 and X_2 be the [cls] token embedding from document 2, the final score is computed via:

Y = MLP([X_1, X_2, X_1 * X_2, X_1 - X_2])  ... (1)

where MLP(.) is a two layered MLP with relu activation functions. In lieu of the much longer sequence length, a batch size of 32 is used, embedding dimension of 128, 4 heads, a FFN dimension of 512 and 4 layers. Model is trained with Adam for 5K steps with a learning rate of 0.5.

## A.2 Image Classification [p. 13]

[p. 13] The gray-scaled (single channel) CIFAR10 is used as the image classification dataset, with 10 classes. The resolution of input images is 32 x 32 and after flattening the input images, the xformer encoders are fed with a sequence of 1024 pixels. Similar to the other classification tasks, there is a classifier head on top of the xformer encoder, consisting of a two-layer MLP with ReLU activation. Softmax cross-entropy has been used for optimizing the parameters of the models. The models are trained for 200 epochs and extensive sweeps over different hyper-parameters are performed. The following values lead to the best average performance across all xformers: 3 layers, 4 heads, 128 as the hidden dimensions of FFN blocks, 64 as the query/key/value hidden dimensions, and a learning rate of 0.01.

### A.2.1 Generalization Gap [p. 13-14]

[p. 13-14] For the image classification benchmark, the authors mentioned in Section 3 that most of the models struggle generalizing to the test set. Table 3 presents the train and test accuracy for different models and for almost all these models, the gap between the two scores is considerably high.

**Table 3** (p. 14): "Test and train accuracy of different models on Image Classification task."

| Model | test accuracy | train accuracy |
|---|---|---|
| Transformer | 42.44 | 69.45 |
| Local Attention | 41.46 | 63.19 |
| Sparse Trans. | **44.24** | 66.74 |
| Longformer | 42.22 | 71.65 |
| Linformer | 38.56 | 97.23 |
| Reformer | 38.07 | 68.45 |
| Sinkhorn Trans. | 41.23 | 69.21 |
| Synthesizer | 41.61 | **97.31** |
| BigBird | 40.83 | 71.49 |
| Linear Trans. | 42.34 | 65.61 |
| Performer | 42.77 | 73.90 |

[p. 14] While this task can be simple to solve for convolutional models (e.g., accuracy of wide-resnet on gray-scale CIFAR10 with no data augmentation is 89.21) it is rather difficult for Transformer-based models with this setup. Naturally, one can find ways to improve the performance with a different setup. For instance, in the authors' setup, models are not informed about the ordinality of pixel intensities and consume them as independent symbols. They observed that learning embedding that reflects this property is rather hard for most of these models (Figure [not numbered in text]). If the embedding layer is simply replaced with a CNN stem, an immediate boost in performance is seen (e.g., replacing the embedding layer of a vanilla Transformer with a convolutional stem, with 3 x 3 kernel, gives accuracy of 75.32).

Another modification that can lead to better performance is to incorporate spatial representation that are translation invariant in Transformer models (e.g., adding 2D relative positional embedding to a vanilla transformer gives accuracy of 61.72). However, adding these sorts of changes makes the setup digress from the original point of this task in the benchmark.

### A.2.2 Visualizations of Learned Embedding by a Vanilla Transformer [p. 14-15]

**Figure 4** (p. 14): "**Left:** The cosine similarity between the embedding learned for each pixel intensity. **Right:** Each tile shows the cosine similarity between the position embedding of the pixel with the indicated row and column and the position embeddings of all other pixels."
- Left panel: Heatmap showing pairwise cosine similarity of learned embeddings for different pixel intensities (0-255 on both axes). Shows higher similarity for close pixel values, but the patterns from learned embeddings do not perfectly reflect the ordinality of pixel intensities.
- Right panel: Grid of 32x32 tiles, each showing the cosine similarity between one pixel's positional embedding and all other pixels' positional embeddings. Shows that the lower the distance between two pixels is, the more similar their learned positional embeddings are. However, the spatial closeness in y axis is more preserved in the learned embedding than the distances in the x axis.

[p. 14-15] On the left, the pairwise similarity of learned embeddings for pixel intensities is visible. Although there is a higher similarity for close pixel values, the patterns from these learned embeddings do not perfectly reflect the ordinality of the pixel intensities. On the right, the pairwise similarity of positional embeddings for different input positions is visible. The lower the distance between two pixels, the more similar their learned positional embeddings. However, the spatial closeness in y axis is more preserved in the learned embedding than the distances in the x axis.

## A.3 Pathfinder [p. 15]

[p. 15] Pathfinder task probes the ability of models to detect long range spatial dependencies between input features. To solve the task, a model requires to identify the target contour and trace it from one end to the other. Although Pathfinder is visually a simple task, it has been shown that the clutter and variations in path shape makes the task difficult for CNN models (Linsley et al., 2018; Kim* et al., 2020).

The Pathfinder task is a binary classification task and the resolution of input images is 32 x 32. Similar to image classification task, the xformer encoders are fed with a sequence of 1024 pixels after flattening the input images. The classifier head on top of the xformer encoder is also a two-layer MLP with ReLU activation and Softmax cross-entropy loss is used for the optimization. The models are trained for 200 epochs. The hyper-parameters used for the xformer model are as follows: 4 layers, 8 heads, 128 as the hidden dimensions of FFN blocks, 128 as the query/key/value hidden dimensions, and the learning rate of 0.01.

### A.3.1 Visualization of the Attention Maps from a Vanilla Transformer [p. 15]

[p. 15] Given that transformers have many units with global receptive field, they have better potential for solving the task, compared to models with local receptive fields. Figure 5 shows the attention distributions for a set of examples given on token (CLS token) as the query. The attention module collects information from different positions in input to be able to trace the target path.

**Figure 5** (p. 15): "Attention map for different examples from the Pathfinder task. Each map presents the attention distribution, given the CLS token at the final layer as the query, averaged across all heads in a vanilla Transformer model. Note that for visualization, we use attention-rollout (Abnar & Zuidema, 2020) for more precise input attribution."
- Grid of attention map visualizations (7 rows x 10 columns approximately). Each panel shows a Pathfinder example image with the attention distribution overlaid. The attention maps highlight regions along the path contours, showing how the Transformer's attention traces the path between the two endpoints.

[p. 15] The authors also include Pathfinder-X in LRA, which is similar to Pathfinder but inputs are in higher resolutions, i.e. longer input sequences. On Pathfinder-X, two setups have been tried for training: first training models from scratch, second evaluating models that are trained on Pathfinder. In both cases, none of the models are able to deal with/generalize to 16K input length.
