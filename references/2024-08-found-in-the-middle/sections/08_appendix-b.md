# B Implementation details [p. 13]

[p. 13] The authors utilize `tulu-2-7b` and `Vicuna-7b-v1.5-16k` as the base models. Both models consist of 32 decoder layers, each with 32 attention heads.

In applying attention calibration method to intervene model attention, they apply only to the last 16 decoder layers (and all of their attention heads). They find that intervening early layers may lead to unstable generation. They leave finding the best set of attention heads to intervene as future directions (Zhang et al., 2023).

In the experiments, they find attention calibration to be robust to the temperature term $t$ in Eq. 5. They set $t = 5e{-}5$ for all experiments.
