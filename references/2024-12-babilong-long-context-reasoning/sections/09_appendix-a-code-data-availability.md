# Appendix A: Code and Data Availability [p. 16]

## Code and data repositories

Code for generating data and evaluating models is available at: https://github.com/booydar/babilong [p. 16]

## Pre-generated evaluation data

We also provide pre-generated evaluation data hosted on HuggingFace datasets. The evaluation sets include 100 samples per length and per task, with lengths from 0k (no background text from PG-19) to 10 million tokens: [p. 16]

- https://huggingface.co/datasets/RMT-team/babilong
- 1000 samples per length and per task with lengths from 0k to 128k tokens: https://huggingface.co/datasets/RMT-team/babilong-1k-samples

## Croissant metadata

The croissant metadata for both evaluation sets is available on HuggingFace: [p. 16]

- https://huggingface.co/api/datasets/RMT-team/babilong/croissant
- https://huggingface.co/api/datasets/RMT-team/babilong-1k-samples/croissant

## License information

Our code is released under the Apache 2.0 License. We use data from the PG-19 corpora (Rae et al., 2020) (Apache 2.0 License¹) and the bAbI dataset (Weston et al., 2016) (BSD License²). [p. 16]

¹https://github.com/google-deepmind/pg19
²https://github.com/facebookarchive/bAbI-tasks/blob/master/LICENSE.md

## A.1 Reproducibility [p. 16]

Our code includes data generation, metrics, and the evaluation pipeline used to benchmark models. Additionally, we release the predictions of all models used in our study to ensure that all reported results can be reproduced and verified: https://github.com/booydar/babilong/tree/predictions_06_2024 [p. 16]
