# 8 Conclusion [p. 9]

The authors have observed that MHA does not always leverage its theoretically superior expressiveness over vanilla attention to the fullest extent. Specifically, they demonstrated that in a variety of settings, several heads can be removed from trained transformer models without statistically significant degradation in test performance, and that some layers can be reduced to only one head.

Additionally, they have shown that in machine translation models, the encoder-decoder attention layers are much more reliant on multi-headedness than the self-attention layers, and provided evidence that the relative importance of each head is determined in the early stages of training.

> "We hope that these observations will advance our understanding of MHA and inspire models that invest their parameters and attention more efficiently." [p. 9]

## Acknowledgments [p. 9]

The authors thank anonymous reviewers for their feedback. They are particularly grateful to Thomas Wolf from Hugging Face, whose independent reproduction efforts allowed them to find and correct a bug in the speed comparison experiments. Research was supported in part by a gift from Facebook.
