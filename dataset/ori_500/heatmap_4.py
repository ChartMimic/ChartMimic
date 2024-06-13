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
categories = [
    "C Subject",
    "C Relation",
    "C Attribute",
    "Q Subject",
    "Q Relation",
    "Last",
]

# Generating random data for illustration purposes
# You will need to replace this with your actual data
data = np.random.uniform(size=(180,))  # 180 values for 6 categories, 30 values each

# Creating a DataFrame
df = pd.DataFrame(
    {
        "Categories": np.tile(categories, 30),  # Repeating each category 30 times
        "Count": np.repeat(range(30), 6),  # Repeating each number from 0-29, 6 times
        "Values": data,
    }
)

# Pivoting the DataFrame to get it into the matrix form
pivot_df = df.pivot(index="Categories", columns="Count", values="Values")

# Reordering the index of the pivot_df to match the desired order
pivot_df = pivot_df.reindex(categories)

xlabel = "Count"
ylabel = "Categories"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting the heatmap with categories on the y-axis
plt.figure(figsize=(6, 3))  # Adjust size as needed

cax = plt.imshow(pivot_df, cmap="Greens", aspect="auto")

# x set only to be 0 4 8 12 16 20 24 28
plt.xticks(np.arange(0, 32, 4), range(0, 32, 4))
plt.yticks(range(len(categories)), categories)
plt.xlabel(xlabel)
plt.ylabel(ylabel)

# Ensure y-tick labels are horizontal
plt.yticks(rotation=0)
# Ensure x-tick labels are horizontal
plt.xticks(rotation=0)

plt.colorbar(cax)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("heatmap_4.pdf", bbox_inches="tight")
