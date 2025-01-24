import numpy as np

# a = np.array([
#     [4, 3, -5],
#     [-2, -4, 5],
#     [8, 8, 0]
# ])

# y = np.array([2, 5, -3])

a = np.array([
    [2, 1, -1, 1],
    [3, 4, 2, -1],
    [1, 2, 3, 2],
    [4, 3, 1, 5]
])

y = np.array([1, 18, 22, 5])

## First Method
x1 = np.linalg.solve(a, y)

print(x1)

## Second method

# Inverse of a matrix
a_inv = np.linalg.inv(a)

x2 = np.dot(a_inv, y)

print(x2)