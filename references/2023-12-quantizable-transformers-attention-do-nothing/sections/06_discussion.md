# 6 Discussion [p. 10]

## "No-op" behavior

[p. 10] The identified "no-op" behavior is likely not limited to transformers and convolutional architectures likely learn something similar. Despite the network trying to learn a full "no-op", still a small amount of noise is added to each residual, which may constitute a form of network regularization. Investigating this further might give a clue as to why neural networks generalize despite being significantly overparametrized if many parameters are rendered unused by not updating the representation in later layers [72].

## Limitations

[p. 10] While the scalability of the method is studied for models up to 1.3B size, the case of very large transformers that are trained for way longer has not been explored. Given the fundamental understanding of the issue underlying the solutions, the same effect on larger-scale models is expected. A very small improvement in FP16/FP32 performance is shown due to the methods, but the results are not deemed exhaustive enough to claim that this will hold in general. Lastly, both methods do have a hyperparameter each, although both methods are shown to be relatively robust to their hyperparameter, and having one is never optimal.

## Impact

[p. 10] As the methods help transformers to be more efficient, the authors expect only positive outcomes of the work. Making neural networks more efficient will help with their high power consumption at inference. It further helps to move inference from the cloud to edge devices which can overcome potential privacy concerns.
