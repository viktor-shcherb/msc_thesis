"""SmolLM3-3B plasticity trajectory across training checkpoints."""
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

# --- Data (from smollm3_model_report.csv, chronological order) ---
checkpoints = [
    "40K",
    "1.2M",
    "2.4M",
    "3.44M",
    "4.2M",
    "4.72M",
    "LC\n4→32K\n4K",
    "LC\n4→32K\n20K",
    "LC\n32→64K\n4K",
    "LC\n32→64K\n20K",
]
short_labels = [
    "40K", "1.2M", "2.4M", "3.44M", "4.2M", "4.72M",
    "LC1\n4K", "LC1\n20K", "LC2\n4K", "LC2\n20K",
]

ap_first = [0.6094, 0.5787, 0.5817, 0.5793, 0.5854, 0.5521, 0.5855, 0.5821, 0.5905, 0.5879]
ap_last  = [0.5695, 0.5165, 0.5206, 0.5220, 0.5235, 0.4940, 0.4325, 0.4356, 0.4222, 0.4270]
ap_drop  = [f1 - l1 for f1, l1 in zip(ap_first, ap_last)]

# Rotation bias_strength (from rotated.csv, same checkpoint order)
bias_str = [0.0092, 0.0160, 0.0165, 0.0166, 0.0168, 0.0194, 0.0032, 0.0032, 0.0018, 0.0018]

x = np.arange(len(checkpoints))

# --- Plot ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 5.5), sharex=True,
                                gridspec_kw={"height_ratios": [3, 1.3], "hspace": 0.08})

# Top panel: plasticity lines
ax1.plot(x, ap_first, "o-", color="#2166ac", linewidth=2, markersize=6, label="$\\mathrm{AP}_{\\mathrm{first\\ 20\\%}}$")
ax1.plot(x, ap_last,  "s-", color="#b2182b", linewidth=2, markersize=6, label="$\\mathrm{AP}_{\\mathrm{last\\ 20\\%}}$")

# Shade the gap (ap_drop)
ax1.fill_between(x, ap_last, ap_first, alpha=0.15, color="#762a83", label="$\\mathrm{AP}_{\\mathrm{drop}}$")

# Phase separators
for boundary in [5.5]:
    ax1.axvline(boundary, color="gray", linestyle="--", linewidth=0.8, alpha=0.6)

# Phase labels
ax1.text(2.5, 0.62, "Pre-training (4K ctx)", ha="center", va="bottom", fontsize=9, color="gray", style="italic")
ax1.text(7.75, 0.62, "LC extension", ha="center", va="bottom", fontsize=9, color="gray", style="italic")

ax1.set_ylabel("Attention Plasticity", fontsize=11)
ax1.set_ylim(0.38, 0.64)
ax1.legend(loc="lower left", fontsize=9, framealpha=0.9)
ax1.grid(True, alpha=0.3)

# Bottom panel: bias_strength
ax2.bar(x, bias_str, color="#4dac26", alpha=0.7, width=0.6)
ax2.set_ylabel("bias strength", fontsize=10)
ax2.set_ylim(0, 0.022)
ax2.axvline(5.5, color="gray", linestyle="--", linewidth=0.8, alpha=0.6)
ax2.grid(True, alpha=0.3, axis="y")

ax2.set_xticks(x)
ax2.set_xticklabels(short_labels, fontsize=8)
ax2.set_xlabel("Training Checkpoint", fontsize=11)

# Format y-axis
ax2.yaxis.set_major_formatter(mticker.FormatStrFormatter("%.3f"))

fig.align_ylabels([ax1, ax2])
plt.tight_layout()
plt.savefig("/Users/Viktor/PycharmProjects/msc_thesis/figures/attention-plasticity/09_smollm3_trajectory/figure.png",
            dpi=200, bbox_inches="tight")
plt.savefig("/Users/Viktor/PycharmProjects/msc_thesis/figures/attention-plasticity/09_smollm3_trajectory/figure.pdf",
            bbox_inches="tight")
print("Done: 09_smollm3_trajectory")
