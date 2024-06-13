# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Dummy data for the purpose of plotting. In a real scenario, you would use your actual data.
number_of_experts = np.array([1, 2, 4, 8])

# IQM Human Normalized Score for DoN
baseline_don = np.array([3, 3.1, 3.2, 3.2])
softmoe_don = np.array([2.5, 2.7, 2.9, 3.1])
top1moe_don = np.array([2, 2.3, 2.5, 2.6])

# Error for DoN
error_don = np.array([0.1, 0.1, 0.1, 0.1])

# IQM Human Normalized Score for Rainbow
baseline_rainbow = np.array([4, 5, 6, 7])
softmoe_rainbow = np.array([5, 5.5, 6.5, 7])
top1moe_rainbow = np.array([6, 6.3, 7, 7.5])

# Error for Rainbow
error_rainbow = np.array([0.2, 0.2, 0.2, 0.2])

# Axes Limits and Labels
ylabel_value_1 = "DoN"
ylabel_value_2 ="Rainbow"
ylim_values_1 = [1.8, 3.8]
yticks_values_1 = [2.0, 2.5, 3.0, 3.5]
ylim_values_2 = [3.0, 8.0]
yticks_values_2 = [
        3.5,
        4.5,
        5.5,
        6.5,
        7.5,
    ]

# Labels
label_Baseline = "Baseline"
label_SoftMoE = "SoftMoE"
label_Top1_MoE = "Top1-MoE"

# Texts
text_1 = "Number of experts"
text_2 = "IQM Human Normalized Score"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create two subplots and unpack the output array immediately
f, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6))

# First subplot for DoN
ax1.errorbar(
    number_of_experts,
    baseline_don,
    yerr=error_don,
    label=label_Baseline,
    color="#3171ad",
    marker="o",
)
ax1.errorbar(
    number_of_experts,
    softmoe_don,
    yerr=error_don,
    label=label_SoftMoE,
    color="#469c76",
    marker="o",
)
ax1.errorbar(
    number_of_experts,
    top1moe_don,
    yerr=error_don,
    label=label_Top1_MoE,
    color="#c17cb9",
    marker="o",
)
ax1.set_ylabel(ylabel_value_1)
# Set grid
ax1.grid(True)
ax1.set_ylim(ylim_values_1)
ax1.set_yticks(yticks_values_1)

# Second subplot for Rainbow
ax2.errorbar(
    number_of_experts,
    baseline_rainbow,
    yerr=error_rainbow,
    label=label_Baseline,
    color="#3171ad",
    marker="o",
)
ax2.errorbar(
    number_of_experts,
    softmoe_rainbow,
    yerr=error_rainbow,
    label=label_SoftMoE,
    color="#469c76",
    marker="o",
)
ax2.errorbar(
    number_of_experts,
    top1moe_rainbow,
    yerr=error_rainbow,
    label=label_Top1_MoE,
    color="#c17cb9",
    marker="o",
)
ax2.set_ylabel(ylabel_value_2)
# Set grid
ax2.grid(True)
ax2.set_ylim(ylim_values_2)
ax2.set_yticks(
    yticks_values_2
)

# Only show ticks on the bottom subplot
plt.setp(ax1.get_xticklabels(), visible=False)

# Create legend above the second subplot
ax2.legend(loc="upper center", bbox_to_anchor=(0.5, 1.2), ncol=3)

# Set the figure's layout so there is space for the xlabel at the bottom
plt.tight_layout()

# Now adjust the subplot to give space for the ylabel on the left
f.subplots_adjust(left=0.15, bottom=0.12)

# Place the legend and adjust subplot parameters
ax2.legend(loc="upper center", bbox_to_anchor=(0.5, 1.2), ncol=3)

f.text(0.55, 0.05, text_1, ha="center", va="center")
f.text(
    0.05,
    0.5,
    text_2,
    ha="center",
    va="center",
    rotation="vertical",
)

# ===================
# Part 4: Saving Output
# ===================
plt.savefig('line_25.pdf', bbox_inches='tight')
