# 6 Related Work [p. 8-9]

[p. 8-9] Considerable attention has been given to demystifying the operation of neural NLP models. An extensive line of work targeted neuron functionality in general, extracting the properties that neurons and subsets of neurons capture (Durrani et al., 2020; Dalvi et al., 2019; Rethmeier et al., 2020; Mu and Andreas, 2020; Vig et al., 2020), regardless of the model architecture or neurons' position in it.

Jacovi et al. (2018) analyzed CNN architectures in text classification and showed that they extract key n-grams from the inputs.

The study of the transformer architecture has focused on the role and function of self-attention layers (Voita et al., 2019; Clark et al., 2019; Vig and Belinkov, 2019) and on inter-layer differences (i.e. lower vs. upper layers) (Tenney et al., 2019; Jawahar et al., 2019). Previous work also highlighted the importance of feed-forward layers in transformers (Press et al., 2020; Pulugundla et al., 2021; Xu et al., 2020). Still, to date, the role of feed-forward layers remains under-explored.

Also related are interpretability methods that explain predictions (Han et al., 2020; Wiegreffe and Pinter, 2019), however, the authors' focus is entirely different: they do not interpret individual predictions, but aim to understand the mechanism of transformers.

Characterizing the functionality of memory cells based on examples that trigger maximal activations has been used previously in NLP (Rethmeier et al., 2020) and vision (Erhan et al., 2009).
