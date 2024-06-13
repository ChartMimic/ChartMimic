# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data for the charts
labels = ["Model", "Optimizer", "Gradient", "Unused"]
full_finetuning_data = [15.7, 19.9, 33.0, 31.4]
qlora_data = [10.5, 6.3, 28.4, 54.9]
colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99"]
titiles = ["LoRA", "QLoRA"]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure with specific dimensions
fig, ax = plt.subplots(1, 2, figsize=(10, 4))

# Full Finetuning Donut Chart
explode1 = (0.1, 0, 0, 0)
ax[0].pie(
    full_finetuning_data,
    labels=labels,
    colors=colors,
    startangle=90,
    counterclock=False,
    wedgeprops=dict(width=0.3),
    explode=explode1,
    autopct="%1.1f%%",
)
ax[0].set_title(titiles[0])

# QLoRA Donut Chart
explode2 = (0, 0.2, 0, 0)
ax[1].pie(
    qlora_data,
    labels=labels,
    colors=colors,
    startangle=90,
    counterclock=False,
    wedgeprops=dict(width=0.3),
    explode=explode2,
    autopct="%1.1f%%",
)
ax[1].set_title(titiles[1])

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout to prevent overlap and Show plot
plt.tight_layout()
plt.savefig('pie_12.pdf', bbox_inches='tight')
