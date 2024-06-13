import numpy as np; np.random.seed(0); np.random.seed(0)

import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data
latitude = np.array([-90.0, -70.0, -50.0, -30.0, -10.0, 10.0, 30.0, 50.0, 70.0, 90.0])
longitude = np.array([-180.0, -140.0, -100.0, -60.0, -20.0, 20.0, 60.0, 100.0, 140.0, 180.0])
Longitude, Latitude = np.meshgrid(longitude, latitude)
Temperature = np.sqrt(Longitude**2 + Latitude**2)

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Contour
fig, ax = plt.subplots(figsize=(6, 6))
cnt = ax.contour(Longitude, Latitude, Temperature, cmap='winter')
ax.clabel(cnt, cnt.levels, inline=True, fontsize=10)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('contour_4.pdf', bbox_inches='tight')
