# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

import pandas as pd

# ===================
# Part 2: Data Preparation
# ===================
# Defining the categories
categories = ["context", "option", "cot", "last"]

# Generating random data for illustration purposes
# You will need to replace this with your actual data
data = np.random.uniform(size=(140,))  # 180 values for 4 categories, 40 values each

# Creating a DataFrame
df = pd.DataFrame(
    {
        "Categories": np.tile(categories, 35),  # Repeating each category 40 times
        "Count": np.repeat(
            range(0, 35), 4
        ),  # Repeating each number from 0-39,  4 times
        "Values": data,
    }
)

# Pivoting the DataFrame to get it into the matrix form
pivot_df = df.pivot(index="Categories", columns="Count", values="Values")

# Reordering the index of the pivot_df to match the desired order
pivot_df = pivot_df.reindex(categories)

color_bar_label = "Values"  # Label for the color bar
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting the heatmap with categories on the y-axis
plt.figure(figsize=(10, 3))  # Adjust size as needed

# Choose a different colormap, e.g., 'viridis'
cmap = plt.get_cmap("turbo")
cax = plt.imshow(pivot_df, cmap=cmap)

# x set only to be 0 5 10 15 20 25 30 35 40
plt.xticks(np.arange(0, 35, 5), range(0, 35, 5))
plt.yticks(range(len(categories)), categories)

plt.yticks(rotation=0)  # Ensure y-tick labels are horizontal
plt.xticks(rotation=0)  # Ensure x-tick labels are horizontal

# Add colorbar
cbar = plt.colorbar(cax)
cbar.set_label(color_bar_label)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("heatmap_17.pdf", bbox_inches="tight")
