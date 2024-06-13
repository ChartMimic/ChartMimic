# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Sample data
digit_length = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
accuracy_direct = [0.6, 0.55, 0.1, 0.15, 0.4, 0.35, 0.2, 0.1, 0.05, 0.1]
accuracy_scratchpad = [0.5, 0.45, 0.2, 0.25, 0.3, 0.25, 0.15, 0.05, 0.0, 0.05]
accuracy_rule_following = [0.65, 0.6, 0.55, 0.5, 0.45, 0.4, 0.3, 0.2, 0.15, 0.2]

# Labels and Plot Types
label_5_shot_direct = "5-shot direct"
label_5_shot_scratchpad = "5-shot scratchpad"
label_5_shot_rule_following = "5-shot rule-following"

# Axes Limits and Labels
xlabel_value = "Digit Length"
ylabel_value = "Accuracy"
xlim_values = [0.6, 10.4]
ylim_values = [-0.03, 0.7]
xticks_values = range(1, 11, 1)
yticks_values = [i * 0.1 for i in range(0, 8)]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting the data
plt.figure(figsize=(6, 4))  # Adjusting figure size as per the given dimensions
plt.plot(digit_length, accuracy_direct, "o--", label=label_5_shot_direct, color="#1f77b4")
plt.plot(
    digit_length, accuracy_scratchpad, "o--", label=label_5_shot_scratchpad, color="#ff7f0e"
)
plt.plot(
    digit_length,
    accuracy_rule_following,
    "o--",
    label=label_5_shot_rule_following,
    color="#2ca02c",
)

# Adding labels and title
plt.xlabel(xlabel_value, fontsize=16)
plt.ylabel(ylabel_value, fontsize=16)

# Adjusting x and y axis limits to add some space before the start and after the end
plt.xlim(xlim_values)
plt.ylim(ylim_values)

# Setting x and y ticks
plt.xticks(xticks_values)  # X-axis from 1 to 10 with a step of 1
plt.yticks(yticks_values)  # Y-axis from 0.0 to 0.7 with a step of 0.1

# Adding legend outside the plot area
plt.legend(loc="upper right", fancybox=True, shadow=False)

# Adding semi-transparent grid
plt.grid(True, which="both", linewidth=0.5, alpha=0.2)  # Semi-transparent grid

# Removing top and right borders
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)

# ===================
# Part 4: Saving Output
# ===================
# Adjusting layout to reduce white space
plt.tight_layout()
plt.savefig('line_5.pdf', bbox_inches='tight')
