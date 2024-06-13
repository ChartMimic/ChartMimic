# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data
gradient_steps = np.array([0, 50, 100, 150, 200])
line1_values = np.array([0.1, 0.8, 1.2, 1.5, 1.3])
line2_values = np.array([1.0, 0.5, 0.8, 1.0, 1.8])
line3_values = np.array([1.8, 1.2, 0.5, 0.4, 0.3])
line4_values = np.poly1d(np.polyfit(gradient_steps, line2_values, 3))(
    gradient_steps
)  # Polynomial trend

# Axes Limits and Labels
xlabel_value = "Gradient Steps (x 62.5K)"

ylabel_value_1 = "Value"
ylabel_value_2 = "Polynomial Value"
yticks_values_1 = np.arange(0, 2.1, 0.5)
yticks_values_2 = np.arange(min(line4_values), max(line4_values) + 0.1, 0.2)

# Labels
label_1 = "Line 1"
label_2 = "Line 2"
label_3 = "Polynomial Trend (from Line 2)"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# First subplot
ax1.plot(gradient_steps, line1_values, "o-", color="orange", label=label_1)
ax1.plot(gradient_steps, line2_values, "s-", color="blue", label=label_2)
ax1.set_xlabel(xlabel_value)
ax1.set_ylabel(ylabel_value_1)
ax1.set_xticks(gradient_steps)
ax1.set_yticks(yticks_values_1)
ax1.legend(loc="upper left")
ax1.grid(True)

# Second subplot
ax2.plot(gradient_steps, line3_values, "^--", color="green", label="Line 3")
ax2.plot(gradient_steps, line4_values, "*-m", label=label_3)
ax2.set_xlabel(xlabel_value)
ax2.set_ylabel(ylabel_value_2)
ax2.set_xticks(gradient_steps)
ax2.set_yticks(yticks_values_2)
ax2.legend(loc="upper right")
ax2.grid(True)

# Annotations and styling
for ax in (ax1, ax2):
    ax.spines["left"].set_position(("outward", 10))
    ax.spines["bottom"].set_position(("outward", 10))
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
for x, y in zip(gradient_steps, line1_values):
    ax1.annotate(
        f"{y:.1f}", xy=(x, y), textcoords="offset points", xytext=(0, 10), ha="center"
    )

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('line_42.pdf', bbox_inches='tight')
