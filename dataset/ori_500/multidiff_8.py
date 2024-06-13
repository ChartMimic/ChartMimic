# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Assuming data values for the bar chart
categories = [
    "Random",
    "Sobol",
    "HCube",
    "No Context",
    "Partial Context",
    "Full Context",
]
values = [0.9, 0.8, 0.7, 0.6, 0.5, 0.3]

# Generate y values for the line chart with a monotonically decreasing array
# Creating arrays for y values with 26 numbers each and random add or subtract 0.01 to make them different
random_regret = np.linspace(0.33, 0.1, 26) + np.random.normal(0, 0.005, 26)
sobol_regret = np.linspace(0.28, 0.08, 26) + np.random.normal(0, 0.01, 26)
hcube_regret = np.linspace(0.26, 0.06, 26) + np.random.normal(0, 0.01, 26)
no_context_regret = np.linspace(0.24, 0.04, 26) + np.random.normal(0, 0.01, 26)
partial_context_regret = np.linspace(0.22, 0.03, 26) + np.random.normal(0, 0.01, 26)
full_context_regret = np.linspace(0.18, 0.01, 26) + np.random.normal(0, 0.01, 26)

# Axes Limits and Labels
xlabel_value_1 = "Generalized Variance"
xlim_values_1 = [0, 1]
xticks_all_1 = np.arange(0, 1.05, 0.05)
xticks_labeled_1 = np.arange(0, 1.1, 0.2)

xticks_2 = np.arange(0, 26, 1)
label_Random ="Random"
label_Sobol = "Sobol"
label_HCube = "HCube"
label_No_Context = "No Context"
ax2_label_1 = "Partial Context"
ax2_label_2 = "Full Context"
xlabel_value_2 = "Trials"
ylabel_value_2 = "Avg. Regret"
ylim_values_2 = [0, 0.37]
xticks_all_2 = np.arange(0, 26, 1)
xticks_labeled_2 = np.arange(0, 26, 5)

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create bar chart
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7, 9))
ax1.barh(categories, values, color="#6194bf")
ax1.set_xlabel(xlabel_value_1)
ax1.set_xlim(xlim_values_1)

# Add more x-ticks but only label some of them
all_xticks = xticks_all_1
labeled_xticks = xticks_labeled_1
ax1.set_xticks(all_xticks)
ax1.set_xticklabels(
    [f"{tick:.1f}" if tick in labeled_xticks else "" for tick in all_xticks]
)

# Create line chart
trials = xticks_2
ax2.plot(trials, random_regret, label=label_Random, color="blue")
ax2.plot(trials, sobol_regret, label=label_Sobol, color="green")
ax2.plot(trials, hcube_regret, label=label_HCube, color="orange")
ax2.plot(trials, no_context_regret, label=label_No_Context, color="purple", linestyle=":")
ax2.plot(
    trials,
    partial_context_regret,
    label=ax2_label_1,
    color="purple",
    linestyle="--",
)
ax2.plot(
    trials, full_context_regret, label=ax2_label_2, color="purple", linestyle="-"
)
ax2.set_xlabel(xlabel_value_2)
ax2.set_ylabel(ylabel_value_2)

# Set the y limit to match the uploaded image aspect
ax2.set_ylim(ylim_values_2)
ax2.legend(loc="upper right", frameon=False)
all_xticks = xticks_all_2
labeled_xticks = xticks_labeled_2
ax2.set_xticks(all_xticks)
ax2.set_xticklabels(
    [f"{tick}" if tick in labeled_xticks else "" for tick in all_xticks]
)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('multidiff_8.pdf', bbox_inches='tight')
