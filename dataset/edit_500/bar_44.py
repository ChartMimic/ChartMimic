import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

# ===================
# Part 2: Data Preparation
# ===================
# Placeholder data
categories = [
    "Healthcare",
    "Finance",
    "Education",
    "E-commerce",
    "Technology",
    "Gaming",
    "Manufacturing",
    "Retail",
    "Logistics",
    "Real Estate",
    "Legal",
    "Supply Chain",
    "Insurance",
    "Travel",
    "Automotive",
    "Telecommunications",
    "Media",
    "Hospitality",
    "Infrastructure",
    "Social Services"
]
gpt_3_5_turbo_values = [25, 18, 19, 22, 27, 15, 23, 19, 21, 20, 24, 26, 17, 28, 16, 30, 22, 25, 18, 20]
gpt_4_values = [15, 12, 19, 17, 14, 10, 13, 11, 16, 18, 14, 15, 12, 16, 11, 17, 13, 15, 10, 14]
# Bar width
bar_width = 0.6

# Positions of the bars on the x-axis
r = np.arange(len(categories))

labels = ["GPT-3.5-Turbo", "GPT-4"]
xlabel = "Categories"
ylabel = "Non-valid NLAs"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the figure and the axes
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the bars
ax.bar(
    r,
    gpt_3_5_turbo_values,
    bottom=gpt_4_values,
    color="blue",
    width=bar_width,
    label=labels[0],
)
ax.bar(r, gpt_4_values, color="orange", width=bar_width, label=labels[1])

# Add labels, title, and legend
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.set_xticks(r)
ax.set_xticklabels(categories, rotation=45, ha="right")
ax.legend(loc="upper left")

# ===================
# Part 4: Saving Output
# ===================
# Show the plot with tight layout
plt.tight_layout()
plt.savefig('bar_44.pdf', bbox_inches='tight')
