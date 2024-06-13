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
few_shot_k = np.array([4, 8, 12, 16, 20, 24, 28, 32])
trained_w_few_shot_ex = np.array([83, 88, 90, 92, 93, 94, 94.5, 95])
def_deduce_ex_gen = np.array([90])
error = np.array([1])

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting
fig, ax = plt.subplots(figsize=(6, 4))  # Adjusting figure size to 432x288 pixels

# Trained with Few-Shot Examples
ax.plot(
    few_shot_k,
    trained_w_few_shot_ex,
    marker="o",
    color="blue",
    label="Trained w Few-Shot Ex",
)
ax.fill_between(
    few_shot_k, trained_w_few_shot_ex - 1, trained_w_few_shot_ex + 1, color="#e1eff4"
)

# Default Deduce + Example Generation set the
ax.errorbar(
    few_shot_k[0],
    def_deduce_ex_gen,
    yerr=error,
    fmt="o",
    color="red",
    label="Def Deduce+Ex Gen",
    capsize=3,
)

# Customizing the plot
ax.set_xlabel("Few-Shot K")
ax.set_ylabel("Micro F1")
ax.set_xlim(2, 34)
ax.set_ylim(82, 96)  # Adjusted y-axis limit to match the reference picture
ax.legend(loc="lower right")
ax.grid(True)
ax.set_xticks([4, 8, 12, 16, 20, 24, 28, 32])

# ===================
# Part 4: Saving Output
# ===================
# Show plot
plt.tight_layout()
plt.savefig("CB_18.pdf", bbox_inches="tight")
