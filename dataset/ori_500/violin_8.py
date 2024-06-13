# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Adjusting sample data to fit within 0-1 range and have appropriate shapes
vanilla_data = np.clip(
    np.random.normal(0.88, 0.05, 200), 0, 1
)  # Slightly lower std dev, larger sample
cot_data = np.clip(np.random.normal(0.86, 0.05, 200), 0, 1)  # Larger sample
extra_data1 = np.clip(
    np.random.normal(0.80, 0.12, 200), 0, 1
)  # Slightly lower std dev, larger sample
extra_data2 = np.clip(np.random.normal(0.68, 0.08, 200), 0, 1)  # Larger sample
extra_data3 = np.clip(np.random.normal(0.57, 0.1, 200), 0, 1)  # Larger sample

pearson_r = [0.18, 0.19, 0.19, 0.18, 0.16]
eer = [3.33, 3.33, 10.67, 16.95, 29.10]

data = [vanilla_data, cot_data, extra_data1, extra_data2, extra_data3]
categories = ["Raw", "125Hz", "50Hz", "25Hz", "10Hz"]
ylabel = "KCC"
ylim=[0, 1.06]
xlabel="Decimated Sampling Rate"
textlabels=[ "Pearson R", "EER(%)"]



# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, ax = plt.subplots(
    figsize=(10, 6)
)  # Adjust the figure size to accommodate more violins

# Create violin plots
violin_parts = ax.violinplot(data, showmeans=False, showmedians=True, showextrema=False)

# Customize the appearance
ax.set_ylabel(ylabel)
ax.set_xticks(
    np.arange(1, len(categories) + 1)
)  # Adjust the x-ticks to match the number of categories
ax.set_xticklabels(categories)
ax.set_ylim(ylim)  # You may need to adjust this if the data range changes
ax.set_xlabel(xlabel)

# Set violin colors and add statistical annotations
colors = [
    "#44739d",
    "#d48640",
    "#539045",
    "#b14743",
    "#8e73ae",
]  # Add more colors as needed
for i, (pc, d) in enumerate(zip(violin_parts["bodies"], data)):
    pc.set_facecolor(colors[i])
    pc.set_edgecolor("black")
    pc.set_alpha(1)

    # Calculate the quartiles and median
    quartile1, median, quartile3 = np.percentile(d, [25, 50, 75])
    iqr = quartile3 - quartile1

    # Calculate whiskers
    lower_whisker = np.min(d[d >= quartile1 - 1.5 * iqr])
    upper_whisker = np.max(d[d <= quartile3 + 1.5 * iqr])

    # Annotate statistics
    ax.vlines(i + 1, quartile1, quartile3, color="k", linestyle="-", lw=4)
    ax.scatter(i + 1, median, color="w", s=10, zorder=3)
    ax.vlines(i + 1, lower_whisker, upper_whisker, color="k", linestyle="-", lw=1)
    ax.text(
        i + 1 + 0.3,
        np.median(data[i]),
        f"{median:.2f}",
        ha="left",
        va="center",
        color="black",
        rotation=45,
    )

    # Annotate with Pearson R and EER values
    ax.text(
        i + 1,
        0.14,
        f"{pearson_r[i]:.2f}",
        ha="center",
        va="center",
        color="green",
        fontsize=10,
    )
    ax.text(
        i + 1,
        0.08,
        f"{eer[i]:.2f}",
        ha="center",
        va="center",
        color="blue",
        fontsize=10,
    )

ax.text(5.6, 0.14,textlabels[0], ha="left", va="center", color="green", fontsize=10)
ax.text(5.6, 0.08,textlabels[1], ha="left", va="center", color="blue", fontsize=10)

# Make the other parts of the violin plots invisible
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
plt.savefig('violin_8.pdf', bbox_inches='tight')
