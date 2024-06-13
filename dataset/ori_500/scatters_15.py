# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data for the plots
names = ["Self-refine", "CoT(maj@1)", "CoT(maj@5)", "SPP", "DefInt", "ToT", "MAD+judge"]
x1 = [45, 20, 10, 15, 10, 30, 35]
y1 = [62, 64, 66, 68, 65, 66, 68]
colors1 = ["green", "blue", "orange", "purple", "pink", "red", "brown"]

x2 = [2.5e6, 1e6, 0.5e6, 1.5e6, 0.5e6, 2e6, 2.5e6]
y2 = [62, 64, 66, 68, 62, 66, 68]
colors2 = ["green", "blue", "orange", "purple", "pink", "red", "brown"]

titles = ["Logic Grid Puzzle(Accuracy versus token cost)", "Logic Grid Puzzle(Accuracy versus TFLOPS)"]
xlabels = ["Token cost($)", "TFLOPS"]
ylabels = ["Accuracy(%)", "Accuracy(%)"]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and axes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# First subplot
ax1.scatter(x1, y1, c=colors1)
ax1.set_title(titles[0])
ax1.set_xlabel(xlabels[0])
ax1.set_ylabel(ylabels[0])
ax1.invert_xaxis()  # Invert x-axis
for i, txt in enumerate(names):
    ax1.annotate(txt, (x1[i], y1[i]), xytext=(-10, 5), textcoords="offset points")
ax1.set_xlim([50, 0])
ax1.set_ylim([60, 70])

# Second subplot
ax2.scatter(x2, y2, c=colors2)
ax2.set_title(titles[1])
ax2.set_xlabel(xlabels[1])
ax2.set_ylabel(ylabels[1])
ax2.ticklabel_format(style="sci", axis="x", scilimits=(0, 0))  # Use scientific notation
for i, txt in enumerate(names):
    ax2.annotate(txt, (x2[i], y2[i]), xytext=(-15, 5), textcoords="offset points")
ax2.set_xlim([3e6, 0e6])
ax2.set_ylim([60, 70])

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save plot
plt.tight_layout()
plt.savefig('scatters_15.pdf', bbox_inches='tight')
