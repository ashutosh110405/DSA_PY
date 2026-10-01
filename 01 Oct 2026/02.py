"""
2. Find the smallest and Largest Element: Write a program to accept N integers into an array and find and display the largest element,
second largest element, smallest element, second smallest element present in the array.
"""

#without using sort function, smallest code

n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    arr.append(int(input("Enter element: ")))

# 1. Find Smallest and Largest
small = largest = arr[0]
for x in arr:
    if x < small:
        small = x
    if x > largest:
        largest = x

# 2. Find Second Smallest and Second Largest
s_small = largest
s_largest = small
for x in arr:
    if x < s_small and x != small:
        s_small = x
    if x > s_largest and x != largest:
        s_largest = x

print("Smallest =", small)
print("Second Smallest =", s_small)
print("Largest =", largest)
print("Second Largest =", s_largest)