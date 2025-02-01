import numpy as np
import matplotlib.pyplot as plt

h=0.01

x = np.arange(0, 2*np.pi, h)

omega = 100
epsilon = 0.01

y = np.cos(x)
y_noise = y + epsilon*np.sin(omega*x)

plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(x, y_noise, "r-", label="cos(x) + noise")
plt.plot(x, y, "b-", label="cos(x)")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Noisy vs. True cos(x)")

y_prime = -np.sin(x)
y_prime_noise = y_prime + epsilon*omega*np.cos(omega*x)

plt.subplot(1, 2, 2)
plt.plot(x, y_prime_noise, "r-", label="Derivative cos(x) + noise")
plt.plot(x, y_prime, "b-", label="Derivative cos(x)")

plt.xlabel("x")
plt.ylabel("y'")
plt.legend()
plt.title("Noisy vs. True Derivative cos(x)")

plt.tight_layout()
plt.show()
