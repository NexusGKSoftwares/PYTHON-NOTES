# Matplotlib Introduction
import numpy as np

# 1. Creating NumPy Arrays
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# 2. Array Operations
arr = arr + 5
print(arr)

# 3. Multi-Dimensional Arrays
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)

# 4. Shape and Reshape
print("Shape:", matrix.shape)
reshaped = matrix.reshape(3, 2)
print(reshaped)

# 5. Array Indexing
print("Element at (0, 1):", matrix[0, 1])

# 6. Slicing Arrays
print("First row:", matrix[0, :])

# 7. Boolean Indexing
bool_arr = matrix > 3
print("Elements greater than 3:", matrix[bool_arr])

# 8. Statistical Functions
mean_value = np.mean(matrix)
print("Mean:", mean_value)

# 9. Summing Elements
total_sum = np.sum(matrix)
print("Sum:", total_sum)

# 10. Maximum and Minimum
max_value = np.max(matrix)
min_value = np.min(matrix)
print("Max:", max_value, "Min:", min_value)

# 11. Dot Product
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
dot_product = np.dot(a, b)
print("Dot Product:", dot_product)

# 12. Concatenating Arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
concat_arr = np.concatenate((arr1, arr2))
print("Concatenated Array:", concat_arr)

# 13. Splitting Arrays
split_arr = np.split(concat_arr, 2)
print("Split Arrays:", split_arr)

# 14. Random Number Generation
random_arr = np.random.rand(5)
print("Random Array:", random_arr)

# 15. Normal Distribution
normal_dist = np.random.normal(0, 1, 1000)
print("Normal Distribution Sample:", normal_dist)

# 16. Linear Space
lin_space = np.linspace(0, 10, 5)
print("Linear Space:", lin_space)

# 17. Matrix Operations
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
matrix_product = np.matmul(matrix1, matrix2)
print("Matrix Product:\n", matrix_product)

# 18. Inverse of a Matrix
inverse_matrix = np.linalg.inv(matrix1)
print("Inverse of Matrix:\n", inverse_matrix)

# 19. Saving Arrays to File
np.save('array.npy', arr)

# 20. Loading Arrays from File
loaded_arr = np.load('array.npy')
print("Loaded Array:", loaded_arr)
