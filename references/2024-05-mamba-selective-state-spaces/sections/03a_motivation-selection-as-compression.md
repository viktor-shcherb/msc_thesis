# Selective State Space Models [p. 5]

Section 3 motivates the selection mechanism using intuition from synthetic tasks (Section 3.1), then explains how to incorporate this mechanism into state space models (Section 3.2). The resulting time-varying SSMs cannot use convolutions, presenting a technical challenge of how to compute them efficiently. This is overcome with a hardware-aware algorithm that exploits the memory hierarchy on modern hardware (Section 3.3). A simple SSM architecture without attention or even MLP blocks is then described (Section 3.4). Finally, additional properties of selection mechanisms are discussed (Section 3.5). [p. 5]

## Motivation: Selection as a Means of Compression

[p. 5]

The authors argue that a fundamental problem of sequence modeling is *compressing context into a smaller state*. They view the tradeoffs of popular sequence models from this point of view:

- **Attention** is both effective and inefficient because it explicitly does not compress context at all. Autoregressive inference requires explicitly storing the entire context (i.e. the KV cache), which directly causes the slow linear-time inference and quadratic-time training of Transformers.
- **Recurrent models** are efficient because they have a finite state, implying constant-time inference and linear-time training. However, their effectiveness is limited by how well this state has compressed the context.

The efficiency vs. effectiveness tradeoff of sequence models is characterized by how well they compress their state: efficient models must have a small state, and effective models must have a state that contains all necessary information from the context. The authors propose that a fundamental principle for building sequence models is **selectivity**: the context-aware ability to focus on or filter out inputs into a sequential state. A selection mechanism controls how information propagates or interacts along the sequence dimension (see Section 3.5 for more discussion). [p. 5]

### Motivating Synthetic Tasks

Two running examples of synthetic tasks (Figure 2) are used to understand this principle: [p. 5]

- The **Selective Copying** task modifies the popular Copying task (Arjovsky, Shah, and Bengio 2016) by varying the position of the tokens to memorize. It requires *content-aware* reasoning to be able to memorize the relevant tokens (*colored*) and filter out the irrelevant ones (*white*).
- The **Induction Heads** task is a well-known mechanism hypothesized to explain the majority of in-context learning abilities of LLMs (Olsson et al. 2022). It requires *context-aware* reasoning to know when to produce the correct output in the appropriate context (*black*).

These tasks reveal the failure mode of LTI models. From the recurrent view, their constant dynamics (e.g. the $(\overline{\boldsymbol{A}}, \overline{\boldsymbol{B}})$ transitions in (2)) cannot let them select the correct information from their context, or affect the hidden state passed along the sequence in an input-dependent way. From the convolutional view, it is known that global convolutions can solve the vanilla Copying task (Romero et al. 2021) because it only requires time-awareness, but that they have difficulty with the Selective Copying task because of lack of content-awareness (Figure 2). More concretely, the spacing between inputs-to-outputs is varying and cannot be modeled by static convolution kernels. [p. 5]

## Figures

**Figure 2** (p. 6): "(*Left*) The standard version of the Copying task involves constant spacing between input and output elements and is easily solved by time-invariant models such as linear recurrences and global convolutions. (*Right Top*) The Selective Copying task has random spacing in between inputs and requires time-varying models that can *selectively* remember or ignore inputs depending on their content. (*Right Bottom*) The Induction Heads task is an example of associative recall that requires retrieving an answer based on context, a key ability for LLMs."

The figure shows three diagrams. Left ("Copying"): input row of colored blocks with constant spacing maps to output row; solution is straightforward for LTI models (e.g. convolutional) that do not need to look at the actual inputs. Right top ("Selective Copying"): similar but with random spacing between colored tokens in the input, requiring content-aware selection. Right bottom ("Induction Heads"): a sequence of colored blocks with a query marker "?" requiring the model to recall the token that followed a matching pattern earlier in the sequence.
