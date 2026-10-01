"""
2. Find the smallest and Largest Element: Write a program to accept N integers into an array and find and display the largest element,
second largest element, smallest element, second smallest element present in the array.
"""

#without using sort function, smallest code

n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

small = arr[0]
s_small = arr[0]
largest = arr[0]
s_largest = arr[0]

for i in range(1, n):
    if arr[i] < small:
        s_small = small
        small = arr[i]
    elif arr[i] < s_small and arr[i] != small:
        s_small = arr[i]

    if arr[i] > largest:
        s_largest = largest
        largest = arr[i]
    elif arr[i] > s_largest and arr[i] != largest:
        s_largest = arr[i]

print("Smallest =", small)
print("Second Smallest =", s_small)
print("Largest =", largest)
print("Second Largest =", s_largest)