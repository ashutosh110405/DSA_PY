"""
6. Remove Duplicate Elements: Write a program to accept N integers into an
array and create a new array containing only the unique elements, removing all duplicate values.
"""
n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

unique_arr = list(set(arr))
print("Original array:", arr)
print("Array with unique elements:", unique_arr)