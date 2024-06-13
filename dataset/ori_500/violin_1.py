# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Set a random seed for reproducibility

# Generate 5 equidistant mean values between 2 and 6
mean_values = np.linspace(2, 6, 5)
# Use smaller standard deviations to ensure data falls between -1 and 7
standard_deviations = [0.5] * 5

data1 = [
    np.random.normal(loc=mean, scale=std, size=50)
    for mean, std in zip(mean_values, standard_deviations)
]
data2 = [
    np.random.normal(loc=mean, scale=std, size=50)
    for mean, std in zip(mean_values, standard_deviations)
]
positions1 = np.array(range(1, len(data1) + 1)) - 0.2
positions2 = np.array(range(1, len(data2) + 1)) + 0.2
legend_labels=["Llama2", "Llama2 (In-Chat)"]
xlabel="Number of examples"
ylabel="logP$_{ICL}$ - logP$_{noICL}$"
xticks=[1, 2, 3, 4, 5]
xtickslabels=["1", "2", "3", "4", "5"]


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure and axis with the specified dimensions
fig, ax = plt.subplots(figsize=(8, 7))

# Narrower violin plots
violin_width = 0.35  # set this to a suitable value

# Create the violin plot with adjusted positions

parts1 = ax.violinplot(
    data1, positions=positions1, widths=violin_width, showmeans=False, showmedians=True
)
parts2 = ax.violinplot(
    data2, positions=positions2, widths=violin_width, showmeans=False, showmedians=True
)

# Customizing the colors of the violin plot
for pc in parts1["bodies"]:
    pc.set_facecolor("#5e74a0")
    pc.set_edgecolor("black")
    pc.set_alpha(1)

for pc in parts2["bodies"]:
    pc.set_facecolor("#c28c69")
    pc.set_edgecolor("black")
    pc.set_alpha(1)

# Customizing the median lines and removing caps
for partname in ("cbars", "cmins", "cmaxes", "cmedians"):
    vp = parts1[partname]
    vp.set_edgecolor("black")
    vp.set_linewidth(1)
    if partname in ("cmins", "cmaxes", "cmedians"):
        vp.set_visible(False)  # Hide caps

    vp = parts2[partname]
    vp.set_edgecolor("black")
    vp.set_linewidth(1)
    if partname in ("cmins", "cmaxes", "cmedians"):
        vp.set_visible(False)  # Hide caps

# Customizing the colors of the violin plot and adding statistics
for i in range(len(data1)):
    # Adding the statistical annotations for data1
    quartile1, median, quartile3 = np.percentile(data1[i], [25, 50, 75])
    iqr = quartile3 - quartile1
    lower_whisker = np.min(data1[i][data1[i] >= quartile1 - 1.5 * iqr])
    upper_whisker = np.max(data1[i][data1[i] <= quartile3 + 1.5 * iqr])
    ax.vlines(positions1[i], quartile1, quartile3, color="black", linestyle="-", lw=4)
    ax.hlines(
        median,
        positions1[i] - 0.025,
        positions1[i] + 0.025,
        color="white",
        linestyle="-",
        lw=1,
        zorder=3,
    )
    ax.vlines(
        positions1[i], lower_whisker, upper_whisker, color="black", linestyle="-", lw=1
    )

    # Adding the statistical annotations for data2
    quartile1, median, quartile3 = np.percentile(data2[i], [25, 50, 75])
    iqr = quartile3 - quartile1
    lower_whisker = np.min(data2[i][data2[i] >= quartile1 - 1.5 * iqr])
    upper_whisker = np.max(data2[i][data2[i] <= quartile3 + 1.5 * iqr])
    ax.vlines(positions2[i], quartile1, quartile3, color="black", linestyle="-", lw=4)
    ax.hlines(
        median,
        positions2[i] - 0.025,
        positions2[i] + 0.025,
        color="white",
        linestyle="-",
        lw=1,
        zorder=3,
    )
    ax.vlines(
        positions2[i], lower_whisker, upper_whisker, color="black", linestyle="-", lw=1
    )

# Change the border color to grey
for spine in ax.spines.values():
    spine.set_edgecolor("grey")

# Remove small ticks beside the numbers on the x and y axes
ax.tick_params(axis="both", which="both", length=0)

# Adding the corrected legend
ax.legend(
    [parts1["bodies"][0], parts2["bodies"][0]],
    legend_labels,
    loc="upper center",
    bbox_to_anchor=(0.5, 1.1),
    ncol=2,
)

# Setting the title and labels
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)

# Setting the x-axis labels
ax.set_xticks(xticks)
ax.set_xticklabels(xtickslabels)

# Enabling y-axis grid lines
ax.yaxis.grid(
    True, linestyle="-", linewidth=0.7, color="grey", zorder=0
)  # You can customize the style of the grid here

# ===================
# Part 4: Saving Output
# ===================
# Adjust figure size to match original image's dimensions
fig.set_size_inches(7, 5)  # Width, Height in inches

# Adjust layout for better fit
plt.tight_layout()

# Display the plot
plt.savefig('violin_1.pdf', bbox_inches='tight')
