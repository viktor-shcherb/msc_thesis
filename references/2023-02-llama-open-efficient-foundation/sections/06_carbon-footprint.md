# 6 Carbon footprint [p. 10-11]

[p. 10] The training of the models consumed a massive quantity of energy, responsible for the emission of carbon dioxide. The recent literature on the subject is followed, and both the total energy consumption and the resulting carbon footprint are broken down in Table 15. A formula from Wu et al. (2022) is followed to estimate the Watt-hour, Wh, needed to train a model, as well as the tons of carbon emissions, tCO2eq. For the Wh, the formula used is:

Wh = GPU-h x (GPU power consumption) x PUE,

where the Power Usage Effectiveness (PUE) is set at 1.1. The resulting carbon emission depends on the location of the data center used to train the network. For instance, BLOOM uses a grid that emits 0.057 kg CO2eq/KWh leading to 27 tCO2eq and OPT a grid that emits 0.231 kg CO2eq/KWh, leading to 82 tCO2eq. In this study, the interest is in comparing the cost in carbon emission of training of these models if they were trained in the same data center. Hence, the location of data center in consideration is not taken, and use, instead, the US national average carbon intensity factor of 0.385 kg CO2eq/KWh. This leads to the following formula for the tons of carbon emissions: [p. 10]

tCO2eq = MWh x 0.385.

[p. 10-11] The same formula is applied to OPT and BLOOM for fair comparison. For OPT, training required 34 days on 992 A100-80GB (see their logs, footnote 4: https://github.com/facebookresearch/metaseq/tree/main/projects/OPT/chronicles). It is estimated that 2048 A100-80GB were used for a period of approximately 5 months to develop the models. This means that developing these models would have cost around 2,638 MWh under the assumptions, and a total emission of 1,015 tCO2eq. The hope is that releasing these models will help to reduce future carbon emission since the training is already done, and some of the models are relatively small and can be run on a single GPU. [p. 10-11]

**Table 15** (p. 11): **Carbon footprint of training different models in the same data center.** Following Wu et al. (2022) to compute carbon emission of training OPT, BLOOM and the authors' models in the same data center. For the power consumption of a A100-80GB, the thermal design power for NVLink systems is taken, that is 400W. A PUE of 1.1 and a carbon intensity factor set at the national US average of 0.385 kg CO2e per KWh are used.

| | GPU Type | GPU Power consumption | GPU-hours | Total power consumption | Carbon emitted (tCO2eq) |
|---|---|---|---|---|---|
| OPT-175B | A100-80GB | 400W | 809,472 | 356 MWh | 137 |
| BLOOM-175B | A100-80GB | 400W | 1,082,880 | 475 MWh | 183 |
| | | | | | |
| LLaMA-7B | A100-80GB | 400W | 82,432 | 36 MWh | 14 |
| LLaMA-13B | A100-80GB | 400W | 135,168 | 59 MWh | 23 |
| LLaMA-33B | A100-80GB | 400W | 530,432 | 233 MWh | 90 |
| LLaMA-65B | A100-80GB | 400W | 1,022,362 | 449 MWh | 173 |
