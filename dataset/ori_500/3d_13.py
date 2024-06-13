# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================

yticklabels = ["Public Schools", "Private Schools"]
years = np.array([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019])
private = np.array([0.79, 0.53, 0.57, 0.93, 0.07, 0.09, 0.02, 0.83, 0.78, 0.87])
public = np.array([0.17, 0.43, 0.39, 0.03, 0.91, 0.89, 0.96, 0.14, 0.19, 0.10])
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(projection="3d")

ax.bar(years, private, zs=0, zdir="y", color="sandybrown", alpha=0.8)
ax.bar(years, public, zs=1, zdir="y", color="skyblue", alpha=0.8)

ax.set_xlabel("Year")
ax.set_ylabel("Type")
ax.set_zlabel("Student to Teacher Ratio")

ax.set_yticks([0, 1])
ax.set_yticklabels(yticklabels)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("3d_13.pdf", bbox_inches="tight")
