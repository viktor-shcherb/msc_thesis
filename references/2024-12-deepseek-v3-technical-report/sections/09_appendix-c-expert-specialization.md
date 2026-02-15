# Appendix C. Expert Specialization Patterns of the 16B Aux-Loss-Based and Aux-Loss-Free Models [p. 48–51]

This appendix records the expert load of the 16B auxiliary-loss-based baseline and the auxiliary-loss-free model on the Pile test set [p. 48].

**Key finding:**
The auxiliary-loss-free model tends to have greater expert specialization across all layers, as demonstrated in Figure 10 [p. 48].

## Figure 10: Expert Load Comparison [p. 49–53]

**Figure 10** (p. 49–53): "Expert load of auxiliary-loss-free and auxiliary-loss-based models on three domains in the Pile test set. The auxiliary-loss-free model shows greater expert specialization patterns than the auxiliary-loss-based one. The relative expert load denotes the ratio between the actual expert load and the theoretically balanced expert load."

Description: Multi-panel heatmap visualization spanning five subfigures (a-e) showing expert load patterns across 26 layers.
- Key elements: Each subfigure contains heatmaps comparing Aux-Loss-Based and Aux-Loss-Free models for consecutive layers
- Y-axis: Three data domains (Wikipedia (en), Github, DM Mathematics)
- X-axis: Expert indices (numbered sequentially)
- Color scale: Relative expert load from 0 (light yellow) to 10 (dark red), representing the ratio between actual and theoretically balanced expert load
- Notable patterns: Aux-loss-free model consistently shows more concentrated high-intensity regions (darker red areas) indicating greater expert specialization, while aux-loss-based model shows more uniform, balanced distributions
- Supports claim: Demonstrates that auxiliary-loss-free load balancing strategy enables greater expert specialization across all model layers [p. 48]

The figure is organized into five subfigures:
- (a) Layers 1-7 [p. 49]
- (b) Layers 7-13 [p. 50]
- (c) Layers 13-19 [p. 51]
- (d) Layers 19-25 [p. 52]
- (e) Layers 25-27 [p. 53]

### Detailed Layer-by-Layer Analysis

The following sections provide detailed descriptions of expert load patterns for each layer shown in Figure 10.

### Layers 1-7 [p. 49]
*Figure 10(a)*

**Aux-Loss-Based Layer 1:**
Heatmap showing relatively uniform expert load distribution across all three domains with occasional moderate peaks.

**Aux-Loss-Free Layer 1:**
Heatmap showing higher specialization with more concentrated expert loads, particularly visible in certain expert indices.

**Aux-Loss-Based Layer 2:**
Shows distributed expert load with some concentration in middle expert indices.

**Aux-Loss-Free Layer 2:**
Displays more pronounced specialization patterns with distinct peaks across different experts for different domains.

**Aux-Loss-Based Layer 3:**
Exhibits relatively balanced expert load distribution with minor variations.

**Aux-Loss-Free Layer 3:**
Shows clear specialization with multiple strong peaks (red regions) indicating certain experts handling specific domain content.

**Aux-Loss-Based Layer 4:**
Maintains fairly uniform distribution across experts with gradual variations.

**Aux-Loss-Free Layer 4:**
Demonstrates significant specialization with concentrated high loads on specific experts.

**Aux-Loss-Based Layer 5:**
Shows moderate expert load distribution without extreme concentrations.

**Aux-Loss-Free Layer 5:**
Exhibits strong specialization with particularly high loads on select experts, notably in DM Mathematics domain.

**Aux-Loss-Based Layer 6:**
Displays relatively even expert utilization across the layer.

**Aux-Loss-Free Layer 6:**
Shows marked specialization with distinct expert preferences varying by domain, particularly strong activation in DM Mathematics.

**Aux-Loss-Based Layer 7:**
Maintains balanced expert load distribution.

**Aux-Loss-Free Layer 7:**
Demonstrates clear specialization patterns with multiple high-intensity regions across different experts.

### Layers 7-13 [p. 50]
*Figure 10(b)*

**Aux-Loss-Based Layer 8:**
Shows generally uniform expert utilization with minor peaks.

**Aux-Loss-Free Layer 8:**
Exhibits increased specialization with concentrated expert loads in specific regions.

**Aux-Loss-Based Layer 9:**
Maintains relatively balanced distribution across experts.

**Aux-Loss-Free Layer 9:**
Shows strong specialization with distinct high-load regions for different domains.

**Aux-Loss-Based Layer 10:**
Displays moderate expert load variation without extreme concentrations.

**Aux-Loss-Free Layer 10:**
Demonstrates clear specialization with high-intensity expert activations.

