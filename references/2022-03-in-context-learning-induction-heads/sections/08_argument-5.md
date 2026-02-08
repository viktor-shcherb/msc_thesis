# Argument 5: For small models, we can explain mechanistically how induction heads work, and can show they contribute to in-context learning. Furthermore, the actual mechanism of operation suggests natural ways in which it could be re-purposed to perform more general in-context learning. [p. 25-26]

## Strength of argument for sub-claims [p. 25]

|                      | Small Attention-Only | Small with MLPs    | Large Models          |
|----------------------|----------------------|--------------------|-----------------------|
| Contributes Some     | Strong, Mechanistic  | Strong, Mechanistic| Medium, Mechanistic   |
| Contributes Majority | Weak, Mechanistic    |                    |                       |

## Semi-empirical argument [p. 25]

One of the main reasons the authors care about whether induction heads drive in-context learning is that they can understand them and so have a path to understanding in-context learning. But one can also turn this around: one can use the understanding of induction heads to make a purely logical argument that they *should* contribute to in-context learning. [p. 25]

The authors begin with a semi-empirical argument. If one takes for granted that induction heads behave the way they have been described and empirically seen -- searching the context for previous examples and copying what happened next -- then one should expect such a procedure to improve a model's ability to predict tokens later in its context. The authors frame this as essentially using the previous context as data points for a nearest neighbor algorithm, and nearest neighbors improves as one gives it more data points. Therefore, if induction heads exist as described, they would contribute to in-context learning as defined. [p. 25]

In some sense, this argument is quite strong if one is only arguing that there exist some cases where induction heads contribute to in-context learning. The authors have shown concrete examples above where induction heads improve token predictions by copying earlier examples. If nothing else, they must help in those cases. And more generally, the definition of induction heads (in terms of their behavior on repeated random sequences) suggests they behave this way quite generally. This argument does not say anything about *what fraction* of in-context learning is performed by induction heads, but it seems like a very strong argument that *some* is, both in large and small models. [p. 25]

## Reverse engineering argument [p. 25-26]

But the really satisfying thing about this line of attack -- namely, using the understanding of induction heads to anticipate their impact on in-context learning -- is that one can actually drop the dependency on empirical observations of induction head behavior, at the cost of needing to make a more complex argument. In the authors' previous paper, they were able to reverse engineer induction heads, showing from the parameter level how they implement induction behavior (and that they should). If one trusts this analysis, one can know how induction heads behave without actually running them, and the argument from the previous paragraph goes through. [p. 25-26]

Of course, there are some limitations. In the previous paper, the authors only reverse engineered a single induction head in a small attention-only model, although they can reverse engineer others (and have done so). A bigger issue is that right now they are unable to reverse engineer induction heads in models with MLP layers. But at least in some cases they have observed, they can look at the parameters of a transformer and identify induction heads, just as a programmer might identify an algorithm by reading through source code. [p. 26]

The authors can actually push this argument a bit further in the case of the two-layer attention-only transformer they reverse engineered in the previous paper. Not only do they understand the induction heads and know that they should contribute to in-context learning, but there does not seem to really be an alternative mechanism that could be driving it.^23 This suggests that induction heads are the primary driver of in-context learning, at least in very small models. [p. 26]

The following section will briefly summarize reverse engineering induction heads. Note that it relies heavily on linking to the previous paper. *We do not expect it to be possible to follow without reading the linked portions.* After that, the authors briefly discuss how the described mechanism could also implement more abstract types of induction head behavior. [p. 26]

## Summary of Reverse Engineering Induction Heads [p. 26]

> *Note: This section provides a dense summary with pointers to our previous paper; please see the previous paper for more information.* [p. 26]

Recall from Key Concepts that induction heads are defined as heads that exhibit both *copying* and *prefix matching*. [p. 26]

### Copying is done by the OV ("Output-Value") circuit [p. 26]

