# ===================
# Part 1: Importing Libraries
# ===================

import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data for the charts
categories = ["Model", "Optimizer", "Gradient+Activations+Other", "Unused"]
full_finetuning_data = [12.6, 15.9, 26.4, 25.1]
qlora_data = [4.6, 5.3, 23.9, 46.2]
colors = ["#FFD580", "#C0C0C0", "#8FBC8F", "#ebf5a4"]

# Variables for plot configuration
full_finetuning_label = 'Full Finetuning'
qlora_label = 'QLoRA'
legend_labels = categories
legend_loc = "lower center"
legend_ncol = 4
legend_frameon = False
title_full_finetuning = "Full Finetuning"
title_qlora = "QLoRA"
wedgeprops_dict = dict(width=0.3)
startangle = 90
counterclock = False

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure with specific dimensions
fig, ax = plt.subplots(2, 1, figsize=(5, 8))

# Full Finetuning Donut Chart
ax[0].pie(
    full_finetuning_data,
    labels=full_finetuning_data,
    colors=colors,
    startangle=startangle,
    counterclock=counterclock,
    wedgeprops=wedgeprops_dict,
)
ax[0].set_title(title_full_finetuning)

# QLoRA Donut Chart
ax[1].pie(
    qlora_data,
    labels=qlora_data,
    colors=colors,
    startangle=startangle,
    counterclock=counterclock,
    wedgeprops=wedgeprops_dict,
)
ax[1].set_title(title_qlora)

# Add legend
fig.legend(legend_labels, loc=legend_loc, ncol=legend_ncol, frameon=legend_frameon)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout to prevent overlap and Show plot
plt.tight_layout()
plt.savefig('pie_13.pdf', bbox_inches='tight')
