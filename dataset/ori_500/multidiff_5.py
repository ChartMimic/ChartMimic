# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Historical document types for the pie chart
document_types = [
    "Ancient Scripts",
    "Medieval Texts",
    "Renaissance Literature",
    "Modern Records",
]
document_counts = [150, 300, 200, 350]

# Historical periods and document counts for the scatter plot
periods = ["Ancient", "Medieval", "Renaissance", "Modern"]
years = [500, 1200, 1600, 1900]
doc_counts = [150, 300, 200, 350]

# Axes Limits and Labels
title_1 = "Historical Document Types in Library"

title_2 = "Document Count Over Historical Periods"
xlabel_value = "Year"
ylabel_value = "Number of Documents"
ylim_values = [100, 450]
xlim_values = [400, 2000]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and set up GridSpec
fig = plt.figure(figsize=(10, 5))
gs = gridspec.GridSpec(1, 2, width_ratios=[1, 1])

# Create pie chart on the left
ax1 = fig.add_subplot(gs[0])
wedges, texts, autotexts = ax1.pie(
    document_counts,
    labels=document_types,
    autopct="%1.1f%%",
    startangle=90,
    colors=["gold", "lightblue", "lightgreen", "salmon"],
)
ax1.set_title(title_1)

# Create scatter plot on the right
ax2 = fig.add_subplot(gs[1])
scatter = ax2.scatter(
    years,
    doc_counts,
    color="purple",
    s=np.array(doc_counts),
    alpha=0.5,
    edgecolor="black",
)
ax2.set_title(title_2)
ax2.set_xlabel(xlabel_value)
ax2.set_ylabel(ylabel_value)
ax2.grid(True)
ax2.set_ylim(ylim_values)
ax2.set_xlim(xlim_values)

# Add text labels to scatter points
for i, txt in enumerate(periods):
    ax2.annotate(txt, (years[i], doc_counts[i] + 20))

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save plot
plt.tight_layout()
plt.savefig('multidiff_5.pdf', bbox_inches='tight')
