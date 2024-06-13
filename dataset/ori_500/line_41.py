# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Updated steps
gradient_steps = np.linspace(0, 200, 50)

# Generating distinct trends for each line
line1_values = np.sin(gradient_steps * 0.1) + 1.0  # Sinusoidal trend
line2_values = np.array(gradient_steps) ** 2 * 0.0001 + 0.5  # Quadratic growth
line3_values = np.random.normal(
    loc=1.5, scale=0.2, size=len(gradient_steps)
)  # Random noise
line4_values = np.exp(0.01 * gradient_steps)  # Exponential growth

# Simulating standard deviations for error
std_dev = 0.1
line1_std = np.full_like(line1_values, std_dev)
line2_std = np.full_like(line2_values, std_dev)
line3_std = np.full_like(line3_values, std_dev)
line4_std = np.full_like(line4_values, std_dev)

# Axes Limits and Labels
xlabel_value = "Gradient Steps (x 62.5K)"
xlim_values = [0, 200]
xticks_values = np.linspace(0, 200, 9)

ylabel_value_1 = "Performance Value"
ylabel_value_2 = "Exponential Scale"
yticks_values_1 = np.arange(0, 5, 1)
yticks_values_2 = np.arange(0, 8, 1)
ylim_values_1 = [0, 5]
ylim_values_2 = [0, 8]

# Labels
label_1 = "Line 1 (Sinusoidal)"
label_2 = "Line 2 (Quadratic)"
label_3 = "Line 3 (Random Noise)"


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Creating a figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 8))

# Plotting on the first subplot
ax1.plot(
    gradient_steps, line1_values, "o-", color="purple", label=label_1
)
ax1.fill_between(
    gradient_steps,
    line1_values - line1_std,
    line1_values + line1_std,
    color="purple",
    alpha=0.2,
)

ax1.plot(gradient_steps, line2_values, "s-", color="blue", label=label_2)
ax1.fill_between(
    gradient_steps,
    line2_values - line2_std,
    line2_values + line2_std,
    color="blue",
    alpha=0.2,
)

ax2.plot(
    gradient_steps,
    line3_values,
    "^--",
    color="green",
    markerfacecolor=(0, 0, 0, 0),
    markeredgecolor="green",
    label=label_3,
)
ax2.fill_between(
    gradient_steps,
    line3_values - line3_std,
    line3_values + line3_std,
    color="green",
    alpha=0.2,
)

ax1.set_xlabel(xlabel_value, fontsize=12)
ax1.set_ylabel(ylabel_value_1, fontsize=12)
ax1.set_xticks(xticks_values)
ax1.set_yticks(yticks_values_1)
ax1.set_xlim(xlim_values)
ax1.set_ylim(ylim_values_1)
ax1.legend(loc="upper center", frameon=False, ncol=2, bbox_to_anchor=(0.5, 1.15))
ax1.grid(
    True, which="both", axis="both", color="lightgray", linestyle="--", linewidth=0.5
)
ax1.set_facecolor("#f9f9f9")

# Plotting on the second subplot
ax2.plot(
    gradient_steps, line4_values, "*-", color="red", label="Line 4 (Exponential Focus)"
)
ax2.fill_between(
    gradient_steps,
    line4_values - line4_std,
    line4_values + line4_std,
    color="red",
    alpha=0.2,
)
ax2.set_xlabel(xlabel_value, fontsize=12)
ax2.set_ylabel(ylabel_value_2, fontsize=12)
ax2.set_xticks(xticks_values)
ax2.set_yticks(yticks_values_2)
ax2.set_xlim(xlim_values)
ax2.set_ylim(ylim_values_2)
ax2.legend(loc="upper center", frameon=False, ncol=2, bbox_to_anchor=(0.5, 1.15))
ax2.grid(
    True, which="both", axis="both", color="lightgray", linestyle="--", linewidth=0.5
)
ax2.set_facecolor("#f9f9f9")

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('line_41.pdf', bbox_inches='tight')
