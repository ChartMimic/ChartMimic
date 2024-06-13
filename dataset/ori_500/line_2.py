# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
gradient_steps = [0, 50, 100, 150, 200]  # 10 data points from 0 to 200
line1_values = [0.1, 0.8, 1.2, 1.5, 1.3]  # Random values for line 1
line2_values = [1.0, 0.5, 0.8, 1.0, 1.8]  # Random values for line 2
line3_values = [1.8, 1.2, 0.5, 0.4, 0.3]  # Random values for line 3

# Simulating standard deviations for error
line1_std = np.random.rand(5) * 0.2
line2_std = np.random.rand(5) * 0.2
line3_std = np.random.rand(5) * 0.2

# Labels
label_Line_1 = "Line 1"
label_Line_2 = "Line 2"
label_Line_3 = "Line 3"

# Axes Limits and Labels
xlabel_value = "Gradient Steps (x 62.5K)"
yticks_values = np.arange(0, 2.1, 0.5)

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting the lines with error bands
plt.figure(figsize=(4, 3))
plt.plot(gradient_steps, line1_values, "o-", color="orange", label=label_Line_1)
plt.fill_between(
    gradient_steps,
    line1_values - line1_std,
    line1_values + line1_std,
    color="orange",
    alpha=0.2,
)

plt.plot(gradient_steps, line2_values, "o-", color="blue", label=label_Line_2)
plt.fill_between(
    gradient_steps,
    line2_values - line2_std,
    line2_values + line2_std,
    color="blue",
    alpha=0.2,
)

plt.plot(gradient_steps, line3_values, "o-", color="green", label=label_Line_3)
plt.fill_between(
    gradient_steps,
    line3_values - line3_std,
    line3_values + line3_std,
    color="green",
    alpha=0.2,
)

# x labels
plt.xlabel(xlabel_value)
plt.xticks(gradient_steps)
plt.yticks(yticks_values)

# Moving axes spines
ax = plt.gca()  # get current axes
ax.spines["left"].set_position(("outward", 10))  # move left y-axis outwards
ax.spines["bottom"].set_position(("outward", 10))  # move bottom x-axis outwards
ax.spines["right"].set_color("none")  # hide the right spine
ax.spines["top"].set_color("none")  # hide the top spine
ax.grid(
    True, which="both", axis="both", color="lightgray", linestyle="--", linewidth=0.5
)

# ===================
# Part 4: Saving Output
# ===================
# Show the plot
plt.tight_layout()
plt.savefig('line_2.pdf', bbox_inches='tight')
