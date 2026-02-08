# 7 Conclusion [p. 10]

The authors presented the Transformer, the first sequence transduction model based entirely on attention, replacing the recurrent layers most commonly used in encoder-decoder architectures with multi-headed self-attention. [p. 10]

For translation tasks, the Transformer can be trained significantly faster than architectures based on recurrent or convolutional layers. On both WMT 2014 English-to-German and WMT 2014 English-to-French translation tasks, a new state of the art is achieved. In the former task the best model outperforms even all previously reported ensembles. [p. 10]

The authors are excited about the future of attention-based models and plan to apply them to other tasks. They plan to extend the Transformer to problems involving input and output modalities other than text and to investigate local, restricted attention mechanisms to efficiently handle large inputs and outputs such as images, audio and video. Making generation less sequential is another stated research goal. [p. 10]

The code used to train and evaluate the models is available at https://github.com/tensorflow/tensor2tensor. [p. 10]

**Acknowledgements:** The authors are grateful to Nal Kalchbrenner and Stephan Gouws for their fruitful comments, corrections and inspiration. [p. 10]
