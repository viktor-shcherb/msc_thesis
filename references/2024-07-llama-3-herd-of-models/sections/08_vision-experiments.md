# 7 Vision Experiments [p. 54–61]

[p. 54] Visual-recognition capabilities are incorporated into Llama 3 via a compositional approach that consists of two main stages. First, a pre-trained image encoder (Xu et al., 2023) and the pre-trained language model are composed by introducing and training a set of cross-attention layers between the two models (Alayrac et al., 2022) on a large number of image-text pairs. This leads to the model illustrated in Figure 28. Second, temporal aggregator layers and additional video cross-attention layers that operate on a large collection of video-text pairs are introduced to learn the model to recognize and process temporal information from videos. [p. 54]

A compositional approach to foundation model development has several advantages: **(1)** it enables parallelization of the development of the vision and language modeling capabilities; **(2)** it circumvents complexities of joint pre-training on visual and language data that stem from tokenization of visual data, differences in background perplexities of tokens originating from different modalities, and contention between modalities; **(3)** it guarantees that model performance on text-only tasks is not affected by the introduction of visual-recognition capabilities; and **(4)** the cross-attention architecture ensures that compute is not expended passing full-resolution images through the increasingly large LLM backbones (specifically, the feed-forward networks in each transformer layer), making it more efficient during inference. The multimodal models are noted to still be under development and not yet ready for release. [p. 54]

Before presenting the results of experiments in Section 7.6 and 7.7, the data used to train visual recognition capabilities, the model architecture of the vision components, how training of those components is scaled, and pre-training and post-training recipes are described. [p. 54]

## 7.1 Data [p. 54–56]

Image and video data are described separately.

### 7.1.1 Image Data [p. 54–56]

[p. 54] The image encoder and adapter are trained on image-text pairs. This dataset is constructed via a complex data processing pipeline that consists of four main stages: **(1)** quality filtering, **(2)** perceptual de-duplication, **(3)** resampling, and **(4)** optical character recognition. A series of safety mitigations are also applied. [p. 54]

- **Quality filtering.** Quality filters are implemented that remove non-English captions and low-quality captions via heuristics such as low alignment scores produced by (Radford et al., 2021). Specifically, all image-text pairs below a certain CLIP score are removed. [p. 54]

- **De-duplication.** De-duplicating large-scale training datasets benefits model performance because it reduces training compute spent on redundant data (Esser et al., 2024; Lee et al., 2021; Abbas et al., 2023) and memorization (Carlini et al., 2023; Somepalli et al., 2023). Hence, training data is de-duplicated for both efficiency and privacy reasons. An internal version of the state-of-the-art SSCD copy-detection model (Pizzi et al., 2022) is used to de-duplicate images at scale. For all images, a 512-dimensional representation is first computed using the SSCD model. Those embeddings are used to perform a nearest neighbor (NN) search for each image across all images in the data set, using a cosine similarity measure. Examples above a certain similarity threshold are defined as duplicates. These duplicates are grouped using a connected-components algorithm, and only one image-text pair per connected component is maintained. The efficiency of the de-duplication pipeline is increased by: (1) pre-clustering the data using k-means clusters and (2) using FAISS (Johnson et al., 2019) for NN searches and clustering. [p. 55]

- **Resampling.** Diversity of the image-text pairs is ensured via resampling akin to Xu et al. (2023); Mahajan et al. (2018); Mikolov et al. (2013). First, a vocabulary of n-grams is constructed by parsing high-quality text sources. Next, the frequency of each vocabulary n-gram in the dataset is computed. The data is then resampled as follows: If any of the n-grams in a caption occurs less than *T* times in the vocabulary, the corresponding image-text pair is kept. Otherwise, each of the n-grams *n_i* in the caption is independently sampled with probability $\sqrt{T/f_i}$ where *f_i* indicates the frequency of n-gram *n_i*; the image-text pair is kept if any of the n-grams was sampled. This resampling aids performance on low-frequency categories and fine-grained recognition tasks. [p. 55]

- **Optical character recognition.** Image-text data is further improved by extracting text written in the image and concatenating it with the caption. The written text is extracted using a proprietary optical character recognition (OCR) pipeline. Adding OCR data into the training data is observed to greatly improve tasks that require OCR capabilities, such as document understanding. [p. 55]

