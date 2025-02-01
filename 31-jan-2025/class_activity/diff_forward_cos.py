import numpy as np
import matplotlib.pyplot as plt

h=0.1
x = np.arange(0, 2*np.pi, h)
y = np.cos(x)

forward_diff = np.diff(y)/h

x_diff = x[:-1]

exact_solution = -np.sin(x_diff)

plt.figure(figsize=(12, 8))
plt.plot(x_diff, forward_diff, "--k", label='Forward Difference')
plt.plot(x_diff, exact_solution, label='Exact Solution')
plt.legend()
plt.show()

max_error = max(abs(exact_solution - forward_diff))
print(f'Maximum error: {max_error}')
