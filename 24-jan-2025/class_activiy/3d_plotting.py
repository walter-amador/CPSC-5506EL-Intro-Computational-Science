
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# create a 3d surface plot of function z=x^2+y^2 for x and y in the range [-5, 5]

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

fig = plt.figure()
ax = plt.axes(projection="3d")

ax.plot_surface(X, Y, Z, cmap="rainbow")

ax.set_title("Surface plot of z = x^2 + y^2")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

plt.show()