import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Set a seed for reproducibility

# Define fiscal quarters
quarters = np.array([1, 2, 3, 4, 5])

# Generate synthetic fuel price changes for two different fuels
fuel_price_changes_gasoline = [-1.28010196,-9.48147536 , 0.99324956, -1.29355215, -1.59264396]  # Example changes in Gasoline prices
fuel_price_changes_diesel = [-3.39330358, -5.90702732 , 2.38541933, -4.00690653, -4.6634545 ]  # Example changes in Diesel prices

labels = ["Gasoline Prices", "Diesel Prices"]
axline = 0
xlabel = "Fiscal Quarter"
ylabel = "Price Change (%)"
ylim = [-10, 10]
yticks = np.arange(-10, 11, 5)

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and subplots
fig, axs = plt.subplots(figsize=(10, 5))
width = 0.4

# Plotting bars for each index
bars1 = axs.bar(
    quarters - width / 2,
    fuel_price_changes_gasoline,
    width=width,
    color="#78a083",
    label=labels[0],
)
bars2 = axs.bar(
    quarters + width / 2,
    fuel_price_changes_diesel,
    width=width,
    color="#d27a41",
    label=labels[1],
)

# Adding text labels on the bars
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        axs.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"{height:.1f}",
            ha="center",
            va="bottom" if height > 0 else "top",
        )

# Additional plot settings
axs.axhline(axline, color="black")
axs.set_xlabel(xlabel)
axs.set_ylabel(ylabel)
axs.set_ylim(ylim)
axs.set_yticks(yticks)
axs.set_xticks(quarters)
axs.yaxis.grid(True)
axs.set_axisbelow(True)

# Adding legend and adjusting layout
plt.legend(loc="upper center", bbox_to_anchor=(0.5, 1.10), ncol=2)

# ===================
# Part 4: Saving Output
# ===================
# Save the figure as a PDF
plt.tight_layout()
plt.savefig('bar_73.pdf', bbox_inches='tight')