**Transcribing documents.** To improve the performance of the models on document understanding tasks, pages from documents are rendered as images and paired with their respective text. The document text is obtained either directly from the source or via a document parsing pipeline. [p. 55]

**Safety.** [p. 55–56] The focus is primarily on ensuring that the pre-training dataset for image recognition does not contain unsafe content, such as sexual abuse material (CSAM) (Thiel, 2023). All training images are scanned for CSAM using perceptual hashing approaches such as PhotoDNA (Farid, 2021) as well as internal, proprietary classifiers. A proprietary media-risk retrieval pipeline is also used to identify and remove image-text pairs that are considered to be NSFW, for example, because they contain sexual or violent content. Minimizing the prevalence of such material in the training dataset is believed to improve the safety of the final model without impacting its helpfulness. Finally, face blurring is performed on all images in the training set. The model is tested against human generated prompts that refer to an attached image. [p. 56]

**Annealing data.** [p. 56] An annealing dataset is created by resampling the image-caption pairs to a smaller volume of ~350M examples using n-grams. Since the n-grams resampling favors richer text descriptions, this selects a higher-quality data subset. The resulting data is augmented with ~150M examples from five additional sources:

- **Visual grounding.** Noun phrases in the text are linked to bounding boxes or masks in the image. The grounding information (bounding boxes and masks) is specified in the image-text pair in two ways. (1) Boxes or masks are overlaid with marks on the image and marks in the text are used as reference, akin to set-of-marks (Yang et al., 2023a). (2) Normalized (*x*_min, *y*_min, *x*_max, *y*_max) coordinates are inserted directly into the text, demarcated by special tokens. [p. 56]

- **Screenshot parsing.** Screenshots are rendered from HTML code and the model is tasked with predicting the code that produced a specific element in the screenshot, akin to Lee et al. (2023). The element of interest is indicated in the screenshot via a bounding box. [p. 56]

- **Question-answer pairs.** Question-answer pairs are included, enabling use of volumes of question-answering data that are too large to be used in model finetuning. [p. 56]

- **Synthetic captions.** Images with synthetic captions that were generated by an early version of the model are included. Compared to original captions, synthetic captions are found to provide a more comprehensive description of images than the original captions. [p. 56]

- **Synthetically-generated structured images.** Synthetically generated images for a variety of domains such as charts, tables, flowcharts, math equations and textual data are also included. These images are accompanied by a structured representation such as the corresponding markdown or LaTeX notation. Besides improving recognition capabilities of the model for these domains, this data is found useful to generate question-answer pairs via the text model for finetuning. [p. 56]

### 7.1.2 Video Data [p. 56]

[p. 56] For video pre-training, a large dataset of video-text pairs is used. The dataset is curated through a multi-stage process. The associated texts are filtered and cleaned using rule-based heuristics, such as ensuring a minimum length and fixing capitalization. Then, language identification models are run to filter out non-English texts. OCR detection models are run to filter out videos with excessive overlaid text. To ensure reasonable alignment between the video-text pairs, CLIP (Radford et al., 2021) style image-text and video-text contrastive models are used. Image-text similarity is first computed using a single frame in the videos, and low similarity pairs are filtered out, then pairs with low video-text alignment are subsequently filtered out. Some data contains static or low-motion videos; this is filtered out using motion-score based filtering (Girdhar et al., 2023). No filters are applied on the visual quality of the videos such as aesthetic scores or resolution filtering. [p. 56]

The dataset contains videos with an average duration of 21 seconds and a median duration of 16 seconds, with over 99% of videos being under a minute. The spatial resolution varies significantly between 320p and 4K videos, with over 70% of the videos having a short side greater than 720 pixels. The videos have varying aspect ratios with almost all videos having between 1:2 and 2:1 aspect ratio, with a 1:1 median. [p. 56]

## 7.2 Model Architecture [p. 56–57]

[p. 56] The visual-recognition model consists of three main components: **(1)** an image encoder, **(2)** an image adapter, and **(3)** a video adapter.

**Image encoder.** The image encoder is a standard vision transformer (ViT; Dosovitskiy et al. (2020)) that is trained to align images and text (Xu et al., 2023). The ViT-H/14 variant of the image encoder is used.

