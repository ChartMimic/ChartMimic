# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# ===================
# Part 2: Data Preparation
# ===================
# Set the figure size to match the original image's dimensions
plt.figure(figsize=(8, 6))

# Create a Venn diagram
venn = venn2(subsets=(24, 8, 45), set_labels=("CigaR", "ChatRepair"))

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Customize the colors and edge styles
venn.get_patch_by_id("10").set_color("pink")
venn.get_patch_by_id("10").set_edgecolor("black")
venn.get_patch_by_id("10").set_linestyle("dashed")
venn.get_patch_by_id("01").set_color("lightgreen")
venn.get_patch_by_id("01").set_edgecolor("black")
venn.get_patch_by_id("01").set_linestyle("dashed")
venn.get_patch_by_id("11").set_color("sandybrown")

# Remove axis
plt.axis("off")

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("HR_13.pdf", bbox_inches="tight")
