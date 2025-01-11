import numpy as np
from sympy import Matrix, pretty_print

matrix = np.array([
    [2, 3, 1],
    [4, 7, 5],
    [6, 2, 8]
])

sympy_matrix = Matrix(matrix)
pretty_print(sympy_matrix)

# Determinant
determinant = np.linalg.det(matrix)
print(f"Determinant: {determinant}")

# Inverse
if determinant != 0:
    inverse = np.linalg.inv(matrix)
    print("Inverse:")
    pretty_print(inverse)
else:
    print("Inverse: Not defined (determinant is zero)")

# Calculate the sum
matrix_sum = np.sum(matrix)
print(f"Sum: {matrix_sum}")
