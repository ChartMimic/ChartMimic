# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

from matplotlib import cm
from matplotlib.image import NonUniformImage

# ===================
# Part 2: Data Preparation
# ===================
interp = "nearest"

# Linear x array for cell centers:
x = np.linspace(-4, 4, 9)

# Highly nonlinear x array:
x2 = x**3

y = np.linspace(-4, 4, 9)

z = np.sqrt(x[np.newaxis, :] ** 2 + y[:, np.newaxis] ** 2)
suptitle="NonUniformImage class"
xlim=[[-4, 4], [-64, 64], [-4, 4], [-64, 64]]
ylim=[[-4, 4], [-4, 4], [-4, 4], [-4, 4]]
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
