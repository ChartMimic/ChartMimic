import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data for demonstration purposes
data_jTrans = np.random.normal(2.5, 0.5, 200)
data_PalmTree = np.random.normal(3.0, 0.6, 200)
data_CLAP = np.random.normal(3.5, 0.4, 200)
xticklabels=["UrbanTransport", "TechGrowth", "SocialTrend"]
ylabel="Growth Rate"
ylim=[0.5, 4.5]
xticks=[1, 2, 3]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure with specified dimensions
fig, ax = plt.subplots(
    figsize=(5, 5)
)  # Adjusted to match the original image's dimensions

# Create violin plots
violin_parts1 = ax.violinplot(data_jTrans, positions=[1], showmeans=True)
violin_parts2 = ax.violinplot(data_PalmTree, positions=[2], showmeans=True)
violin_parts3 = ax.violinplot(data_CLAP, positions=[3], showmeans=True)

# Customize colors with vibrant colors
violin_parts1["bodies"][0].set_facecolor("#FF6347")  # Tomato red
violin_parts2["bodies"][0].set_facecolor("#4682B4")  # Steel blue
violin_parts3["bodies"][0].set_facecolor("#6A5ACD")  # Slate blue

# Change mean line colors to blue for each violin plot
for partname in ("cmeans", "cmaxes", "cmins", "cbars"):
    vp = violin_parts1[partname]
    vp.set_edgecolor("#3b75af")
    vp.set_linewidth(1)

    vp = violin_parts2[partname]
    vp.set_edgecolor("#3b75af")
    vp.set_linewidth(1)

    vp = violin_parts3[partname]
    vp.set_edgecolor("#3b75af")
    vp.set_linewidth(1)

# Set x-axis and y-axis labels
ax.set_xticks(xticks)
ax.set_xticklabels(xticklabels)
ax.set_ylabel(ylabel)

# Set y-axis limits
ax.set_ylim(ylim)

# ===================
# Part 4: Saving Output
# ===================
# tight layout
plt.tight_layout()

# Display the plot
plt.savefig('violin_4.pdf', bbox_inches='tight')
