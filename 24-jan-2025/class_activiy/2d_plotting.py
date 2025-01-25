import numpy as np
import matplotlib.pyplot as plt

# Simple plot
# x = [0, 1, 2, 3]
# y = [0, 1, 4, 9]

# plt.plot(x, y)
# plt.show()

# Make a plot of the function y = x^2 for x in the range [-5, 5]
# x = np.linspace(-5, 5, 100)
# y = x**2

# plt.plot(x, y)
# plt.show()

x = np.linspace(-5, 5, 20)
plt.plot(x, x**2, "ko")
plt.plot(x, x**3, "r*")

plt.title("Plot of y = x^2 and y = x^3")
plt.xlabel("x")
plt.ylabel("y")
plt.show()