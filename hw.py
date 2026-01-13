import numpy as np

arr = np.array([10, 20, 30, 40, 50])
print("Original array:", arr)

print("Addition (+5):", arr + 5)
print("Subtraction (-5):", arr - 5)
print("Multiplication (*2):", arr * 2)
print("Division (/2):", arr / 2)

print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Standard Deviation:", np.std(arr))

print("First element:", arr[0])
print("Last element:", arr[-1])
print("Slice (index 1 to 3):", arr[1:4])

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr2)
print("Reshaped to 3x2:\n", arr2.reshape(3, 2))

print("Elements greater than 25:", arr[arr > 25])

print("Sorted array:", np.sort(arr))

print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data type:", arr.dtype)
