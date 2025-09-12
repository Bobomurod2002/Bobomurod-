import numpy as np

# 1. Convert List to 1D Array
lst = [12.23, 13.32, 100, 36.32]
arr = np.array(lst)
print("Original List:", lst)
print("One-dimensional NumPy array:", arr)

# 2. Create 3x3 Matrix (2–10)
matrix = np.arange(2, 11).reshape(3, 3)
print("\n3x3 matrix with values from 2 to 10:\n", matrix)

# 3. Null Vector (10) & Update Sixth Value
z = np.zeros(10)
print("\nNull vector:", z)
z[6] = 11   # 6-chi indeks emas, 7-elementni yangilayapmiz
print("Update sixth value to 11:", z)

# 4. Array from 12 to 38
arr2 = np.arange(12, 38)
print("\nArray with values ranging from 12 to 38:\n", arr2)

# 5. Convert Array to Float Type
arr3 = np.array([1, 2, 3, 4])
print("\nOriginal array:", arr3)
print("Array converted to float:", arr3.astype(float))

# 6. Celsius to Fahrenheit Conversion
celsius = np.array([0, 12, 45.21, 34, 99.91, 0])
fahrenheit = celsius * 9/5 + 32
print("\nValues in Celsius degrees:", celsius)
print("Values in Fahrenheit degrees:", fahrenheit)

# 7. Append Values to Array
arr4 = np.array([10, 20, 30])
print("\nOriginal array:", arr4)
arr4_appended = np.append(arr4, [40, 50, 60, 70, 80, 90])
print("After append values to the end of the array:", arr4_appended)

# 8. Array Statistical Functions
rand_arr = np.random.rand(10)
print("\nRandom array:", rand_arr)
print("Mean:", np.mean(rand_arr))
print("Median:", np.median(rand_arr))
print("Standard Deviation:", np.std(rand_arr))

# 9. Find min and max
arr5 = np.random.rand(10, 10)
print("\n10x10 random array min:", np.min(arr5))
print("10x10 random array max:", np.max(arr5))

# 10. 3x3x3 random array
arr6 = np.random.rand(3, 3, 3)
print("\n3x3x3 random array:\n", arr6)
