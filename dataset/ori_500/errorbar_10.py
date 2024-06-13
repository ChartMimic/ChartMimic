# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data
number_of_experts = [1, 2, 3, 4]
baseline = [6] * len(number_of_experts)
softmoe_unchanged = [5.8, 6.2, 7.5, 6.4]
softmoe_div_numexperts = [5.7, 6.1, 6.9, 6.2]
errors = [0.2, 0.15, 0.1, 0.05]

# Labels and Plot Types
label1 = "SoftMoE (unchanged)"
label2 = "SoftMoE (÷ NumExperts)"
label3 = "Baseline"

# Axes Limits and Labels
xlabel_value = "Number of experts"
ylabel_value = "IQM Human Normalized Score"
title = "Expert dimension"
xticklabels = ["1", "2", "4", "8"]
ylim_values = [5, 8]
yticks_values = np.arange(5, 8, 1)
legend_title = "Expert dimension"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting
fig, ax = plt.subplots(figsize=(8, 6))  # Adjusted for the given dimensions
bar_width = 0.4
opacity = 0.8

bar1 = ax.bar(
    np.array(number_of_experts) - bar_width / 2,
    softmoe_unchanged,
    bar_width,
    alpha=opacity,
    color="#41886c",
    label=label1,
    yerr=errors,
    capsize=3,
)

bar2 = ax.bar(
    np.array(number_of_experts) + bar_width / 2,
    softmoe_div_numexperts,
    bar_width,
    alpha=opacity,
    color="#b886b3",
    label=label2,
    yerr=errors,
    capsize=3,
)

ax.plot(
    number_of_experts,
    baseline,
    linestyle="--",
    color="b",
    linewidth=2,
    label=label3,
)

ax.set_xlabel(xlabel_value)
ax.set_ylabel(ylabel_value)
ax.set_title(title)
ax.set_xticks(number_of_experts)
ax.set_xticklabels(xticklabels)
ax.set_ylim(ylim_values)
ax.set_yticks(yticks_values)
ax.legend(loc="upper left", title=legend_title)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("errorbar_10.pdf", bbox_inches="tight")
