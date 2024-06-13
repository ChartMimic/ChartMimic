import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data for the purpose of this example
tech_innovation_data = np.random.normal(70, 20, 200)
market_adoption_data = np.random.normal(65, 11, 100)

data = [tech_innovation_data, market_adoption_data]
categories = ["Tech Innovation", "Market Adoption"]
ylabel ="Success Rate"
xticks=[1, 2]
ylim=[10, 120]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, ax = plt.subplots(
    figsize=(6, 4)
)  # Adjusting figure size to match original image dimensions
violin_parts = ax.violinplot(data, showmeans=False, showmedians=True, showextrema=False)

# Customizing the appearance
ax.set_ylabel(ylabel)
ax.set_xticks(xticks)
ax.set_xticklabels(categories)
ax.grid(axis="y", alpha=0.6)  # Adding horizontal grid lines
ax.set_ylim(ylim)  # Setting y-axis limits

# Removing the ticks on the x and y axes
ax.tick_params(axis="x", which="both", length=0)  # Remove x-axis ticks
ax.tick_params(axis="y", which="both", length=0)  # Remove y-axis ticks

# Coloring the violins and adding the desired statistical annotations
for i, (pc, d) in enumerate(zip(violin_parts["bodies"], data)):
    pc.set_facecolor(["#ce7a9b", "#3b78bb"][i])
    pc.set_edgecolor("black")
    pc.set_alpha(1)

    # Calculate the quartiles and interquartile range
    quartile1, median, quartile3 = np.percentile(d, [25, 50, 75])
    iqr = quartile3 - quartile1

    # Calculate lower and upper whiskers using 1.5xIQR rule
    lower_whisker = np.min(d[d >= quartile1 - 1.5 * iqr])
    upper_whisker = np.max(d[d <= quartile3 + 1.5 * iqr])

    # Placing lines for median, quartiles, and whiskers
    ax.vlines(i + 1, quartile1, quartile3, color="k", linestyle="-", lw=4)
    ax.scatter(i + 1, median, color="w", s=10, zorder=3)
    ax.vlines(i + 1, lower_whisker, upper_whisker, color="k", linestyle="-", lw=1)

# Remove the lines (medians, whiskers, etc.)
for partname in ("cbars", "cmins", "cmaxes", "cmedians"):
    vp = violin_parts.get(partname)
    if vp:
        vp.set_visible(False)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout for better fit
plt.tight_layout()

# Display the plot
plt.savefig('violin_6.pdf', bbox_inches='tight')
