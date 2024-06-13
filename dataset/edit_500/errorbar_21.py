import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Categories and values for different countries
categories = ["Quantum Computing", "Nanotechnology", "Biotechnology", "Astrophysics", "Robotics"][::-1]
funding_received = [-1800, -2400, -2200, -2000, -1900][::-1]  # Funding received in millions of dollars
funding_error = [250, 300, 275, 260, 240][::-1]  # Error values for funding received

research_output = [28, 22, 30, 25, 20][::-1]  # Research output as percentage of total projects
output_error = [3.4, 3.1, 3.7, 3.2, 2.9][::-1]  # Error values for research output
xlabels = ["Funding Received (Millions of Dollars)", "Research Output (%)"]
titles = ["Total Funding Received by Field", "Research Output by Field"]
xlims = [[-3000, 0], [0, 35]]


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create horizontal bar chart with subplots
fig, axes = plt.subplots(1, 2, figsize=(10, 6), sharey=True)  # Adjust figure size

# Setting colors for the bars
neg_colors = ["#c5b3d6"] * 5
pos_colors = ["#76d7c4"] * 5

# Plotting bars for negative values (Energy Consumption)
bars = axes[0].barh(
    categories,
    funding_received,
    color=neg_colors,
    edgecolor="white",
    height=0.5,
    xerr=funding_error,
    capsize=0,
)
axes[0].set_xlabel(xlabels[0])
axes[0].set_title(titles[0])
axes[0].invert_yaxis()
axes[0].set_xlim(xlims[0])
axes[0].xaxis.grid(True)
axes[0].spines["top"].set_visible(False)
axes[0].spines["right"].set_visible(False)

# Plotting bars for positive values (Renewable Energy Usage)
bars2 = axes[1].barh(
    categories,
    research_output,
    color=pos_colors,
    edgecolor="white",
    height=0.5,
    xerr=output_error,
    capsize=0,
)
axes[1].set_xlabel(xlabels[1])
axes[1].set_title(titles[1])
axes[1].invert_yaxis()
axes[1].set_xlim(xlims[1])
axes[1].xaxis.grid(True)
axes[1].spines["top"].set_visible(False)
axes[1].spines["right"].set_visible(False)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('errorbar_21.pdf', bbox_inches='tight')
