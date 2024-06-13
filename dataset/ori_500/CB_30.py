# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample financial data
quarters = ["Q1", "Q2", "Q3", "Q4"]
companyA = [200, 250, 300, 350]
companyB = [220, 270, 320, 370]
companyC = [240, 290, 340, 390]
companyD = [260, 310, 360, 410]
growth = [0.8, 0.4, 0.2, 0.1]

# Errors (e.g., standard deviation)
errorA = [20, 25, 30, 35]
errorB = [22, 27, 32, 37]
errorC = [24, 29, 34, 39]
errorD = [26, 31, 36, 41]
error_growth = [0.08, 0.04, 0.06, 0.04]
labels = ["Tesla", "Benz", "BYD", "Porsche"]
xlabel = "Quarter"
ylabel1 = "Earnings ($1000s)"
ylabel2 = "Growth %"
legend_title = "Companies"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and axis
fig, ax1 = plt.subplots(figsize=(8, 6))

# Bar plot with error bars
bar_width = 0.2
index = np.arange(len(quarters))
ax1.bar(
    index,
    companyA,
    bar_width,
    label=labels[0],
    color="limegreen",
    yerr=errorA,
    capsize=5,
    ecolor="gray",
)
ax1.bar(
    index + bar_width,
    companyB,
    bar_width,
    label=labels[1],
    color="sandybrown",
    yerr=errorB,
    capsize=5,
    ecolor="gray",
)
ax1.bar(
    index + 2 * bar_width,
    companyC,
    bar_width,
    label=labels[2],
    color="cornflowerblue",
    yerr=errorC,
    capsize=5,
    ecolor="gray",
)
ax1.bar(
    index + 3 * bar_width,
    companyD,
    bar_width,
    label=labels[3],
    color="plum",
    yerr=errorD,
    capsize=5,
    ecolor="gray",
)

# Line plot with error bars
ax2 = ax1.twinx()
ax2.errorbar(
    index + 1.5 * bar_width,
    growth,
    yerr=error_growth,
    fmt="o-",
    color="#f72585",
    label="Growth",
    linewidth=2,
    markersize=5,
    capsize=5,
)

# Set labels and title
ax1.set_xlabel(xlabel)
ax1.set_ylabel(ylabel1)
ax2.set_ylabel(ylabel2)

# Set x-axis tick labels
ax1.set_xticks(index + 1.5 * bar_width)
ax1.set_xticklabels(quarters)

# Add legends
ax1.legend(loc="lower center", ncol=4, bbox_to_anchor=(0.5, -0.25), title=legend_title)
ax2.legend(loc="upper left", ncol=1)

# Set ax2.yticklabels to be percentage
ax2.set_ylim(0, 1)
ax2.set_yticks(np.linspace(0, 1, 11))
ax2.set_yticklabels([f"{x*100:.0f}%" for x in ax2.get_yticks()])

# Grid and layout adjustment
ax1.grid(axis="y")
ax1.set_axisbelow(True)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("CB_30.pdf", bbox_inches="tight")
