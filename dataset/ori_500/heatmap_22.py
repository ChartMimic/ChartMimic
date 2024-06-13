# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import pandas as pd

# ===================
# Part 2: Data Preparation
# ===================
# Creating dummy data based on the visual observation of the provided image
data_LLaMA = pd.DataFrame(
    {
        "Baseline": ["#17", "#3", "#13", "#5"],
        "Reversed Order": ["#24", "#8", "#10", "#4"],
        "Reversed IDs": ["#23", "#17", "#3", "#10"],
    }
)

data_GPT = pd.DataFrame(
    {
        "Baseline": ["#5", "#17", "#11", "#24"],
        "Reversed Order": ["#17", "#5", "#24", "#1"],
        "Reversed IDs": ["#1", "#23", "#9", "#15"],
    }
)


# Creating a function to convert the string indices to numeric values for plotting
def convert_to_numeric(cell):
    return int(cell.replace("#", ""))


# Convert the dataframes
data_LLaMA_numeric = data_LLaMA.applymap(convert_to_numeric)
data_GPT_numeric = data_GPT.applymap(convert_to_numeric)

# Axes Limits and Labels
ax1_title = "LLaMA"
ax1_ylabel = "Rank"
ax2_title = "GPT"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Creating the heatmap using matplotlib with increased linewidths for separation
fig, (ax1, ax2) = plt.subplots(
    ncols=2, figsize=(6, 3), gridspec_kw={"width_ratios": [1, 1], "wspace": 0.1}
)

# Setting the color map to match the image: Oranges for LLaMA, Blues for GPT
cmap_LLaMA = plt.get_cmap("Oranges")
cmap_GPT = plt.get_cmap("Blues")

# Heatmap for LLaMA with increased cell borders
im1 = ax1.imshow(data_LLaMA_numeric, cmap=cmap_LLaMA)
ax1.set_title(ax1_title)
ax1.set_ylabel(ax1_ylabel)
ax1.set_xticks(range(len(data_LLaMA.columns)))
ax1.set_xticklabels(data_LLaMA.columns, rotation=45)
ax1.set_yticks(range(len(data_LLaMA.index)))
ax1.set_yticklabels(data_LLaMA.index, rotation=0)

# Add annotations for LLaMA
for i in range(len(data_LLaMA.index)):
    for j in range(len(data_LLaMA.columns)):
        ax1.text(j, i, data_LLaMA.iloc[i, j], ha="center", va="center", color="black")

# Heatmap for GPT with increased cell borders
im2 = ax2.imshow(data_GPT_numeric, cmap=cmap_GPT)
ax2.set_title(ax2_title)
ax2.set_xticks(range(len(data_GPT.columns)))
ax2.set_xticklabels(data_GPT.columns, rotation=45)
ax2.set_yticks(range(len(data_GPT.index)))
ax2.set_yticklabels(data_GPT.index, rotation=0)

# Add annotations for GPT
for i in range(len(data_GPT.index)):
    for j in range(len(data_GPT.columns)):
        ax2.text(j, i, data_GPT.iloc[i, j], ha="center", va="center", color="black")

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("heatmap_22.pdf", bbox_inches="tight")
