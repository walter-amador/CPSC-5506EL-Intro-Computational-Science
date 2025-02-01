import numpy as np

f = np.array([10,15,22,35])
d = np.diff(f)

print(f)
print(d)

# remove last element for forward difference to have exact solution
