# 3 Does RoPE decay activations with distance? [p. 4–5]

## Challenging the Common Claim

In this section, we argue against the common claim that RoPE is helpful because it helps to decay activations as the relative distance between tokens increases. Such claims often work under the assumption that queries and keys are for instance a vector with all entries equal to each other, which we believe is an unrealistic oversimplification⁵. Importantly, this claim was originally provided by the authors of RoPE (Su et al., 2024) as a justification for the chosen structure of the encoding. Follow up works have used this claim to justify other choices, such as increasing the base wavelength θ to 500,000. We therefore find it important to point out cases in which this decay does not in fact occur [p. 4].

## Proposition 3.1: RoPE Can Be Maximal at Arbitrary Distance

**Proposition 3.1** (RoPE can be maximal at arbitrary distance). *Given any query* **q** *and any relative distance* r ∈ ℤ, *we can find a key* **k** *such that the attention value is maximal at distance* r *with RoPE*.

We start by showing, in Proposition 3.1 that given any key, we can find a query such that RoPE is maximal for any chosen relative distance. This exploits the fact that RoPE provides Transformers with *robust* ways to attend to specific relative distances. In fact, we will show, in Section 4, that this mechanism is what Gemma 7B uses to construct heads that attend to specific positions. We provide the proof in the Appendix (Section A.1) [p. 4–5].

## Proposition 3.2: Gaussian Queries and Keys Do Not Decay

**Proposition 3.2** (Gaussian queries and keys do not decay). *Let* **q**, **k** ∼ N(0, I). *Then, for any relative distance* r ∈ ℤ, *we have that*:

```
𝔼[q,k∼N(0,I)] [q^⊤ R^r k] = 0.
```

Next, in Proposition 3.2, we show that given queries and keys sampled independently from a standard multivariate Gaussian, the expected value of the activations is 0. Moreover, this is independent of the relative distance of the queries and keys – implying that the expected value of the activations is independent of the relative distance when the queries and keys are sampled from a Gaussian. We provide the proof in the Appendix (Section A.1) [p. 5].

## Empirical Verification

We showcase this by constructing a synthetic experiment in which we either set queries and keys as all-ones vectors, e.g. as done by Su et al. (2024); Xiong et al. (2023), or sample entries independently from a Gaussian, accounting for appropriate normalisation. Figure 2 shows the results. While there seems to be some form of decay of the activations as relative distance increases when the queries and keys are all-ones vectors (a) – up to appropriate normalisation, this is clearly not the case when the queries and keys are instead random Gaussian vectors (b) [p. 5].

**Figure 2** (p. 4): "RoPE applied to either (a) constant 'all-ones' queries and keys or (b) queries and keys with entries sampled IID from a Gaussian. The decay of the activations is present when the queries and keys are constant all-ones vectors, but not when they are Gaussian random vectors."

Description: Two line plots comparing activation patterns
- (a) Constant queries and keys: Shows clear decay curve from 1.0 to near 0.0 over relative distance 0-5000
- (b) Gaussian queries and keys: Shows noisy fluctuation around 0.0 with no clear decay pattern over relative distance 0-5000
- Key elements: X-axis shows "Relative Distance", Y-axis shows "Activation"
- Notable patterns: Stark contrast between the predictable decay in constant case versus no decay in Gaussian case
- Supports claim: Empirically demonstrates that RoPE decay is not universal and depends on the structure of queries and keys

## Section Summary

**Summary of the Section:** *While RoPE helps to decay activations with relative distance in very specific conditions, this does not have to happen. In fact, we will see in the next section that this is something that Gemma 7B exploits to create specific attention patterns* [p. 5].

---

⁵Intuitively, Su et al. (2024) ask the question of what happens, as we vary the relative distance, to the dot product between already aligned queries and keys, whose product *can increase* with relative distance. However, this perspective ignores what happens to originally misaligned queries and keys, whose product can *increase* with relative distance.
