# 6 Conclusion [p. 10-11]

[p. 10] The authors explore the notion of compression as a means of extending the temporal receptive field of Transformer-based sequence models. They see a benefit to this approach in the domain of text, with the Compressive Transformer outperforming existing architectures at long-range language modelling. To continue innovation in this area, they also propose a new book-level LM benchmark, PG-19. This may be used to compare long-range language models, or to pre-train on other long-range reasoning language tasks, such as NarrativeQA (Kocisky et al., 2018).

The idea of compressive memories is applicable not only to the modality of text, but also audio, in the form of modelling the waveform of speech, and vision, within a reinforcement-learning agent trained on a maze-like memory task. In both cases, the authors compare to very strong baselines (WaveNet from Oord et al. (2016) and IMPALA from Espeholt et al. (2018)).

## Limitations

[p. 10] The main limitation of this work is additional complexity: if the task one wishes to solve does not contain long-range reasoning then the Compressive Transformer is unlikely to provide additional benefit. However as a means of scaling memory and attention, compression is a simpler approach to dynamic or sparse attention -- which often requires custom kernels to make efficient. One can build effective compression modules from simple neural network components, such as convolutions. The compression components are immediately efficient to run on GPUs and TPUs.

## Future directions

[p. 10-11] Memory systems for neural networks began as compressed state representations within RNNs. The recent wave of progress using attention-based models with deep and granular memories shows that it is beneficial to refrain from immediately compressing the past. However the authors hypothesise that more powerful models will contain a mixture of granular recent memories and coarser compressed memories. Future directions could include:
- Investigation of adaptive compression rates by layer
- The use of long-range shallow memory layers together with deep short-range memory
- The use of RNNs as compressors

> "Compressive memories should not be forgotten about just yet." [p. 11]

## Acknowledgements [p. 11]

Funded by DeepMind. The authors thank Chris Dyer, Felix Gimeno, and Koray Kavukcuoglu for reviewing the manuscript.

## Author Contributions [p. 11]

- Model and Experiment design: JR, TL, AP, SJ
- Dataset creation: AP, JR, CH
- Text experiments: JR, AP
- RL experiments: SJ
- Speech experiments: JR

## Funding [p. 11]

This research was funded by DeepMind.

## Competing Interests [p. 11]

The authors declare no competing financial interests.
