# Appendix C: Details on the zsRE Evaluation Task [p. 23-24]

[p. 23] zsRE setup notes:

- Task originally from Levy et al. (2017), reused in model-editing work by De Cao et al. (2021) and Mitchell et al. (2021).
- Authors use Mitchell et al. train/test split; methods not requiring training discard training split.
- Each record contains factual statement, paraphrase prompts, and neighborhood prompts.

[p. 23-24] Additional baselines:

- KE-zsRE and MEND-zsRE custom-trained on zsRE split to reduce distribution mismatch versus default KE/MEND checkpoints.
