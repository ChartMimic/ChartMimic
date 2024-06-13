import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)



# ===================
# Part 2: Data Preparation
# ===================
def gaussian_mixture(x, n=6):
    """Return a random mixture of *n* Gaussians, evaluated at positions *x*."""

    def add_random_gaussian(a):
        amplitude = 1 / (0.1 + np.random.random())
        dx = x[-1] - x[0]
        x0 = (2 * np.random.random() - 0.5) * dx
        z = 5 / (0.1 + np.random.random()) / dx
        a += amplitude * np.exp(-((z * (x - x0)) ** 2))

    a = np.zeros_like(x)
    for j in range(n):
        add_random_gaussian(a)
    return a


x = np.linspace(0, 200, 201)
ys = [gaussian_mixture(x) for _ in range(6)]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, ax = plt.subplots(figsize=(6, 5))
ax.stackplot(x, ys, baseline="wiggle")

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('HR_17.pdf', bbox_inches='tight')
