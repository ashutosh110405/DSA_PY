"""
2. Find the smallest and Largest Element: Write a program to accept N integers into an array and find and display the largest element,
second largest element, smallest element, second smallest element present in the array.
"""

n = int(input("Enter the number of elements: "))
arr = []

#give short code
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

arr.sort()

print("Smallest = ", arr[0])
print("Second Smallest = ",arr[1])
print("Largest = ", arr[n-1])
print("Second Largest = ", arr[n-2])