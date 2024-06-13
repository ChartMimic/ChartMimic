import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

from matplotlib import cm
from matplotlib.image import NonUniformImage

# ===================
# Part 2: Data Preparation
# ===================
interp = "nearest"
# Linear x array for cell centers:
x = np.linspace(0, 5, 9)

# Highly nonlinear x array:
x2 = np.sin(x * np.pi / 5)

y = np.linspace(0, 5, 9)

z = np.abs(np.cos(x[np.newaxis, :] + y[:, np.newaxis]))
suptitle="Transformed NonUniformImage"
xlim=[[-5, 5], [-5, 5], [-5, 5], [-5, 5]]
ylim=[[0, 10], [0, 10], [0, 10], [0, 10]]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, axs = plt.subplots(nrows=2, ncols=2, layout="constrained", figsize=(8, 6))
fig.suptitle(suptitle, fontsize="large")
ax = axs[0, 0]
im = NonUniformImage(ax, interpolation=interp, extent=(xlim[0][0], xlim[0][1], ylim[0][0], ylim[1][0]), cmap=cm.magma)
im.set_data(x, y, z)
ax.add_image(im)
ax.set_xlim(xlim[0])
ax.set_ylim(ylim[0])
ax.set_title(interp)

ax = axs[0, 1]
im = NonUniformImage(ax, interpolation=interp, extent=(xlim[1][0],xlim[1][1], ylim[0][0], ylim[1][0]), cmap=cm.magma)
im.set_data(x2, y, z)
ax.add_image(im)
ax.set_xlim(xlim[1])
ax.set_ylim(ylim[1])
ax.set_title(interp)

interp = "bilinear"

ax = axs[1, 0]
im = NonUniformImage(ax, interpolation=interp, extent=(xlim[2][0],xlim[2][1],ylim[2][0],ylim[2][1]), cmap=cm.magma)
im.set_data(x, y, z)
ax.add_image(im)
ax.set_xlim(xlim[2])
ax.set_ylim(ylim[2])
ax.set_title(interp)

ax = axs[1, 1]
im = NonUniformImage(ax, interpolation=interp, extent=(xlim[3][0],xlim[3][1],ylim[3][0],ylim[3][1]), cmap=cm.magma)
im.set_data(x2, y, z)
ax.add_image(im)
ax.set_xlim(xlim[3])
ax.set_ylim(ylim[3])
ax.set_title(interp)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('HR_25.pdf', bbox_inches='tight')
