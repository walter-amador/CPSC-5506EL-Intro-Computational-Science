import numpy as np
import matplotlib.pyplot as plt

omega = 20
epsilon = 0.1
x = np.linspace(-2, 2, 200)

y = x**2
y_noise = y + epsilon * np.cos(x * omega)

plt.figure(figsize=(10,5))

plt.subplot(1, 2, 1)
plt.plot(x, y, "-b", label="x^2")
plt.plot(x, y_noise, "-r", label="Noisy x^2")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("x^2 vs. Noisy x^2")

y_prime = 2 * x
y_prime_noise = y_prime + epsilon * omega * - np.sin(x * omega)

plt.subplot(1, 2, 2)
plt.plot(x, y_prime, "-b", label="Derivative of x^2")
plt.plot(x, y_prime_noise, "-r", label="Noisy Derivative of x^2")
plt.xlabel("x")
plt.ylabel("y'")
plt.legend()
plt.title("Derivative of x^2 vs. Noisy Derivative of x^2")

plt.tight_layout()
plt.show()
