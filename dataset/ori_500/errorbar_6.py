# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data for the left plot (Out-of-domain accuracy)
left_categories = [
    "all",
    "arg_causal",
    "test_0",
    "test_1",
    "test_2",
    "test_3",
    "test_4",
    "test_5",
    "test_6",
    "constant",
]
left_means = [0.832, 0.828, 0.830, 0.829, 0.830, 0.829, 0.828, 0.827, 0.826, 0.826]
left_errors = [0.002] * 10

# Data for the right plot (Shift gap)
right_categories = [
    "all",
    "arg_causal",
    "test_0",
    "test_1",
    "test_2",
    "test_3",
    "test_4",
    "test_5",
    "test_6",
    "constant",
]
right_means = [0.040, 0.035, 0.036, 0.036, 0.036, 0.036, 0.036, 0.036, 0.036, 0.035]
right_errors = [0.005] * 10

title1 = "Out-of-domain accuracy"
ylim1 = [0.824, 0.835]
yticks1 = np.arange(0.824, 0.835, 0.002)
title2 = "Shift gap"
ylim2 = [0, 0.050]
suptitle = "Diabetes"


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Left plot
ax1.bar(
    left_categories,
    left_means,
    yerr=left_errors,
    color=["#c53a32"] + ["#9ab6bd"] + ["#678c95"] * 7 + ["#454545"],
    capsize=5,
    error_kw=dict(ecolor="black", lw=1, capsize=5, capthick=2),
)
ax1.set_title(title1)
ax1.set_ylim(ylim1)
ax1.set_yticks(yticks1)
ax1.set_xticklabels(left_categories, rotation=90, ha="center")
ax1.tick_params(axis="both", length=0)  # Hide tick marks
ax1.grid(True)
ax1.set_axisbelow(True)
for spine in ax1.spines.values():
    spine.set_color("gray")

# Right plot
ax2.bar(
    right_categories,
    right_means,
    yerr=right_errors,
    color=["#c53a32"] + ["#9ab6bd"] + ["#678c95"] * 7 + ["#454545"],
    capsize=5,
    error_kw=dict(ecolor="black", lw=1, capsize=5, capthick=2),
)
ax2.set_title(title2)
ax2.set_ylim(ylim2)
ax2.set_xticklabels(right_categories, rotation=90, ha="center")
ax2.tick_params(axis="both", length=0)  # Hide tick marks
ax2.grid(True)
ax2.set_axisbelow(True)

# Set the title for the entire figure
fig.suptitle(suptitle)

for spine in ax2.spines.values():
    spine.set_color("gray")

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the figure
plt.tight_layout()
plt.savefig("errorbar_6.pdf", bbox_inches="tight")
