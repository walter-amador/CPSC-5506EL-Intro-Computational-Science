import numpy as np

# Define the matrices
matrix_2x2 = np.array([
    [4, 7],
    [2, 6]
])

matrix_3x3 = np.array([
    [2, 3, 1],
    [4, 7, 5],
    [6, 2, 8]
])

# Calculate determinant and inverse for 2x2 matrix
det_2x2 = np.linalg.det(matrix_2x2)
inv_2x2 = np.linalg.inv(matrix_2x2)

# Calculate determinant and inverse for 3x3 matrix
det_3x3 = np.linalg.det(matrix_3x3)
inv_3x3 = np.linalg.inv(matrix_3x3)

# Print results
print(matrix_2x2)

print("Determinant:", det_2x2)
print("Inverse:")
print(inv_2x2)

print(matrix_3x3)

print("Determinant:", det_3x3)
print("Inverse:")
print(inv_3x3)