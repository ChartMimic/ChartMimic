# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Categories and values (estimated from the image)
categories = [
    "Syntax: Tagging, Chunking and Parsing",
    "Discourse and Pragmatics",
    "Information Extraction",
    "Machine Learning for NLP",
    "Information Retrieval and Text Mining",
    "Phonology, Morphology and Word Segmentation",
    "Computational Social Science and Social Media",
][::-1]
values = [-3.20, -3.1, -3.00, -2.90, -2.80, -2.70, -2.60][::-1]
error = [0.1, 0.15, 0.3, 0.25, 0.2, 0.1, 0.05]
xlabel = "A"
ylabel = "Categories"
title = "Your Chart Title Here"
xlim = [-3.5, -1.5]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create horizontal bar chart
fig, ax = plt.subplots(figsize=(8, 8))  # Adjust figure size
bars = ax.barh(
    categories,
    values,
    color="#c5b3d6",
    edgecolor="white",
    height=0.5,
    xerr=error,
    capsize=0,
)

# Set labels and title (if any)
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.set_title(title)

# Invert y-axis to match the image
ax.invert_yaxis()

# Set x-axis range to match the reference image
ax.set_xlim(xlim)

# Remove grid lines
ax.xaxis.grid(False)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Set background color to white
ax.set_facecolor("white")

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("errorbar_9.pdf", bbox_inches="tight")
