# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data
categories = [
    "Parameter",
    "Method Declaration",
    "Variable Declaration",
    "Conditional Statement",
    "Loop",
    "Conditional Block",
    "Argument",
    "External Class",
    "Variable",
    "Return",
    "External Variable/Method",
    "Method Call",
    "Exception Handling",
    "Operation",
    "Comment",
    "Operator",
    "Assignment",
    "Literal",
]
differences = [
    -5,
    10,
    -20,
    -10,
    10,
    20,
    30,
    -30,
    -40,
    60,
    70,
    80,
    80,
    100,
    130,
    160,
    160,
    180,
]
colors = ["#d1605e" if x < 0 else "#85b6b2" for x in differences]

title = "Relative Difference in Machine vs. Human Focus on Semantic Categories"
xlabel = "Difference (%)"
ylabel = "Semantic Category"
xlim = [-50, 200]
xticks = range(-50, 201, 50)

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and plot
fig, ax = plt.subplots(figsize=(10, 5))
ax.barh(categories, differences, color=colors)

# Set title and labels
ax.set_title(title)
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)

# Set x-axis limits and labels
ax.set_xlim(xlim)
ax.set_xticks(xticks)
ax.xaxis.grid(True)

# ===================
# Part 4: Saving Output
# ===================
# Save the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("bar_40.pdf", bbox_inches="tight")
