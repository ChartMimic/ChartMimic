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
# Generating a similar style data for demonstration
# Assuming there are 3 quarters and 3 products
quarters = ["Q1", "Q2", "Q3"]
products = ["Product A", "Product B"]
sales_data = []

# Generating random sales and percentage changes for the example
for product in products:
    for quarter in quarters:
        sales = np.random.randint(100, 1000, size=9)
        np.random.shuffle(sales)
        percent_change = np.round(np.random.uniform(-50, 50), 2)
        for rank, sale in enumerate(sales, start=1):
            sales_data.append(
                {
                    "Product": product,
                    "Quarter": quarter,
                    "Rank": rank,
                    "Sales": sale,
                    "PercentChange": percent_change,
                }
            )

# Create the DataFrame
df = pd.DataFrame(sales_data)

# Pivoting the dataframe for the heatmap
df_pivot = df.pivot_table(
    index="Rank", columns=["Product", "Quarter"], values="Sales", aggfunc="first"
)

title = "Sales Performance Heatmap"
xlabel = "Product and Quarter"
ylabel = "Sales Rank"
color_bar_label = "Sales"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Initialize the matplotlib figure
fig, ax = plt.subplots(figsize=(6, 10))

# Create a custom colormap for the heatmap
cmap = plt.get_cmap("coolwarm")

# Draw the heatmap
cax = ax.imshow(df_pivot, cmap=cmap)

# Decorations
plt.title(title, fontsize=14)
plt.xlabel(xlabel, fontsize=12)
plt.ylabel(ylabel, fontsize=15)

# Set x-axis and y-axis labels
ax.set_xticks(range(len(df_pivot.columns)))
ax.set_xticklabels(
    [f"{col[0]} {col[1]}" for col in df_pivot.columns], rotation=45, ha="right"
)
ax.set_yticks(range(len(df_pivot.index)))
ax.set_yticklabels(df_pivot.index)

# Add annotations
for i in range(len(df_pivot.index)):
    for j in range(len(df_pivot.columns)):
        ax.text(j, i, df_pivot.iloc[i, j], ha="center", va="center", color="black")

# Add colorbar to be smaller
cbar = fig.colorbar(cax, ax=ax, fraction=0.2, pad=0.04)
cbar.set_label(color_bar_label)

# ===================
# Part 4: Saving Output
# ===================
# Show the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("heatmap_16.pdf", bbox_inches="tight")
