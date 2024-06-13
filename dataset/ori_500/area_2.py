# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
import matplotlib.lines as mlines

# ===================
# Part 2: Data Preparation
# ===================
# Sample data
time_step = np.linspace(0, 4, 40)
rsa_gt = np.exp(time_step)
rsa_drs = np.exp(0.7 * time_step)
rsa_pr = np.exp(0.5 * time_step)
cr_gt = 1 - np.linspace(0, 0, 40)
cr_drs = 1 + np.log(np.linspace(1, 0.98, 40))
cr_pr = 1 + np.log(np.linspace(1, 0.96, 40))

# Extracted variables
rsa_gt_label = "GT"
rsa_drs_label = "DRS"
rsa_pr_label = "PR-based"
cr_gt_label = "GT"
cr_drs_label = "DRS"
cr_pr_label = "PR-based"
rsa_ylim = [0, 50]
rsa_xlim = [0, 4]
rsa_yticks = [0, 10, 20, 30, 40, 50]
rsa_xticks = [0, 1, 2, 3]
rsa_ylabel = "RSA"
cr_ylim = [0.96, 1.0]
cr_xlim = [0, 4]
cr_yticks = [0.96, 0.98, 1.0]
cr_xticks = [0, 1, 2, 3]
cr_xlabel = "time step"
cr_ylabel = "CR"
legend_labels = ["GT", "DRS", "PR-based"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and axes
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

# Plot RSA
ax1.plot(time_step, rsa_gt, "o-", color="#377e22", label=rsa_gt_label)
ax1.fill_between(time_step, rsa_gt, color="#ebf2e8")
ax1.plot(time_step, rsa_drs, "s-", color="#020ddc", label=rsa_drs_label)
ax1.fill_between(time_step, rsa_drs, color="#d3dbe4")
ax1.plot(time_step, rsa_pr, "^-", color="#bd2b25", label=rsa_pr_label)
ax1.fill_between(time_step, rsa_pr, color="#cdc6cf")
ax1.set_ylim(rsa_ylim)
ax1.set_xlim(rsa_xlim)
ax1.set_yticks(rsa_yticks)
ax1.set_xticks(rsa_xticks)
ax1.set_ylabel(rsa_ylabel)
ax1.tick_params(axis="both", which="both", length=0)

# Plot CR
ax2.plot(time_step, cr_gt, "o-", color="#377e22", label=cr_gt_label)
ax2.fill_between(time_step, cr_gt, color="#ebf2e8")
ax2.plot(time_step, cr_drs, "s-", color="#020ddc", label=cr_drs_label)
ax2.fill_between(time_step, cr_drs, color="#d3dbe4")
ax2.plot(time_step, cr_pr, "^-", color="#bd2b25", label=cr_pr_label)
ax2.fill_between(time_step, cr_pr, color="#cdc6cf")
ax2.set_ylim(cr_ylim)
ax2.set_xlim(cr_xlim)
ax2.set_yticks(cr_yticks)
ax2.set_xticks(cr_xticks)
ax2.set_xlabel(cr_xlabel)
ax2.set_ylabel(cr_ylabel)
ax2.tick_params(axis="both", which="both", length=0)

# Create custom legend
green_line = mlines.Line2D(
    [], [], color="green", marker="o", markersize=6, label=legend_labels[0]
)
blue_line = mlines.Line2D(
    [], [], color="blue", marker="s", markersize=6, label=legend_labels[1]
)
red_line = mlines.Line2D(
    [], [], color="red", marker="^", markersize=6, label=legend_labels[2]
)
plt.legend(
    handles=[green_line, blue_line, red_line],
    loc="lower center",
    bbox_to_anchor=(0.5, -0.2),
    ncol=6,
    frameon=False,
)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the figure
plt.tight_layout()
plt.savefig("area_2.pdf", bbox_inches="tight")
