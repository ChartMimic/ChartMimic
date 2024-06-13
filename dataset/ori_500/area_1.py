# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting
x = [1, 2, 3, 4, 5]
y1 = [18, 24, 27, 29, 29.5]
y2 = [12, 17, 21, 23, 24]
y3 = [6, 10, 12, 14, 15]
y4 = [5, 6, 7, 8, 8.5]

# Labels for legend
label_activity_net_mIoU = "ActivityNet mIoU"
label_breakfast_mof = "Breakfast MoF"
label_activity_net_cider = "ActivityNet CIDEr"
label_qvhighlights_map = "QVHighlights mAP"

# Plot limits
xlim_values = (1, 5)
ylim_values = (0, 35)

# Axis labels
xlabel_values = ["10K", "50K", "1M", "5M", "10M"]
ylabel_values = [0, 10, 20, 30, 34]

# Axis ticks
xticks_values = x
yticks_values = [0, 10, 20, 30, 34]

# Horizontal line value
axhline_value = 30

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting the data
plt.figure(figsize=(9, 8))  # Adjusting figure size to match original image dimensions
plt.plot(
    x,
    y1,
    "o-",
    clip_on=False,
    zorder=10,
    markerfacecolor="#eec7bb",
    markeredgecolor="#d77659",
    markersize=12,
    color="#d77659",
    label=label_activity_net_mIoU,
)
plt.plot(
    x,
    y2,
    "o-",
    clip_on=False,
    zorder=10,
    markerfacecolor="#f5dbc3",
    markeredgecolor="#e8a66c",
    markersize=12,
    color="#e8a66c",
    label=label_breakfast_mof,
)
plt.plot(
    x,
    y3,
    "o-",
    clip_on=False,
    zorder=10,
    markerfacecolor="#b4d7d1",
    markeredgecolor="#509b8d",
    markersize=12,
    color="#509b8d",
    label=label_activity_net_cider,
)
plt.plot(
    x,
    y4,
    "o-",
    clip_on=False,
    zorder=10,
    markerfacecolor="#abb5ba",
    markeredgecolor="#2e4552",
    markersize=12,
    color="#2e4552",
    label=label_qvhighlights_map,
)

# Filling the area under the curves
plt.fill_between(x, y1, y2, color="#eec7bb", alpha=1)
plt.fill_between(x, y2, y3, color="#f5dbc3", alpha=1)
plt.fill_between(x, y3, y4, color="#b4d7d1", alpha=1)
plt.fill_between(x, y4, color="#abb5ba", alpha=1)

# Adding a horizontal dashed line at y=axhline_value
plt.axhline(axhline_value, color="black", linestyle="dotted")

# Setting the x-axis、y-axis limits
plt.xlim(*xlim_values)
plt.ylim(*ylim_values)

# Setting the x-axis tick labels
plt.xticks(xticks_values, xlabel_values)
plt.yticks(yticks_values, ylabel_values)

# Adding a legend
plt.legend(loc="lower center", ncol=4, bbox_to_anchor=(0.5, -0.1), frameon=False)
plt.gca().tick_params(axis="both", which="both", length=0)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("area_1.pdf", bbox_inches="tight")