One of the defining properties of an induction head is that it copies. Induction heads are not alone in this -- transformers seem to have quite a number of copying heads, of which induction heads are a subset. This is done by having a "copying matrix" OV circuit, most easily characterized by its positive eigenvalues. [p. 26]

### Prefix matching is implemented with K-composition (and to a lesser extent Q-composition) in the QK ("Query-Key") Circuit [p. 26]

In order to do prefix matching, the key vector at the attended token needs to contain information about the *preceding* tokens -- in fact, information about the *attended token itself* is quite irrelevant to calculating the attention pattern for induction.^24 In the models the authors study, "key shifting" occurs primarily using what they call K-composition. That is to say that an induction head's $W_K$ reads from a subspace written to by an earlier attention head. The most basic form of an induction head uses pure K-composition with an earlier "previous token head" to create a QK-Circuit term of the form $\text{Id} \otimes h_{prev} \otimes W$ where $W$ has positive eigenvalues. This term causes the induction head to compare the *current* token with every earlier position's *preceding* token and look for places where they are similar. More complex QK circuit terms can be used to create induction heads which match on more than just the preceding token. [p. 26]

---
[p. 27 continued]

**Unnumbered figure** (p. 27): "Induction head mechanism diagrams." Two diagrams illustrating how induction heads use previous heads to shift key information and match it against the present token. As they get more sophisticated, they also shift query information.

- **Top diagram**: Shows a simple induction head operating on Harry Potter text (`out about the Potters. Mrs Potter was ... neighbours would say if the Pot[ters] arrived in`). Three rows show: (1) the attention pattern moving information from an earlier "Pot" token to the current position, creating a logit effect; (2) the key is set at the earlier "Pot" token position (highlighted in green); (3) the query is set at the current "Po" token (highlighted in red). The attention pattern (red arrow) moves information rightward, and the logit effect appears at the destination.

- **Bottom diagram**: Shows a more sophisticated induction head on text (`Mr and Mrs Dursley, of number ... with such nonsense. Mr D[urs]ley was the`). Similar three-row layout: (1) attention pattern moves information with logit effect; (2) the key is at the "D" position in the earlier "Dursley" occurrence (green); (3) the query is at the "Mr" token preceding the current position (red). This diagram illustrates that more sophisticated heads shift *both* key and query information.

Caption: "Induction heads use previous heads to shift key information and match it against the present token. As they get more sophisticated, they also shift query information."

### Combined, these are a detectable mechanism for induction heads [p. 27]

In the small models studied in the previous paper, all induction heads have the described QK term driving their attention pattern and a positive eigenvalue circuit performing copying. [p. 27]

### Some models use a different mechanism to implement induction heads [p. 27]

In GPT-2 [10], the authors have seen evidence of a second "pointer-arithmetic" mechanism for induction heads. This mechanism makes use of the positional embedding and "Q-composition". In GPT-2, the earlier attention head attends to previous copies of the current token, and its $W_{OV}$ circuit copies their positional embedding into a subspace in the present token. The induction head then uses Q-composition to rotate that position embedding one token forward, and thereby attend to the following token. This mechanism is not available to the models studied here, since they do not add positional information into the residual stream.^25 [p. 27]

## What About More Complex Induction Heads? [p. 27]

What about the induction heads seen in Argument 2 with more complex behavior? Can they also be reverse engineered? Do they operate on the same mechanisms? Presently, fully reverse engineering them is beyond the authors, since they exist in large models with MLPs, which they do not have a strong framework for mechanistically understanding. However, the authors hypothesize they are different in two ways: (1) using more complex QK terms rather than matching on just the previous token; and (2) matching and copying more abstract and sophisticated linguistic features, rather than precise tokens. [p. 27]

When the authors first introduced induction heads, they observed that they could be seen as a kind of "in-context nearest neighbor" algorithm. From this perspective, it seems natural that applying the same mechanism to more abstract features can produce more complex behavior. [p. 27]
