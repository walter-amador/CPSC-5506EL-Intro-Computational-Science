import numpy as np
import matplotlib.pyplot as plt

h=0.1
x = np.arange(0, 2*np.pi, h)
y = np.cos(x)

forward_diff = np.diff(y)/h
backward_diff = np.diff(y)/h

x_forward_diff = x[:-1]

x_backward_diff = x[1:]

exact_solution_forward = -np.sin(x_forward_diff)
exact_solution_backward = -np.sin(x_backward_diff)

plt.figure(figsize=(12, 8))
plt.plot(x_forward_diff, forward_diff, "--k", label='Forward Difference')
plt.plot(x_forward_diff, exact_solution_forward, label='Exact Solution')
plt.plot(x_backward_diff, backward_diff, "--", label='Backward Difference')
plt.plot(x_backward_diff, exact_solution_backward, label='Exact Solution')
plt.legend()
plt.show()

max_error = max(abs(exact_solution_forward - forward_diff))
print(f'Maximum error forward: {max_error}')
max_error = max(abs(exact_solution_backward - backward_diff))
print(f'Maximum error backward: {max_error}')