**Figure 28** (p. 55): "Illustration of the compositional approach to adding multimodal capabilities to Llama 3 that we study in this paper. This approach leads to a multimodal model that is trained in five stages: **(1)** language model pre-training, **(2)** multi-modal encoder pre-training, **(3)** vision adapter training, **(4)** model finetuning, and **(5)** speech adapter training."

The figure shows four main architectural components arranged left to right:

1. **Image Encoder:** Takes a single image, splits into image patches, passes through a linear transform, self-attention, and feedforward network.

2. **Video Aggregator:** Takes video input (multiple image patches), passes through the image encoder to get image patch representations, which feed into temporal aggregator layers followed by cross-attention and feedforward network, producing a video representation. Outputs every ~3rd layer.

3. **Language Model:** Takes text tokens, produces token embeddings, passes through self-attention, cross-attention (which receives image/video representations every 4th layer), and feedforward network. Outputs text tokens via autoregressive decoding.

4. **Speech Encoder:** Takes a speech segment, passes through conformer blocks, then a speech adapter.

A legend indicates five training stages shown by different shadings: vision and speech encoder pre-training, vision adapter training, language model pre-training, model finetuning, and speech adapter training. The transformer blocks in the language model alternate between standard self-attention layers and cross-attention layers that attend to visual representations.

---
[p. 57 continued]

[p. 57] The image encoder has 630M parameters and was trained on 2.5B image-text pairs for five epochs. It is pre-trained on images with resolution 224 x 224; images are split up into 16 x 16 patches of equal size (i.e., a patch size of 14x14 pixels). As also demonstrated by prior work such as ViP-Llava (Cai et al., 2024), image encoders trained via a contrastive text alignment objective are unable to preserve fine-grained localization information. To alleviate this, a *multi-layer* feature extraction is employed, where features from the 4th, 8th, 16th, 24th and 31st layers are also provided in addition to the final layer features. In addition, 8 *gated* self-attention layers are further inserted (making a total of 40 transformer blocks) prior to pre-training of the cross-attention layers to learn alignment-specific features. The image encoder therefore eventually has a total 850M parameters with the additional layers. With the multi-layer features, the image encoder produces a 7680-dimensional representation for each of the resulting 16 x 16 = 256 patches. The parameters of the image encoder are *not* frozen during subsequent training stages as it is found to improve performance, especially in domains such as text recognition. [p. 57]

**Image adapter.** Cross-attention layers are introduced between the visual token representations produced by the image encoder and the token representations produced by the language model (Alayrac et al., 2022). The cross-attention layers are applied after every fourth self-attention layer in the core language model. Like the language model itself, the cross-attention layers use generalized query attention (GQA) for increased efficiency. The cross-attention layers introduce substantial numbers of additional trainable parameters into the model: for Llama 3 405B, the cross-attention layers have approximately 100B parameters. The image adapter is pre-trained in two stages: (1) initial pre-training followed by (2) annealing: [p. 57]

- **Initial pre-training.** The image adapter is pre-trained on a dataset of ~6B image-text pairs described above. For compute efficiency reasons, all images are resized to fit within *at most* four tiles of 336 x 336 pixels each, where the tiles are arranged to support different aspect ratios, e.g., 672 x 672, 672 x 336, and 1344 x 336. [p. 57]

- **Annealing.** Training of the image adapter continues on ~500M images from the annealing dataset described above. During annealing, the per-tile image resolution is increased to improve performance on tasks that require higher-resolution images, for example, infographics understanding. [p. 57]

**Video adapter.** The model takes as input up to 64 frames (uniformly sampled from a full video), each of which is processed by the image encoder. Temporal structure in videos is modeled through two components: **(i)** encoded video frames are aggregated by a temporal aggregator which merges 32 consecutive frames into one, **(ii)** additional video cross attention layers are added before every fourth image cross attention layer. The temporal aggregator is implemented as a perceiver resampler (Jaegle et al., 2021; Alayrac et al., 2022). Pre-training uses 16 frames per video (aggregated to 1 frame), but the number of input frames is increased to 64 during supervised finetuning. The video aggregator and cross attention layers have 0.6B and 4.6B parameters for Llama 3 7B and 70B, respectively. [p. 57]
