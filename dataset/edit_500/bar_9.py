# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0);


# ===================
# Part 2: Data Preparation
# ===================
# Data for BC5CDR
transportation_categories = ["Infrastructure", "Vehicle Safety", "Emissions", "Public Transport Usage", "Total"]
transportation_manual_mapping = [70, 50, 90, 30, 70]
transportation_llm_revision = [60, 40, 80, 20, 60]
transportation_llm_revision_wcot = [85, 65, 95, 35, 85]
transportation_verifner = [95, 75, 85, 45, 95]

# Data for Nationwide Transport
Nationwide_transportation_categories = ["Infrastructure", "Vehicle Safety", "Emissions", "Public Transport Usage", "Total"]
Nationwide_transportation_manual_mapping = [60, 50, 70, 30, 80]
Nationwide_transportation_llm_revision = [40, 60, 70, 50, 40]
Nationwide_transportation_llm_revision_wcot = [75, 85, 75, 95, 45]
Nationwide_transportation_verifner = [45, 55, 85, 35, 95]

labels = ["Manual Mapping", "LLM-revision", "LLM-revision w/CoT", "VerifNER"]
title = "Improvement in Transportation Metrics (%)"
title1 = "City Transport"
title2 = "Nationwide Transport"

ylim1 = [0, 100]
yticks1 = np.arange(0, 101, 20)
ylim2 = [0, 100]
yticks2 = np.arange(0, 101, 20)


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set up the figure and axes
fig, axs = plt.subplots(2, 1, figsize=(9, 6))  # Width, Height in inches

# Plot for GENIA
x = np.arange(len(transportation_categories))
width = 0.18  # Adjust this value to change the width of the bars
spacing = 0.2  # Adjust this value to change the spacing between the bars

axs[0].bar(
    x - spacing * 1.5,
    transportation_manual_mapping,
    width,
    label=labels[0],
    color="#e19e9c",
)
axs[0].bar(
    x - spacing / 2, transportation_llm_revision, width, label=labels[1], color="#f7ce91"
)
axs[0].bar(
    x + spacing / 2,
    transportation_llm_revision_wcot,
    width,
    label=labels[2],
    color="#de6560",
)
axs[0].bar(x + spacing * 1.5, transportation_verifner, width, label=labels[3], color="#94d4ac")
# axs[0].set_ylabel('Error correction rate (%)')
axs[0].set_title(title1)
axs[0].set_xticks(x)
axs[0].set_xticklabels(transportation_categories)
axs[0].set_ylim(ylim1)
axs[0].set_yticks(yticks1)
axs[0].legend(loc="upper right", ncol=2)

# Plot for BC5CDR
x = np.arange(len(transportation_categories))
axs[1].bar(x - spacing * 1.5, Nationwide_transportation_manual_mapping, width, color="#e19e9c")
axs[1].bar(x - spacing / 2, Nationwide_transportation_llm_revision, width, color="#f7ce91")
axs[1].bar(x + spacing / 2, Nationwide_transportation_llm_revision_wcot, width, color="#de6560")
axs[1].bar(x + spacing * 1.5, Nationwide_transportation_verifner, width, color="#94d4ac")
# axs[1].set_ylabel('Error correction rate (%)')
axs[1].set_title(title2)
axs[1].set_xticks(x)
axs[1].set_xticklabels(Nationwide_transportation_categories)
axs[1].set_ylim(ylim2)
axs[1].set_yticks(yticks2)

# Add a common y-axis label
fig.text(
    0.0001,
    0.5,
    title,
    va="center",
    rotation="vertical",
    fontsize=12,
)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the figure
plt.tight_layout()
plt.savefig('bar_9.pdf', bbox_inches='tight')
