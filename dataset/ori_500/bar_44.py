# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Placeholder data
categories = [
    "AFAN",
    "AFBE",
    "AFCE",
    "AFEO",
    "AFEX",
    "AFIG",
    "AFPK",
    "AFPO",
    "AFPP",
    "AFPR",
    "AFRL",
    "AFSC",
    "AFSI",
    "AFTH",
    "AFVC",
    "AFWS",
    "AFWT",
    "DAH",
    "IC",
    "SS",
]
gpt_3_5_turbo_values = np.random.randint(5, 30, size=len(categories))
gpt_4_values = np.random.randint(5, 20, size=len(categories))

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
plt.savefig("bar_44.pdf", bbox_inches="tight")