**Aux-Loss-Based Layer 11:**
Shows fairly uniform expert utilization.

**Aux-Loss-Free Layer 11:**
Exhibits significant specialization with multiple concentrated peaks across experts.

**Aux-Loss-Based Layer 12:**
Maintains balanced expert load distribution.

**Aux-Loss-Free Layer 12:**
Shows pronounced specialization patterns with domain-specific expert preferences.

### Layers 13-19 [p. 51]
*Figure 10(c)*

**Aux-Loss-Based Layer 13:**
Displays relatively uniform expert load across the layer.

**Aux-Loss-Free Layer 13:**
Shows moderate specialization with some concentrated regions.

**Aux-Loss-Based Layer 14:**
Maintains balanced distribution without strong peaks.

**Aux-Loss-Free Layer 14:**
Exhibits clear specialization with distinct high-load experts for specific domains.

**Aux-Loss-Based Layer 15:**
Shows even expert utilization across the layer.

**Aux-Loss-Free Layer 15:**
Demonstrates significant specialization with multiple high-intensity regions.

**Aux-Loss-Based Layer 16:**
Displays relatively uniform expert load distribution.

**Aux-Loss-Free Layer 16:**
Shows strong specialization patterns with concentrated expert activations.

**Aux-Loss-Based Layer 17:**
Maintains balanced expert utilization.

**Aux-Loss-Free Layer 17:**
Exhibits clear specialization with varying expert preferences across domains.

**Aux-Loss-Based Layer 18:**
Shows moderate, fairly uniform expert load distribution.

**Aux-Loss-Free Layer 18:**
Demonstrates specialization with concentrated high loads on specific experts.

### Layers 19-25 [p. 52]
*Figure 10(d)*

**Aux-Loss-Based Layer 19:**
Displays relatively uniform expert load distribution across all three domains.

**Aux-Loss-Free Layer 19:**
Shows clear specialization with multiple concentrated regions, particularly visible in Github and DM Mathematics domains.

**Aux-Loss-Based Layer 20:**
Maintains balanced expert utilization without extreme peaks.

**Aux-Loss-Free Layer 20:**
Exhibits significant specialization with strong activations in specific expert indices across different domains.

**Aux-Loss-Based Layer 21:**
Shows fairly uniform expert load across the layer.

**Aux-Loss-Free Layer 21:**
Demonstrates pronounced specialization with distinct high-load regions, notably concentrated activations in DM Mathematics.

**Aux-Loss-Based Layer 22:**
Displays relatively even expert distribution.

**Aux-Loss-Free Layer 22:**
Shows clear specialization patterns with concentrated expert loads, particularly strong activation in DM Mathematics domain.

**Aux-Loss-Based Layer 23:**
Maintains balanced expert load without strong concentrations.

**Aux-Loss-Free Layer 23:**
Exhibits significant specialization with multiple high-intensity regions across domains, with notable peaks in Github and DM Mathematics.

**Aux-Loss-Based Layer 24:**
Shows moderate, fairly uniform expert utilization.

**Aux-Loss-Free Layer 24:**
Demonstrates strong specialization with concentrated high loads on specific experts, showing distinct patterns for different domains.

### Layers 25-27 [p. 53]
*Figure 10(e)*

**Aux-Loss-Based Layer 25:**
Displays relatively uniform expert load distribution.

**Aux-Loss-Free Layer 25:**
Shows pronounced specialization with multiple concentrated high-intensity regions, particularly in Github and DM Mathematics domains.

**Aux-Loss-Based Layer 26:**
Maintains balanced expert utilization across the layer.

**Aux-Loss-Free Layer 26:**
Exhibits strong specialization patterns with distinct expert preferences varying significantly across domains, showing particularly concentrated activations in specific expert indices.

## Summary of Patterns [p. 48–51]

**Overall trend:**
Across all 18 layers shown, the auxiliary-loss-free model consistently exhibits greater expert specialization compared to the auxiliary-loss-based baseline [p. 48]. This is visible in:
- More concentrated high-intensity regions (darker red areas) in aux-loss-free heatmaps
- More diverse expert activation patterns across different domains
- Stronger domain-specific expert preferences in the aux-loss-free model

**Auxiliary-loss-based model:**
- Shows more uniform, balanced expert load distribution
- Lower peak intensities in expert activations
- Less variation in expert utilization across different domains

**Auxiliary-loss-free model:**
- Shows distinct specialization patterns with high-intensity peaks
- Different experts specialize for different content domains
- More pronounced variation in relative expert load (higher maximum values on color scale)
- This greater specialization occurs across all layers tested
