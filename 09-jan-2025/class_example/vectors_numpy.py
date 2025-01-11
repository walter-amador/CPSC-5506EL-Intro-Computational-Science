import numpy as np

# Define a vector using NumPy
vector = np.array([1, 2, 3])

# Perform operations
magnitude = np.linalg.norm(vector) # Calculate magnitude
print("Vector magnitude:", magnitude)

scaled_vector = 2 * vector # Scale the vector
print("Scaled vector:", scaled_vector)

# Dot product of two vectors
vector2 = np.array([4, 5, 6])
dot_product = np.dot(vector, vector2)

print("Dot product:", dot_product)
