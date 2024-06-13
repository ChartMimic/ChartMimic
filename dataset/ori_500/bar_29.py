# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

# ===================
# Part 2: Data Preparation
# ===================
# Data
pdes = ["Wave", "Diffusion", "Heat", "Poisson", "Burgers", "N-S"]
rbf_int = [1e-2, 1e-3, 1e-2, 1e-2, 1e-3, 1e-2]
rbf_pol = [1e-1, 1e-4, 1e-2, 1e-2, 1e-3, 1e-1]
rbf_com = [1e-1, 1e-3, 1e-2, 1e-2, 1e-3, 1e-1]

x = np.arange(len(pdes))  # the label locations
width = 0.25  # the width of the bars

# Labels for legend
label_rbf_int = "RBF-INT"
label_rbf_pol = "RBF-POL"
label_rbf_com = "RBF-COM"

# Axis labels
xlabel = "PDEs"
ylabel = "log L2"

# Axis ticks
xticks = x
yticks = [1e-4, 1e-3, 1e-2, 1e-1]

# Axis tick labels
xticklabels = pdes
yticklabels = ["1e-4", "1e-3", "1e-2", "1e-1"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width, rbf_int, width, label=label_rbf_int, color="#3c0f64")
rects2 = ax.bar(x, rbf_pol, width, label=label_rbf_pol, color="#ae4256")
rects3 = ax.bar(x + width, rbf_com, width, label=label_rbf_com, color="#e47f37")

ax.set_ylabel(ylabel)
ax.set_yscale("log")
ax.set_xlabel(xlabel)
ax.set_xticks(xticks)
ax.set_xticklabels(xticklabels)

# Set custom y-ticks on the log scale and their labels
ax.set_yticks(yticks)
ax.set_yticklabels(yticklabels)

ax.legend(ncol=3, loc="upper center", bbox_to_anchor=(0.5, 1.1), frameon=False)

ax.tick_params(axis="both", which="both", length=0)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("bar_29.pdf", bbox_inches="tight")
