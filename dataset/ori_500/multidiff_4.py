# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)



# ===================
# Part 2: Data Preparation
# ===================
def f(t):
    return np.cos(2 * np.pi * t) * np.exp(-t)


t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)
t3 = np.arange(0.0, 2.0, 0.01)

X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Axes Limits and Labels
ylabel_value_1 = "Energy Consumption (GWh)"
xlabel_value_1 = "Relative Year"

zlim_values = [-1, 1]
xlabel_value_2 = "Relative Year"
ylabel_value_2 = "Relatetive Month"
zlabel_value_2 = "Renewable Energy Ratio (%)"


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set up a figure twice as tall as it is wide
fig = plt.figure(figsize=(8, 10))

# First subplot
ax = fig.add_subplot(2, 1, 1)
ax.plot(t1, f(t1), "bo", t2, f(t2), "k--", markerfacecolor="green")
ax.grid(True)
ax.set_ylabel(ylabel_value_1)
ax.set_xlabel(xlabel_value_1)

# Second subplot
ax = fig.add_subplot(2, 1, 2, projection="3d")
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, linewidth=0, antialiased=False)
ax.set_zlim(zlim_values)
ax.set_xlabel(xlabel_value_2)
ax.set_ylabel(ylabel_value_2)
ax.set_zlabel(zlabel_value_2)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
# Show the plot
plt.savefig('multidiff_4.pdf', bbox_inches='tight')
