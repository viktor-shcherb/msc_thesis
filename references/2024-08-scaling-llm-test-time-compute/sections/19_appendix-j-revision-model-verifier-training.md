# Appendix J. Revision Model Verifier Training [p. 26–27]

[p. 26] The authors found that the PRM they finetuned on the PaLM 2-S* base model outputs was not as effective when applied to the PaLM 2-S* revision model's outputs (see Figure 15(a)), likely due to distribution shift with the revision model. They therefore determined that it would be better to use with their PaLM 2-S* revision model an ORM verifier that is separately trained on the revision model outputs. They could have trained a PRM as well, but opted for an ORM due to the high cost of generating per-step PRM labels.

[p. 26] They modified the standard ORM slightly for the revision setting, by finetuning the ORM with previous revision in context, such that the verifier has access to the same context as the revision model, allowing the verifier see the revision model's previous answer attempts when scoring the current answer. All other experiment details are identical to those used in training the PRM.

[p. 27] Empirically, they find that including the revision history in context improves performance slightly (see Figure 15(b)). Additionally, even without the revisions in context, they see that sequential revisions still slightly outperforms parallel, demonstrating improvements from sequential sampling are not just due to the verifier's context.

**Figure 15** (p. 27): Two-panel comparison of verifier training approaches

Description: Two line plots showing MATH Test Accuracy (%) vs Number of Generations (log scale from 2^0 to 2^6)

Left panel: "Revision Model Verifier Versus Base-LM PRM"
- Three lines: Sequential + Revision ORM (blue, top), Sequential + Base LM PRM (red, middle), Parallel (orange, bottom)
- Shows performance from ~18% at 2^0 to ~40% at 2^6 generations
- Sequential + Revision ORM reaches highest performance (~40%)
- Sequential + Base LM PRM reaches ~38%
- Parallel baseline reaches ~37%

Right panel: "Revision Model Verifier With Versus Without History"
- Three lines: Sequential + Verifier With History (blue, top), Sequential + Verifier Without History (red, middle), Parallel (orange, bottom)
- Shows performance from ~18% at 2^0 to ~40% at 2^6 generations
- With history reaches ~40%
- Without history reaches ~39%
- Parallel baseline reaches ~37%

Key findings:
- The ORM adapted to the revision model outperforms the PRM trained on base model outputs, likely due to distribution shift with the revision model
- Including previous revisions in-context helps the verifier slightly, but both settings still outperform the parallel baseline
- Sequential revisions improve over parallel even without revision history in verifier context, showing benefits are not solely due to context
