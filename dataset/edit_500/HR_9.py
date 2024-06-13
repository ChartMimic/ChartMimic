import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

import matplotlib.patches as patches
import matplotlib.colors as mcolors


# ===================
# Part 2: Data Preparation
# ===================

data1 = [np.random.normal(loc, 5, 100) for loc in range(11, 20)]
data2 = [np.random.normal(loc, 30, 100) for loc in range(35, 50)]
xticks=[[1, 3], [1, 3]]
xticklabels=[["Sunny", "Rainy"], ["Sunny", "Rainy"]]
titles=["Weather Station = North", "Weather Station = South"]
ylabel = "Temperature Variation (°C)"
width =1.6
# ===================
# Part 3: Plot Configuration and Rendering
# ===================

def custom_boxplot(
    ax,
    data,
    position,
    width,
    facecolor="lightblue",
    edgecolor="gray",
    mediancolor="gray",
    num_rectangles=10,
):
    median = np.median(data)
    q1, q3 = np.percentile(data, [25, 75])
    iqr = q3 - q1
    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)

    # Draw the box
    box = patches.Rectangle(
        (position, q1), width, q3 - q1, facecolor=facecolor, edgecolor=edgecolor
    )
    ax.add_patch(box)

    # Draw the median line
    ax.plot([position, position + width], [median, median], color=mediancolor)

    colors = mcolors.LinearSegmentedColormap.from_list("", [facecolor, "white"])(
        np.linspace(0.2, 0.7, 5)
    )
    # Draw the whiskers
    lower_values = np.linspace(lower_bound, q1, num_rectangles // 2 + 1)
    upper_values = np.linspace(q3, upper_bound, num_rectangles // 2 + 1)
    # Find the outliers
    outliers = data[(data < lower_bound) | (data > upper_bound)]

    # Draw the outliers
    ax.scatter(
        [position + width / 2] * len(outliers),
        outliers,
        marker="o",
        edgecolor="gray",
        facecolor="None",
        s=30,
    )
    for i in range(num_rectangles // 2):
        lower_val_min = lower_values[i]
        lower_val_max = lower_values[i + 1]
        upper_val_min = upper_values[i]
        upper_val_max = upper_values[i + 1]
        widthupper = (
            0.6 - 0.59 * abs(np.sqrt(i)) / (np.sqrt(num_rectangles // 2 - 1))
        ) * width
        widthlower = (
            0.6
            - 0.59
            * abs(np.sqrt(num_rectangles // 2 - 1 - i))
            / np.sqrt((num_rectangles // 2 - 1))
        ) * width
        lower_whisker = patches.Rectangle(
            (position + (width - widthlower) / 2, lower_val_min),
            widthlower,
            lower_val_max - lower_val_min,
            facecolor=colors[num_rectangles // 2 - 1 - i],
            edgecolor=edgecolor,
        )
        upper_whisker = patches.Rectangle(
            (position + (width - widthupper) / 2, upper_val_min),
            widthupper,
            upper_val_max - upper_val_min,
            facecolor=colors[i],
            edgecolor=edgecolor,
        )
        ax.add_patch(lower_whisker)
        ax.add_patch(upper_whisker)


fig, axs = plt.subplots(1, 2, figsize=(10, 4))
custom_boxplot(axs[0], data1[0], 0, width, facecolor="#516897")
custom_boxplot(axs[0], data1[1], 2, width, facecolor="#be825c")

axs[0].set_xticks(xticks[0])
axs[0].set_xticklabels(xticklabels[0])
axs[0].set_title(titles[0])
axs[0].set_ylabel(ylabel)
axs[0].spines["top"].set_visible(False)
axs[0].spines["right"].set_visible(False)
custom_boxplot(axs[1], data2[0], 0, width, facecolor="#516897")
custom_boxplot(axs[1], data2[1], 2, width, facecolor="#be825c")
axs[1].set_xticks(xticks[1])
axs[1].set_xticklabels(xticklabels[1])
axs[1].set_title(titles[1])
axs[1].set_yticklabels([])
axs[1].spines["top"].set_visible(False)
axs[1].spines["right"].set_visible(False)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('HR_9.pdf', bbox_inches='tight')
