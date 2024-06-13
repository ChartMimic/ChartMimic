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
roles = ["Werewolf", "Seer", "Witch", "Hunter", "Villager"]
duration_means = [84.97, 102.67, 67.17, 78.22, 85.17]
duration_errors = [15, 20, 10, 15, 10]
tokens_means = [449.33, 780.67, 547.39, 612.99, 618.52]
tokens_errors = [100, 150, 80, 100, 90]

ylabel1 = "Duration (s)"
xlabel1 = "(a) Speak duration of roles"
ylabel2 = "Tokens"
xlabel2 = "(b) Speak tokens of roles"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create subplots
fig, (ax1, ax2) = plt.subplots(
    1, 2, figsize=(10, 4)
)  # Adjusted for the given dimensions
colors = ["#acd9bb", "#83c3c7", "#5da2c7", "#3a77b0", "#224e8d"]

# Speak duration of roles
ax1.bar(roles, duration_means, yerr=duration_errors, color=colors, capsize=5)
ax1.set_ylabel(ylabel1)
ax1.set_xlabel(xlabel1)
for i, v in enumerate(duration_means):
    ax1.text(i, v + duration_errors[i] + 2, str(v), ha="center", va="bottom")
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)
ax1.yaxis.grid(True)
ax1.set_axisbelow(True)

# Speak tokens of roles
ax2.bar(roles, tokens_means, yerr=tokens_errors, color=colors, capsize=5)
ax2.set_ylabel(ylabel2)
ax2.set_xlabel(xlabel2)
for i, v in enumerate(tokens_means):
    ax2.text(i, v + tokens_errors[i] + 20, str(v), ha="center", va="bottom")

ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)
ax2.yaxis.grid(True)
ax2.set_axisbelow(True)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the figure
plt.tight_layout()
plt.savefig("errorbar_4.pdf", bbox_inches="tight")
